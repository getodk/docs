:og:image: https://docs.getodk.org/_static/img/entities-intro.png

**************************
Introduction to Entities
**************************

If you've heard something about ODK Entities and want to better understand whether they're useful for your longitudinal data collection, you're in the right place! We've organized this page as a series of questions that are independent from each other so you can focus on the topics that interest you.

For a quick reference, check out the :doc:`quick reference </entities-quick-reference/>`. If you're someone who learns best by doing, you may prefer to jump straight into the tutorial on :doc:`building a community reporting tool with Entities <tutorial-community-reporting>` and to come back here if you have any questions. If you have a question that we haven't answered, you can `post on the forum <https://forum.getodk.org/c/support/6>`_.

**Topics**

* :ref:`Overview <entities-intro-concepts>`: how Entities fit with ODK concepts like Forms and longitudinal data collection
* :ref:`What's coming <entities-intro-limitations>`: current limitations and plans for the future
* :ref:`Alternatives <entities-intro-alternatives>`: other concepts in ODK you can use and other software to consider
* :ref:`Get started <entities-intro-get-started>`: how to use Entities in your workflow

.. note::

    This document assumes you are using `ODK Cloud <https://getodk.org/#pricing>`_ or an up-to-date :doc:`ODK Central <central-intro>` server. Entities are not yet available in other ODK-based systems.

.. _entities-intro-concepts:

Concepts
========

What are Entities?
------------------

In the ODK context, an "Entity" can be thought of as a "thing". If your project involves things that need to be shared between forms and may change over time, you can represent them as Entities. You can use Entities to represent real things like trees, people, or cities. You can also represent more abstract things like tree visits, malaria cases, or city ratings as Entities.

Entities are organized in Entity Lists that group together Entities of the same type. You can think of Entity Lists as spreadsheets or databases that are shared across forms. Forms can create, read, and update Entities. You can also think of Entities as the nouns (trees) and the forms as the verbs (Register a tree).

ODK has historically been form-based: every workflow starts by opening a blank form and filling it out. We are now working towards providing an Entity-based option in which workflows start by selecting an Entity. Currently, you can have each of your forms start with a question that lets users select an Entity from a list. In the future, you'll have the option to first select an Entity and then see what forms, if any, apply to that Entity.

.. image:: _static/img/entities-intro.png

Can you show me how it works?
-----------------------------

Sure! The video below shows an Entities-powered example of a bed net distribution project where you register households and then return to the households with children to distribute bed nets.

..  youtube:: 3afegV6-4wI
   :width: 100%

How are Entities and forms related?
-----------------------------------

Entities and forms exist at the same level in projects. Forms define actions that can be taken in your project and Entities store data that can be accessed as part of taking those actions. A form definition can attach and access many different Entity Lists but currently, a form submission can only create or update a single Entity. Eventually, it will be possible to create or update multiple Entities from a single submission. 

Once a submission has been processed and it creates or updates an Entity, the submission and the resulting Entity become independent. That means that if you edit the submission, those changes are not automatically applied to the related Entity. You can choose to apply them manually if applicable.

Should I use Entities?
----------------------

Entities are an optional add-on to ODK. There are many users of ODK who don't need to use Entities because their data collection is done at a single moment in time and doesn't use any previously collected data.

Any workflow that involves multiple steps over time has the potential to benefit from Entities. If you find yourself wishing you could flow data from one form to another or send data back to devices, you likely want to use Entities. Common examples include site inspections, studies that involve linking baseline and follow-up visits, and case management.

Entities can also be helpful for sharing data that rarely changes between multiple forms. For example, if all your forms need to use a country's districts, you can represent those once in an Entity List and share that list between the forms. This means if the districts do change, you can make the necessary updates in one place and know that all related forms will get the update.

Entities are very powerful and it can be tempting to look for ways to use them in every project. This power comes at a cost of greater complexity and more potential for error, though. When you use Entities, you have to consider the possibility that some users may be offline for some time, possibly resulting in conflicts. You also have to consider that Entities themselves will change over time and affect form design logic in ways you may not expect.

