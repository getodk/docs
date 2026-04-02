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
        subgraph Data[Entity Lists]
            direction LR
            E[(enumerators)]
            H[(households)]
            M[(members)]
        end

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

The baseline form needs to:

* get the enumerator's identity
* show the enumerator the households they're responsible for
* help the enumerator navigate to the next household to visit
* ask the household head for consent and end if consent is not given
* ask baseline household questions
* get listing of household members and ask them baseline questions

See `the final form <https://docs.google.com/spreadsheets/d/1Qs9UCRshSxkEAp7EPDxXsFXFlmH0YAo-P-iKxItzPYs>`_
