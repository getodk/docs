.. spelling::
  Tuk
  tuk

Home Locater
=======================

.. image:: /img/hope-study-tour/hope-study-home-locator.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _hope-study-tour-home-locator-function:

Function
------------------------

The Home Locater module is used to navigate to the client via provided instructions and waypoints on a map. The main screen shows you this list of instructions, including the means of transportation to travel between each one (such as walking or Tuk-tuk). These instructions are populated by pressing the :guilabel:`Add Waypoint` button. This button launches a survey that records the transportation type, GPS coordinates, and enters it in its proper place in the list.

A button is also provided to launch a :guilabel:`Map View`.

  .. image:: /img/hope-study-tour/hope-study-home-locator-map.*
   :alt: Main Menu
   :class: device-screen-vertical

This map view shows the same list of instructions on the top, but uses most of the screen real-estate to show the waypoint markers on the map. Tapping a map marker highlights the instruction. Tapping the instruction on the list opens a *Detail View* of the instruction.


.. _hope-study-tour-home-locator-implementation:

Implementation
------------------------

The Home Locater module functions almost as a miniature version of the rest of the application. The root *List View*, much like the :doc:`hope-study-tour-existing-client` module, receives its list from the caller query via the :code:`odkData.getViewData(...)` call and uses that to render a list of clickable items that will launch the *Detail View*. The *Detail View* shows to basic data about the record, similarly retrieved with the :code:`odkData.getViewData(...)` call.

The :guilabel:`Add Waypoint` button acts similarly to the :guilabel:`Add Client` button in the Existing Clients module, but launches the *Home Locater* form. This form contains a few basic :tc:`text` and :tc:`select_one` prompts, as well as a :tc:`geopoint` prompt to collect location data. The *properties* worksheet is what makes this form distinct from the other forms in this application. It specifies all the mappings to set up the *Map View*, such as the :tc:`mapListViewFileName` and the :tc:`defaultViewType` as a :tc:`MAP`.

The :file:`tables/geopoints/html/geopoints_map_list.html` and :file:`tables/geopoints/js/geopoints_map_list.js` files fine a basic list that should be recognizable in structure to the other *List View* files. However, it has added logic to handle the ordering of the list items basic on selected points on the map in the :code:`render(...)` function.


.. _hope-study-tour-home-locator-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

  - :file:`tables/geopoints/html/geopoints_list.html`
  - :file:`tables/geopoints/js/geopoints_list.js`
  - :file:`tables/geopoints/html/geopoints_detail.html`
  - :file:`tables/geopoints/js/geopoints_detail.js`
  - :file:`tables/geopoints/html/geopoints_map_list.html`
  - :file:`tables/geopoints/js/geopoints_map_list.js`
  - :file:`tables/geopoints/forms/geopoints.xlsx`

.. _hope-study-tour-home-locator-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~~~~

  - *Home Locater* with form ID *geopoints*

.. _hope-study-tour-home-locator-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~

  - *geoopoints*


