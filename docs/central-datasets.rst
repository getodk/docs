Datasets and Entities in Central
================================

.. warning::
   This is an *experimental* feature! Please do not use it unless you are comfortable with things going wrong, or features changing in future releases. It is very unlikely you will ever lose data using Datasets and Entities, but either due to unknown bugs or early confusion it is always possible you may end up with *unexpected* data.
  
   You should also be aware that since there are not yet Dataset filtering features in this early version, all devices will download all registered Entities always. You may not want or be able to accept this due to privacy concerns.

   Last, know that for now Datasets are early and slow. Collect and Central aren't smart enough to understand when a Dataset has updated, so clients will download data on every update even if nothing has changed. Large Datasets may also become a performance problem.

   All of that said, if you have thoughts and feedback for the direction of Datasets and Entities, please raise them on the `discussion forum <https://forum.getodk.org/>`_.

New in Central as of version 2022.3, **Datasets** and **Entities** are a powerful new way to bring the information you are collecting right back to your devices and forms in the field.

In ODK today, you can pull in data you have already available during the form creation process, often through ``choices`` sheets or ``.csv`` files. Once this data is loaded into the form, you can use it as the source for selection choices, to prepopulate data fields in the form, or validate new input. A list of districts, for example, can be used as choices for selection, but also information about each district can then be shown to the user or checked against. If you are new to these techniques, you can learn more about them on the :doc:`Form Datasets <form-datasets>` page.

This is wonderful if this data is already known when you are publishing your form, and if it doesn't change over the course of your project. In many cases, however, the data being collected today for the project often *is* the data you need tomorrow for the same project. Think about seeing a patient for the first and then second time, or registering and then revisiting a survey site for a follow-up. These kinds of workflows are called :ref:`Multiple Encounter <multiple-encounters-with-the-same-entity>` or longitudinal workflows.

Today, if you have this kind of a registration form, you can use the registered data items in a future form, but it requires some work. You can download the submission data from the registration form in Central, and then you can load that data into the data included with a follow-up form, just as described in the second paragraph above. This means that the data available to devices in the field is only as current as you are able to complete this transfer, from submitted data of a registration form to the static source data for any follow-up forms. Some people write programs that automate this process over the API.

Now there is a way to automate this process from within Central itself.

  .. image:: /img/central-datasets/intro-diagram.svg

No big changes. First, just some words: we have a name for the data referenced by any form: it is a **Dataset**. A ``districts`` choices list, or a file ``patients.csv``, these are Datasets. Each item in a Dataset is called an **Entity**. So each district would be an Entity in the districts Dataset, and each patient would be an Entity in the patients Dataset.

Next, a new feature. You can now teach Central that some of your incoming submission data should be set aside in a Dataset just for that purpose, created and managed for you by Central under whatever name you assign it——``patients``, for example. This Dataset can then be pulled in by that name (*(1)* above) into your follow-up forms, exactly like you would with existing Dataset data today.

Unlike today, however, you don't then have to create or upload, say, ``patients.csv`` yourself, nor update it when new patients are added. When submissions arrive (and are approved *(2)*) that Central has been taught about, it will create *(3)* new Entities that will appear in patient follow-up forms as soon as those devices update those follow-up forms.

.. tip::
   For now, you can only add a new **Entity** to the Dataset for each submission, but in the future you will be able to update existing Entities, or create multiple Entities at once. Also, there is not yet a way to directly upload data you may already have into a Central-managed Dataset *(4)*.

There are details that are explained further on, like how to actually create a Dataset, but for now this overview should be what you need to know.

If you are interested in seeing how Datasets can fit into your workflow right away, we recommend following the Quick Start guide in this next section, where you will upload a tree registration form and a tree follow-up form we have created already and see how trees are created in one form and appear in another.

.. _central-datasets-quick-start:

Quick Start: the Trees dataset
------------------------------

In this Quick Start, you will upload two Forms we have already authored for you: the `Tree registration form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_ and the `Tree follow-up form <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_. You will step through the registration of a new tree and the process of following up on that tree in a later form.

First, let's prepare the forms for use with Central.

