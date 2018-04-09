Installing the Sample Application
====================================

.. _survey-sample-app-install:

Unlike ODK Collect, the ODK 2 tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as is the sample applications provided for :doc:`tables-intro`. This means that you can only deploy one of these sample application at a time onto a device. We also provide :ref:`instructions <survey-launching-appname>` to rename one of these so that two or more applications can co-exist and not interfere with each other on this same device.

To access the sample application and its six sample forms:

  1. Launch ODK Survey. Press the :guilabel:`Settings` button that resembles a gear. This will launch the ODK Services tool to the settings page.

    .. image:: /img/survey-sample-app/survey-settings-button.*
      :alt: Survey Setting Button
      :class: device-screen-vertical

  2. Follow the :ref:`services-managing-server-config` instructions to set up your server.

    - Set your :guilabel:`Server URL` to :file:`https://opendatakit-2.appspot.com`.

      .. note::

        The server URL starts with :file:`https://` not :file:`http://`. Don't forget to include the *s*.

    - Leave your authentication as :guilabel:`None (anonymous access)`.

  3. Back out until you return to Survey.
  4. Follow the :ref:`services-using-sync` instructions (see :ref:`launching from Survey <services-using-sync-launch-other>`).

    - Again, leave your user as :menuselection:`None (anonymous access)`.
    - Leave the file attachment setting to :menuselection:`Fully Sync Attachments`

After synchronization is complete, your device's configuration will exactly match that of the server. This includes both collected data and application level files (such as form definitions and HTML files). If you had nothing on your device before, your device will be populated with this data and these application files. If you already had files on this device in this application namespace they will be updated to match the server version. Any local configuration files for data tables or forms that are not present on the server will be removed from your device. Everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server.

Once the configuration and data on the device is an exact match to that of the server, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful. This will not overwrite or hurt anything to do multiple synchronizations in a row.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the Services, returning to Survey.

If the sync was successful, ODK Survey will scan through the downloaded configuration, updating its list of available forms.

  .. image:: /img/survey-sample-app/survey-scanning.*
    :alt: Survey Scanning Form Definitions
    :class: device-screen-vertical

When that is completed you should now be presented with the list of those six sample forms.

.. _survey-sample-app-installing-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~

For instructions on installing your own Survey application to a device, view the :ref:`build-app-move-to-device` guide.

