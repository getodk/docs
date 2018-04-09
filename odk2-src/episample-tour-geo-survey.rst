Village Geographic Survey
==============================

.. image:: /img/episample-tour/episample-collect-blank.*
  :alt: Collection Screen
  :class: device-screen-vertical

.. _episample-tour-geo-survey-function:

Function
------------------

The Village Geographic Survey module is used to gather census data about each household. It records basic information: a house number, a head-of-household name, and the GPS coordinates of that household. The house number field is automatically increased with each saved record.

Recorded households are listed in the bottom portion of the screen. This list includes the name and house number, an :guilabel:`Edit` button that allows you to update the record, and an icon indicating whether the record is :guilabel:`Valid` or not. The validity of a record is determined by the accuracy of its GPS coordinates. The thresholds are set in the :doc:`episample-tour-config` module.

The quality of the GPS signal is depicted by the color of the spinner and the specific rating listed.

  .. image:: /img/episample-tour/episample-collect-poor-gps.*
    :alt: Collection Screen with Poor GPS signal
    :class: device-screen-vertical side-by-side

  .. image:: /img/episample-tour/episample-collect-invalid.*
    :alt: Collection Screen with Invalid Record
    :class: device-screen-vertical side-by-side

The above screen on the left depicts a GPS signal that is not accurate enough, and is displayed in yellow. The screen on the right shows that the icon next to :guilabel:`Beth` is an :guilabel:`I` for *Invalid*, rather than the :guilabel:`V` for *Valid* next to Alex.

A running total of records is indicated in between the collection portion of the screen and the record list. It is separated into the *Valid*, *Invalid*, and *Excluded* categories. The difference between *Invalid* and *Excluded* is that an *Excluded* record is manually excluded via the :guilabel:`Exclude` checkbox.

In *Invalid* record can only be made valid by recapturing the GPS coordinates when the accuracy is sufficient. The image below shows the record editing screen.

  .. image:: /img/episample-tour/episample-collect-update.*
    :alt: Collection Update Screen
    :class: device-screen-vertical

To replace the GPS, the :guilabel:`Replace GPS` check-mark should be checked, and the :guilabel:`Update` button should be pressed.

After all of the household data has been recorded, the user should synchronize their results to the server (:ref:`Syncing instructions <services-using-sync>`).

.. _episample-tour-geo-survey-implementation:

Implementation
----------------------

The basic structure of the user interface is defined in :file:`assets/eps_collect.html`, including all the input fields and the container for the list. Dynamic adjustments to this user interface, as well as calls to the database and device hardware, are made in :file:`assets/js/eps_collect.js`. This file's makes heavy use of the third party :program:`Backbone` JavaScript library. Also notice that the third party library :program:`Underscore` is included, along with template HTML, for dynamically adding list items.

The file :file:`eps_collect.js` handles:

  1. Keeping track of the GPS coordinates and accuracy in real time. It also updates the user interface as necessary when these change. The thresholds for GPS accuracy are read from the settings with the :file:`epsConfigLib.js` file.
  2. Reading, Creating, and Updating records in the *Census* table. This data is also validated before being recorded. The records are read through a number of calls to :code:`odkData.query(...)` and :code:`odkData.ArbitraryQuery(...)`. They are recorded with calls to :code:`odkData.addRow(...)` and the are updated with calls to :code:`odkData.updateRow(...)`.
  3. Dynamically creating the visualization of the list of records from the *Census* and updating it as that list changes. This list is also paginated. The running totals of *Valid*, *Invalid*, and *Excluded* records are populated with :code:`odkData.arbitraryQuery` calls.

The file :file:`assets/js/util.js` is included to generate UUIDs (unique ids and primary keys in the database) for each new record as it is created.


.. _episample-tour-geo-survey-implementation-files:

Files
~~~~~~~~~~~~~~~~

  - :file:`assets/eps_collect.html`
  - :file:`assets/js/eps_collect.js`
  - :file:`assets/js/util.js`

.. _episample-tour-geo-survey-implementation-forms:

Forms
~~~~~~~~~~~~~~~~

None

.. _episample-tour-geo-survey-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~

  - *Config*
  - *Census*



