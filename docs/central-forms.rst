.. spelling::

  Undeleting
  undelete


.. _central-forms-overview:

Managing Forms in Central
=========================

Forms are at the heart of ODK. Once fetched onto a mobile device from ODK Central, they define the questions, validation, and logic to be presented during data collection. They also serve to organize the data coming back from mobile devices.

.. _central-forms-forms:

Forms in ODK Central
--------------------

In ODK Central, there are four important tasks you'll perform while managing a data collection project:

1. **Form drafting** is where you design the Form itself, laying out many details like the questions and acceptable responses. ODK Central itself does not help with form design: instead, please take a look at the :doc:`introduction to form design <form-design-intro>` for help creating your form. Central does, however, help with **testing** your design, with Form Drafts. When you first upload your Form, it will be a Draft to which you can connect a mobile device and submit test data. If you are not satisfied with the Form, you can adjust the design and upload a new version in place of the old Draft. Once you are satisfied, you can **Publish** the Form to make it ready for use.
2. **Form lifecycle** settings allow you to control who can access and submit to particular Forms. These tools can help manage user permissions, but they can also help phase out outdated Forms as they come to the end of their life. You can control these using the :ref:`Form Access <central-projects-form-access>` tab on the Project.
3. **Data extraction and analysis** can occur either at the end of the project, or continually as the project runs. Either way, ODK Central provides several different methods for extracting and analyzing your submission data. This is covered in the :doc:`Form Submissions <central-submissions>` article.
4. **Form updates** allow you to make changes to a Form while it is already in use. Central allows you to create a new Draft of any Form at any time. As with initial Form creation, this Draft allows you to test your changes in a staging environment where it will not affect the live Form or its data. When you are satisfied with the Draft, you can again **Publish** it, and it will replace the live version.

Drafting and version updates are new as of Central 0.8. We will cover all of these topics in the sections below.

.. _central-forms-upload:

Uploading a form to ODK Central
-------------------------------

As mentioned, ODK Central does not feature a built-in form design utility. Please take a look at the :doc:`introduction to form design <form-design-intro>` for help creating your form.

As of version 0.7, Central will accept either XForms :file:`.xml` or XLSForm :file:`.xls`/:file:`.xlsx` files. If you have written your own :file:`.xml` file, we strongly recommend that you first double check that it is valid using `ODK Validate <https://github.com/getodk/validate>`_. If you upload an XLSForm spreadsheet, Central will convert it to an XForm for you, and it will be automatically validated as part of that process.

Once you have your form file, the next step will be to upload it into ODK Central. To do this, navigate to the Project (click on its name from the ODK Central homepage) to which you would like to add the Form, and locate the Forms listing section at the bottom of that page:

   .. image:: /img/central-forms/listing.png

From there, click on the :guilabel:`New` button next to the section header, and you should see a popup appear:

   .. image:: /img/central-forms/new.png

You can either click on the :guilabel:`choose one` button to browse for your :file:`.xml`, :file:`.xls`, or :file:`.xlsx` file, or if you already have it handy somewhere, you can drag it over the gray box and drop it to choose it. Either way, once you have chosen your file (you will see the name of your file at the bottom of the gray box when you do), you can click on the :guilabel:`Create` button immediately below to upload the form.

.. admonition:: Some errors you may see:

   - If you are uploading an XLSForm, and the converter flags warnings with it, your form will not be immediately created. You'll be shown the warnings, and given the option to either ignore them and create the form anyway, or else you can fix the issues and start over by uploading a new file.
   - You may see a message that reads **A resource already exists with xmlFormId value(s) of xyz.** If you do, there already exists a form within this project with the same unique designation. If you are using XLSForm, try changing the name of the file or the ``form_id`` in the settings sheet. If you designed the form by hand, please check the ``id="…"`` attribute immediately inside the ``<instance>`` tag.
   - You may see a message that says **A form previously existed which had the same formId and version as the one you are attempting to create now. To prevent confusion, please change one or both and try creating the form again.** This means there once was a form within this project that has since been deleted that has exactly the same formId (see the previous bullet point) *and* version designation as the one you are now trying to upload. Central won't accept the new form, because this conflict could cause confusion with mobile devices that still have the old form sitting around. To upload this form, change either the formId (again, see the previous bullet point) or `update the version <https://getodk.github.io/xforms-spec/#primary-instance>`_ and try again.

Once the form is successfully uploaded, you will be taken to the Form Draft page. It will not be accessible to data collection clients until you publish the Draft, which we will cover in the following section.

.. _central-forms-draft:

Working with Form Drafts
------------------------

Form Drafts, available as of Central 0.8, provide a way to safely and easily verify the design of your Form before you make it available for use. Drafts are accessible only to privileged Project staff. Each Form Draft has a unique access token which allows configured data collection clients to submit test submissions to the Draft. These test submissions disappear automatically when the Draft is published. Once a Draft is published, it is available for use according to the access rules you have specified in the :ref:`Form Access <central-projects-form-access>` tab on the Project.

   .. image:: /img/central-forms/draft-overview.png

