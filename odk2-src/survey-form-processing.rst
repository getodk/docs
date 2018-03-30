.. spelling::

  ctxt
  requirejs
  combodate
  baseContext
  msg
  odkCommon
  seqAtEnd
  parsequery
  Parsequery
  tableId
  instanceId
  mdl
  arg
  columnValue
  screenManager
  mutexes

ODK Survey Form Processing
==============================

.. _form-processing:

.. contents:: :local:

The XLSXConverter converts the XLSX file defining an Survey form into a JSON representation of that form. This representation is then layered on top of the generic Survey JavaScript framework to produce the JavaScript code that is executed when filling out the form.

The primary building blocks of this generic Survey JavaScript framework are:

  * bootstrap  - for prompt UI and behavior
  * Handlebars - for HTML content rendering
  * Backbone   - for event handling within prompts
  * requirejs  - for module dependencies and loading
  * jQuery     - generic utility functions
  * underscore - generic utility functions
  * moment     - date and time handling support

Some additional libraries are use for specific widgets and capabilities (e.g., d3 for graphing, combodate for calendar widgets).

The Survey JavaScript framework then adds form navigation, data validation, data storage and data retrieval functions. Central to this framework is the **calling context** which provides a continuation abstraction for chaining and resuming processing during asynchronous interactions.

.. contents:: :local:

.. _form-processing-ctxt:

Survey Calling Contexts (ctxt)
---------------------------------------

The success and failure callbacks used within the `odkData` API are also used throughout the Survey JavaScript. These are so common, that they are passed into functions as a single "calling context" argument, generally named `ctxt`. Whereas many libraries have success and failure callbacks:

  * :code:`obj.action(successCallbackFn, failureCallbackFn);`

the Survey JavaScript would just pass in the ctxt object:

  * :code:`obj.action(ctxt);`

This `ctxt` object consists, at a minimum, of a :code:`success` function and a :code:`failure` function. The :code:`failure` function generally takes one argument which is an object containing a `message` field that holds an error message. The :code:`success` function may pass in an argument or not.

These calling contexts are created, tracked and managed by the `controller` class via:

  * :code:`window.controller.newContext( event )`  -- when needed during event processing
  * :code:`window.controller.newCallbackContext()` -- on callbacks from Java shim
  * :code:`window.controller.newStartContext()` -- special case
  * :code:`window.controller.newFatalContext()` -- special case

The ctxt object extends the baseContext defined within controller, which has:

.. code-block:: javascript

    {
    	contextChain: [],
    	append: function( method, detail ) {...},
    	success: function() {...},
    	failure: function(msg) {...},
    }

A well-written :code:`success()` or :code:`failure(msg)` function will perform its actions then call the success or failure function of the parent instance from which it is extended.  So you will often see code like this in Survey JavaScript:

.. code-block:: javascript

    var that = this;
    this.render($.extend({}, ctxt, { success: function() {
            that.postRender(ctxt);
        }, failure: function(msg) {
            ctxt.append("mymethod", "unable to render");
            ctxt.failure(msg);
    } });

Where :code:`postRender(ctxt)` will be responsible for calling the success or failure methods of the ctxt object that was extended and passed into the render() method.  The failure(msg) code, in contrast, just logs a message to the context log (via append(), discussed below), and calls the parent instance’s failure function.

By always calling the parent instance’s success or failure function, you can do interesting things, like implement mutexes (an advanced software construct) -- because you are always assured that if you extend a ctxt, that one of your failure(msg) and success() functions will always be called.

The failure(msg) function takes an argument, which is an object that may contain an optional
‘message’ parameter, which could be a description of what the failure was. This is used during validation.

The use of the ctxt object enables you to store values within the ctxt, and ensure that these are available later in your code, or, via extending it, to change the success function so that it takes an argument, etc., as needed by your code (the database layer quite frequently needs to pass values into the ctxt success method).

The append() function on the context enables you to append a log record to the context. The baseContext’s success() and failure(msg) methods both cause the accumulated log messages to be written via the odkCommon.log(). On Chrome, the log message is suppressed. On Android, it is written to the :file:`/opendatakit/{appName}/output/logging` directory and emitted in the system log if an error or warning.

The ‘seq:’ and ‘seqAtEnd:’ values emitted in these logs are useful for understanding what events are processed concurrently within the JavaScript. ‘seq’ is the sequence number of this context, and ‘seqAtEnd’ is the sequence number of the newest context in-process at the time this context completes.

Note that when interacting with other asynchronous frameworks, it is easy to convert from ctxt-based style to the success/failure function style:

.. code-block:: javascript

    fwk.action( function() { ctxt.success(); }, function() { ctxt.failure(); } );

Finally, these calling contexts are very similar to JavaScript promises. However, within the Survey JavaScript, the typical construction is to insert processing steps before taking the success or failure action of the incoming calling context. In contrast, with promises, the typical construction is to append processing steps upon completion of the promise.

In the rare cases when it is necessary to append actions after a calling context chain completes (like the Promise model), two APIs are provided:

  * :code:`ctxt.setChainedContext(aCtxt);`
  * :code:`ctxt.setTerminalContext(aCtxt);`

Chained contexts are executed in-order, depth-first, from first registered to last registered, after which all terminal contexts are executed in the order in which they were collected from within all of the executed chained contexts. In practice, the Survey JavaScript framework only makes use of terminal contexts, and those usages only register a single terminal context.

.. _form-processing-js-modules:

Survey JavaScript Modules
--------------------------

All user forms processed within Survey load the same HTML file. Form-specific content and behaviors are specified via the `window.location.hash` portion of the URL. The common HTML file is here::

    /opendatakit/{appName}/system/index.html

and its contents are:

.. code-block:: html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OpenDataKit Common Javascript Framework</title>
        <link rel="stylesheet" type="text/css" id="custom-styles" />
        <link rel="stylesheet" type="text/css" id="theme" href="libs/bootstrap-3.3.7-    dist/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="../config/assets/css/odk-survey.css" />
        <link rel="stylesheet" type="text/css" id="theme" href="libs/spinner/waitMe.css" />
    	<script type="text/javascript" src="../config/assets/framework/frameworkDefinitions.js"></script>
    	<script type="text/javascript" src="../config/assets/commonDefinitions.js"></script>
        <script type="text/javascript" src="js/odkCommon.js"></script>
        <script type="text/javascript" src="js/odkData.js"></script>
        <script type="text/javascript" src="tables/js/odkTables.js"></script>
        <script type="text/javascript" src="survey/js/odkSurvey.js"></script>
        <script type="text/javascript" src="survey/js/odkSurveyStateManagement.js"></script>
        <noscript>This page requires javascript and a Chrome or WebKit browser</noscript>
    </head>
    <body>
        <div id="block-ui"></div>
        <div class="odk-page">
            <div class="odk-screen">
                <div class="odk-toolbar"></div>
                <div class="odk-scroll">
                    <div class="odk-container">Please wait...</div>
                </div>
                <div class="odk-footer"></div>
            </div>
        </div>
        <script type="text/javascript" data-main="survey/js/main" src="libs/require.2.3.3.js"></script>
    </body>
    </html>

This loads a :file:`/config/assets/css/odk-survey.css` file that users can customize, loads the common JavaScript wrapper objects and translation files, and finally triggers `requirejs` to load the framework and (eventually) process the `window.location.hash` to load and interpret the form definition.

The `requirejs` module management framework, under the direction of the :file:`/system/survey/js/main.js` configuration and initialization file, loads the JavaScript files used by the Survey form framework.

Listed alphabetically, these are:

  - **builder** - responsible for reading the formDef.json and initializing the controller with the list of prompts in the survey.
  - **controller** - handles the logic for moving from one prompt to the next; this includes pre- and post- actions and performing the validation logic.
  - **database** - Handles the interactions with the `odkData` interface to the database. This also constructs and maintains the in-memory model description holding the form definition and the instance’s data and of the structure of the table in which it is stored.
  - **databaseUtils** - contains utility functions for transforming between the database storage strings and the JavaScript reconstructions in the model.
  - **formulaFunctions** - common functions accessible from the user's JavaScript eval environment (for use within their formulas).
  - **handlebarsHelpers** - Handlebars helper functions for use within handlebars templates. These are invoked via :code:`{{helperFunction arg1}}` or :code:`{{helperFunction arg1 arg2}}` within the handlebars templates.
  - **main** - the `requirejs` configuration and initialization file loaded via :file:`index.html` that guides the JavaScript loading process. It waits for various components to load, cleans up the WebKit URL, and invokes :code:`parsequery.changeUrlHash(ctxt)`.
  - **odkSurvey** - simple wrapper for invoking the various media capture actions exposed by Survey
  - **odkSurveyStateManagement** - this is used only within App Designer to simulate the injected Java interface of the same name.
  - **opendatakit** - a random collection of methods that don't quite belong anywhere. Some of these cache and wrap requests to the `odkCommon` layer.
  - **parsequery** - responsible for parsing the hash fragment and triggering the building of the form, the triggering the initialization of the data table, changing of the viewed page, etc.
  - **prompts** - the core set of prompts defined by the Survey JavaScript framework.  The first of these, `base`, defines the basic operation of a prompt.
  - **promptTypes** - due to the way `requirejs` works, this defines an empty object into which the prompts (above) are inserted.
  - **screenManager** - handles the rendering of a screen, including any please-wait or other in-progress notifications, and the events that initiate actions on that screen (e.g., change language, swipe left/right, back/forward button clicks).  Many of those actions invoke methods on the `controller` to complete.  Note that rendering of the prompts within a screen (equivalent to an ODK Collect field-list) are handled within the definition of the screen.
  - **screens** - the core set of screen renderers defined by the Survey JavaScript framework. This includes the templating screen for customized layouts and the standard screen renderer.
  - **screenTypes** - due to the way `requirejs` works, this defines an empty object into which the screens (above) are inserted.

.. _form-processing-control-flow:

Survey Control Flow Overview
--------------------------------

.. _form-processing-control-flow-index:

:file:`index.html` Initialization Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :file:`index.html` file explicitly loads these script files:
  * **frameworkDefinitions.js** - translations for standard Survey buttons and prompts
  * **commonDefinitions.js** - application-wide translations defined by the user
  * **odkCommon.js** - wrapper object for `odkCommonIf` injected Java interface
  * **odkData.js** - wrapper object for `odkDataIf` injected Java interface
  * **odkTables.js** - wrapper object for `odkTablesIf` injected Java interface and convenience methods for Tables navigation actions.
  * **odkSurvey.js** - wrapper object providing convenience methods for media capture interactions.
  * **odkSurveyStateManagement.js** - mock object used only within App Designer to provide functionality equivalent to the injected Java interface by the same name.
  * **require.js** - the requirejs module management library
  * **main.js** - loaded indirectly by requirejs to begin the module-load process

The relatively rapid loading of :file:`index.html` very quickly presents ‘Please wait...’ to the user. This is not internationalized. Once the Survey framework is initialized, this will change to an internationalized prompt (using the `waiting_text` translations), and then be replaced by the requested screen in the form (or first screen of the form) when the form definition is fully processed.

.. _form-processing-control-flow-main:

Main
~~~~~~~~~~~

The :file:`main.js` file declares the interdependencies among the various JavaScript frameworks. It relies on `requirejs` for package dependency management and loading. The code first loads jQuery and an extended regex library (for Unicode strings). Once those are loaded, it then loads additional 3rd party libraries and the main Survey JavaScript framework files via:

.. code-block:: javascript

    require([ 'spinner', 'databaseUtils', 'opendatakit', 'database', 'parsequery',
                            'builder', 'controller', 'd3', 'jqueryCsv', 'combodate'],
      function(...) {...})

Once the ODK frameworks has loaded, the body of the function is executed. The body then initializes the parsequery object (needed to avoid circular references):

.. code-block:: javascript

    parsequery.initialize(controller,builder);

And then either triggers a reload to clean up the `window.location` value or initiates the parsing of the :file:`formDef.json` specified in the URL location.hash via:

.. code-block:: javascript

    parsequery.changeUrlHash(ctxt);

.. _form-processing-control-flow-parsequery:

Parsequery
~~~~~~~~~~~~~~~~~~~~~~

`parsequery` has two main entry points. The first:

.. code-block:: javascript

    parsequery.changeUrlHash(ctxt) {
        parsequery._parseParameters(wrappedCtxt);
        // when complete:
        that.controller.registerQueuedActionAvailableListener(ctxt, opendatakit.getRefId());

parses the formDef and calls the controller to initiate the processing of data callbacks from the Java layer.

The second entry point is `_prepAndSwitchUI`, which is called deep within the processing performed inside :code:`changeUrlHash(ctxt)` and also by the `controller` when opening a specific `instanceId` within a form. That entry point assumes that the tableId and formId have not changed from what they currently are.

:code:`parsequery._parseParameters(ctxt)` has the following flow (accomplished with many asynchronous processing steps -- arguments are omitted):

.. code-block:: javascript

    parsequery._parseParameters() {
        if ( !sameForm ) {
            controller.reset( function() {
                // webpage now displays "Please wait..." with translations
                parseQuery._parseFormDefFile();
            });
        } else {
            parseQuery._parseQueryParameterContinuation();
        }
    }

    // called to load the (new) formDef.json
    parseQuery._parseFormDefFile() {
        requirejs( "formDef.json", function() {
            parseQuery._parseQueryParameterContinuation();
        })
    }

    // called to interpret hash parameters after formDef.json loaded
    // If the tableId is changed, load information about the tableId
    // from the database layer so we know what fields are in it.
    // Otherwise, interpret the formDef.json and construct the
    // javascript objects that are used to render that form.
    // And, once the object tree is initialized, call
    // _prepAndSwitchUI() to render the specified screen in that form.
    parseQuery._parseQueryParameterContinuation() {
        if ( !sameTable ) {
            controller.reset( function() {
                // webpage now displays ‘Please wait...’ with translations
                // Load information about the tableId from the database
                // layer so we know what fields are in it.
                database.initializeTables(function() {
                    // parse and construct form objects
                    builder.buildSurvey( function() {
                        // render the specified screen in this form
                        parseQuery._prepAndSwitchUI();
                    });
                });
            });
        } else if ( !sameForm ) {
            controller.reset( function() {
                // webpage now displays ‘Please wait...’ with translations
                // parse and construct form objects
                builder.buildSurvey( function() {
                    // render the specified screen in this form
                    parseQuery._prepAndSwitchUI();
                });
            });
        } else if ( !sameInstance ) {
            controller.reset( function() {
                // webpage now displays ‘Please wait...’ with translations
                // render the specified screen in this form
                parseQuery._prepAndSwitchUI();
            });
        } else {
            // render the specified screen in this form
            parseQuery._prepAndSwitchUI();
        }
    }

    // retrieve and cache information for the instanceId (row)
    // being manipulated (if any) and render the specified screen
    // in the current form
    parseQuery._prepAndSwitchUI() {
        database.initializeInstance( function() {
            controller.startAtScreenPath(ctxt, screenPath);
        });
    }

From this flow, you can see that the rough sequence of flow is:

  #. :code:`controller.reset()` is called to display ‘Please wait...’
  #. :code:`database.initializeTables()` to retrieve metadata about the tableId.
  #. :code:`builder.buildSurvey()` to process the raw formDef.json file.
  #. :code:`database.initializeInstance()` creates the initial (largely empty) row of an instanceId (if it is new) and reads the data for the instanceId from the database (if it is pre-existing), sets the current instance id and populates the mdl with the values for that instance id.
  #. :code:`controller.startAtScreenPath()` is called to direct the Survey JavaScript framework to display the requested screen.
  #. :code:`controller.registerQueuedActionAvailableListener()` is called to initiate the processing of any Java data callbacks (e.g., responses from intents).

.. _form-processing-control-flow-builder:

Builder
~~~~~~~~~~~~~~~~~~~

Builder's only entry point is `buildSurvey`. This attempts to load several well-known files and then processes the :file:`formDef.json`.

It begins by attempting to load (in order)::

    /opendatakit/{appName}
         /config/tables/{tableId}/tableSpecificDefinitions.js
         /config/tables/{tableId}/forms/{formId}/customScreenTypes.js
         /config/tables/{tableId}/forms/{formId}/customPromptTypes.js

The file :file:`tableSpecificDefinitions.js` contains the translations described earlier.

The :file:`customScreenTypes.js` file contains user-defined screen types. These should follow the constructions of the basic screens defined in :file:`/system/survey/js/screens.js` and should be stored as property fields inside the `screenTypes` object.

The :file:`customPromptTypes.js` file contains user-defined prompt types. These should follow the constructions of the basic prompts defined in :file:`/system/survey/js/prompts .js` and should be stored as property fields inside the `promptTypes` object.

The `column_types` field in the `specification` object within the :file:`formDef.json` is a map consisting of column names and their expected column types. This is used to convert ordinary text describing a calculation into JavaScript functions that perform the calculation (via `eval`). For simplicity, these column names are interpreted independent of the sheet within the XLSX file from which the :file:`formDef.json` is constructed. The allowed values for column types is only partially extensible as it must be interpreted and processed within the builder. The valid column types are:

  * function
  * formula
  * formula(arg1[, arg2[,...]])
  * requirejs_path

Columns with the `function` type are expected to contain column values ({columnValue}) that are a text string that can be evaluated as a function definition -- e.g., {columnValue} would be something like: :code:`function() { return 3; }`.

The `formula` type and the :code:`formula(...)` type are expected to have {columnValue} be an expression that is the return value of a function. These are wrapped by the builder to construct either

.. code-block:: javascript

    function() { return ({columnValue}); }

or

.. code-block:: javascript

    function(arg1[, arg2[,...]) { return ({columnValue}); }

Function and formula column types have their content evaluated in the context of the methods exposed by `formulaFunctions` to produce JavaScript functions. Because they are evaluated within the `formulaFunctions` context, they only have limited access to the internals of the Survey framework. This intentionally limits their power and the potential for damage that they might otherwise wreak.

The `requirejs_path` type causes builder to prefix the path to the form's directory. This supports referencing custom prompt templates and, potentially, images and other media, that are stored in the form directory.

The default `column_types` map can be extended in the XLSX file by defining a `column_types` sheet with headings that are column names and a single row beneath that defines the column type for that column name.

The default `column_types` map consists of:

.. code-block:: javascript

    {
        _screen_block: 'function',
        condition: 'formula',
        constraint: 'formula',
        required: 'formula',
        calculation: 'formula', // 'assign' prompt and on calculates sheet.
        newRowInitialElementKeyToValueMap: 'formula',
        openRowInitialElementKeyToValueMap: 'formula',
        selectionArgs: 'formula',
        url: 'formula', // external_link prompt
        uri: 'formula', // queries
        callback: 'formula(context)', // queries
        choice_filter: 'formula(choice_item)', // expects "choice_item" context arg.
        templatePath: 'requirejs_path'
    }

Builder uses the `column_types` field in the `specification` object within the :file:`formDef.json` to convert fields (column names) into their appropriate types. This conversion consists of a a full traversal of content from the calculates, settings, choices, queries, and all the survey sheets in the original XLSX file.

Next, for each of the survey sheets, builder creates Backbone instances of the prompt types referenced on those sheets, one instance for each declared prompt. These instances fold the field definitions the user specified in the XLSX file on top of the default values provided by the prompt definitions (and custom prompt definitions), allowing the user to customize the prompt through explicit changes in the XLSX file. These prompt instances are used when rendering the survey.

Lastly, the builder attempts to load::

    /opendatakit/{appName}
         /config/tables/{tableId}/forms/{formId}/customStyles.css

It then attempts to load::

    /opendatakit/{appName}
         /config/tables/{tableId}/forms/{formId}/customTheme.css

Or, if that doesn't exist, it examines the formDef.json to see if there was a `theme` defined on the `settings` sheet of the XLSX file and attempts to load::

    /opendatakit/{appName}
         /config/assets/css/{theme}.css

And, lastly, it examines the formDef.json to see if there was a `font-size` defined on the `settings` sheet of the XLSX file and attempts to set it in the body:

.. code-block:: javascript

    $('body').css("font-size", fontSize.value);

.. _form-processing-control-flow-database:

Database
~~~~~~~~~~~~~~~~~~~~~~

The Survey database layer is a fairly thin wrapper around the `odkData` object. It maintains a cache of all of the field values in the referenced instanceId (row) within the current form. This cache is synchronously referenced and modified within the presentation layer and asynchronously updated via calls to the `odkData` object. In general, these asynchronous writes occur during lose-focus event processing.

Additionally, it maintains a copy of the properties of that table (e.g., display name of the table and display names of the fields) and a description of the field types in the database table (the table definition). These are returned via the `odkData` object. This information is used within Survey to enable formulas to refer to field values either via their `elementPath` or via the database column in which they are stored (`elementKey`). A prime example of this is a *geopoint*. If the name of the *geopoint* field is `mylocation` then the individual `latitude`, `longitude`, etc. values are maintained within the cache as individual keys within a `mylocation` object -- you can refer to them naturally as `mylocation.latitude`, `mylocation.longitude`, etc. This is the `elementPath` representation of these fields. However, within the database layer, these are stored as individual columns with column names of `mylocation_latitude`, `mylocation_longitude` etc. That is the `elementKey` representation. A similar transformation occurs for file attachments and any user-defined complex data type (multi-valued prompts). Simple select-multiple prompts, which manipulate arrays of values, have an `elementPath` representation within the cache as a Javascript array of selected values. Within the database layer, their `elementKey` representation is a JSON serialization of this array (in contrast, select-multiple prompts that reference linked tables would not store their selections in the dominant data table but rely upon filter conditions and storing a (foreign) key in the subordinate table, or in an association table, to establish their linkage).

The support this synchronous cache and this data abstraction, the main entry points for this layer can be divided into 4 sections:

  #. :ref:`form-processing-control-flow-database-retrieving`
  #. :ref:`form-processing-control-flow-database-create-row`
  #. :ref:`form-processing-control-flow-database-modify-row`
  #. :ref:`form-processing-control-flow-database-utility`

.. _form-processing-control-flow-database-retrieving:

Retrieving Information About a Database Table
"""""""""""""""""""""""""""""""""""""""""""""""""

Two methods:

  - :code:`initializeTables(ctxt, formDef, tableId, formPath)`
  - :code:`readTableDefinition(ctxt, formDef, tableId, formPath)`

The first is called during the initial loading of the form; the second is used by linked table prompts.

.. _form-processing-control-flow-database-create-row:

Creating and Deleting a Database Row
""""""""""""""""""""""""""""""""""""""

Five methods:

  - :code:`initializeInstance(ctxt, model, formId, instanceId, sameInstance, keyValueMap)`
  - :code:`get_linked_instances(ctxt, dbTableName, selection, selectionArgs, displayElementName, orderBy)`
  - :code:`save_all_changes(ctxt, model, formId, instanceId, asComplete)`
  - :code:`ignore_all_changes(ctxt, model, formId, instanceId)`
  - :code:`delete_checkpoints_and_row(ctxt, model, instanceId)`

The first method, `initializeInstance` is used to initialize the synchronous cache with data values. It takes a boolean, `sameInstance` that is true if this is a reload of values for the current `instanceId` (row). It also takes a map of data changes `keyValueMap` to apply to this instance.

If `sameInstance` is true, this array is ignored.

If `sameInstance` is false and `instanceId` is null (we are not yet editing a row) then any initial values for the form's session variables that are specified in the `keyValueMap` are applied, and any initial values for any of the row's fields are ignored.

If `sameInstance` is false and `instanceId` is not null, the row's values are fetched from the database. If the row does not exist, it is initialized with the default values specified in the form for each of the row's fields, and then those changes are overlaid with the changes specified in the `keyValueMap`. And, finally, any initial values for the form's session variables that are specified within the `keyValueMap` are applied.

The second method, `get_linked_instances` is used by linked table prompts to retrieve rows from other data tables (e.g., for linked table prompts).

The remaining methods (`save_all_changes`, `ignore_all_changes` and `delete_checkpoints_and_row`) manage the retention and deletion of the row in the database table.

.. _form-processing-control-flow-database-modify-row:

Getting and Modifying Fields In a Database Row
"""""""""""""""""""""""""""""""""""""""""""""""""

Five methods:

  - :code:`setValueDeferredChange( name, value )`
  - :code:`getDataValue(name)`
  - :code:`getInstanceMetaDataValue(name)`
  - :code:`applyDeferredChanges(ctxt)`
  - :code:`setInstanceMetaData(ctxt, name, value)`

The first 3 of these methods are the standard setters and getters of values. In general, the metadata fields of a row are read-only within Survey JavaScript. For this reason, there is no synchronous setter method for these fields.

The last 2 methods, `applyDeferredChanges` and `setInstanceMetaData`, are used internally within the Survey JavaScript framework to flush the changes in the synchronous cache through to the database via calls to `odkData`. Nearly all manipulation of a row's instance metadata is done within the Java layer. The exception is the changing of the current row's locale, which is effected via the call to `setInstanceMetaData`.

.. _form-processing-control-flow-database-utility:

Utility Functions for Parsing Selection and Order-By Clauses
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Two methods:

  - code:`convertSelectionString(linkedModel, selection)`
  - code:`convertOrderByString(linkedModel, order_by)`

These functions examine where clauses and order-by clauses to replace any `elementPath` expressions with `elementKey` values. Because this is not within the database layer, these conversions are not entirely fool-proof.

.. _form-processing-control-flow-controller:

Controller
~~~~~~~~~~~~~~~~~~~

The initial load of a form ends with a call to :code:`controller.startAtScreenPath()` followed by a call to  :code:`controller.registerQueuedActionAvailableListener()`.

The `controller` object is responsible for navigating the form, ensuring that required fields are populated, that constraints are applied, that all validation logic is executed, and that appropriate actions are taken when the user launches an external application (e.g., for media capture), launches a sub-form, saves the form, exits without saving, or elects to delete a row from the database.

To implement *back button* functionality, the controller maintains a history of how the user has navigated through the form. This navigation history is necessary because there is no fixed execution path through an Survey form (user-directed navigation is one of the big changes between the javarosa-based tools and Survey).  The `odkSurveyStateManagement` injected Java interface provides the underlying storage mechanism for this functionality and is directly called by `controller` during its processing.

The types of actions that the controller can perform, and how these are defined in the `formDef.json` will be described later in this document. At this time, it is sufficient to know that the controller is executing a program that performs actions, such as the rendering of a screen containing one or more prompts, as well as performing conditional and unconditional branches within that program.

The controller's progress through this program is tracked by the history stack maintained within `odkSurveyStateManagement` and the top of that history stack identifies the operation which the controller is currently executing. The controller's (vastly simplified) form processing flow is as follows:

.. code-block:: javascript

    controller.startAtScreenPath(ctxt, screenPath) {
        var op = operation corresponding to screenPath.
        controller._doActionAt(op);
    }
    //
    // starting at the operation referenced by 'op',
    // execute operations until a screen is rendered
    controller._doActionAt(op) {
        controller._doActionAtLoop(op);
        // when the above completes, we are
        // given a screenOp (screen rendering
        // operation) to transition to, or
        // have already produced a pop-up to
        // communicate an error to the user.
        if ( screenOp !== null ) {
            controller.setScreenWithMessagePopup(ctxt, screenOp, ...);
        }
    }
    //
    // main execution loop
    controller._doActionAtLoop(op) {
        while () {
            switch ( op._token_type ) {
            case "goto_label":
                // jump (possibly conditionally)
                // to another operation
                break;
            ...
            // other control flow options
            // some of these can return out
            // of this while without returning
            // a screen rendering operation.
            // any that do will have already
            // produced an alert or error pop-up
            ...
            case "assign":
                // do assignment
                break;
            case "begin_screen":
                // render a screen
                return op; // the ‘screenOp’ in _doActionAt();
            }
        }
    }
    //
    // render a screen
    controller.setScreenWithMessagePopup(ctxt, screenOp, options, msg) {
        // set up a 500ms delay timer to render the ‘msg’ pop-up
        // so that the UI can settle on the new page before we
        // display the message. Otherwise, it might be lost
        // during the rendering of the screen.
        setTimeout(function() {
            screenManager.showScreenPopup(m);
        }, 500);
        screenManager.setScreen(ctxt, screenOp, options);
    }

i.e., the processing flow eventually calls `screenManager` to display a screen (via `setScreen(ctxt, screenOp, options)`) and perhaps also shows a pop-up with some sort of alert or error message (via `showScreenPopup(m)`).

When the *next button* is pressed or the screen is swiped forwards, the framework calls :code:`controller.gotoNextScreen()` which verifies that all required fields are filled-in and all constraints are applied. It then triggers much the same processing sequence -- calling `doActionAt()` with the operation *after* the currently-rendered screen.

When the *back button* is pressed or the screen is swiped backward, the framework calls :code:`controller.gotoPreviousScreen()` which pops the operation history stack for the current survey sheet until a screen-rendering operation is found, and that screen is then rendered. And, if the history for the current survey sheet is exhausted, then the contents screen for that sheet is displayed.

Finally, returning to the discussion of the control flow on the initial load of a form, after the current screen is rendered, the call to :code:`controller.registerQueuedActionAvailableListener()` causes an action listener to be registered with `odkCommon` and then calls that listener to process any results that became available before the listener was registered. If there are any results from a previous :code:`odkCommon.doAction(...intentArgs...)` request (e.g., a media-file capture request), then the controller's action listener will interpret the results to identify what prompt in the current screen should receive and process these results and then invoke that prompt to complete the processing. Otherwise, if there are no results, no additional actions are taken.  This completes the control flow on the initial load of the form.

.. _form-processing-control-flow-screenManager:

ScreenManager
~~~~~~~~~~~~~~~~~~~~~~

The screenManager provides event handling for swiping and the navigation bars at the top and bottom of a screen. It delegates to the `screen` object to construct the DOM representation for that content and also delegates to the `screen` object to register and unregister event handlers for any other DOM elements via calls to :code:`recursiveUndelegateEvents()` and :code:`recursiveDelegateEvents()`. Those event handlers are expected to be defined in the Backbone-based `screen` objects and `prompt` objects.

The high-level actions of the screen manager are:

.. code-block:: javascript

    screenManager.setScreen(ctxt, screen) {
        // show "loading..." spinner
        screenManager.showSpinnerOverlay();
        // stop processing all events on the current screen
        screenManager.disableSwipeNavigation();
        screenManager.activeScreen.recursiveUndelegateEvents();
        // construct the DOM objects in the page (heavily nested)
        screen.buildRenderContext(... {
            screen.render(... {
                screenManager.activeScreen = screen;
                // replace the screen
                screenManager.$el.find(".odk-page").replaceWith(screen.$el);
            });
        });
        //
        // and via a ctxt.terminalContext()  registration
        // so that the DOM replacement and redraw can take effect
        screenManager.activeScreen.afterRender();
        screenManager.activeScreen.recursiveDelegateEvents();
        screenManager.hideSpinnerOverlay();
    }

.. _form-processing-control-flow-screen:

Screen
~~~~~~~~~~~~~~~~

The `screen` object determines the set of prompts that should be displayed and lays them out. The custom screen example shows how this can be done within an arbitrary HTML template by using ids on DOM elements to identify where the inner HTML for a prompt should be injected.

Immediately prior to screen rendering, any unsaved changes in data values are asynchronously flushed to the database.

The `screen` object also enforces required fields and constraints and can reject any attempts by the `controller` object to move off of this screen or pop-up a confirmation for the user to accept.

See the :file:`screens.js` file.

.. _form-processing-control-flow-prompt:

Prompt
~~~~~~~~~~~~~~~~~~~~

Prompts register event handlers for their DOM elements and are responsible for restoring and saving values displayed in those DOM elements into the synchronous data cache and for validating those values and enforcing any constraints (if so directed).

See the :file:`prompts.js` file.

.. _form-processing-controller-actions:

Survey Controller Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned earlier, the main processing loop within the `controller` executes a program derived from the form's XLSX file and encoded in the `formDef.json`. The 10 primitive operations in this program are described in :doc:`survey-controller-actions`.
