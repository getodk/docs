Installing ODK Tables
===========================

.. _tables-install:

.. _tables-install-prereqs:

Prerequisites
--------------------------------------

.. _tables-install-required:

Required
~~~~~~~~~~~~~~~

Before installing ODK Tables, you will need the following ODK Tools:

  - :doc:`services-intro`

As well as the following third party apps:

  - `OI File Manager <https://play.google.com/store/apps/details?id=org.openintents.filemanager>`_

.. _tables-install-recommended:

Recommended
~~~~~~~~~~~~~~~

We also recommend installing:

  - :doc:`survey-intro`

ODK Survey is not required, but Tables and Survey are most versatile when used together. Survey offers a simple, form based data collected workflow similar to ODK Collect that can be seamlessly integrated with Tables to create and modify records.

.. _tables-install-app:

Installing the ODK Tables App
-----------------------------------


  1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

    - Make sure *Unknown Sources* is checked.
    - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

  2. Open a web browser on your phone.
  3. Navigate to http://opendatakit-dev.cs.washington.edu/2_0_tools/download and download the latest ODK Tables APK.
  4. In the download window, you will see ODK_Tables.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the ODK Tables APK <https://opendatakit-dev.cs.washington.edu/2_0_tools/download/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. tip::

  You can also `install ODK Tables on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and is only recommended for developers actively working on Tables.

