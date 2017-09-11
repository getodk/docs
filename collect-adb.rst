*****************************************
Using Android Debug Bridge with Collect
*****************************************

This document focuses specifically on using **adb** as a command line tool to perform a variety of tasks related to Collect. 

.. _what-is-it:

What is Android Debug Bridge (adb)?
====================================

Android Debug Bridge or `adb <https://developer.android.com/studio/command-line/adb.html>`_ is a command line tool which, as the name suggests, acts as a bridge between the Android device and the terminal. It can control your device over USB from a computer, copy files back and forth, install and uninstall apps, run shell commands, and more. For the developers of ODK Collect, the most common ones include pushing blank forms to SD Card, pulling the form database, deleting forms, making the **.apk** file from the source code, etc. To install **adb**, please follow the instructions given `here <https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/>`_.

.. _downloading-adb:

Downloading adb
================

If you're already working on Android studio, you'll have **adb** already installed with it, but it requires specific configurations. To use adb with a device connected over USB, you must enable USB debugging in the device system settings, under Developer options. On Android 4.2 and higher, the Developer options screen is hidden by default. To make it visible, go to ``Settings``, then ``About phone`` and tap ``Build number`` seven times. Return to the previous screen to find Developer options at the bottom.

For people who don't have Android studio installed, **adb** can be downloaded as a standalone tool, either through command line or from the official Android Studio's `Command line tools page <https://developer.android.com/studio/index.html#command-tools>`_.

.. _using-adb:

Using adb with Collect
=======================

As mentioned before in the `Form Management section <https://docs.opendatakit.org/collect-forms/>`_, forms can be manipulated pretty easily from the command line itself. The following points describe how **adb** can be used to work with the app:

Loading blank forms
~~~~~~~~~~~~~~~~~~~~

All the data related to form instances and other files are saved in :guilabel:`sdcard/odk/forms/` folder on the device. Hence if can easily download a form from external sources and transfer them to the device via USB cable. To do this, just run:

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

While filling the form, it is possible to copy the contents of one form into another eaisly, just by knowing the path of the form.

.. code-block:: none

  $ adb shell cp /sdcard/odk/forms/form-1.xml /sdcard/odk/forms/form-2.xml

.. note::

  Copying the contents of the form doesn't copy the current state (saved, sent or finalized) of the form. 

Deleting forms
~~~~~~~~~~~~~~~

You can delete form instances directly with :command:`adb`. They are stored in :file:`sdcard/odk/forms`, with a directory for each instance. You can do so by using the command:

.. code-block:: none

  $ adb shell rm -d /sdcard/odk/forms/my_form.xml

Downloading forms to your computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download a specified form from the emulator/device to your computer using the **adb** tool. Developers might also need to check the entries in the database from the computer. In such case we can simple pull the database file from the SD card and use any database visualizer to see the data. For getting a form, simply run:

.. code-block:: none

  $ adb pull /sdcard/odk/forms/my_form.xml

.. _saving-screenshot:

Saving screenshot
~~~~~~~~~~~~~~~~~~

Document writers need to take screenshots of the running app to help the readers visualize and verify everything. While using an emulator or a device, this might take some time. For this purpose, **adb** also provides a feature call **screencap** which can take a screenshot and upload it to your computer. For taking a screenshot, just run:

.. code-block:: none

  $ adb shell screencap /sdcard/screen.png

Here, the image will be stored as ``screen.png`` which can be downloaded to the computer by running:

.. code-block:: none

  $ adb pull /sdcard/screen.png




