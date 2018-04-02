Initial Data Set
=======================

.. image:: /img/cold-chain-tour/cold-chain-initial-data.*
  :alt: Refrigerator Data Set

.. _cold-chain-tour-initial-data-function:

Function
-----------------

The initial data set is not part of the actual workflow of the application, but is described here to provide context for how this application is set up and how it might be used in the field. This initial data set is the full list of health facilities, refrigerators, and refrigerator types that currently exist in the health system to be modeled. The initial Deployment Architect could choose to collect this data via survey forms within the application itself (which are already provided, and used for adding data as the current state changes), but if they already have a database of health facility inventory, this might be the more convenient method.

For demonstration purposes the provided default data set also has maintenance logs that are seeded into the database.

.. _cold-chain-tour-initial-data-implementation:

Implementation
--------------------

The initial data set is codified in :file:`.csv` files specified in :file:`assets/tables.init` that will be imported into the database on the initial startup. Instructions for how this works are available here: :ref:`tables-managing-config-at-startup`.

Each :file:`.csv` matches the schema of its corresponding table in the database. The appropriate values are filled in for each data field. Additionally, the :th:`_group_modify`, :th:`_group_privileged`, and :th:`group_read_only` columns include the group names to properly organize the data. The full set of custom groups in the provided data set include:

    - **REGION_NORTH**
    - **REGION_CENTRAL**
    - **REGION_CENTRAL_EAST**
    - **REGION_CENTRAL_WEST**
    - **REGION_SOUTH**
    - **REGION_SOUTH_EAST**
    - **REGION_SOUTH_WEST**

.. note::

  The group **GROUP_ADMIN** is also used, but is a default group provided to all Data Management Applications.

The :th:`_group_priviledged` column should be set to :tc:`GROUP_ADMIN` for all rows in all tables. This provides full access to administrators to modify any data they choose. In :file:`refrigerator_type.csv` the columns :th:`_group_modify` and :th:`_group_read_only` should both also be set to :tc:`GROUP_ADMIN` to restrict changes to this protected table. In :file:`health_facility.csv` and :file:`refrigerator.csv` the :th:`_group_modify` column should be set to the most specific group the item belongs to, while the :th:`_group_read_only` column should be set to the broader region. For example, a health facility in the South East region should have its :th:`_group_modify` set to :tc:`GROUP_REGION_SOUTH_EAST` and its :th:`_group_read_only` column set to :tc:`GROUP_REGION_SOUTH`. This will allow users in the South East region to update this facility, but only view facilities in the South West region.

.. note::

  This group organization and permissions set up is specific to the default data set provided with the reference application. However, this is not a requirement of the ODK 2 tools. Groups could be set up to modify regions and view everything, or only read the region they belong to, or even restrict some users from modifying anything and only reading data. See :doc:`data-permission-filters` for more details.

The JavaScript is configured to expect these groups and this set up. To use the application you will need to configure your :doc:`sync-endpoint` to have at least one table administrator. You should also add users to the various groups, and set their default group as the region where they can edit records. For example, user `dana` might belong to groups *synchronize_tables*, *region_south* and *region_south_east* and have their default group set to *region_south_east*. In this scenario `data` can modify data in the group *region_south_east* and can see but not modify the rest of *region south* (namely, *region_south_west*).

.. _cold-chain-tour-initial-data-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~

 - :file:`assets/tables.init`
 - :file:`assets/csv/health_facility.csv`
 - :file:`assets/csv/refrigerators.csv`
 - :file:`assets/csv/refrigerator_types.csv`
 - :file:`assets/csv/refrigerator_types/...`

.. _cold-chain-tour-initial-data-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~

None

.. _cold-chain-tour-initial-data-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~

  - *Health Facility*
  - *Refrigerators*
  - *Regrigerator Types*


