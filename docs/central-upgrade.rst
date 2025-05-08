.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. We recommend that you upgrade as soon as you can to get access to the newest features, bug fixes, and security updates. It is not possible to downgrade and we do not guarantee that versions prior to the latest release can still be installed.

Start by reviewing upgrade notes for all versions between your current version and the one you are upgrading to. You will directly install the latest version but you must follow all upgrade instructions between your current version and the one you are upgrading to. If you are upgrading over many versions, the chance of error increases. We recommend first trying the upgrade on a clone of your production environment to validate the steps that you need to follow.

Upgrade notes
-------------

* Central v2025.1: no upgrade notes
* :ref:`Central v2024.3 <central-upgrade-2024.3>`: update Entity-related forms for offline Entities
* :ref:`Central v2024.2 <central-upgrade-2024.2>`: changes to ``.env`` and SSL no longer require rebuilding, consider using S3 storage
* Central v2023.5, v2024.1: no upgrade notes
* :ref:`Central v2023.4 <central-upgrade-2023.4>`: improve email delivery
* :ref:`Central v2023.3 <central-upgrade-2023.3>`: clean up old database if needed
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

.. code-block:: bash

  $ cd central
  $ git pull

.. note::

  If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, run ``git pull`` and it will tell you.

3. **Get the latest client and server**.

.. code-block:: bash

  $ git submodule update -i

4. **Build** from the latest code you just fetched. The ``pull`` option ensures all Docker images are up-to-date.

.. code-block:: bash

  $ docker compose pull && docker compose build --pull

.. note::

  If you run into problems with this step, try stopping Central (``docker compose stop``) and then retry ``docker compose build --pull``.

5. **Clean up unused Docker images**

.. code-block:: bash

  $ docker image prune

You'll be asked to confirm the removal of all dangling images. Agree by typing the letter ``y`` and pressing ``Enter``.

.. note::

  For a more thorough, but potentially dangerous clean up, consider using `docker system prune <https://docs.docker.com/engine/reference/commandline/system_prune/>`_.


6. Restart the server

.. code-block:: bash

  $ docker compose stop && docker compose up -d

.. _version-specific-instructions:

Version-specific upgrade instructions
--------------------------------------

.. _central-upgrade-2024.3:

Upgrading to Central v2024.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version of Central automatically updates all Entity-related forms so that Entities are created and updated offline in Collect. This change is **NOT compatible with versions of Collect older than v2024.3**. If you use Collect for Entity-related projects, make sure all devices have a recent Collect version before you upgrade Central.

.. _central-upgrade-2024.2:

Upgrading to Central v2024.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are no required special steps related to this upgrade. However, there are some optional changes that you may want to know about or opt into.

1. Changes to ``.env`` and SSL no longer require rebuilding
************************************************************

If you make changes to your ``.env`` file or your SSL certificates to configure Central as described in the :doc:`setup and configuration instructions <central-install-digital-ocean>`, you no longer have to rebuild Central for the changes to take effect. Instead, a stop and restart is now enough:

.. code-block:: bash

   $ docker compose stop
   $ docker compose up -d

2. Files can be stored in S3-compatible storage
************************************************

By default, Central stores all of its data in a database, including files like XLSForm definitions and images attached to submissions. If you have or plan on collecting a lot of files, you may prefer to store these in separate storage to reduce load on the database and possibly reduce hosting costs. See instructions on :ref:`configuring S3-compatible storage <central-install-digital-ocean-s3>`.

3. Docker images now published
*******************************

If you use your own infrastructure for orchestrating the different components needed to run Central, you may prefer to use published Docker images. You can now find these `on GHCR <https://github.com/orgs/getodk/packages?tab=packages&repo_name=central>`_.

.. _central-upgrade-2023.4:

Upgrading to Central v2023.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Determine whether the install you are upgrading is using a custom mail server** or the default one:

   .. code-block:: bash

     $ grep EMAIL_HOST .env

   If you get nothing back or there's nothing after the ``=``, you are using the default mail server. If ``DB_HOST`` is set to any value, you are using a custom mail server.

#. **Upgrade your install** according to your mail server type.

