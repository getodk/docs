******************************
ODK Collect
******************************

.. _collect-introduction:

:dfn:`ODK Collect` is an open source Android app that replaces paper forms used in survey-based data gathering. 

Here is a typical pattern of use:

- :ref:`Get blank forms <loading-forms-into-collect>` from :ref:`ODK Aggregate Server or Google Drive <in-app-get-blank-forms>`
- :ref:`Fill out surveys <fill-blank-forms>` with participants
- :ref:`Upload completed surveys <uploading-forms>` to Aggregate or Google Drive


.. _installing-collect:

Installing Collect
====================

.. _install-collect-from-google-play:

Install from Google Play Store
---------------------------------

**Recommended**

`The ODK Collect App is available in the Google Play store <https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_.


Install Manually
-------------------

You can also download from the web and install manually.

- From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

  - Make sure *Unknown Sources* is checked.
  - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

- Open a web browser on your phone.
- Navigate to https://opendatakit.org/downloads/download-category/collect/  and download the ODK Collect APK.
- In the download window, you will see ODK_Collect_vN.N.N.apk. - Select it to download the file.

  - On older devices, the APK will automatically install after you approve the security settings.
  - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

- You can also `download the ODK Collect APK <https://opendatakit.org/downloads/download-category/collect/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

--------

.. note::

  On older Android devices (4.0 and earlier), ODK Collect required an external SD Card. This is no longer an issue because Android devices have internal storage. Virtually all current Android devices will run ODK Collect.

.. tip::

  Developers can also `install ODK Collect on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and buggy and is not recommended.


.. _connecting-to-server:

Connecting to a Server
================================

When you first install Collect, it connects to the `ODK Aggregate Demo server <https://opendatakit.appspot.com/Aggregate.html>`_. You can try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :ref:`filling them out <fill-blank-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.

.. tip::
  Managing forms from an ODK Aggregate server or Google Drive is typical. However, there are other ways to use ODK Collect. You can also :ref:`upload blank forms directly to your device <loading-forms-directly>`, :doc:`download completed forms directly with adb <collect-adb>`, or :doc:`use ODK Briefcase <briefcase-forms>`.


.. _connecting-to-aggregate:

Connecting to your own ODK Aggregate Server
------------------------------------------------

See :doc:`aggregate-install` to setup your ODK Aggregate server.

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`ODK Aggregate`.
- Edit :guilabel:`ODK Aggregate settings` to connect to your ODK Aggregate instance.

.. _connecting-to-google:

Connecting to a Googe Drive Account
--------------------------------------

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`Google Drive, Google Sheets`.
- Select your Google account. (The available Google Accounts are pulled from the Google Play Store app.)

.. _connecting-to-other:

Connecting to another server app
-----------------------------------

Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`_ can be connected to, using the :ref:`connecting-to-aggregate` instructions. Choose :menuselection:`ODK Aggregate` as the server type.

.. warning::

  In :menuselection:`Server Settings`, there is currently a :guilabel:`Type` option of :menuselection:`Other`. It is unlikely you will need this option, since any server application will need to implement the same API as ODK Aggregate. 

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.opendatakit.org/c/support>`_.

  The :menuselection:`Other` option will likely be deprecated in the future, and its use is not recommended.  
