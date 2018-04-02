Administrator Options
===========================

Administrator Options are available when the authenticated user is a Table Administrator. They provide the admin with enhanced permissions, including viewing the entire data set, creating data visualizations, deleting records, and adding new health facilities.

.. _cold-chain-tour-admin-menu:

Administrator Options Menu
----------------------------------

.. image:: /img/cold-chain-tour/cold-chain-admin-main-menu.*
  :alt: Main Menu with Administrator Option
  :class: device-screen-vertical side-by-side

.. image:: /img/cold-chain-tour/cold-chain-admin-options.*
  :alt: Administrator Options
  :class: device-screen-vertical side-by-side

.. _cold-chain-tour-admin-menu-function:

Function
~~~~~~~~~~~~~~~~~~~~~~

The Administrator Options Menu is the hub that launches the special actions the administrator can perform. It is only accessible by authenticated Table Administrators. This screen is accessed by pressing the :guilabel:`Administrator Options` button the main menu.

The administrator has access the full hierarchy of regions. Above the :guilabel:`Administrator Options` button is the list of all the highest tier regions. Tapping any of those individual options will filter the data into that region. They admin can keep advancing through the regions until they reach the child tiers, which is the same :doc:`cold-chain-tour-regions` interface.

.. _cold-chain-tour-admin-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~

This screen is shown the :file:`assets/index.html` and :file:`/assets/menu.js` execute the :ref:`authentication code <cold-chain-tour-auth-implementation>` and find a user that is a Table Administrator. This will trigger the function :code:`showSubregionButtonsAndTitle(...)` to show the top level regions (see :doc:`cold-chain-tour-regions` for details), and the :code:`addMenuButton(...)` function to add the :guilabel:`Administrator Options Button`.

When the :guilabel:`Administrator Options` button is pressed, the function :code:`odkTables.launchHTML(...)` launches :file:`assets/coldchaindemo.html`. This file defines the four option buttons, and :file:`assets/js/coldchandemo.js` handles logic that they trigger.

  - :guilabel:`View Health Facilities`: Launches :ref:`cold-chain-tour-admin-view-health-facilities` with :code:`odkTables.launchHTML(...)`.
  - :guilabel:`View Inventory`: Launches :ref:`cold-chain-tour-admin-inventory` with :code:`odkTables.launchHTML(...)`.
  - :guilabel:`View Refrigerator Models`: Launches :ref:`cold-chain-tour-admin-refrigerator-types` with :code:`odkTables.launchTableToListView(...)`.
  - :guilabel:`Add Health Facility`: Launches :ref:`cold-chain-tour-admin-add-health-facility` with :code:`odkTables.launchHTML(...)`.

.. _cold-chain-tour-admin-menu-implementation-files:

Files
"""""""""""""""""""""

  - :file:`assets/index.html`
  - :file:`assets/js/menu.js`
  - :file:`assets/js/util.js`
  - :file:`assets/coldchaindemo.html`
  - :file:`assets/js/coldchaindemo.js`

.. _cold-chain-tour-admin-menu-implementation-forms:

Forms
""""""""""""""""""""""

None

.. _cold-chain-tour-admin-menu-implementation-tables:

Database Tables
"""""""""""""""""""""""

  - *Health Facility*


.. _cold-chain-tour-admin-view-health-facilities:

View Health Facilities
----------------------------

.. image:: /img/cold-chain-tour/cold-chain-admin-view-facilities.*
  :alt: View Health Facilities
  :class: device-screen-vertical

.. _cold-chain-tour-admin-view-health-facilities-function:

Function
~~~~~~~~~~~~~~~~~~~~~

The administrator can view the full list of health facilities, unfiltered by region. This gives the administrator full control investigate, modify, or delete any facility in the data set. They can choose to find a facility with one of two methods:

  - :guilabel:`Filter By Type`:

      .. image:: /img/cold-chain-tour/cold-chain-admin-view-facilities-type.*
        :alt: View Health Facilities By Type
        :class: device-screen-vertical

    This option presents an interface similar to the :guilabel:`Filter Health Facilities By Type` option in the :ref:`cold-chain-tour-health-facilities-lists`. This version functions the same, but includes all facilities in the system. Selecting a type brings up the normal *Map View* list.

 - :guilabel:`Search By Name/ID`:

      .. image:: /img/cold-chain-tour/cold-chain-admin-view-facilities-search.*
        :alt: Search Health Facilities
        :class: device-screen-vertical

     This interface presents a search list that looks and behaves the same as :ref:`cold-chain-tour-refrigerators-lists`. It includes :guilabel:`Delete` buttons on each entry. The search box accepts facility ID and facility names.


.. _cold-chain-tour-admin-view-health-facilities-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~

The root level HTML file for this option is :file:`assets/filterHealthFacilities.html`. It defines the two buttons and :file:`assets/js/filterHealthFacilities.js` handles their logic.

  - :guilabel:`Filter By Type`: uses :code:`odkTables.launchHTML(...)` to launch :file:`assets/filterHealthFacilitiesByType.html` and :file:`assets/js/filterHealthFacilitiesByType.js`. This JavaScript file uses :file:`util.getFacilityTypesByDistrict(...)` from :file:`assets/js/util.js` to create the facility type buttons and add their facility counts. Tapping one of the facility type buttons will use :code:`odkTables.openTableToMapView(...)` to launch :ref:`cold-chain-tour-health-facilities-lists`. This workflow is similar to the :guilabel:`Filter Health Facilities By Type` option on that screen.

  - :guilabel:`Search By Name/ID`: uses :code:`odkTables.launchHTML(...)` to launch :file:`tables/health_facility/html/health_facility_lists.html` and :file:`tables/health_facility/html/health_facility_lists.js`. These files use the same search list pattern found in :ref:`cold-chain-tour-refrigerators-lists`. See :ref:`cold-chain-tour-list-logic` for details on how :file:`assets/js/list_view_logic.js` renders this user interface. The :code:`listQuery` value selects all health facilities from the *Health Facility* table. The :code:`searchParams` sets the search fields to facility ID and facility name.


.. _cold-chain-tour-admin-view-health-facilities-implementation-files:

Files
""""""""""""""""""

  - :file:`assets/filterHealthFacilities.html`
  - :file:`assets/js/filterHealthFacilities.js`
  - :file:`assets/filterHealthFacilitiesByType.html`
  - :file:`assets/js/filterHealthFacilitiesByType.js`
  - :file:`tables/health_facility/html/health_facility_list.html`
  - :file:`tables/health_facility/js/health_facility_list.js`
  - :file:`assets/js/list_view_logic.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-admin-view-health-facilities-implementation-forms:

Forms
""""""""""""""""""""

None

.. _cold-chain-tour-admin-view-health-facilities-implementation-tables:

Database Tables
"""""""""""""""""""""""

 - *Health Facility*


.. _cold-chain-tour-admin-inventory:

Inventory
--------------------

.. image:: /img/cold-chain-tour/cold-chain-admin-inventory.*
  :alt: Inventory
  :class: device-screen-vertical

.. _cold-chain-tour-admin-inventory-function:

Function
~~~~~~~~~~~~~~~~~~~

The Inventory option provides two visualizations of the state of the data set, both of which can be customized to chosen parameters.

  - :guilabel:`Refrigerator Age`

      .. image:: /img/cold-chain-tour/cold-chain-admin-inventory-graph-by-age.*
        :alt: Inventory Graph By Refrigerator Age
        :class: device-screen-vertical

     The refrigerator age visualization presents a bar chart of the current stock of refrigerators, grouped by age. This can be useful as an assessment of the quality of the stock and as an estimate of maintenance demands. This graph can be filtered by region, facility type, and power source. With this option the administrator might compare the age distribution of refrigerators in the North and the South regions when allocating upgrade budgets.

  - :guilabel:`Facility Grid Power Available`

      .. image:: /img/cold-chain-tour/cold-chain-admin-inventory-graph-by-power.*
        :alt: Inventory Graph BY Grid Power
        :class: device-screen-vertical

    The grid power visualization presents a pie chart comparing the ratios of power options available. This can be filtered by region and facility type.

The data sets to be graphed are filtered with a set of drop menus that can be chosen to specify the desired data set.

  .. image:: /img/cold-chain-tour/cold-chain-admin-inventory-filter.*
    :alt: Inventory Filter
    :class: device-screen-vertical


.. _cold-chain-tour-admin-inventory-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~

The root level HTML file for this option is :file:`assets/filterInventory.html`. It defines the two buttons and :file:`assets/js/filterInventory.js` handles their logic.

