Task List Generation
============================

.. image:: /img/episample-tour/episample-task-gen.*
  :alt: Task List Generation
  :class: device-screen-vertical

.. _episample-tour-task-gen-function:

Function
-------------------

The Task List Generation module is used to create a randomized task list for each data collector to perform.

.. note::

  It is important that the Task List Generation module has access to all of the census data. Every data collector should synchronize their device to the server (:ref:`Syncing instructions <services-using-sync>`) so that all the records are available. After that, a synchronization can be performed to receive the full record set.

The :guilabel:`Main`, :guilabel:`Additional`, and :guilabel:`Alternate` points parameters are set in the :doc:`episample-tour-config` module.

.. tip::

  To allow these fields to be set in this module, set the parameters to zeros in the Config module.

If there are sufficient records available to meet the parameters, the user can press the :guilabel:`Select` button to generate the task list. A progress bar will appear while this process takes place, followed by a completion notification. This process can take some time if the data set is large. After the task list is generated it can be synchronized to the server, followed by each data collector synchronizing to receive the list.

This list of tasks is used to determine where to perform follow up surveys.


.. _episample-tour-task-gen-implementation:

Implementation
--------------------

The file :file:`assets/eps_select.html` implements the look of this screen. This screen is not nearly as dynamic as the others, and as such most of the user interface is hard coded here. This includes the loading screen that appears while the list is being generated.

The file :file:`assets/js/eps_select.js` reads the *Main*, *Alternate*, and *Additional* point configuration and populates the user interface with it. If these are configured to zeros, it will read in the user defined values for these fields.

When the :guilabel:`Select` button is pressed, the configuration is used to determine the points to select for the task list. The third party :program:`Async` library is used to handle these long running calculations in the background without locking up the user interface. While they run, the :guilabel:`Please Wait` loading screen is shown. The records are read from the *Census* table with an :code:`odkData.arbitraryQuery` call, and then randomized. When this process is complete, the affected records in the *Census* table are updated with :code:`odkData.updateRow` calls.


.. _episample-tour-task-gen-implementation-files:

Files
~~~~~~~~~~~~~~~~~~

  - :file:`assets/eps_select.html`
  - :file:`assets/js/eps_select.js`

.. _episample-tour-task-gen-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~

None

.. _episample-tour-task-gen-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~

  - *Config*
  - *Census*


