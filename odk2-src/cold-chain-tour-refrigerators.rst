.. spelling::
  prepopulated

Refrigerators
=========================

Refrigerators are a key element of the Cold Chain application. Their working status is necessary for keeping vaccines cold and effective. This application focuses on providing easy access to the working status of lists of refrigerators organized in a multitude of different ways. It also tracks basic information about the refrigerator, such as its age and model.

Refrigerators belong to :doc:`cold-chain-tour-health-facilities` and they contain :doc:`cold-chain-tour-maintenance-records`.

.. _cold-chain-tour-refrigerators-lists:

Lists of Refrigerators
------------------------------

.. image:: /img/cold-chain-tour/cold-chain-refrigerator-list-region.*
  :alt: Refrigerator List
  :class: device-screen-vertical

.. _cold-chain-tour-refrigerators-lists-function:

Function
~~~~~~~~~~~~~~~~~~~~~

A Refrigerator List contains a clickable list of refrigerators: clicking the refrigerator will open the :ref:`cold-chain-tour-refrigerators-menu`. The list can be searched by the refrigerator's ID, the tracking ID, the health facility name, or the health facility ID:

  .. image:: /img/cold-chain-tour/cold-chain-refrigerator-list-region-search.*
    :alt: Refrigerator List Search
    :class: device-screen-vertical

The search string does not need to be a perfect match. Substrings and approximate matches can be searched and all matching records will be displayed. For example, if you searched *225* then you might get back refrigerators with ID *22500172*, *22500035*, and *22500032*.

This page is paginated by default to 10 refrigerators per page. This can be adjusted to 20, 50, 100, or 1000 by selecting the option from the drop menu. To navigate between pages of refrigerators, use the :guilabel:`Next` and :guilabel:`Prev` buttons.

Tapping the :guilabel:`Edit` button will launch the full Survey form for this refrigerator. Each field will be prepopulated with the values shown in the menu, so that only the values that are incorrect need to be filled in.

These lists can be organized a number of ways:

  - **By Region**: This lists all refrigerators in the region and is launched by pressing the :guilabel:`View All Refrigerators` button on the :ref:`cold-chain-tour-regions-menu`. This is what is shown above.

  - **By Health Facility**: This lists all refrigerators in a particular health facility. It is launched by pressing the :guilabel:`Refrigerator Inventory` button on the :ref:`cold-chain-tour-health-facilities-menu`.

      .. image:: /img/cold-chain-tour/cold-chain-refrigerator-list-inventory.*
        :alt: Refrigerator Inventory List
        :class: device-screen-vertical

  - **By Type**: This lists all refrigerators in a particular region organized by type. This is launched by pressing the :guilabel:`View All *Model ID* Refrigerators` button on a :ref:`cold-chain-tour-refrigerator-types-menu`.

      .. image:: /img/cold-chain-tour/cold-chain-refrigerator-list-model.*
        :alt: Refrigerator List by Model
        :class: device-screen-vertical

  - **Needing Service**: This lists all refrigerators in a particular region that are in need of service. This is launched by pressing the :guilabel:`View All Refrigerators Needing Service` button on the :ref:`cold-chain-tour-regions-menu`.


.. _cold-chain-tour-refrigerators-lists-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~

The refrigerator lists launched **By Region**, **By Health Facility**, and **By Type** all use :file:`config/tables/refrigerators/html/refrigerators_list.html` and achieve their different lists by passing different query parameters. This file defines the search form, the pagination drop menu, and the JavaScript functions to call on button presses. All the rest of the user interface is added dynamically in :file:`config/tables/refrigerators/js/refrigerators_list.js`. However, this file only handles populating the user interface elements defined in :file:`refrigerators-list.html`. All of the logic is handled by the shared library file :file:`config/assets/js/list_view_logic.js`. This file is discussed in the following subsection: :ref:`cold-chain-tour-list-logic`.

The refrigerator list launched by **Needing Service** uses :file:`config/tables/refrigerators/html/refrigerators_service_list.html` and :file:`config/tables/refrigerators/js/refrigerators_service_list.js`, but these files work nearly identically to their :file:`refrigerators_list.*`. The only difference is the :code:`listQuery` variable that defines the SQL query to be run. Both files join the *Refrigerators*, *Health Facilities*, and *Refrigerator Types* tables in order to support filtering and sorting on facility name, facility ID, tracking ID, and refrigerator ID (see the :code:`searchParams` variable). The :file:`refrigerators_service_list.js` file differs in that it adds arguments for refrigerator maintenance priority.

