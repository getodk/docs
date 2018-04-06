Using ODK Tables
===================

.. _tables-using:

.. contents:: :local:

.. _tables-using-custom-home:

Custom Home Screen
-----------------------

The custom home screen is an HTML file written by your organization to customize the look-and-feel of using Tables. If a custom home screen is provided, by default it will be the first screen shown after opening Tables.

.. _tables-custom-home-hide:

Showing/Hiding the Custom Home Screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To hide the custom home screen and see the *Table Manager* for a list of data tables on the device:

  1. Open Tables. On the custom home screen press the button with three lines in the upper right.

    .. image:: /img/tables-using/tables-home-launch-manager.*
      :alt: Tables Custom Home Launching Manager
      :class: device-screen-vertical

  2. The *Table Manager* will be visible with a full list of data tables stored on the device.

    .. image:: /img/tables-using/tables-home-table-manager.*
      :alt: Tables Table Manager
      :class: device-screen-vertical

To return to the custom home screen press the back button in your Android navigation buttons.

.. warning::

  You may need to enable the custom home screen before it will appear.

.. _tables-custom-home-disable:

Enabling/Disabling the Custom Home Screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable or disable the use of the custom home screen, follow the instructions for :ref:`services-user-tables-settings`.


.. _tables-using-table-manager:

Table Manager
------------------

The *Table Manager* allows you to modify table settings, delete tables, and import or export data into your tables. See the :ref:`Deployment Architect instructions <tables-managing-table-manager>` for details.

.. _tables-using-view-data:

Viewing Data
--------------------

Tables supports viewing collected data in a variety of formats. Survey allows you to review individual form instances, but Tables lets you view full data tables as well as create your own customized visualizations. This is a significant departure from the form based model of data collection, and allows you to manage data directly on the device.

.. _tables-using-view-types:

View Types
~~~~~~~~~~~~~~~~~

Tables offers a number of view options for presenting data. These will have been configured by your organizations Deployment Architect and you may not always have a choice in how you view your data. These view types are:

  - :ref:`Spreadsheet View <tables-using-view-data-spreadsheet>`
  - :ref:`List View <tables-using-view-data-list>`
  - :ref:`Detail View <tables-using-view-data-detail>`
  - :ref:`Detail with Sublist View <tables-using-view-data-detail-with-list>`
  - :ref:`Graph View <tables-using-view-data-graph>`
  - :ref:`Map View <tables-using-view-data-map>`
  - :ref:`Navigate View <tables-using-view-data-navigate>`
  - :ref:`Custom View <tables-using-view-data-custom>`

.. warning::

  Many of the view types in Tables are customizable by a Deployment Architect. This guide will provide some basic outlines of how to use these view types, but for more accurate instructions you may need to contact your organization's Deployment Architect.


.. _tables-using-view-data-spreadsheet:

Spreadsheet View
""""""""""""""""""""

*Spreadsheet View* is the only view option that will be the same for all Data Management Applications. It is not customizable. It serves as a reliable way to view all of the data stored in a table on the device.

  .. image:: /img/tables-using/tables-spreadsheet-view.*
    :alt: Tables Spreadsheet View
    :class: device-screen-vertical


It is intended to have the familiar view as if you were using a spreadsheet program such as :program:`Excel`. Each row represents a data record, which often (but not always) corresponds to a form instance created by Survey. You can scroll up and down to view all of the records, or left and right to see each column.

The thin column on the left is called the *status column*: it will show a different color based on the status of that row.

  - **White (clear)** -- The row is downloaded from the server and has not been modified.
  - **Yellow** -- The row is modified.
  - **Green** -- The row is an entirely new row
  - **Black** -- The row is deleted. It will show as black until you sync with the server and publish those changes.

Custom color rules can be set in table properties. They change the colors of spreadsheet cells based on the values of those cells. This can be useful in browsing larger data sets for records that meet certain criteria. For example, you might be recording crop heights and mark all cells with heights above a certain height as impossible so that they can be revisited or removed. For details on setting these color rules, see the :ref:`color rules guide <tables-managing-table-properties-color-rules>`

