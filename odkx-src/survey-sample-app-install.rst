Installing the Sample Application
====================================

Prerequisites
---------------

Install ODK-X Survey and its prerequisites from the guide :doc:`basics-install`.

.. _survey-sample-app-install:

Unlike ODK Collect, the ODK-X tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as are the sample applications provided for :doc:`tables-intro`. This means that you can only deploy one of these sample applications onto a device at a time. We also provide :ref:`instructions <survey-launching-appname>` to rename one of these so that two or more applications can co-exist on the same device without interfering with each other.

To access the sample application and its six sample forms:

  1. Launch ODK-X Survey. Press the :guilabel:`Settings` button that resembles a gear. This will launch the ODK-X Services tool to the settings page.

    .. image:: /img/survey-sample-app/survey-settings-button.*
      :alt: Survey Setting Button
      :class: device-screen-vertical

  2. Select :guilabel:`Server Settings` (more info on setting up your server can be found here: :ref:`services-managing-server-config`)

    - Set your :guilabel:`Server URL` to :file:`https://demo2.odk-x.com`.

      .. note::

        The server URL starts with :file:`https://` not :file:`http://`. Don't forget to include the *s*.

    - Click on Server Sign-on Credential and change your authentication from  :guilabel:`None (anonymous access)` to :guilabel:`Username`. Then, click Username, and enter :menuselection:`demo_user1` in the space. Also change your server password to :menuselection:`password`. When you are done, your screen should look like this:

  .. image:: /img/survey-sample-app/survey-demo-server-credential.*
    :alt: Server Sign-on Credential
    :class: device-screen-vertical

  3. Back out and click :guilabel:`Authenticate New User` in the popup window. On the resulting page, press :guilabel:`Verify User Permissions` and click :guilabel:`OK` on the message stating that the verification was successful. Back out until you return to Survey.

  4. Press the Sync button as shown below.

  .. image:: /img/survey-sample-app/survey-demo-sync.*
    :alt: Launching Sync from Survey
    :class: device-screen-vertical

5. Once this launches ODK-X Services, click the :guilabel:`Sync Now` button.
    - Again, leave your user as :menuselection:`demo_user1`.
    - Leave the file attachment setting to :menuselection:`Fully Sync Attachments`

 .. image:: /img/survey-sample-app/survey-demo-services-sync.*
    :alt: Syncing from the demo server
    :class: device-screen-vertical

After synchronization is complete, your device's configuration will exactly match that of the server. This includes both collected data and application level files (such as form definitions and HTML files). If you had nothing on your device before, your device will be populated with this data and these application files. If you already had files on this device in this application namespace they will be updated to match the server version. Any local configuration files for data tables or forms that are not present on the server will be removed from your device. Everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server.

Once the configuration and data on the device is an exact match to that of the server, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful. It will not overwrite or hurt anything to do multiple synchronizations in a row.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the Services, returning to Survey.

If the sync was successful, ODK-X Survey will scan through the downloaded configuration, updating its list of available forms.

  .. image:: /img/survey-sample-app/survey-scanning.*
    :alt: Survey Scanning Form Definitions
    :class: device-screen-vertical

When that is completed you should now be presented with the list of those six sample forms.

.. _survey-sample-app-installing-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~

For instructions on installing your own Survey application to a device, view the :ref:`build-app-move-to-device` guide.