How are Entities and longitudinal data collection related?
----------------------------------------------------------

Longitudinal studies involve following one thing over time. Because Entities represent things that are shared between forms, they can be used to represent longitudinal study subjects. Those Entities can be used to make sure each subject is only registered once, to track and verify the number of data capture events related to one subject, and to link encounters of the same subject at analysis time.

When designing a longitudinal study supported by Entities, you will likely have an Entity List with a name like ``participants`` or ``subjects``. The Entities model is flexible so you can choose exactly the structure that best supports your desired workflow and reflects the terminology that's used in your domain.

How are Entities and case management related?
---------------------------------------------

A "case" is a term used in many domains to mean an instance of something. A case is opened when a specific condition is detected, may go through multiple steps across a broad range of caseworkers while the case condition is still true, and then is closed when the case condition is no longer true. For example:

* Medicine: healthcare workers may manage pregnancy cases

* Utilities: a electricity provider may get multiple case reports of households without electricity

* Crisis response: a humanitarian team may be involved in child protection cases or asylum cases

.. seealso::
    The :doc:`Community reporting tutorial <tutorial-community-reporting>` implements a simple case management workflow in which anyone can open a case (called "problem" in the tutorial) and specific individuals can resolve them.

You can use Entities to support managing pregnancies, power outages, legal cases, and other case management tasks. And, you can use Entity Lists with terminology that matches your specific workflow like ``risky_pregnancies``, ``power_outages``, and ``vulnerable_children``. 

We use the word "entities" because it's more neutral. Even in domains where case management is common, there is often a need to support other kinds of workflows within the same tool and it can be awkward to use the word "case" in those contexts, especially when referencing real things like trees, people, or cities.

Why can't I just flow data from one form to another form?
---------------------------------------------------------

We have added the Entity concept instead of letting data flow directly between forms because it adds more flexibility. In particular, it's common to have a workflow centered around a thing with a status that determines what needs to be done with that thing. Having an Entity representation with one or more properties that represent its status means it's significantly easier to have multiple forms that can update that status and to show a list of Entities with the latest status information.

In many contexts, the information that needs to be shared between forms is minimal and sometimes as little as an ID and label are enough. Sometimes the subjects of a workflow are known ahead of time, either from a prior ODK form or some other system. Entities make both of these scenarios straightforward to represent.

If your workflow requires accessing all captured data about an Entity, directly flowing data between forms would likely have worked well. You can achieve something similar with Entities by creating an Entity List that represents encounters with the Entity. 

For example, let's say that you have trees that you want to evaluate over time. You could have a ``trees`` Entity List that includes fixed properties of the trees: their location, their species, etc. Then you could have a second Entity List called ``tree_measurements`` that includes a property that represents a link back to a ``tree`` Entity as well as any measurements made during a new encounter.

.. _entities-intro-limitations:

Limitations
===========

.. seealso::
  :ref:`Entities roadmap and limitations <central-entities-roadmap>`

I filled out a registration form and don't immediately see my Entity in follow-up forms, why?
---------------------------------------------------------------------------------------------

If you are using a version of Central older than 2024.3.0, Enketo web forms, or a version of Collect older than 2024.3.0, Entities are not created or updated offline. This means that in order for a submission to create or update an Entity, that submission has to be processed by your server. If you create a new Entity or update an existing one by filling out a form, you won't see that change reflected in follow-up forms until you download the latest update to your Entity List from your server.

If you usually have Internet connectivity, this is unlikely to be very important. Similarly, if your registration and follow-up periods happen at very different times, this limitation is not a problem. But for workflows in which follow-up needs to happen immediately after registration or multiple follow-ups are needed while offline, this limitation is significant. 

I need to assign specific Entities to specific data collectors, how can I represent this?
-----------------------------------------------------------------------------------------

Currently, an entire Entity List is always sent to every device and there is no way to subset the list. This is something that we intend to eventually enable. 

