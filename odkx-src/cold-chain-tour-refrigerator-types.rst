Refrigerator Types
========================

Refrigerator Types represent the different models of refrigerators available. This is convenient for adding a new refrigerator to a health facility, as the model will already include information about the refrigerator that might not be obvious to the worker installing the unit. It also provides an easy reference if spare parts are needed or the model itself is needed for any reason.

.. _cold-chain-tour-refrigerator-types-lists:

Lists of Refrigerator Types
----------------------------------

.. image:: /img/cold-chain-tour/cold-chain-refrigerator-type-list.*
  :alt: List of Refrigerator Types
  :class: device-screen-vertical

.. _cold-chain-tour-refrigerator-types-lists-function:

Function
~~~~~~~~~~~~~~~~~~~~~

A List of Refrigerator Types is similar to a :ref:`cold-chain-tour-refrigerators-lists`. It is launched by pressing the :guilabel:`View Refrigerator Models` button on the :ref:`cold-chain-tour-regions-menu`.

The list portion contains each refrigerator type. Clicking that list item will open the :ref:`cold-chain-tour-refrigerator-types-menu`. The list can be searched by the refrigerator type ID, catalog ID, or the manufacturer. A substring of the search string can be provided and all matching records will be displayed.

The list items each show a picture of the refrigerator model to ease navigation and provide a more familiar reference than the model name.

This page is paginated by default to 10 refrigerator types per page. This can be adjusted to 20, 50, 100, or 1000 by selecting the option from the drop menu. To navigate between pages of refrigerator types, use the :guilabel:`Next` and :guilabel:`Prev` buttons.

.. _cold-chain-tour-refrigerator-types-lists-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~

The refrigerator types list uses the files :file:`tables/refrigerator_types/html/regrigerator_types_list.html` and :file:`tables/refrigerator_types/js/refrigerator_types.js` similarly to the :ref:`refrigerators list <cold-chain-tour-refrigerators-lists-implementation>`.

The key differences are the :code:`listQuery` and :code:`searchParams` variables that define the values that will populate the same user interface. This file's versions of :code:`listQuery` performs a simple :code:`SELECT *` from the *Refrigerator Types* table and this versions of :code:`searchParams` searches for matching catalog ID, manufacturer, or model ID.

That logic that implements that user interface is discussed in :ref:`cold-chain-tour-list-logic`.

.. _cold-chain-tour-refrigerator-types-lists-implementation-files:

Files
""""""""""""""""""

  - :file:`tables/refrigerator_types/html/refrigerator_types_list.html`
  - :file:`tables/refrigerator_types/js/refrigerator_types_list.js`

.. _cold-chain-tour-refrigerator-types-lists-implementation-forms:

Forms
"""""""""""""""""""

None

.. _cold-chain-tour-refrigerator-types-lists-implementation-tables:

Database Tables
"""""""""""""""""""

  - *Refrigerator Types*

.. _cold-chain-tour-refrigerator-types-menu:

Refrigerator Type Menu
-----------------------------

.. image:: /img/cold-chain-tour/cold-chain-refrigerator-type-menu.*
  :alt: Refrigerator Type Menu
  :class: device-screen-vertical


.. _cold-chain-tour-refrigerator-types-menu-function:

Function
~~~~~~~~~~~~~~~~~~~~~~

The Refrigerator Type Menu is a *Detail View* that lists all the model information about the particular refrigerator type, and shows a picture if available.

It also has a :guilabel:`View all *Model ID* Refrigerators` that shows the number of refrigerators in the region with this particular type. Tapping that button will launch a :ref:`cold-chain-tour-refrigerators-lists` containing all refrigerators in that region of that type.

.. _cold-chain-tour-refrigerator-types-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~

The *Detail View* for a refrigerator type is defined by :file:`tables/refrigerator_types/html/refrigerator_types_detail.html`. This file lists each user interface element (including all the data values of the refrigerator type as well as the buttons). These elements contain their labels, and the values are filled in by :file:`tables/refrigerator_types/js/refrigerator_types_detail.js`.

After localizing its text, this JavaScript retrieves the refrigerator log data with the standard :code:`odkData.getViewData(...)` call. It also makes an :code:`odkData.query(...)` call to the *Refrigerators* table. The resulting data sets are combined to fill in the display fields on the detail view.

If the :guilabel:`View all *Model ID* Refrigerators` button is pressed, :code:`odkTables.launchHTML(...)` is called to launch :ref:`cold-chain-tour-refrigerators-lists`.


.. _cold-chain-tour-refrigerator-types-menu-implementation-files:

Files
""""""""""""""""""""

  - :file:`tables/refrigerator_types/html/refrigerator_types_detail.html`
  - :file:`tables/refrigerator_types/js/refrigerator_types_detail.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-refrigerator-types-menu-implementation-forms:

Forms
"""""""""""""""""""

None

.. _cold-chain-tour-refrigerator-types-menu-implementation-tables:

Database Tables
"""""""""""""""""""""

  - *Refrigerator Types*
  - *Refrigerators*


