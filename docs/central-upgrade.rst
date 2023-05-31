.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. We recommend that you upgrade as soon as you can to get access to the newest features, bug fixes, and security updates. It is not possible to downgrade and we do not guarantee that versions prior to the latest release can still be installed.

Start by reviewing upgrade notes for all versions between your current version and the one you are upgrading to. You can skip upgrades and directly install the latest version as long as you make sure to follow all relevant upgrade instructions.

Upgrade notes
-------------

* :ref:`Central v2023.2 <central-upgrade-2023.2>`: upgrade Docker, PostgreSQL, and move configuration to ``.env``
* :ref:`Central v2023.1 <central-upgrade-2023.1>`: plan ahead for longer than usual downtime during upgrade
* :ref:`Central v2022.3 <central-upgrade-2022.3>`: update your NGINX configuration if you have disabled or customized Sentry
* :ref:`Central v1.5 <central-upgrade-1.5>`: fix errors with ``git pull`` if you have disabled or customized Sentry
* :ref:`Central v1.4 <central-upgrade-1.4>`: optionally add memory if you have tens of thousands of submissions
* :ref:`Central v1.3 <central-upgrade-1.3>`: ensure you have the correct version of ``docker-compose``
* :ref:`Central v1.2 <central-upgrade-1.2>`: fix errors with ``git pull``
* Central v1.0, v1.1: no upgrade notes
* :ref:`Central v0.9 <central-upgrade-0.9>`: configure firewall

.. note::
  To see your version, click on the question mark icon in the upper right section of your Central menu bar, then click :guilabel:`Version`. If you don't see the question mark, you can see the version by adding ``version.txt`` to the root URL (e.g., `demo.getodk.cloud/version.txt <https://demo.getodk.cloud/version.txt>`_).

.. _central-upgrade-steps:

Upgrade steps
----------------

.. warning::
  Before starting:

  #. :doc:`Back up your server <central-backup>`.
  #. Make sure you have some time available in case something goes wrong (we recommend at least 2 hours). You may want to announce a maintenance window.
  #. Review upgrade instructions for **all versions** between your current version and the version you are upgrading to.

#. **Log into your server**. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>`, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

#. **Get the latest infrastructure version**.

.. code-block:: console

  $ cd central
  $ git pull

.. note::

  If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, run ``git pull`` and it will tell you.

3. **Get the latest client and server**.

.. code-block:: console

  $ git submodule update -i

4. **Build** from the latest code you just fetched. The ``pull`` option ensures all Docker images are up-to-date.

.. code-block:: console

  $ docker compose pull
  $ docker compose build --pull

.. note::

  If you run into problems with this step, try stopping Central (``docker compose stop``) and then retry ``docker compose build --pull``.

5. **Clean up unused Docker images**

.. code-block:: console

  $ docker image prune

You'll be asked to confirm the removal of all dangling images. Agree by typing the letter ``y`` and pressing ``Enter``.

.. note::

  For a more thorough, but potentially dangerous clean up, consider using `docker system prune <https://docs.docker.com/engine/reference/commandline/system_prune/>`_.


6. Restart the server

.. code-block:: console

  $ docker compose up -d

.. _version-specific-instructions:

Version-specific upgrade instructions
--------------------------------------

.. _central-upgrade-2023.2:

Upgrading to Central v2023.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is *critical infrastructure upgrade*. In particular, it upgrades the included PostgreSQL database from 9.6 (no longer supported) to 14 (stable and supported through 2026). Docker and Docker Compose are also upgraded. This release also changes the way that configurations are made to reduce conflicts with future updates to Central. Please read the following instructions carefully.

.. warning::
  This upgrade may take more time and disk space than previous updates.

.. warning::
  Before starting:

  #. :doc:`Back up your server <central-backup>`.
  #. Make sure you have some time available in case something goes wrong (we recommend at least 3 hours). You may want to announce a maintenance window.
  #. Review upgrade notes for all versions between your current version and the version you are upgrading to.

#. **Log into the web interface** and make a quick note of some of the data you see, such as submission counts and latest submission dates. You may want to use this information to do a quick spot check after the upgrade is finished.

#. **Log into your server.** If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>`, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

#. **Go to the central folder.**

   .. code-block:: console

     $ cd central

#. **Upgrade Docker if needed.** Check to see if you have Docker Engine v23.x and Docker Compose v2.16.x or greater:

   .. code-block:: console

     $ docker --version && docker compose version

   If you are using old versions, follow the instructions to install `Docker Engine <https://docs.docker.com/engine/install/ubuntu>`_ (not Desktop) for Ubuntu, the operating system we recommend and support. The instructions will help you setup the Docker ``apt`` repository and install the latest version of Docker Engine and Docker Compose.