For now, you can limit the Entities that are available from a :ref:`select_one_from_file <select-from-external-dataset>` using a :ref:`choice_filter <cascading-selects>`. This won't limit the amount of data sent to each device but it can significantly reduce the amount of options shown to each user and can help speed up :ref:`lookup expressions <referencing-values-in-datasets>`.

Can I have millions of Entities?
--------------------------------

Yes, but there are two limitations that may make millions of Entities impractical: data transfer and form performance.

Currently, all Entities are sent to every device on every update. Depending on how much data is stored in your Entities and your team's network connection, using millions of Entities may not be practical. To address this limitation, we plan on adding support for archiving Entities, synchronizing only updated Entities, or assigning a subset of Entities to a user.

Choice filters and :ref:`lookup expressions <referencing-values-in-datasets>` are the other limiting factor. Starting in Collect v2024.3 and Central v2024.3, simple and common expressions with ``=``, ``and`` and ``or`` are very fast. Complex expressions in lookups or choice filters (e.g., :doc:`functions <form-operators-functions>` like :func:`substr`) may slow your form if you have more than 50,000 Entities on devices with low amounts of RAM. We regularly review our analytics to look for opportunities for performance improvements.

The number of properties that each Entity has, the size and uniqueness of values saved, and the devices used all affect data transfer and form performance. If you have a form with many Entities that feels slow, we encourage you to post about it on `the forum <https://forum.getodk.org/c/support/6>`_ so that we can recommend approaches that will make it work faster or design improvements to the system.

.. note::
    We do not recommend using `search() <https://xlsform.org/en/#dynamic-selects-from-pre-loaded-data>`_ instead of ``select_one_from_file`` because it does not work with offline Entities and is less flexible. Starting in Collect v2024.3 and Central v2024.3, there is limited performance benefit to ``search()``.

My form captures data on multiple different things, can I create multiple Entities with a single submission?
------------------------------------------------------------------------------------------------------------

Not yet, but this is something we will eventually support.

If you find yourself wanting to create or update multiple Entities of the same type in a repeat, your best option currently is to use multiple submissions of the same form instead of a repeat. You can capture base information in one form and then use a separate form to create each Entity that you currently represent by repeat instances.

If there is a parent-child relationship between the different Entities, you can save the parent's ID to each child. If your versions of Central and Collect support offline Entities, parent Entities will be available to other forms the moment the registration form is finalized. This means the registration form for the child Entities can include a question to select the parent Entity which will establish the link between the two.

Similarly, if you'd like to establish relationships between multiple Entities of different types, you can have a registration form for each type and include a field to represent a link to another Entity.

My Entities have associated media, can I attach files to them?
---------------------------------------------------------------

Not yet, but this is something we will eventually support. If you are interested in possible temporary workarounds, see `this forum thread <https://forum.getodk.org/t/retrieving-dynamic-media-from-entity/47820>`_

.. _entities-intro-alternatives:

Alternatives
============

What's the difference between Entities and CSV form attachments?
----------------------------------------------------------------

From a form design perspective, they are identical. That means you can attach them to forms, look values up in them or build selects on them in the exact same way.

From a server perspective, a CSV form attachment can only be associated with a single form, unlike Entities which can be shared between forms. CSV form attachments are stored as files and if you need to update one row in a CSV attachment, you need to replace the whole file. In contrast, Entities can be updated individually.

You can -- and many users do -- accomplish the same thing as Entities with CSV form attachments and your own automation using the :doc:`Central API <central-api>`. The biggest advantage of Entities over that approach is that you don't need to run your own automation.

I use CSV form attachments for longitudinal data collection, should I use Entities instead?
-------------------------------------------------------------------------------------------

If CSV form attachments are working well for you, you don't need to change anything. In particular, if your workflow involves distinct phases such as annual data collection events, it may be better to analyze and clean baseline data before feeding it into the next phase rather than automatically flowing data with Entities.

