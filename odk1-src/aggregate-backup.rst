.. spelling::

  macOS

Backing Up Aggregate
====================

.. warning::
  Aggregate is no longer actively developed. Please use :doc:`ODK Central <central-intro>` instead.

Backup and restore forms and submissions with Briefcase
-------------------------------------------------------

You can use :doc:`ODK Briefcase <briefcase-intro>` to backup your forms and submissions by :ref:`pulling <pull-from-aggregate>` them from Aggregate, and restore them by :ref:`pushing <push-to-aggregate>` them back to Aggregate.

.. warning::

  Please, be aware that this procedure doesn't backup your server's configuration, users, exported forms, publisher configurations, and other important settings that you might still want to account for.

PostgreSQL backup & restore
---------------------------

Backup
~~~~~~

1. Stop running Tomcat. This step, although optional, is recommended to produce full and coherent database dumps.

2. Produce a database backup file:

  .. tabs::

    .. group-tab:: Windows

      .. code-block:: console

        pg_dump.exe [ dbname ] > [ backup file location ]

    .. group-tab:: macOS and Linux:

      .. code-block:: console

        pg_dump [ dbname ] > [ backup destination ]

3. Start Tomcat if you stopped it on the first step.

You could get some errors depending on your particular PostgreSQL users and server configuration. Refer to the `pg_dump documentation <https://www.postgresql.org/docs/10/app-pgdump.html>`_ for more information on the options you can add to this command.

Restore
~~~~~~~
1. Stop running Tomcat.

2. Load the backup file:

  .. tabs::

    .. group-tab:: Windows

      .. code-block:: console

        psql.exec -f [ backup file location ] [ dbname ]

    .. group-tab:: macOS and Linux:

      .. code-block:: console

        psql -f [ backup file location ] [ dbname ]

3. Start Tomcat.

You could get some errors depending on your particular PostgreSQL users and server configuration. Refer to the `psql documentation <https://www.postgresql.org/docs/10/app-psql.html>`_ for more information on the options you can add to this command.

MySQL backup & restore
----------------------

Backup
~~~~~~

1. Stop running Tomcat. This step, although optional, is recommended to produce full and coherent database dumps.

2. Produce a database backup file:

  .. tabs::

    .. group-tab:: Windows

      .. code-block:: console

        mysqldump.exe [ dbname ] > [ backup file location ]

    .. group-tab:: macOS and Linux:

      .. code-block:: console

        mysqldump [ dbname ] > [ backup destination ]

3. Start Tomcat if you stopped it on the first step.

You could get some errors depending on your particular MySQL users and server configuration. Refer to the `mysqldump documentation <https://dev.mysql.com/doc/refman/5.6/en/mysqldump.html>`_ for more information on the options you can add to this command.

Restore
~~~~~~~
1. Stop running Tomcat.

2. Load the backup file:

  .. tabs::

    .. group-tab:: Windows

      .. code-block:: console

        mysql.exec [ dbname ] < [ backup file location ]

    .. group-tab:: macOS and Linux

      .. code-block:: console

        mysql [ dbname ] < [ backup file location ]

3. Start Tomcat.

You could get some errors depending on your particular MySQL users and server configuration. Refer to the `mysql documentation <https://dev.mysql.com/doc/refman/5.6/en/mysql.html>`_ for more information on the options you can add to this command.
