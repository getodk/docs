*****************************************
Using Android Debug Bridge with Collect
*****************************************

This document focuses specifically on using **adb** as a command line tool to perform tasks related to Collect. 

.. _what-is-adb:

What is Android Debug Bridge (adb)?
====================================

Android Debug Bridge or `adb <https://developer.android.com/studio/command-line/adb.html>`_ is a command line tool which acts as a bridge between the Android device and the terminal. It can control device over USB from a computer, copy files back and forth, install and uninstall apps, run shell commands, and more. To install **adb**, please follow the instructions given `here <https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/>`_. For the developers and users of ODK Collect, the most common uses are:

- include pushing blank forms to SD Card
- pulling the form database, deleting forms
- making the **.apk** file from the source code

.. _using-adb-with-collect:

Using adb with Collect
=======================

Forms can be manipulated from the command line itself. The following sections describe how **adb** can be used to work with the app.

.. _loading-blank-forms-with-adb:

Loading blank forms
~~~~~~~~~~~~~~~~~~~~

The forms are stored in :guilabel:`sdcard/odk/forms/` folder on the device. They can be downloaded from external source and loaded via a USB device using:

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

Contents of a form can be copied by running:

.. code-block:: none

  $ adb shell cp /sdcard/odk/forms/form-1.xml /sdcard/odk/forms/form-2.xml

.. note::

  Copying the contents of the form doesn't copy the current state of the form. 

.. _deleting-forms-with-adb:

Deleting forms
~~~~~~~~~~~~~~~

Forms can be deleted from :file:`sdcard/odk/forms` by running:

.. code-block:: none

  $ adb shell rm -d /sdcard/odk/forms/my_form.xml

.. _downloading-forms:

Downloading forms to your computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download a specific form from the computer, run:

.. code-block:: none

  $ adb pull /sdcard/odk/forms/my_form.xml

.. _downloading-database-with-adb:

Downloading database
~~~~~~~~~~~~~~~~~~~~~~

Developers might also need to check the entries in the database from the computer. In such case pull the database file from the SD card and use any **SQLite visualizer** to view it. To pull the database into the computer, run:

.. code-block:: none
  
  $  adb -d shell "run-as org.odk.collect.android cat databases/database.name" > target.sqlite

Here *target* refers to the location where the database is stored on computer.

.. _saving-screenshot-with-adb:

Saving screenshot
~~~~~~~~~~~~~~~~~~

Document writers need to take screenshots of the running app to help the readers visualize and verify everything. While using an emulator or a device, this might take some time. For this purpose, **adb** also provides a feature call **screencap** which can take a screenshot and upload it to your computer. For taking a screenshot, run:

.. code-block:: none

  $ adb exec-out screencap /sdcard/screen.png

Here, the image will be stored as ``screen.png`` which can be downloaded to the computer by running:

.. code-block:: none

  $ adb pull /sdcard/screen.png

.. note::

  You can also use Collect's program to get a screenshot by referring to the instructions given in the `Contribution Guide <https://docs.opendatakit.org/contributing/#screenshots-from-odk-collect>`_.

.. _recording-video-with-adb:

Recording a video
~~~~~~~~~~~~~~~~~~~

**adb** can be used to record video on device's screen. This can be done by running:

.. code-block:: none

  $ adb shell screenrecord /sdcard/example.mp4

This command will start recording your device’s screen using the default settings and save the resulting video to a file at :guilabel:`/sdcard/example.mp4` file on your device.


