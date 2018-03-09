.. spelling::

 fastlane
 screengrab
 Screengrab
 Gradle
 gradle
 androidTest
 apks
 sdk
 

Automating Form-Widgets Guide
===================================

This guide gives information on how to automate generation of screenshots for form-widgets guide as well as regenerating form-widgets guide whenever new widgets are added.

.. _screenshot-screengrab:

Screenshot Generation using Screengrab
----------------------------------------

`Screengrab <https://docs.fastlane.tools/actions/screengrab/>`_ is a command line tool, provided by fastlane. fastlane is an open source platform, which provides a toolchain and automates tasks like generating screenshots, dealing with code signing, and releasing your application. Screengrab can be configured to load up different locales, run all the UI tests and take screenshots during the execution of the test on various devices. 

.. _setting-screengrab:

Setting up Screengrab
~~~~~~~~~~~~~~~~~~~~~~~~~

To configure screengrab, follow the steps given below:

.. _install-screen:

Installation
""""""""""""""""""

In the command line type, the following command to check if RubyGem is installed or not. RubyGems is a package manager for the Ruby programming language that provides a standard format for distributing Ruby programs and libraries (in a self-contained format called a *gem*). If Ruby is installed, the command given below would return the version number.

.. code-block:: console

  $ gem -v

If it is not installed, you can install it using the instructions `given here <https://rubygems.org/pages/download>`_. Windows users are recommended to use `RubyInstallers <https://rubyinstaller.org/>`_.

.. note::
  
 Mac users 

After installing RubyGem install the gems:

Windows and Mac users can use the following commands:

.. code-block:: console

  $ gem install fastlane

  $ gem install screengrab

Linux users can use the commands given below:

.. code-block:: console

  $ sudo gem install fastlane

  $ sudo gem install screengrab


.. note::

 - Before proceeding further make sure you have installed adb globally that is, you can use adb from the command line irrespective of the location. The installation instructions are given :ref:`here <install-adb>`. Windows users should `download <https://devs-lab.com/usb-adb-drivers-for-all-android-devices.html>`_ Universal ADB Drivers. USB Debugging mode should be :ref:`enabled <enable-usb-debugging>`.

 - Make sure that you have `JDK 8 <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_ installed and you have `correctly set the JAVA_HOME variable <https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html>`_ in your environment to match the location of your Java installation.

Clone down ODK Collect repository
"""""""""""""""""""""""""""""""""""""""

1. Go to `ODK collect repo on Github <https://github.com/opendatakit/collect>`_ , select the :guilabel:`Clone or download` button. Copy the URL from the text box that opens up. It will be : ``https://github.com/opendatakit/collect.git``.

2. Open your terminal. Then `git clone` the repo:

  .. code-block:: console

    $ git clone https://github.com/opendatakit/collect.git
  

.. warning::

  Before cloning the repository Windows users should run the following command to avoid line-ending issues.

  .. code-block:: console

    > git config core.autocrlf false

.. _configure-build:

Configuring the Build
""""""""""""""""""""""""

`Gradle <https://gradle.org/>`_ is an advanced build toolkit which is used to automate and manage the build process, while allowing you to define flexible custom build configurations. The Android plug-in for Gradle works with the build toolkit to provide processes and configurable settings that are specific to building and testing Android applications.

Gradle and the Android plug-in run independent of Android Studio which means that you can build Android apps from within Android Studio or from the command line on your machine. If you are not using Android Studio, you can move to the next section to know how to build Collect app from the command line. If you want to use Android Studio to build the app move to :ref:`this section <build-android-studio>`.

.. _building-command-line:

Building App from the Command Line
''''''''''''''''''''''''''''''''''''''

1. :command:`cd` to your preferred directory, and create a directory named :file:`sdk`.

2. Download the command line tools from `here <https://developer.android.com/studio/index.html#command-tools>`_ and extract the downloaded zip file to the sdk directory.

3. Define the location of :file:`sdk` directory with an ANDROID_HOME environment variable, Alternatively you can use a :file:`local.properties` file to define the location.  

 - Create a local.properties file and move it :file:`collect/` directory. It must be placed in the root folder.

 - Open :file:`local.properties` file using an editor and add the following line.

   On Windows:

   .. code-block:: console

     > sdk.dir=C\:\\path-to-sdk\\sdk

   On Linux or Mac:

   .. code-block:: console

     $ sdk.dir=/path-to-sdk/sdk

