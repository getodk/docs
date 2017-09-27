******************
Form Guidelines
******************

.. note::

  This page is a reference guide for users who edit the raw XML in ODK forms. If you use the XLSForm form designer, see http://xlsform.org for form design help.

This document gathers the set of guidelines for creating your own forms. These range from naming suggestions to feature and performance considerations.

.. form-id-guidelines:

Form ID Guidelines
===================

Open Data Kit depends upon the presence of either the ``id`` attribte (preferred) or the "xmlns" (deprecated) on the tag within the Xform's ``<instance>`` tag to uniquely identify the form. Filled-in forms, when finalized by ODK Collect, contain this ``id``attribute. When these are submitted to the server (e.g., ODK Aggregate), it extracts the form id and retrieves the corresponding, previously-uploaded, form definition. Using that form definition, the server can then extract the data values from the submission and store them in the appropriate data tables.

Within ODK Aggregate, the Form ID is used in the persistence layer as a prefix for the names of the tables into which your form data is stored. Most persistence mechanisms, and particularly databases like MySQL, restrict the lengths of their column and table names to fewer than 64 characters. For this reasion, it is recommended:

- the form ID should be short (ideally < 10 characters).
- the form ID should be unique within your organization.
- the form ID must not contain any spaces or punctuation characters.
- the form ID should contain only alphanumeric characters and the characters ``_`` and ``-``.
- the form ID should start with a letter.
- it may be useful to add a revision designation to the form ID (e.g, "medinfo-01") to aid in tracking major revisions to your forms.
- a separate version setting is used for revisions that do not change the data being collected or their data types. These 'minor' revisions include adding language translations, correcting spelling errors within the text, changing external dataset files, and updating multi-media prompts. E.g., changing the media files used in audio, image or video labels (prompts). Using the version setting enables form definitions to be enhanced mid-survey while allowing all of the older and newer submissions to be stored in the same data table on the ODK Aggregate server. The version of the form definition used is retained in the meta-data of each individual submission so that it is available during data analysis.

.. note::
 
  Underscores and dashes may limit or complicate the publish-ability of the form to other systems such as Google Spreadsheet or Google Fusion Tables. If you want to use these, please verify that the data can be published to those systems.

**Once a form is uploaded to ODK Aggregate, the number of questions or the type of question cannot be changed.** You either have to delete the form from the datastore (deleting all of its submissions) or change the id or xmlns attribute to re-upload the form (in which case it will be treated as an entirely different form and can co-exist with the original). This is by design — it prevents you from changing the format of the data mid-data-collection (which could confound ODK Aggregate's ability to extract the data values submitted using the earlier versions of the form or create database problems). But, as noted above, other changes to the form definition are allowed through the use of the version setting. These two values that identify a form are specified on the XLSForm spreadheet's settings tab:

- **form_id**  -- must be changed when the data model changes (when you add or remove a prompt, or change a prompt from a string to an integer or decimal or multiple-choice value).
- **version**  -- must be a small 10-digit-or-less numeric string. We recommend using strings of the form: 'yyyymmddrr' e.g., 2018012901 (the 1st revision on January 29, 2018). Revised form definitions must have a version string that compares lexically (alphabetically) greater than the current form definition. I.e., ODK Aggregate does not accept changes to a form definition unless the version string is different and lexically (alphabetically) greater than the version string of the existing form definition (and the version string must be a 10-digit-or-less integer).

As mentioned above, if you leave the form_id unchanged, and change the version, then you can upload the new form XML to ODK Aggregate. The new form will replace the old one on ODK Aggregate (you will no longer be able to download the older form), and the new and old form submissions will be submitted into the same submissions table.  The version of the form used when the survey was finalized is available as metadata on each submission.
