
ODK-X Notify
=======================
.. _notify-intro:

:dfn:`ODK-X Notify` has 2 components:

- Desktop application(Skunkworks-Parrot) 
- Mobile application(Skunkworks-Bat)

:program:`Skunkworks-Parrot` is the desktop application, written in Java, that provides a user interface for writing messages, creating user groups to receive them, and sending those messages via the Firebase Cloud Messaging. 

:program:`Skunkworks-Bat` is the Android application that receives these messages via Firebase, checks the user credentials to see if the user is in the group that should receive this message, and displays the message to the user. 



Installing ODK-X Notify
-------------------------

.. _notify-prereqs:

Prerequisites
""""""""""""""""

- **Skunkworks-Parrot:**

  - :doc:`sync-endpoint`
  - :ref:`ODK-X Services<services-using>`
  - :ref:`ODK-X Tables<tables-using>`
  - `Java 8 or higher <https://java.com/en/download/>`_

- **Skunkworks-Bat:**

  - :ref:`ODK-X Services<services-using>`


.. _notify-setup:

Setting up ODK-X Notify
"""""""""""""""""""""""""

:program:`Skunkworks-Parrot (Desktop App)`:
''''''''''''''''''''''''''''''''''''''''''''''

  1. Navigate to https://github.com/odk-x/skunkworks-parrot/releases and download the latest ODK-X_Notify_Desktop.jar file.
  2. Double click the file to start. If that fails try running:

    .. code-block:: console

  	  $ java -jar path/to/jar

  3. When the application opens, Click Configure. A window shown below will appear

    .. image:: /img/notify-setup/notify-setup.*

  4. To use the Skunkworks-Parrot App, the user needs to create a firebase project and add that project's information in the configure window. `Here <https://drive.google.com/file/d/1OBs5mITcIMREp_q7qKwEwO4XRQjzNnWj/view>`_ you can find the step by step instructions for the same.

  5. After adding all the required information in configure window, Click :menuselection:`Save`.


:program:`Sync-Endpoint`:
'''''''''''''''''''''''''''''''

.. note::

    Make sure you have installed the ODK-X Services app and ODK-X Tables app in an android device and have a running Sync-Endpoint server before proceeding for following steps.

1. Download all the folders from this `link <https://drive.google.com/drive/folders/1_WOhFrUDW2yLjeOaI5gW2AKiq-akGB78?usp=sharing>`_ and move them to :file:`sdcard/opendatakit/default/config/tables/` directory in your android device.

2. Place “google-services.json” file obtained from step 8 of `firebase setup <https://drive.google.com/file/d/1OBs5mITcIMREp_q7qKwEwO4XRQjzNnWj/view>`_ under the :file:`sdcard/opendatakit/default/config/assets/` directory.

3. Open the ODK-X Tables app. Tables app will automatically generate all the required files for server setup. After you see the message “Initialization completed successfully” you can close the ODK-X Tables app.

4. Using ODK-X Services app :ref:`reset app server<services-managing>`.


:program:`Skunkworks-Bat (Android App)`:
'''''''''''''''''''''''''''''''''''''''''''

.. note::

    Before installing the Bat app make sure you have installed the :ref:`ODK-X Services<services-using>` app.

1. From your device's :guilabel:`Settings`, choose :menuselection:`Security`.

  - Make sure *Unknown Sources* is checked.
  - (On older versions of Android, this setting is in :menuselection:`Applications` rather than :menuselection:`Security`)

2. Open a web browser on your phone.
3. Navigate to https://github.com/odk-x/skunkworks-bat/releases/ and download the latest ODK-X Notify APK.
4. In the download window, you will see ODK-X_Notify.N.N.apk. - Select it to download the file.

  - On older devices, the APK will automatically install after you approve the security settings.
  - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  You can also `download the ODK-X Notify-Bat APK <https://github.com/odk-x/skunkworks-bat/releases/>`_ to your computer and load it on your device via `adb <https://developer.android.com/studio/command-line/adb.html>`_ or another tool like `AirDroid <https://www.howtogeek.com/105813/control-your-android-from-a-browser-with-airdroid/>`_.

Using ODK-X Notify
-------------------------

.. toctree::
  :maxdepth: 2

  notify-using