The **Draft Status** page gives insight into the current status of your Draft, and provides controls for managing it.

On the left, you will find the Draft Checklist, which suggests the steps you might take before publishing your Draft. On the right are details about the currently uploaded Draft version of the Form, including its current version string, and actions you may take on the Draft:

 - The :guilabel:`Upload new definition` button will allow you to upload a new Form definition, which will replace the current Draft version. When this happens, all test submissions will be erased. If you have uploaded Media Files, Central will attempt to preserve any that match the new definition.
 - The :guilabel:`Publish Draft` button will publish the Draft, making it available for use according to the access rules you have specified on the :ref:`Form Access <central-projects-form-access>` tab on the Project. Any test submissions you have made will be erased.
 - The :guilabel:`Abandon Draft` button will delete the Draft. When there is not yet a published version, this will delete the entire Form. If the Form has been published, only the Draft will be deleted.

.. tip::
  When a form is first created, none of the existing App Users on the project will be able to access it for download or submission, even once the Form is published. Once you are ready to allow App Users to access the form, use the Project :ref:`Form Access <central-projects-form-access>` tab.

When you first create a new Form, the navigation tabs on the left will not be accessible. They pertain to the published version of the Form, and will become available once you publish your Draft. The tabs on the right, within the gray Draft section, relate to the Draft.

If your Draft requires Media Files, there will be a checklist step asking you to upload them, and a Media Files tab at the top of the page. See the next section :ref:`Forms With Attachments <central-forms-attachments>` for more information about uploading and managing attachments.

The :guilabel:`Testing` Draft tab shows test submissions that have been made to the Draft, and instructions for doing so:

   .. image:: /img/central-forms/testing.png

At the top of the page are instructions and a QR Code which will configure a mobile device to submit to the Draft Form. For help configuring a mobile device, please see :doc:`importing settings into Collect <collect-import-export>`. The table below these instructions contains any test submissions that have been made to the current Draft. For help with this table or exporting test data, please see :doc:`Form Submissions in Central <central-submissions>`.

.. _central-forms-attachments:

Forms With Attachments
----------------------

If your Form Draft references any external files (images, audio, or video included as part of your question prompts, or data lookup files used to populate selection lists), Central will see this and open up some additional displays and controls you will need to provide those external files:

   .. image:: /img/central-forms/attachments-overview.png

If you see this extra **Upload Form Media Files** checklist step and **Media Files** tab at the top of your Form Draft checklist, then Central believes you need to upload some files associated with this form. If the checklist step has been checked off, then you've already completed this task: great work! Otherwise, click on the :menuselection:`--> Media Files` tab at the top to see what files you'll need to provide.

   .. image:: /img/central-forms/attachments-listing.png

This form design references three files that we'll need to provide, one of which we've already uploaded. You can see the name and expected type of the file in the table, as well as when the file was last uploaded. You can click on the name of any uploaded file to download what Central has for it. To upload a new one, you'll want to drag-and-drop one or more files onto the table.

.. admonition:: On File Types and Contents

   While Central will detect the type of file the form design expects, and will verify that the name of any uploaded file matches one that is expected, Central will *not* double-check the *type* of the file, nor the *contents* of the file for you. So, just because Central accepts your file does not necessarily mean that it will work correctly.

Once you publish a Draft, you will not be able to modify the Attachments associated with it without creating a new Draft.

.. _central-forms-attachments-multi:

Bulk-uploading Many Attachments At Once
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. image:: /img/central-forms/attachments-multi.png

If you select and drag many files at once onto the table, Central will automatically try to match each file with a name in the table. You'll have a chance to see what it came up with and confirm that things look okay before the upload begins. You will see a warning if one or more of your dragged files don't match any of the expected names.

.. _central-forms-attachments-single:

Uploading One Attachment
~~~~~~~~~~~~~~~~~~~~~~~~

   .. image:: /img/central-forms/attachments-single.png

If you drag a single file onto the table, you'll have the option of which table row you'd like to upload that file into. This way, if the file isn't named exactly what Central expects, you can still upload a file into that slot without having to rename it on your own computer. But if the file does have the appropriate name, you can drop it somewhere other than a specific slot (for example, just below or just above the table) to have Central match it up with the correct slot automatically.

.. _central-forms-checklist:

The Form Overview page
----------------------

Here, you can get a brief summary of the status of your form, and recommended next steps. You are automatically taken here when you publish a Form Draft or click on the form name in the Form listing page. You can also get back here from other form-related pages by clicking the :menuselection:`--> Overview` tab below the name of the form.

   .. image:: /img/central-forms/checklist.png

The currently published version information is on the left. If you have a Draft in progress, you'll see its information on the right.

.. _central-forms-submissions:

Seeing Form Submissions
-----------------------

To see the current submissions uploaded to Central for a form, you can click on the :menuselection:`--> Submissions` tab below the name of the form. Here, you will see a summary table of all known submissions, and you will find multiple options for downloading and analyzing your submission data. This page and these options are covered in more detail in the :doc:`central-submissions` article.