Spreadsheet view can also be used to edit data. See the :ref:`Spreadsheet View editing guide <tables-using-edit-spreadsheet>` for further instructions.

.. _tables-using-view-data-list:

List View
""""""""""""""""""""

*List View* is a customizable view that will change based on your Data Management Application's code. In general, it is used to render a list of records from a data table, displaying only a few key values for each record.

  .. image:: /img/tables-using/tables-list-view-tea.*
    :alt: Tables List View
    :class: device-screen-vertical side-by-side

  .. image:: /img/tables-using/tables-list-view-hope.*
    :alt: Tables List View
    :class: device-screen-vertical side-by-side

Often the items in a *List View* are clickable to launch a *Detail View*, a *Detail With Sublist View*, or a *Custom View* to display details of that item. Sometimes these views can also be viewed as *Map Views* and *Navigation Views*. See :ref:`tables-using-view-data-change-views` for instructions on how to find if these view options are available.

.. _tables-using-view-data-detail:

Detail View
""""""""""""""""""""

*Detail View* is a customizable view that will change based on your Data Management Application's code. In general, it is used to render the data from a single record in a logical fashion.

  .. image:: /img/tables-using/tables-detail-view-tea.*
    :alt: Tables Detail View
    :class: device-screen-vertical side-by-side

  .. image:: /img/tables-using/tables-detail-view-geo.*
    :alt: Tables Detail View
    :class: device-screen-vertical side-by-side

A *Detail View* may include some or all of the values from the record it is presenting, and it may include values drawn from other tables. The interface used to present that data is completely customized by the organization writing the Data Management Application.

This view is often launched from a *List View* or a *Map View*.

.. _tables-using-view-data-detail-with-list:

Detail With Sublist View
"""""""""""""""""""""""""""""""

*Detail With Sublist View* is a customizable view that will change based on your Data Management Application's code. It is a combination of a *Detail View* on the top half of the screen and a *List View* on the bottom half of the screen.

  .. image:: /img/tables-using/tables-detail-with-sublist-view.*
    :alt: Tables Detail With Sublist View
    :class: device-screen-vertical

The *Detail View* on the top half of the screen follows all the same rules as a normal *Detail View*. In addition, it can control the *List View* rendered below it. There may be an interactive element within the *Detail View* that will cause the subordinate *List View* to redraw with different values.

.. _tables-using-view-data-graph:

Graph View
"""""""""""""""""""""

*Graph View* is a customizable view that will change based on your Data Management Application's code. In general, it is a often specialized *List View* that creates a graphical rendering of the data (such as a bar graph or pie chart). It may also be a specialized *Detail View* or *Custom View*.

  .. image:: /img/tables-using/tables-graph-view-hope.*
    :alt: Tables Graph View
    :class: device-screen-vertical side-by-side

  .. image:: /img/tables-using/tables-graph-view-plot.*
    :alt: Tables Graph View
    :class: device-screen-vertical side-by-side

A *Graph View* uses JavaScript libraries such as :program:`D3` to create visualizations of collected data on the device. These will be rendered on demand using the data available, meaning that they will update and change as new data is collected.

.. _tables-using-view-data-map:

Map View
""""""""""""""""""""

*Map View* is a partially customizable view that will change based on your Data Management Application's code. The top portion of the view is a *List View* representing the records in the data table, and the bottom portion of the screen renders the records as geopoints on a map using :program:`Google Maps`.

  .. image:: /img/tables-using/tables-map-view-tea.*
    :alt: Tables Map View
    :class: device-screen-vertical side-by-side

  .. image:: /img/tables-using/tables-map-view-geo.*
    :alt: Tables Map View
    :class: device-screen-vertical side-by-side

Points are added to the map based on their recorded latitude and longitude values. The map can be navigated by pinching or widening to zoom in and out, or swipe around to move the window (the same controls as the stand alone :program:`Google Maps`).

When a point is selected in a *Map View* it will usually update the *List View* on the top portion of the screen to select the same point, and possibly present more data about that point.

.. _tables-using-view-data-navigate:

Navigate View
""""""""""""""""""""

*Navigate View* is similar to *Map View*, but the top portion is replaced with navigational tools to aid in finding a location on the map in the real world. The bottom portion of the screen still renders the records as geopoints on a map using :program:`Google Maps`.

  .. image:: /img/tables-using/tables-navigate-view.*
    :alt: Tables Navigate View
    :class: device-screen-vertical

When a point on the map is selected, the navigation controls on the top portion of the screen will update to guide you to the selected point.

  - **Compass** shows you cardinal directions in addition to an arrow pointing at the navigation point.
  - **Distance** shows the distance between your GPS location and the navigation point.
  - **Heading** shows the direction that you are facing.
  - **Bearing** shows the angle between your heading and your navigation point.
  - **GPS Accuracy Spinner** shows the GPS's current accuracy estimate. It will change color based on how good this accuracy is.

The :guilabel:`Arrive` button will return you to the screen that launched the *Navigation View* with a success code. This may launch a follow up Survey or workflow to be performed at the navigation point.

The :guilabel:`Cancel` button also returns you to the screen that launched the *Navigation View*, but with a failure code. It indicates that the navigation point was not reached and it will not trigger a follow up workflow.

.. _tables-using-view-data-custom:

Custom View
"""""""""""""""""""""

*Custom View* is a completely customized view that is defined by your Data Management Application's code. There is no general pattern for *Custom Views*.

  .. image:: /img/tables-using/tables-custom-view-tea.*
    :alt: Tables Custom View Navigation
    :class: device-screen-vertical side-by-side

  .. image:: /img/tables-using/tables-custom-view-jgi.*
    :alt: Tables Custom View Data Entry
    :class: device-screen-vertical side-by-side

*Custom Views* are arbitrary user interfaces built on top of web technologies and rendered in Tables. They can be anything your organization needs to implement its custom workflow.

.. note::

  *Custom Views* are not limited to displaying data. They can also be used to collect or modify data. See the guide for :ref:`editing data with custom views <tables-using-edit-custom>`.

.. _tables-using-view-data-change-views:

Changing View Types: The Lined Paper Button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The view types that represent multiple records (:ref:`tables-using-view-data-spreadsheet`, :ref:`tables-using-view-data-list`, :ref:`tables-using-view-data-map`, :ref:`tables-using-view-data-navigate`) can be alternately chosen, depending on what the Deployment Architect has configured in the table's settings.

To change to another view type, tap the lined paper icon from the upper right:

  .. image:: /img/tables-using/tables-change-view-button.*
    :alt: Tables Change View Button
    :class: device-screen-vertical

This will bring up a menu that lets you select your desired alternate view type.

  .. image:: /img/tables-using/tables-change-view-menu-full.*
    :alt: Tables Change View Menu
    :class: device-screen-vertical

.. tip::

  :ref:`tables-using-view-data-graph` is a special case. You may have the lined paper icon available to you, but it may only have *Spreadsheet View* as its alternative option, and may not have an option to return to the *Graph View*. Usually pressing the back button from *Spreadsheet View* will return you to the *Graph View*.

  *Graph Views* also may not have the lined paper icon available at all if they are instead mapped as a *Detail View* or a *Custom View*.

.. note::

  Not all view types will always be available. For example, if the data set does not contain geographic data, the *Map View* and *Navigate View* options will not be available.

  .. image:: /img/tables-using/tables-change-view-menu-no-map.*
    :alt: Tables Change View Menu Without Maps
    :class: device-screen-vertical


.. _tables-using-edit-data:

Creating and Editing Data
---------------------------------

