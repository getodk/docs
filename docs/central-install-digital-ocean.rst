.. _central-install-digital-ocean:

Installing Central on DigitalOcean
===================================

If you'd like to set up an ODK server that's accessible from anywhere via the Internet, DigitalOcean provides a one-click configuration that's nicely geared with nearly all the tools you'll need to set up your new server. The only thing it doesn't do is register a domain name, which you will have to do in order to obtain a security certificate for your server.

.. tip::
  If you have not already created a DigitalOcean account, use `our referral link <https://m.do.co/c/39937689124c>`_.

  DigitalOcean will give you $100 of credit to spend during the first 60 days so that you can try things out. Once you have spent $25 with them, we’ll get $25 to put towards our hosting costs.

In general, this installation process will involve five phases:

1. Getting a server and loading it with the appropriate base system.
2. Getting a web address (domain name) and pointing it at your new server.
3. Getting the Central software and installing it on your server.
4. Preparing Central for startup and running it for the first time.
5. Creating your first Central Administrator account and logging into it.

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
 - The datacenter region selects where physically your server will be located. If you have security concerns, this is your chance to decide which country hosts your data. Otherwise, generally selecting the option with closest geographic proximity to your users is a good idea.
 - If you are technically savvy and understand what an SSH key is, there is a field here that you will want to fill in. If not, don't worry about it.

.. tip::
  If you choose a 1GB server we strongly recommend you :ref:`add swap <central-install-digital-ocean-swap>`.

Once you click on **Create**, you'll be taken back to the Droplet management page. It may think for a moment, and then your new server should appear. Next to it will be an IP address, which should look something like ``183.47.101.24``. This is where your server is publicly located on the Internet. Don't worry, nobody can do anything with it until you let them.

Congratulations! With those steps, you have now created a new server which you can access over the Internet, and started it up. Next, we will get a web domain name address (like ``getodk.org``) to point at it.

.. _central-install-digital-ocean-domain:

Getting a Web Address (Domain Name)
-------------------------------------

Now is the time to set up a domain name. We will do so, and then configure it so that it sends users to the server you created in the previous step.

You'll need to do this for two reasons: a memorable name (like ``google.com``) will be easier to remember and access than a pile of numbers, and you cannot get a security certificate without one. It is not currently possible to host Central within a subdirectory on another domain (so, ``my-website.com/my-odk-server`` is not possible, but ``my-odk-server.com`` is allowed, as is ``my-odk-server.my-website.com``).

If you already know how to do these sorts of things, feel free to ignore the following instructions and proceed on your own. You can rejoin us at the next section.

