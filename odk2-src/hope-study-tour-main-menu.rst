Main Menu
===================

.. image:: /img/hope-study-tour/hope-study-main-menu.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _hope-study-tour-main-menu-function:

Function
---------------

The Main Menu module is the first screen a user sees after launching the application, and provides a basic choice of the three main workflow options available:

  - :guilabel:`Screen Female Client`: to launch the female client screening form: :doc:`hope-study-tour-screen-client`.
  - :guilabel:`Follow Up with Existing Client`: to find the record for an existing client and launch the appropriate follow up form (the :doc:`hope-study-tour-existing-client` module).
  - :guilabel:`Send Data`: To launch the synchronization interface and sync the database with the server: :doc:`hope-study-tour-send-data`.

.. _hope-study-tour-main-menu-implementation:

Implementation
---------------------

This is the first screen a user sees, which would usually imply that its html file is :file:`assets/index.html`. However, this application is embedded within the larger Tables Sample Application, which claims the :file:`index.html` file. That demo launches :file:`assets/hope.html`, which defines this screen. If this application were extracted from this sample application and deployed on its own, this file would need to be renamed :file:`index.html`.

This file creates its HTML :code:`<body>` dynamically with embedded JavaScript. This JavaScript defines the three buttons:

  - :guilabel:`Screen Female Client`: Calls :code:`odkTables.addRowWithSurvey(...)` to launch the *screenClient* form. Notice that the database table being written to is *femaleClients* which is shared among other forms. See the :ref:`Follow Up Forms module implementation details <hope-study-tour-follow-up-forms-implementation>`.
  - :guilabel:`Follow Up with Existing Client`: Calls :code:`odkTables.openTableToListView(...)` to launch the Existing Client module.
  - :guilabel:`Send Data`: Calls :code:`odkCommon.doAction(...)` to launch the *SyncActivity*. This is the same functionality as pressing the sync button in the upper right of the screen, but with two advantages.

    1. The call is embedded within the custom workflow of the application so the user can be instructed to use it at th appropriate time.
    2. The :code:`doAction` function supports the Action-Callback workflow, which means further actions could be triggered after synchronization is completed.


.. _hope-study-tour-main-menu-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~

  - :file:`assets/hope.html`

.. _hope-study-tour-main-menu-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~

None

.. _hope-study-tour-main-menu-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~

None


