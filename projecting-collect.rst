********************************************
Projecting ODK Collect onto another screen
********************************************

This guide helps the users to project ODK collect onto a screen. There are various methods available to do this, some of the methods are discussed below:

.. _using-vysor:

Using Vysor
--------------

Vysor is an extension for the Google Chrome browser that connects to an app on your smartphone. This extension enables you to control your phone from your PC or Mac using the mouse/trackpad and keyboard.

Before proceeding further make sure USB Debugging mode is enabled:

.. _enable-usb-debugging:

Enable USB Debugging Mode on Android
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Go to :menuselection:`Settings`, choose :guilabel:`About phone`.
2. Scroll down and tap :guilabel:`Build number` seven times.

.. image:: /img/project-collect/build-number.*
  :alt: Image showing build number
  :class: device-screen-vertical
  
3. Go back to :menuselection:`Settings` and there you will find :guilabel:`Developer options` in the menu.

.. image:: /img/project-collect/developer-options.*
  :alt: Image showing developer options
  :class: device-screen-vertical
  
4. Scroll down and enable :guilabel:`USB debugging` mode. 

.. image:: /img/project-collect/usb-debugging.*
  :alt: Image showing USB debugging mode
  :class: device-screen-vertical
  
5. Confirm the action when prompted.

.. note::
  
  Windows users should make sure that they have `downloaded <https://devs-lab.com/usb-adb-drivers-for-all-android-devices.html>`_ Universal ADB Drivers.

Follow the instructions given below to use Vysor:

1. Make sure you have Google chrome installed, if not download it from `here <https://www.google.com/chrome/browser/desktop/index.html>`_.
2. Download `Vysor extension <https://chrome.google.com/webstore/detail/vysor/gidgenkbbabolejbgbpnhbimgjbffefm>`_.
3. Click on :guilabel:`Add To Chrome`

.. image:: /img/project-collect/vysor-download.*
  :alt: Vysor download

4. Confirm your action by clicking on :guilabel:`Add app`.

.. image:: /img/project-collect/vysor-add-app.*
  :alt: Vysor add app button

.. warning:: 
  
  On Windows, You may get an error **WebGL is not supported** 
  
  .. image:: /img/project-collect/webgl.*
    :alt: Image on WebGL error
  
  To fix this, follow the procedures given below:
  
  First, we need to enable hardware acceleration:
  
  1. Go to ``chrome://settings``, scroll down and click on :guilabel:`Advanced`.
  
  .. image:: /img/project-collect/advanced-setting.*
    :alt: Image showing advanced settings
    
  |
  
  2. In the System section, ensure the Use :guilabel:`hardware acceleration when available` is enabled. You'll need to relaunch Chrome for any changes to take effect. Click on :guilabel:`RELAUCH`
  
  .. image:: /img/project-collect/acceleration.*
    :alt: Image showing hardware acceleration option
  
  |
  
  3.  Then, we need to enable WebGL, go to ``chrome://flags``, scroll down and search for **WebGL 2.0**. From the drop-down list choose :guilabel:`Enabled`.
  
  .. image:: /img/project-collect/webgl-enabled.*
    :alt: Image showing enabled WebGL 2.0
  
  |
  
  Now you can return to `Vysor extension <https://chrome.google.com/webstore/detail/vysor/gidgenkbbabolejbgbpnhbimgjbffefm>`_ and install it again.
  
5. After adding the extension, you would be able to see it in the chrome toolbar, if it is not visible there go to ``chrome://apps`` and you would be able to see there.

.. image:: /img/project-collect/vysor-chrome.*
  :alt: Image showing vysor app

6. Launch the extension and connect your phone through USB.

.. image:: /img/project-collect/vysor-launch.*
  :alt: Image showing options after launching vysor
    
7. Click on :guilabel:`Find Devices`, select your device and click on :guilabel:`Select`.