1. Create a new Project, if you can. It can be easier to see what's going on without other Forms in the way.
2. Upload the Tree registration form linked above. Notice how it has seen from the form definition that the Form creates a Dataset, and populates three fields within that Dataset.
3. Publish the Form. As the dialog says, this action creates the ``trees`` Dataset within the Project you created.
4. Now, upload the Tree follow-up form.
5. Switch over to the Form Attachments tab before you publish this form, and notice how the form wants a data file called ``trees.csv``, but that Central has already linked the Dataset ``trees`` (created when you published the registration form in step 3) and you don't need to upload any data here.
6. Go back to the Draft Status page and publish this form. Because this form only *consumes* Datasets, it does not make any changes to any Dataset fields.
7. Now, create an app user within this Project, allow it to access both of these forms, and load them up into Collect or some other ODK-compatible client.

Next, let's see these forms working together.

1. First, fill out and submit the Tree registration form. Be sure to choose a species and specify a Tree circumference. Use 100 if you are not sure what to fill in.
2. Go back to Central. You can download the ``trees`` Dataset under the Datasets tab in your Project.
3. But your tree isn't there. It does take a moment sometimes to create an Entity from a submission, but in this case it's because we're not done yet. An Entity will not be created until you *approve* the submission.
4. Go to the Trees registration form submissions page, and approve your tree.
5. Open the Submission details page for that submission by clicking on More over the row.
6. You should now see a record of your approval, as well as of the creation of a new Entity based on the submission. If you don't see the Entity yet, wait a second and refresh.
7. You can try downloading the ``trees`` Dataset again if you want to see your tree there.
8. Now go back to Collect and update your Forms to fetch the new data.
9. Next, fill out the Tree follow-up form.
10. Your tree is here! Choose it.
11. Report a new circumference that is smaller than the old one. This is probably not a good idea for a tree. See how the form warns you about this problem, based on the data you'd put into the registration form.
12. Correct the circumference to a larger number, and submit the form.

That's it! The follow-up form just creates a normal submission, so you can access the data it collects like any form.

.. _central-datasets-overview:

How to use Datasets in v2022.3
------------------------------

If you skipped the Quick Start above, we suggest you go back and give it a try. You will learn hands on with Central a lot of what will be described below.

In these early versions of the Datasets and Entities feature, you cannot create a Dataset directly through the Central website. To begin using Datasets, you will need to author a form which feeds data into one. By uploading a form that specifies the fields in a submission that should be used to form a new Entity, and the name of the Dataset these new Entities should go to, you will prompt Central to activate the feature. You'll be able to see the Dataset information Central recognized in your form once you upload it.

When you publish this form, the new Dataset and/or new fields will be created for you automatically within the Project. You can learn more about authoring these kinds of forms :ref:`in the sections below <central-datasets-authoring>`.

In this version of Datasets and Entities, a submission must be approved before an Entity will be created from it. In future versions, you will be able to choose to create the Entity immediately when the server receives the submission.

To see this new Dataset and download data from it, visit the :guilabel:`Datasets` tab on the Project page. In future versions, you will see many more controls and more helpful information than you do now.

To use data from a Dataset in another form, you can refer to it by ``NAME.csv`` where ``NAME`` is the name of your Dataset. When you upload that form, you should see on the Form Attachments tab that the file has been automatically linked to the Dataset. You can always override this connection by uploading your own data file to use instead. This does not affect the Dataset itself, your file is used *instead* of the Dataset.

.. _central-datasets-testing:

Testing Forms with Datasets in v2022.3
--------------------------------------

Checking that your forms are working together the way you expect is challenging with Datasets. Usually you can create a Draft of a form and use it as a safe space to try out form definitions and data submissions. But Datasets reach *across* forms. They live alongside forms within the Project. How do these drafts connect together?

It's very confusing, and the current Drafts feature doesn't really handle these questions very well. A future version of Central will provide better answers.

For now, *Datasets work on published forms and submissions only*. The creation of Datasets or new Dataset fields only occurs at the moment you publish the form, and only then will entities be created according to that form's design.

This means that you will be unable to directly test the usage of Dataset data on follow-up forms. 

In the meantime, we recommend that you manually upload your Entities into your follow-up forms, as described in the introduction to this page discussing how things are done today.