.. _central-forms-public-links:

Managing Public Access Links
----------------------------

Public Access Links allow broad web-based distribution of a Form for direct responses from subjects. They can be used to conduct large remote self-administered data collection campaigns, or allow direct surveying of the public at large. Respondents will fill the Form directly in their web browser.

For more information, please see the :ref:`relevant section <central-submissions-public-link>` in the Submission article.

.. _central-forms-lifecycle:

Managing Form Lifecycle
-----------------------

Forms can be in one of three lifecycle stages: **Open**, **Closing**, and **Closed**. All forms start in **Open** state when they are first created. You can see what each of these means below:

========= ================================ ===================================
  State    Available for download to apps   Accepts new submissions from apps
--------- -------------------------------- -----------------------------------
Open      **yes**                          **yes**
Closing   no                               **yes**
Closed    no                               no
========= ================================ ===================================

As you can see, you can use the **Closing** state to prevent further distribution of a form while still allowing the final few submissions to come in, while the **Closed** state effectively turns the form off completely. You can always set the form lifecycle stage to whatever you want: you can always, for example, re-open a closed form.

To set the form lifecycle stage, go to the :ref:`Form Access <central-projects-form-access>` tab for the Project, under the name of the Project at the top of the page. You may have to navigate back out of the Form first by clicking on the :guilabel:`Back to Project Overview` link at the top of the page. Here, you will find the three possible stages in a dropdown for each Form on the left side of the page. Select the ones you want for each Form, then click :guilabel:`Save` at the top-right to save the changes.

You can find more information about the Form Access page :ref:`here <central-projects-form-access>`.

.. _central-forms-updates:

Updating Forms to a New Version
-------------------------------

As of Central 0.8, it is possible to update a published Form with a new definition, or new Media Files, and to test these changes before they are applied to the Form in use.

There is one primary restriction Central enforces on updated definitions: once defined in a published Form version, each field Data Name (in technical terms, the Instance XPath) cannot change its Data Type. Unused fields may be removed, and new fields may be added, but if any field reuses a previously existing Data Name, it must have the same Type as it did before. If you run into an error with this restriction, the easiest solution is usually to rename the changed field to a new name.

To begin the process of updating a published Form, click on the :guilabel:`Create a new Draft` button in the Draft navigation on the Form:

   .. image:: /img/central-forms/update-form.png

Initially, the new Draft will have the same definition as the published Form. If you only want to update attachment Media Files, this means you don't have to bother uploading a definition at all: you can go straight to the :guilabel:`Media Files` tab and :ref:`upload the changed files <central-forms-attachments>`.

You can replace the Draft definition, Media Files, and make test submissions as with the :ref:`initial Form Draft <central-forms-draft>` before the Form was first published. Test submissions will not interfere with published Form submissions.

Once you are satisfied that your updated Form is ready to be published for immediate use, you can click on the :guilabel:`Publish Draft` button on the Draft Status tab.

.. admonition:: Form Version naming

  If you did not change the definition, or your updated definition did not change the ``version`` of the Form, Central will not be able to publish the Form as-is. This is because the ``version`` must change in order for data collection clients to understand that they should update. You can upload a new definition with a changed ``version``, or else Central will offer to change it in-place for you.

Once the Draft has been published, it becomes the version in use and there will no longer be a Draft associated with the Form.

.. admonition:: What happens to my submissions?

  When a new Form version is published in place of an old one, all the previous submissions continue to exist, and will export along with all your data over Zip download or OData. However, only the current Form definition will be used in that export: if, for example, you have deleted a field that used to exist, that field will not appear in the export.

  Draft testing submissions will never export with your final data, and only exist as long as the Draft does. If you delete, publish, or replace your current Draft, all test submissions will be cleared away.

.. _central-forms-versions:

Accessing Older Form Versions
-----------------------------

If you have published multiple version of a Form, you can see each of them under the :guilabel:`Versions` tab.

   .. image:: /img/central-forms/versions.png

Each published version of the Form will be listed, along with actions to download the definition of each Form. In future versions of Central, the Media File attachments associated with each version of the Form will be downloadable as well.

.. _central-forms-delete:

Deleting a Form
---------------

.. tip::
   If you only want to turn the form off so that it doesn't appear to users of mobile data collection apps, we suggest using the :ref:`form lifecycle controls <central-forms-lifecycle>` explained above.

If you are certain you wish to delete a Form, you can find the option on the Form Settings page: click on the :menuselection:`--> Settings` tab under the name of the form at the top of the page. On the right side of this page, you will find the :guilabel:`Delete this form` button.

   .. image:: /img/central-forms/trash.png

Once a Form has been deleted, it will remain in the Trash for 30 days before being permanently deleted. You can find the Trash on the Project page, under the Forms list. Here, you can undelete a Form using the button on the right. Undeleting a Form will restore it exactly as it was when deleted.

After 30 days, when a Form is permanently deleted, the data will be removed from the system completely.