For the rest of us, there are some options here:

 - You can pay one of the many popular commercial domain registrars for a full domain name, like ``MyOdkCollectionServer.com``. Search for "domain registrar" to find one of these. These often cost as little as $3/year.
 - You can use a free DNS service: we recommend `FreeDNS <https://freedns.afraid.org/>`_, which has run for a long time and has a good reputation. With it, you can get a free name, albeit with a fixed second half (like ``MyOdkCollectionServer.dynet.com``). If you choose this route, we recommend using one of the *less popular* names, as the heavily occupied names can run into trouble later on (in particular, getting a security certificate from Let's Encrypt).

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

First, you'll need to upgrade to docker-compose v1.28.3 or later. Follow these commands from `Docker's documentation <https://docs.docker.com/compose/install/#install-compose-on-linux-systems>`_.

.. code-block:: console

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

Next, we will want to ensure that Docker starts up whenever the server starts. Docker will in turn ensure that Central has started up. To do this, run ``systemctl enable docker``.

You will need to change one more thing on this server before we proceed: you will need to modify the system firewall for Enketo features in Central to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  While it sounds dangerous, disabling your system firewall does not put your server at greater risk. In fact, most Linux operating systems come with the system firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be really difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your Central website over HTTPS on its public domain name, all Enketo features should work correctly.

Getting and Setting Up Central
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you'll need to download the software. In the server window, type ``git clone https://github.com/getodk/central`` and press **Enter**. It should think for some time and download many things. Then type ``cd central`` to start working with the software.

   .. image:: /img/central-install/cloned.png

You now have the framework of the server software, but some components are missing. Type ``git submodule update -i`` and press **Enter** to download them.

Next, you need to update some settings. First, copy the settings template file so you can edit it: type ``mv .env.template .env`` and press **Enter**.

Then, edit the file by typing ``nano .env`` and pressing **Enter**. This will launch a text editing application. 

 - Change the ``DOMAIN`` line so that after the ``=`` is the domain name you registered above. As an example: ``DOMAIN=MyOdkCollectionServer.com``. Do not include anything like ``http://``.
 - Change the ``SYSADMIN_EMAIL`` line so that after the ``=`` is your own email address. The Let's Encrypt service will use this address only to notify you if something is wrong with your security certificate.
 - Leave the rest of the settings alone. If you have a custom security or network environment you are trying to integrate Central into, see the :ref:`advanced configuration <central-install-digital-ocean-advanced>` sections for more information on these options.
 - Hold ``Ctrl`` and press ``x`` to quit the text editor. Press ``y`` to indicate that you want to save the file, and then press **Enter** to confirm the file name. Do not change the file name.

   .. image:: /img/central-install/nano.png

Now, we will bundle everything together into a server. Type ``docker-compose build`` and press **Enter** to do this. This will take a long time and generate quite a lot of text output. Don't worry if it seems to pause without saying anything for a while. When it finishes, you should see some "Successfully built" type text and get your input prompt back. When that happens, type ``docker-compose up --no-start`` and press **Enter**.

Once that is complete, congratulations! You have installed your copy of Central. Next, we need to teach the server how to start it up, and do so.

.. _central-install-digital-ocean-startup:

Starting up Central
-------------------

Now, run ``docker-compose up -d`` to start the server software. The first time you start it, it will take a while to set itself up. Once you give it a few minutes and you have input control again, you'll want to see whether everything is running correctly:

 - To see if ODK has finished loading, run ``docker-compose ps``. Under the ``State`` column, for the ``nginx`` row, you will want to see text that reads ``Up`` or ``Up (healthy)``. If you see ``Up (health: starting)``, give it a few minutes. If you see some other text, something has gone wrong. It is normal to see ``Exit 0`` for the ``secrets`` container.
 - If your domain name has started working, you can visit it in a web browser to check that you get the Central management website.

You're almost done! All you have to do is create an Administrator account so that you can log into Central.

.. _central-install-digital-ocean-account:

Logging into Central
--------------------

If visiting your server domain name address in your browser does not load the Central management website, you may have to wait a few minutes or hours (possibly even a day) for the domain name itself to get working. These instructions are explained in further depth on the page detailing the :doc:`central-command-line`.

Once you do see it working, you'll want to set up your first Administrator account. To do this:

 - Ensure that you are in the ``central`` folder on your server. If you have not closed your console session from earlier, you should be fine. If you have just logged back into it, you'll want to run ``cd central`` to navigate to that folder.
 - Then, type ``docker-compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-create``, substituting your email address as appropriate. Press **Enter**, and you will be asked for a password for this new account.
 - The previous step created an account but did not make it an administrator. To do this, type ``docker-compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-promote`` **Enter**.
 - You are done for now, but if you ever lose track of your password, you can always reset it by typing ``docker-compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-set-password``. As with account creation, you will be prompted for a new password after you press **Enter**.

Once you have one account, you do not have to go through this process again for future accounts: you can log into the website with your new account, and directly create new users that way.

.. tip::
  If you find that users are not receiving emails, read about :ref:`troubleshooting emails <troubleshooting-emails>`.

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

To avoid Central crashing if your server runs out of memory, you may want to add swap. If you are having issues with Central running out of memory, we recommend adding more physical memory. However, adding swap can be an effective temporary workaround or a preventative measure against spikes if, for example, multiple people initiate data exports at the same time.

Whether or not you choose to add swap, we recommend :ref:`monitoring memory usage <central-install-digital-ocean-monitoring>` and `adding memory <https://www.digitalocean.com/docs/droplets/how-to/resize/>`_ if your server is routinely running close to the physical memory limit.

To add swap, log into your server so you have a console prompt, and run these commands, adapted from `this article <https://help.ubuntu.com/community/SwapFaq#How_do_I_add_a_swap_file.3F>`_:

.. code-block:: console

 fallocate -l 1G /swap
 dd if=/dev/zero of=/swap bs=1k count=1024k
 chmod 600 /swap
 mkswap /swap
 swapon /swap

Run ``nano /etc/sysctl.conf`` and add the following to the end of the file to ensure that swap is only used when the droplet is almost out of memory.

.. code-block:: console

 vm.swappiness=10

Finally, run ``nano /etc/fstab`` and add the following to the end of the file to ensure that the swap file is permanently available.

.. code-block:: console

 /swap swap swap defaults 0 0

.. _central-install-digital-ocean-external-storage:

Adding External Storage
-----------------------

Forms with many large media attachments can fill up your droplet's storage space. To move your database to external storage, follow these steps:

1. `Add a new volume <https://www.digitalocean.com/docs/volumes/quickstart/>`_ to your droplet.

2. `Move the Docker data directory <https://www.guguweb.com/2019/02/07/how-to-move-docker-data-directory-to-another-location-on-ubuntu/>`_ to the new volume.

     1. To find the location of your new volume, run ``df -h``. The mount location will look like ``/mnt/volume_nyc1_01``. 
     2. Then create a ``docker`` folder at that location with ``sudo mkdir /mnt/volume_nyc1_01/docker``. 
     3. ``/mnt/volume_nyc1_01/docker`` will be the ``/path/to/your/docker`` you use.

.. _central-install-custom-memory:

Increasing Memory Allocation
-----------------------------

During upgrades or exports, some versions of Central may use more memory than the 2GB typically available to Central. If you run into this problem, increase the memory allocated to the Central service.

First, ensure you have more than 2GB of physical memory in your server. If you have less, instructions for increasing your physical memory on DigitalOcean can be found `in this support article <https://www.digitalocean.com/docs/droplets/how-to/resize/>`_.

If you can't increase physical memory, you can alternatively :ref:`add swap <central-install-digital-ocean-swap>`. This will result in slower performance than adding physical memory but can be acceptable if it is only needed for occasional exports or upgrades.

Then, in your ``docker-compose.yml`` file, add a ``NODE_OPTIONS`` variable with a ``--max_old_space_size`` flag set to the new value (e.g., 3.5GB or 3584 MB). Be sure to choose a value that leaves enough memory for your server's operating system and any other applications that may be running.

.. code-block:: console

  service:
    ...
    volumes:
      - secrets:/etc/secrets
      - /data/transfer:/data/transfer
    environment:
      - NODE_OPTIONS=--max_old_space_size=3584
      - DOMAIN=${DOMAIN}
      - SYSADMIN_EMAIL=${SYSADMIN_EMAIL}
    command: [ "./wait-for-it.sh", "postgres:5432", "--", "./start-odk.sh" ]

Now rebuild the service container with ``docker-compose build service``, ``docker-compose stop service``, ``docker-compose up -d service``.

If the cause of the memory error was a migration, you may remove these changes after the upgrade is complete and rebuild the container again.

.. _central-install-digital-ocean-custom-ssl:

Using a Custom SSL Certificate
------------------------------

By default, Central uses Let's Encrypt to obtain an SSL security certificate. For most users, this should work perfectly, but larger managed internal networks may have their own certificate trust infrastructure. To use your own custom SSL certificate rather than the automatic Let's Encrypt system:

1. Generate a ``fullchain.pem`` (``-out``) file which contains your certificate followed by any necessary intermediate certificate(s).
2. Generate a ``privkey.pem`` (``-keyout``) file which contains the private key used to sign your certificate.
3. Copy those files into ``files/local/customssl/`` within the repository root.
4. In ``.env``, set ``SSL_TYPE`` to ``customssl`` and set ``DOMAIN`` to the domain name you registered. As an example: ``DOMAIN=MyOdkCollectionServer.com``. Do not include anything like ``http://``.
5. Build and run: ``docker-compose build nginx``, ``docker-compose stop nginx``, ``docker-compose up -d nginx``. If that doesn't work, you may need to first remove your old nginx container (``docker-compose rm nginx``).

.. _central-install-digital-ocean-custom-mail:

Using a Custom Mail Server
--------------------------

Central ships with a basic EXIM server bundled to forward mail out to the internet. To use your own custom mail server:

1. Ensure you have an SMTP relay server visible to your Central server network host.
2. Edit the file ``files/service/config.json.template`` to reflect your network hostname, the TCP port, and authentication details. The ``secure`` flag is for TLS and should be set to ``true`` if the port is 465 and ``false`` for other ports. If no authentication is required, remove the ``auth`` section.

  .. code-block:: console

   "email": {
     "serviceAccount": "my-replyto-email",
     "transport": "smtp",
     "transportOpts": {
       "host": "smtp.example.com",
       "port": 587,
       "secure": false,
       "auth": {
         "user": "my-smtp-user",
         "pass": "my-smtp-password"
       }
     }
   }

3. Build and run: ``docker-compose build service``, ``docker-compose stop service``, ``docker-compose up -d service``.

.. _central-install-digital-ocean-custom-db:

Using a Custom Database Server
------------------------------

.. warning::
  Using a custom database server, especially one that is not local to your local network, may result in poor performance. We strongly recommend using the Postgres v14 server that is bundled with Central.

Central ships with a PostgreSQL database server. To use your own custom database server:

1. Ensure you have a PostgreSQL database server visible to your Central server network host.
2. Ensure your database has ``UTF8`` encoding by running the following command on the database.

  .. code-block:: console

    SHOW SERVER_ENCODING;

3. Ensure ``CITEXT`` and ``pg_trgm`` extensions exist by running the following commands on the database.

  .. code-block:: console

    CREATE EXTENSION IF NOT EXISTS CITEXT;
    CREATE EXTENSION IF NOT EXISTS pg_trgm;

4. Edit the file ``files/service/config.json.template`` to reflect your database host, table, and authentication details.

  .. code-block:: console

    "database": {
      "host": "my-db-host",
      "user": "my-db-user",
      "password": "my-db-password",
      "database": "my-db-table"
    },

4. Edit the file ``docker-compose.yml`` to update the command for the ``service`` container.

  .. code-block:: console

    command: [ "./wait-for-it.sh", "my-db-host:my-db-port", "--", "./start-odk.sh" ]

5. Build and run: ``docker-compose build service``, ``docker-compose stop service``, ``docker-compose up -d service``.

.. _central-install-digital-ocean-dkim:

Configuring DKIM
----------------

.. tip::
  Users are not receiving emails? Read :ref:`troubleshooting emails <troubleshooting-emails>` before configuring DKIM.

DKIM is a security trust protocol which is used to help verify mail server identities. Without it, your sent mail is likely to be flagged as spam. If you intend to use a custom mail server (see the following section), these instructions will not be relevant to you. Otherwise:

1. Ensure that your server's name in DigitalOcean `matches your full domain name <https://www.digitalocean.com/community/questions/how-do-i-setup-a-ptr-record?comment=30810>`_, and that the `hostname does as well <https://askubuntu.com/questions/938786/how-to-permanently-change-host-name/938791#938791>`_. If you had to make changes for this step, restart the server to ensure they take effect.
2. There can be in some cases a placeholder folder that you may have to delete first. If you run this command and no file was deleted, proceed to step 3.

   .. code-block:: console

     rmdir ~/central/files/dkim/rsa.private

3. Now, you'll need to generate a cryptographic keypair and enable the DKIM configuration. Run these commands:

   .. code-block:: console

     cd ~/central/files/dkim
     openssl genrsa -out rsa.private 1024
     openssl rsa -in rsa.private -out rsa.public -pubout -outform PEM
     cp config.disabled config

4. With the contents of the public key (``cat rsa.public``), you'll want to create two new TXT DNS records:

   1. At the location ``dkim._domainkey.YOUR-DOMAIN-NAME-HERE``, create a new ``TXT`` record with the contents ``k=rsa; p=PUBLIC-KEY-HERE``. You only want the messy text *between* the dashed boundaries, and you'll want to be sure to remove any line breaks in the public key text, so that it's all only letters, numbers, ``+``, and ``/``.
   2. At your domain name location, create a new ``TXT`` record with the contents ``v=spf1 a mx ip4:SERVER-IP-ADDRESS-HERE -all`` where you can obtain the server IP address from the DigitalOcean control panel.

5. Finally, build and run to configure EXIM to use the cryptographic keys you generated:

   .. code-block:: console

     cd ~/central
     docker-compose build mail
     docker-compose stop mail
     docker-compose up -d mail

   If you see an error that says ``Can't open "rsa.private" for writing, Is a directory.``, you will need to ``rmdir ~/central/files/dkim/rsa.private``, then attempt ``docker-compose build mail`` again. If you see some other error, you may need to first remove your old mail container (``docker-compose rm mail``).

.. _central-install-digital-ocean-enketo:

Customizing Enketo
------------------

.. warning::
  Changing Enketo's configuration may break Central in subtle and unexpected ways. Do not make changes if you do not understand the implications of those changes.

Enketo is the software that Central uses to render forms in a web browser. It is used for form previews, web browser submission, and submission editing. Common customizations include enabling geocoding, adding analytics, and setting a default theme.

1. Read the Enketo `configuration tutorial <https://enketo.github.io/enketo-express/tutorial-10-configure.html>`_ and `default-config.json <https://github.com/enketo/enketo-express/blob/master/config/default-config.json>`_ to understand what is possible.
2. Edit the file ``files/enketo/config.json.template`` to reflect your desired changes.
3. Build and run: ``docker-compose build``, ``docker-compose stop``, ``docker-compose up -d``.


.. _central-install-digital-ocean-sentry:

Disabling or Customizing Sentry
-------------------------------

By default, we enable `Sentry error logging <https://sentry.io>`_ in Central's service container, which provides the Central development team with an anonymized log of unexpected programming errors that occur while your server is running. This information is only visible to the development team and should never contain any of your user or form data, but if you feel uncomfortable with this anyway, you can take the following steps to disable Sentry:

1. Edit the file ``files/service/config.json.template`` and remove the ``sentry`` lines, starting with ``"sentry": {`` through the next three lines until you remove the matching ``}``.
2. Build and run: ``docker-compose build service``, ``docker-compose stop service``, ``docker-compose up -d service``.
3. Edit the file ``files/nginx/odk.conf.template`` and replace the ``csp-report`` lines, starting with ``location /csp-report {`` through the next two lines until you remove the matching ``}`` with:

  .. code-block:: console

    location /csp-report {
      return 200 'CSP report discarded.';
      add_header Content-Type text/plain;
    }

4. Build and run: ``docker-compose build nginx``, ``docker-compose stop nginx``, ``docker-compose up -d nginx``.

If on the other hand you wish to use your own Sentry instance, take these steps:

1. Create a free account on `Sentry <https://sentry.io>`_, and create a new ``nodejs`` project.
2. The new project will generate a ``DSN`` of the format ``https://SENTRY_KEY@SENTRY_SUBDOMAIN.ingest.sentry.io/SENTRY_PROJECT``.
3. In ``files/service/config.json.template``, replace ``SENTRY_SUBDOMAIN``, ``SENTRY_KEY`` and ``SENTRY_PROJECT`` with the values from step 2.

  .. code-block:: console

   {
     "default": {
       "database": {...},
       "email": {...},
       "env": {...},
       "external": {
         "sentry": {
           "orgSubdomain": "SENTRY_SUBDOMAIN",
           "key": "SENTRY_KEY",
           "project": "SENTRY_PROJECT"
         }
       }
     }
   }

The error logs sent to Sentry (if enabled) are also being written to ``/var/log/odk/stderr.log`` in the running service container.

4. In ``files/nginx/odk.conf.template``, replace ``https://o130137.ingest.sentry.io/api/1298632/security/?sentry_key=3cf75f54983e473da6bd07daddf0d2ee`` with your own Sentry ingest URL, which you can find in `Sentry's Content-Security-Policy documentation <https://docs.sentry.io/product/security-policy-reporting/#content-security-policy>`_.
