.. _central-install-digital-ocean:

Installing Central on DigitalOcean
===================================

If you'd like to set up an ODK server that's accessible from anywhere via the Internet, DigitalOcean provides a one-click configuration that's nicely geared with nearly all the tools you'll need to set up your new server. The only thing it doesn't do is register a domain name, which you will have to do in order to obtain a security certificate for your server.

.. tip::
  If you have not already created a DigitalOcean account, use `our referral link <https://m.do.co/c/39937689124c>`_.

  DigitalOcean will give you $100 of credit to spend during the first 60 days so that you can try things out. Once you have spent $25 with them, we’ll get $25 to put towards our hosting costs.

In general, this installation process will involve five phases:

#. Getting a server and loading it with the appropriate base system.
#. Getting a web address (domain name) and pointing it at your new server.
#. Getting the Central software and installing it on your server.
#. Preparing Central for startup and running it for the first time.
#. Creating your first Central Administrator account and logging into it.

There are also some optional other steps you can take, which you can find at the bottom of this page.

.. _central-install-digital-ocean-server:

Getting a Server
------------------

In this phase, you will create a new server on DigitalOcean, choose a pricing tier, configure it with the correct base operating system, and start it up.

If you haven't already, create an account on `DigitalOcean <https://m.do.co/c/39937689124c>`_. Then, from the DigitalOcean control panel, use the **Create** button at the top to create a new Droplet. This is their name for a server you can access and manage.

   .. image:: /img/central-install/create-droplet.png

At the very top, under **Choose an image**, switch to the **Marketplace** tab and select the **Docker** option. The version does not matter.

   .. image:: /img/central-install/docker-app.png

As you continue down this page, there are a few options that may be important to you:

- There is a section for standard droplets and another for more expensive optimized droplets. In general, you should not need optimized droplets.
- The **size** option affects a few things, but the most important is the amount of memory available to your server. Memory does not affect storage space, it sets the amount of "thinking room" the server gets while it's working on things. If you don't expect many forms to be submitted at once and you don't expect many large media attachments, you can start with 1GB. Higher-load servers and servers which handle many image or video attachments may need 2GB or more. It is pretty easy to upgrade to a larger size later.

  .. tip::

    If you choose a 1GB server we strongly recommend you :ref:`add swap <central-install-digital-ocean-swap>`.

- The datacenter region selects where physically your server will be located. If you have security concerns, this is your chance to decide which country hosts your data. Otherwise, generally selecting the option with closest geographic proximity to your users is a good idea.
- If you are technically savvy and understand what an SSH key is, there is a field here that you will want to fill in. If not, don't worry about it.


Once you click on **Create**, you'll be taken back to the Droplet management page. It may think for a moment, and then your new server should appear. Next to it will be an IP address, which should look something like ``183.47.101.24``. This is where your server is publicly located on the Internet. Don't worry, nobody can do anything with it until you let them.

**Congratulations**! With those steps, you have now created a new server which you can access over the Internet, and started it up. Next, we will get a web domain name address (like ``getodk.org``) to point at it.

.. _central-install-digital-ocean-domain:

Getting a Web Address (Domain Name)
-------------------------------------

Now is the time to set up a domain name. We will do so, and then configure it so that it sends users to the server you created in the previous step.

You'll need to do this for two reasons: a memorable name (like ``google.com``) will be easier to remember and access than a pile of numbers, and you cannot get a security certificate without one. It is not currently possible to host Central within a subdirectory on another domain (so, ``my-website.com/my-odk-server`` is not possible, but ``my-odk-server.com`` is allowed, as is ``my-odk-server.my-website.com``).

If you already know how to do these sorts of things, feel free to ignore the following instructions and proceed on your own. You can rejoin us at the next section.

For the rest of us, there are some options here:

- You can pay one of the many popular commercial domain registrars for a full domain name, like ``MyOdkCentralServer.com``. Search for "domain registrar" to find one of these. These often cost as little as $3/year.
- You can use a free DNS service: we recommend `FreeDNS <https://freedns.afraid.org/>`_, which has run for a long time and has a good reputation. With it, you can get a free name, albeit with a fixed second half (like ``MyOdkCentralServer.dynet.com``). If you choose this route, we recommend using one of the *less popular* names, as the heavily occupied names can run into trouble later on (in particular, getting a security certificate from Let's Encrypt).

Whichever option you choose, once you get a domain name you'll want to look at `DigitalOcean's guide <https://www.digitalocean.com/docs/networking/dns>`_ on setting up domain names for your Droplet. In general, you'll point your domain name in DigitalOcean's direction at your registrar, then in DigitalOcean itself you'll want to create an A record that points to the IP address we found above.

New domain names take a little bit to get working. Meanwhile, we can get working on installing the server software.

.. _central-install-digital-ocean-build:

Installing Central
------------------

In this phase of installation, we will log into your new server, get the Central software, load some settings into it, and install it.

First, you'll need to be able to log into the server itself. If you are an advanced user who filled in an SSH key above, you're good to go. Otherwise, click your email for a message from DigitalOcean with your server password.

Once you have that password in hand, you'll be able to use the **Launch Console** button to log into your server: when it asks for ``login``, type ``root`` and press **Enter**. Then type the password you were emailed and press **Enter** again.

   .. image:: /img/central-install/access-page.png

Once you are in your server, you'll want to change your password so that people snooping your email do not gain access. You should be automatically asked for a new password the first time you log in. If you are not, type ``passwd`` and press **Enter**, then follow the instructions to choose a new password. From now on, you will use that password to log in.

Changing Server Settings
~~~~~~~~~~~~~~~~~~~~~~~~

#. Make sure you are running Docker Engine v23.x and Docker Compose v2.16.x or greater.

.. code-block:: console

  $ docker --version && docker compose version

If you are using old versions, follow the instructions to install `Docker Engine <https://docs.docker.com/engine/install/ubuntu>`_ (not Desktop) for Ubuntu, the operating system we recommend and support. The instructions will help you setup the Docker ``apt`` repository and install the latest version of Docker Engine and Docker Compose.

#. Modify the system firewall for web form features in Central to work correctly (using Enketo).

.. code-block:: console

  $ ufw disable

You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  While it sounds dangerous, disabling your system firewall does not put your server at greater risk. In fact, most Linux operating systems come with the system firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your Central website over HTTPS on its public domain name, all Enketo features should work correctly.

Getting and Setting Up Central
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the software. In the server window, type:

   .. code-block:: console

     $ git clone https://github.com/getodk/central

   and press **Enter**. It should think for some time and download many things.

#. Go into the new central folder:

   .. code-block:: console

     $ cd central

#. Get the latest client and server:

   .. code-block:: console

     $ git submodule update -i

#. Update settings. First, copy the settings template file so you can edit it:

   .. code-block:: console

     $ cp .env.template .env

#. Launch the ``nano`` text editing application and specify required settings:

   .. code-block:: console

     $ nano .env

   - Change the ``DOMAIN`` line so that after the ``=`` is the domain name you registered above. As an example: ``DOMAIN=MyOdkCentralServer.com``. Do not include ``http://`` or ``https://`` in the domain.
   - Change the ``SYSADMIN_EMAIL`` line so that after the ``=`` is your own email address. The Let's Encrypt service will use this address only to notify you if something is wrong with your security certificate.
   - Leave the rest of the settings alone. If you have a custom security or network environment you are trying to integrate Central into, see the :ref:`advanced configuration <central-install-digital-ocean-advanced>` sections for more information on these options.
   - Hold ``Ctrl`` and press ``x`` to quit the text editor. Press ``y`` to indicate that you want to save the file, and then press **Enter** to confirm the file name. Do not change the file name.

     .. image:: /img/central-install/nano.png

#. Let the system know that you want the latest version of the database:

   .. code-block:: console

     $ touch ./files/allow-postgres14-upgrade

   This is mostly useful for *upgrades* but is also currently necessary for fresh installs.

#. Bundle everything together into a server. This will take a long time and generate quite a lot of text output. Don't worry if it seems to pause without saying anything for a while.

   .. code-block:: console

     $ docker compose build

   When it finishes, you should see some "Successfully built" type text and get your input prompt back.

**Congratulations**! You have installed your copy of Central. Next, we need to teach the server how to start it up, and do so.

.. _central-install-digital-ocean-startup:

Starting up Central
-------------------

#. Start the server software. The first time you start it, it will take a while to set itself up.

   .. code-block:: console

     $ docker compose up -d

#. See whether ODK has finished loading.

   .. code-block:: console

     $ docker compose ps

   Under the ``Status`` column, for the ``central-nginx-1`` row, you will want to see text that reads ``Up`` or ``Up (healthy)``. If you see ``Up (health: starting)``, give it a few minutes. If you see some other text, something has gone wrong.

#. Visit your domain name in a web browser. If it's not accessible yet, you should continue waiting. Once it is accessible, check that you get the Central website.

**You're almost done**! All you have to do is create an Administrator account so that you can log into Central.

.. _central-install-digital-ocean-account:

Logging into Central
--------------------

If visiting your server domain name address in your browser does not load the Central website, you may have to wait a few minutes or hours (possibly even a day) for the domain name itself to get working. These instructions are explained in further depth on the page detailing the :doc:`central-command-line`.

Once you do see it working, you'll want to set up your first Administrator account. To do this:

#. Ensure that you are in the ``central`` folder on your server. If you have not closed your console session from earlier, you should be fine. If you have just logged back into it:

   .. code-block:: console

     $ cd central

#. Create a new account. Make sure to substitute the email address that you want to use for this account.

   .. code-block:: console

     $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-create

   Press **Enter**, and you will be asked for a password for this new account.

#. Make the new account an administrator.

   .. code-block:: console

     $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-promote

#. Log into the Central website. Go to your domain name and enter in your new credentials. Once you have one administrator account, you do not have to go through this process again for future accounts: you can log into the website with your new account, and directly create new users that way.

.. tip::
  If you find that users are not receiving emails, read about :ref:`troubleshooting emails <troubleshooting-emails>`.

  If you ever lose track of your password, you can reset it with

  .. code-block:: console

    $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-set-password

.. _central-install-digital-ocean-backups:

Setting Up Backups
------------------

The next step is setting up automated system backups. We strongly recommend you have backups because they provide a safety net if something goes wrong.

You can find instructions for setting up backups in `DigitalOcean's backups guide <https://docs.digitalocean.com/products/images/backups/quickstart/>`_.

Note that Central has its own :ref:`backups <central-backup>` system that you can configure in addition to full system backups. Central's built-in backups are particularly helpful if you wish to backup your data via API.

.. _central-install-digital-ocean-monitoring:

Setting Up Monitoring
---------------------

The last thing you will want to do is to set up server monitoring. Alerts and monitoring are important because they can inform you of problems with your server before they affect your data collection project.

You can find instructions for setting up alerts in the `DigitalOcean's monitoring guide <https://docs.digitalocean.com/products/monitoring/quickstart/>`_.

We strongly recommend creating an alert for Disk Utilization. A threshold of 90% is usually reasonable. By far the most common operations issue we see is servers running out of disk space as large media attachments pile up. If your server runs entirely out of disk space, it can crash and become unresponsive. It is best to upgrade your storage plan before this happens.

If you are familiar with server operations, you may wish to set up some other alerts: CPU usage and Memory Utilization are the most interesting remaining metrics. However, these are not as important or easily understandable as the Disk Utilization alert, so you may skip this if you're not sure what to do here.

You're done! Congratulations. In the future, you may wish to consult the :doc:`central-upgrade` guide, but for now you may begin using Central. The :doc:`central-using` sections can help you with your next steps if you aren't sure how to proceed.

.. _central-install-digital-ocean-advanced:

Advanced Configuration Options
==============================

The following sections each detail a particular customization you can make to your server setup. Most installations should not need to perform these tasks, and some of them assume some advanced working knowledge on administering Linux web servers. If you aren't sure what something means, the best option is probably to skip the section completely.

.. _central-install-digital-ocean-swap:

Adding Swap
-----------

.. tip::
 We recommend :ref:`monitoring memory usage <central-install-digital-ocean-monitoring>` to see how much memory your server is using.

If you are having issues with Central running out of memory, we strongly recommend `adding physical memory <https://www.digitalocean.com/docs/droplets/how-to/resize/>`_. If you cannot add physical memory, adding swap can be an effective workaround against temporary memory spikes.

#. To add 2GB swap, log into your server's console and run these commands.

   .. code-block:: console
   
     $ fallocate -l 2G /swap
     $ dd if=/dev/zero of=/swap bs=1k count=2048k
     $ chmod 600 /swap
     $ mkswap /swap
     $ swapon /swap

#. Make sure swap is only used when the server is almost out of memory.

   .. code-block:: console

     $ sysctl -w vm.swappiness=10

#. Edit ``/etc/sysctl.conf`` and add the following to the end of the file to ensure that change is permanently available.

   .. code-block:: console

     $ nano /etc/sysctl.conf

   .. code-block:: bash

     vm.swappiness=10

#. Edit ``/etc/fstab`` and add the following to the end of the file to ensure that the swap file is permanently available.

   .. code-block:: console
  
     $ nano /etc/fstab
  
   .. code-block:: bash
  
    /swap swap swap defaults 0 0

.. _central-install-digital-ocean-external-storage:

Adding External Storage
-----------------------

Forms with many large media attachments can fill up your droplet's storage space. To move your Central install to external storage, follow these steps:

#. `Add a new volume <https://www.digitalocean.com/docs/volumes/quickstart/>`_ to your droplet.

#. Find the location of your new volume. It will look like ``/mnt/your-volume-name``. 

   .. code-block:: console

     $ df -h | grep /mnt/


#. Create a ``docker`` folder at that location.

   .. code-block:: console
  
     $ sudo mkdir /mnt/your-volume-name/docker

#. `Move the Docker data directory <https://blog.adriel.co.nz/2018/01/25/change-docker-data-directory-in-debian-jessie/>`_ to the new volume. Use ``/mnt/your-volume-name/docker`` as the ``data-root`` path.

.. _central-install-custom-memory:

Increasing Memory Allocation
-----------------------------

During upgrades or exports, some versions of Central may use more memory than the 2GB typically available to the Central service. If you run into this problem, increase the memory allocated to the Central service.

#. Ensure you have more than 2GB of physical memory in your server. If you have less, `add more physical memory <https://www.digitalocean.com/docs/droplets/how-to/resize/>`_.

   .. tip::
     If you can't add more physical memory, :ref:`add swap <central-install-digital-ocean-swap>`. This will result in slower performance than adding physical memory but can be acceptable if it is only needed for occasional exports or upgrades.

#. Edit ``.env`` to add a ``SERVICE_NODE_OPTIONS`` variable with a ``--max_old_space_size`` flag set to your desired maximum memory in MB.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano .env

   .. code-block:: bash

     SERVICE_NODE_OPTIONS='--max_old_space_size=3072'

   .. note::

     Choose a memory size that leaves enough memory for your server's operating system and any other applications. 3072MB is a good starting point for a machine with 4GB of RAM.

#. Build and restart the service container.

   .. code-block:: console

     $ docker compose build service && docker compose up -d service

If an upgrade was the cause of the memory error, you may revert these changes after the upgrade and build and restart the service container.

.. _central-install-digital-ocean-custom-ssl:

Using a Custom SSL Certificate
------------------------------

Central uses Let's Encrypt SSL certificates to secure all communication. To use your own certs:

#. Generate a ``fullchain.pem`` (``-out``) file which contains your certificate followed by any necessary intermediate certificate(s).
#. Generate a ``privkey.pem`` (``-keyout``) file which contains the private key used to sign your certificate.
#. Copy those files into ``files/local/customssl/``.

   .. code-block:: console

     $ cp fullchain.pem central/files/local/customssl/
     $ cp privkey.pem central/files/local/customssl/

#. In ``.env``, set ``SSL_TYPE`` to ``customssl`` and set ``DOMAIN`` to the domain name you registered. 

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano .env

   .. code-block:: bash

     DOMAIN=MyOdkCentralServer.com
     SSL_TYPE=customssl

   .. note::

     Do not include ``http://`` or ``https://`` in the domain.

#. Build and restart the nginx container.

   .. code-block:: console

     $ docker compose build nginx && docker compose up -d nginx

.. _central-install-digital-ocean-custom-mail:

Using a Custom Mail Server
--------------------------

Central comes with an mail server to send password reset emails. To use your own mail server:

#. Edit ``.env`` with your mail server host, port, and authentication details.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano .env

   .. code-block:: bash

     EMAIL_HOST=my-email-host
     EMAIL_PORT=my-email-port
     EMAIL_IGNORE_TLS=true-or-false
     EMAIL_SECURE=true-or-false
     EMAIL_USER=my-email-user
     EMAIL_PASSWORD=my-email-password

   .. note::

     ``EMAIL_IGNORE_TLS`` should generally be set to ``false``. ``EMAIL_SECURE`` should generally be set to ``true`` if you use port 465 and set to ``false`` for other ports.

     ``EMAIL_USER`` and ``EMAIL_PASSWORD`` are both required.

#. Build and restart the service container.

   .. code-block:: console

     $ docker compose build service && docker compose up -d service

.. _central-install-digital-ocean-custom-db:

Using a Custom Database Server
------------------------------

.. warning::
  Using PostgreSQL 14 isn't strictly required, but we only test with and support PostgreSQL 14.

  Using a custom database server that is not on your local network, may result in poor performance.

Central comes with a PostgreSQL v14.x database server to store your data. To use your own PostgreSQL database server:

#. Connect to your database server.

   .. code-block:: console

     $ psql -h mydbhost -p 5432 -U mydbadmin

#. Ensure your database server uses the ``UTF8`` encoding.

   .. code-block:: postgres

      SHOW SERVER_ENCODING;

#. Create the database user and database.

   .. code-block:: postgres

      CREATE USER mydbuser WITH PASSWORD 'mydbpassword';
      CREATE DATABASE mydbname WITH OWNER=mydbuser ENCODING=UTF8;

#. Ensure ``CITEXT`` and ``pg_trgm`` extensions exist on `mydbname`.

   .. code-block:: postgres

      CREATE EXTENSION IF NOT EXISTS CITEXT;
      CREATE EXTENSION IF NOT EXISTS pg_trgm;

#. Edit ``.env`` with your database server host, database name, and authentication details.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano .env

   .. code-block:: bash

     DB_HOST=my-db-host
     DB_USER=my-db-user
     DB_PASSWORD=my-db-password
     DB_NAME=my-db-name

#. Build and restart the service container.

   .. code-block:: console

     $ docker compose build service && docker compose up -d service

.. _central-install-digital-ocean-dkim:

Configuring DKIM
----------------

.. tip::
  Users are not receiving emails? Read :ref:`troubleshooting emails <troubleshooting-emails>` before configuring DKIM.

DKIM is a protocol which is used to help verify mail server identities. Without it, your sent mail is likely to be flagged as spam. If you intend to use a :ref:`custom mail server <central-install-digital-ocean-custom-mail>`, these instructions will not be relevant to you.

#. Ensure that your server's name in DigitalOcean `matches your full domain name <https://www.digitalocean.com/community/questions/how-do-i-setup-a-ptr-record?comment=30810>`_, and that the `hostname does as well <https://askubuntu.com/questions/938786/how-to-permanently-change-host-name/938791#938791>`_. If you had to make changes for this step, restart the server to ensure they take effect.

#. Generate a public and private key.

   .. code-block:: console

     $ cd central

     $ openssl genrsa -out files/mail/rsa.private 1024
     $ openssl rsa -in files/mail/rsa.private -out files/mail/rsa.public -pubout -outform PEM

#. Ensure any changes to DKIM private key are kept private

   .. code-block:: console

     $ git update-index --skip-worktree files/mail/rsa.private

#. Copy the contents of the public key with the boundary dashes removed.

   .. code-block:: console

     $ cat files/mail/rsa.public | grep -v "^-"

#. Create four new DNS records in these locations:

   1. ``dkim._domainkey.DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content. Be sure to remove any newlines or line breaks.

      .. code-block:: console

        k=rsa; p=PUBLIC-KEY-HERE

   2. ``_dmarc.DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content.

      .. code-block:: console

        v=DMARC1; p=none
   
   3. ``DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content. Get the server IP address from the DigitalOcean control panel. 

      .. code-block:: console

        v=spf1 a mx ip4:SERVER-IP-ADDRESS-HERE -all

   4. ``DOMAIN-NAME-HERE``: create a ``MX`` record with the following content.

      .. code-block:: console

        10 DOMAIN-NAME-HERE

#. Build, stop, and start the mail container.

   .. code-block:: console

     $ docker compose build mail && docker compose stop mail && docker compose up -d mail

.. _central-install-digital-ocean-enketo:

Customizing Enketo
------------------

.. warning::
  Customizing Enketo may break Central in subtle and unexpected ways. Do not make changes if you do not understand the implications of those changes.

Enketo is the software that Central uses to render forms in a web browser. It is used for form previews, web browser submission, and submission editing. Common customizations include enabling geocoding, adding analytics, and setting a default theme.

#. Read the Enketo `configuration tutorial <https://enketo.github.io/enketo-express/tutorial-10-configure.html>`_ and `default-config.json <https://github.com/enketo/enketo-express/blob/master/config/default-config.json>`_ to understand what is possible.

#. Edit the file ``files/enketo/config.json.template`` with your desired changes.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano files/enketo/config.json.template

#. Build and restart all containers.

   .. code-block:: console

     $ docker compose build && docker compose up -d

.. _central-install-digital-ocean-sentry:

Disabling or Customizing Sentry
-------------------------------

By default, we enable `Sentry error logging <https://sentry.io>`_ in Central's service container, which provides the Central team with an anonymized log of unexpected errors that occur while your server is running. 

This information is only visible to the development team and should never contain any of your user or form data, but if you feel uncomfortable with this, you can disable Sentry:

#. Edit the file ``files/service/config.json.template`` and remove the ``sentry`` lines, starting with ``"sentry": {`` through the next three lines until you remove the matching ``}``.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano files/service/config.json.template

   .. code-block:: json

     "env": {
       "domain": "https://${DOMAIN}:${HTTPS_PORT}",
       "sysadminAccount": "${SYSADMIN_EMAIL}"
     },
     "external": {
     }

#. Edit the file ``files/nginx/odk.conf.template`` and replace the ``csp-report`` lines, starting with ``location /csp-report {`` through the next two lines until you remove the matching ``}`` with:

   .. code-block:: console

     $ nano files/service/config.json.template

   .. code-block:: bash

      location /csp-report {
        return 200 'CSP report discarded.';
        add_header Content-Type text/plain;
      }

#. Build and restart all containers.

   .. code-block:: console

     $ docker compose build && docker compose up -d

If you wish to use your own Sentry instance to receive your own errors, take these steps:

#. Create an account on `Sentry <https://sentry.io>`_, and create a new ``nodejs`` project.
#. The new project will generate a ``DSN`` in this format: ``https://SENTRY_KEY@SENTRY_ORG_SUBDOMAIN.ingest.sentry.io/SENTRY_PROJECT``.
#. In ``.env``, set ``SENTRY_SUBDOMAIN``, ``SENTRY_KEY`` and ``SENTRY_PROJECT`` to the values from step 2.

   .. code-block:: console

     $ cd central

   .. code-block:: console

     $ nano .env

   .. code-block:: bash

     SENTRY_ORG_SUBDOMAIN=
     SENTRY_KEY=
     SENTRY_PROJECT=

#. Build and restart all containers.

   .. code-block:: console

     $ docker compose build && docker compose up -d
