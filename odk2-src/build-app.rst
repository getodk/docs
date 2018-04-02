.. spelling::
  testForm
  getHashString
  tableId
  isAdult
  yesno
  prepopulate
  defaultViewType
  detailViewFileName
  listViewFileName

Building an Application
====================================================

.. _build-app:

This will walk you through the steps of building a Data Management Application from scratch. The goal is to start with an empty folder and show you the necessary steps to create a working application that runs on you Android device.

.. note::

  This section covers topics useful to Deployment Architects. A Deployment Architect is an author of a data management application or a consumer of collected data. This person might create forms and edit Javascript on their computer to deploy to the Android device. Or they might download data from the server and use Excel to perform analysis. Examples include technical staff and data analytics staff.

  Other perspective definitions can be found :ref:`here <odk-2-perspectives>`.


.. _build-app-prereqs:

Prerequisites
---------------------

You will need to install:

  - :doc:`app-designer-intro`
  - :doc:`services-intro`
  - :doc:`survey-intro`
  - :doc:`tables-intro`

Before getting started, be sure you have familiarized yourself with the ODK 2 platform. The :doc:`getting-started-2-user` and :doc:`getting-started-2-architect` guides are a good place to start. The :doc:`survey-sample-app` and :doc:`tables-sample-app` are also good reference points.

.. _build-app-clean-app-designer:

Cleaning App Designer
-----------------------------------

Your freshly installed copy of Application Designer comes with lots of example forms, tables, and configuration. This is useful for learning the tools and as references when building our application, but the files should be cleaned before building your own application.

Enter your Application Designer directory, navigate to :file:`app/config/` and delete everything inside the directory.

.. _build-app-designing-a-form:

ODK Survey: Designing a Form
-------------------------------

When creating a new form, the appropriate directory structure must be created. Once this directory structure is in place, an :file:`.xlsx` form can be created. From this :file:`.xlsx` form, a :file:`formDef.json` file will be generated using the XLSX Converter. This :file:`formDef.json`, in the appropriate directory, is what the system will use to create the Survey form.

.. _build-app-creating-directory:

Creating the Directory Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New forms must be placed under the :file:`app/config/tables/` directory as described in the :ref:`app-designer-dirs-app-config-tables` section. Given a form with the name *formId*, it will have a *tableId* of the same name unless you explicitly specify otherwise. The directory structure that should be created is :file:`app/config/tables/tableId/forms/formId` (where, under many circumstances, the value for *tableId* will be the same as the value for *formId*). To get started, for Windows open a:program:`cmd` window within your :file:`Application Designer` folder (click the :program:`cmd` shortcut you created earlier), and for Mac/Unix open a :program:`terminal` window within your :file:`Application Designer` folder. Type:

.. code-block:: console

  $ grunt addtable:tableId

Where tableId is the name of your new form and table. For example, to create a census form, type:

.. code-block:: console

  $ grunt addtable:census

This will create the required directory structure for an individual table, including the forms directory. It also created basic HTML and JavaScript files, which will be covered later.

Navigate into the forms directory (:file:`app/config/tables/census/forms/` in our example), and create a directory with the form ID as its name. For our example, create a :file:`app/config/tables/census/forms/census` directory. Within that directory, ODK Survey expects to find the :file:`formDef.json` that defines the form.

.. tip::
  We recommend placing the :file:`.xlsx` file used to generate that :file:`formDef.json` in this folder as well. Survey will not use this file, but it is a useful reference and provides an easy to remember storage location in case the form needs to be updated in the future.

Any custom screen, prompt templates, or other media related to the form should be also placed in this directory (or in a sub-directory).

.. _build-app-creating-xlsx-form:

Creating an :file:`xlsx` Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the proper directory structure in place, you can now create your form. The :doc:`xlsx-converter-intro` documentation extensively details the full range of options, settings, and features available when creating a form. For this basic example, follow these instructions:

  1. Create a new file :file:`census.xlsx` inside the :file:`app/config/tables/census/forms/census` folder created in the previous section.

  2. Create a *settings* worksheet. This sheet holds general settings for the form. Create the following headers:

    - :th:`setting_name`: has defined options, such as :tc:`form_id`.
    - :th:`value`: the value of the named setting.
    - :th:`display.title.text`: the text shown to the user inside Survey.

  3. Create the following rows:

    .. list-table:: *settings* worksheet
      :header-rows: 1

      * - setting_name
        - value
        - display.title.text
      * - form_id
        - census
        -
      * - form_version
        - 20180101
        -
      * - table_id
        - census
        -
      * - survey
        -
        - Census Form

  4. Create a *survey* worksheet. This sheet defines the questions and flow of your form. Create the following headers:

    - :th:`type`: the prompt type.
    - :th:`values_list`: the name of the list of choices for a multiple choice question.
    - :th:`name`: the variable name.
    - :th:`display.promp.text`: the question the user will see in Survey

  5. Create the following rows:

    .. list-table:: *survey* worksheet
      :header-rows: 1

      * - type
        - values_list
        - name
        - display.prompt.text
      * - text
        -
        - name
        - What is your name?
      * - select_one
        - yesno
        - isAdult
        - Are you 18 years or older?

  6. Create a *choices* worksheet. This sheet contains the lists of responses you define for your multiple choice questions. Add the following headers:

    - :th:`choice_list_name`: the group name for all the responses in a choice set
    - :th:`data_value`: the data value to be selected
    - :th:`display.title.text`: the text the user will see to select this value

  7. Create the following rows:

    .. list-table:: *choices* worksheet
      :header-rows: 1

      * - choice_list_name
        - data_value
        - display.title.text
      * - yesno
        - y
        - Yes
      * - yesno
        - n
        - No

With this :file:`.xlsx` file you've created a simple Survey form that will ask the user to type in their name and respond whether they are 18 years old or not. This form will be titled *Census* and it will write to a table in the database with table ID *census*.

.. _build-app-creating-framework:

Creating :file:`framework.xlsx`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :file:`framework.xlsx` file is central to the structure of the Application Designer. It defines which forms exist. It has no persisted data. In this case, it only presents a list of forms and allows you to open them.

  1. Create the following directories: :file:`config/assets/framework/forms/`.

  2. Inside that folder, create :file:`framework.xlsx`

  3. Create an *initial* worksheet. Add header: :th:`clause` and value :tc:`do section survey`.

    .. list-table:: *initial* worksheet
      :header-rows: 1

      * - clause
      * - do section survey

  4. Create a *settings* worksheet. Add the same headers: :th:`setting_name`, :th:`value`, :th:`display.title.text`.

  5. Fill in the following rows:

    .. list-table:: *settings* worksheet
      :header-rows: 1

      * - setting_name
        - value
        - display.title.text
      * - table_id
        - framework
        -
      * - form_version
        - 20180101
        -
      * - form_id
        - framework
        -
      * - survey
        -
        - Common JavaScript Framework

  6. Create a *framework_translations* sheet. This sheet allows you to translate or customize the text displayed in buttons, messages, and other system text. Translations for your form would be specified in its own *translations* sheet in its :file:`.xlsx` file. For now, copy the :th:`string_token` and :th:`text.default` columns from one of the example :file:`framework.xlsx` files provided with the default Application Designer.

  7. Create a *choices* sheet. Add the same headers: :th:`choice_list_name`, :th:`data_value`, :th:`display.title.text`.

  8. Add the following row:

    .. list-table:: *choices* worksheet
      :header-rows: 1

      * - choice_list_name
        - data_value
        - display.title.text
      * - test_forms
        - census
        - Census Form

  9. Create a *survey* sheet. Add the headers: :th:`branch_label`, :th:`url`, :th:`clause`, :th:`condition`, :th:`type`, :th:`values_list`, :th:`display.prompt.text`.

  10. Add the following rows. They tell the software what to do if you're previewing in :program:`Chrome`.

    .. list-table:: *survey* worksheet
      :header-rows: 1

      * - branch_label
        - url
        - clause
        - condition
        - type
        - values_list
        - display.prompt.text
      * -
        -
        - if
        - | opendatakit.getPlatformInfo().container == "Chrome"
        -
        -
        -
      * -
        -
        -
        -
        - user_branch
        - test_forms
        - Choose a test form
      * -
        -
        - else
        -
        -
        -
        -
      * -
        -
        -
        -
        - note
        -
        - This is the default form.
      * -
        -
        - end if
        -
        -
        -
        -
      * -
        -
        - exit section
        -
        -
        -
        -
      * - census
        -
        -
        -
        -
        -
        -
      * -
        - | '?' + odkSurvey.getHashString('census')
        -
        -
        - external_link
        -
        - Open form
      * -
        -
        - exit section
        -
        -
        -
        -

