Managing Entities in Central
================================

.. versionadded:: v2022.3

**Entities** in ODK let you share information between Forms so you can collect longitudinal data, manage cases over time, and support other complex workflows.

Without Entities, you can attach existing data during the Form creation process, often through ``choices`` sheets or ``.csv`` files. Once this data is loaded into the Form, you can use it as the source for selection choices, to prepopulate data fields in the Form, or validate new input. A list of districts, for example, can be used as choices for selection, and information about each district can then be shown to the user or checked against. If you are new to these techniques, you can learn more about them on the :doc:`Form Datasets <form-datasets>` page.

This is wonderful if the data you want to use is already known when you are publishing your Form, and if it doesn't change over the course of your project. In many cases, however, the data being collected today for the project *is* the data you need tomorrow for the same project. Think about seeing a patient for the first and then second time, or registering and then revisiting a survey site for a follow-up. These kinds of workflows are called :ref:`multiple encounter <multiple-encounters-with-the-same-entity>` or longitudinal workflows.

If you have this kind of workflow, you can use the registered data items in a follow-up Form without using Entities, but it requires some work. You can download the Submission data from the registration Form, and then you can attach that data to a follow-up Form, as described above. However, the data available to devices in the field is only as current as your latest follow-up Form update. Some people write programs that automate this process over the API but this requires technical skills that many projects don't have. Now there is a way to automate this process from within Central itself.

.. _central-entities-introduction:

Introducing Entities
---------------------

To give you a quick sense of the end-to-end process, below is a video that shows a simple survey with baseline and follow-up data collection.

..  youtube:: YHkKNWgYKaI
   :width: 100%

.. note::
   The forms in the above video show a simple survey with baseline and follow-up forms. The follow-up form shows three possible ways to look up an existing participant. Download the XLSForms: `Add participant <https://docs.google.com/spreadsheets/d/13pdMv3wNbd14hjN-dqxXgmgLN0fzvfGxbQa6OXvJNpU/edit#gid=0>`_ and `Participant follow-up <https://docs.google.com/spreadsheets/d/1tfrpIrixbOHdAb_aLejWq7HTeJaSjZVqcQLdAP86WA0/edit#gid=0>`_.

First, some definitions: each item that gets managed by an ODK workflow is called an **Entity**. Entities can be physical (e.g., a tree) or abstract (e.g., a site visit). Entities of the same type are organized in **Entity Lists**.

.. note::

   In Central versions prior to v2023.4, Entity Lists were called Datasets.

Next, a new feature. You can now tell Central that some of your incoming Submission data should create Entities in an Entity List created and managed for you by Central. This Entity List can then be attached by that name to your follow-up Forms, exactly like you would manually attach a :doc:`CSV document <form-datasets>`. You can attach an Entity List to any number of Forms, even to a registration Form.

.. image:: /img/central-entities/intro-diagram.png

Using this functionality, you don't have to create and upload Entity Lists yourself. When Central receives submissions (or they are approved, see :ref:`the settings section <central-entities-settings>`), new Entities are automatically created. As soon as users of the Follow-up Form(s) get Form updates, they can interact with the new Entities.

If you are interested in seeing how Entities can fit into your workflow right away, we recommend following the :ref:`Quick Start <central-entities-quick-start>` guide below, where you will upload a tree registration Form and a tree follow-up Form we have created already and see how trees are created by one Form and appear in another.

If you would prefer a more personalized introduction, request a demo at https://getodk.org.

.. _central-entities-roadmap:

Roadmap and limitations
-----------------------

Entities are a big new concept that open up a lot of new possibilities. While we think many workflows can benefit from Entities today, they have some limitations that you should be aware of.

What's available now:

- Create an Entity with a registration form (automatically or after project manager approval)
- Use multiple different registration forms targeting the same Entity List (e.g., registration at school vs. registration at home)
- Use Entities in one or more follow-up form
- Download Entities into Power BI, Excel, Python, and R

Important limitations:

- Entity create and update requires Internet access
- Entity delete is only available via API
- Client performance (ODK Collect or Enketo web forms) suffers when managing more than 10,000 Entities
- All devices will always download all Entities which may be a privacy concern
- The Form specification and API may change

We expect all of these limitations to be addressed over time. The roadmap at `getodk.org/roadmap <https://getodk.org/roadmap>`_ has what we're working on now and what's coming next.

.. _central-entities-quick-start:

Quick Start
-----------

We recommend watching the video below once or twice to get an overview of how Entities work in Central. Once you have that context, proceed with the steps below to try it yourself!

.. note::

   In Central versions prior to v2023.4, Entity Lists were called Datasets. The video below was recorded with Central v2022.3 so many small improvements have been made since.

..  youtube:: hbff-oaI8yg
   :width: 100%

In this Quick Start, you will upload two Forms we have already authored for you: the `Tree registration Form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_ and the `Tree follow-up Form <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_. You will step through the registration of a new tree and the process of following up on that tree in a later Form.

First, let's prepare the Forms for use with Central.

1. Create a new Project, if you can. It can be easier to see what's going on without other Forms in the way.
2. Upload the `Tree registration Form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_. Notice how Central knows from the Form definition that the Form creates Entities in an Entity List, and populates three Entity Properties.
3. Publish the Form. As the dialog says, this action creates the ``trees`` Entity List within the Project you created.
4. Now, upload the `Tree follow-up Form <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_.
5. Switch over to the Form Attachments tab before you publish this Form, and notice how the Form wants a data file called ``trees.csv``, but that Central has already linked the Entity List ``trees`` (created when you published the registration Form in step 3) and you don't need to upload any data here.
6. Go back to the Draft Status page and publish this Form. Because this Form only *consumes* ``trees``, it does not make any changes to any Entity Properties.
7. Now, create an App User within this Project, allow it to access both of these Forms, and load them up into Collect or some other ODK-compatible client.

Next, let's see these Forms working together.

#. First, fill out and submit the Tree registration Form. Be sure to choose a species and specify a Tree circumference. Use 100 if you are not sure what to fill in.
#. Go back to Central and click on ``trees`` in the :guilabel:`Entities` tab in your Project.
#. Click on the :guilabel:`Data` tab and you should see your new tree! If you don't, you can wait a second or two and refresh.
#. Now go back to Collect and update your Forms to fetch the new data.
#. Next, fill out the Tree follow-up Form.
#. Your tree is here! Choose it.
#. Report a new circumference that is smaller than the old one. This is probably not a good idea for a tree. See how the Form warns you about this problem, based on the data you'd put into the registration Form.
#. Correct the circumference to a larger number, and submit the Form.

That's it! The follow-up Form creates normal Submissions, so you can access the data it collects like any Form.

.. _central-entities-overview:

Creating Entity Lists
---------------------

.. note::
  If you skipped the Quick Start above, we suggest you go back and give it a try. You will learn hands on with Central a lot of what will be described below.

In these early versions of Entities, you cannot create an Entity List directly through the Central website. To begin using Entities, you will need to author a Form which defines them. By uploading a Form that specifies the fields in a Submission that should be used to create a new Entity, and the name of the Entity List these new Entities should go to, you will prompt Central to create the Entity List. You'll be able to see the Entity information that Central recognized in your Form once you upload it.

When you publish this Form, the new Entity List and new Entity Properties will be created for you automatically within the Project. You can learn more about authoring these kinds of Forms :ref:`in the sections below <central-entities-authoring>`.

.. note::
  By default, Entities are created immediately when the server receives the Submission. If you want to require a review step before Entities are available for follow-up, you can configure this in each Entity List's :ref:`settings <central-entities-settings>`.

To see this new Entity List and download data from it, visit the :guilabel:`Entities` tab on the Project page.

To use data from a Entity List in a Form, you can refer to it in a :ref:`select_one_from_file <selects-from-csv>` question as ``NAME.csv`` where ``NAME`` is the name of your Entity List. When you upload that Form, you will see on the Form Attachments tab that the file has been automatically linked to the Entity List.

.. _central-entities-testing:

Testing Forms with Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checking that your Forms are working together the way you expect is challenging with Entities. You can create a Draft of a Form and use it as a safe space to try out Form definitions and see resulting Submissions. But Entity Lists reach *across* Forms. They live alongside Forms within the Project. How do Form Drafts related to the same Entities connect together?

Drafts currently don't handle this question very well and a future version of Central will provide better answers.

For now, *you can only create Entity Lists and Entities from published Forms and Submissions*. The creation of Entity Lists or new Entity Properties only occurs at the moment you publish the Form. Only real form Submissions create Entities. This means that you can't test the usage of Entities in follow-up Forms until real Entities have been created.

To try the end-to-end workflow across multiple Forms, we recommend creating a temporary Project just for testing. You can publish all the Forms, create Entities for testing, and make sure that all the Forms work well together.

You can also try a follow-up Form Draft by manually creating a CSV of sample Entities and then attaching it to your Draft, as described in :ref:`central-forms-attachments`. When you have verified the logic of the follow-up Form and are ready to publish it, you can change the link from the CSV to the desired Entity List.

.. _central-entities-authoring:

Creating Forms to use Entities
--------------------------------

Central does a lot of work to help you manage Entities, but at least for now the only way to ask it to do so is to create a Form that describes how.

In the following section, we describe how to author Forms that create new Entities, also known as registration Forms. After that, we discuss Forms that use Entities, also known as follow-up Forms.

.. _central-entities-registration-forms:

Build a Form that creates Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You’ll start by building a Form that creates new Entities in an Entity List called ``trees``. When you publish this Form, a ``trees`` Entity List will be created for you. When a Submission to this Form is received, an Entity will be created in the ``trees`` Entity List from data in the Submission. These types of Forms are often referred to as registration, enrollment, intake or discovery Forms.

.. _central-entities-registration-forms-structure:

Define the structure of the Entity-creating Form
""""""""""""""""""""""""""""""""""""""""""""""""

Start by defining the structure of your Form in `XLSForm <https://docs.getodk.org/xlsform/>`_ using the standard Form building blocks. For example, `this form <https://docs.google.com/spreadsheets/d/1ogupGLD_O42MRAW380IP4LDQY6tUdrGyLaSFZux-vuI/edit#gid=0>`_ is used to register trees:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
 
  geopoint, location, Tree location
  select_one species, species, Tree species
  integer, circumference, Tree circumference in cm
  text, intake_notes, Intake notes

Test your Form to make sure it works and collects the data that you need. 

.. _central-entities-registration-forms-destination:

Specify the Entity List the Form should save Entities to
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Add a new ``entities`` sheet to your XLSForm. This is where you will specify your Entity List name, under ``list_name``.

The Entity List name will be used by Central to uniquely identify that Entity List. If an Entity List with the name you specify already exists in Central, this Form will create Entities in that existing Entity List. If Central doesn't yet have a Entity List with the specified name, it will be created.

Each Entity must have a label to identify it on Central and for use in follow-up Forms. The ``label`` field on the ``entities`` sheet is where you provide the expression to define the label for each Entity. This is very similar to the `instance name specified for a Submission <https://docs.getodk.org/xlsform/#naming-filled-forms>`_. The label expression can use any field in the Form, including ones that aren't saved to Entity Properties.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: list_name, label

  trees,"concat(${circumference}, ""cm "", ${species})"

.. _central-entities-registration-forms-fields:

Specify the Form fields that are saved to Entities
""""""""""""""""""""""""""""""""""""""""""""""""""

If you think of your Entity List as a spreadsheet, each row represents an individual Entity and each column specifies an Entity Property.

You define Entity Properties by adding a ``save_to`` column to your XLSForm. You then put an Entity Property name in the ``save_to`` column for each Form field that you would like to save for use in follow-up Forms.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, save_to
 
  geopoint, current_location, Tree location, geometry
  select_one species, species, Tree species, species
  integer, circumference, Tree circumference in cm, circumference_cm
  text, intake_notes, Intake notes

If you'd like to check your work, you can compare with `this example form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_, with the ``entities`` sheet and ``save_to`` information.