.. _central-datasets-authoring:

Writing forms to use Central Datasets and Entities
==================================================

Central does a lot of work to help you manage Entity data, but at least for now the only way to ask it to do so is to create a form that describes how.

In the following section, we describe how to author forms that create new Entities, also known as registration forms. After that, we discuss forms that use Entities, also known as follow-up forms.

.. _central-datasets-registration-forms:

Build a form that creates new Entities
--------------------------------------

You’ll start by building a Form that creates new Entities in a Dataset called ``trees``. When you publish this Form, a ``trees`` Dataset will be created for you. When a Submission to this form is approved, an entity will be created in the ``trees`` Dataset from data in the Submission. These types of Forms are often referred to as registration, enrollment, intake or discovery forms.

In this current release, you will start building your form in XLSForm and make some modifications to it in XML before upload. In the future, you will be able to define your Entities-related forms entirely in XLSForm.

.. _central-datasets-registration-forms-structure:

Define the structure of the entity-creating form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start by defining the structure of your form in `XLSForm <https://docs.getodk.org/xlsform/>`_ using the standard form building blocks. For example, `this form <https://docs.google.com/spreadsheets/d/1ogupGLD_O42MRAW380IP4LDQY6tUdrGyLaSFZux-vuI/edit#gid=0>`_ is used to register trees:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
 
  geopoint, location, Tree location
  select_one species, species, Tree species
  integer, circumference, Tree circumference in cm
  text, intake_notes, Intake notes

Test your form to make sure it works and collects the data that you need. 

.. _central-datasets-registration-forms-destination:

Specify the Dataset that the form should save entities to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a new `entities` sheet to your XLSForm. This is where you will specify your Dataset’s name, under ``dataset``.

Each Entity will be automatically assigned a unique name based on one or more fields from the Entity data, just like the ``instanceName`` on submissions. The ``label`` field here is where you provide the expression to use as a label for each entity in the Dataset.

The Dataset name will be used by Central to uniquely identify that Dataset. If a Dataset with the name you specify already exists in Central, this form will create entities in that existing Dataset. If Central doesn't yet have a Dataset with the specified name, it will be created.

The label expression can use any field in the form.

.. rubric:: XLSForm

.. csv-table:: entities
  :header: dataset, label

  trees,"concat(${circumference}, ""cm "", ${species})"

.. _central-datasets-registration-forms-fields:

Specify the form fields that are saved to entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you think of your Dataset as a spreadsheet, each row represents an individual Entity and each column specifies an Entity Property.

You define Entity Properties by adding a ``save_to`` column to your XLSForm. You then put an Entity Property name in the ``save_to`` column for each form field that you would like to save for use in follow-up forms.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, save_to
 
  geopoint, current_location, Tree location, geometry
  select_one species, species, Tree species, species
  integer, circumference, Tree circumference in cm, circumference_cm
  text, intake_notes, Intake notes

If you'd like to check your work, you can compare with `this example form <https://docs.google.com/spreadsheets/d/1xboXBJhIUlhs0wlblCxcQ3DB5Ubpx2AxLDuaXh_JYyw/edit#gid=2050654322>`_, with the ``entities`` sheet and ``save_to`` information.

When you publish this form on Central, the ``trees`` Dataset will be created for you.

.. _central-datasets-follow-up-forms:

Build a form that uses Entities
-------------------------------

Your ``trees`` Dataset can now be attached to any Form using ``select_one_from_file`` or ``csv-external``.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation
 
  select_one_from_file trees.csv, tree, Please select a tree
  calculate, prior_circumference, ,instance('trees')/root/item[name=${tree}]/circumference_cm
  integer, circumference, The circumference was previously measured as ${prior_circumference}cm. Please enter the current circumference in cm.

You can see the above example as a working spreadsheet `here <https://docs.google.com/spreadsheets/d/12oJZDpJ8RxtmNopfqNKp3RWMsf4O3MWACYOTub_yZaQ/edit#gid=0>`_.

The same Dataset can be used in many different Forms. The concepts and patterns described in the :doc:`data collector workflows <data-collector-workflows>` and the :doc:`form datasets <form-datasets>` apply to server-managed Datasets as well.