#. **Remove docker-compose.** You will be using ``docker compose`` from now on (the dash has been replaced with a space).

   .. code-block:: console

     $ rm -f `which docker-compose`

#. **Migrate configuration customizations.** This will simplify future Central upgrades. First, check what files have been customized:

   .. code-block:: console

     $ git status

   If you do not see any files listed with a `modified:` prefix, you can go on to the next step.

   If you see files listed with a `modified:` prefix, follow instructions for each of them:

   .. dropdown:: ``files/service/config.json.template``
     :icon: file-code

     #. Make a backup copy of the file. You will manually copy differences to your local computer later so this is for additional protection:

        .. code-block:: console

          $ cp files/service/config.json.template files/service/config.json.template.bak

     #. Copy changes to your local computer:

        .. code-block:: console

          $ git diff files/service/config.json.template

        You will see additions in green with ``+`` prefixes. Copy those to a scratch file on your local computer (e.g. using CTRL+C and CTRL+V). You will use this to copy your custom values into the new format.

     #. Open the ``.env`` file for editing:

        .. code-block:: console

          $ nano .env

     #. If you use a custom database server, you will see changes in the database section. Copy the values from that section to the ``.env`` file in the following format:

        .. code-block:: bash

          DB_HOST=my-db-host
          DB_USER=my-db-user
          DB_PASSWORD=my-db-password
          DB_NAME=my-db-name

        .. note::

          If your password has special characters in it, you will need to put single quotes ( ``'`` and ``'``) around the password. Values without special characters do not need quotes around them.

        .. note::

          If your database requires an SSL connection, add ``DB_SSL=true`` to ``.env``. If you don't need an SSL connection, omit that variable. Note that ``DB_SSL=true`` allows self-signed certificates.

     #. If you use a custom email server, you will see changes in the email section. Copy those values to the ``.env`` file in the following format:

        .. code-block:: bash

          EMAIL_FROM=my-no-reply-email-address
          EMAIL_HOST=my-email-host
          EMAIL_PORT=my-email-port
          EMAIL_IGNORE_TLS=true-or-false
          EMAIL_SECURE=true-or-false
          EMAIL_USER=my-email-user
          EMAIL_PASSWORD=my-email-password

        .. note::

          ``EMAIL_IGNORE_TLS`` should generally be set to ``false``. ``EMAIL_SECURE`` should generally be set to ``true`` if you use port 465 and to ``false`` for other ports.

        .. note::

          If your password has special characters in it, you will need to put single quotes ( ``'`` and ``'``) around the password. Values without special characters do not need quotes around them.

        .. note::

          ``EMAIL_FROM`` is equivalent to ``email.serviceAccount`` in the json config. If you omit it, the default is ``no-reply@${YOUR_DOMAIN}``. You can specify a name that will be shown by email clients by using the following structure:

          .. code-block:: bash

            EMAIL_FROM=My Cool Server <no-reply@my-server.server>

     #. Discard all ``files/service/config.json.template`` customizations. Make sure you have correctly copied all of them into ``.env``. You may want to keep the copy on your local computer until you have verified that everything works.

        .. code-block:: console

          $ git checkout -- files/service/config.json.template

   .. dropdown:: ``docker-compose.yml``
     :icon: file-code

     #. Make a backup copy of the file. You will manually copy differences to your local computer later so this is for additional protection:

        .. code-block:: console

          $ cp docker-compose.yml docker-compose.yml.bak

     #. Copy changes to your local computer:

        .. code-block:: console

          $ git diff docker-compose.yml

        You will see additions in green with ``+`` prefixes.

        You can ignore any changes related to a custom database because those have been addressed by migrating ``files/service/config.json.template``.

        Copy any other changes to a scratch file on your local computer (e.g. using CTRL+C and CTRL+V). You will use this to copy your custom values into the new format.

     #. If you specify a value for ``SERVICE_NODE_OPTIONS``, open the ``.env`` file for editing:

        .. code-block:: console

          $ nano .env

        Copy that to the ``.env`` file in the following format:

        .. code-block:: bash

          SERVICE_NODE_OPTIONS=my-node-options

     #. If you specify any other customizations in your ``docker-compose.yml`` file, this is considered advanced and you will need to apply them manually after the upgrade. If you're not sure how to do this, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.

     #. Discard all ``docker-compose.yml`` customizations. Make sure you have correctly copied all of them into ``.env``. You may want to keep the copy on your local computer until you have verified that everything works.

        .. code-block:: console

          $ git checkout -- docker-compose.yml

   .. dropdown:: ``files/enketo/config.json.template`` or any others
     :icon: file-code

     #. Stash changes so they can be applied after the upgrade. These are considered advanced customizations and you may need to resolve merge conflicts when you re-apply them.

        .. code-block:: console

          $ git stash


