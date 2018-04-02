.. spelling::
  Prepopulated
  prepopulated

Household Data Collection
==============================

.. image:: /img/episample-tour/episample-household-survey.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _episample-tour-househould-survey-function:

Function
--------------

The Household Data Collection module is an ODK Survey form that is configured in the :doc:`episample-tour-config` module. This is intended to be provided by the Deployment Architect for their particular use case, which makes this application flexible to different scenarios. For example, this could be used for follow up after a Malaria outbreak or it could be adapted to handle another disease by swapping this form.

The data collected in this form is available in the same database as the rest of the application and can be used by it.

.. _episample-tour-household-survey-implementation:

Implementation
--------------------

The Household Data Collection form is user configured and not provided in this reference application. The provided form could be a simple survey or could include complex skip logic, data quality checks, and customizations to the look-and-feel. Instructions for creating these forms are available in :ref:`build-app-designing-a-form` guide as well as the :doc:`xlsx-converter-intro` guide.

Prepopulated forms could also be included with CSV files. See the files in the :file:`assets/csv` directory  and the :file:`assets/tables.init` file for examples.

.. _episample-tour-household-survey-implementation-files:

Files
~~~~~~~~~~~~

  - The files associated with the selected form.

.. _episample-tour-household-survey-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~

  - The form configured in the :doc:`episample-tour-config` module.

.. _episample-tour-household-survey-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~

  - The table corresponding to the selected form.


