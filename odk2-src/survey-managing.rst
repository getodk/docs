.. spelling::
  myapp

Managing ODK Survey
==========================

.. _survey-managing:

.. contents:: :local:

.. _survey-managing-prereqs:

Prerequisites
---------------------

.. _survey-managing-prereqs-required:

Required
~~~~~~~~~~~~~

To create an Data Management Application that uses ODK Survey, you will need the ODK tools:

  - :doc:`services-intro`
  - :doc:`app-designer-intro`
  - :doc:`cloud-endpoints-intro`

As well as the third party apps:

- `OI File Manager <https://play.google.com/store/apps/details?id=org.openintents.filemanager>`_

If you have not installed Survey already, follow our guide for :doc:`survey-install`

.. _survey-managing-prereqs-recommended:

Recommended
~~~~~~~~~~~~~~~~~

We also recommend:

  - :doc:`tables-intro`

ODK Tables is not required, but Tables and Survey are built to seamlessly integrate and support more robust Data Management Applications.

.. _survey-dev-environment:

Setting up a Form Development Environment
--------------------------------------------

To get started creating your own Data Management Applications, go to the :doc:`app-designer-intro` documentation.

.. _survey-designing-form:

Designing a Form
--------------------

Basic instructions for designing Survey forms are provided in the :ref:`build-app-designing-a-form`.

Survey forms are created in :program:`Excel` and saved as :file:`.xlsx` files. These are converted into form definitions using the :doc:`xlsx-converter-intro`. The linked guide should help you create and modify the files to create your own forms.

.. _survey-xlsx-reference:

Full XLSX Reference
~~~~~~~~~~~~~~~~~~~~~

Use the :doc:`xlsx-converter-reference` to find all the features you can use in your Survey forms.

.. _survey-launching-appname:

Launching With a Different AppName
---------------------------------------------

The ODK 2 tools are designed to support multiple independent Data Management Applications running on the Android device. Each of our tools has the ability to run in the context of either a default application name, or a specified application name.

By default, ODK Survey runs under the *default* application name (as does ODK Tables and the other ODK 2 tools). Application names correspond to the name of the directory under :file:`/sdcard/opendatakit` where the configuration and data files for that application are stored.

.. warning::

  Though the Android tools support multiple AppNames on the device, each :doc:`cloud-endpoints-intro` only supports one AppName at a time. For each application you have running on the device, you will need a new Cloud Endpoint that is configured with that AppName.

  Each Data Management Application will store its own server configuration. Therefore after an initial setup that points each application at its proper server, the user will not need to remember which server hosts which app.

Here we describe how to launch the ODK 2 tools into an application name of your choice with the use of widget shortcuts.

First, you must create an alternative application. As a contrived example, we will make an exact copy of the *default* application on the device with a new name. To do so, first load an application to the device (such as the :ref:`sample application <survey-sample-app-install>`). Then open :program:`OI File Manager`, navigate to the :file:`/sdcard/opendatakit` directory, and copy the *default* directory, renaming it *myapp*. You have now created the *myapp* application! It is isolated from and operates independently of the default application.

To launch and use that application:

.. _survey-launching-appname-android-4:

Android 4.x Devices
~~~~~~~~~~~~~~~~~~~~~~~~~

  #. Choose to view the installed applications.
  #. Select the :guilabel:`Widgets` tab at the top of that screen.
  #. Navigate through the available widgets, and select and hold the :guilabel:`ODK Survey Form` widget. Drag and drop it onto one of your Android launcher (home) screens.
  #. A list of available applications and forms will appear, in the form of application name for applications, and :menuselection:`application name --> form name` for each form within an application. Pick the :menuselection:`myapp` application that you created via :program:`OI File Manager`.

.. _survey-launching-appname-android-5:

Android 5.x and Higher Devices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  #. Long press an open area of the device home screen
  #. Select the :guilabel:`Widgets` tab at the bottom of resulting screen.
  #. Navigate through the available widgets, and select and hold the :guilabel:`ODK Survey Form` widget. Drag and drop it onto one of your Android launcher (home) screens.
  #. A list of available applications and forms will appear, in the form of application name for applications, and :menuselection:`application name --> form name` for each form within an application. Pick the :menuselection:`myapp` application that you created via :program:`OI File Manager`.

.. _survey-launching-appname-try-new:

Trying the New Launcher
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, play around with launching ODK Survey using this application shortcut and :guilabel:`Finalizing` a new filled-in form. Exit ODK Survey, and launch it from the applications list (so that it launches as the default application). Verify that you do not see that newly filled-in form. You can also create a new filled-in form in this default application and confirm that it is not visible in the myapp application.

This highlights the isolation of Data Management Applications in the ODK 2 tools. This is even more powerful with applications that use ODK Tables because you can create entirely isolated applications, such as a forestry app and a health clinic app, and have the forms and data entirely independent of each other.

This eliminates the need for different groups to fork the ODK code base.

.. _survey-launching-appname-make-new:

Making a New AppName
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Download a new copy of :doc:`app-designer-intro`. Clear out the :file:`config` directory as you normally would.
  2. Open :file:`app-designer/gruntfile.js`.
  3. In the :code:`modle.exports` function, find the variable :code:`tablesConfig`.
  4. Modify the value of :code:`appName` in variable :code:`tablesConfig`. This value starts as *default*. Set it to the desired new AppName.

    .. note::

      The new AppName cannot be the same as another AppName that already exists on the device.

  5. Save :file:`Gruntfile.js`
  6. Develop your Data Management Application and push it to the device the normal way (instructions in the :ref:`guide <build-app-pushing>`).

Using the above technique will keep your apps cleanly separated. You can also maintain multiple Data Management Applications in the same Application Designer instance by making alternative :file:`app-designer/app` directories and creating new :program:`Grunt` tasks to push them to the device.

