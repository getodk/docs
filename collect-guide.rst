******************************
Collect Guide
******************************

:dfn:`ODK Collect` is an open source Android app that replaces paper forms used in survey-based data gathering. 

Here is a typical pattern of use:

- :ref:`Get blank forms` from an :ref:`ODK Aggregate Server` or :ref:`Google Drive`
- :ref:`Fill out surveys` with participants
- :ref:`Upload completed surveys` to Aggregate or Google Drive

You can also:

- :ref:`Upload forms directly to Collect`
- :ref:`Copy form to and from Collect with ODK Briefcase` (?)
- :ref:`Configure Collect instances via barcode`  

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

  - Make sure Unknown sources is checked.
  - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`

- Open a web browser on your phone.
- Navigate to https://opendatakit.org/downloads/download-category/collect/  and download the ODK Collect APK.
- In the download window, you will see ODK_Collect_vN.N.N.apk. - Select it to download the file.

  - On older devices, the APK will automatically install after you approve the security settings.
  - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

- You can also `download the ODK Collect APK <https://opendatakit.org/downloads/download-category/collect/`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDriod <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/`_.

--------

.. note::

  On older Android devices (4.0 and earlier), ODK Collect required an external SD Card. This is no longer an issue because Android devices have internal storage. Virtually all current Android devices will run ODK Collect.

.. tip::

  Developers can also `install ODK Collect on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and buggy, and is not recommended.


.. _connecting-to-server:

Connecting to a Server
================================

When you first install Collect, it connects to the `ODK Aggregate Demo server <https://opendatakit.appspot.com/Aggregate.html>.` You can try out the app by :ref:`downloading blank example forms`, filling them out, and :ref:`uploading completed forms` back to the demo server.

.. tip::
  Managing forms from an ODK Aggeegate server or Google Drive is typical. However, there are other ways to use ODK Collect. You can also :ref:`upload forms directly to your device`, :ref:`download completed forms directly`, or :ref:`use ODK Briefcase`.


.. _connecting-to-aggregate:

Connecting to your own ODK Aggregate Server
------------------------------------------------

See :ref:`installing-aggregate` to setup your ODK Aggregate server.

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`ODK Aggregate`
- Edit :guilabel:`ODK Aggregate settings` to connect to your ODK Aggregate instance.

.. _connecting-to-google:

Connecting to a Googe Drive Account
--------------------------------------

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`Google Drive, Google Sheets`
- Select your Google account. (The available Google Accounts are pulled from the Google Play Store app.)

.. _connecting-to-other:

Connecting to another server app
-----------------------------------

Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>` can be connected to, using the :ref:`connecting-to-aggregate` instructions. Choose :menuselection:`ODK Aggregate` as the server type.

.. warning::

   In :menuselection:`Server Settings`, there is currently a :guilabel:`Type` option of :menuselection:`Other`. It is unlikely you will need this option, since any server application will need to implement the same API as ODK Aggregate. 

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.opendatakit.org/c/support>`.

  The :menuselection:`Other` option will likely be deprecated in the future, and its use is not recommended.  


.. _loading-forms-into-collect:

Loading Blank Forms
====================

A :dfn:`blank form` is a `.xml` file contaning a form definition consistent with the `XForm specification <https://opendatakit.github.io/xforms-spec/>`_. Blank forms can be created using `ODK Build <https://build.opendatakit.org/>`_ or `XLSForm <https://opendatakit.org/use/xlsform/>`_.

In order to complete out forms with survey participants, you must first load blank forms into the Collect App.

.. _in-app-get-blank-forms:

Loading Forms from ODK Aggregate Server or Google Drive 
------------------------------------------------------------

If you have :ref:`connected ODK Collect to a server <connecting-to-server>` or :ref:`Google Drive <connecting-to-google>`, use :guilabel:`Get blank forms` on the app home screen to browse available forms and download them to your device.

.. note::

  Before downloading blank forms from Aggregate or Google Driveto Collect, those forms have to be uploaded. 

  .. link to Aggregate guide, once there is one

.. _loading-forms-directly:

Loading forms directly
------------------------

You can load forms directly from a computer to your device via USB, using `Android Developer Bridge <https://developer.android.com/studio/command-line/adb.html>`_.

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

You can also download forms to  your device via a web browser, and move them to the :file:`odk/forms/` directory, using the device's file manager (:menuselection:`Settings -> Storage & USB -> Explore`).

Loading form media
~~~~~~~~~~~~~~~~~~~~~

If a form :ref:`includes images or other media <including-images-as-choices>`, those files have to be loaded to the device along with the form.

Media files should be placed in a folder labeled :file:`{form-name}-media`. 

- When using ODK Aggregate, the form upload prompt includes instructions to upload the :file:`-media` folder. The files are downloaded automatically when :ref:`fetching forms from Aggregate <in-app-get-blank-forms>`.
- When using Google Drive, the :file:`-media` folder should be uploaded to the same location as the form.
- If :ref:`loading forms directly to your device <loading-forms-directly>`, the :file:`-media` folder needs to be placed in the :file:`sdcard/odk/forms` directory, alongside the form itself.

.. _fill-blank-forms:

Filling out forms
===================

Once you have at least one form :ref:`loaded into ODK Collect <loading-forms-into-collect>`, you can fill out a form. 

- Select :guilabel:`Fill Blank Form` from the app home screen.
- Select the form you would like to fill out from the form list.
- Typically, you will :gesture:`Swipe Left` to advance forward through the question, and :gesture:`Swipe Right` to backup.
  - You can switch from :gesture:`Swipe` navigation to Forward/Backward buttons in :menuselection:`⋮ -> General Settings -> User Interface`
  - Some questions will :ref:`auto-advance <autoadvance-widget>` after being answered.
  - `Required questions <http://xlsform.org/#required>`_ will not allow you to advance unless answered.
- To **remove a response**, :gesture:`Long Press` on the :term:`question label`. 


For a (mostly) complete guide to form question appearance, see :doc:`form-widgets`.

.. _completing-form:

Completing a Form
-------------------

Once you have reached the end of a form, you will have the opportunity to Save and Exit the form. At this point, you may also:

.. _name-form-instance:

Name the form
~~~~~~~~~~~~~~~

The last form screen provides a default name for the form (defined by the form designer). You can rename it. This name only applies to that particular instance of a completed form (not to the blank form).

The Form Name identifies the form for :ref:`later viewing <viewing-completed-forms>` and :ref:`uploading to a server <uploading-completed-forms>`. For this reason, a meaningful name may be important to you. 

.. _finalize-form:

Mark the form as *Finalized*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only :formstate:`Finalized` forms can be :ref:`uploaded to a server <uploading-completed-forms>`. 

.. _editing-saved-forms:

Editing *Saved* forms
----------------------

- From the app home screen, select :guilabel:`Edit Saved Form`. 
- From the form list, select a form by name.

This will reopen the form, which are then free to edit.

.. note:: 

  - :formstate:`Sent` forms will not appear in the :guilabel:`Edit Saved Forms` list.

  - You may freely edit :formstate:`Saved` and :formstate:`Finalized` forms.


Uploading Finalized Forms
===========================

If you are connected to :ref:`an ODK Aggregate server <connecting-to-aggregate>` or :ref:`Google Drive Account <connecting-to-google>`, use :guiselect:`Send Finalized Forms` to upload :formstate:`finalized` form instances. 

For local form management, use `ODK Briefcase <https://opendatakit.org/use/briefcase/>`_ to pull :formstate:`finalized` form instances to your local computer.

:formstate:`Sent` forms are no longer editable, but they remain viewable until deleted. Select :guilabel:` 
