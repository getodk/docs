Installing Collect
====================

.. _install-collect-from-google-play:

Install from Google Play Store (**Recommended**)
----------------------------------------------------

`The ODK Collect App is available in the Google Play store <https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_.


Install Manually
-------------------

The Google Play store always has the latest stable release.

If you need a different version of Collect, you can download from the web and install manually.

1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

   - Make sure *Unknown Sources* is checked.
   - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

2. Open a web browser on your phone.
3. Navigate to https://opendatakit.org/downloads/download-category/collect/  and download the ODK Collect APK.
4. In the download window, you will see ODK_Collect_vN.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::
  
  You can also `download the ODK Collect APK <https://opendatakit.org/downloads/download-category/collect/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. note::

  On older Android devices (4.0 and earlier), ODK Collect required an external SD Card. This is no longer an issue because Android devices have internal storage. Virtually all current Android devices will run ODK Collect.

.. tip::

  You can also `install ODK Collect on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and is only recommended for developers actively working on Collect.

