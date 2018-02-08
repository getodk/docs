Setting Up ODK Services
==============================

.. _services-setup-install:

Installing ODK Services
--------------------------------

  1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

    - Make sure *Unknown Sources* is checked.
    - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

  2. Open a web browser on your phone.
  3. Navigate to http://opendatakit-dev.cs.washington.edu/2_0_tools/download and download the latest ODK Services APK.
  4. In the download window, you will see ODK_Services_vN.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the ODK Services APK <https://opendatakit-dev.cs.washington.edu/2_0_tools/download/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. tip::

  You can also `install ODK Services on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and is only recommended for developers actively working on Services.

.. _services-setup-servers:

Compatible Servers
-------------------------

The latest version of ODK Services is Version 2.0.2 (December 2017).

To synchronize data with the latest version of ODK Services (rev218) requires a rev 218, 216 or 214 :doc:`cloud-endpoints-intro`. ODK Aggregate v1.4.15 or Sync Endpoint 2.0.2 rev 218 will work. It will not work with earlier versions of ODK Aggregate. See :doc:`sync-endpoint` or :doc:`aggregate-tables-extension` for further information on how to configure the server to accept ODK 2.0 synchronization requests.
