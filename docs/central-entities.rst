Managing Entities in Central
================================

New in Central as of version 2022.3, **Entities** are a powerful new way to automatically bring the information you are collecting right back to your devices and Forms in the field.

In ODK today, you can attach existing data during the Form creation process, often through ``choices`` sheets or ``.csv`` files. Once this data is loaded into the Form, you can use it as the source for selection choices, to prepopulate data fields in the Form, or validate new input. A list of districts, for example, can be used as choices for selection, and information about each district can then be shown to the user or checked against. If you are new to these techniques, you can learn more about them on the :doc:`Form Datasets <form-datasets>` page.

This is wonderful if this data is already known when you are publishing your Form, and if it doesn't change over the course of your project. In many cases, however, the data being collected today for the project *is* the data you need tomorrow for the same project. Think about seeing a patient for the first and then second time, or registering and then revisiting a survey site for a follow-up. These kinds of workflows are called :ref:`Multiple Encounter <multiple-encounters-with-the-same-entity>` or longitudinal workflows.

If you have this kind of workflow, you can use the registered data items in a follow-up Form without using Entities, but it requires some work. You can download the Submission data from the registration Form, and then you can attach that data to a follow-up Form, as described above. However, the data available to devices in the field is only as current as your latest follow-up Form update. Some people write programs that automate this process over the API but this requires technical skills that many projects don't have.

Now there is a way to automate this process from within Central itself.

.. _central-entities-introduction:

Introducing Entities
---------------------

First, some definitions: each item that gets managed by an ODK workflow is called an **Entity**. Entities can be physical (e.g., a tree) or abstract (e.g., a site visit). A collection of Entities is called a **Dataset**.

Next, a new feature. You can now tell Central that some of your incoming Submission data should create Entities in a Dataset created and managed for you by Central. This Dataset can then be attached by that name to your follow-up Forms, exactly like you would manually attach a :doc:`CSV Dataset <form-datasets>`. You can attach a Dataset to any number of Forms, even to a registration Form.

.. image:: /img/central-entities/intro-diagram.png

Using this functionality, you don't have to create and upload Datasets yourself. When Submissions arrive and are approved, Central will create new Entities that will appear in follow-up Forms as soon as those Form updates are received.

If you are interested in seeing how Entities can fit into your workflow right away, we recommend following the Quick Start guide below, where you will upload a tree registration Form and a tree follow-up Form we have created already and see how trees are created by one Form and appear in another.

.. _central-entities-roadmap:

Roadmap and limitations
-----------------------

.. warning::
   Entities are currently in *experimental preview*! Please do not use it for real projects unless you are comfortable with things going wrong, or features changing in future releases. It is very unlikely you will ever lose data using Entities, but you may end up with *unexpected* data.

   The current limitations are:

   - Entity update and delete are not yet available
   - Performance is poor when managing more than a few thousand Entities
   - The Form specification and API may change

   You should also be aware that currently, all devices will always download all Entities. This may not be acceptable to you due to privacy concerns.

Here's what's available now and what's coming next. If you have feedback on this roadmap, please post on the `discussion forum <https://forum.getodk.org/>`_.

Available now
~~~~~~~~~~~~~
- Create an Entity with a registration form (requires project manager approval via UI or API)
- Create an Entity with different registration forms (e.g., child vs adult registration)
- Use Entities in a follow-up form
- Use Entities in different follow-up forms (e.g., weekly vs monthly follow-up)
- Use different Datasets in different registration and follow-up forms
- Download Datasets into Power BI, Excel, Python, and R

In three months
~~~~~~~~~~~~~~~

- Create, update, and delete Entities via Central's API (from external source and follow-up data)
- Update and delete Entities in Central's UI

In six months
~~~~~~~~~~~~~

- Automatically create Entities with registration forms (configurable for each Dataset)

In one year
~~~~~~~~~~~

- Automatically update Entities from follow-up forms
- Create Entities from uploaded spreadsheets

After one year
~~~~~~~~~~~~~~

- Create and update Entities offline
- Archive Entities (e.g., for closing cases)
- Segment Entities by user or other criteria (e.g., for tasking)
- Link Entities to each other (e.g., for nested entities)