Tables supports creating new rows and editing existing records and provides a variety of methods to do so. These can be integrated into your Data Management Application's workflow or accessed directly.

.. _tables-using-edit-survey:

Editing With Survey
~~~~~~~~~~~~~~~~~~~~~~~~

Most data change options use Survey to create or update the record. These options will launch Survey from the Table in question to directly edit the relevant record, and then return control back to Tables where you left off. Which options are available depends on which view type you are currently using.

.. _tables-using-edit-plus:

Creating a Record: The :guilabel:`+` Button
""""""""""""""""""""""""""""""""""""""""""""""

  .. image:: /img/tables-using/tables-list-view-new-record.*
    :alt: Tables + Button
    :class: device-screen-vertical

The :guilabel:`+` button is available in any of the multi-record views: :ref:`tables-using-view-data-list`, :ref:`tables-using-view-data-graph`, :ref:`tables-using-view-data-map`, and :ref:`tables-using-view-data-navigate`. This button will launch the configured Survey form to create a new record in the table currently being viewed. The example picture above shows the *Tea Houses* *List View* from the :doc:`tables-sample-app`. If the :guilabel:`+` is pressed it will launch a Survey to create a new tea house in the table.

.. _tables-using-edit-pencil:

Editing a Record: The Pencil Button
"""""""""""""""""""""""""""""""""""""

  .. image:: /img/tables-using/tables-detail-view-edit-record.*
    :alt: Tables Pencil Button
    :class: device-screen-vertical

The pencil button is available in any of the single record views: :ref:`tables-using-view-data-detail` and :ref:`tables-using-view-data-detail-with-list`. *Detail With Sublist View* is considered a single record view as the *Detail View* portion is considered the controlling view, and the *List View* below is subordinate.

If the pencil button is pressed, it will launch the configured Survey form to edit the record currently be viewed. When the record has been updated and control returns to the calling view, the new details should be rendered in that view.


.. _tables-using-edit-spreadsheet:

Spreadsheet View
"""""""""""""""""""""""

*Spreadsheet View* also offers methods to launch Survey to create or edit records. If you know exactly the table or record you want to edit, this view may be the more direct option. You can also use :ref:`tables-managing-table-properties-color-rules` to find records that require your attention and then edit them directly.

  - **Creating a Record** follows the same workflow as the other :ref:`multirecord views <tables-using-edit-plus>`. Press the :guilabel:`+` button to create a new row in the data table and see it in the *Spreadsheet View*.
  - **Editing a Record** can be performed by long pressing on the desired row. A pop up will open when the long press is released.

    .. image:: /img/tables-using/tables-spreadsheet-edit-record.*
      :alt: Tables Spreadsheet Pop Up
      :class: device-screen-vertical

  This gives you the option to:

    - :guilabel:`Delete Row` - This will produce a confirmation dialog make sure you want to delete the record. If affirmed, the row will be marked for deleted (or marked for deletion on the next synchronization).
    - :guilabel:`Edit Row` - This will launch the Survey form corresponding to this record, similar to the :ref:`pencil button <tables-using-edit-pencil>`.

.. _tables-using-edit-custom:

Editing Directly in Tables: Custom Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tables supports direct creation and updates to data in the database through JavaScript API calls. These will be completely customized to your organization's Data Management Application and you may need to contact that person to find out how to use your particular design.

For more information on how to edit data with these custom views, see :ref:`tables-managing-custom-web-view`.

.. _tables-using-syncing:

Syncing Data
--------------------------

See the instructions in the :ref:`ODK Services user guide <services-using-sync>`.

.. warning::

  If a data table has any checkpoint saves (for example, caused by form crashes), the data table will not be synchronized. Checkpoints must be resolved before sync can proceed. The user must open a form on the problem table and either delete the checkpoint or edit the checkpoint. If editing, after that is complete they must save is as either incomplete or finalized. Once the checkpoints are eliminated, the user can initiate another synchronization, and the data in this table will then be synchronized with the information on the server.