.. tabs::
   
  .. tab:: Default mail server
     .. tip:: While enabling DKIM on the default mail server will improve email delivery, we strongly recommend you use a :ref:`custom mail server <central-install-digital-ocean-custom-mail>` instead.

 
     #. **Copy any existing DKIM files to a new location**.

        .. code-block:: bash

         $ cd central

        .. code-block:: bash

         $ mkdir files/mail
         $ test -f files/dkim/rsa.private && cp files/dkim/rsa.private files/mail/rsa.private 

     #. **Delete the old DKIM folder** and its contents.

        .. code-block:: bash

         $ rm -r files/dkim

     #. **Follow** the :ref:`standard upgrade instructions <central-upgrade-steps>`. Be sure to return here after the upgrade.

     #. **Follow** the :ref:`configure DKIM <central-install-digital-ocean-dkim>` instructions to further improve email delivery. Redo these instructions even if you have previously configured DKIM. 

  .. tab:: Custom mail server

     #. **Follow** the :ref:`standard upgrade instructions <central-upgrade-steps>`.

     .. note:: After the upgrade, consider deleting the now unused DKIM folder and its contents.

        .. code-block:: bash

         $ cd central

        .. code-block:: bash

         $ rm -r files/dkim

.. _central-upgrade-2023.3:

Upgrading to Central v2023.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. **Determine which version of Central you are running.** To see your version, click on the question mark icon in the upper right section of your Central menu bar, then click :guilabel:`Version`. If you don't see the question mark, you can see the version by adding ``version.txt`` to the root URL (e.g., `demo.getodk.cloud/version.txt <https://demo.getodk.cloud/version.txt>`_).

#. **Select the tab below** that matches the version of Central you are running.

.. tabs::

  .. tab:: Versions older than v2023.2

    If you are running a version older than v2023.2, follow the :ref:`Central v2023.2 <central-upgrade-2023.2>` instructions. After following those instructions, you will be running v2023.3. No further action will be needed.

  .. tab:: Version v2023.2

    #. **Determine whether the server you are upgrading is using a custom database** (e.g. externally hosted on Azure, AWS, etc.) or the default one:

       .. code-block:: bash

         $ grep DB_HOST .env

       If you get nothing back or there's nothing after the ``=``, you are using the default database. If ``DB_HOST`` is set to any value, you are using a custom database server.

    #. **If you use the default database, clean up old data.** We have found that this step often failed in the v2023.2 upgrade and have made it more reliable. This is safe to run again even if you already successfully deleted the old database. If you are using a custom database, you don't need to do anything.

       .. code-block:: bash

        $ touch ./files/postgres14/upgrade/delete-old-data \
          && docker compose up --abort-on-container-exit postgres

    #. **Follow** the :ref:`standard upgrade instructions <central-upgrade-steps>`.


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

   .. code-block:: bash

     $ cd central

#. **Upgrade Docker if needed.** Check to see if you have Docker Engine v23.x and Docker Compose v2.16.x or greater:

   .. code-block:: bash

     $ docker --version && docker compose version

   If you are using old versions, follow the instructions to install `Docker Engine <https://docs.docker.com/engine/install/ubuntu>`_ (not Desktop) for Ubuntu, the operating system we recommend and support. The instructions will help you setup the Docker ``apt`` repository and install the latest version of Docker Engine and Docker Compose.

#. **Remove docker-compose.** You will be using ``docker compose`` from now on (the dash has been replaced with a space).

   .. code-block:: bash

     $ rm -f `which docker-compose`