.. _build-app-updating-framework:

Updating :file:`framework.xlsx`
"""""""""""""""""""""""""""""""""""

To add another new form to an existing :file:`framework.xlsx` file, take the following steps.

.. note::

  These steps are not part of the running example. They are provided here for reference.

Assuming you have created a :file:`testForm.xlsx`, the appropriate directory structures for :file:`testForm.xlsx`, and then properly generated and saved the :file:`formDef.json:`, the following lines would need to be added into the :file:`framework.xlsx` *survey*.

.. csv-table:: Example Framework Survey Worksheet
  :header: "branch_label", "url", "clause", "condition", "type", "values_list", "display.text", "display.hint"

  "testForm",
  , "''?' + opendatakit.getHashString('testForm')",,, "external_link",,"Open form",
  ,,"exit section",

The following changes will also need to be made to the :file:`framework.xlsx` **choices worksheet**

.. csv-table:: Example Framework Choices Worksheet
  :header: "choice_list_name", "data_value", "display.text"

  "test_forms", "testForm", "testForm"

The changes to the *choices* sheet add the *testForm* form as one of the choices that is shown in the :tc:`user_branch` prompt (a user-directed branching prompt type). The changes on the *survey* sheet add a branch label, :tc:`testForm`, that matches the :th:`data_value` from the *choices* sheet (this branch label will be jumped to if the user selects the :tc:`testForm` selection on the :tc:`user_branch` screen). The new branch label then renders an :tc:`external_link` prompt type that has the necessary arguments to open the *testForm*.


.. _build-app-generate-formdef:

Generating :file:`formDef.json`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have a saved your :file:`.xlsx` file, you can use the XLSX Converter to create a :file:`formDef.json`. Make sure your Application Designer is running (see :doc:`app-designer-launching`) and navigate to the :guilabel:`XLSX Converter` tab. Drag the :file:`.xlsx` form or select it with the :guilabel:`Choose File` button and use the :guilabel:`Save to File System` button to save the form definition file back to the file system.

For the ongoing example, convert the :file:`app/config/assets/framework.xlsx` using the instructions above. Then repeat this process with :file:`app/config/tables/census/forms/census/census.xlsx`

.. warning::

  The :guilabel:`Save to File System` button uses the *form_id* and *table_id* within the :file:`.xlsx` file to identify where to write the :file:`formDef.json` file. If you have copied the :file:`.xlsx` file from some other location, and forgot to edit it, it may update back to that older location! If the *form_id* is equal to the *table_id*, two additional files are written that define the table's user data fields and that define the key-value properties for the table.

Once you have made these changes and used XLSX Converter on the :file:`framework.xlsx` file to update the :file:`app/config/assets/framework/forms/framework/formDef.json` file, you should see your new form show up in the :guilabel:`Preview` tab of the Application Designer. Clicking on that should open your form.

.. tip::

  If you don't see your form in the :guilabel:`Preview`, try refreshing your browser.

.. _build-app-debugging-survey:

Debugging your Survey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The XLSX Converter should report most problems with your survey.

If the form is not being rendered correctly but your survey generates a :file:`formDef.json` without an error, first try purging the database (dropping all the existing data tables) using the :guilabel:`Purge Database` button on the :guilabel:`Preview` tab. You will typically need to purge the database whenever you add or remove fields from your form or change their data type.

If that does not resolve the issue, try stopping the :program:`grunt` command (on Windows, :kbd:`Control-C` should produce a prompt asking to confirm whether to stop or not. On Mac, :kbd:`Control-C` kill the process with no prompt.), and re-running it. :program:`Grunt` can sometimes get overwhelmed with changes and stop working. After restarting, test your form.

If there are other problems, the contents of the JavaScript Console will be helpful to the ODK core team for debugging. Open the JavaScript Console by clicking the icon with the three bars in the top right, select :guilabel:`More Tools`, select :guilabel:`Developer Tools`, and then select the :guilabel:`Console` tab. Select all of the debugging output, then copy it, save it to a file, and post it to the |forum|_ or create a ticket on the `Github Issue Tracker <https://github.com/opendatakit/opendatakit/issues>`_.

.. _build-app-move-to-device:

Moving Files To The Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
  You must have USB debugging enabled on your device in order to perform this step. See `these instructions <https://www.phonearena.com/news/How-to-enable-USB-debugging-on-Android_id53909>`_ for help.

In order to see these changes on an Android device, you must first have ODK Survey installed on your device. Then:

  #. Connect the device to your computer via a USB cable
  #. Open a :program:`cmd` or :program:`terminal` window within the :guilabel:`Application Designer` directory (the one containing :file:`Gruntfile.js`), as described in the :doc:`app-designer-directories` documentation.
  #. Type:

.. code-block:: console

  $ grunt adbpush

.. note::

  If it gives you an error, you may need to run :code:`grunt adbpush -f` to force it.

This will copy all of the files under config onto your device. You should then be able to launch ODK Survey, and it will display your form in its list of forms. Click the form to open it.

More :program:`grunt` commands can be found in :ref:`build-app-pushing`.



.. _build-app-design-view:

ODK Tables: Designing a Custom View
-------------------------------------

One of the most powerful aspects of ODK Tables is its ability to run HTML and
JavaScript pages as the skin of the app. Through a JavaScript API presented to these files, you can query the database and control the app.

Writing an app using HTML and JavaScript yields a lot of power. However, it can lead to a complicated design cycle.

The HTML and JavaScript files you write rely on the JavaScript API implemented within the ODK Tables APK to vend data-table values into your HTML pages, where they can be displayed as a list of items, as a detail view of a single item, or graphed in any number of ways. This JavaScript API, since it is implemented in the APK, makes it difficult to debug your custom views off the phone. At present, the only way to test your HTML pages is on the device. Fortunately, on Android 4.4 and higher, :program:`Chrome` can access the browser Console and set breakpoints on the device, providing a clumsy but viable debug environment.

.. _build-app-understanding-web-file:

Understanding the Web File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several pieces of boilerplate you have to include in your own code in order to debug the files in :program:`Chrome`.

In the default Application Designer, open :file:`app/config/tables/Tea_houses/html/Tea_houses_list.html`. Alternatively, if you are doing the running example, open :file:`app/config/tables/census/html/census_list.html`, which should have been automatically created for you. Notice the following four lines in :code:`<head>`:

.. code-block:: html

    <script type="text/javascript" src="../../../assets/libs/jquery-3.2.1.js"></script>
    <script type="text/javascript" src="../../../../system/js/odkCommon.js"></script>
    <script type="text/javascript" src="../../../../system/js/odkData.js"></script>
    <script type="text/javascript" src="../../../../system/tables/js/odkTables.js"></script>


In the first line you are making the :program:`jQuery` object available to your code. :program:`jQuery` is a powerful, commonly used set of functions for accessing and performing actions within a webpage. In the next three lines you are adding the *odkCommon*, *odkTables*, and *odkData* objects if they are not already provided by the browser environment. When running on the device, the ODK Tables APK will provide these, and the contents of these files will be ignored. When running in Application Designer on your computer, these files provide the approximate functionality of the APK, allowing you to create and debug your scripts. However, at the moment, these implementations make use of RequireJS, which the ODK Tables HTML files do not use (RequireJS is extensively used by ODK Survey). This causes these to break in Application Designer **Previews**.

More detail is provided in :doc:`tables-web-pages`.

.. _build-app-creating-web-file:

Creating Web Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To write your own file, first decide on the *tableId* for your table and instantiate a directory using the :program:`grunt` command:

.. code-block:: console

  $ grunt addtable:tableId

If you completed the example in :ref:`build-app-designing-a-form` you have already done this for the *census* table.

This :program:`grunt` task creates the needed directory structures and also constructs the HTML and JavaScript files with the necessary features for working within the :program:`Chrome` development environment.

.. note::

  These files need content from your data table to display. It is recommended that you first design a Survey form (for example, using :ref:`this guide <build-app-designing-a-form>`) which you can use to populate data. You can also prepopulate data into the database with a :file:`tables.init` file. Further instructions are available in the :ref:`tables-managing-config-at-startup` guide.

.. _build-app-creating-web-file-list-view:

Creating a List View
""""""""""""""""""""""""""

Continuing the ongoing example, open or create the file :file:`app/tables/census/html/census_list.html`. This will display a list of records collected with the form.

Ensure the file looks like this:

.. code-block:: html

  <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
  <html>
  <!--List View-->
      <head>
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <link href="../../../assets/css/list.css" type="text/css" rel="stylesheet" />
          <script type="text/javascript" src="../../../assets/commonDefinitions.js"></script>
          <script type="text/javascript" src="../tableSpecificDefinitions.js"></script>
          <script type="text/javascript" src="../../../assets/libs/jquery-3.2.1.js"></script>
          <script type="text/javascript" src="../../../../system/js/odkCommon.js"></script>
          <script type="text/javascript" src="../../../../system/js/odkData.js"></script>
          <script type="text/javascript" src="../../../../system/tables/js/odkTables.js"></script>
      </head>
      <body>
          <script type="text/javascript" src="../js/census_list.js"></script>
          <div id="wrapper">
              <div id="list"></div>
          </div>
          <script>
              $(function() { resumeFn(0); });
          </script>
      </body>
  </html>

This HTML file should be minimal. It links all the source files and provides :code:`<div>` to put the list in. Most of the work happens in the JavaScript file. Open or create :file:`app/tables/census/js/census_list.js`. Ensure its contents look like this:

.. code-block:: javascript

  /* global $, odkTables, odkData, odkCommon */
  'use strict';

  // The first function called on load
  var resumeFn = function() {

      // Retrieves the query data from the database
      // Sets displayGroup as the success callback
      // and cbFailure as the fail callback
	    odkData.getViewData(displayGroup, cbFailure);
  }

  // Display the list of census results
  var displayGroup = function(censusResultSet) {

      // Set the function to call when a list item is clicked
      $('#list').click(function(e) {

          // Retrieve the row ID from the item_space attribute
		      var jqueryObject = $(e.target);
		      var containingDiv = jqueryObject.closest('.item_space');
		      var rowId = containingDiv.attr('rowId');

          // Retrieve the tableID from the query results
		      var tableId = censusResultSet.getTableId();

		      if (rowId !== null && rowId !== undefined) {

              // Opens the detail view from the file specified in
              // the properties worksheet
				      odkTables.openDetailView(null, tableId, rowId, null);
			    }
		  });

      // Iterate through the query results, rendering list items
      for (var i = 0; i < censusResultSet.getCount(); i++) {

          // Creates the item space and stores the row ID in it
          var item = $('<li>');
          item.attr('id', censusResultSet.getRowId(i));
          item.attr('rowId', censusResultSet.getRowId(i));
          item.attr('class', 'item_space');

          // Display the census name
          var name = censusResultSet.getData(i, 'name');
          if (name === null || name === undefined) {
              name = 'unknown name';
          }
          item.text(name);

          // Creates arrow icon
          var chevron = $('<img>');
          chevron.attr('src', odkCommon.getFileAsUrl('config/assets/img/little_arrow.png'));
          chevron.attr('class', 'chevron');
          item.append(chevron);

          // Add the item to the list
          $('#list').append(item);

          // Don't append the last one to avoid the fencepost problem
          var borderDiv = $('<div>');
          borderDiv.addClass('divider');
          $('#list').append(borderDiv);
        }
        if (i < censusResultSet.getCount()) {
            setTimeout(resumeFn, 0, i);
        }
  };

  var cbFailure = function(error) {
      console.log('census getViewData CB error : ' + error);
  };

The HTML and JavaScript files also depend on a few more files. For convenience, the example reuses CSS and image files from the :doc:`tables-sample-app`. Open up a default Application Designer and copy the following files to this application's directory (using the same directory paths):

  - :file:`config/assets/css/list.css`
  - :file:`config/assets/img/little_arrow.png`
  - :file:`config/assets/libs/jquery-3.2.1.js`

.. _build-app-creating-web-file-detail-view:

Creating a Detail View
""""""""""""""""""""""""""

A *Detail View* will display the details of a record. It is commonly used alongside *List View* to provide options to browse through a data set and learn more about a particular record.

Open or create :file:`app/tables/census/html/census_detail.js` Ensure the file looks like this:

.. code-block:: html

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
      <head>
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <link href="../../../assets/css/detail.css" type="text/css" rel="stylesheet" />
          <script type="text/javascript" src="../../../assets/commonDefinitions.js"></script>
          <script type="text/javascript" src="../tableSpecificDefinitions.js"></script>
          <script type="text/javascript" src="../../../assets/libs/jquery-3.2.1.js"></script>
          <script type="text/javascript" src="../../../../system/js/odkCommon.js"></script>
          <script type="text/javascript" src="../../../../system/js/odkData.js"></script>
          <script type="text/javascript" src="../../../../system/tables/js/odkTables.js"></script>
      </head>
      <body>
          <script type="text/javascript" src="../js/census_detail.js"></script>

          <h1><span id="TITLE" class="main-text"></span></h1>

          <fieldset>
            Is over 18: <input id="FIELD_1" type="checkbox" name="isAdult" />
          </fieldset>

          <script>
              $(display);  // calls the detail display function when ready
          </script>
      </body>
  </html>

This HTML file should define the user interface elements that will be populated by database calls in the JavaScript. Open or create :file:`app/tables/census/js/census_detail.js`. Ensure its contents look like this:

.. code-block:: javascript

  /* global $, odkTables, odkData */
  'use strict';

  var censusResultSet = {};
  var typeData = {};

  // Called when the page loads
  var display = function() {

    // Runs the query that launched this view
    odkData.getViewData(cbSuccess, cbFailure);
  };

  // Called when the query returns successfully
  function cbSuccess(result) {

    censusResultSet = result;
    // and update the document with the values for this record
    updateContent();
  }

  function cbFailure(error) {

    // a real application would perhaps clear the document fiels if there were an error
    console.log('census_detail getViewData CB error : ' + error);
  }

  /**
   * Assumes censusResultSet has valid content.
   *
   * Updates the document content with the information from the censusResultSet
   */
  function updateContent() {

    nullCaseHelper('name', '#TITLE');

    if(censusResultSet.get('isAdult') === 'y') {
      $('#FIELD_1').attr('checked', true);
    }
    $('#FIELD_1').attr('disabled', true);

  }

  /**
   * Assumes censusResultSet has valid content
   *
   * Updates document field with the value for the elementKey
   */
  function nullCaseHelper(elementKey, documentSelector) {
    var temp = censusResultSet.get(elementKey);
    if (temp !== null && temp !== undefined) {
      $(documentSelector).text(temp);
    }
  }

As with the *List View*, this view requires a separate CSS file. Copy the following file from a default Application Designer, maintaining the directory path in this application's directory:

  - :file:`config/assets/css/detail.css`


.. _build-app-creating-web-file-properties:

Defining Default View Files
""""""""""""""""""""""""""""

