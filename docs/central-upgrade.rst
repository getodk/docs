.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. We recommend that you upgrade as soon as you can to get access to the newest features, bug fixes, and security updates. It is not possible to downgrade and we do not guarantee that versions prior to the latest release can still be installed.

Start by reviewing upgrade notes for all versions between your current version and the one you are upgrading to. You can skip upgrades and directly install the latest version as long as you make sure to follow all relevant upgrade instructions.

Upgrade notes
-------------

* :ref:`Central v2023.2 <central-upgrade-2023.2>`: plan ahead for even longer than usual downtime during upgrade
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

Upgrading to Central v2023.2
-----------------------------

.. warning::

  This upgrade is more complicated than normal.  Please :ref:`see the guide below for full instructions <central-upgrade-2023.2>`.

Upgrade steps (older versions)
------------------------------

.. warning::
  Before starting:

  #. :doc:`Back up your server <central-backup>`
  #. Make sure you have some time available in case something goes wrong (we recommend at least 2 hours). You may want to announce a maintenance window.
  #. Review upgrade notes for all versions between your current version and the version you are upgrading to.

#. Log into your server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>`, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

#. Get the latest infrastructure version.

.. code-block:: console

  cd central
  git pull

.. note::

  If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, run ``git pull`` and it will tell you.

3. Get the latest client and server.

  .. code-block:: console

    git submodule update -i

4. Build from the latest code you just fetched.

  .. code-block:: console

    docker-compose build

.. note::

  If you run into problems with this step, try stopping Central (``docker-compose stop``) and then retry ``docker-compose build``.

5. Perform maintenance

  .. code-block:: console

    docker prune

You'll be asked to confirm the removal of all dangling images. Agree by typing the letter ``y`` and pressing ``Enter``.

.. note::
  If it thinks ``prune`` is not a docker command, run ``docker image prune`` instead.

6. Restart the server

  .. code-block:: console

    docker-compose up -d

.. _central-upgrade-2023.2:

Upgrading to Central v2023.2
-----------------------------

.. warning::
  This upgrade may take more time and disk space than previous updates, as it includes upgrading the PostgreSQL database version.

.. warning::
  Before starting:

  #. :doc:`Back up your server <central-backup>`
  #. Make sure you have some time available in case something goes wrong (we recommend at least 2 hours). You may want to announce a maintenance window.
  #. Review upgrade notes for all versions between your current version and the version you are upgrading to.

#. Log into your server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>`, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

#. Get the latest infrastructure version.

.. code-block:: console

  cd central
  git pull

.. note::

  If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, run ``git pull`` and it will tell you.

3. Get the latest client and server.

  .. code-block:: console

    git submodule update -i

.. _central-upgrade-2023.1:

4. Check that you have enough disk space available.

  .. code-block:: console

    sudo ./files/check-available-space

5. Create a disclaimer file to prove that you're reading these instructions.

  .. code-block:: console

    touch allow-postgres14-upgrade

6. Stop ODK Central services.

  .. code-block:: console

    docker-compose stop

7. Build from the latest code you just fetched.

  .. code-block:: console

    docker-compose build

8. Start the database upgrade.

  .. code-block:: console

    docker-compose up postgres

9. Check the output of the previous command to see if there were any errors.

10. Check the upgrade success marker file has been created

  .. code-block:: console

    ls ./postgres14-upgrade/upgrade-completed-ok

11. Restart the server

  .. code-block:: console

    docker-compose up -d


Upgrading to Central v2023.1
-----------------------------

There are several time-consuming steps in this upgrade. Central will not be accessible during those steps. Plan for a minimum of an hour of downtime.

If you have 30k or more submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

If you have 20k or more versions of a single form (generally generated by an automated script that uses the API to update a form attachment), email support@getodk.org with details about your infrastructure and the number of form versions you have **before starting the upgrade process** so we can help you plan for a successful upgrade.

.. _central-upgrade-2022.3:

Upgrading to Central v2022.3
-----------------------------

In v2022.3, we added Content Security Policy reporting. If you have disabled or customized Sentry, then you will need to modify ``files/nginx/odk.conf.template``. See our documentation about :ref:`configuring Sentry <central-install-digital-ocean-sentry>` to learn more about the specific changes that you need to make.

.. _central-upgrade-1.5:

Upgrading to Central v1.5
----------------------------

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
--------------------------

There are several time-consuming migrations in v1.4. If you have tens of thousands of submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

.. _central-upgrade-1.3:

Upgrading to Central v1.3
--------------------------

Before upgrading, run ``docker-compose --version`` to confirm you have docker-compose v1.28.3 or later. If you don't, upgrade with these commands from `Docker's documentation <https://docs.docker.com/compose/install/#install-compose-on-linux-systems>`_.

.. code-block:: console

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

.. _central-upgrade-1.2:

Upgrading to Central v1.2
--------------------------

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
--------------------------

Particularly if you are installed on DigitalOcean, you will need to modify the system firewall for Enketo features in Central to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  While it sounds dangerous, disabling your system firewall does not put your server at greater risk. In fact, most Linux operating systems come with the system firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be really difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your Central website over HTTPS on its public domain name from within the Enketo container, all Enketo features should work correctly.


