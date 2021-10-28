Installing ODK-X Basic Tools
================================

These instructions describe the steps to install the ODK-X basic tools on a tablet.

.. _basic-prereqs:

Prerequisites
-------------------

You must have an Android tablet with an operating system version 5.0 or higher.

If you are working on a Windows/Mac/Linux machine, you can use `Android Studio <https://developer.android.com/studio>`_ to launch an Android emulator for testing purposes.

.. note::

  Please note that ODK-X Services version 2.1.7 doesn't work on Android 11. You will need Android 10 with an API level of less than 30 for version 2.1.7.

Before installing any of the ODK-X tools, you will need the following third-party app:

  - `OI File Manager <https://github.com/openintents/filemanager/releases>`_

Required
~~~~~~~~~~~~~~~

There are no other ODK-X Android tools that are prerequisites to installing :doc:`services-using`. However, ODK-X Services is a prerequisite for all the other ODK-X Android tools.

Recommended
~~~~~~~~~~~~~~~

We also recommend installing both :ref:``ODK-X Survey <https://docs.odk-x.org/survey-using/>`_<survey-using>` and :ref:`ODK-X Tables<tables-using>`. Having both is not required, but Tables and Survey are most versatile when used together. Tables offers a way to visualize, process, and modify data collected by Survey, all on the device. Survey offers a simple, form-based data collected workflow similar to ODK Collect that can be seamlessly integrated with Tables to create and modify records.

.. _services-install:


Installing Services
--------------------------------

  1. From your device's :guilabel:`Settings`, choose :menuselection:`Apps & notifications`. (On older versions of Android, this setting may be in :menuselection:`Applications` or :menuselection:`Security` depending upon your android version.)

    - Go to :guilabel:`Special app access` in :guilabel:`Advanced` and choose :guilabel:`Install unknown apps`
    - From the list of applications, select a browser of your choice and check :guilabel:`Allow from this source`.
    - (On older versions of Android, the above two steps are not required, make sure installation from *Unknown Sources* is checked.)

  2. Open the same web browser that you authorized to install unknown apps on your Android device. (For older versions of Android any web browser can be used since you do not need to specifically authorize the web browser's ability to install.)
  3. Navigate to https://github.com/odk-x/services/releases/latest and download the latest ODK-X Services APK.
  4. In the download window, you will see ODK_Services_vN.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the ODK-X Services APK <https://github.com/odk-x/services/releases/latest/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. tip::

  You can also `install ODK-X Services on an Android emulator <https://github.com/odk-x/tool-suite-X/wiki/Developer-Environment-Setup>`_. However, this can be slow and is only recommended for developers actively working on Services.

.. _survey-install:

Installing the `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ App
-----------------------------------

  1.  From your device's :guilabel:`Settings`, choose :menuselection:`Apps & notifications`. (On older versions of Android, this setting may be in :menuselection:`Applications` or :menuselection:`Security` depending upon your android version.)

    - Go to :guilabel:`Special app access` in :guilabel:`Advanced` and choose :guilabel:`Install unknown apps`
    - From the list of applications, select a browser of your choice and check :guilabel:`Allow from this source`.
    - (On older versions of Android, the above two steps are not required, ensure installation from *Unknown Sources* is checked.)
    
  2. Open the same web browser that you authorized to install unknown apps on your Android device. (For older versions of Android any web browser can be used since you do not need to specifically authorize the web browser's ability to install.)
  3. Navigate to https://github.com/odk-x/survey/releases/latest and download the latest `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ APK.
  4. In the download window, you will see ODK-X_Survey.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ APK <https://github.com/odk-x/survey/releases/latest>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. tip::

  You can also `install `ODK-X Survey <https://docs.odk-x.org/survey-using/>`_ on an Android emulator <https://github.com/odk-x/tool-suite-X/wiki/Developer-Environment-Setup>`_. However, this can be slow and is only recommended for developers actively working on Survey.


.. _tables-install:

Installing the ODK-X Tables App
-----------------------------------


  1.  From your device's :guilabel:`Settings`, choose :menuselection:`Apps & notifications`. (On older versions of Android, this setting may be in :menuselection:`Applications` or :menuselection:`Security` depending upon your android version.)

    - Go to :guilabel:`Special app access` in :guilabel:`Advanced` and choose :guilabel:`Install unknown apps`
    - From the list of applications, select a browser of your choice and check :guilabel:`Allow from this source`.
    - (On older versions of Android, the above two steps are not required, make sure installation from *Unknown Sources* is checked.)
    
  2. Open the same web browser that you authorized to install unknown apps on your Android device. (For older versions of Android any web browser can be used since you do not need to specifically authorize the web browser's ability to install.)
  3. Navigate to https://github.com/odk-x/tables/releases/latest and download the latest ODK-X Tables APK.
  4. In the download window, you will see ODK_Tables.N.N.apk. - Select it to download the file.

   - On older devices, the APK will automatically install after you approve the security settings.
   - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the ODK-X Tables APK <https://github.com/odk-x/tables/releases/latest>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

.. tip::

  You can also `install ODK-X Tables on an Android emulator <https://github.com/odk-x/tool-suite-X/wiki/Developer-Environment-Setup>`_. However, this can be slow and is only recommended for developers actively working on Tables.
