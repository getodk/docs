.. spelling::
  testForm
  getHashString

Application Designer Common Tasks
====================================

.. contents:: :local:

.. _app-designer-common-tasks-designing-a-form:

ODK Survey: Designing a Form
-------------------------------

This section assumes that all of the necessary software has been installed and verified. If not, complete the instructions in the :doc:`getting-started-2-user` and :doc:`getting-started-2-architect`.

When creating a new form, the appropriate directory structure must be created. Once this directory structure is in place, an XLSX form can be created. From this XLSX form, a :file:`formDef.json` file will be generated using the XLSX Converter. This :file:`formDef.json`, in the appropriate directory, is what the system will use to create the survey form.

.. _app-designer-common-tasks-creating-directory:

Creating a Canonical Directory Structure for a New Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New forms must be placed under the :file:`app/config/tables/` directory as described in the :file:`app/config/tables/` folder section. Given a form with the name *formId*, it will have a *tableId* of the same name unless you explicitly specify otherwise. The directory structure that should be created is :file:`app/config/tables/tableId/forms/formId` (where, under many circumstances, the value for *tableId* will be the same as the value for *formId*). To get started, for Windows open a:program:`cmd` window within your :file:`Application Designer` folder (click the :program:`cmd` shortcut you created earlier), and for Mac/Unix open a :program:`terminal` window within your :file:`Application Designer` folder. Type:

.. code-block:: console

  $ grunt addtable:tableId

This will create the required directory structure for an individual table, including the forms directory. Navigate into that, and create your :file:`formId` directory. Within that directory, ODK Survey expects to find the :file:`formDef.json` that defines the form. We recommend placing the XLSX file used to generate that :file:`formDef.json` in this folder. Any custom screen or prompt templates or other media related to the form should be also placed in this directory (or in a sub-directory). For example, if you wanted to create a new form named :file:`testForm.xlsx`, the directory structure that would be have to created for this form would be :file:`app/config/tables/testForm/forms/testForm`.

.. _app-designer-common-tasks-creating-survey:

Creating an ODK Survey
~~~~~~~~~~~~~~~~~~~~~~~~~

With the proper directory structure in place, you can now create your survey form. The :doc:`xlsx-converter-intro` documentation extensively details the worksheets that will need to be created within your XLSX file to create a survey. Also, you can use the **File Browser** window of the Application Designer to navigate to example XLSX files under the :file:`app/tables/` directory. It will likely be easier to start with one of the existing example forms and modify it. The key modification would be on the settings page -- changing the values for *table_id* and *form_id* (if present).

.. _app-designer-common-tasks-generate-formdef:

Generating a :file:`formDef.json` File with XLSX Converter
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Once you have a saved your survey XLSX file, you can use the XLSX Converter to create a :file:`formDef.json`. Use the :guilabel:`Save to File System` button to save the form definition file back to the file system.

.. warning::

  The :guilabel:`Save to File System` button uses the *form_id* and *table_id* within the XLSX file to identify where to write the :file:`formDef.json` file. If you have copied the XLSX file from some other location, and forgot to edit it, it may update back to that older location! If the *form_id* is equal to the *table_id*, two additional files are written that define the table's user data fields and that define the key-value properties for the table.

You will notice that the form still does not appear in the list of forms found under the **Preview** tab of the Application Designer. In order for the form to appear, the :file:`framework.xlsx` file in the :file:`app/config/assets/framework/forms/framework/` directory must be modified, and the :file:`formDef.json` file in that same directory updated using XLSX Converter.

The :file:`framework.xlsx` file is another form definition, but it generally has no persisted data. In this case, it only presents a list of forms and allows you to open them.

The modifications to the :file:`framework.xlsx` are as follows. Assuming you have created a :file:`testForm.xlsx`, the appropriate directory structures for :file:`testForm.xlsx`, and then properly generated and saved the :file:`formDef.json:`, the following lines would need to be added into the :file:`framework.xlsx` **survey worksheet**.

.. csv-table:: Example Framework Survey Worksheet
  :header: "branch_label", "url", "clause", "condition", "type", "values_list", "display.text", "display.hint"

  "testForm",
  , "''?' + opendatakit.getHashString('../config/tables/testForm/forms/testForm/',null)",,, "external_link",,"Open form",
  ,,"exit section",

The following changes will also need to be made to the :file:`framework.xlsx` **choices worksheet**

