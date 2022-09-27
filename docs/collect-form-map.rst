Viewing filled forms on a map
================================

.. versionadded:: 1.25

  `ODK Collect v1.25.0 <https://github.com/getodk/collect/releases/tag/v1.25.0>`_

If you are collecting data related to physical locations, you can see a map of all filled forms from the :doc:`Fill Blank Form <collect-filling-forms>` menu. Use the map view to see your progress, to identify filled forms with bad locations and to plan your travel to the next location to survey.

.. note:: 
  Blank forms must be downloaded with Collect v1.25 or later. Previously-downloaded forms will not have corresponding maps. If you update a form downloaded before Collect v1.25 and open its map, only filled forms created with the new form version will be displayed. Any previously-filled forms will not be included.

In the :guilabel:`Fill Blank Form` list, form definitions with a geopoint question outside of any repeat have a map button (:fa:`map`). Tap on the map button to open a map showing the filled forms for that form definition. The first geopoint question in the form definition that is outside of any repeat is used to map filled forms. This question can either be :ref:`a visible geopoint question <location-widgets>` or :ref:`a question that gets the location in the background <metadata-start-geopoint>`. On the map, you will also see your current position and be able to fill a new instance of the current form definition.

   .. image:: /img/collect-forms/form-map-with-selection.*
     :alt: The map for a form with title "Enquête SICAP Sacré Coeur." Several saved and finalized forms are shown as purple markers. One filled form is selected and its description is provided at the bottom of the screen. It says "Khadim Aïdara - Gestionnaire de projet" followed by the finalization time and a button to edit the saved form.


.. form-instance-map-markers:

Form instance map markers
----------------------------

Filled forms are represented by colored map markers. The color of each map marker indicates the status of the filled form:

* Blue: saved and unfinalized
* Purple: finalized
* Green: sent
* Red: send attempt failed

Tapping on a map marker shows details about the filled form at the bottom of the screen. The filled form will be identified by its `instance name <http://xlsform.org/en/#specify-form-submission-name>`_. In the screenshot above, first name, last name, and job title are displayed. Strategically choosing data from the form to show in the instance name can make the form map into a useful dashboard.

The detail view also shows a button for viewing or editing the selected filled form depending on its status. By default, forms with `Saved`, `Finalized`, and `Submission Failure` status are opened for edit and `Sent` forms are opened for viewing. However, if the :guilabel:`Edit Saved Form` button is made unavailable from the :ref:`admin settings <user-access-control-settings>`, forms with `Saved`, `Finalized`, and `Submission Failure` status are opened as view-only.


.. form-map-controls:

Map controls
-------------

There are three control buttons clustered at the top right of the map. The top button is used to zoom to the current location. The middle button adjusts the zoom level to ensure that all mapped filled forms are displayed on the screen. The last button is used to change layers if :doc:`offline layers <collect-offline-maps>` are available. The basemap and reference layer settings are used across all of Collect so the same ones will be used for this form map as for :ref:`location widgets with maps <location-widgets>`.

The button at the bottom right of the screen can be used to fill a new instance of the current form definition. After you save a new filled form, you will be returned to the map and the filled form will be displayed if it has a geopoint associated with it.

.. form-map-status-bar:

Status bar
-----------

The bar at the bottom of the screen displays the total number of saved forms and how many of these are shown on the map. All filled forms with a value for the first geopoint question will be displayed. To ensure that all filled forms are displayed, make the identifying geopoint question :ref:`required <requiring-responses>`.

.. note::
  Deleted or :doc:`encrypted <encrypted-forms>` filled forms are not shown on the map. However, forms that were successfully sent and then deleted and forms that are encrypted both contribute to the total number of saved forms. See :ref:`deleting-forms` for more on how filled form deletion works.