If there's a need to periodically update your CSV form attachment, you may want to consider using Entities to save time and reduce the opportunity for mistakes that can come from a manual process such as forgetting to update or attaching the wrong file.

What's the difference between Entities and choice lists?
--------------------------------------------------------

From a form design perspective, they are nearly identical. The only significant difference is that because Entity Lists are defined outside of a form, you need to explicitly attach them to your forms using :ref:`select_*_from_file <select-from-external-dataset>` or :ref:`csv-external <form-datasets-attaching-csv>`. Another difference is that there currently isn't support for media or translations in Entity Lists. Other than that, the way that you look up values in choice lists and Entity Lists using ``instance()`` is identical.

Can ODK now replace more specialized software?
----------------------------------------------

ODK is a flexible data collection platform. Its strength is that it lets you quickly build forms that meet your exact needs. With Entities, you can now think of ODK as an application-building platform. With data defined by your Entity Lists and behavior defined by your forms, you have the freedom to represent only the things that matter to you and to define exactly what actions can be taken on them.

The domain that you work in likely has systems for managing workflows similar to the ones you need to support. This could be a system designed to support a community health worker program, to monitor tree health over time, to track samples in a lab, etc. Those systems typically have some built-in concepts around the data that needs to be collected, the people that might be involved, the status changes that a workflow subject can go through, and so on.

If you have specialized software that supports your domain's workflows, we recommend giving that software a try. If you find that you need the flexibility to define your forms and Entity Lists to exactly match your workflow needs, ODK may be a better fit.

Here are some questions to consider when deciding between using ODK and specialized software:

* Which platform provides the data collection features I need? If you need powerful features like custom logic, offline basemaps, and barcode scanning, ODK has that and more.
* How easy is it for me to support the basic concepts of my workflow? For example, implementing patient transfers between health workers is possible in ODK, but it requires a lot of work.
* Are my workflows mostly data collection or mostly something else? If your workflows are primarily driven by data collection, you'll likely be better served with ODK.

In general, workflows that are focused or short-lived can very easily be represented in ODK and may not benefit from a system made specifically for that purpose. More wide-ranging or long-lived workflows are more likely to benefit from a more structured and specialized system.

That said, in many contexts, workflow needs are so specific that a flexible platform like ODK offers great benefits. Once you have defined your workflow in ODK, the forms you have built can become the standard, specialized way to support others in your domain.

.. _entities-intro-get-started:

Get started
============

How do I use forms to create or update Entities?
------------------------------------------------

Add an ``entities`` sheet to your form. This sheet is used to define how data from this form's submissions should be applied to Entity Lists.

Currently, a single submission can only affect a single Entity in a fixed Entity List. To specify which list to create or update an Entity in, use the ``list_name`` column.

If you're creating Entities, you'll also need to specify an expression that defines the label of each Entity in the ``label`` column. This is very similar to :ref:`the instance_name column <instance-name>` for naming filled forms.

If you're updating Entities, you must add an ``entity_id`` column. In that column, put a reference to a form field that holds the unique id of the Entity you want to update. For example, if you have a select question named ``tree`` that lets the user select a tree from the Entity List, you would put ``${tree}`` in the ``entity_id`` column. You may also specify an expression that defines the label for each Entity in the ``label`` column if you would like the label to change, for example to show an updated status.

Next, specify which form fields should be saved to Entity properties. This is done on the ``survey`` sheet by putting the desired property name in the ``save_to`` column for each form field that you want to save.

.. seealso::
    * :doc:`Community reporting tutorial <tutorial-community-reporting>`
    * :ref:`Build a form that creates Entities <central-entities-registration-forms>`
    * :ref:`Build a form that updates Entities <central-entities-build-update>`

How do I access Entities from my forms?
---------------------------------------

First, attach the Entity List(s) that you want to access Entities from in your form definition using ``select_one_from_file`` or ``csv-external``, as described below. Note that you can attach multiple Entity Lists to a single form via these methods, and they do not need to be listed in the ``entities`` sheet in the XLSForm: only the Entity List in which Entities are created or updated needs to be included in this sheet.

