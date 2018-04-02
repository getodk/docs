Configuration
=======================

.. image:: /img/episample-tour/episample-config-blank.*
  :alt: Config Startup
  :class: device-screen-vertical

.. _episample-tour-config-function:

Function
-----------------

The Configuration module is the first screen the user sees after launching the application. It allows the user to customize the behavior of the application via the Settings Screen. It also requires the user to specify the location that the surveys will take place through a series of drop menus. Below you can see that the :guilabel:`Select` button is not revealed until the full location is specified.

  .. image:: /img/episample-tour/episample-config-filled.*
    :alt: Config Ready
    :class: device-screen-vertical

The location chosen on this screen is saved and all future modules will make use of that information.

The Settings screen is a submodule of Configuration. It allows you to customize the behavior of each module. This includes the acceptable GPS accuracy range, the number of data points to collect, and the Survey form to use for the :doc:`episample-tour-household-survey`. These settings are shared across all devices that share :doc:`cloud-endpoints-intro`.

  .. image:: /img/episample-tour/episample-settings.*
    :alt: Config Startup
    :class: device-screen-vertical

The settings can be protected behind a user defined administrative password. If a password is set, the settings cannot be viewed or modified until it is entered, as shown below.

  .. image:: /img/episample-tour/episample-settings-locked.*
    :alt: Config Startup
    :class: device-screen-vertical

.. _episample-tour-config-implementation:

Implementation
-----------------

This is the home screen first shown when the application is launched, so its HTML file must be: :file:`assets/index.html`.

In the :code:`<head>` of :file:`index.html` notice that, among the standard ODK 2 JavaScript imports there are also :file:`libs/sha256.js` and :file:`js/epsConfigLib.js`. The :file:`sha256.js` file is used for encrypting the admin password. The :file:`epsConfigLib.js` file provides an interface for reading and writing the configuration to the *Config* table of the database. Since the configuration is stored in the ODK database, any time the application is synchronized, these settings will be synchronized with the server. In this way an administrator can remotely control the settings on all the field workers phones. This custom library is included across all the files in this application.

The library :file:`libs/bootstrap-3.3.7...` and the file :file:`js/eps_select_place_name.js` are also linked at the bottom of the :code:`<body>`. :program:`Bootstrap` is a third party library used for formatting and look-and-feel. :file:`eps_select_place_name.js` implements the dynamic portions of the user interface of the home screen including: the series of drop downs that specify the place name, the :guilabel:`Settings` button, and the login screen for password protected settings.

The place names dropdowns are populated dynamically by reading from the *Place Names* table. These are read via :code:`odkData.query` and :code:`odkData.arbitraryQeury` calls. When the place name is selected, it is stored for later use by the rest of the modules with :code:`odkCommon.setSessionVariable`. The :guilabel:`Select` button launches :file:`eps_main_menu.html`, which is covered in the next module.

When the :guilabel:`Settings` or :guilabel:`Login` buttons are pressed, they will launch :file:`assets/eps_config.html`. This file implements the Settings screen and all its inputs. It links to :file:`assets/js/eps_config.js` to handle its logic. This file handles reading the stored configuration from the database (via :file:`epsConfigLib.js`), populating that into the form fields, and saving the new configuration back to the database after the :guilabel:`Save` button is pressed.

To populate the :guilabel:`Choose Form` dropdown, the :code:`populateChooseFormControl()` function in :file:`eps_config.js` reads the list of available Survey forms via the :code:`odkData.getAllTableIds` function.

.. _episample-tour-config-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~

  - :file:`assets/index.html`
  - :file:`assets/js/epsConfigLib.js`
  - :file:`assets/js/eps_select_place_name.js`
  - :file:`assets/eps_config.html`
  - :file:`assets/js/eps_config.js`

.. _episample-tour-config-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~

None

.. _episample-tour-config-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~

  - *Config*
  - *Place name*