.. _cold-chain-tour-list-logic:

The :file:`list_view_logic.js` library
"""""""""""""""""""""""""""""""""""""""""""""""

This library handles the queries, ordering, search, and pagination for all the search *List Views* in the Cold Chain application. In this section the calling files are :file:`refrigerators_list.js` and :file:`refrigerators_service_list.js`, but there are others as well. For the rest of this section I will refer to these as the caller.

When the caller is initializing, it will use the *set* functions to build state. First the table ID must be set with :code:`setTableId(...)`. Then the query parameters with :code:`setListQuery(...)`, :code:`setListQueryParams(...)`, and :code:`setSearchParams(...)`. And finally the user interface elements need to be supplied with :code:`setListElement(...)`, :code:`setSearchTextElement(...)`, and so on, to allow the :file:`list_view_logic.js` file to read and write to them directly.

After state is initialized, the :code:`resumeFn(...)` can be called. This function uses session variables (via :code:`odkCommon.setSesionVariable(...)` and :code:`odkCommon.getSessionVariable(...)` to track search terms, query keys, and pagination indices. It uses these values to build SQL queries and then runs them with a series of `odkData.arbitraryQuery(...)` commands to count the matching records and then retrieve the appropriate subset to display on the page. The results of that final query are used to create the list elements and populated them onto the page. Each list element contains a :code:`odkTables.openDetailView(...)` command embedded in it. This works in a generic file like this because the default *Detail View* for each of these tables has been set in the *settings* page of the corresponding :file:`.xlsx` file.

There is also more complex logic to handle the :guilabel:`Edit` and :guilabel:`Delete` buttons. The file must ensure the authenticated user has the requisite permissions for each record before displaying the button. If they do, and the button is pressed, the functions :code:`odkTables.editRowWithSurvey(...)` and :code:`odkData.deleteRow(...)` are called, respectively.

There are controls for the :guilabel:`Next` and :guilabel:`Prev:` navigation buttons that ensure they do not go beyond the bounds of the full result set. Each time they are pressed, the :code:`resumeFn(...)` is called again to re-query and redraw the results. Similarly, the :guilabel:`Search` button parses the text of the search, constructs a new query, and calls :code:`resumeFn(...)`. All of these functions communicate their parameters for the redraw through session variables.

.. _cold-chain-tour-refrigerators-lists-implementation-files:

Files
""""""""""""""""""""""

  - :file:`config/tables/refrigerators/html/refrigerators_list.html`
  - :file:`config/tables/refrigerators/js/refrigerators_list.js`
  - :file:`config/tables/refrigerators/html/refrigerators_service_list.html`
  - :file:`config/tables/refrigerators/js/refrigerators_service_list.js`
  - :file:`config/assets/js/list_view_logic.js`

.. _cold-chain-tour-refrigerators-lists-implementation-forms:

Forms
""""""""""""""""""""

None

.. _cold-chain-tour-refrigerators-lists-implementation-tables:

Database Tables
""""""""""""""""""""

  - *Refrigerators*
  - *Health Facilities*
  - *Refrigerator Types*

.. _cold-chain-tour-refrigerators-menu:

Refrigerator Menu
----------------------------

.. image:: /img/cold-chain-tour/cold-chain-refrigerator-menu.*
  :alt: Refrigerator Menu
  :class: device-screen-vertical side-by-side

.. image:: /img/cold-chain-tour/cold-chain-refrigerator-menu-buttons.*
  :alt: Refrigerator Menu Buttons
  :class: device-screen-vertical side-by-side

.. _cold-chain-tour-refrigerators-menu-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~

The Refrigerator Menu is a *Detail View* that shows all the information about the particular refrigerator. Notable fields include :guilabel:`Status` and :guilabel:`Date Serviced`.

