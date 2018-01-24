Using ODK Survey
=======================

.. _survey-using:

In this guide we will be demonstrating how to use ODK Survey via a guided tour of the sample application. If you have not installed it yet, follow the instructions for :doc:`survey-install-sample`. However, this guide can also be used as a reference.

.. contents:: :local:

.. _survey-using-open-form:

Opening a Form
-------------------------

Open ODK Survey. If you have successfully installed the sample application, you should be presented with a list of the six sample forms. Select the desired form.

.. note::

  The *Household Members* and *Education* forms are not intended to be called directly, but are launched from within the *Household* form.

Forms in ODK Survey are HTML. You can control the look-and-feel of the forms using CSS and add new prompt widgets by writing JavaScript. To navigate forms using OpenDataKit's look-and-feel:

  - Tap on the name of the survey in the top left to access a pop-up menu of options.
  - Tap the :guilabel:`back` or :guilabel:`next` buttons in the top right of the form to navigate through the form.

Every change you make to the data in the form is written immediately to the database as a **checkpoint** save. You may also manually save the form as *incomplete* or *finalize* the form, as you did with ODK Collect. To do so anywhere in the form, open the pop-up menu and take the desired action.

Otherwise, to exit the form without saving or cancelling your changes (and return to the form chooser screen), tap the device's back button (on newer devices, tap the back arrow icon at the bottom of the touch screen). You will be asked whether to ignore any changes since your last explicit save, whether to save your changes as an incomplete change, or whether to cancel the back (exit) action and return to the form.

.. _survey-using-syncing:

Syncing Forms and Data
--------------------------

See the instructions in the :ref:`ODK Services user guide <services-using-sync>`.

.. warning::

  If a data table has any checkpoint saves (for example, caused by form crashes), the data table will not be synchronized. Checkpoints must be resolved before sync can proceed. The user must open a form on the problem table and either delete the checkpoint or edit the checkpoint. If editing, after that is complete they must save is as either incomplete or finalized. Once the checkpoints are eliminated, the user can initiate another synchronization, and the data in this table will then be synchronized with the information on the server.

.. _survey-using-launching-appname:

Launching with a different AppName
---------------------------------------------

The ODK 2.0 tools are designed to support multiple, independent, ODK 2.0 applications running on the Android device. Each of our tools has the ability to run in the context of either a default application name, or a specified application name.

By default, ODK Survey runs under the *default* application name (as does ODK Tables and the other ODK 2.0 tools). Application names correspond to the name of the directory under :file:`/sdcard/opendatakit` where the configuration and data files for that application are stored.

Here we describe how to launch the ODK 2.0 tools into an application name of your he use of widget shortcuts.

First, you must create an alternative application. To do so, open :program:`OI File Manager`, navigate to the :file:`/sdcard/opendatakit` directory, and copy the *default* directory, renaming it *myapp*. You have now created the *myapp* application! It is isolated from and operates independently of the default application.

To launch and use that application:

.. _survey-using-launching-appname-android-4:

Android 4.x devices
~~~~~~~~~~~~~~~~~~~~~~~~~

  #. Choose to view the installed applications.
  #. Select the :guilabel:`Widgets` tab at the top of that screen.
  #. Navigate through the available widgets, and select and hold the :guilabel:`ODK Survey Form` widget. Drag and drop it onto one of your Android launcher (home) screens.
  #. A list of available applications and forms will appear, in the form of application name for applications, and :menuselection:`application name --> form name` for each form within an application. Pick the :menuselection:`myapp` application that you created via :program:`OI File Manager`.

.. _survey-using-launching-appname-android-5:

Android 5.x and higher devices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  #. Long press an open area of the device home screen
  #. Select the :guilabel:`Widgets` tab at the bottom of resulting screen.
  #. Navigate through the available widgets, and select and hold the :guilabel:`ODK Survey Form` widget. Drag and drop it onto one of your Android launcher (home) screens.
  #. A list of available applications and forms will appear, in the form of application name for applications, and :menuselection:`application name --> form name` for each form within an application. Pick the :menuselection:`myapp` application that you created via :program:`OI File Manager`.

.. _survey-using-launching-appname-try-it:

Trying the new launcher
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, play around with launching ODK Survey using this application shortcut and :guilabel:`Finalizing` a new filled-in form. Exit ODK Survey, and launch it from the applications list (so that it launches as the default application). Verify that you do not see that newly-filled-in form. You can also create a new filled-in form in this default application and confirm that it is not visible in the myapp application.

This highlights the isolation of applications in the ODK 2.0 tools. This is even more powerful with applications that use ODK Tables because you can create entirely isolated applications, such as a forestry app and a health clinic app, and have the forms and data entirely independent of each other.

This should eliminate much of the need for different groups to fork the ODK codebase.

.. _survey-using-dev-environment:

Setting up a Form Development Environment
--------------------------------------------

To get started creating your own forms, go to the :doc:`app-designer-intro` documentation.
