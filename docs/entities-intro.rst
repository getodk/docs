:orphan:

.. spelling:word-list::

    Airtable
    AppSheet
    Farmforce

**************************
Introduction to Entities
**************************

If you've heard something about ODK Entities and want to better understand whether they're useful for you, you're in the right place! We've organized this page as a series of questions that are independent from each other so you can pick and choose the sections that interest you.

If you're someone who learns best by doing, you may prefer to jump straight into the tutorial on :doc:`building a community reporting tool with Entities <tutorial-community-reporting>` and to come back here if you have any questions. If you have a question that we haven't answered, you can `post on the forum <https://forum.getodk.org/c/support/6>`_.

.. note::

    Entities are not available in every ODK-compatible system. Use :doc:`ODK Central <central-intro>` for the best Entities experience.

Concepts
========

What are Entities?
------------------

In the ODK context, an "Entity" can be thought of as a "thing". If your project involves things that need to be shared between forms and may change over time, you can represent them as Entities. You can use Entities to represent real things like trees, people, or cities. You can also represent more abstract things like tree visits, malaria cases, or city ratings as Entities.

Entities are organized in Entity Lists that group together Entities of the same type. You can think of Entity Lists as spreadsheets or databases that are shared across forms. Forms can create, read, and update Entities. You can also think of Entities as the nouns (trees) and the forms as the verbs (Register a tree).

ODK has historically been form-based: every workflow starts by opening a blank form and filling it out. We are now working towards an Entity-based data collection where workflows start by selecting an Entity. If you need this behavior today, have your form start with a question that lets users select an Entity from a list.

What's the relationship between Entities and forms?
---------------------------------------------------

Entities and forms exist at the same level in projects. Forms define actions that can be taken in your project and Entities store data that can be accessed as part of taking those actions. Currently, a form submission can create or update a single Entity. Eventually, it will be possible to create multiple Entities of the same type or to update different Entities from a single form.

Once a submission has been processed and it creates or updates an Entity, the submission and the resulting Entity become independent. That means that if you edit the submission, those changes are not automatically applied to the related Entity. You can choose to apply them manually if applicable.

Should I use Entities?
----------------------

Entities are an optional add-on to ODK. There are many users of ODK don't need to use Entities because their data collection is done at a single moment in time and doesn't use any previously collected data.

That said, any workflow that involves multiple steps over time has the potential to benefit from Entities. If you find yourself wishing you could flow data from one form to another or send data back to devices, you likely want to use Entities. Common examples include site inspections, studies that involve linking baseline and follow-up visits, and case management.

Entities can also be helpful for sharing data that rarely changes between multiple forms. For example, if all your forms need to use a country's districts, you can represent those once in an Entity List and share that list between the forms. This means if the districts do change, you can make the necessary updates in one place and know that all related forms will get the update.

Entities are very powerful and it can be tempting to look for ways to use them in every project. This power comes at a cost of greater complexity and more potential for error, though! When you use Entities, you have to consider the possibility that some users may be offline for some time, possibly resulting in conflicts. You also have to consider that Entities themselves will change over time and affect form design logic in ways you don't expect.

What's the relationship between Entities and longitudinal data collection?
--------------------------------------------------------------------------

Longitudinal studies involve following one thing over time. Because Entities represent things that are shared between forms, they can be used to represent longitudinal study subjects. Those Entities can be used to make sure each subject is only registered once, to track and verify the number of data capture events related to one subject, and to link encounters of the same subject at analysis time.

When designing a longitudinal study supported by Entities, you will likely have an Entity List with a name like ``participants`` or ``subjects``. The Entities model is flexible so you can choose exactly the structure that best supports your desired workflow and reflects the terminology that's used in your domain.

What's the relationship between Entities and case management?
-------------------------------------------------------------

"Case" is a term used in many fields to mean an instance of something. A case is opened when a specific condition is detected, may go through multiple steps across a broad range of caseworkers while the case condition is still true, and then is closed when the case condition is no longer true. For example:

* Medicine: healthcare workers may manage malaria cases or pregnancy cases

* Humanitarian services: a humanitarian team may be involved in child protection cases or asylum cases.

* Law: legal teams may manage human rights violation cases or property damage cases.

Other related terms include "issues" or "problems". An "incident" generally references to a group of cases with the same root cause. For example, an electricity provider may get multiple case reports of households without electricity and declare an outage incident that needs to be managed.

You can use ODK Entities to support managing cases, issues, problems, incidents, etc. To do so, you will likely have Entity Lists with names like ``malaria_cases``, ``outages``, ``issues``. 

.. seealso::
    The :doc:`Community reporting tutorial <tutorial-community-reporting>` implements a simple case management workflow in which anyone can open a case (called "problem" in the tutorial) and specific individuals can resolve them.

While case management is a process that is familiar in many fields, it's not universal. ODK has always been a generic tool and by using more a more general approach, we believe we can better support the needs of users who work in diverse domains.

Even in fields where case management is common, there is often a need to support other kinds of workflows within the same tool and it can be awkward to use the word "case" in those contexts, especially when referencing concrete entities such as participants or hospitals. Our goal is to let you define Entity Lists that make sense in your context and to allow you to use and connect them in ways that best support your workflow.

Why can't I just flow data from one form to another form?
---------------------------------------------------------
TODO: focus on list of last state

While flowing data between forms is intuitive and works really well for workflows with a baseline and one or more independent follow-ups, it can become difficult to use for more complex workflows that involve multiple steps. For example, imagine that you want to represent a workflow in which a tree disease is reported and then the tree is visited multiple times by different people for treatment until the disease is resolved. If you wanted a form to show the tree's current status, you would need to look up that status in the latest submission made about that tree that includes a status update. That involves writing an expression that joins submissions across multiple forms and means that those submissions need to be available on all devices.

Let's say you want to add a new form to the tree workflow and that this form needs to consider the status of trees. In a world where data flows directly from one form to another, you have to be careful to connect every single form that may capture status information to this new form (alternately you could make sure all submissions about a tree has a status but that also has downsides). If you forget one, your form will appear to work but may use the wrong status.

We believe that Entities is more intuitive for complex workflows and helps avoid these kinds of mistakes while encouraging small, single-action forms. Entities also makes it relatively straightforward to build ways to select survey subjects or show lists and summaries of all survey subjects. These are common needs that are harder to satisfy with a form-to-form model.

With Entities, you can update the Entity's status with each related submission and access the status directly. Only the latest status of the Entity needs to be communicated to devices. If you prefer having the full history like you would with form submission data being flowed between forms, you can use a ``tree_visits`` Entity List that you add to rather than a ``trees`` Entity List in which you make updates. The additional Entity List provides more flexibility in how you support your workflow needs.

In many contexts, the information that needs to be shared between forms is minimal, sometimes only an ID and label are needed. Sometimes the subjects of a workflow are known ahead of time, either from a prior ODK form or some other system. Entities makes both of these cases straightforward and intuitive to represent.

Limitations
===========

I filled out a registration form and don't immediately see my Entity in follow-up forms, why?
---------------------------------------------------------------------------------------------

Currently, in order for a submission to create or update an Entity, that submission has to be processed by your server. That means that if you create a new Entity or update an existing one by filling out a form, you won't see that change reflected in follow-up forms until you download the latest update to your Entity List from your server.

If you usually have Internet connectivity, this is unlikely to be very important. Similarly, if your registration and follow-up periods happen at very different times, this limitation is not a problem. But for workflows in which follow-up needs to happen immediately after registration or multiple follow-ups are needed while offline, this limitation is significant. 

Offline Entity support is expected in late 2024, read more `on the forum <https://forum.getodk.org/t/collect-coming-soon-offline-entities/46505>`_.

I need to assign specific Entities to specific data collectors, how can I represent this?
-----------------------------------------------------------------------------------------

