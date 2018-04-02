.. spelling::
  prepopulated

Maintenance Records
===========================

Maintenance Records detail service performed on a particular refrigerator. Individually they are a brief record of service performed, and taken together they compose the service history of a refrigerator.

.. _cold-chain-tour-maintenance-records-lists:

Lists of Maintenance Records
-----------------------------------

.. image:: /img/cold-chain-tour/cold-chain-maintenance-list.*
  :alt: Maintenance Log
  :class: device-screen-vertical

.. _cold-chain-tour-maintenance-records-lists-function:

Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A List of Maintenance Records is similar to a :ref:`cold-chain-tour-refrigerators-lists`. It is launched by pressing the :guilabel:`View All Maintenance Records` button on the :ref:`cold-chain-tour-refrigerators-menu`.

The list portion contains each maintenance record in the log for a particular refrigerator, with the date serviced highlighted. Clicking that list item will open the :ref:`cold-chain-tour-maintenance-records-menu`.

Records can be searched by refrigerator ID. This page is paginated by default to 10 records per page. This can be adjusted to 20, 50, 100, or 1000 by selecting the option from the drop menu. To navigate between pages of maintenance records, use the :guilabel:`Next` and :guilabel:`Prev` buttons.

Tapping the :guilabel:`Edit` button will launch the Survey form for this maintenance record. Each field will be prepopulated with the values shown in the menu, so that only the values that are incorrect need to be filled in.


.. _cold-chain-tour-maintenance-records-lists-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~

The maintenance records list uses the files :file:`tables/maintenance_logs/html/maintenance_logs_list.html` and :file:`tables/maintenance_logs/js/meaintenance_logs_list.js` similarly to the :ref:`refrigerators list <cold-chain-tour-refrigerators-lists-implementation>`.

The key differences are the :code:`listQuery` and :code:`searchParams` variables that define the values that will populate the same user interface. This file's versions of :code:`listQuery` finds all maintenance logs that match the refrigerator ID and this versions of :code:`searchParams` searches for matching refrigerator IDs.

That logic that implements that user interface is discussed in :ref:`cold-chain-tour-list-logic`.


.. _cold-chain-tour-maintenance-records-lists-implementation-files:

Files
"""""""""""""""""""""

  - :file:`tables/maintenance_logs/html/maintenance_logs_list.html`
  - :file:`tables/maintenance_logs/js/maintenance_logs_list.js`
  - :file:`config/assets/js/list_view_logic.js`

.. _cold-chain-tour-maintenance-records-lists-implementation-forms:

Forms
""""""""""""""""""""

None

.. _cold-chain-tour-maintenance-records-lists-implementation-tables:

Database Tables
"""""""""""""""""""""

  - *Maintenance Logs*
  - *Refrigerators*

.. _cold-chain-tour-maintenance-records-menu:

Maintenance Record Menu
---------------------------

.. image:: /img/cold-chain-tour/cold-chain-maintenance-menu.*
  :alt: Maintenance Record
  :class: device-screen-vertical


.. _cold-chain-tour-maintenance-records-menu-function:

Function
~~~~~~~~~~~~

The Maintenance Record Menu is a *Detail View* that lists the full account of the service, including the :guilabel:`Reason Not Working`, the :guilabel:`Date Serviced`, :guilabel:`Spare Parts`, and other details.

It also includes an :guilabel:`Edit Log` button, which launches the Survey form for this maintenance record. Each field will be prepopulated with the values shown in the menu, so that only the values that are incorrect need to be filled in.

.. _cold-chain-tour-maintenance-records-menu-implementation:

Implementation
~~~~~~~~~~~~~~~~~~~~~~~~

The *Detail View* for a maintenance record is defined by :file:`tables/maintenance_logs/html/maintenance_logs_detail.html`. This file lists each user interface element (including all the data values of the maintenance record as well as the buttons). These elements contain their labels, and the values are filled in by :file:`tables/maintenance_records/js/maintenance_records_detail.js`.

After localizing its text, this JavaScript retrieves the maintenance log data with the standard :code:`odkData.getViewData(...)` call. It also makes an :code:`odkData.query(...)` call to the *Refrigerators* table. The resulting data sets are combined to fill in the display fields on the detail view.

The :guilabel:`Edit Log` and :guilabel:`Delete Log` buttons are dynamically hidden or shown depending on the privileges of the authenticated user.

If the :guilabel:`Edit Log` button is pressed, the *Maintenance Logs* form is launched with :code:`odkTables.editRowWithSurvey(...)`. The forms :file:`.xlsx` file is located at :file:`tables/maintenance_logs/forms/maintenance_logs/maintenance_logs.xlsx`. This form is discussed in the :ref:`refrigerator menu implementation section <cold-chain-tour-refrigerators-menu-implementation>` under the :guilabel:`Add Maintenance Record` bullet.

If the :guilabel:`Delete Log` button is pressed, :code:`odkData.deleteRow(...)` is called to remove the record from the database.

.. _cold-chain-tour-maintenance-records-menu-implementation-files:

Files
""""""""""""""""""""

  - :file:`tables/maintenance_logs/html/maintenance_logs_detail.html`
  - :file:`tables/maintenance_logs/js/maintenance_logs_detail.js`
  - :file:`assets/js/util.js`
  - :file:`tables/maintenance_logs/forms/maintenance_logs/maintenance_logs.xlsx`

.. _cold-chain-tour-maintenance-records-menu-implementation-forms:

Forms
"""""""""""""""""""""

  - *Maintenance Logs* with form ID *maintenance_logs*

.. _cold-chain-tour-maintenance-records-menu-implementation-tables:

Database Tables
""""""""""""""""""""""""

  - *Maintenance Logs*
  - *Refrigerators*