#. **Migrate configuration customizations.** This will simplify future Central upgrades. First, check what files have been customized:

   .. code-block:: bash

     $ git status

   If you do not see any files listed with a `modified:` prefix, you can go on to the next step.

   If you see files listed with a `modified:` prefix, follow instructions for each of them:

   .. dropdown:: ``files/service/config.json.template``
     :icon: file-code

     #. Make a backup copy of the file. You will manually copy differences to your local computer later so this is for additional protection:

        .. code-block:: bash

          $ cp files/service/config.json.template files/service/config.json.template.bak

     #. Copy changes to your local computer:

        .. code-block:: bash

          $ git diff files/service/config.json.template

        You will see additions in green with ``+`` prefixes. Copy those to a scratch file on your local computer (e.g. using CTRL+C and CTRL+V). You will use this to copy your custom values into the new format.

     #. Open the ``.env`` file for editing:

        .. code-block:: bash

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

          ``EMAIL_IGNORE_TLS`` should generally be set to ``false``. ``EMAIL_SECURE`` should be set to ``true`` if you use port 465 and to ``false`` for other ports.

        .. note::

          If your password has special characters in it, you will need to put single quotes ( ``'`` and ``'``) around the password. Values without special characters do not need quotes around them.

        .. note::

          ``EMAIL_FROM`` is equivalent to ``email.serviceAccount`` in the json config. If you omit it, the default is ``no-reply@${YOUR_DOMAIN}``. You can specify a name that will be shown by email clients by using the following structure:

          .. code-block:: bash

            EMAIL_FROM=My Cool Server <no-reply@my-server.server>

     #. Discard all ``files/service/config.json.template`` customizations. Make sure you have correctly copied all of them into ``.env``. You may want to keep the copy on your local computer until you have verified that everything works.

        .. code-block:: bash

          $ git checkout -- files/service/config.json.template

   .. dropdown:: ``docker-compose.yml``
     :icon: file-code

     #. Make a backup copy of the file. You will manually copy differences to your local computer later so this is for additional protection:

        .. code-block:: bash

          $ cp docker-compose.yml docker-compose.yml.bak

     #. Copy changes to your local computer:

        .. code-block:: bash

          $ git diff docker-compose.yml

        You will see additions in green with ``+`` prefixes.

        You can ignore any changes related to a custom database because those have been addressed by migrating ``files/service/config.json.template``.

        Copy any other changes to a scratch file on your local computer (e.g. using CTRL+C and CTRL+V). You will use this to copy your custom values into the new format.

     #. If you specify a value for ``SERVICE_NODE_OPTIONS``, open the ``.env`` file for editing:

        .. code-block:: bash

          $ nano .env

        Copy that to the ``.env`` file in the following format:

        .. code-block:: bash

          SERVICE_NODE_OPTIONS=my-node-options

     #. If you specify any other customizations in your ``docker-compose.yml`` file, this is considered advanced and you will need to apply them manually after the upgrade. If you're not sure how to do this, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.

     #. Discard all ``docker-compose.yml`` customizations. Make sure you have correctly copied all of them into ``.env``. You may want to keep the copy on your local computer until you have verified that everything works.

        .. code-block:: bash

          $ git checkout -- docker-compose.yml

   .. dropdown:: ``files/enketo/config.json.template`` or any others
     :icon: file-code

     #. Stash changes so they can be applied after the upgrade. These are considered advanced customizations and you may need to resolve merge conflicts when you re-apply them.

        .. code-block:: bash

          $ git stash


#. **Determine whether the server you are upgrading is using a custom database** (e.g. externally hosted on Azure, AWS, etc.) or the default one:

   .. code-block:: bash

     grep DB_HOST .env

   If you get nothing back or there's nothing after the ``=``, you are using the default database. If ``DB_HOST`` is set to any value, you are using a custom database server.

#. **Upgrade your database** according to your database type.

   .. tabs::
   
     .. tab:: Default database
       .. warning::
         Before starting, read the instructions at the top of this section carefully and **make sure you are actually using the default database configuration**. Following these instructions with a custom database setup could result in perceived data loss.
   
       #. **Get the latest infrastructure version.**
   
          .. code-block:: bash
   
             $ git pull
   
       #. **Get the latest client and server.**
   
          .. code-block:: bash
   
             $ git submodule update -i
   
       #. **Check that you have enough disk space available.** If you are prompted for a password, enter the system superuser password (not a Central password). You will see a message about how much space is required and if you have enough free space to proceed.
   
          .. code-block:: bash
   
             $ sudo ./files/postgres14/upgrade/check-available-space
   
          *If you don't have enough space,* **stop here** and resume when you have increased the disk space available. You may achieve this by clearing out data you don't need (e.g., logs) or by    increasing the total disk space available.
   
       #. **Create a file to prove that you're carefully reading these instructions.** This is required to continue.
   
          .. code-block:: bash
   
             $ touch ./files/allow-postgres14-upgrade
   
       #. **Reapply any advanced customizations**. If you had made notes on advanced configurations and/or stashed some edited files, reapply those advanced customizations now:

          .. code-block:: bash

             $ git stash pop

       #. **Build from the latest code you just fetched.**
   
          .. code-block:: bash
   
             $ docker compose pull
             $ docker compose build --pull
   
       #. **Start the database upgrade and wait for the process to exit.** This is where the new PostgreSQL 14 database is made and data copied into it. This will take a long time if you have a lot of data and/or a slow server.
   
          .. code-block:: bash
   
             $ docker compose up postgres
   
       #. **Check the output of the previous command to see if there were any errors.** If there were any errors that you can't resolve, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.
   
       #. **Check the upgrade success file has been created.**
   
          .. code-block:: bash
   
             $ ls ./files/postgres14/upgrade/upgrade-successful
   
          If you see "No such file or directory," try doing ``docker compose up postgres`` again. If the file has still not been created, `write a support post on the forum <https://forum.getodk.org/c/support/6>`_.
   
       #. **Restart the server.**
   
          .. code-block:: bash
   
               $ docker compose up -d
   
       #. **Log into the web interface and do some quick spot checks.** For example, verify that submission counts and latest submission dates look right and try a data export.
   
       #. **Clean up**
   
          #. **Remove unused Docker images**.

             .. code-block:: bash

                 $ docker image prune

             You'll be asked to confirm the removal of all dangling images. Agree by typing ``y`` and pressing Enter.

          #. **See how much space the old database takes**. The upgrade process performs a copy and leaves the old database intact.

             .. code-block:: bash

                  $ docker compose up postgres

          #. **Delete the old data**. Make sure you have verified that the server works as expected first.

             .. code-block:: bash
   
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
   
          .. code-block:: bash
   
            $ docker compose stop
   
       #. **Upgrade your database server**. We recommend using the latest point release of PostgreSQL 14 that is available.

       #. **Regenerate optimizer statistics**. You need to regenerate all database statistics to avoid performance issues. Run the following SQL command inside your database.
   
          .. code-block:: postgresql
   
            ANALYZE VERBOSE;

       #. **Create a file to prove that you're carefully reading these instructions.** This is required to continue.
   
          .. code-block:: bash
   
            $ touch ./files/allow-postgres14-upgrade
   
       #. Follow the :ref:`standard upgrade instructions <central-upgrade-steps>`.