* If you want the user to be able to select an Entity from a list, you can use a :ref:`select_one_from_file <select-from-external-dataset>` question with the name of your Entity List followed by ``.csv``. For example, if your Entity List is named ``trees``, you would create a ``select_one_from_file trees.csv`` question.

  Everything you know about selects and selects from files applies to attached Entity Lists. For example, you can use an Entity property in a :ref:`choice_filter <cascading-selects>` expression to filter down an Entity List.

* If you want to look up Entities using a user-provided value such as a unique ID scanned from a barcode, entered manually, or looked up from another Entity's property, you can attach your Entity List with :ref:`csv-external <form-datasets-attaching-csv>`. For example, if your Entity List is named ``trees``, you would create a form field of type ``csv-external`` with name ``trees``.

You can access a specific Entity's properties using a :ref:`lookup expression <referencing-values-in-datasets>`. If you've used CSV form attachments or looked up values in a choice list before, looking up values in an Entity List works exactly the same way.

.. seealso::
    * :ref:`Looking up values in a list <referencing-values-in-datasets>`
    * :doc:`Community reporting tutorial <tutorial-community-reporting>`
    * :ref:`Build a form that uses Entities <central-entities-follow-up-forms>`

.. _entities-intro-form-fields:

What form fields should I save to my Entities as properties?
------------------------------------------------------------

This will vary a lot project by project. In many cases, a descriptive label clearly identifying individual Entities is enough to meet goals like making sure that no duplicate Entities are created and connecting submissions about the same Entity in analysis.

For more complex workflows, it can be helpful to include a property that represents a status which determines what forms can operate on any given Entity. In some contexts, it may be important to include multiple identifying properties to make sure that the correct Entity is selected. Sometimes it's important to show data collectors a summary of information that was previously captured and so it must all be saved on the Entity.

We recommend thinking carefully about the minimum amount of data that you need to drive your workflow. The less data you save and access, the simpler your form design will be and the less data will need to be transmitted to data collectors. However, there is no enforced limit on number of properties.

Currently, once a property is added to an Entity List, it can't be removed. You can stop writing data to that column and ignore it in follow-up forms but you can't delete it.

What are Entity conflicts and what can I do to avoid them?
----------------------------------------------------------

A conflict happens when two form Submissions both representing updates to the same Entity with the same version are received by the server. If the two Submissions specify different, overlapping updates to one or more properties, Central will provide an interface for understanding and resolving the conflict. All conflicts have to be explicitly dismissed.

One of our goals with Entities is to let field staff make as much progress as possible without interruption. For this reason, Central uses a last-write-wins strategy and applies all Entity updates it receives. Conflicts are shown from Central so that project administrators can look at the submitted data and work with field staff to resolve the issue.

When possible, we recommend using Entity properties and a :ref:`choice_filter <cascading-selects>` to limit the number of Entities that a specific field worker sees. This will greatly reduce the chance of conflicts.

.. seealso::
    * :ref:`Managing Entity conflicts <central-entities-update-conflicts>`

Should I analyze Entity data, form submission data or both?
-----------------------------------------------------------

Which is most appropriate will depend on the goals of your project.

Entities can be very useful for tracking work completion. Computing counts of Entities or of Entities of a particular status can be a simple way to understand project status. This can be useful independent of how final data analysis is conducted.

When the goal of a project is to deliver a service or to understand the final state of some Entities, it may be most practical to analyze the data in the Entities themselves.

Many projects involve capturing in-depth survey data at multiple points in time. In those cases, it's not important and can even be undesirable for historical data to be sent back to devices as Entities. In those cases, Entities can be used to drive the workflow and analysis can be conducted on form submission data, using Entity IDs to link submissions to each other.

Can I import data from another system as Entities?
--------------------------------------------------

Yes, you can import Entities to an existing Entity List by :ref:`uploading a CSV <central-entities-upload>` or :doc:`using the API <central-api-entity-management>`.
