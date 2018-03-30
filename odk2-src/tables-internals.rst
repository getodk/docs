ODK Tables: Internal Details
==============================

.. _tables-internal-details:

.. _tables-app-layout-details:

Layout of Application Files
-------------------------------------

The layout of a Data Management Application is as follows:

  - :file:`/sdcard/opendatakit`-- directory containing all ODK 2 applications. Each application is a sub-directory within this directory.
  - :file:`/sdcard/opendatakit/default` -- default application name (directory) for the ODK 2 tools

Within the application folder (:file:`/sdcard/opendatakit/default`), the following directories are present:

  - :file:`config` -- contains read-only configuration files that define the user's application (for example, the 5demos example application you just synced from https://opendatakit-tablesdemo.appspot.com). Within this folder are:

      - :file:`assets` -- contains files that initialize your data tables (in the csv sub-folder) and define the custom home screen and provides CSS files for overall appearance of your app, and JavaScript libraries and files for common behaviors in your app.
      - :file:`tables` -- contains directories that are named with table ids. Within these sub-directories, the ODK Survey forms and table-specific HTML, JavaScript, and CSS files are found. For example, the HTML file describing the list view for the tea houses table is found in :file:`config/tables/Tea_houses/html/Tea_houses_list.html`.

  - :file:`data` -- contains the database and row-level attachments (files).
  - :file:`output` -- contains files that are generated (such as detailed logging files) or exported (such as CSV files) by the ODK tools on the device.
  - :file:`system` -- an area maintained by the tools themselves (ODK Survey, ODK Tables, ODK Scan, and so on). These files are extracted and placed here by the APKs. You should not modify files in this folder; when first started, the ODK tools sweep this directory to verify that these files match their internal copy. Any deviant file is replaced with a fresh internal copy.

The automatic configuring and loading of data into ODK Tables is governed by the :file:`config/assets/tables.init` file. It provides a list of table ids and the CSV files (located in the :file:`config/assets/csv` folder) that should be imported to populate them. This is discussed in more detail in the :ref:`Tables User Guide <tables-managing-config-at-startup>`.

.. note::

  This file is the only configuration file that is not synced to the server. This is to optimize start-up of your application on other devices; once this initial data has been loaded into your data tables and synced to the server, the other devices will obtain the data through an ordinary sync action.

.. note::

  This file is scanned once. If the import(s) fail, it could leave some tables partially initialized. The file will be re-processed and data rows re-loaded by clicking on :menuselection:`Reset Configuration` on the :guilabel:`Settings` screen then exiting the ODK Tools and re-launching them. Upon being re-launched, the file will be scanned and processed.

Most of the app-level settings that are configured through the :menuselection:`Settings` page are stored in the :file:`config/assets/app.properties` file. Excluded from this file are the :guilabel:`Server Sign-On Credential type`, and the values for that credential (such as username and password). This allows the application designer to specify and enforce most of the app-level settings (such as the server used when syncing) via the sync mechanism.
