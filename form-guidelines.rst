******************
Form Guidelines
******************

.. note::

  This page is a reference guide for users who edit the raw XML in ODK forms. If you use the XLSForm form designer, see http://xlsform.org for form design help.

This document gathers the set of guidelines for creating your own forms. These range from naming suggestions to feature and performance considerations.

.. form-id-guidelines:

Form ID Guidelines
===================

Open Data Kit depends upon the presence of either the ``id`` attribte (preferred) or the "xmlns" (deprecated) on the tag within the Xform's ``<instance>`` tag to uniquely identify the form. Filled-in forms, when finalized by ODK Collect, contain this ``id`` attribute. When these are submitted to the server (e.g., ODK Aggregate), it extracts the form id and retrieves the corresponding, previously-uploaded, form definition. Using that form definition, the server can then extract the data values from the submission and store them in the appropriate data tables.

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

.. group-and-fieldname-guidelines:

Group and Fieldname Guidelines
================================

Answers to your survey questions are identified by their field names within your form. In ODK Build, the Data Name property specifies the field name. In an XLSForm spreadsheet, the name column specifies the field name. Question groupings also have names, and these guidelines also apply to their names.

Field names appear as the column headers in the Submissions tab in ODK Aggregate. If they are nested within a group, the group name and field name (space-separated) appear as the column header. In the exported CSV file, the group name and field name are concatenated with colon separators (:). Because group names and field names are displayed to the data analyst and/or end user, they should be meaningful.

The structure of the data you send is defined in the ``<instance/>`` section of the XForm. An example, with field names: :guilabel:`name`, :guilabel:`age` and :guilabel:`date`, is shown here:

.. code-block:: html

  <model>
      <instance>
        <data id="sampleForm">
          <name/>
          <age/>
          <date/>
        </data>
      </instance>
      ...
  </model>

An example transmission from ODK Collect of a filled-in form with this structure is shown below (new-line inserted for readability):

.. code-block:: xml

  <?xml version='1.0' ?><data id="sampleForm"><name>John Smith</name><age>23</age>
  <date>2010-09-17T22:16:16.536</date></data>

Even with short field names, around 50% of the size of the message is consumed by the field names. The more grouped and deeply nested your form is, the more space will be consumed by the names of these groups and their nesting. If you are gathering text-only data, and pay for the amount of data you transmit, you should strive to use the shortest possible meaningful field names. But, again, for downstream usability, we strongly recommend meaningful names (e.g., "age" is easier to comprehend than "q2").

All these message size concerns are insignificant if you are transmitting captured audio, image, or video clips. In that case, the size of the captured images, audio or video will be several orders of magnitude greater than the size of any textual form data you might collect.

Finally, within ODK Aggregate, the field and group names are mapped to the specific columns or tables in which the data for those fields (or groups of nested fields) are stored. Most persistence mechanisms, and particularly databases like MySQL, restrict the lengths of their column and table names to fewer than 64 characters. Aggregate will compact your field names to fit within those limits and use those compacted names as the column and table names in the datastore. The compacted names of deeply nested fields or fields with long field names may be awkwardly cryptic if you are accessing the datastore (e.g., MySQL) directly.

Compacted names are formed by prefixing the name(s) of the groups in which the field is nested to the field's name, each separated by a ``_`` character. All lower case characters are then capitalized and an ``_`` character is inserted at word breaks; non-alphanumeric characters are also replaced with ``_`` characters. The group prefix is then compacted to consume no more than 1/3 of the column name allowed by the datastore; the field name is compacted to fit the remaining space.

Thus, ``thisFormField`` and ``this-form-field`` will both become ``THIS_FORM_FIELD``, as would a field named Field nested within a thisForm group. Any overlaps of the resulting column names within a single database table are prevented through additional processing steps. In light of these processing steps, it is recommended that field names:

- be short (ideally < 30 characters).
- must be unique within their enclosing group within the form (this is required by Xml and Javarosa).
- cannot contain any spaces.
- should contain only alphanumeric characters and the characters ``_`` and ``-``.
- should start with a letter.
- should all consistently follow either the camel-case convention (e.g., thisFormField) with leading capitals denoting word breaks within the field name, or use either the ``_`` or ``-`` characters to mark word breaks (e.g., this-form-field).
- should not have two or more fields that are distinguished only by either their capitalization, use of dashes, or use of underscores. E.g., a form that contains two or more of these field names will be confusing: ``thisFormField``, ``this-form-field``, ``thisformfield`` or ``this_formField``.

.. note::

  Underscores and dashes within the field name (not the compacted name) may limit or complicate the publish-ability of the form to other systems such as Google Spreadsheet or Google Fusion Tables. If you want to use them, please verify that the data can be published to those systems.

.. _select-values:

Select values
==============

The underlying values defined with ``<value>`` tag for select clauses should follow the same naming as the field names, above. In particular, these values should not contain embedded spaces, as the parsing at the server will split the strings at the spaces, causing "my value" to be stored on the server as two selection values "my" and "value".





