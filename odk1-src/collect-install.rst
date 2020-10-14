Installing Collect
====================

.. _install-collect-from-google-play:

Installing from Google Play Store (recommended)
----------------------------------------------------

ODK Collect is available in the `Google Play Store <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_.


.. _install-collect-manually:

Installing manually
-------------------

The Google Play Store always has the latest stable release. 

If you need a different version of Collect, you can download from the web and install manually.

1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

   - Make sure *Unknown Sources* is checked.
   - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

2. Open a web browser on your phone.
3. Navigate to https://github.com/getodk/collect/releases/latest and download the ODK Collect APK.
4. In the download window, you will see ODK_Collect_vN.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::
  
  You can also `download the ODK Collect APK <https://github.com/getodk/collect/releases/latest>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. note::

  On older Android devices (4.0 and earlier), ODK Collect required an external SD Card. This is no longer an issue because Android devices have internal storage. Virtually all current Android devices will run ODK Collect.

.. tip::

  You can install ODK Collect on the `Android emulator <https://developer.android.com/studio/run/emulator>`_. This is especially helpful if you need to :doc:`project Collect onto a screen <projecting-collect>`.

.. _collect-permissions:

Understanding permissions
-------------------------

The ODK Collect application requires permissions to access device resources. 

If your device runs a version of Android below 6, you will be prompted to accept all of the permissions on app install. 

If your device runs Android 6 or above, permissions will be requested as they are needed. For example, the camera permission will only be requested the first time that you try to take a picture. Once the permission is granted, you won't be prompted again. If you deny the permission, you will be asked again the next time you try to access the feature that requires the permission unless you check "Don't ask me again." If you deny the permission, you will be shown a dialog explaining why the permission is needed.

The only permission that is required for using Collect is the storage permission and it will be requested on first launch on Android 6+. Other permissions may or may not be needed depending on the forms and features used. The permissions that may be requested by Collect are:

+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Permission |                                                             Reason                                                                |
+============+===================================================================================================================================+
| Storage    | required for Collect to be able to access and save form data                                                                      |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Camera     | required by :ref:`image <image-widgets>` and :ref:`video <video>` questions to capture new media                                  |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Contacts   | required to configure a Google account for Google Drive, Google Sheets submissions                                                |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Location   | required for :ref:`location <location-widgets>` questions                                                                         |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Microphone | required by :ref:`audio <audio>` and :ref:`video <video>` questions to capture new media                                          |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Phone      | optional on form send to include deviceID in the submission and required for forms that capture :ref:`device metadata <metadata>` |
+------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. | SMS        | required to send :doc:`SMS submissions <collect-sms-submissions>`                                                                 |
.. +------------+-----------------------------------------------------------------------------------------------------------------------------------+

Changing permissions from settings in Android 6+
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are setting up Collect for someone who is not familiar with Android, you may want to make sure all required permissions are granted in advance. To do this, open the Settings application and tap on the Apps heading. You should now see a list of all your installed applications. Scroll down to find ODK Collect and tap on it to see details about Collect. Tap on the Permissions heading. You can now grant all of the permissions that will be needed.

You can also use Settings application to grant a permission after denying it or to revoke a previously-granted permission.
