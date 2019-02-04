Backing Up Aggregate
================================

.. _briefcase-backup:

Recovering data from Briefcase
------------------------------

Use :doc:`ODK Briefcase  <briefcase-intro>` to back up all forms and submissions on Aggregate. You can :ref:`pull forms from your Aggregate server <pull-from-aggregate>` into your local machine using Briefcase. In particular, Briefcase's :ref:`command line interface <cli-use>` makes this easier.

.. _mysql-backup:

Recovering database from MySQL dump
--------------------------------------

1. Stop running Tomcat.
2. :doc:`Upgrade to the latest version of Aggregate <aggregate-upgrade>`.
3. Finally, restore it from MySQL dump. An SQL dump of a database is a common method to safely store away a snapshot of the database for archival purposes or to migrate data between database instances, e.g. between two major system releases. The content of a SQL dump is a large collection of SQL commands in ASCII. Running the script will recreate the database in the same state as it was when the dump was created. The primary tool to consider for making an ASCII dump is `mysqldump <https://dev.mysql.com/doc/mysql-backup-excerpt/5.7/en/using-mysqldump.html>`_, which includes a wide variety of options.

.. code-block:: console

  $ mysqldump [ options ] [ dbname ]

Some of the useful options are:

- :option:`-h hostname` or :option:`--host=hostname` specifies host to connect to.
- :option:`-p portnr` or :option:`--port=portnr` specifies port to connect to.
- :option:`-u user` or :option:`--user=user` specifies user id.
- :option:`-d database` or :option:`--database=database` specifies database to connect to.

To take a backup of database:

.. code-block:: console

  $ mysqldump database > backup-file.sql;

To restore a database:

.. code-block:: console

  $ mysql database < backup-file.sql;

To copy a database from one server to another

.. code-block:: console

  $ mysqldump --opt database | mysql --host=remote_host -C database

**remote_host** indicates a remote server where you want to take backup.

.. note::

  Creation of the dump respects your credentials, which means you only can dump the tables you have access to.