.. image:: /img/project-collect/find-device.*
  :alt: Image showing options to find and select devices.

8. After clicking :guilabel:`Select`, Vysor would be automatically downloaded to your phone, and you will be able to see your phone screen.

.. image:: /img/project-collect/phone-screen .*
  :alt: phone screen on vysor

9. Click on the Collect app and there you go, you have successfully projected your phone screen.

.. image:: /img/project-collect/collect-app.*
  :alt: Image showing collect-app after launching vysor

.. _using-android-studio:

Using Android Studio
----------------------------

Android Studio is the official IDE for Android. It provides tools for building apps for every type of Android device. Android Emulator can be used to test your app virtually on any Android device configuration.

Follow the procedures given below to run your app on the emulator:

1. `Download Android Studio <https://developer.android.com/studio/index.html#downloads>`_ with SDK according to your platform.

2. Here is a `tutorial <https://developer.android.com/studio/install.html>`_ on how to set up Android Studio according to different platforms.

3. After installing, launch Android Studio and click on :guilabel:`Start a new Android Studio project` or if you have an existing project click on  :guilabel:`Open an existing Android Studio project`.

.. image:: /img/project-collect/android-studio.*
  :alt: Image showing Android studio screen 

4. To create a new project follow further steps but if you have an existing project skip to the step 9. 

5. Choose your project location and fill out the :guilabel:`Application name` and click on :guilabel:`Next`.

.. image:: /img/project-collect/application-name.*
  :alt: Image showing new project window
  
6. Select the :guilabel:`Phone and Tablet` option and choose your :menuselection:`Minimum SDK`. Click on :guilabel:`Next`.

.. image:: /img/project-collect/target-android.*
  :alt: Image showing Target Android Devices window

7. Select an Activity, **Empty Activity is preferable**. Click on :guilabel:`Next`.

.. image:: /img/project-collect/activity.*
  :alt: Image showing window having various activities
  
8. In Customize the Activity window, don't change the default options and click on :guilabel:`Finish`.

.. image:: /img/project-collect/customize-activity.*
  :alt: Image showing Customize Activity window
  
9. After few minutes, you will be able to see the Android Studio main window, click on |AVD| icon, alternatively, you can click on :menuselection:`Tools` then select :guilabel:`Android`, from the drop-down menu select :guilabel:`AVD Manager`.

.. |AVD| image:: /img/project-collect/avd-manager.*
  :alt: Image showing avd manager icon
  
.. image:: /img/project-collect/main-window.*
  :alt: Image showing Android Studio main window
  
10. If you are an existing user list of all virtual devices would appear on the screen, to create a new virtual device, click on :guilabel:`+ Create Virtual Device...`

.. image:: /img/project-collect/avd-list.*
  :alt: Image showing list of virtual devices.

  
11. In the Select Hardware window, choose a device definition for your virtual device. I have chosen :guilabel:`Nexus 5`, click on :guilabel:`Next`.

.. image:: /img/project-collect/hardware.*
  :alt: Image showing hardware window
  
12. Select a system image, I have chosen Lollipop version.Click on :guilabel:`Next`.

.. image:: /img/project-collect/system-image.*
  :alt: Admin settings menu
  
13. Enter your :guilabel:`AVD Name`, choose startup orientation and click on :guilabel:`Finish`.

.. image:: /img/project-collect/verify-configuration.*
  :alt: Configuration verification menu

14 Now you would be able to see your virtual device in Android Virtual Device Manager. Click on |run| to run your Android emulator.

.. |run| image:: /img/project-collect/run-icon.*
         :alt: image showing run icon

.. image:: /img/project-collect/update-virtual.*
  :alt: Image showing updated virtual devices  

  
.. note::
 
 Please wait for some time as Android emulator takes very long time to start.
 
15. After the emulator is started, you would be able to see the screen of your emulator. :

.. image:: /img/project-collect/emulator-screen1.*
  :alt: Image showing emulator screen.
   