#. **Determine whether the server you are upgrading is using a custom database** (e.g. externally hosted on Azure, AWS, etc.) or the default one:

   .. code-block:: bash

     grep DB_HOST .env

   If you get nothing back or there's nothing after the ``=``, you are using the default database. If ``DB_HOST`` is set to any value, you are using a custom database server.

#. **Upgrade your database** according to your database type.

   .. tabs::
   
     .. tab:: Default database
       .. warning::
         Before starting:
   
         * Read the instructions at the top of this section carefully and **make sure you are actually using the default database configuration**. Following these instructions with a custom database setup could result in perceived data loss.
   
       #. **Get the latest infrastructure version.**
   
          .. code-block:: console
   
             $ git pull
   
       #. **Get the latest client and server.**
   
          .. code-block:: console
   
             $ git submodule update -i
   
       #. **Check that you have enough disk space available.** If you are prompted for a password, enter the system superuser password (not a Central password). You will see a message about how much space is required and if you have enough free space to proceed.
   
          .. code-block:: console
   
             $ sudo ./files/postgres14/upgrade/check-available-space
   
          *If you don't have enough space,* **stop here** and resume when you have increased the disk space available. You may achieve this by clearing out data you don't need (e.g., logs) or by    increasing the total disk space available (e.g., by :ref:`adding external storage <central-install-digital-ocean-external-storage>`).
   
       #. **Create a file to prove that you're carefully reading these instructions.** This is required to continue.
   
          .. code-block:: console
   
             $ touch ./files/allow-postgres14-upgrade
   
       #. **Reapply any advanced customizations**. If you had made notes on advanced configurations and/or stashed some edited files, reapply those advanced customizations now:

          .. code-block:: console

             $ git stash pop

       #. **Build from the latest code you just fetched.**
   
          .. code-block:: console
   
             $ docker compose pull
             $ docker compose build --pull
   
       #. **Start the database upgrade and wait for the process to exit.** This is where the new PostgreSQL 14 database is made and data copied into it. This will take a long time if you have a lot of data and/or a slow server.
   
          .. code-block:: console
   
             $ docker compose up postgres
   
       #. **Check the output of the previous command to see if there were any errors.** If there were any errors that you can't resolve, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.
   
       #. **Check the upgrade success file has been created.**
   
          .. code-block:: console
   
             $ ls ./files/postgres14/upgrade/upgrade-successful
   
          If you see "No such file or directory," try doing ``docker compose up postgres`` again. If the file has still not been created, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.
   
       #. **Restart the server.**
   
          .. code-block:: console
   
               $ docker compose up -d
   
       #. **Log into the web interface and do some quick spot checks.** For example, verify that submission counts and latest submission dates look right and try a data export.
   
       #. **Clean up**
   
          #. **Remove unused Docker images**.

             .. code-block:: console

                 $ docker image prune

             You'll be asked to confirm the removal of all dangling images. Agree by typing ``y`` and pressing Enter.

          #. **See how much space the old database takes**. The upgrade process performs a copy and leaves the old database intact.

             .. code-block:: console

                  $ docker compose up postgres

          #. **Delete the old data**. Make sure you have verified that the server works as expected first.

             .. code-block:: console
   
               $ touch ./files/postgres14/upgrade/delete-old-data \
                  && docker compose up --abort-on-container-exit postgres
   
     .. tab:: Custom database
       .. warning::
        Using PostgreSQL 14 isn't strictly required, but we only test with and support PostgreSQL 14.

       #. **Find instructions for upgrading your database server to PostgreSQL 14**. Here are instructions for some popular fully-managed options:
   
          * `DigitalOcean <https://docs.digitalocean.com/products/databases/postgresql/how-to/upgrade-version/>`_
          * `Amazon <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html#USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Process>`_
          * `Azure <https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-upgrade-using-dump-and-restore>`_
   
       #. **Determine whether upgrading your database requires downtime**. If it does, stop Central before continuing:
   
          .. code-block:: console
   
            $ docker compose stop
   
       #. **Upgrade your database server**. We recommend using the latest point release of PostgreSQL 14 that is available.

       #. **Regenerate optimizer statistics**. You need to regenerate all database statistics to avoid performance issues. Run the following SQL command inside your database.
   
          .. code-block:: postgresql
   
            ANALYZE VERBOSE;

       #. **Create a file to prove that you're carefully reading these instructions.** This is required to continue.
   
          .. code-block:: console
   
            $ touch ./files/allow-postgres14-upgrade
   
       #. Follow the :ref:`standard upgrade instructions <central-upgrade-steps>`.

