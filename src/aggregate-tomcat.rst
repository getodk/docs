:orphan:

.. spelling::

  databaseserver
  Glassfish
  useHttpOnly
  sudo

Installing on Tomcat
====================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

`Apache Tomcat <http://tomcat.apache.org/>`_ is an open source Java web server that can be used to serve ODK Aggregate.

This document guides you through the installation and initial setup of a self-hosted instance of ODK Aggregate, running on Tomcat with a `PostgreSQL <https://www.postgresql.org/>`_, or `MySQL <https://www.mysql.com/>`_ database server. "Self-hosted" could mean on your own hardware or on a cloud-based server.

If you're planning on hosting your server on a cloud provider, you can use these provider-specific guides:

- :doc:`DigitalOcean (recommended) <aggregate-digital-ocean>`
- :doc:`Amazon Web Services <aggregate-aws>`
- :doc:`Google Cloud <aggregate-google-cloud>`
- :doc:`Microsoft Azure <aggregate-azure>`

.. note::

  - Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility. You must also plan for the security of your data and systems.

  - Local hosting requires that you configure your network routers. It is recommended to seek assistance from your local computer technical support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.


Considerations before you begin
----------------------------------

Please, read the :doc:`Aggregate deployment planning <aggregate-deployment-planning>` guide before continuing.

Database systems
~~~~~~~~~~~~~~~~~~

ODK Aggregate works with any of these database servers:

- PostgreSQL

  PostgreSQL is the recommended database server for Aggregate.

- MySQL

  Although MySQL is supported, it's not actively being tested during the release cycle. MySQL tables have a row size limit that will affect performance for very large forms.


Installation procedure
--------------------------

1. Install Java 8.0.221 or higher. We recommend using OpenJDK 11 LTS from AdoptOpenJDK:

  .. tabs::

    .. group-tab:: Windows

      Download `OpenJDK 11 LTS <https://adoptopenjdk.net/>`_ and run it as administrator.

    .. group-tab:: macOS

      Download `OpenJDK 11 LTS <https://adoptopenjdk.net/>`_ and install it.

    .. group-tab:: Ubuntu

      .. code-block:: console

        sudo apt-get install openjdk-11-jre

2. Ensure that the installed Java bin directory is in the `PATH environment variable <https://docs.oracle.com/javase/tutorial/essential/environment/paths.html>`_.

3. Install Apache Tomcat 8.5:

  .. tabs::

    .. group-tab:: Windows

      Download `the Windows Service installer <https://tomcat.apache.org/download-80.cgi>`_, and run it as administrator.

    .. group-tab:: macOS

      If you have `Homebrew <https://brew.sh>`_, run:

      .. code-block:: console

        brew install tomcat@8.5

    .. group-tab:: Ubuntu

      .. code-block:: console

        sudo apt-get install tomcat8 tomcat8-common tomcat8-user tomcat8-admin

4. Configure your server and network devices so that laptops or Android devices connecting to the internet from an external access point can access your server.

  If your organization has a network or systems administrator, contact them for assistance. The steps for this are:

  - configure your server firewall to allow access
  - make your server visible on the internet (optional)
  - establish a DNS name for the server

5. `Obtain and Install an SSL certificate <https://gist.github.com/yanokwa/399a7fcbc3d9ad8a0bd3>`_ if you need secure ``https`` access.

6. Install PostgreSQL:

  .. tabs::

    .. group-tab:: Windows

      Download `the PostgreSQL 10.6 Windows installer <https://www.enterprisedb.com/downloads/postgres-postgresql-downloads>`_, and run it as administrator.

    .. group-tab:: macOS

      Download `the PostgreSQL 10.5 Postgres.app DMG installer <https://postgresapp.com/downloads.html>`_, and open it.

    .. group-tab:: Ubuntu

      .. code-block:: console

        sudo apt-get install postgresql-10

7. Install `ODK Aggregate <https://github.com/getodk/aggregate/releases/latest>`_. Select the latest release for your operating system.

  The installer will guide you through configuring ODK Aggregate for your setup. The installer will produce a WAR file (web archive) containing the configured ODK Aggregate code, a :file:`create_db_and_user.sql` script for creating the database and user that ODK Aggregate will use to access this database, and a :file:`Readme.html` file with instructions on how to complete the installation.

  .. tip::

    - When asked for the fully qualified hostname of the ODK Aggregate server, you should enter the DNS name you established above.
    - The install also asks for a database name, user and password. The user should not be postgres (PostgreSQL), or root (MySQL).
    - ODK Aggregate will use this user when accessing this database (and it will only access this database).
    - By specifying different databases and users, you can set up multiple ODK Aggregate servers that share the same database server, store their data in different databases, and operate without interfering with each other.
    - If you are upgrading to a newer version of ODK Aggregate, as long as you specify the same database name, user and password, you do not need to re-run the :file:`create_db_and_user.sql` script.