.. _central-upgrade-2023.1:

Upgrading to Central v2023.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several time-consuming steps in this upgrade. Central will not be accessible during those steps. Plan for a minimum of an hour of downtime.

If you have 30K or more submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

If you have 20K or more versions of a single form (generally generated by an automated script that uses the API to update a form attachment), email support@getodk.org with details about your infrastructure and the number of form versions you have **before starting the upgrade process** so we can help you plan for a successful upgrade.

.. _central-upgrade-2022.3:

Upgrading to Central v2022.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v2022.3, we added Content Security Policy reporting. If you have disabled or customized Sentry, then you will need to modify ``files/nginx/odk.conf.template``. See our documentation about :ref:`configuring Sentry <central-install-digital-ocean-sentry>` to learn more about the specific changes that you need to make.

.. _central-upgrade-1.5:

Upgrading to Central v1.5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v1.5.3, we updated Central's Sentry configuration to match a change to the Sentry API. If you have not changed your :ref:`Sentry configuration <central-install-digital-ocean-sentry>`, then you do not need to do anything special.

If you have changed your Sentry configuration, that means that you have modified ``files/service/config.json.template``. If you run the ``git pull`` command, then you will see an error message like the following:

.. code-block:: bash

 error: Your local changes to the following files would be overwritten by merge:
         files/service/config.json.template
 Please commit your changes or stash them before you merge.

Don't worry, nothing bad happens if you see this. To get around this error, run this set of commands instead of ``git pull``:

.. code-block:: bash

 mv files/service/config.json.template config-tmp
 git pull
 mv config-tmp files/service/config.json.template

If you see an error message when you run this set of commands, copy and paste your entire console session into a `forum thread <https://forum.getodk.org/c/support/6>`_ and someone will help you out.

If you are using your own Sentry instance, then you must complete one additional step. You will need to modify ``files/service/config.json.template``. Below the line that contains ``"sentry": {``, insert a new line that looks like this:

.. code-block:: bash

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

.. code-block:: bash

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

.. _central-upgrade-1.2:

Upgrading to Central v1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In v1.2, we added some advanced features to Central's server configuration. These features will not be meaningful to most users. However, because we would like to make this change and further improvements in the future, we have modified the template ``.env`` configuration file you set up during installation.

Since you have made your own changes to the ``.env`` file to set Central up for your environment, you will see an error message when you run the ``git pull`` command:

.. code-block:: bash

 error: Your local changes to the following files would be overwritten by merge:
         .env
 Please commit your changes or stash them before you merge.

Don't worry, nothing bad happens if you see this. To get around this error, run this set of commands instead of ``git pull``:

.. code-block:: bash

 mv .env env-tmp
 git pull
 mv env-tmp .env

Afterwards, ``git status`` should not say anything about the ``.env`` file at all and you can continue with the upgrade instructions above. 

If ``git status`` still shows errors, copy and paste your entire console session into a `forum thread <https://forum.getodk.org/c/support/6>`_ and someone will help you out.

.. _central-upgrade-0.9:

Upgrading to Central v0.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to disable the system firewall for web form features to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If you do, the firewall is configured correctly.

.. note::

  While it sounds dangerous, disabling your firewall does not put your server at greater risk. In fact, most Linux operating systems come with the firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. To verify that this is the case, try to ``curl`` your Central website over HTTPS on its public domain name from within one of the containers.

