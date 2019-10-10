.. spelling::
  Balaka
  prepopulated

Health Facilities
========================

Health Facilities in the Cold Chain application contain the state of real world health facilities. They include general information about their status, power, location, and vaccine stock, as well as an active record of their refrigerator inventory. The intention of this application is that a user or administrator could navigate the application to a health facility and learn its basic advantages and disadvantages, and if it needs attention.

.. _cold-chain-tour-health-facilities-lists:

Lists of Health Facilities
------------------------------

.. image:: /img/cold-chain-tour/cold-chain-health-facility-list-region.*
  :alt: Health Facility List
  :class: device-screen-vertical

.. _cold-chain-tour-health-facilities-lists-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~~~~

The list of health facilities is presented as a *Map View*. The list portion of the view provides a clickable list of health facilities: clicking a facility will launch the :ref:`cold-chain-tour-health-facilities-menu`. The map portion renders that list according to the location data stored in those facilities. This can be used to navigate to facilities or to find a facility in which you may know the location better than the name.

  - **View All Health Facilities**: This screen is reached by pressing the :guilabel:`View All Health Facilities` button on the :ref:`cold-chain-tour-regions-menu` page. It lists every health facility located inside of the specified region. It is pictured above.

  - **Filter Health Facilities By Type**: This screen is reached by pressing the :guilabel:`Filter Health Facilities by Type` button on the :ref:`cold-chain-tour-regions-menu` page. It lists each type of health facility contained in the region, and a the number of health facilities that match the type:

      .. image:: /img/cold-chain-tour/cold-chain-health-facility-list-region-nav.*
        :alt: Health Facility Types
        :class: device-screen-vertical

   When one of those health facility types is selected, a list similar to the full health facility list above is rendered, but only containing health facilities within the specified region that match the chosen type. The image below is the list of :guilabel:`Regional Vaccine Store` type facilities in the Balaka region:

      .. image:: /img/cold-chain-tour/cold-chain-health-facility-list-type.*
        :alt: Health Facility List By Type
        :class: device-screen-vertical

.. _cold-chain-tour-health-facilities-lists-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - **View All Health Facilities**: This path to the health facilities list launches :file:`tables/health_facility/html/hFacility_list.html`. It contains a :code:`<div>` for the wrapper and for the list of facilities, which is populated with :file:`tables/health_facility/js/hFacility_list.js`. This JavaScript file follows a standard *List View* pattern: it retrieves the query data with :code:`odkData.getViewData(...)`, creates list items for each of the rows, adds them to the HTML view, includes a link to :code:`odkTables.openDetailView(...)` for each list item, and handles paging with :code:`resumeFn(...)` called with an index.

  - **Filter Health Facilities By Type**: This path launches :file:`assets/filterHealthFacilitiesByType.html`. It contains :code:`<div>` tags for buttons that will be filled in by :file:`assets/js/filterHealthFacilitiesByTypes.js`. This file uses the provided district to construct a query, which is executed by :code:`util.getFacilityTypesByDistrict(...)` in :file:`assets/js/util.js` and calls :code:`odkData.arbitraryQuery(...)`. This query runs on the *health_facility* table and finds all facilities in the region, groups them by type, and returns the count in each type. These results are then fed back into :file:`filterHealthFacilitiesByType.html` which creates the buttons. Each button, if pressed, will use :code:`odkTables.openTableToMapView(...)` to launch the same :file:`hFacility_list.html` used above, but with the query narrowed by facility type.


.. _cold-chain-tour-health-facilities-lists-implementation-files:

Files
"""""""""""""""""""""""""""

  - :file:`tables/health_facility/html/hFacility_list.html`
  - :file:`tables/health_facility/js/hFacility_list.js`
  - :file:`assets/filterHealthFacilitiesByType.html`
  - :file:`assets/js/filterHealthFacilitiesByType.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-health-facilities-lists-implementation-forms:

Forms
""""""""""""""""""""""""""

None

.. _cold-chain-tour-health-facilities-lists-implementation-tables:

Database Tables
""""""""""""""""""""""""""""""

  - *Health Facility*

.. _cold-chain-tour-health-facilities-menu:

Health Facility Menu
---------------------------------

.. image:: /img/cold-chain-tour/cold-chain-health-facility-menu.*
  :alt: Health Facility Menu
  :class: device-screen-vertical side-by-side

.. image:: /img/cold-chain-tour/cold-chain-health-facility-menu-buttons.*
  :alt: Health Facility Menu Buttons
  :class: device-screen-vertical side-by-side

.. _cold-chain-tour-health-facilities-menu-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~

The Health Facility Menu is a *Detail View* that lists all the information about the chosen health facility. This includes :guilabel:`Basic Facility Information`, :guilabel:`Power Information`, :guilabel:`Location Information`, and :guilabel:`Stock Information`. If any of this information is out of date or needs to be modified, the :guilabel:`Edit Health Facility` button launches an ODK Survey form that allows you to modify these values:

  .. image:: /img/cold-chain-tour/cold-chain-health-facility-edit-facility.*
    :alt: Selecting a Region
    :class: device-screen-vertical

The prompts in this form will be prepopulated with the values shown on the menu page. All correct values can be safely skipped, so you can edit only the fields that need to be corrected.

The menu also provides a button to view the :guilabel:`Refrigerator Inventory`. This will launch the :ref:`list of refrigerators <cold-chain-tour-refrigerators-lists>` contained within this health facility.

The :guilabel:`Add Refrigerator` button will launch a Survey form to create a new refrigerator. When the form is completed, this refrigerator will automatically be added to the inventory of this health facility and organized into the containing region.

.. _cold-chain-tour-health-facilities-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Detail View* for a health facility is defined by :file:`tables/health_facility/html/health_facility_detail.html`. This file lists each user interface element (including all the data values of the health facility as well as the buttons). These elements contain their labels, and the values are filled in by :file:`tables/health_facility/js/health_facility_detail.js`.

After localizing its text, this JavaScript retrieves the health facility data with the standard :code:`odkData.getViewData(...)` call. It also makes a call to :code:`odkData.query(...)` to the *refrigerators* table and finds all refrigerators that belong to this health facility. These two data sets are combined to fill in the fields on the detail view and the size of the refrigerator inventory on the button.

If the :guilabel:`Edit Facility` button is pressed, :code:`odkTables.editRowWithSurvey(...)` is called for the form *Health Facility* and pointed at this particular row ID. This form can be viewed at :file:`tables/health_facility/forms/health_facility/health_facility.xlsx`. It condenses its prompts into only a few screens with extensive use of :tc:`begin screen` and :tc:`end screen` :th:`clause` values. Notice that all text in this form also has Spanish translations provided. The form contains many static :tc:`select_one` prompts with their choices defined in the *choices* worksheet. Additionally, the :tc:`Admin Region` :tc:`select_one_dropdown` has its choices populated dynamically from a query defined in the *queries* worksheet. This list is then filtered by the value in the :th:`choice_filter` column back in the *survey* worksheet. The *settings* worksheet contains the supported languages in addition to the normal settings. The *properties* worksheet defines the default *Detail View*, *List View*, and *Map View* files and settings. The *model* links the region levels from to the database.

If the :guilabel:`Refrigerator Inventory` button is pressed, :code:`odkTables.launchHTML(...)` is called to launch the :ref:`cold-chain-tour-refrigerators-lists` screen with this health facility as the filter.

If the :guilabel:`Add Refrigerator` button is pressed, :code:`odkTables.addRowWithSurvey(...)` is called for the *Refrigerators* form. The permission and group values of the current health facility are passed in as arguments as well, in order to create this new refrigerator with the same values. This form can be viewed at :file:`tables/refrigerators/forms/refrigerators/refrigerators.xlsx`. It is similar to the *Health Facility* form: short and compressed into a small number of screens. The refrigerator model and health facility choices are both queried from the database (see the *queries* worksheet). The necessary fields are linked in the *models* worksheet. The *choices*, *properties*, and *settings* worksheets are similar to those found in the *Health Facility* form, but with their own values.

.. _cold-chain-tour-health-facilities-menu-implementation-files:

Files
"""""""""""""""

  - :file:`tables/health_facility/html/health_facility_detail.html`
  - :file:`tables/health_facility/js/health_facility_detail.js`
  - :file:`assets/js/util.js`
  - :file:`tables/health_facility/forms/health_facility/health_facility.xlsx`
  - :file:`tables/health_facility/forms/health_facility/regions2-3.csv`
  - :file:`tables/refrigerators/forms/refrigerators/refrigerators.xlsx`
  - :file:`tables/refrigerators/forms/refrigerators/refrigerators.xlsx`
  - :file:`tables/refrigerators/forms/refrigreators/regions1-2.csv`
  - :file:`tables/refrigerators/forms/refrigreators/regions2-3.csv`

.. _cold-chain-tour-health-facilities-menu-implementation-forms:

Forms
""""""""""""""""

  - *Health Facility* with form ID: *health_facility*

.. _cold-chain-tour-health-facilities-menu-implementation-tables:

Database Tables
""""""""""""""""""""""

  - *Health Facility*
  - *Refrigerators*


