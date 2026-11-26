.. spelling:word-list::
  hh

Entities tutorial: household survey
===================================

Household-based surveys are one of the most common patterns in field data collection, spanning population studies, public health, agriculture, education, and humanitarian response. Across these domains, the same core structure is found: there's a household or other parent unit, the people or items linked to it, and the operational forms and supporting data needed to carry out the work.

This tutorial shows how to leverage Entities to support a household survey at scale.

In this workflow, households have already been identified, sampled, and assigned to enumerators. We focus on enumerators visiting each of their assigned households to capture baseline data and build member rosters. They will then need to follow up both with the households and selected individuals over time:

.. mermaid::
    :align: center

    flowchart LR
        A@{ shape: notch-rect, label: "Register\nhouseholds" }
        B[Assign enumerators outside ODK]
        C@{ shape: notch-rect, label: "Build roster\nand baseline" }
        D@{ shape: notch-rect, label: "Household\nfollow-up" }
        E@{ shape: notch-rect, label: "Member\nfollow-up" }

        A --> B --> C --> D
        C --> E

        style C stroke-width:3px

Goals
-----

* Use existing data to drive a workflow
* Use Entities to assign work and keep track of its completion
* Create or update multiple Entities with a single submission
* Experience the design process for an Entity-driven workflow

Prerequisites
-------------

This tutorial requires Central v2025.4.4 and Collect v2026.1 or later. It assumes familiarity with :doc:`XLSForm <xlsform>` and :doc:`ODK Entities <entities-intro>`.

You will need administrator access to an ODK Central project. We recommend using a new project just for this tutorial. You can also use a project with other test forms, but be aware that you may end up with conflicts with existing form or Entity List names.

If needed, you can add a prefix or suffix to the names used in this tutorial. If you do so, be sure to apply it consistently everywhere needed, including in expressions to read from Entity Lists.

Designing the Entity model
--------------------------

Because this workflow involves repeat encounters with the same households over time, it's helpful to represent those households as Entities so that their current status can be accessed and updated by forms. This enables enumerators to immediately see their progress as they visit households and automatically access data they previously captured in follow-up forms, even while offline. The ``households`` Entity List stores this household data. You can think of it as a data table, where each row is a single ``household`` Entity.

A key part of workflows that divide work across data collectors is making sure the full work gets done while avoiding duplicate effort. In this example, that is done with an ``enumerators`` Entity List. Each Entity in the list represents one person responsible for a set of households. The assignments are represented by a link from each ``household`` Entity to the ``enumerator`` it is assigned to. A single ``enumerator`` is generally assigned to multiple ``households``.

In our workflow, enumerators will also need to follow up with individual members, so it is helpful to represent those members separately in a ``members`` Entity List with a property linking them to the ``household`` they belong to.

When deciding what to store in Entity Lists, focus on what needs to be available during ongoing fieldwork. Form submissions capture raw data and are typically used later for analysis, while Entities store the current state of real-world things that need to be accessed and updated over time.

If you only needed follow-up from households and not individual members, you might choose to keep member data only in submissions and access it at analysis time. Similarly, if you only needed members' names, you could join them with a character like ``|`` and store them in a single property in the ``households`` Entity List for quick reference.

However, if you need multiple pieces of information about members to be available and updated during follow-up, it is better to represent them in a separate ``members`` Entity List.

Here are the Entity Lists and relationships we will use to support our workflow:

.. mermaid::
    :align: center

    flowchart LR
        E[(enumerators)]
        H[(households)]
        M[(members)]

        E -.- |1 → many| H
        H -.- |1 → many | M

Setting up the enumerators and households lists
------------------------------------------------

In workflows where only a sampled subset of households need to be visited, it's generally beneficial to carry out initial household discovery as a separate step. This could be done as part of a different project such as a local census or it could be carried out using an ODK form that does not automatically create Entities. Then, submission data can be cleaned as needed and used as a basis for sampling and assigning to enumerators.

For this tutorial, we have prepared two files with sample data. Start by downloading these:

* `enumerators.csv <https://docs.google.com/spreadsheets/d/1Liz9nzDDIoH3d901KTl-0uskeYYJ1reFo1xbvuQpfyM/export?format=csv>`_
* `households.csv <https://docs.google.com/spreadsheets/d/13wK6LN_lu7lAXb_oojsDL0r8bkCCtKBFjZo16U2ioR8/export?format=csv>`_

.. note::

  The names, places, and phone numbers in these files may look somewhat like real ones in Tanzania but they are entirely made up. Even the administrative areas are not completely correct.