.. csv-table:: Example Framework Choices Worksheet
  :header: "choice_list_name", "data_value", "display.text"

  "test_forms", "testForm", "testForm"

The changes to the choices sheet adds the *testForm* form as one of the choices that is shown in the *user_branch* prompt (a user-directed branching prompt type). The changes on the ``survey sheet`` add a branch label, *testForm*, that matches the *data_value* from the ``choices sheet`` (this branch label will be jumped to if the user selects the *testForm* selection on the *user_branch* screen). The new branch label then renders an *external_link* prompt type that has the necessary arguments to open the *testForm*.

Once you have made these changes and used XLSX Converter on the :file:`framework.xlsx` file to update the :file:`app/config/assets/framework/forms/framework/formDef.json` file, you should see your new form show up in the **Preview** tab of the Application Designer. Clicking on that should open your form.

.. _app-designer-common-tasks-debugging-survey:

Debugging your Survey
"""""""""""""""""""""""""

The XLSX Converter should report most problems with your survey.

If the form is not being rendered correctly but your survey generates a :file:`formDef.json` without an error, first try purging the database (dropping all the existing data tables) using the :guilabel:`Purge Database` button on the **Preview** tab. You will typically need to purge the database whenever you add or remove fields from your form or change their data type.

If that does not resolve the issue, try stopping the :program:`grunt` command (on Windows, :kbd:`Control-C` should produce a prompt asking to confirm whether to stop or not. On Mac, :kbd:`Control-C` kill the process with no prompt.), and re-running it. :program:`Grunt` can sometimes get overwhelmed with changes and stop working. After restarting, test your form.

If there are other problems, the contents of the JavaScript Console will be helpful to the ODK core team for debugging. Open the JavaScript Console by clicking the icon with the three bars in the top right, select :guilabel:`More Tools`, select :guilabel:`Developer Tools`, and then select the :guilabel:`Console` tab. Select all of the debugging output, then copy it, save it to a file, and post it to |forum|_ or create a ticket on the `Github Issue Tracker <https://github.com/opendatakit/opendatakit/issues>`_.

.. _app-designer-common-tasks-move-to-device:

Moving the New ODK Survey Form to a Device
""""""""""""""""""""""""""""""""""""""""""""

.. note::
  You must have USB debugging enabled on your device in order to perform this step. See `these instructions <https://www.phonearena.com/news/How-to-enable-USB-debugging-on-Android_id53909>`_ for help.

In order to see these changes on an Android device, you must first have ODK Survey installed on your device. Then:

  #. Connect the device to your computer via a USB cable
  #. Open a :program:`cmd` or :program:`terminal` window within the :guilabel:`Application Designer` directory (the one containing :file:`Gruntfile.js`), as described in the :doc:`app-designer-directories` documentation.
  #. Type:

.. code-block:: console

  $ grunt adbpush

This will copy all of the files under config onto your device. You should then be able to launch ODK Survey, and it will display your form in its list of forms. Click the form to open it.

More :program:`grunt` commands can be found in `Pushing updates to the Device`_.

.. _app-designer-common-tasks-design-view:

ODK Tables: Designing a Custom View
-------------------------------------

One of the most powerful aspects of ODK Tables is its ability to run HTML and
JavaScript pages as the skin of the app. Through a JavaScript API presented to these files, you can query the database and control the app.

Writing an app using html/js yields a lot of power. However, it can lead to a complicated design cycle.

The html/js files you write rely on the JavaScript API implemented within the ODK Tables APK to vend data-table values into your HTML pages, where they can be displayed as a list of items, as a detail view of a single item, or graphed in any number of ways. This JavaScript API, since it is implemented in the APK, makes it difficult to debug your custom views off the phone. Long-term, we intend to support this through a more capable Application Designer environment. At present, the only way to test your HTML pages is on the device. Fortunately, on Android 4.4 and higher, :program:`Chrome` can access the browser Console and set breakpoints on the device, providing a clumsy but viable debug environment.

.. _app-designer-common-tasks-understanding-web-file:

Understanding the Web File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several pieces of boilerplate you have to include in your own code in order to debug the files in :program:`Chrome`.

In the ODK Application Designer, use the file browser to open the :file:`config/tables/Tea_houses/html/Tea_houses_list.html` file for the list view of the *Tea_houses* table. Right-click and select :guilabel:`View Frame Source`. This shows the contents of that file. The important part to note is the following lines in the ``<head>``:

.. code-block:: html

  <script type="text/javascript" src="../../../assets/libs/jquery.js"></script>
  <script type="text/javascript" src="../../../../system/js/odkCommon.js"></script>
  <script type="text/javascript" src="../../../../system/js/odkData.js"></script>
  <script type="text/javascript" src="../../../../system/tables/js/odkTables.js"></script>

In the first line you are making the :program:`jQuery` object available to your code. :program:`jQuery` is a powerful, commonly used set of functions for accessing and performing actions within a webpage. In the second two lines you are adding the *odkCommon*, *odkTables*, and *odkData* objects if they are not already provided by the browser environment. When running on the device, the ODK Tables APK will provide these, and the contents of these files will be ignored. When running in Application Designer on your computer, these files provide the approximate functionality of the APK, allowing you to create and debug your scripts. However, at the moment, these implementations make use of RequireJS, which the ODK Tables HTML files do not use (RequireJS is extensively used by ODK Survey). This causes these to break in Application Designer.

.. _app-designer-common-tasks-writing-web-file:

Writing Your Own Web Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To write your own file, first decide on the *tableId* for your table and instantiate a directory using the :program:`grunt` command:

.. code-block:: console

  $ grunt addtable:tableId

This :program:`grunt` task creates the needed directory structures and also constructs the HTML and JavaScript files with the necessary features for working within the :program:`Chrome` development environment.

These files need content from your data-table in order enable you to begin creating your custom screens. We recommend that you first design an ODK Survey form to facilitate populating the table and then set up a :file:`tables.init` file to auto-populate the form with test data. Then, as you shut down and restart your app, it will auto-load that test data.

After that, you can deploy your app to your device and open ODK Tables onto the custom view (see the ``properties`` sheet section of the XLSX Converter for how to specify the HTML file that should be opened). Once it opens, you can use the :program:`Chrome` browser on your computer to inspect for devices and connect to this custom screen on your Android device, and debug from there.

.. warning::
  The edit-debug cycle is awkward because you must make the HTML or JavaScript change on your computer then push the change to your device, and reload the page (for example, by rotating the screen). When you do rotate the screen, however, it is rendered in a new web page, necessitating connecting to that new page to resume debugging (the prior page sits idle and will eventually be destroyed. If you don't see any activity, it is likely because you are pointing at the wrong web page. Return to inspect devices, and select the newest page).

As with ODK Survey, you can use the JavaScript Console to look for and fix errors in your HTML/JavaScript. If you are having trouble please check on the |forum|_. Keep in mind that the debug objects only emit a subset of the data in your ODK Tables database.

.. _app-designer-common-tasks-pushing:

Pushing updates to the Device
-------------------------------

.. note::
  You must have USB debugging enabled on your device in order to perform this step. See `these instructions <https://www.phonearena.com/news/How-to-enable-USB-debugging-on-Android_id53909>`_ for help.

There are several times during app development where you will need to push and pull files to and from the phone. You will have to open one of the ODK tools on the device before these commands succeed.

 - The :command:`push` command is used to push the entire app directory to the mobile device.
 - The :command:`pull` command is used to pull the database or exported CSVs from the device to the desktop computer.

.. tip::
  Exported CSVs can be used to set up :file:`tables.init` to load test data.

:program:`Grunt` tasks have been written in :file:`Gruntfile.js` that perform these operations for you.

These commands can be run anywhere within the :file:`Application Designer` directory.

  - :command:`grunt adbpush`: Pushes everything under the app directory to the device.
  - :command:`grunt adbpull-db`: Pulls the database from the device to the PC.
  - :command:`grunt adbpull-csv`: Pull the exported CSVs from the device to the PC.

The pull commands will place the pulled content in the :file:`app/output/` directory.

The database is a :program:`SQLite` database and can be viewed using :program:`SQLite Browser`. This tool can also be used to view the content of the database used by :program:`Chrome` on your computer (the location of that file is OS dependent).

If you pull the CSV files, they will be under the :file:`output/csv/` directory. You can then copy them to the :file:`config/assets/csv/` directory and set up the :file:`tables.init` file to read them in order to provision test data for your development effort. If you need any of this data in production, you will want to sync to a server then export the CSV files and copy them to the :file:`config/assets/csv/` directory so that they have all of their metadata field values populated.

.. tip::
  Running :command:`grunt adbpull` will perform all the pull tasks.

.. tip::
  There are a number of additional grunt tasks available. Assuming you have installed grunt and node, you can view the available tasks by running :command:`grunt --help` anywhere in the repo.

