Installing the Sample Application
====================================

Prerequisites
---------------

Install `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ and its prerequisites from the guide :doc:`basics-install`.

.. _survey-sample-app-install:

Unlike ODK Collect, the ODK-X tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as are the sample applications provided for :doc:`tables-using`. This means that you can only deploy one of these sample applications onto a device at a time. We also provide :ref:`instructions <survey-launching-appname>` to rename one of these so that two or more applications can co-exist on the same device without interfering with each other.

To access the sample application and its six sample forms, authentication and syncing are required.

  1. Launch `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_. Tap the :guilabel:`Settings` button represented by a gear. This launches the ODK-X Services tool to the settings page.

    .. image:: /img/survey-sample-app/survey-settings-button.*
      :alt: Survey Setting Button
      :class: device-screen-vertical

  2. Select :guilabel:`Server Settings` (more info on setting up your server can be found here: :ref:`services-managing-server-config`)

    .. image:: /img/survey-sample-app/survey-server-settings.*
      :alt: Server Settings Button
      :class: device-screen-verticalsurvey

    - Set your :guilabel:`Server URL` to :file:`https://survey-demo.odk-x.org`.

      .. image:: /img/survey-sample-app/survey-server-url.*
        :alt: Server Url Setting
        :class: device-screen-verticalsurvey

      .. note::

        The server URL starts with :file:`https://` not :file:`http://`. Don't forget to include the *s*.

    - Tap Server Sign-on Credential and change your authentication from  :guilabel:`None (anonymous access)` to :guilabel:`Username`. 
    
      .. image:: /img/survey-sample-app/survey-signon-credential.*
        :alt: Server Sign-on Credential
        :class: device-screen-verticalsurvey
    
    - Next, tap Username and enter :menuselection:`demo_user1` in the space. 
    
      .. image:: /img/survey-sample-app/survey-username-settings.*
        :alt: Username settings
        :class: device-screen-verticalsurvey
    
    - Change your server password to :menuselection:`password`. 

      .. image:: /img/survey-sample-app/survey-password-settings.*
        :alt: Password settings
        :class: device-screen-verticalsurvey
   
    - When you are done, your screen should look like this:

      .. image:: /img/survey-sample-app/survey-demo-server-credential.*
        :alt: Final settings picture
        :class: device-screen-vertical

      .. tip::

        You can also :ref:`login by scanning a QR code.<services-login-with-qr>`
          
  3. Tap your device's back button and choose the :guilabel:`Authenticate New User` option in the popup window. On the resulting page, tap the :guilabel:`Verify User Permissions` button. If successfully authenticated, you should see a popup window with a message stating that the verification was successful. 

    .. image:: /img/survey-sample-app/survey-successful-authentication.*
      :alt: Successful authentication
      :class: device-screen-vertical

    Tap :guilabel:`OK` on the window and go back to the `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ application.

  4. Tap the Sync button at the top of the screen.

  .. image:: /img/survey-sample-app/survey-demo-sync.*
    :alt: Launching Sync from Survey
    :class: device-screen-vertical

5. Once this launches ODK-X Services, click the :guilabel:`Sync Now` button.
    - Again, leave your user as :menuselection:`demo_user1`.
    - Leave the file attachment setting as the default :menuselection:`Fully Sync Attachments`

   .. image:: /img/survey-sample-app/survey-demo-services-sync.*
    :alt: Syncing from the demo server
    :class: device-screen-vertical

   Synchronization might take a while.
  
After synchronization is complete, your device's configuration will exactly match that of the server. This includes both collected data and application level files (such as form definitions and HTML files). If you had nothing on your device before, your device will be populated with this data and these application files. If you already had files on this device in this application namespace they will be updated to match the server version. Any local configuration files for data tables or forms that are not present on the server will be removed from your device. Everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server.

Once the configuration and data on the device is an exact match to that of the server, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful. It will not overwrite or hurt anything to do multiple synchronizations in a row.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the Services, returning to Survey.

 .. image:: /img/survey-sample-app/survey-sync-success.*
   :alt: Sync success
   :class: device-screen-vertical

If the sync was successful, `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ will scan through the downloaded configuration, updating its list of available forms.

  .. image:: /img/survey-sample-app/survey-scanning.*
    :alt: Survey Scanning Form Definitions
    :class: device-screen-vertical

When that is completed you should now be presented with the list of those six sample forms.

.. _survey-sample-app-installing-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~

For instructions on installing your own Survey application to a device, view the :ref:`build-app-move-to-device` guide.