.. _central-upgrade-2023.1:

Upgrading to Central v2023.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several time-consuming steps in this upgrade. Central will not be accessible during those steps. Plan for a minimum of an hour of downtime.

If you have 30k or more submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

If you have 20k or more versions of a single form (generally generated by an automated script that uses the API to update a form attachment), email support@getodk.org with details about your infrastructure and the number of form versions you have **before starting the upgrade process** so we can help you plan for a successful upgrade.

.. _central-upgrade-2022.3:

Upgrading to Central v2022.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v2022.3, we added Content Security Policy reporting. If you have disabled or customized Sentry, then you will need to modify ``files/nginx/odk.conf.template``. See our documentation about :ref:`configuring Sentry <central-install-digital-ocean-sentry>` to learn more about the specific changes that you need to make.

.. _central-upgrade-1.5:

Upgrading to Central v1.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v1.5.3, we updated Central's Sentry configuration to match a change to the Sentry API. If you have not changed your :ref:`Sentry configuration <central-install-digital-ocean-sentry>`, then you do not need to do anything special.

If you have changed your Sentry configuration, that means that you have modified ``files/service/config.json.template``. If you run the ``git pull`` command, then you will see an error message like the following:

.. code-block:: console

 error: Your local changes to the following files would be overwritten by merge:
         files/service/config.json.template
 Please commit your changes or stash them before you merge.

Don't worry, nothing bad happens if you see this. To get around this error, run this set of commands instead of ``git pull``:

.. code-block:: console

 mv files/service/config.json.template config-tmp
 git pull
 mv config-tmp files/service/config.json.template

If you see an error message when you run this set of commands, copy and paste your entire console session into a `forum thread <https://forum.getodk.org/c/support/6>`_ and someone will help you out.

If you are using your own Sentry instance, then you must complete one additional step. You will need to modify ``files/service/config.json.template``. Below the line that contains ``"sentry": {``, insert a new line that looks like this:

.. code-block:: console

 "orgSubdomain": "SENTRY_ORGANIZATION_SUBDOMAIN",

Replace ``SENTRY_ORGANIZATION_SUBDOMAIN`` with your `Sentry organization subdomain <https://forum.sentry.io/t/organization-subdomains-in-dsns/9360>`_.

.. _central-upgrade-1.4:

Upgrading to Central v1.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several time-consuming migrations in v1.4. If you have tens of thousands of submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

.. _central-upgrade-1.3:

Upgrading to Central v1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before upgrading, run ``docker-compose --version`` to confirm you have docker-compose v1.28.3 or later. If you don't, upgrade with these commands from `Docker's documentation <https://docs.docker.com/compose/install/#install-compose-on-linux-systems>`_.

.. code-block:: console

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

.. _central-upgrade-1.2:

Upgrading to Central v1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v1.2, we added some advanced features to Central's server configuration. These features will not be meaningful to most users. However, because we would like to make this change and further improvements in the future, we have modified the template ``.env`` configuration file you set up during installation.

Since you have made your own changes to the ``.env`` file to set Central up for your environment, you will see an error message when you run the ``git pull`` command:

.. code-block:: console

 error: Your local changes to the following files would be overwritten by merge:
         .env
 Please commit your changes or stash them before you merge.

Don't worry, nothing bad happens if you see this. To get around this error, run this set of commands instead of ``git pull``:

.. code-block:: console

 mv .env env-tmp
 git pull
 mv env-tmp .env

Afterwards, ``git status`` should not say anything about the ``.env`` file at all and you can continue with the upgrade instructions above. 

If ``git status`` still shows errors, copy and paste your entire console session into a `forum thread <https://forum.getodk.org/c/support/6>`_ and someone will help you out.

.. _central-upgrade-0.9:

Upgrading to Central v0.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Particularly if you are installed on DigitalOcean, you will need to modify the system firewall for Enketo features in Central to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  While it sounds dangerous, disabling your system firewall does not put your server at greater risk. In fact, most Linux operating systems come with the system firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be really difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your Central website over HTTPS on its public domain name from within the Enketo container, all Enketo features should work correctly.