The :file:`.xlsx` form should be updated to indicate the default view type, and where to find the HTML files for *Detail View* and *List View*. Open :file:`app/config/tables/census/forms/census/census.xlsx` and add a new worksheet titled *properties*. Add the following headers: :th:`partition`, :th:`aspect`, :th:`key`, :th:`type`, and :th:`value`.

Add the following rows to set your *List View* and *Detail View* default files:

.. list-table:: *properties* worksheet
  :header-rows: 1

  * - partition
    - aspect
    - key
    - type
    - value
  * - Table
    - default
    - defaultViewType
    - string
    - LIST
  * - Table
    - default
    - detailViewFileName
    - string
    - config/tables/census/html/census_detail.html
  * - Table
    - default
    - listViewFileName
    - string
    - config/tables/census/html/census_list.html

See :ref:`xlsx-ref-properties` for more details about specifying custom HTML files.

Run :file:`census.xlsx` through the XLSX Converter again (:ref:`build-app-generate-formdef`) to update the configuration.

After that, you can deploy your app to your device. Open Survey and fill in a few census records. Then, open Tables and select the *Census* table. This should automatically launch the *List View* defined above. Tapping an item in the *List View* should launch the detail view.

.. _build-app-debugging-tables:

Debugging Tables Web Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :program:`Chrome` browser on your computer to inspect for devices and connect to this custom screen on your Android device, and debug from there.

