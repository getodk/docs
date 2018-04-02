.. spelling::
  Balaka
  Chiitipa

Regions
=================

Regions are tiered geographic groupings that contain a list of health facilities. The Cold Chain application is intended to scale to national deployments, and support for regions allows the large data set to be subdivided into manageable pieces. Furthermore, users in different regions are restricted to viewing and modifying data in their region. This has the dual advantage of clearing up the extra clutter that is not relevant to the user, and preventing them from making changes to data they should not have access to.

Regions affect health facility, refrigerator, and maintenance data. Every row in these three tables will be tied to a particular region. The refrigerator type data is not tied to particular regions.

Regions have multiple tiers. For example, the Balaka region is contained inside the South East Region, which is contained in the larger South region. This example has three tiers, but this is not required. The Chiitipa region is contained in the North region (there is no East/West subdivision).

.. _cold-chain-tour-regions-navigation:

Selecting a Region
---------------------------

.. image:: /img/cold-chain-tour/cold-chain-regions-navigation.*
  :alt: Selecting a Region
  :class: device-screen-vertical side-by-side

.. image:: /img/cold-chain-tour/cold-chain-regions-navigation-north.*
  :alt: Selecting a Region
  :class: device-screen-vertical side-by-side

.. _cold-chain-tour-regions-navigation-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~~

The Region Selection screen is the first screen you will encounter after being authenticated and granted access. This will differ based on the authenticated user's particular group. For example, the user authenticated in the image to the left above has a default group of **REGION_SOUTH_EAST** and the user in the image to the right above has a default group of **REGION_NORTH**. This is the same first screen shown to each user, it is populated to fit their location.

Each button in the list signifies a smaller region contained in the lager region, and the list is generated dynamically based on the region shown. The number of tiers needed to get to the smallest region level will depend on the default group of the authenticated user and the number of tiers it contains.

.. _cold-chain-tour-regions-navigation-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~

This screen is shown when :file:`assets/index.html` and :file:`assets/menu.js` execute the :ref:`authentication code <cold-chain-tour-auth-implementation>` and find a user with a valid region. This will trigger the function :code:`showSubregionButtonsAndTitle(...)` in :file:`menu.js`, which handles the tiered subregions and creates a list of buttons based on the regions one tier below the authenticated users default group region. The default group region is parsed by the :code:`util.getMenuOptions(...)` function in :file:`assets/util.js`. This default group string might, itself, contain its subgroups if the group is a higher tier. If that is the case those subregions will be listed as the buttons, and when pressed they will relaunch this screen with a URL parameter indicating the subregion as the new focus region. See :code:`addMenuButton(...)` in :`menu.js` to see how :file:`index.html` is relaunched with a new parameter.

If the sub regions are not found by the above method, then the database is queried for the sub regions: :code:`util.getDistrictsByAdminLevel2(...)` calls :code:`odkData.arbitraryQuery(...)` and queries the *health_facility* table.

When *leaf regions* or regions at the child tier that contain :doc:`cold-chain-tour-health-facilities` are reached, the region buttons will launch the :ref:`cold-chain-tour-regions-menu` screen.

.. _cold-chain-tour-regions-navigation-implementation-files:

Files
"""""""""""""""""""""

  - :file:`assets/index.html`
  - :file:`assets/js/menu.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-regions-navigation-implementation-forms:

Forms
"""""""""""""""""""""""

None

.. _cold-chain-tour-regions-navigation-implementation-tables:

Database Tables
"""""""""""""""""""""""

  - *Health Facility*


.. _cold-chain-tour-regions-menu:

Region Menu
----------------------

.. image:: /img/cold-chain-tour/cold-chain-regions-menu.*
  :alt: Region Menu
  :class: device-screen-vertical

.. _cold-chain-tour-regions-menu-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~~~

The region menu is the hub of most of the activities you might want to perform. It contains buttons to:

  - :guilabel:`View All Health Facilities`: Launch a list of :ref:`health facilities <cold-chain-tour-health-facilities-lists>` located in this region.
  - :guilabel:`Filter Health Facilities By Type`: Launch a menu listing types of :ref:`health facilities <cold-chain-tour-health-facilities-lists>`.
  - :guilabel:`View All Refrigerators`: Launch a list of :ref:`refrigerators <cold-chain-tour-refrigerators-lists>` located in health facilities in this region.
  - :guilabel:`View All Refrigerators Needing Service`: Launch a list of :ref:`refrigerators <cold-chain-tour-refrigerators-lists>` located in health facilities in this region that are marked as needing service. This is particularly useful for a maintenance worker looking for refrigerators to fix, or for administrators looking to see how many refrigerators are in need of service in a particular region.
  - :guilabel:`View Refrigerator Models`: Launch a list of :ref:`refrigerator types <cold-chain-tour-refrigerator-types-lists>` contained in the region.

.. _cold-chain-tour-regions-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HTML file :file:`assets/leafRegion.html` contains all five button definitions as they are the same no matter what region is selected or user is authenticated. The corresponding JavaScript file :file:`assets/js/leafRegion.js` localizes the strings, fills in the region name on top (from :code:`util.getQueryParameter(...)`), and adds actions to each button.

The actions are the same for each region, but the query parameters are passed along to the next view. The are generated with :code:`util.getKeysToAppendToColdChainURL(...)`. The actions are:

  - :guilabel:`View All Health Facilities`: Open the :ref:`cold-chain-tour-health-facilities-lists` to the *Map View* with :code:`odkTables.openTableToMapView(...)`. The query specifies to select all rows matching the current region from the *health_facility* table.
  - :guilabel:`Filter Health Facilities By Type`: Open the :ref:`cold-chain-tour-health-facilities-lists` to the type filtered navigation menu with :code:`odkTables.launchHTML(...)`. This API is used for customized web views.
  - :guilabel:`View All Refrigerators`: Open the :ref:`cold-chain-tour-refrigerators-lists` with :code:`odkTables.launchHTML(...)`. This does not take a query as a parameter as a normal *List View* would, but rather performs its own queries as needed based on the URL parameters passed and the user interactions on the page.
  - :guilabel:`View All Refrigerators Needing Service`: Same as above but with appropriate URL parameters and HTML file arguments.
  - :guilabel:`View Refrigerator Modesl`: Open the :ref:`cold-chain-tour-refrigerator-types-lists` with :code:`odkTables.openTableToListView(...)`


.. _cold-chain-tour-regions-menu-implementation-files:

Files
"""""""""""""""""""

  - :file:`assets/leafRegion.html`
  - :file:`assets/js/leafRegion.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-regions-menu-implementation-forms:

Forms
"""""""""""""""""""""

None

.. _cold-chain-tour-regions-menu-implementation-tables:

Database Tables
"""""""""""""""""""""""""

None
