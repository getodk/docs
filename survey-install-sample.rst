Installing the ODK Survey Sample Application
==============================================

.. _survey-sample-app:

.. _survey-sample-app-install:

Install the Sample Application
--------------------------------------

We have provided a sample application to help you acquaint yourself with the various features of ODK Survey. This sample app contains six sample forms within it.

Unlike ODK Collect, the ODK 2.0 tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as are the sample applications provided for :doc:`tables-intro` :doc:`services-intro`. This means that you can only deploy one of these sample application at a time onto a device. Later, we will explain how to rename one of these so that two or more applications can co-exist and not interfere with each other on this same device (this will require setting up an :doc:`cloud-endpoints-intro` for that renamed application; each Endpoint can host only one application at a time and must be configured with the application name that it will host).

.. _survey-sample-app-overview:

Six Sample Forms
~~~~~~~~~~~~~~~~~~~~~~~

A reference set of sample forms to start with are:

  - **Example Form** -- a form with many examples of data entry widgets.
  - **Grid Screen Form** -- a form used to demonstrate a new screen layout that allows fully-customized prompt placement.
  - **Household Survey** -- a form used to gather information about a household. To operate correctly, this requires the *Household Member Survey* sub-form and the *Education* sub-form (you should not open those sub-forms directly -- they are launched from within Household Survey).
  - **Select Examples** -- a form with several examples of select widgets, including widgets that access data on Yahoo servers, and others that access CSV files for their choice lists. It also demonstrates the use of custom CSS styles to change the look of the form.
  - **Household Member Survey** -- a form used to gather information about household members. This is a sub-form of the Household Survey form (you should not open it directly -- it is launched from within Household Survey). ODK Survey eliminates the repeat group concept and replaces it with sub-forms. From within the Household Survey you navigate into this sub-form by entering information about individuals in a household.
  - **Education** -- a form used to gather education information about household members. This is another sub-form of the Household Survey form (you should not open it directly -- it is launched from within Household Survey). This sub-form saves information to the same underlying data table (household_members) as the Household Member Survey form, but it asks different questions. This demonstrates the use of multiple forms to revise different sets of values within a data table. From within the Household Survey you navigate into this form when you enter education information about individuals in a household.

.. note::

  Since the *Education* and *Household Member Survey* operate on the same table, you will only see five tables in ODK Tables and in the Cloud Endpoint even though there are six forms.

To access the sample application and its six sample forms:

  1. Launch ODK Survey.
  2. Click on the sync icon (2 curved arrows) to launch ODK Services directly into the sync activity.
  3. From the menu, choose :menuselection:`Settings -> Server Settings`. You may be presented with a pop-up warning you that there are changes on your device that have not been sync'd to your server. Since you are setting up this demonstration application for the first time, you can choose :guilabel:`Ignore Unsynced Changes`.
  4. Choose Server URL and specify https://opendatakit-2.appspot.com as the server URL (note that this URL begins with https:// ).
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

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the ODK Services application, returning to ODK Survey.

If the sync was successful, ODK Survey will scan through the downloaded configuration, updating its list of available forms, and you should now be presented with the list of those six sample forms.
