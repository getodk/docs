*****************************************
Using Android Debug Bridge with Collect
*****************************************

`Android Debug Bridge <https://developer.android.com/studio/command-line/adb.html>`_ is a command which acts as a bridge between the Android device and the terminal. It can control device over USB from a computer, copy files back and forth, install and uninstall apps, run shell commands etc. For the developers and users of ODK Collect, the most common uses are:

- loading blank forms to SD Card
- fetching completed forms
- deleting forms
- copying the form database
- installing the **.apk** file from the source code

.. _install-adb:

Installing adb
~~~~~~~~~~~~~~~

If you plan to work on ODK Collect or run the app using an emulator, download the `Android Studio <https://developer.android.com/studio/index.html>`_. It already comes with the adb tool. To use it, `enable USB Debugging <https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility/>`_.

To install :command:`adb` as a standalone tool, please follow the instructions given `here <https://android.gadgethacks.com/how-to/android-basics-install-adb-fastboot-mac-linux-windows-0164225/>`_.

Forms can be manipulated from the command line itself. The following sections describe how :command:`adb` can be used to work with the app.

.. _loading-blank-forms-with-adb:

Loading blank forms
~~~~~~~~~~~~~~~~~~~~

The forms are stored in :file:`sdcard/odk/forms/` folder on the device. They can be loaded via a USB device using:

.. code-block:: console

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

.. note::

  Path on the phone must include the file name and not just the folder name

.. _deleting-forms-with-adb:

Deleting forms
~~~~~~~~~~~~~~~

Forms can be deleted from :file:`sdcard/odk/forms` by running:

.. code-block:: console

  $ adb shell rm -d /sdcard/odk/forms/my_form.xml

.. _downloading-forms:

Downloading forms to your computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download a completed form or form instance from the computer, run:

.. code-block:: console

  $ adb pull /sdcard/odk/forms/my_form.xml

.. _downloading-database-with-adb:

Downloading database
~~~~~~~~~~~~~~~~~~~~~~

Developers might also need to check the entries in the database from the computer. In such case pull the database file from the SD card and use any **SQLite visualizer** to view it. To pull the database into the computer, run:

.. code-block:: console
  
  $  adb -pull /sdcard/odk/database/database.name

.. _saving-screenshot-with-adb:

Saving screenshot
~~~~~~~~~~~~~~~~~~

For taking a screenshot, run:

.. code-block:: console

  $ adb exec-out screencap /sdcard/screen.png

Here, the image will be stored as ``screen.png`` which can be downloaded to the computer by running:

.. code-block:: console

  $ adb pull /sdcard/screen.png

.. note::

  You can also use ODK docs program to get a screenshot by referring to the instructions given in the :ref:`Contribution Guide <screenshots>`.

.. _recording-video-with-adb:

Recording a video
~~~~~~~~~~~~~~~~~~~

:command:`adb` can be used to record video on device's screen. This can be done by running:

.. code-block:: console

  $ adb shell screenrecord /sdcard/example.mp4

As you hit :guilabel:`Enter`, this command will start recording your device’s screen using the default settings and save the resulting video to a file at :guilabel:`/sdcard/example.mp4` file on your device.

To stop the recording, press :guilabel:`ctrl` + :guilabel:`C`


