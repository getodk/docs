******************************
ODK Collect with Google Drive 
******************************

.. _odk-gdrive-intro:

Google Spreadsheet as a ODK Collect Data Container
===================================================
Google spreadsheet is an excel-like program associated with your Google account, and it can be integrated with ODK Collect to store survey submissions. Unlike server-based aggregate, Google sheet is accessible and free.
This guide is adapted `from <https://www.google.com/earth/outreach/tutorials/odkcollect_drive.html>`_, and it gives instructions on connecting ODK Collect application to Google Drive.

ODK has three main processes illustrated below:

.. image:: img/odk-general.png


The following table shows pros and cons of Google Drive with ODK Collect.

+------------------------------+----------------------------------+
| Pros                         | Cons                             |
+==============================+==================================+
| Allow Grouping questions.    | No repeat of questions.          |
+------------------------------+----------------------------------+
| Support pictures.            | Maximum of 254 variables.        |
+------------------------------+----------------------------------+
| Support all XLSForm features.| No Support to Audio and video.   |
+------------------------------+----------------------------------+

.. _odk-google-prerequisite:

Before You Start:
------------------

- Know how to use :ref:`Build ODK forms <intro-odk-build>`.
- Install :ref:`ODK Collect app <installing-collect>` on mobile.
- Create a `Google account <https://www.gcflearnfree.org/googleaccount/creating-a-google-account/1/>`_.

.. _odk-google-prepare:

Prepare Google Spreadsheet
---------------------------
1. Create a new `Google spreadsheet <https://gsuite.google.com/learning-center/products/sheets/get-started/>`_ (this file will be used to store submissions of your survey).
2. Give a good name to the sheet without adding content.
3. Change the `spreadsheet permission <https://www.gcflearnfree.org/googlespreadsheets/sharing-and-collaborating/1/>`_ , allow share and edit.
4. Keep this sheet opened for further use.


.. _odk-google-form-desigin:

Design Survey Form
-------------------

5. :ref:`Build your survey form <intro-odk-build>`.
6. Save the form as XLSForm.
7. Open the XLSForm in excel and move to the ``Settings`` tab (this is created by the Build tool you used).
8. Copy the sheet URL you created in step 1, and paste it under ``submission_url`` column in the form.
9. Save the form as `.xlsx` in excel.
10. Convert the XLSForm into XML format( ODK Collect app reads XML and visualizes its content), use the online ODK `XLSForm converter <http://opendatakit.org/xiframe/>`_ .
11. Download the XML file into your local computer, then upload it to your google account ( for organization, put ODK files in a new directory).
12. You can view your form in ODK Collect app by :ref:`setting the server as google drive <connecting-to-google>`, it will sync with your Google Drive account. Search for the name of the directory you chose in step 11 and locate select your XML file.
13. Distribute the XML among target participants.


.. _odk-google-data-view:

Survey Submission View
-----------------------

To view the collected data, open your submission sheet in google drive (named in step 2). 