:guilabel:`Refrigerator Age` uses :code:`odkTables.launchHTML(...)` to launch :file:`assets/filterFrigInventoryForAge.html` an :file:`assets/js/filterFrigInventoryForAge.js`. The HTML file defines the three drop menus. The values specified by these drop menus are read and used as query parameter arguments when launching :file:`assets/graphFrigInventoryForAge.html` and :file:`assets/js/graphFrigInventoryForAge.js`. This JavaScript file uses query parameters provided the caller to construct a SQL query run an :code:`odkData.query(...)` call on the *Health Facility* table. The result of this call are used to construct a new query that finds refrigerators that match health facilities with an :code:`odkData.arbitraryQuery(...)` call on the *Refrigerators* table. When these results return, the :code:`frigHistogramByAge()` function uses that data and the :program:`D3` library to render the bar chart.


:guilabel:`Facility Grid Power Available` follows the same pattern as :guilabel:`Refrigerator Age` to present drop menus and use their values as query parameters. The file that renders this graph is :file:`assets/js/graphFacilityInventoryForGridPower.js`. This file also operates similarly to :file:`graphFrigInventoryForAge.js` but only performs a single query on the *Health Facilities* table. That data set is used, along with :program:`D3` by the :code:`displayHealthFacilityGridPower()` function to render the pie chart.


.. _cold-chain-tour-admin-inventory-implementation-files:

Files
"""""""""""""""""

  - :file:`assets/filterInventory.html`
  - :file:`assets/js/filterInventory.js`
  - :file:`assets/filterFrigInventoryForAge.html`
  - :file:`assets/js/filterFrigInventoryForAge.js`
  - :file:`assets/filterFacilityInventoryForGridPower.html`
  - :file:`assets/js/filterFacilityInventoryForGridPower.js`
  - :file:`assets/graphFrigInventoryForAge.html`
  - :file:`assets/js/graphFrigInventoryForAge.js`
  - :file:`assets/graphFacilityInventoryForGridPower.html`
  - :file:`assets/js/graphFacilityInventoryForGridPower.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-admin-inventory-implementation-forms:

Forms
"""""""""""""""""""

None

.. _cold-chain-tour-admin-inventory-implementation-tables:

Database Tables
""""""""""""""""""""

  - *Health Facility*
  - *Refrigerators*


.. _cold-chain-tour-admin-refrigerator-types:

Refrigerator Types
---------------------------

.. image:: /img/cold-chain-tour/cold-chain-admin-view-models.*
  :alt: Refrigerator Types
  :class: device-screen-vertical

The Refrigerator types list is identical to the interface presented in the :ref:`cold-chain-tour-refrigerator-types-lists` guide. The button is included here as a convenience. See the linked documentation for details.

.. _cold-chain-tour-admin-add-health-facility:

Add Health Facility
------------------------

.. image:: /img/cold-chain-tour/cold-chain-admin-add-facility.*
  :alt: Add Health Facility
  :class: device-screen-vertical

.. _cold-chain-tour-admin-add-health-facility-function:

Function
~~~~~~~~~~~~~~~~~~~~~

The Add Health Facility interface provides a method for an administrator to add a new health facility to the data set. The administrator must specify the region that should contain the facility (the region must be a child tier, it cannot contain other regions). When the :guilabel:`Add Facility` button is pressed, a form is launched to fill in the details of the facility.

.. _cold-chain-tour-admin-add-health-facility-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~

The root level HTML file for this option is :file:`assets/addHealthFacility.html`. It defines the button and drop menu and :file:`assets/js/addHealthFacility.js` handles their logic.

The JavaScript file reads the value from the drop menu and uses it to construct the :code:`defaults` argument to :code:`odkTables.addRowWithSurvey(...)`. The variable also includes the group permissions. The form launched is :file:`tables/health_facility/forms/health_facility/health_facility.xlsx`

This form resembles many of the other forms in this application. Mostly :tc:`select_one` prompts are grouped into screens. The region choices are populated by a query from the *queries* worksheet. The *settings, *properties*, and *model* worksheets all contain their typical values, setting the form and table IDs, setting the default view files, and mapping to the database, respectively. The *properties* file includes security properties including :tc:`unverifiedUserCanCreate` and :tc:`defaultAccessOnCreation` that restrict which users can use this form.

.. _cold-chain-tour-admin-add-health-facility-implementation-files:

Files
"""""""""""""""""""""

  - :file:`assets/addHealthFacility.html`
  - :file:`assets/js/addHealthFacility.js`
  - :file:`assets/js/util.js`
  - :file:`tables/health_facility/forms/health_facility/health_facility.xlsx`

.. _cold-chain-tour-admin-add-health-facility-implementation-forms:

Forms
""""""""""""""""""""""""

  - *Health Facility* with form ID *health_facility*

.. _cold-chain-tour-admin-add-health-facility-implementation-tables:

Database Tables
""""""""""""""""""""""""

  - *Health Facility*

