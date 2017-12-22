Form Management
==================

You can add, download and delete forms, export data into useful formats, publish data into another service, manually upload submissions and view the published data. ODK Aggregate provides all these options under the :guilabel:`Form Management` tab.

.. _create-manage:

Managing forms
----------------

You can view all your forms, add new forms, delete forms, download forms as well as restrict submissions for a form.

Click on :guilabel:`Forms list` tab to see a list of all your forms.  

.. image:: /img/aggregate-use/form-list.*
   :alt: Image showing list of all forms.

Under the :guilabel:`Form list` tab, you will see :guilabel:`Add New Form` button  to upload a new form definition to ODK Aggregate. 

.. image:: /img/aggregate-use/add-form.*
   :alt: Image showing add form button.

When you click on it a box will open asking for details of the form. :guilabel:`Form Definition` is required and :guilabel:`Media File(s)` is optional. Choose the .xml file that will be used. You can also choose the appropriate media files for the form.  

.. image:: /img/aggregate-use/add-form-options.*
   :alt: Image showing add form options.

You can manage all the forms present on your server in your form list. All options displayed in the form list are as follow:

- Click on :guilabel:`Title` to view the XML for a form. You can then download XML for that form by clicking on :guilabel:`Download XML` in the Form XML Viewer.

.. image:: /img/aggregate-use/xml-viewer.*
   :alt: Image showing xml viewer for form.

- :guilabel:`Form Id` is the unique name for the form.
- :guilabel:`Media Files` displays the count of media files you have uploaded for the form.
- :guilabel:`User` is the user who uploaded the form.
- Clicking on :guilabel:`Downloadable` checkbox enables/disables Aggregate from displaying the form to remote clients so that they can download the form.
- Clicking on :guilabel:`Accept Submissions` checkbox enables/disables Aggregate ability to accept submissions for the particular form. 

.. tip::

  Disable accepting submission by unchecking the :guilabel:`Accept Submissions` checkbox if you want to prevent users from submitting more data for a particular form.

- Click on :guilabel:`Delete` when you want to remove a form.     

.. _export-form:

Exporting form data
---------------------

Click on :guilabel:`Export` option in the form list to export form into useful formats and choose the format in which you want to export data. You can also choose a filter which you have saved for the form to export only a certain subset of form. Details on :ref:`exporting data <export-data>` are given in the :doc:`data transfer  <aggregate-data-access>` section.   

.. _publish-form:

Publishing form data
-------------------------
 
Click on :guilabel:`Publish` option in the form list to publish the form into another service. You can choose where you want to publish data and which data you want to publish. Details on :ref:`publishing data <publish-data>` are given in the :doc:`data transfer  <aggregate-data-access>` section.

.. _view-publish-data:

Viewing Published data
----------------------------

You can get a view of the published data you have created for a particular form by clicking on :guilabel:`Published Data`. 

.. image:: /img/aggregate-use/published-data.*
   :alt: Image showing published data.

- Select the form corresponding to the published data in the :guilabel:`Form` dropdown.
- Read the message that appears and click on :guilabel:`Purge Published Data`.
- :guilabel:`Created By` shows the email of the user who created the published file.
- :guilabel:`Status` can be `ACTIVE` (the file is ready to view) or `ESTABLISHED` (something went wrong in the process of exporting.)
- :guilabel:`Start Date` shows the time when you finished filling out the :guilabel:`Publish` form.
- :guilabel:`Action` is based on your selection of upload only, stream only, or both in the :guilabel:`Publish` form.
- :guilabel:`Type` shows the type you choose to publish your data to.
- :guilabel:`Owner` shows the owner of the published data.
- :guilabel:`Name` is the place where you published your data. If the type was a Google Fusion Table, click on the link to view the Fusion Table.
- Select delete box in the :guilabel:`Delete` column if you want to delete your published file.     

.. _submission-admin:

Managing Submissions manually
---------------------------------

You can manually upload submissions for a form and check incomplete submissions under the :guilabel:`Submission Admin` tab. Following options are available:

.. image:: /img/aggregate-use/submission-admin.*
   :alt: Image showing submission admin tab.

- Click on :guilabel:`Manually upload submission data` to manually upload submissions.

.. image:: /img/aggregate-use/submission-upload.*
   :alt: Image showing window to manually upload submissions.

.. note::

  Submissions are located under the /odk/instances directory on the phone's sdcard. This directory will contain subdirectories with names of the form: formID_yyyy-mm-dd_hh-MM-ss. Within each of these subdirectories are the submission data file (named: formID_yyyy-mm-dd_hh-MM-ss.xml),and zero or more associated data files for the images, audio clips, video clips, etc. linked with this submission.

- Select form in the :guilabel:`Form` dropdown and click on :guilabel:`Purge Submission Data` if you want remove submission data for a particular form.

- You can also see a list of incomplete submissions for a particular form under the :guilabel:`Incomplete Submissions` list.

.. note::

  If you upload the submission, but fail to upload all media attachments, it places the submission in the incomplete submissions bucket. While it resides there, it won't be published to external servers or downloadable via ODK Briefcase.      


