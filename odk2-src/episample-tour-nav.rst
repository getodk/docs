Geographic Navigation
==========================

.. image:: /img/episample-tour/episample-navigation.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _episample-tour-nav-function:

Function
---------------------

The Navigation Module helps guide a data collector to the households specified in the task list. The compass, distance, and other navigational indicators will update in real time.

The map will show the points on the task list. The households displayed can be configured on the :doc:`episample-tour-main-menu` module to show only *Main* points, or show *Main* and *Additional* and so on.

When the data collector arrives at the household, they can tap the :guilabel:`Arrive` button to launch the :doc:`episample-tour-household-survey` module. Or they can press :guilabel:`Cancel` at any time to return to the Main Menu.


.. _episample-tour-nav-implementation:

Implementation
------------------

This view is provided by the ODK 2 platform and is not customizable. The view is launched by a call to :code:`odkTables.openTableToNavigateView(...)` with query parameters to select the map markers. The query that selects the map markers is discussed in the :ref:`episample-tour-main-menu-implementation` section. The handling of the results of the :guilabel:`Arrive` and :guilabel:`Cancel` button presses are also discussed in that section.

.. _episample-tour-nav-implementation-files:

Files
~~~~~~~~~~~~~~

None

.. _episample-tour-nav-implementation-forms:

Forms
~~~~~~~~~~~~~~

None

.. _episample-tour-nav-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~

  - *Census*