In ODK Central, open your project and go to the :guilabel:`Entity Lists` tab to create and configure the Entity Lists so you can populate them with the data from the CSVs.

Create the ``enumerators`` Entity List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Click :guilabel:`New Entity List`.
* Enter ``enumerators`` as the name.
* The declared properties must match columns from the CSV. Add the following properties:

  * ``code`` (unique code for each enumerator)
* Upload the ``enumerators.csv`` file.

Each row in the file becomes an Entity in the ``enumerators`` list. Note that Central does not validate or guarantee uniqueness or property values so you are responsible for choosing naming conventions that ensure uniqueness.

For the sample data we have generated, we used the following structure for enumerator codes: ``region code - first 4 letters of first name - first letter of last name``. For our 5 sample enumerators, this produces unique codes. When building your own household workflow, use a convention appropriate for your context or pre-existing values like employee ids.

Create the ``households`` Entity List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Click :guilabel:`New Entity List`.
* Enter ``households`` as the name.
* The declared properties must match columns from the CSV. Add the following properties:

  * ``hhid`` (unique code)
  * ``geometry`` (geopoint representing the household location)
  * ``enumerator`` (code of the assigned enumerator)
  * ``admin1`` (region)
  * ``admin2`` (district)
  * ``admin3`` (ward)
  * ``hh_head_name`` (full name of household head)
  * ``hh_head_phone`` (phone number of household head)
* Upload the ``households.csv`` file.

Each row in the file becomes an Entity in the ``households`` list.