Currently, an entire Entity List is always sent to every device and there is no way to subset the list. This is something that we intend to eventually enable. 

For now, you can limit the Entities that are available from a :ref:`select_one_from_file <select-from-external-dataset>` using a :ref:`choice_filter <cascading-selects>`. This won't limit the amount of data sent to each device but it can significantly reduce the amount of options shown to each user and can help speed up lookup expressions.

Can I have millions of Entities?
--------------------------------

There are two current limitations that make millions of Entities impractical: data transfer and form performance.

Currently, all Entities that have not been deleted are sent to every device on every update. Depending on your data connection, this may be a limiting factor for your project. We will eventually add support for archiving Entities to address this limitation.

Entities are currently represented in memory for access by forms. Modern devices can easily process multiple tens of thousands of entities in this way, but your form may become slow or crash if you have more than 50,000 Entities.

We are actively working on addressing these performance limitations and expect significant improvements by late 2024. In the mean time, one possible workaround is to use `pulldata <https://xlsform.org/en/#how-to-pull-data-from-csv>`_ and `search() <https://xlsform.org/en/#dynamic-selects-from-pre-loaded-data>`_ instead of `instance` and `select_one_from_file`. These methods are less flexible but they will perform better.

My form captures data on multiple different things, can I create multiple Entities with a single submission?
------------------------------------------------------------------------------------------------------------

Not yet, but this is something we will eventually support.

If you'd like to create or update multiple Entities of the same type in a repeat, you can capture base information in one form and then use a separate form to create each Entity that you currently represent by repeat instances. You can link those submissions to their parent by including the parent ID in the child Entity. 

If you are working in an environment with Internet connectivity, you can refresh the forms to see your created parent Entities in your child Entity creation forms. If you are working in a disconnected environment, you can have data collectors copy the ID from the parent form to the child forms.

Similarly, if you'd like to establish relationships between multiple Entities of different types, you can have a registration form for each type and include a field to represent a link to another Entity.

Alternatives
=============

What's the relationship between Entities and CSV form attachments?
---------------------------------------------------------------------

From a form design perspective, they are identical! That means you can attach them to forms, look values up in them or build selects on them in the exact same way.

From a server perspective, a CSV form attachment can only be associated with a single form, unlike Entities which can be shared between forms. CSV form attachments are stored as files and if you need to update one row in a CSV attachment, you need to replace the whole file. In contrast, Entities can be updated individually.

You can -- and many users do -- accomplish the same thing as Entities with CSV form attachments and your own automation using the Central API. The biggest advantage of Entities over that approach is that you don't need to run your own automation.

I currently use CSV form attachments to manage a workflow over time, should I use Entities instead?
----------------------------------------------------------------------------------------------------

If this process is working well for you, you don't need to change anything. Entities can help you avoid mistakes or save time. If you aren't making mistakes and don't feel like supporting your workflow is too time-consuming, do not feel like you need to change anything. In particular, if your workflow involves distinct phases, it may be better to analyze and clean baseline data before feeding it into the next phase rather than automatically flowing data with Entities.

What's the relationship between Entities and choice lists?
------------------------------------------------------------

From a form design perspective, they are nearly identical! The only significant difference is that because Entity Lists are defined outside of a form, you need to explicitly attach them to your forms using :ref:`select_*_from_file <select-from-external-dataset>` or :ref:`csv-external <form-datasets-attaching-csv>`. Another difference is that there isn't currently support for media or translations to be defined for Entity Lists. Other than that, the way that you look up values in choice lists and Entity Lists using ``instance()`` is identical.

Now that ODK has Entities, can it replace more specialized software that I use (DHIS2, Farmforce, etc)?
-------------------------------------------------------------------------------------------------------

ODK is a general-purpose data collection and workflow automation platform. Its strength is that it lets users quickly build tools that meet their exact needs. You can even think of ODK as an application-building platform: with data defined by your Entity Lists and behavior defined by your forms, you truly could implement nearly any app you can imagine in ODK.

