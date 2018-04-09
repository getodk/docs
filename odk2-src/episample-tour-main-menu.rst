Main Menu
===================

.. image:: /img/episample-tour/episample-main-menu.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _episample-tour-main-menu-function:

Function
----------------

The Main Menu module is the hub to launch the other modules. The currently selected place name is displayed along the top for convenience.

The buttons that launch other modules can be dynamically added and removed via the Settings screen in the :doc:`episample-tour-config` module.

.. _episample-tour-main-menu-implementation:

Implementation
------------------

The file :file:`assets/eps_main_menu.html` is launched by the :guilabel:`Select` button in the :doc:`episample-tour-config` module. It provides a basic skeleton for this UI, but most of this screen's elements are dynamic. They are defined in :file:`assets/js/eps_main_menu.js`.

The file :file:`eps_main_menu.js` creates the buttons to launch the various modules of this application. It selectively hides these buttons if the configuration dictates this (see the :code:`init()` function). It also handles setting up the state for launching each of these modules.

To launch the :doc:`episample-tour-geo-survey` (with the :guilabel:`Collect` button), no setup is required. A direct call to :code:`odkTables.launchHTML(...)` will suffice. This is true of the :doc:`episample-tour-task-gen` (with the :guilabel:`Select` button) as well.

To launch the :doc:`episample-tour-nav`, a query must be passed that selects the points to which this particular user should navigate. The call happens with this function: :code:`odkTables.openTableToNavigateView(...)` which queries the *Census* table for these points (see the :doc:`episample-tour-geo-survey` for how this table is populated). The preceding code dynamically generates the SQL :code:`WHERE` clause and :code:`SELECT` arguments. This view is also opened with a :code:`dispatchStruct`, which triggers the Action-Callback workflow.

The launch of the :doc:`episample-tour-nav` is automatic, unlike the manual button pressing of the other modules. This occurs via the Action-Callback workflow triggered when the Navigation module is launched. See the :code:`actionCBFn()` function and the :code:`odkCommon.registerListener(...)`, :code:`odkCommon.viewFirstQueuedAction(...)`, and :code:`odkCommon.removFirstQueuedAction(...)` functions. When the Navigation module completes its action, the result is handled by this function. If the result indicates to do so, the Household Survey module will be launched via :code:`odkTables.editRowWithSurvey(...)` (using the configured Form ID).

The Household Survey is also launched with the Action-Callback workflow. When it returns, the results are used to update the *Census* table to match its corresponding form's completion status.

The currently selected location is displayed at the top by reading the value from :code:`localStorage`.


.. _episample-tour-main-menu-implementation-files:

Files
~~~~~~~~~~~~~~~~~~

  - :file:`assets/eps_main_menu.html`
  - :file:`assets/js/eps_main_menu.js`

.. _episample-tour-main-menu-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~

None

.. _episample-tour-main-menu-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~

  - *Config*
  - *Census*