4. :command:`cd` to the sdk directory and enter the following command.

  On Windows:

  .. code-block:: console

    > cd tools\bin

  On Linux or Mac:

  .. code-block:: console

    $ cd tools/bin 

5. When you run a build from the command line, Gradle can automatically download missing SDK packages that a project depends on, as long as the corresponding SDK license agreements have already been accepted using the SDK Manager. To accept the licenses, under the :file:`bin` directory, run the :command:`sdkmanager` command and accept the licenses.

  .. code-block:: console

    $ ./sdkmanager --licenses

  On Windows:

  .. code-block:: console

    $ sdkmanager --licenses

6. Android SDK Build-Tools is a component of the Android SDK required for building Android apps. To download build-tools and  platform-tools, enter the following command:

  .. code-block:: console

    $ ./sdkmanager "build-tools;26.0.2" "platforms;android-27"

  On Windows:

  .. code-block:: console

    $ sdkmanager "build-tools;26.0.2" "platforms;android-27"

7. The Gradle build system in Android Studio makes it easy to include external binaries or other library modules to your build as dependencies. :command:`cd` to the collect directory and run the command given below. The following command download and cache all the dependencies on the first run without executing the unit tests.

  .. code-block:: console

    $ ./gradlew build -x test

  On Windows:

  .. code-block:: console

    $ gradlew build -x test

8. To run UI tests on the connected devices.

  .. code-block:: console

    $ ./gradlew connectedAndroidTest

  On Windows:

  .. code-block:: console

    $ gradlew connectedAndroidTest

  A successful build indicates that UI test are working fine on the connected device.

.. note::
 
  On Windows instead of command :command:`./gradlew`, :command:`gradlew` is used.

.. _build-android-studio:

Building App from the Android Studio
''''''''''''''''''''''''''''''''''''''

1. `Download Android Studio <https://developer.android.com/studio/index.html#downloads>`_ with SDK according to your platform.

2. Here is a `tutorial <https://developer.android.com/studio/install.html>`_ on how to set up Android Studio according to different platforms.

3. Whenever you import an Android project, Android Studio starts a gradle daemon which automatically builds the project. Alternatively you can go to :menuselection:`Build--> Make Project` to trigger gradle build.

.. _generate-test-debug:

Generating Test and Debug APKs
"""""""""""""""""""""""""""""""

To generate test and debug apks, run the following command.

  .. code-block:: console

    $ ./gradlew assembleDebug assembleAndroidTest

The debug app APK will be stored in :file:`collect_app/build/outputs/apk/debug/` directory and debug tests APK will be stored in :file:`collect_app/build/outputs/apk/androidTest/debug/` directory.

.. warning::
  
  Make sure to use the apks which are generated only by using the commands :command:`./gradlew assembleDebug assembleAndroidTest` and :command:`./gradlew connectedAndroidTest`, otherwise adb may fail to install apks. Also, if the main APK and the test APK use the same library but in different versions, then gradle build may fail.

.. _generate-screenshots:

Generating Screenshots
"""""""""""""""""""""""""

1. Run the command :command:`fastlane screengrab`.

2. You will be asked to choose debug app APK (collect-debug-version-number.apk), and debug tests APK(collect-debug-androidTest-version-number.apk), provide required parameters and make sure that debug app APK and debug test APK are of same version. You can also skip this step by removing leading hash and adding app_apk_path 'path/to/your/app.apk' and tests_apk_path 'path/to/your/tests.apk' in the :file:`Screengrab` file present in :file:`collect/fastlane` directory.

Screenshots will be generated and saved to :file:`collect/fastlane/metadata/android/[locale]/images/phoneScreenshots`. An HTML file would be created with an overview of all the screenshots.

.. note::

  The setup needs to be configured once only. After the complete setup there is no need to run the :command:`gradlew` commands again, but in order to add new widgets, that is to reflect the changes made in integration test, :command:`./gradlew assembleDebug assembleAndroidTest` command should be run again.

