16. Now click on |SDK| to see the location of Android SDK.

.. |SDK| image:: /img/project-collect/sdk-manager.*
         :alt: Image showing SDK manager icon
  
.. image:: /img/project-collect/emulator-screen.*
  :alt: Image showing SDK manager in the Android main window.
  
17. Open the terminal and move to the `platform-tools` of the `SDK` directory.

.. code-block:: console

  $ cd platform-tools
  
18. Copy the :file:`collect.apk` into :file:`platform-tools` folder. You can `download <https://opendatakit.org/downloads/download-info/odk-collect-apk/>`_ the apk file from here.

19. Type the following command to see the list connected devices:

.. code-block:: console

  $ adb devices

You should be able to see the emulator along with its port number, e.g emulator-5554, Here 5554 is the port number. If the emulator is not present in the list, restart the emulator.

To install apk file, in the emulator type the following command: 

.. code-block:: console

  $ adb install collect.apk
 
If the command is successfully executed, you will find your file in the launcher of your emulator.

.. image:: /img/project-collect/collect-emulator.*
  :alt: Image showing collect app on the emulator screen
  
.. image:: /img/project-collect/collect-emulator2.*
  :alt: Image showing collect app on the emulator screen
  
.. _using-command-line:
  
Using Command Line 
~~~~~~~~~~~~~~~~~~~~~~~

You can also run the emulator using command line. Follow the steps given below to start your emulator using the command line:

.. note::

  If SDK installation has been put in another drive or folder instead of in its default location of ``$USER_HOME`` or ``$HOME``. Make sure you have set the environment variables according to that. In the command line type the following command to set environment variables.
  
  .. code-block:: console
  
    set ANDROID_SDK_ROOT=path\sdk\


1. Open the terminal and move to the :file:`emulator` folder of the `SDK` directory.

.. code-block:: console

  $ cd emulator
  
2. For the list of available virtual devices, type the following command:

.. code-block:: console

  $ emulator -list-avds
 
.. tip::

  If you are not able to locate :file:`emulator.exe` file in :file:`SDK` folder. Type the following command to know the location of the file:
  
  .. code-block:: console

    $ which emulator
  
  On Windows:
  
  .. code-block:: doscon

    > where emulator

3. Use :command:`emulator` to start the emulator. Here *avd_name* is the name of Android virtual device that you have created.

.. code-block:: console

  $ emulator -avd avd_name

.. note::
  
  1. You can use :command:`sdkmanager` command to update, install, and uninstall packages for the Android SDK. This method is not recommended as it is not   user-friendly and also takes time.

     To create an emualtor you need to download system image for a particular API level.
	
    .. code-block:: console

      $ sdkmanager --verbose "system-images;android-19;google_apis;x86"
	  
	  
    - The :option:`--verbose` option or :option:`-v` option shows errors, warnings and all messages.
    - ``system-images;android-19;google_apis`` specifies the system image package for the Android virtual device.
    - ``android-19`` specifies the API level. You can choose different API level if you want.
   
  2. To create and manage Android Virtual device from the command line, you can use :command:`avdmanager`.
  
     After downloading system image, you can use the following command to create an emulator.
   
    .. code-block:: console

      $ avdmanager -v create avd --name testAVD -k "system-images;android-19;google_apis;x86" -g "google_apis"
	  
	 
    - The :option:`create avd` option creates a new Android virtual device.
    - :option:`--name` option is a **required** option which is used to specify name of the AVD. Here, the name of the AVD is testAVD.
    - The :option:`-g` specifies the sys-img tag to use for the AVD.
    - :option:`-k` specifies package path of the system image for the AVD.
   
.. seealso::

  You can also use `Genymotion <https://www.genymotion.com/>`_ as an alternative as it is very fast as compared to custom android emulators. It is also easy to use and configure, and it is available free of cost for personal use.
