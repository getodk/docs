Installing ODK-X Scan
=======================

.. _odk-x-scan-prereqs:

Prerequisites
-------------------

Before installing ODK-X Scan, you will need the following ODK-X Tools:

  - :doc:`services-using`
  - :doc:`survey-using`
  - :doc:`tables-using`

As well as the `Files by Google <https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.files&hl=en&gl=US>`_ app.

.. _odk-x-scan-install:

Installing Scan
-----------------------

.. warning::

  ODK-X Scan is only compatible with Android versions 4.4 or newer.

To install the apk:

  1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

    - Make sure *Unknown Sources* is checked.
    - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

  2. Open a web browser on your phone.
  3. Navigate to https://github.com/odk-x/scan/releases/latest and download the ODK-X Scan APK.
  4. In the download window, you will see ODK_Scan.N.N.apk. - Select it to download the file.

    - On older devices, the APK will automatically install after you approve the security settings.
    - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::
  You can also `download the ODK-X Scan APK <https://github.com/odk-x/scan/releases/latest>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. note::
  To synchronize your data with the cloud you will also need :doc:`cloud-endpoints-intro`.

.. note::
  Before scanning you'll first need to create printable form template using the :doc:`scan-form-designer-intro`.