.. _central-entities-quick-start:

Quick Start
-----------

We recommend watching the video below once or twice to get an overview of how Entities work in Central. Once you have that context, proceed with the steps below to try it yourself!

..  youtube:: hbff-oaI8yg
   :width: 100%

In this Quick Start, you will upload two Forms we have already authored for you: the `Tree registration Form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_ and the `Tree follow-up Form <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_. You will step through the registration of a new tree and the process of following up on that tree in a later Form.

First, let's prepare the Forms for use with Central.

1. Create a new Project, if you can. It can be easier to see what's going on without other Forms in the way.
2. Upload the `Tree registration Form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_. Notice how it has seen from the Form definition that the Form creates Entities in a Dataset, and populates three Entity Properties.
3. Publish the Form. As the dialog says, this action creates the ``trees`` Dataset within the Project you created.
4. Now, upload the `Tree follow-up Form <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_.
5. Switch over to the Form Attachments tab before you publish this Form, and notice how the Form wants a data file called ``trees.csv``, but that Central has already linked the Dataset ``trees`` (created when you published the registration Form in step 3) and you don't need to upload any data here.
6. Go back to the Draft Status page and publish this Form. Because this Form only *consumes* ``trees``, it does not make any changes to any Entity Properties.
7. Now, create an App User within this Project, allow it to access both of these Forms, and load them up into Collect or some other ODK-compatible client.

Next, let's see these Forms working together.

1. First, fill out and submit the Tree registration Form. Be sure to choose a species and specify a Tree circumference. Use 100 if you are not sure what to fill in.
2. Go back to Central. You can download the ``trees`` Dataset under the Datasets tab in your Project.
3. But your tree isn't there. It does take a moment sometimes to create an Entity from a Submission, but in this case it's because we're not done yet. An Entity will not be created until you *approve* the submission.
4. Go to the Trees registration Form Submissions page, and approve your tree.
5. Open the Submission details page for that Submission by putting your mouse on its row and clicking More.
6. You should now see a record of your approval, as well as of the creation of a new Entity based on the Submission. If you don't see the Entity yet, wait a second and refresh.
7. You can try downloading the ``trees`` Dataset again if you want to see your tree there.
8. Now go back to Collect and update your Forms to fetch the new data.
9. Next, fill out the Tree follow-up Form.
10. Your tree is here! Choose it.
11. Report a new circumference that is smaller than the old one. This is probably not a good idea for a tree. See how the Form warns you about this problem, based on the data you'd put into the registration Form.
12. Correct the circumference to a larger number, and submit the Form.

That's it! The follow-up Form only creates normal Submissions, so you can access the data it collects like any Form.

.. _central-entities-overview:

Entities in v2022.3
---------------------

If you skipped the Quick Start above, we suggest you go back and give it a try. You will learn hands on with Central a lot of what will be described below.

In these early versions of Entities, you cannot create a Dataset directly through the Central website. To begin using Entities, you will need to author a Form which defines them. By uploading a Form that specifies the fields in a Submission that should be used to create a new Entity, and the name of the Dataset these new Entities should go to, you will prompt Central to create the Dataset. You'll be able to see the Dataset information Central recognized in your Form once you upload it.

When you publish this Form, the new Dataset and/or new Entity Properties will be created for you automatically within the Project. You can learn more about authoring these kinds of Forms :ref:`in the sections below <central-entities-authoring>`.

.. note::
  In this version of Entities, a Submission must be approved before an Entity will be created from it. In future versions, you will be able to choose to create the Entity immediately when the server receives the Submission.

To see this new Dataset and download data from it, visit the :guilabel:`Datasets` tab on the Project page. In future versions, you will see many more controls and more helpful information than you do now.

To use data from a Dataset in another Form, you can refer to it by ``NAME.csv`` where ``NAME`` is the name of your Dataset. When you upload that Form, you should see on the Form Attachments tab that the file has been automatically linked to the Dataset. You can always override this connection by uploading your own data file to use instead. This does not affect the Dataset itself, your file is used *instead* of the Dataset for that Form only.

.. _central-entities-testing:

Testing Forms with Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checking that your Forms are working together the way you expect is challenging with Entities. You can create a Draft of a Form and use it as a safe space to try out Form definitions and see resulting Submissions. But Datasets reach *across* Forms. They live alongside Forms within the Project. How do Form Drafts related to the same Entities connect together?

It's very confusing, and Drafts currently don't handle this question very well. A future version of Central will provide better answers.

For now, *Datasets work on published Forms and Submissions only*. The creation of Datasets or new Entity Properties only occurs at the moment you publish the Form. Only real form Submissions create Entities. This means that you can't test the usage of Datasets in follow-up Forms until real Entities have been created.

To try the end-to-end workflow across multiple Forms, we recommend creating a temporary project just for testing. You can publish all the Forms, create Entities for testing, and make sure that all the Forms work well together.

You can also try a follow-up Form Draft by manually creating a CSV of sample Entities and then attaching it to your Draft, as described in :ref:`central-forms-attachments`. When you have verified the logic of the follow-up Form and are ready to publish it, you can change the link from the CSV to the desired Dataset.

.. _central-entities-authoring:

Creating Forms to use Entities
-------------------------------------------

Central does a lot of work to help you manage Entities, but at least for now the only way to ask it to do so is to create a Form that describes how.

In the following section, we describe how to author Forms that create new Entities, also known as registration Forms. After that, we discuss Forms that use Entities, also known as follow-up Forms.

.. _central-entities-registration-forms:

Build a Form that creates Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You’ll start by building a Form that creates new Entities in a Dataset called ``trees``. When you publish this Form, a ``trees`` Dataset will be created for you. When a Submission to this Form is approved, an Entity will be created in the ``trees`` Dataset from data in the Submission. These types of Forms are often referred to as registration, enrollment, intake or discovery Forms.

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

Specify the Dataset the Form should save Entities to
""""""""""""""""""""""""""""""""""""""""""""""""""""

Add a new ``entities`` sheet to your XLSForm. This is where you will specify your Dataset’s name, under ``dataset``.

Each Entity will be automatically assigned a unique name based on one or more Properties from the Entity data, just like the ``instanceName`` on submissions. The ``label`` field here is where you provide the expression to use as a label for each Entity in the Dataset.

The Dataset name will be used by Central to uniquely identify that Dataset. If a Dataset with the name you specify already exists in Central, this Form will create Entities in that existing Dataset. If Central doesn't yet have a Dataset with the specified name, it will be created.

The label expression can use any field in the Form.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: dataset, label

  trees,"concat(${circumference}, ""cm "", ${species})"

.. _central-entities-registration-forms-fields:

Specify the Form fields that are saved to Entities
""""""""""""""""""""""""""""""""""""""""""""""""""

If you think of your Dataset as a spreadsheet, each row represents an individual Entity and each column specifies an Entity Property.

You define Entity Properties by adding a ``save_to`` column to your XLSForm. You then put an Entity Property name in the ``save_to`` column for each Form field that you would like to save for use in follow-up Forms.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, save_to
 
  geopoint, current_location, Tree location, geometry
  select_one species, species, Tree species, species
  integer, circumference, Tree circumference in cm, circumference_cm
  text, intake_notes, Intake notes

If you'd like to check your work, you can compare with `this example form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_, with the ``entities`` sheet and ``save_to`` information.

When you publish this Form on Central, the ``trees`` Dataset will be created for you.

.. _central-entities-follow-up-forms:

Build a Form that uses Entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your ``trees`` Dataset can now be attached to any Form using ``select_one_from_file`` or ``csv-external``.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation
 
  select_one_from_file trees.csv, tree, Please select a tree
  calculate, prior_circumference, ,instance('trees')/root/item[name=${tree}]/circumference_cm
  integer, circumference, The circumference was previously measured as ${prior_circumference}cm. Please enter the current circumference in cm.

You can see the full XLSForm `here <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_.

The same Dataset can be used in many different Forms. The concepts and patterns described in the :doc:`data collector workflows <data-collector-workflows>` and the :doc:`Form Datasets <form-datasets>` sections apply to server-managed Datasets as well.