It also contains a number of buttons:

  - :guilabel:`View Model Information`: Launches the corresponding :ref:`cold-chain-tour-refrigerator-types-menu`.
  - :guilabel:`View Facility Information`: Launches the :ref:`cold-chain-tour-health-facilities-menu` of the facility this refrigerator belongs to.
  - :guilabel:`Add Maintenance Record`: Launches a Survey form to add a new :doc:`cold-chain-tour-maintenance-records`. This record will be associated with this refrigerator and appear in future logs. This is meant to be filled out after a refrigerator is serviced.
  - :guilabel:`View All Maintenance Records`: Launches a :ref:`cold-chain-tour-maintenance-records-lists` of all records associated with this particular refrigerator. It serves as a full service history of this unit.
  - :guilabel:`Edit Refrigerator Status`: Launches a Survey form that modifies only the service related details of this refrigerator. To be pressed when this refrigerator breaks or receives maintenance.
  - :guilabel:`Edit Refrigerator`: Launches the full Survey form for this refrigerator. Each field will be prepopulated with the values shown in the menu, so that only the values that are incorrect need to be filled in.

.. _cold-chain-tour-refrigerators-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~

The *Detail View* for a refrigerator is defined by :file:`tables/refrigerators/html/refrigerators_detail.html`. This file lists each user interface element (including all the data values of the refrigerator as well as the buttons). These elements contain their labels, and the values are filled in by :file:`tables/refrigerators/js/refrigerators.js`.

After localizing its text, this JavaScript retrieves the refrigerator data with the standard :code:`odkData.getViewData(...)` call. It also makes :code:`odkData.query(...)` calls to the *Health Facility*, *Refrigerator Types* and *Maintenance Logs* tables. All of these resulting data sets are combined to fill in the display fields on the detail view.

If a button is pressed:

  - :guilabel:`View Model Information`: Launches :code:`odkTables.openDetailView(...)` to :ref:`cold-chain-tour-refrigerator-types-menu`.
  - :guilabel:`View Facility Information`: Launches :code:`odkTables.openDetailView(...)` to :ref:`cold-chain-tour-health-facilities-menu`.
  - :guilabel:`Add Maintenance Record`: Launches :code:`odkTables.addRowWithSurvey(...)` to the *Maintenance Logs* form. The permission and group values of the current refrigerator are passed as arguments as well, in order to create this maintenance record with the same values. This form can be viewed at :file:`tables/maintenance_logs/forms/maintenance_logs/maintenance_logs.xlsx`. This brief form only contains two screens. There is an :tc:`if` clause that is set to never trigger, because the :tc:`refrigerator_id` will already be supplied by the caller. The rest of this form functions similarly to the rest of the forms in this application.
  - :guilabel:`View All Maintenance Records`: Launches :code:`odkTables.launchHTML(...)` to :ref:`cold-chain-tour-maintenance-records-lists`.
  - :guilabel:`Edit Refrigerator Status`: Launches :code:`odkTables.editRowWithSurvey(...)` to the *Refrigerator Status* form. This form can be found at :file:`tables/refrigerators/forms/refrigerator_status/refrigerator_status.xlsx`. This form writes to the *Refrigerators* table the same as the *Refrigerators* form does, but only presents a subset of the data fields. It displays a single screen of prompts relating to the status of the refrigerator. These will be prepopulated and only need be updated as necessary. This mapping is set up in the *settings* worksheet.
  - :guilabel:`Edit Refrigerator`: Launches :code:`odkTables.editRowWithSurvey(...)` to the *Refrigerators* form. This performs similarly to the above option, but presents the data fields of the entire table. The form is discussed in more detail in :ref:`Health Facilities Menu Implementation <cold-chain-tour-health-facilities-menu-implementation>` under the :guilabel:`Add Refrigerator` option.

.. _cold-chain-tour-refrigerators-menu-implementation-files:

Files
"""""""""""""""

  - :file:`tables/refrigerators/html/refrigerators_detail.html`
  - :file:`tables/refrigerators/js/refrigerators_detail.js`
  - :file:`config/assets/js/util.js`
  - :file:`tables/maintenance_logs/forms/maintenance_logs/maintenance_logs.xlsx`
  - :file:`tables/refrigerators/forms/refrigerator_status/refrigerator_status.xlsx`
  - :file:`tables/refrigerators/forms/refrigerators/refrigerators.xlsx`

.. _cold-chain-tour-refrigerators-menu-implementation-forms:

Forms
"""""""""""""""""""

  - *Maintenance Logs* with form ID *maintenance_logs*
  - *Refrigerator Status* with form ID *refrigerator_status*
  - *Refrigerators* with form ID *refrigerators*

.. _cold-chain-tour-refrigerators-menu-implementation-tables:

Database Tables
"""""""""""""""""""""

  - *Refrigerators*
  - *Health Facility*
  - *Refrigerator Types*
  - *Maintenance Logs*


