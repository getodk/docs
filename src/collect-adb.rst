.. spelling::

  logcat
  bugreport
  screencap


Using Android Debug Bridge with Collect
===========================================

`Android Debug Bridge`_ is a tool that provides command-line access
to a USB-connected Android device.
It can be used to move files between the device and your computer,
install applications,
and take screenshots and videos.
When connected to a device that has ODK Collect installed,
it can be used to push blank form definitions
and pull completed forms.

.. _Android Debug Bridge: https://developer.android.com/studio/command-line/adb

.. _install-adb:

Installing and setting up ADB
------------------------------------

.. _install-adb-android-studio:

Android Studio
~~~~~~~~~~~~~~~~~

The easiest and most well-supported way to install ADB is to
install `Android Studio`_,
which includes ADB.
After installing, you'll need to
`enable USB Debugging`__.

__ https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility_

.. _install-adb-standalone:

Standalone ADB
~~~~~~~~~~~~~~~~

You can also `install ADB without Android studio`__.
This is not well supported, though,
and should only be done
if you cannot install Android Studio on your computer.

__ https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/_

.. _adb-forms:

Managing forms with ADB
---------------------------

Form definitions are stored on the device in the :file:`forms` subdirectory of :ref:`your Collect directory <collect-directory>`.

.. _loading-blank-forms-with-adb:

Loading blank forms
~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb push local/path/to/form.xml <collect-directory>/forms/form.xml

.. note::

  The target path on the phone
  (the last part of the command)
  must include the file name.

.. _deleting-forms-with-adb:

Deleting forms
~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb shell rm -d <collect-directory>/forms/form.xml

.. _downloading-forms:

Downloading forms to your computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download all filled records from a device:

.. code-block:: console

  $ adb pull <collect-directory>/instances/*


.. _adb-dev-tasks:

Developer tasks and troubleshooting with ADB
-----------------------------------------------

.. _downloading-database-with-adb:

Downloading Collect databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect stores form definition and form record state information
in a few SQLite databases,
which you can pull onto your local computer.

.. code-block:: console

  $  adb pull <collect-directory>/metadata/*.db

.. _saving-screenshot-with-adb:

Taking screenshots
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb exec-out screencap /sdcard/image-name.png

To pull the saved image locally:

.. code-block:: console

  $ adb pull /sdcard/image-name.png

.. note::

  ODK Docs contributors can use the :ref:`screenshot utility script <screenshots>`, which wraps the :command:`adb` commands and assists with saving the images to the correct location and inserting appropriate markup in the documentation source.

.. _recording-video-with-adb:

Recording video
~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb shell screenrecord /sdcard/video-name.mp4

When you hit :guilabel:`Enter`, the video starts recording immediately.

To stop the recording, press :kbd:`CTRL-C`. If you don't interrupt the recording, it will stop after three minutes.

To pull the video locally:

.. code-block:: console

  $ adb pull /sdcard/video-name.png

.. _adb-debug-logs:

Capturing logs for debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _logcat:

Capturing in-progress logs with logcat
""""""""""""""""""""""""""""""""""""""""

If you are experiencing crashes or other serious glitches,
and you can reproduce the bug,
use :command:`adb logcat` to capture log events during the crash.

#. Before reproducing the bug, begin piping logs to a file:

   .. code-block:: console

     adb logcat > logfile.txt

   This will write all logged errors to your local file :file:`logfile.txt` as they occur.

#. Reproduce the bug or crash event.

#. Type :kbd:`CTRL-C` to stop logging.

You can then upload the :file:`logfile.txt` file to
a `a support forum post <https://forum.getodk.org/c/support>`_
or post in the |forum|.

.. _bugreport:

Pull a bug report
""""""""""""""""""

If more in-depth information is needed,
you can pull a complete bug report from the device.

.. code-block:: console

  adb bugreport

This copies a ZIP file locally containing all system messages,
error logs, and diagnostic output,
along with information about the device's
hardware, firmware, and operating system.

.. seealso:: https://developer.android.com/studio/debug/bug-report.html

.. _collect-directory:

Identifying the Collect directory on your device
-------------------------------------------------

The ODK Collect directory on your device is:

* :file:`/sdcard/odk` if you are running an ODK Collect version less than v1.26.0 or have a file migration banner on the main screen
* :file:`/sdcard/Android/data/org.odk.collect.android/files` if you have ODK Collect version v1.26.0+ and don't have a file migration banner on the main screen
* If you have Collect 2021.2 or later then each ref:`Project <collect-projects>` will have its own directory which can be found in :file:`/sdcard/Android/data/org.odk.collect.android/files/projects`. The Project directories will contain a blank file with the same name as the Project itself so you can identify it.

Prior to ODK Collect v1.26.0, all Collect files were stored in the :file:`/sdcard/odk` directory. This directory was available to other applications to integrate with which can be very useful but can pose privacy risks. Starting August 2020, Google will no longer allow Android applications to read or write files directly to this folder. Instead, each application will only be able to write files to a special directory that only it has access to. You can read more about this change `on the forum <https://forum.getodk.org/t/odk-collect-v1-26-storage-migration/25268>`_.