.. warning::
  The edit-debug cycle is awkward because you must make the HTML or JavaScript change on your computer then push the change to your device, and reload the page (for example, by rotating the screen). When you do rotate the screen, however, it is rendered in a new web page, necessitating connecting to that new page to resume debugging (the prior page sits idle and will eventually be destroyed. If you don't see any activity, it is likely because you are pointing at the wrong web page. Return to inspect devices, and select the newest page).

As with ODK Survey, you can use the JavaScript Console to look for and fix errors in your HTML/JavaScript. If you are having trouble please check on the |forum|_. Keep in mind that the debug objects only emit a subset of the data in your ODK Tables database.

.. _build-app-pushing:

Pushing and Pulling Files
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


.. _build-app-deploying:

Deploying an Application
----------------------------

This step requires that you first set up a :doc:`cloud-endpoints-intro`.

  1. Push your application to a clean device (guide: :ref:`build-app-pushing`).

  2. Authenticate as a user in the table administrator group (guide: :ref:`services-using-change-user`).

  3. Reset the App Server (guide: :ref:`services-using-reset-app-server`).

The application is now deployed to your server. Other devices can synchronize with that server to download the application and start collected data.

.. _build-app-deploying-updating:

Updating an Application
~~~~~~~~~~~~~~~~~~~~~~~~~

  - **Changing view files**: In this scenario you are not changing the database schema and your changes only affect the presentation. These changes can be synchronized to the server and do not require resetting the app server.

  - **Changing the database schema**: In this scenario you want to change the database schema, such as adding a new column. These changes cannot be synchronized and require resetting the app server.

    .. warning::

      Resetting the app server will start a new data set. If you want to keep the old data, you should download it to a separate database.