Notice that the ``enumerator`` property stores the code of the assigned enumerator, linking each Entity in the ``households`` list to an Entity in the ``enumerators`` list. Because the relationship between enumerators and households is established outside of ODK, we use our own identifiers for linking (enumerators' ``code``) instead of Central's system-assigned IDs, which are not available when preparing the data.

In the next section, we will create a form to get basic information about all members of the household as well as some baseline data.

Building the baseline form
--------------------------

We will go through each part of the baseline workflow below. You can challenge yourself to build the form with the provided information or follow along with `the complete form <https://docs.google.com/spreadsheets/d/1Qs9UCRshSxkEAp7EPDxXsFXFlmH0YAo-P-iKxItzPYs>`_

The baseline form needs to:

* get the enumerator's identity
* show the enumerator the households they're responsible for
* help the enumerator select and navigate to the next household
* ask the household head for consent and end if consent is not given
* ask baseline household questions
* get a listing of household members and ask each baseline questions

Household status
~~~~~~~~~~~~~~~~~

The properties of the ``households`` list so far represent identifying information about each household. These properties may change (for example, if a family moves or a phone number changes), but such updates are expected to be rare.

In an Entity-based workflow, we often also have properties that represent the status of Entities within the context of the current project. For example, you can use properties to track completion of each step of a multi-step workflow. 

In this workflow, the baseline form will be responsible for two steps that need to be tracked: getting consent and completing the baseline questionnaire. These need to be tracked to avoid re-visiting households that either have not consented or that have already completed the baseline interview.

To track consent and baseline completion, we will add two properties to the ``household`` list: ``consent`` and ``baseline_date``. We won't set these in our form until later but it's often helpful to think through what state needs to be saved before designing the form because often we need to access this kind of state early in the workflow. In this case, we will use these properties to determine the ``households`` that can be selected.

The Entity model is very flexible so you can decide how to represent status information in a way that is most comfortable to you. For example, you could replace the ``consent`` and ``baseline_date`` properties with a single ``baseline_status`` property with values ``complete`` and ``no_consent`` if you don't plan to use the date of baseline completion.

Identifying the enumerator
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this workflow, we trust enumerators and we want them to be able to easily take on each other's households if assignments need to change while offline. For example, this could happen if one enumerator has finished all their assigned households or has to take a day off. For these reasons, we can have enumerators identify themselves by selecting their name from the ``enumerators`` list. In a lower-trust context where it's important to know with certainty who completed each task, we could have them enter in a password instead.

.. rubric:: XLSForm

.. csv-table:: survey
   :header: type, name, label, required, appearance, default, parameters

   select_one_from_file enumerators.csv, enumerator, Enumerator, yes, minimal, last-saved#enumerator, value=code

We've applied a few customizations to this select to improve the enumerator experience:

* The ``minimal`` appearance means enumerators only have to see the full list of names if they tap into the field. This is helpful if there's a long list of enumerators.
* The ``default`` value of ``last-saved#enumerator`` automatically fills out the enumerator value based on what was selected last. This is helpful in a context where each device is generally used by a single user.
* Using ``value=code`` in the ``parameters`` column means the ``code`` for the selected enumerator will be saved rather than the system ID.

Selecting the next household to visit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once an enumerator has been identified, we show them the households assigned to them so they can select the next one to visit. Because households are identifiable by their location and that enumerators need to travel to those locations, we will show assignments on a map.

.. rubric:: XLSform

.. csv-table:: survey
  :header: type, name, label, required, appearance, choice_filter

  select_one_from_file households.csv, hh, Next household, yes, map, enumerator = ${enumerator} and baseline_date='' and consent != 'no'

Because we have applied the ``map`` appearance to this select, each Entity in the ``households`` list will be displayed on a map using the value of their ``geometry`` property.

The expression in the ``choice_filter`` column ensures that enumerators will only see households assigned to them that they have not visited yet:

* ``enumerator = ${enumerator}`` means only households whose ``enumerator`` property matches the selected enumerator's code will be included.
* ``baseline_date=''`` means only ``households`` with a blank ``baseline_date`` property will be included.
* ``consent != 'no'`` means only ``households`` with a value other than ``no`` for the ``consent`` property will be included.

These expressions are joined with ``and`` so an Entity from the ``households`` list will only be included if it meets all three conditions.

Confirming the household details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After an Entity is selected, it's often helpful to show information about it so that enumerators can confirm that they have made the right selection. This requires writing expressions to access Entity properties. In our form, they look like:

``instance('households')/root/item[name=${hh}]/property``

* ``instance('households')`` selects the ``households`` Entity list.
* ``/root/item`` selects each item in the list.
* ``[name=${hh}]`` filters the ``items`` by system ID to find one that matches the value of the ``hh`` question set when selecting a household from the map. The ``name`` property stores the system-generated Entity ID. When selecting a household from the map, ``${hh}`` is set to this ID, which is why we match on ``name`` here.
* ``/property`` is replaced with the name of the property you want to get.

For example, ``instance('households')/root/item[name=${hh}]/hh_head_name`` is the full expression to get the name of the household head for the selected household.

You can either save these values to ``calculate`` fields to reuse them later in the form or write them directly in a ``note`` label to only display them. In `the complete form <https://docs.google.com/spreadsheets/d/1Qs9UCRshSxkEAp7EPDxXsFXFlmH0YAo-P-iKxItzPYs>`_, we have done both depending on whether the values are used later in the form or not. Also consider that values stored in calculates will be available when you analyze submission data whereas values shown directly in notes will not.

Note that we display the household phone number using ``Phone: [${phone}](tel:${phone})``. This will display the phone number and also make it clickable. Clicking the phone number will launch the default call application with the number ready to call.


Asking for consent
~~~~~~~~~~~~~~~~~~

Once an enumerator selects and goes to a household, they will need to introduce the survey and request consent. Requesting consent typically involves a yes or no question that then determines the visibility of the rest of the survey. In this case, we will also store the result of the consent step on the corresponding Entity in the ``households`` list so that we can use consent status in follow-up forms or when this form is used again (see the filtering on the ``households`` list above).

.. rubric:: XLSform

.. csv-table:: survey
  :header: type, name, label, save_to, required, relevant

  select_one yes_no, consent, Intro... ${hh_head} consents?, households#consent, yes
  note, no_consent, "Thank you, please submit",,, ${consent}='no'
	begin_group, survey, Survey,,, ${consent}='yes'

The ``households#consent`` value in the ``save_to`` column ensures that the response is saved to ``consent`` property of the selected household Entity. We use the ``households#`` prefix to specify which Entity List to write to, since this form will also write to other lists.

When we introduce a ``save_to``, we also need to define the target Entity List on the ``entities`` sheet. This will allow us to say whether to create or update Entities and to define an Entity label. In this case, we update existing ``households`` Entities and do not change their label:

.. rubric:: XLSform

.. csv-table:: entities
  :header: list_name, label, entity_id

  households,,${hh}

Asking baseline household questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that household selection and consent are set up, you can ask household-level baseline questions. `The complete form <https://docs.google.com/spreadsheets/d/1Qs9UCRshSxkEAp7EPDxXsFXFlmH0YAo-P-iKxItzPYs>`_ has one as an example but you may have many more.

Typically, not all baseline data needs to be used in follow-up encounters so it does not need to be saved to an Entity. Full analysis can be done using submissions to the baseline form. Any data that does to be available in follow-up encounters can be saved to the households list or to a linked Entity in a baselines list, for example.

Building household member roster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~