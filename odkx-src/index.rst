.. spelling::

  geotagging

ODK-X documentation
================================================

.. _odk-2-introduction:

The ODK-X Tool Suite is free and open-source software for collecting, managing, and using data in resource-constrained environments.

In ODK-X, developers and data managers can create data management applications that consist of survey forms as well as Javascript-based apps. These allow you to render a fully customizable user interface to gather, manage, and visualize data on an Android device.

.. _odk-2-intro-key-features:

Key features
------------

Two-way data sync
"""""""""""""""""
A two-way synchronization protocol allows you to create data management applications with:

 - Follow-up surveys and repeat data collection locations

 - Pre-filled forms for faster data collection

 - Data can be synced to all devices from the server

Offline data collection
"""""""""""""""""""""""
Allows users to collect data without an internet connection. Form data can be synced to the server when the user has internet access.

Linked and embedded surveys
"""""""""""""""""""""""""""
ODX-X tools enable you to open and edit other surveys with links back to the originating survey. Create a sub-form (nested) relationship among surveys (for example: household and household-member) or relational links across your data (for example: tea-houses and tea-types).

View data on device
"""""""""""""""""""
Investigate and visualize entire datasets directly on the device through graphical, map, and tabular displays and through filtered views.

User access control
""""""""""""""""""""
Control data viewing, editing and deleting privileges for different users and groups.

Customizable survey flows and appearance
""""""""""""""""""""""""""""""""""""""""
Use basic web development (HTML, JavaScript, and CSS) to specify the layout of nearly all the screens viewed by the data collectors.

.. _odk-2-intro-list-of-tools:

List of Tools
--------------
The ODK-X Tool Suite consists of:

  - :doc:`survey-intro` - a customizable data **collection** application.
  - :doc:`tables-intro` - a data **curation and visualization** application that can also run custom-built data collection workflows.
  - :doc:`services-intro` - an application for **user authentication and data synchronization** between the ODK-X applications.
  - :doc:`cloud-endpoints-intro` - a **cloud server** to host data and application files, and to support bi-directional data synchronization across mobile devices.
  - :doc:`suitcase-intro` - a **desktop tool** for synchronizing data with a cloud endpoint.
  - :doc:`app-designer-intro` - a design environment for **creating, customizing, and previewing** your forms, data curation, and visualization applications. This is where you build your ODK-X applications.

.. note::
  ODK-X mobile applications are available for Android devices only.

.. _odk-2-intro-selecting-the-right-tools:

Selecting the Right Tools to Use
--------------------------------

The ODK-X tools can operate independently – you are not required to use all the tools, or even install them on your device. Some example tool combinations are:

Field data collection
"""""""""""""""""""""

 - ODK-X Application Designer: data collection form creation
 - ODK-X Survey: data collection
 - ODK-X Services: data sync and database access
 - ODK-X Cloud Endpoints: data and application files cloud server

Data sharing and visualization
""""""""""""""""""""""""""""""

 - ODK-X Tables: data display and visualization
 - ODK-X Services: data sync and database access
 - ODK-X Cloud Endpoints: data and application files cloud server

See :doc:`reference-apps` for examples of ODK-X tools in use.

.. _odk-2-intro-trying-it-out:

Trying It Out
-------------

The :doc:`getting-started-2-user` walks you through the process of using a basic geotagging application and submitting data to the server.


.. toctree::
  :maxdepth: 1
  :hidden:

  select-tool-suite
  getting-started-2-user
  getting-started-2-architect

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Survey

  survey-intro
  survey-install
  survey-sample-app
  survey-using
  survey-managing

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Tables
  
  tables-intro
  tables-install
  tables-sample-app
  tables-using
  tables-managing
  tables-internals

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Services
  
  services-intro
  services-install
  services-using
  services-managing
  services-internals

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Scan
  
  scan-intro
  scan-install
  scan-using
  scan-managing
  scan-data
  
.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Application Designer

  app-designer-intro
  app-designer-setup
  app-designer-using

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Cloud Endpoints

  cloud-endpoints-intro
  sync-endpoint
  aggregate-tables-extension

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Suitcase

  suitcase-intro
  suitcase-install
  suitcase-using

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Application Building

  build-app
  xlsx-converter-intro
  tables-web-pages
  injected-interfaces
  injected-interfaces-methods
  scan-form-designer-intro
  reference-apps

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Advanced Topics

  advanced-topics-architect
  advanced-topics-developer

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Contributing

  contributing

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Reference
