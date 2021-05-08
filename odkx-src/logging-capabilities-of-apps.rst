Logging Capabilities of Apps
=================================
There are three types of logging that exist.

ODK-X Logging System
----------------------

The ODK-X log files are stored in the directory :file:`/sdcard/opendatakit/default/output/logging` of your Android device. If you do not have an external storage, the same directory would start with Internal Storage instead of sdcard.  If you would like to zip all of your ODK-X data and share it please watch `this video <https://www.youtube.com/watch?v=jzqu7w4VepM>`_ . 

Android Logging
----------------------

The Android logging system provides a mechanism for collecting and viewing system debug output. Logs from various applications and portions of the system are collected in a series of circular buffers, which then can be viewed and filtered by the `logcat` command. You can use `logcat` from an Android Debug Bridge shell to view the log messages. You can also see it in Android Studio.
The command in a shell environment is:

.. code-block:: console

  $ adb logcat

For detailed information please see `here <https://www.brainbell.com/android/logcat.html>`_ .

Sync-Endpoint Docker
----------------------

To fetch logs of a container, you can run the command

.. code-block:: console

  $ docker logs [OPTIONS] CONTAINER

For instance, you would like to fetch logs of ODK-X sync-endpoint. The command would be

.. code-block:: console

  $ docker logs odkx-sync-endpoint

In case you're not sure about the container names you can view which containers are active in docker by the following command:

.. code-block:: console

  $ docker ps

You can also redirect the logs into an output file for easy access via

.. code-block:: console

  $ docker logs odkx-sync-endpoint >output.txt

For more information, check the following: `https://docs.docker.com/engine/reference/commandline/logs/ <https://docs.docker.com/engine/reference/commandline/logs/>`_