There exist many systems that are designed specifically for managing cases/incidents/issues in a specific field. Those systems typically have some built-in concepts around the types of teams that might be involved in the management process, the kinds of status changes that a case may go through, and how cases can be resolved.

Here are some questions to consider when deciding between using ODK or specialized software:

* Does the specialized software support needs like working in an offline environment?
* Is the workflow encoded by the purpose-built software appropriate for my context? How close is it to my ideal workflow?
* What concepts are important to my workflow and are these easy or hard to represent in ODK vs the specialized platform? (for example: caseworkers, referrals, payments,...)
* How complex is my workflow? How many different states can my Entities be in? How many different actions can be taken on them?
* Do I expect I'll want to iterate on my workflow over time as I learn more or conditions change?
* Do I have the time and resources to fully test custom forms? (note that even using purpose-built tools is likely to involve some adaptation and testing time)
* What are the implications of a form design error? (for example: a field worker will call me and I will fix it vs. someone could die because they fail to receive care)

If you work in a field with well-defined workflows and specific software that already supports those workflows, we generally recommend using that over ODK. ODK's strength is in letting you define and refine your forms and Entity Lists to exactly match your workflow needs.

ODK Entities don't have any built-in concepts or structure to support managing a certain kind of data. This means you have complete freedom to represent only the things that matter to you and to define exactly what actions can be taken on them. This is extremely powerful but it also means that you have the responsibility to think through every design decision and test it.

You should also consider the complexity of your needs. Let's consider some case management examples. Cases can be short-lived with few, predictable interventions needed like in the case of a pothole reported to a city that may be closed within a week when the city repairs the pothole. Cases can also be very long-lived with many, unpredictable interventions needed like in the case of an refugee case that may last multiple years involving legal teams, humanitarians and politicians from multiple countries.

Workflows that are short-lived can very easily be represented in ODK and may not benefit from a system made specifically for that purpose. On the other hand, purpose-built systems may be easier to find and customize for simple projects.

More complex workflows are more likely to benefit from a more structured and tested system, especially in contexts like healthcare where specific protocols have been developed and the implications of a workflow error are serious. On the other hand, complex workflows may benefit from the flexibility that ODK offers. For example, ODK makes it very easy to add new states that cases could be in as they are needed, new forms to support those states, or stop collecting or using data values that are found not to be useful.

For many contexts, workflow needs are so specific and dynamic that a platform like ODK offers many benefits. Once you have defined your workflow in ODK, the forms you have built can become the standard, specialized way to support others in your domain.

With Entities, is ODK now like Airtable/Notion/AppSheet?
---------------------------------------------------------------------

All of these are examples of tools that make it possible to define data tables and provide different kinds of views on top of those data tables. Some differences between these platforms and ODK:

* ODK is designed with offline contexts in mind. Most of the other mentioned tools either need connectivity or have limited offline modes.
* ODK forms encode workflows to help field workers complete their tasks. Forms use constraints, field types, relevance, etc to limit and guide what form users can do. They also can use a broad range of dynamic question types and appearances. In contrast, the data management tools described above use a data-first model and although they are getting more and more features to define forms on top of data models, these are typically less powerful and more tightly linked to the corresponding data model than they are in ODK. The other tools tend to shine in high-trust teams with individuals who define their own data views and modify data tables directly.
* ODK can be used to support large-scale, time-bound efforts like mass vaccination campaigns. This requires many field users active for a short amount of time. The other tools mentioned usually base their pricing model on the number of end users which is not well-suited to those kinds of efforts.

ODK remains closer to surveying platforms but Entities give it workflow automation functionality.

Mechanics
===========

How do I access Entities from my forms?
---------------------------------------

The first thing you need to do in your form definition is to attach the Entity List you want to access Entities from. If you want the user to be able to select an Entity from a list, you can use a :ref:`select_one_from_file <select-from-external-dataset>` question with the name of your Entity List followed by `.csv`. For example, if your Entity List is named ``trees``, you would have a ``select_one_from_file trees.csv`` question. Everything you know about selects and selects from files apply to attached Entity Lists. For example, you can use an Entity property in a :ref:`choice_filter <cascading-selects>` expression to filter down an Entity List.

