Installing the ODK Tables Sample Application
===============================================

.. _tables-sample-app:

.. _tables-sample-app-install:

Install the Sample Application
---------------------------------

We have provided a sample application to help you acquaint yourself with the various features. This sample app contains five demo apps within it.

Unlike ODK Collect, the ODK 2.0 tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as are the sample applications provided for :doc:`survey-intro` :doc:`services-intro`. This means that you can only deploy one of these sample application at a time onto a device. Later, we will explain how to rename one of these so that two or more applications can co-exist and not interfere with each other on this same device (this will require setting up an :doc:`cloud-endpoints-intro` for that renamed application; each Endpoint can host only one application at a time and must be configured with the application name that it will host).

.. _tables-sample-app-overview:

Five Demo Apps
~~~~~~~~~~~~~~~~~~~~~

This sample application consists of 5 separate demo apps:

  - **Tea Houses** - a fictional Benin Teahouse directory.
  - **Hope Study** - a simplified subset of a perinatal follow-up application that was piloted on ODK Tables and ODK Collect (now converted to use ODK Survey).
  - **Plot** - a fictional agricultural field pest- and yield- assessment application.
  - **Geotagger** - a simple geotagging application.
  - **JGI** - an app used to track the daily behavior of chimpanzees.

We will use the ODK 2.0 synchronization mechanism to install this app. It is about 26 MB in size and takes a few minutes to download from the web.

.. warning::

  Using the sync mechanism will delete all the configuration files for any data tables not present on the server. If you have experimented with creating forms and pushing them to your device, when you sync to the server, the synchronization process will delete these extraneous forms from your device and leave only the forms and files defined on the server.

To access this sample application and its 5 demo apps,

  1. Launch ODK Tables.
  2. Click on the sync icon (2 curved arrows) to launch ODK Services directly into the sync activity.
  3. From the menu, choose :menuselection:`Settings --> Server Settings`. You may be presented with a pop-up warning you that there are changes on your device that have not been sync'd to your server. Since you are setting up this demonstration application for the first time, you can choose :guilabel:`Ignore Unsynced Changes`.
  4. Choose :guilabel:`Server URL` and specify https://opendatakit-tablesdemo.appspot.com as the server URL (note that this URL begins with https:// ).
  5. Because this server allows anonymous access, the :guilabel:`Server Sign-on Credential` should be set to: :menuselection:`None (anonymous access)`. Other options are :menuselection:`Username and Google Account`. When setting up your own server, the ODK Sync Endpoint only supports Username. ODK Aggregate supports both Username and Google Account.
  6. Exit out of the :menuselection:`Server Settings` page, and then the :menuselection:`Settings` page, by using the back button.  During this process, if you had chosen a :guilabel:`Server Sign-on Credential` other than :menuselection:`None`, you will be prompted to authenticate that user.

  .. warning::

    If you decline (by choosing to :guilabel:`Log Out`), or if your credential is rejected by the server, then your credential will be reset to the anonymous (unprivileged) user.

  7. Confirm that the Server URL matches that set up above. From this point forward, whenever you initiate a sync, you do not need to visit the :menuselection:`Settings` page, but can perform the sync entirely from this screen.
  8. The sync interaction has four options:

    - :menuselection:`Fully Sync Attachments` - *Default* - Synchronize all row-level data and file attachments with the server.
    - :menuselection:`Upload Attachments Only` - Only upload attachments from the device to the server
    - :menuselection:`Download Attachments Only` - Only download attachments from the server to the device
    - :menuselection:`Do Not Sync Attachments` -  Do not sync any attachments

  8. Click on :guilabel:`Sync Now`.

The sync process will now begin. If you have selected to use a Google Account, you may be challenged to authorize access to your Google account information. Otherwise, the sync will begin and a progress dialog will appear. As stated above, this synchronization mechanism forces the configuration of the device to exactly match that of the server. Any local configuration files for data tables or forms that are not present on the server will be removed from your device (i.e., everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server).

.. note::

  As a safeguard to prevent data loss, data tables that are only defined on the device will not be deleted. However, because their associated configuration files will have been removed, they are generally inaccessible until you restore their configuration files and their forms onto the device.

Once the configuration of the device is an exact match to that of the server, the data within the data tables are synchronized. And, finally, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful; the system stops at the first timeout and does not attempt any retries.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the ODK Services application, returning to ODK Tables. ODK Tables should now present a custom home screen with five tabs, one for each of the demos. If it does not, back out of ODK Tables and re-launch it.

Select a tab (demo application), then click the :guilabel:`Launch Demo` button to enter that sample application.

.. _tables-sample-app-layout:

Layout of Application Files
-------------------------------------

The layout of this sample app is as follows:

  - :file:`/sdcard/opendatakit`-- directory containing all ODK 2.0 applications. Each application is a sub-directory within this directory.
  - :file:`/sdcard/opendatakit/default` -- default application name (directory) for the ODK 2.0 tools

Within the application folder (:file:`/sdcard/opendatakit/default`), the following directories are present:

  - :file:`config` -- contains read-only configuration files that define the user's application (for example, the 5demos example application you just synced from https://opendatakit-tablesdemo.appspot.com). Within this folder are:

      - :file:`assets` -- contains files that initialize your data tables (in the csv sub-folder) and define the custom home screen and provides CSS files for overall appearance of your app, and JavaScript libraries and files for common behaviors in your app.
      - :file:`tables` -- contains directories that are named with table ids. Within these sub-directories, the ODK Survey forms and table-specific HTML, JavaScript, and CSS files are found. For example, the HTML file describing the list view for the tea houses table is found in :file:`config/tables/Tea_houses/html/Tea_houses_list.html`.

  - :file:`data` -- contains the database and row-level attachments (files).
  - :file:`output` -- contains files that are generated (such as detailed logging files) or exported (such as CSV files) by the ODK tools on the device.
  - :file:`system` -- an area maintained by the tools themselves (ODK Survey, ODK Tables, ODK Scan, and so on). These files are extracted and placed here by the APKs. You should not modify files in this folder; when first started, the ODK tools sweep this directory to verify that these files match their internal copy. Any deviant file is replaced with a fresh internal copy.

The automatic configuring and loading of data into ODK Tables is governed by the :file:`config/assets/tables.init` file. It provides a list of table ids and the CSV files (located in the :file:`config/assets/csv` folder) that should be imported to populate them. This is discussed in more detail in the :ref:`Tables User Guide <tables-using-config-at-startup>`.

.. note::

  This file is the only configuration file that is not synced to the server. This is to optimize start-up of your application on other devices; once this initial data has been loaded into your data tables and synced to the server, the other devices will obtain the data through an ordinary sync action.

.. note::

  This file is scanned once. If the import(s) fail, it could leave some tables partially initialized. The file will be re-processed and data rows re-loaded by clicking on :menuselection:`Reset Configuration` on the :guilabel:`Settings` screen then exiting the ODK Tools and re-launching them. Upon being re-launched, the file will be scanned and processed.

Most of the app-level settings that are configured through the :menuselection:`Settings` page are stored in the :file:`config/assets/app.properties` file. Excluded from this file are the :guilabel:`Server Sign-On Credential type`, and the values for that credential (such as username and password). This allows the application designer to specify and enforce most of the app-level settings (such as the server used when syncing) via the sync mechanism.
