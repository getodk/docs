*****************************
Form Management in Collect
*****************************

This section explains how users can work with forms in Collect app. This includes loading blank forms from external servers or from local computer, filling them, saving and finalizing the contents, and lastly sending and deleted them. This document also explains how `adb <https://developer.android.com/studio/command-line/adb.html>`_, or Android Developer Bridge can be used as a command line tool to perform a variety of tasks. For the developers of ODK, the most common ones include pushing blank forms to SD Card, pulling the form database, deleting forms, making the **.apk** file from the source code, etc. To install **adb**, please follow the instructions given `here <https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/>`_.

If you're already working on Android studio, you'll have **adb** already installed with it, but it requires specific configurations. To use adb with a device connected over USB, you must enable USB debugging in the device system settings, under Developer options. On Android 4.2 and higher, the Developer options screen is hidden by default. To make it visible, go to ``Settings``, then ``About phone`` and tap ``Build number`` seven times. Return to the previous screen to find Developer options at the bottom.

.. note::

  These forms reside in the :guilabel:`sdcard/odk` folder in the phone.

These forms 

.. _loading-forms-into-collect:

Loading Blank Forms
====================

A :dfn:`blank form` is a `.xml` file containing a form definition consistent with the `XForm specification <https://opendatakit.github.io/xforms-spec/>`_. Blank forms can be created using `ODK Build <https://build.opendatakit.org/>`_ or `XLSForm <https://opendatakit.org/use/xlsform/>`_.

In order to fill out forms with survey participants, you must first load blank forms into the Collect App.

.. _in-app-get-blank-forms:

Loading Forms from ODK Aggregate Server or Google Drive 
------------------------------------------------------------

If you have :ref:`connected ODK Collect to a server <connecting-to-server>` or :ref:`Google Drive <connecting-to-google>`, use :guilabel:`Get blank forms` on the app home screen to browse available forms and download them to your device.

.. note::

  Before downloading blank forms from Aggregate or Google Drive to Collect, those forms have to be uploaded to those locations.

  .. link to Aggregate guide, once there is one

.. _loading-forms-directly:

Loading forms directly
------------------------

You can load forms directly from a computer to your device via USB, using the **adb** command:

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

You can also download forms to your device via a web browser, and move them to the :file:`odk/forms/` directory, using the device's file manager (:menuselection:`Settings -> Storage & USB -> Explore`).

Loading form media
~~~~~~~~~~~~~~~~~~~~~

If a form :ref:`includes images or other media <image-options>`, those files have to be loaded to the device along with the form.

Media files should be placed in a folder labelled :file:`{form-name}-media`. 

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

Once you have reached the end of a form, you will have the opportunity to *Save* and *Exit* the form. At this point, you may also:

.. _name-form-instance:

Name the form
~~~~~~~~~~~~~~~

The last form screen provides a default name for the form (defined by the form designer). You can rename it. This name only applies to that particular instance of a completed form (not to the blank form).

The Form Name identifies the form in lists throughout the app. For this reason, a meaningful name may be important to you. After you've saved the name, the form automatically moves to the :guilabel:`Send Finalized Form` section, from where you can send it.

.. _finalize-form:

Mark the form as *Finalized*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only :formstate:`Finalized` forms can be :ref:`uploaded to a server <uploading-forms>`. 

.. _editing-saved-forms:

Editing *Saved* forms
----------------------

- From the app home screen, select :guilabel:`Edit Saved Form`. 
- From the form list, select a form by name.

This will reopen the form, which you are then free to edit.

.. note:: 

  - :formstate:`Sent` forms will not appear in the :guilabel:`Edit Saved Forms` list.

  - :formstate:`Sent` forms, will be available for viewing in :guilabel:`View Sent Forms` list, along with the details which cannot be edited.

  - You may freely edit :formstate:`Saved` and :formstate:`Finalized` forms. 

.. _uploading-forms:

Uploading Finalized Forms
===========================

If you are connected to :ref:`an ODK Aggregate server <connecting-to-aggregate>` or :ref:`Google Drive Account <connecting-to-google>`, use :guilabel:`Send Finalized Forms` to upload :formstate:`finalized` form instances. 

For local form management, use `ODK Briefcase <https://opendatakit.org/use/briefcase/>`_ to pull :formstate:`finalized` form instances to your local computer.

:formstate:`Sent` forms are no longer editable, but they remain viewable until they are deleted. 

.. note:: 

  - You can copy form instances from the device using :command:`adb`, however this will not update the state of the form to :formstate:`Sent`.

.. _deleting-forms:

Deleting Forms
===============

You can delete :formstate:`Saved`, :formstate:`Finalized`, :formstate:`Sent`, and :formstate:`Blank` forms by selecting :guilabel:`Delete Saved Form` on the app home screen. This page contains two tabs, :guilabel:`Saved Forms`, which contains the list of all form instances that are saved, finalized or sent, and :guilabel:`Blank Forms`.

You can also delete form instances directly with :command:`adb`. They are stored in :file:`sdcard/odk/instances`, with a directory for each instance. You can do so by using the command:

.. code-block:: none

  $ adb shell rm -d /sdcard/odk/forms/my_form.xml



.. note:: 

  - Deleted Forms are listed, but cannot be viewed. They are indicated with the crossed-out eye icon.

.. _downloading-forms:

Downloading forms to your computer
===================================

You can download a specified form from the emulator/device to your computer using the **adb** tool. Developers might also need to check the entries in the database from the computer. In such case we can simple pull the database file from the SD card and use any database visualizer to see the data. For getting a form, simply run:

.. code-block:: none

  $ adb pull /sdcard/odk/forms/my_form.xml

.. _saving-screenshot:

Document writers need to take screenshots of the running app to help the readers visualize and verify everything. While using an emulator or a device, this might take some time. For this purpose, **adb** also provides a feature call **screencap** which can take a screenshot and upload it to your computer. For taking a screenshot, just run:

.. code-block:: none

  $ adb shell screencap /sdcard/screen.png

Here, the image will be stored as ``screen.png`` which can be downloaded to the computer by running:

.. code-block:: none

  $ adb pull /sdcard/screen.png