If you want to look up Entities using a user-provided value such as a unique ID scanned from a barcode or entered manually, you can attach your Entity List with :ref:`csv-external <form-datasets-attaching-csv>`.

Once a specific Entity is selected, you can look up its properties using a :ref:`lookup expression <referencing-values-in-datasets>`. All of this works exactly the same way as it does with attached CSV files!

.. seealso::
    * :doc:`Community reporting tutorial <tutorial-community-reporting>`
    * :ref:`Central Entities documentation <central-entities-follow-up-forms>`

Can I use data from another system or an existing form's submissions as Entities?
----------------------------------------------------------------------------------

Yes, you can add Entities to an existing Entity List by :ref:`uploading a CSV <central-entities-upload>` or :doc:`using the API <central-api-entity-management>`.

How do I use forms to create or update Entities?
------------------------------------------------

There are two parts to declaring that a form's submissions should create or update an Entity. First, you need to add an ``entities`` sheet to your form and at minimum use it to define the Entity List that the form populates and an expression to give each Entity a label. Second, you can optionally declare that certain form fields should be saved to Entity properties by putting the desired property name in the ``save_to`` column for each form field.

.. seealso::
    * :doc:`Community reporting tutorial <tutorial-community-reporting>`
    * :ref:`Central Entities documentation <central-entities-follow-up-forms>`

What form fields should I save to my Entities as properties?
------------------------------------------------------------

This will vary a lot project by project. In many cases, a descriptive label clearly identifying individual Entities is enough to meet goals like making sure that no duplicate Entities are created and connecting submissions about the same Entity in analysis.

For more complex workflows, it can be helpful to include a property that represents some sort of status which determines what forms can operate on any given Entity. In some contexts, it may be important to include multiple identifying properties to make sure that the correct Entity is selected. Sometimes it's important to show data collectors a summary of information that was previously captured and so it must all be saved on the Entity.

We generally recommend thinking carefully about the minimum amount of data that you need to drive your workflow. The less data you save and access, the simpler your form design will be and the less data will need to be transmitted to data collectors. However, there is no enforced limit on number of properties.

Currently, once a property is added to an Entity List, it can't be removed. You can stop writing data to that column and ignore it in follow-up forms but you can't delete it.

What are Entity conflicts and what can I do to avoid them?
------------------------------------------------------------

When two form submissions that are received by Central specify updates to the same Entity with the same version, Central considers this a conflict. If the two submissions specify different, overlapping updates to one or more properties, Central considers this a hard conflict and will provide an interface for resolving it. Both hard and soft conflicts have to be explicitly dismissed.

One of our goals with Entities is to let field staff make as much progress as possible without interruption so Central applies conflicting updates with the latest one taking precedence. The conflict is shown on the server and office staff can look at the submitted data and work with field staff to resolve the issue.

When possible, we recommend using Entity properties and a :ref:`choice_filter <cascading-selects>` to limit the number of Entities that a specific field worker sees. This will greatly reduce the opportunity for conflicts.

.. seealso::
    * :ref:`Entity updates from submissions <central-entities-update>`

Should I process/analyze Entity data, form submission data or both?
---------------------------------------------------------------------

Any of those are possible and which is most appropriate will depend on the goals of your project.

Entities can be very useful for tracking work completion. Computing counts of Entities or of Entities of a particular status can be a simple way to understand project status. This can be useful independent of how final data analysis is conducted.

When the goal of a project is to deliver a service or to understand the final state of some Entities, it may be most practical to base analysis on Entities themselves.

Many projects involve capturing in-depth survey data at multiple points in time. In those cases, it's not important and can even be undesirable for historical data to be sent back to devices. In those cases, Entities can be used to drive the workflow and analysis can be conducted on survey data, using Entity ids to link submissions to each other.