When you publish this Form on Central, the ``trees`` Entity List will be created for you.

.. _central-entities-follow-up-forms:

Build a Form that uses Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your ``trees`` Entity List can now be attached to any Form using ``select_one_from_file`` or ``csv-external``.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation
 
  select_one_from_file trees.csv, tree, Please select a tree
  calculate, prior_circumference, ,instance('trees')/root/item[name=${tree}]/circumference_cm
  integer, circumference, The circumference was previously measured as ${prior_circumference}cm. Please enter the current circumference in cm.

You can see the full XLSForm `here <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_.

The same Entity List can be used in many different Forms. The concepts and patterns described in the :doc:`data collector workflows <data-collector-workflows>` and the :doc:`Form Datasets <form-datasets>` sections apply to Entity Lists as well.

.. _central-entities-update:

Updating Entities from Forms
----------------------------

.. versionadded:: v2023.5

You can use Forms to update Entity information. These Forms can be authored to, for example, update previous observations to new values or change the status of an Entity. Just like Entity creation through Forms, you can specify which properties on which Entity instances will be updated when the Form's Submissions are uploaded to Central. The data in Submissions uploaded by Entity-updating Forms are applied to the Entity data saved on the Central server. These updated Entity values are then distributed to data collection clients once they synchronize with Central.

.. _central-entities-update-conflicts:

Parallel Updates in Updating Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you begin allowing updates to Entities to come in through the field, you can run into incidents where two people attempt to update the same Entity at the same time. If you have a project setup where Entities would only be updated by one person at a time (for example, if that person is the only one assigned to a particular area), you can ignore this section.

.. _central-entities-update-conflicts-what-is:

What is a parallel update?
""""""""""""""""""""""""""

What does it mean that updating an Entity "at the same time" causes a conflict? Every time an Entity is updated, whether by direct edits on the Central management panel, through the API, or by a Submission upload, a new "version" of that Entity is created that has the latest data.

Say Alice fetches all her Tree data on her device. This update includes a brand new Tree entity called "Zach's backyard tree". Alice updates Zach's tree with new measurements. This results in version 2 of that tree once the Submission is uploaded to Central. In a "clean," not-conflicting update Bob would get the latest Tree data, see version 2 of Zach's tree in his update Form, and upload his new changes to create version 3 of the tree on Central. Version 1 led to version 2, and version 2 was updated to create version 3.

However, if Bob doesn't update his data before filling his Form, and so he's still working off version 1 of the tree, then a conflict results. Two updates have been created based on version 1, and Bob didn't know that Alice had already made the changes resulting in version 2. Alice and Bob are both looking at version 1 and trying to create version 2.

.. note::
   The same rules and behaviors apply when updating Entities through updates made directly to Entities in Central's management panel, or over the API. It's possible, for example, that Bob opened an Entity data edit window in Central before Alice's update is uploaded, but he didn't actually press Submit on his changes until much later. The same is true: Bob is looking at version 1 and thinking he's creating version 2.

Central's behavior in these cases is basic: **it will always apply any changes it receives at the time and in the order it receives them**. This means that in this case, Bob's changes will always "win" over Alice's. Any time this happens, Central will generate a :guilabel:`conflict` warning in several places in the Central management panel so Project managers can see that a problem might have occurred.

Of course, it's possible that Bob's changes and Alice's changes are totally compatible. For example, it's possible Alice only updated the circumference of the tree's trunk, while Bob only reported that moss is now growing. How often and severely conflicts create actual consistency problems with Entity data will depend on the design and complexity of your data collection process and your Forms. Central attempts to help Project managers determine the severity of conflicts by separating conflict warnings into two levels of severity.

**All** conflicts surfaced by Central occur because two Entity updates were generated based off the same base version of an Entity. This circumstance is called a :guilabel:`Parallel Update` in Central. In the special case that a property included in an update has also been changed in the meantime, *and* the value currently stored in Central is different from the new updated value, a full :guilabel:`Conflict` error will be created instead, indicating that multiple possibly conflicting values were written into the same property at once. So if Alice and Bob have both updated the circumference of the tree at the same time to the same value, only a Parallel Update warning and not a Conflict will be flagged. Only if their inputs disagree will you see a full Conflict.

.. _central-entities-build-update:

Building a Form that updates an Entity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updating Entities isn't too different from creating new Entities, but you'll have to specify the ``entity_id`` of the specific Entity instance you want to update in the ``entities`` sheet.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: list_name, entity_id
 
  trees, ${tree}

In this example, a tree in the ``trees`` Entity List will be updated when Submissions based on this Form are created. The particular tree to be updated must be given in the ``entity_id`` column, which here is a reference to the ``tree`` form field. That form field could be a ``select_one`` that lets the user choose a specific tree, a QR code scanning field, or any other field that will hold the value of a specific tree's ID.

Once you have this update information set up, you can add ``save_to`` rules to your Form questions as with Entity creation:

.. csv-table:: survey
  :header: type, name, label, save_to
 
  geopoint, current_location, Tree location, location
  select_one species, species, Tree species
  integer, circumference, Tree circumference in cm, circumference_cm
  text, notes, Notes

Here, the ``current_location`` and ``circumference`` questions have been set up to update properties in the Entity, while the ``species`` and ``intake_notes`` questions don't update anything to the Entity.

.. _central-entities_build-update-label:

Updating the Entity Label
"""""""""""""""""""""""""

To update the label of an Entity from a Form, fill in the optional ``label`` column in the ``entities`` sheet as you would when setting the label on Entity creation.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: list_name, entity_id, label
 
  trees, ${tree},"concat(${circumference}, ""cm "", ${species})"

.. _central-entities_build-update-conditional:

Setting conditions under which an Entity is updated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can limit a Form to only update an Entity under certain conditions, based on an expression using the Entity and Submission data.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: list_name, entity_id, update_if
 
  trees, ${tree}, true()

In this case, ``true()`` is given in the optional ``update_if`` column, which means the Entity will always be updated upon submission. If an expression is given instead, the Entity is only updated when the expression evaluates to ``true`` or ``1``.

.. _central-entities_build-update-create:

Creating AND Updating Entities with one Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can give both a ``create_if`` and an ``update_if`` rule for the same Form. If only one of these expression evaluates to ``true`` or ``1``, then only that operation will be carried out. If both rules evaluate to ``true`` or ``1``, the Entity will be created if it does not exist (as identified by the ``entity_id`` expression), and updated if it does. Of course, if neither rule evaluates to ``true`` or ``1``, no Entity changes will occur.

.. _central-entities-managing:

Managing Entities
-------------------

To browse all Entity Lists in a Project, go to the :guilabel:`Entities` tab within the Project. You will see a list of all Entity Lists that have been created by Forms in this Project. Click on any Entity List to see basic details about it.

   .. image:: /img/central-entities/entity-landing.png

On this page, you can see how this Entity List relates to other incoming data in your Project: which Forms contribute to the Entity List, which ones read data from it, and which fields are being read or written. To see the actual data in your Entity List, click on the :guilabel:`Data` tab at the top.

.. _central-entities-data:

Managing Entity Data
--------------------

You can preview or download Entity data from Central from the :guilabel:`Data` tab on the Entity List's page.

   .. image:: /img/central-entities/entity-table.png

Similar to the Submissions data page for a Form, you will see overall metadata like the create and update time on the left side of the table, and the actual data values on the right. You can press :guilabel:`Refresh` to fetch the latest data, or use any of the options at the top right of the table to export the data to a file or an analysis tool.

To see, edit, and manage additional details about a particular Entity, hover over its row in the table and click on :guilabel:`More` to go to the Entity Detail page. Alternatively, you can click on the pencil icon to edit the Entity data immediately.

   .. image:: /img/central-entities/entity-table-review.png

By default, you see all Entities in the Entity List. If an Entity has a :ref:`conflict warning <central-entities-update-conflicts>` attached to it, you will see an alert in that table row. You can filter down to only Entities that do or don't have conflict warnings using the filter above the table. On the row of any Entity with a conflict warning, you can click on the red :guilabel:`Review Parallel Updates` button to see more information about the warning, make any edits needed to correct problems, and dismiss the warning if desired. You can also click through to the Entity Detail page to do these things with a little more information.

.. _central-entities-detail:

Seeing Entity Detail
~~~~~~~~~~~~~~~~~~~~

The Entity Detail page provides a complete look at the data and history of a particular Entity, and gives tools and options to manage it. You might arrive here by clicking on the Entity name somewhere else, like in an update feed, but you can always find the Entity you want in the Entity Data table and click on the :guilabel:`More` button.

   .. image:: /img/central-entities/entity-detail.png

Similar to the Submission data detail page, the Entity detail page has some basic information about your Entity on the left, and an Activity Feed showing you the history of the Entity on the right.

You can see the actual data stored in the Entity in the bottom left under the :guilabel:`Entity Data` section, and you can edit that information by clicking on :guilabel:`Edit` right there.

   .. image:: /img/central-entities/entity-conflict.png

When there is a conflict warning active on the Entity, you will see a notice above the Activity Feed. Here you can see a summary table of all the Entity updates that might be conflicting with each other. In the feed below, updates that are possibly in conflict will be highlighted. If you want a broad look at the updates in concern, the table is a great summary, but sometimes it can help to look at the changes described in each update in the Feed to really see what's going on.

You can dismiss the conflict warning by pressing :guilabel:`Mark as Resolved` underneath the summary table. When you do this, the warning is dismissed. All values about this Entity currently in Central are now considered non-conflicting. Therefore, you may wish to :guilabel:`Edit` the values using the button on screen before marking the warning as resolved.

.. _central-entities-edit:

Editing Entity Data
~~~~~~~~~~~~~~~~~~~

To edit the data stored for an Entity, you can locate the Entity in the :ref:`Entity data table <central-entities-data>` and click on the pencil icon that shows up on top of its row, or you can click on the :guilabel:`Edit` button if you are already looking at the detail page for the Entity.

   .. image:: /img/central-entities/entity-edit.png

A dialog will appear with all the Entity data listed. You will see the name of the field in the first column, the currently saved value for each field in the second column, and an edit field you can use to update the data in the third column.

The very first row labeled :guilabel:`Entity Label *` is not part of the Form data collected. Rather, it is the title of the Entity, which is computed from the Entity data when the Entity is first created using rules set by the Form author. You can change it to any value here.

As you type, Central will highlight any fields you have changed in yellow so you can see what you've done.

To complete the process press the :guilabel:`Update` button to save your changes to the Entity. You will see a confirmation that the save succeeded. If you don't like your changes, you can click on the :guilabel:`x` or the :guilabel:`Never mind` link to close the dialog.

.. _central-entities-manage-conflicts:

Managing Entity conflicts
-------------------------

When an Entity is in a possible conflict, Central will raise the issue in many places throughout the management panel: in the homepage Entity Lists tables, in Entities tables on Project pages, in the Entity Data table, and on Entity Detail pages.

You can review and dismiss conflicts from the :ref:`Entity table <central-entities-data>`, or from the :ref:`Entity Detail page <central-entities-detail>`. When you dismiss a conflict warning, the warning goes away and whatever values are currently recorded in Central are considered correct.

.. _central-entities-settings:

Changing Entity List Settings
------------------------------

Right now, only one setting is available for Entity Lists in Central. To reach it, click on the :guilabel:`Settings` tab on the Entity List page.

   .. image:: /img/central-entities/entity-settings.png

Here, you can choose whether Entities are created immediately when they are first received by Central, or if Central should wait until the Submission is approved before creating any Entities from it.

Note that only one of these two behaviors can be chosen at a time. If you change the setting from "on approval" to "when received" but you still have unapproved Submissions, Central will not ever be told to make Entities out of these Submissions. If this is the case for you and you try to make this setting change, you will see a special message and you will have the option to convert all pending (not approved or rejected) Submissions into Entities right away.

Select either option and you should see a confirmation the setting has changed.


