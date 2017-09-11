*************************
File Structure of Collect
*************************

This document describes the file structure of the Collect app. For complete understanding, it is advisable to follow this document while viewing the `Collect app's repo <https://github.com/opendatakit/collect/>`_. 

An android project can consist of multiple app modules with their own configurations and settings. In this project, we just have one one app module, named :file:`collect_app`. This module further contains other subdirectories which are described below:

.. _src-files:

Source files
~~~~~~~~~~~~

The :file:`collect-app/src/` contains the source files associated with the project, like activity "controller" files as well as the models and helpers. This further has other subdirectories:
  
- :file:`src/main/` - Contains the "main" sourceset files: the Android code and resources shared by all build variants. This also contains the :file:`res/` folder, which contains all the resource files associated with your project. All graphics, strings, layouts, and other resource files are stored in the resource file hierarchy under the **res** directory.

  - :file:`src/main/assets/` - Contains file that should be compiled into an .apk file. You can navigate this directory in the same way as a typical file system using URIs and read files as a stream of bytes using the AssetManager.

  - :file:`src/main/AndroidManifest.xml/` - Describes the nature of the application and each of its components.


- :file:`src/androidTest/` - Contains code for instrumentation tests that run on an Android device.

.. _libs-files:

Libraries
~~~~~~~~~

The :file:`collect_app/libs/` contains private libraries used in the project. The libraries are mostly copied as .jar files in this folder. 

.. _gradle-files:

Gradle
~~~~~~

Gradle is the build configuration of the system. This build system automatically takes all the source files (.java or .xml), then applies the appropriate tool (e.g. takes java class files and converts them to dex files), and groups all of them into one compressed file, which we later use as APK. 

You might notice that there are two gradle systems defined in the project. The first one, :file:`collct_app/build.gradle/`, is specific for a single module. And the other one, :file:`build.gradle/` is present in the top level project directory. This specfies the configurations which are to be applied globally across all the modules of the project.

