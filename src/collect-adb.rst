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

.. _Android Debug Bridge: https://developer.android.com/studio/command-line/adb.htlm

.. _install-adb:

Installing adb
----------------

Android Studio
~~~~~~~~~~~~~~~~~

The easiest and most well-supported way to install ADB is to 
install `Android Studio`_,
which includes ADB.
After installing, you'll need to
`enable USB Debugging`__.

__ https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility_

Standalone ADB
~~~~~~~~~~~~~~~~

You can also `install ADB without Android studio`__.
This is not well supported, though,
and should only be done
if you cannot instal Android Studio on your computer.

__ https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/_

Managing Forms with ADB
---------------------------

Forms are stored on the device in  :file:`sdcard/odk/forms/`.

.. _loading-blank-forms-with-adb:

Loading blank forms
~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb push local/path/to/form.xml /sdcard/odk/forms/form.xml

.. note::

  Path on the phone must include the file name and not just the folder name

.. _deleting-forms-with-adb:

Deleting forms
~~~~~~~~~~~~~~~

.. code-block:: console

  $ adb shell rm -d /sdcard/odk/forms/form.xml

.. _downloading-forms:

Downloading forms to your computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download a completed form or form instance from the computer:

.. code-block:: console

  $ adb pull /sdcard/odk/forms/form.xml

  
Developer tasks and troubleshooting with ADB
-----------------------------------------------
  
.. _downloading-database-with-adb:

Downloading Collect databases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect stores settings and form state information
in several SQLite databases, 
which you can pull onto your local computer.

To see a list of available databases:

.. code-block:: console
  
  $  adb ls /sdcard/odk/database/

To pull a database locally:

.. code-block:: console
  
  $  adb pull /sdcard/odk/database/{database-name}

.. _saving-screenshot-with-adb:

Taking screenshota
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
