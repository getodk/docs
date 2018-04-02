Inventory Management and Maintenance App
==========================================

.. _cold-chain-intro:

The Cold Chain application is a health facility maintenance application originally developed at the University of Washington in collaboration with `PATH <http://www.path.org/>`_ and `Village Reach <http://www.villagereach.org/>`_. It is a prototype meant to be deployed at national scale to manage refrigerator inventory and maintenance at health facilities across the country. The purpose of this is to ensure vaccines are kept at sufficiently cold temperature and maintain their efficacy.

  .. image:: /img/cold-chain-intro/cold-chain-home.*
    :alt: Cold Chain Home Screen
    :class: device-screen-vertical side-by-side


.. _cold-chain-odk2-features:

Key Features
----------------------------

The Cold Chain application provides a good example of the following ODK 2 platform features:

  - **Data Synchronization and Reuse**: The health facility, refrigerator, and maintenance log data set is stateful rather than the traditional model of being actively collected. If a refrigerator breaks, it is synchronized and the state is updated so other users can see this state change.
  - **Custom Web Views**: Finding and viewing the details of health facilities, refrigerator models, and individual refrigerators is completely customized to the needs of this application. Custom visualizations provide statistics on the full data set, such as refrigerator age.
  - **Complex Workflows**: This application does not follow the traditional data collection model. A custom workflow for managing and repairing inventory is implemented in JavaScript.
  - **Mapping**: An up to date map of health facilities is rendered from the data set, and is organized into regions, to provide context for where problems may occur and to help navigate to different sites.
  - **Advanced Form Design**: The Survey forms use database queries, choice filters, and other advanced features.
  - **User and Group Permissions**: This application is meant to be deployed at national scale with thousands of data points. Each user is only given access to a subset of that data that is relevant to their region, and is not be able to modify data outside of their area of responsibility.
  - **Translations**: This application supports both English and Spanish locales.


  .. _cold-chain-installing:

Installing Cold Chain
--------------------------

Source code for this Data Management Application can be found in the `cold-chain-demo branch ofthe App Designer repository <https://github.com/opendatakit/app-designer/tree/cold-chain-demo>`_. As with all of the ODK 2 reference applications (and the ODK 2 platform itself), the code is free and open source. Feel free to reuse, modify, or extend this application and its component parts to suit your organization's needs.

.. warning::

  This application requires user and group permissions to be set up on the server before use. Please review the documentation for :doc:`data-permission-filters` and :ref:`Sync Endpoint LDAP <sync-endpoint-ldap>`.

  You will need at least one user that is a table administrator, and to set up the groups:

    - REGION_NORTH
    - REGION_CENTRAL
    - REGION_CENTRAL_EAST
    - REGION_CENTRAL_WEST
    - REGION_SOUTH
    - REGION_SOUTH_EAST
    - REGION_SOUTH_WEST

  You should add users to the various groups, and set their default group as the region where they can edit records. For example, user `dana` might belong to groups *synchronize_tables*, *region_south* and *region_south_east* and have their default group set to *region_south_east*. In this scenario `data` can modify data in the group *region_south_east* and can see but not modify the rest of *region south* (namely, *region_south_west*).


.. note::
  The Cold Chain application (and all other Data Management Applications provided in these docs) come with a full copy of the Application Designer they were developed in.

After you have have downloaded the application, you can set it up according to the :doc:`Application Designer setup <app-designer-setup>` instructions. Similarly You can push the application to your device using the :ref:`build-app-pushing` instructions.


.. _cold-chain-intro-tour:

Guided Tour
------------------------

A walk-through of the features and the application and an overview of how they are implemented is provided in the guide below.

.. toctree::
  :maxdepth: 2

  cold-chain-tour

