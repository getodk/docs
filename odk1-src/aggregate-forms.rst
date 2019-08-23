Managing Forms in Aggregate
================================

You can add, download and delete forms, export data into useful formats, publish data into another service, manually upload submissions and view the published data. ODK Aggregate provides all these options under the :guilabel:`Form Management` tab.

.. _aggregate-view-blank-form-list:

View blank form list
----------------------

Click on :guilabel:`Forms list` tab to see a list of all your forms.  

From here, you can add new forms, delete forms, download forms as well as restrict submissions for a form.


.. image:: /img/aggregate-use/form-list.*
   :alt: Image showing list of all forms.

.. _aggregate-form-list-info:

Blank form info in list
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the functional columns described below, the form list displays the following information about each form.

- :guilabel:`Form Id` is the unique name for the form.
- :guilabel:`Media Files` is the count of media files associated with the form.
- :guilabel:`User` is the user who uploaded the form.

.. _aggregate-add-new-forms:

Adding New Forms
------------------
   
Under the :guilabel:`Form list` tab, you will see :guilabel:`Add New Form` button  to upload a new form definition to ODK Aggregate. 

.. image:: /img/aggregate-use/add-form.*
   :alt: Image showing add form button.

When you click on it a box will open asking for details of the form. :guilabel:`Form Definition` is required and :guilabel:`Media File(s)` is optional. Choose the ``.xml`` file that will be used. You can also choose the appropriate media files for the form.  

.. image:: /img/aggregate-use/add-form-options.*
   :alt: Image showing add form options.

.. _aggregate-view-download-form:
   
Viewing and downloading forms
-----------------------------------------

From the :ref:`form list <aggregate-view-blank-form-list>`,  click on form's :guilabel:`Title` to view the XForm (the actual XML file). You can then download the file by clicking on :guilabel:`Download XML` in the Form XML Viewer.

.. image:: /img/aggregate-use/xml-viewer.*
   :alt: Image showing xml viewer for form.

.. note::

  Please, be aware that Aggregate doesn't store the original uploaded blank form. Instead, it rebuilds a blank form with what's stored in the database. This implies that there could be some slight differences:

  - All blank forms downloaded from Aggregate will include an XML comment with the build date.
  - Any left padding with zeroes will be lost on the form's version number if it was originally present (`000042` will become `42`).

.. _aggregate-toggle-form-download:

Disabling or enabling downloading of a form
----------------------------------------------
   
To disable or enable the ability of Collect or other clients to download forms, toggle the checkbox in the :guilabel:`Downloadable` column of the :ref:`blank forms list <aggregate-view-blank-form-list>`.

.. _aggrgete-toggle-form-submission:

Disabling or enabling submission of a form
--------------------------------------------

To disable or enable the ability of Collect or other clients to submit completed instances of a form, toggle the checkbox in the :guilabel:`Accept Submissions` column of the :ref:`blank forms list <aggregate-view-blank-form-list>`.

.. _aggregate-delete-blank-form:

Deleting a blank form
-----------------------

Click on the :guilabel:`Delete` button for the form in the :ref:`blank forms list <aggregate-view-blank-form-list>`.

.. _export-form:

Exporting form data
---------------------

Click on :guilabel:`Export` option in the form list to export form into useful formats and choose the format in which you want to export data. You can also choose a filter which you have saved for the form to export only a certain subset of the form. Details on :ref:`exporting data <export-data>` are given in the :doc:`data transfer  <aggregate-data-access>` section.   

.. _publish-form:

Publishing form data
-------------------------
 
Click on :guilabel:`Publish` option in the form list to publish the form into another service. You can choose where you want to publish data and which data you want to publish. Details on :ref:`publishing data <publish-data>` are given in the :doc:`data transfer  <aggregate-data-access>` section.

.. _view-publish-data:

Viewing published data
~~~~~~~~~~~~~~~~~~~~~~~~~~

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
- :guilabel:`Name` is the place where you published your data.
- Select delete box in the :guilabel:`Delete` column if you want to delete your published file.     

.. _managing-form-submissions:

Managing submissions manually
---------------------------------

You can manually upload submissions for a form and check incomplete submissions under the :guilabel:`Submission Admin` tab.

.. image:: /img/aggregate-use/submission-admin.*
   :alt: Image showing submission admin tab.

.. _aggregate-submit-forms-directly:
   
Submitting forms directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
To manually upload form submissions, click on :guilabel:`Manually upload submission data`.

.. image:: /img/aggregate-use/submission-upload.*
   :alt: Image showing window to manually upload submissions.

.. note::

  Submissions in the Collect app are located under the /odk/instances directory on the phone's SD card. This directory will contain subdirectories with names of the form in the format ``formID_yyyy-mm-dd_hh-MM-ss``. Within each of these subdirectories are the submission data file (``formID_yyyy-mm-dd_hh-MM-ss.xml``), and zero or more associated media files (images, audio, video) associated with this submission.

    .. add link to collect file structure 
    
.. note::

  If you upload a submission, but fail to upload all media attachments, it places the submission in the incomplete submissions bucket. While it resides there, it won't be published to external servers or downloadable via ODK Briefcase.      

.. _aggregate-remove-form-submissions:
  
Removing form submissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
To remove a form submission, select the form in the :guilabel:`Form` dropdown and click on :guilabel:`Purge Submission Data`.

.. _incomplete-form-submissions:

Incomplete form submissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see a list of incomplete submissions for a particular form under the :guilabel:`Incomplete Submissions` list.



