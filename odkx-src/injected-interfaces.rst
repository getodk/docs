.. spelling::

  odkCommon
  odkData
  odkTables
  odkSurvey
  deviceId
  src
  formIds

Injected JavaScript Interfaces
===================================

.. _injected-interfaces:

.. contents:: :local:

The Java framework on the Android device injects two Java interfaces (`odkCommonIf` and `odkDataIf`) into both Tables and Survey WebKits. Additionally, it injects one additional Java interface into each: `odkTablesIf` into Tables WebKits and `odkSurveyStateManagement` into Survey WebKits.

Within the Javascript, it is expected that all interactions with these interfaces will be done through wrapper objects. Specifically, for *odkCommonIf* and *odkDataIf*, Javascript programmers would invoke methods on the `odkCommon` and `odkData` objects defined in

  - :file:`system/js/odkCommon.js`
  - :file:`system/js/odkData.js`

The Tables-specific interface is interacted with via the `odkTables` object defined in:

  - :file:`system/tables/js/odkTables.js`

This wrapper object mostly invokes `odkCommon` to perform its actions, but does call the `odkTablesIf` injected interface's one method to load the list view portion of the split-screen detail-with-list-view layout.

The Survey interface is invoked within the Javascript that implements the survey presentation and navigation logic and should not be directly called by form designers.


.. _injected-interfaces-odkcommon:

odkCommon.js
-----------------

This creates a `window.odkCommon` object that wraps calls to the injected `odkCommonIf` Java interface. When loaded inside the App Designer, it also creates a mock implementation of the injected interface.

This `class <https://github.com/opendatakit/app-designer/blob/development/app/system/js/odkCommon.js>`_ provides support for:

  #. obtaining information about the runtime environment (e.g., Android OS version, etc.)
  #. obtaining information about the currently-selected locale.
  #. obtain the active user.
  #. obtain system properties (e.g., deviceId).
  #. emitting log messages to an application log.
  #. translations of text, media files and urls.
  #. conversion functions for retrieving and storing timestamps and intervals.
  #. storing and retrieving session variables (transient values that persist for the lifetime of this WebKit).
  #. converting relative paths of configuration files and of row-level attachments into URLs suitable for use in HTML documents (e.g., image src attributes).
  #. constructing form references used to launch ODK Survey.
  #. invoking arbitrary intents (external programs) on Android devices.
  #. obtaining the results from an intent that was previously invoked.
  #. exiting the current WebKit and specifying a return intent status value and extras bundle.

The explicit session variable interfaces (:code:`odkCommon.getSessionVariable(elementPath)` and :code:`odkCommon.setSessionVariable(elementPath, value)`) provide a mechanism to preserve the state of a webpage within the Java Activity stack so that no matter how nested the call stack to external applications becomes, it can be unwound and the state of the webpage recovered. Similarly, the invoking of arbitrary intents and the retrieving of their result intent status and extras bundle (excluding byte arrays) provides direct access to Android's native application inter-operation capabilities from within the WebKit.  This interface is used within Survey for media captures; the internal methods that accomplish this are in :file:`system/survey/js/odkSurvey.js`. Within Tables, this capability is used to navigate between HTML pages for general content, list views, and detail views (largely via the higher-level methods of the `odkTables` wrapper object). As a webpage designer, there is nothing preventing you from performing media captures from Tables web pages, or from defining custom prompts within Survey that launch into Tables list views, etc. by leveraging one or the other of the `odkSurvey` or `odkTables` objects.

.. _injected-interfaces-odkdata:

odkData.js
--------------------

This creates a :code:`window.odkData` object that wraps calls to the injected `odkDataIf` Java interface. When loaded inside the App Designer, a mock implementation of the injected interface is loaded that uses W3C SQL to emulate the injected interface's capabilities.

This class provides support for asynchronous interactions with a SQL database (internally, this is implemented via a SQLite database).

The interaction to get the active user's roles would be:

.. code-block:: javascript

    // declare a success function
    var successFn = function( resultObj ) {
      // do success handling
      var roles = resultObj.getRoles();
      // this will be a list of the roles and groups the user
      // belongs to.
    };
    // declare the failure function
    var failureFn = function( errorMsg) {
      // errorMsg is a text string. Typically the getMessage()
      // of the Java Exception that occurred during processing.
      // do failure handling
    };
    //
    // make the asynchronous request
    odkData.getRoles(successFn, failureFn);

If the request failed, the `errorMsg` is the message returned from within the Java layer. As noted, this is typically the :code:`getMessage()` of an exception.

Otherwise, the :code:`resultObj` returned contains information about the outcome. This object is a wrapper object with accessor methods defined `here <https://github.com/opendatakit/app-designer/blob/development/app/system/js/odkData.js#L349)>`_.

.. note::

  #. the color information is only present within Tables. It is not computed and returned within Survey.
  #. the display names will need to be localized before use. See the APIs provided by `odkCommon`.

.. _injected-interfaces-odktables:

odkTables.js
--------------------

As noted, this is here:

    :file:`system/tables/js/odkTables.js`

It provides methods to open Tables generic web pages and list and detail views. These are generally just wrappers for calls to `odkCommon` to invoke the intents for those views.

.. _injected-interfaces-odksurvey:

odkSurvey.js
------------------

As noted, this is here:

    :file:`system/survey/js/odkSurvey.js`

It provides methods to capture media files and. like `odkTables` these are generally just wrappers for calls to `odkCommon` to invoke the intents for those actions.

.. _injected-interfaces-other:

Other system/survey/js files
-----------------------------

These files are generally not used by web page developers. They implement the survey form execution logic and their functions will be broadly covered later in this document.


