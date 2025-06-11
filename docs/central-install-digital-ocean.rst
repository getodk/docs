.. spelling:word-list::
  Cloudflare

.. _central-install-digital-ocean:

Installing Central on DigitalOcean
===================================

.. tip::
  `ODK Cloud <https://getodk.org/#pricing>`_ is the best way to use ODK. With ODK Cloud, you can be collecting the data you need a few minutes after you subscribe. No technical skills required. `Get started today <https://getodk.org/#pricing>`_.

If you'd like to set up an ODK server that's accessible from anywhere via the Internet, DigitalOcean provides a one-click configuration that's nicely geared with nearly all the tools you'll need to set up your new server. The only thing it doesn't do is register a domain name, which you will have to do in order to obtain a security certificate for your server.

.. tip::
  If you have not already created a DigitalOcean account, use `our referral link <https://m.do.co/c/39937689124c>`_.

  DigitalOcean will give you $200 of credit to spend during the first 60 days so that you can try things out. Once you have spent $25 with them, we’ll get $25 to put towards our hosting costs.

  If you are a student, enroll via GitHub's `Student Developer Pack <https://education.github.com/pack?utm_source=github+digitalocean>`_  to get your DigitalOcean credit extended for 1 year.

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
- The **size** option affects a few things, but the most important is the amount of memory available to your server. Memory does not affect storage space, it sets the amount of "thinking room" the server gets while it's working on things. If you don't expect many forms to be submitted at once and you don't expect many large media attachments, you can start with 1 GB. Higher-load servers and servers which handle many image or video attachments may need 2 GB or more. It is pretty easy to upgrade to a larger size later.

  .. tip::

    If you choose a 1 GB server we strongly recommend you :ref:`add swap <central-install-digital-ocean-swap>`.

- The datacenter region selects where physically your server will be located. If you have security concerns, this is your chance to decide which country hosts your data. Otherwise, generally selecting the option with closest geographic proximity to your users is a good idea.
- If you are technically savvy and understand what an SSH key is, there is a field here that you will want to fill in. If not, don't worry about it.

Once you click on **Create**, you'll be taken back to the Droplet management page. It may think for a moment, and then your new server should appear. Next to it will be an IP address, which should look something like ``183.47.101.24``. This is where your server is publicly located on the Internet. Don't worry, nobody can do anything with it until you let them.

**Congratulations**! With those steps, you have now created a new server which you can access over the Internet, and started it up. Next, we will get a web domain name address (like ``getodk.org``) to point at it.

.. _central-install-digital-ocean-domain:

Getting a Web Address (Domain Name)
-------------------------------------

.. note::
  To self-host Central, you must have a domain name (e.g., `central.example.com`) mapped to your server. For security reasons, Central will not work with just an IP address (e.g., `93.184.216.34`).

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

Getting and Setting Up Central
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Make sure you are running Docker Engine v23.x and Docker Compose v2.16.x or greater.

   .. code-block:: bash

    $ docker --version && docker compose version

   If you are using old versions, follow the instructions to install `Docker Engine <https://docs.docker.com/engine/install/ubuntu>`_ (not Desktop) for Ubuntu, the operating system we recommend and support. The instructions will help you setup the Docker ``apt`` repository and install the latest version of Docker Engine and Docker Compose.

#. Disable the system firewall for web form features to work correctly.

   .. code-block:: bash

    $ ufw disable

   You should see the message ``Firewall stopped and disabled on system startup``. If you do, the firewall is configured correctly.

   .. note::

    While it sounds dangerous, disabling your firewall does not put your server at greater risk. In fact, most Linux operating systems come with the firewall disabled.

    If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

    The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. To verify that this is the case, try to ``curl`` your Central website over HTTPS on its public domain name from within one of the containers.

#. Download the software. In the server window, type:

   .. code-block:: bash

     $ umask 022; git clone https://github.com/getodk/central

   and press **Enter**. It should think for some time and download many things.

#. Go into the new central folder:

   .. code-block:: bash

     $ cd central

#. Get the latest client and server:

   .. code-block:: bash

     $ git submodule update -i

#. Update settings. First, copy the settings template file so you can edit it:

   .. code-block:: bash

     $ cp .env.template .env

#. Launch the ``nano`` text editing application and specify required settings:

   .. code-block:: bash

     $ nano .env

   - Change the ``DOMAIN`` line so that after the ``=`` is the domain name you registered above. As an example: ``DOMAIN=MyOdkCentralServer.com``. Do not include ``http://`` or ``https://`` in the domain.
   - Change the ``SYSADMIN_EMAIL`` line so that after the ``=`` is your own email address. The Let's Encrypt service will use this address only to notify you if something is wrong with your security certificate.
   - Leave the rest of the settings alone. If you have a custom security or network environment you are trying to integrate Central into, see the :ref:`advanced configuration <central-install-digital-ocean-advanced>` sections for more information on these options.
   - Hold ``Ctrl`` and press ``x`` to quit the text editor. Press ``y`` to indicate that you want to save the file, and then press **Enter** to confirm the file name. Do not change the file name.

     .. image:: /img/central-install/nano.png

#. Let the system know that you want the latest version of the database:

   .. code-block:: bash

     $ touch ./files/allow-postgres14-upgrade

   This is mostly useful for *upgrades* but is also currently necessary for fresh installs.

#. Bundle everything together into a server. This will take a long time and generate quite a lot of text output. Don't worry if it seems to pause without saying anything for a while.

   .. code-block:: bash

     $ docker compose build

   When it finishes, you should see some "Successfully built" type text and get your input prompt back.

**Congratulations**! You have installed your copy of Central. Next, we need to teach the server how to start it up, and do so.

.. _central-install-digital-ocean-startup:

Starting up Central
-------------------

#. Start the server software. The first time you start it, it will take a while to set itself up.

   .. code-block:: bash

     $ docker compose up -d

#. See whether ODK has finished loading.

   .. code-block:: bash

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

   .. code-block:: bash

     $ cd central

#. Create a new account. Make sure to substitute the email address that you want to use for this account.

   .. code-block:: bash

     $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-create

   Press **Enter**, and you will be asked for a password for this new account.

#. Make the new account an administrator.

   .. code-block:: bash

     $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-promote

   If you ever lose track of your password, you can reset it with

   .. code-block:: bash

     $ docker compose exec service odk-cmd --email YOUREMAIL@ADDRESSHERE.com user-set-password

#. Log into the Central website. Go to your domain name and enter in your new credentials. Once you have one administrator account, you do not have to go through this process again for future accounts: you can log into the website with your new account, and directly create new users.

.. tip::

  We strongly recommend using a :ref:`custom mail server <central-install-digital-ocean-custom-mail>` to ensure account creation and password reset emails are delivered. If account creation is failing or users are not receiving emails, see :ref:`troubleshooting emails <troubleshooting-emails>`.

.. _central-install-digital-ocean-backups:

Setting Up Backups
------------------

The next step is setting up automated system backups. We strongly recommend you have backups because they provide a safety net if something goes wrong.

You can find instructions for setting up backups in `DigitalOcean's backups guide <https://docs.digitalocean.com/products/images/backups/getting-started/quickstart/>`_.

Note that Central has its own :ref:`backups <central-backup>` system that you can configure in addition to full system backups. Central's built-in backups are particularly helpful if you wish to backup your data via API.

.. _central-install-digital-ocean-monitoring:

Setting Up Monitoring
---------------------

The last thing you will want to do is to set up server monitoring. Alerts and monitoring are important because they can inform you of problems with your server before they affect your data collection project.

You can find instructions for setting up alerts in the `DigitalOcean's monitoring guide <https://docs.digitalocean.com/products/monitoring/getting-started/quickstart/>`_.

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

#. To add 2 GB swap, log into your server's console and run these commands.

   .. code-block:: bash
   
     $ fallocate -l 2G /swap
     $ dd if=/dev/zero of=/swap bs=1k count=2048k
     $ chmod 600 /swap
     $ mkswap /swap
     $ swapon /swap

#. Make sure swap is only used when the server is almost out of memory.

   .. code-block:: bash

     $ sysctl -w vm.swappiness=10

#. Edit ``/etc/sysctl.conf`` and add the following to the end of the file to ensure that change is permanently available.

   .. code-block:: bash

     $ nano /etc/sysctl.conf

   .. code-block:: bash

     vm.swappiness=10

#. Edit ``/etc/fstab`` and add the following to the end of the file to ensure that the swap file is permanently available.

   .. code-block:: bash
  
     $ nano /etc/fstab
  
   .. code-block:: bash
  
    /swap swap swap defaults 0 0

#. Finally, :ref:`increase memory allocation <central-install-custom-memory>` so Central can use the swap you've added.

.. _central-install-custom-memory:

Increasing RAM Allocation
-------------------------

During upgrades or exports, some versions of Central may use more memory than the 2 GB typically available to the Central service. If you run into this problem, increase the memory allocated to the Central service.

#. Ensure you have more than 2 GB of physical memory in your server. If you have less, `add more physical memory <https://www.digitalocean.com/docs/droplets/how-to/resize/>`_.

   .. tip::
     If you can't add more physical memory, :ref:`add swap <central-install-digital-ocean-swap>`. This will result in slower performance than adding physical memory but can be acceptable if it is only needed for occasional exports or upgrades.

#. Edit ``.env`` to add a ``SERVICE_NODE_OPTIONS`` variable with a ``--max-old-space-size`` flag set to your desired maximum memory in MB.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     SERVICE_NODE_OPTIONS='--max-old-space-size=3072'

   .. note::

     Choose a memory size that leaves enough memory for your server's operating system and any other applications. 3072 MB is a good starting point for a machine with 4 GB of RAM.

#. Build and restart the service container.

   .. code-block:: bash

     $ docker compose build service && docker compose stop service && docker compose up -d service

If an upgrade was the cause of the memory error, you may revert these changes after the upgrade and build and restart the service container.

.. _central-install-digital-ocean-custom-ssl:

Using a Custom SSL Certificate
------------------------------

Central uses Let's Encrypt SSL certificates to secure all communication. To use custom certificates:

#. Generate a ``fullchain.pem`` (``-out``) file which contains your certificate followed by any necessary intermediate certificate(s).
#. Generate a ``privkey.pem`` (``-keyout``) file which contains the private key used to sign your certificate.
#. Copy those files into ``files/local/customssl/``.

   .. code-block:: bash

     $ cp fullchain.pem central/files/local/customssl/
     $ cp privkey.pem central/files/local/customssl/

#. In ``.env``, set ``SSL_TYPE`` to ``customssl`` and set ``DOMAIN`` to the domain name you registered. 

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     DOMAIN=MyOdkCentralServer.com
     SSL_TYPE=customssl

   .. note::

     Do not include ``http://`` or ``https://`` in the domain.

#. Build and restart the nginx container.

   .. code-block:: bash

     $ docker compose build nginx && docker compose stop nginx && docker compose up -d nginx

.. _central-install-digital-ocean-custom-mail:

Using a Custom Mail Server
--------------------------

.. tip::
  We recommend using a dedicated email service such as `Mailjet <https://www.mailjet.com>`_ for your custom mail server. Follow the dedicated service's instructions for enabling DKIM and SPF to ensure your messages are delivered.

Central comes with a mail server to send password reset emails. To use a custom mail server:

#. Edit ``.env`` with your mail server host, port, and authentication details.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     EMAIL_FROM=my-no-reply-email-address
     EMAIL_HOST=my-email-host
     EMAIL_PORT=my-email-port
     EMAIL_IGNORE_TLS=true-or-false
     EMAIL_SECURE=true-or-false
     EMAIL_USER=my-email-user
     EMAIL_PASSWORD=my-email-password

   .. note::

     ``EMAIL_FROM`` is the address the email should come from. It's sometimes known as the sender address.

     ``EMAIL_IGNORE_TLS`` should generally be set to ``false``. ``EMAIL_SECURE`` should be set to ``true`` if you use port 465 and set to ``false`` for other ports.

     ``EMAIL_USER`` and ``EMAIL_PASSWORD`` are both required.

#. Build and restart the service container.

   .. code-block:: bash

     $ docker compose build service && docker compose stop service && docker compose up -d service

.. _central-install-digital-ocean-custom-db:

Using a Custom Database Server
------------------------------

.. warning::
  Using PostgreSQL 14 isn't strictly required, but we only test with and support PostgreSQL 14.

  Using a custom database server that is not on your local network, may result in poor performance.

Central comes with a PostgreSQL v14.x database server to store your data. To use a custom PostgreSQL database server:

#. Connect to your database server.

   .. code-block:: bash

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
      CREATE EXTENSION IF NOT EXISTS pgrowlocks;

#. Edit ``.env`` with your database server host, database name, and authentication details.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     DB_HOST=my-db-host
     DB_USER=my-db-user
     DB_PASSWORD=my-db-password
     DB_NAME=my-db-name

#. Build and restart the service container.

   .. code-block:: bash

     $ docker compose build service && docker compose stop service && docker compose up -d service

.. _central-install-digital-ocean-s3:

Using S3-compatible Storage
---------------------------

By default, Central stores form and submission attachments in its main database, but it can be configured to move these to an external object store. If you already have or plan to collect many files, storing them outside the main database can reduce database load and cost. It can also make it more practical to backup and restore the database.

Consider the following to help you decide whether S3-compatible storage is a good fit:

* You can configure S3-compatible storage at any time and migrate existing files out of your database. However, once you opt into using S3-compatible storage, there is no automated way to migrate files back to the database.
* If you opt into S3-compatible storage, any system you use to retrieve file data from Central must be able to follow redirects (for example, Briefcase will not be able to retrieve form and submission attachments but ``pyodk`` will).
* The names of objects stored in S3-compatible storage do not stand alone and must be converted to useful filenames and connected to the right forms and/or submissions by Central. For example, object names will look like ``blob-412-950ababd4c8cf8d11rf5421433b5e3dafx5f6e75``.
* If you opt into S3-compatible storage, you must design a backup and restore strategy for that storage.

To use S3-compatible storage for all files saved in Central, follow these steps:

#. Set up a bucket with your chosen S3-compatible provider. Options include:

   * `Amazon S3 <https://aws.amazon.com/s3/>`_
   * Locally-hosted service such as `MinIO <https://min.io/docs/minio/linux/index.html>`_
   * `DigitalOcean Spaces <https://www.digitalocean.com/products/spaces>`_
   * `Google Cloud Storage <https://cloud.google.com/storage/>`_
   * `Cloudflare R2 <https://developers.cloudflare.com/r2/>`_

#. Make sure that the bucket's visibility is set to PRIVATE

#. Create a user with minimal permissions to your bucket only. The exact process and permissions will depend on your S3 provider. For example:

   * DigitalOcean Spaces: create an `"Access Key" <https://docs.digitalocean.com/products/spaces/how-to/manage-access/>`_
   * Amazon S3: create an IAM user

     * .. collapse:: Example policy

           .. code-block:: json

              {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Effect": "Allow",
                    "Action": [
                      "s3:GetBucketLocation",
                      "s3:PutObject",
                      "s3:GetObject",
                      "s3:DeleteObject",
                      "s3:ListBucketMultipartUploads",
                      "s3:ListMultipartUploadParts"
                    ],
                    "Resource": [
                      "arn:aws:s3:::MY_BUCKET/*",
                      "arn:aws:s3:::MY_BUCKET"
                    ]
                  }
                ]
              }

#. Edit ``.env`` with your chosen service's URL as well as your bucket name, access key and secret. If your service has a region concept, use a general URL that does not specify region. For example, the URL to use for S3 is `https://s3.amazonaws.com`. You must use an ``https`` URL, not an ``http`` one.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

      S3_SERVER=https://service.com
      S3_ACCESS_KEY=MY_ACCESS_KEY
      S3_SECRET_KEY=MY_SECRET
      S3_BUCKET_NAME=MY_BUCKET

#. Stop and restart your server to apply the configuration:

   .. code-block:: bash

     $ docker compose stop
     $ docker compose up -d

#. Try the configuration by attempting to upload existing one existing file. If this is a new server, you can upload an XLSForm to create a file.

   .. code-block:: bash

     $ docker compose exec service node lib/bin/s3.js upload-pending 1

   .. note::

     If you are using a custom database,
     :ref:`ensure all required extensions are installed <central-install-digital-ocean-custom-db>`.

   If the configuration is correct, you should see a success message. If there are issues with the configuration, you should see an error message with hints on what needs to be fixed. To try uploading the same file again, you will need to reset its status to pending:

   .. code-block:: bash

     $ docker compose exec service node lib/bin/s3.js reset-failed-to-pending
     $ docker compose exec service node lib/bin/s3.js upload-pending 1

Once you have a working configuration, Central will move new and existing files from the database to the external storage provider once every 24 hours. In each 24-hour period that there are new files to process, there will be a :doc:`Central Server Audit Log <central-server-audits/>` entry created with successes and failures.

You can manually request an upload of all pending files by using the ``upload-pending`` task described above without a count:

   .. code-block:: bash

     $ docker compose exec service node lib/bin/s3.js upload-pending

If there are any issues uploading a file, it will be marked as `failed` and will stay in the database. You can use the ``reset-failed-to-pending`` command as shown above to try uploading it again.

You can also use the same ``s3.js`` tool to get counts of files in any of the following statuses: 'pending', 'in_progress', 'uploaded', 'failed'. For example, to get a count of successfully uploaded files:

.. code-block:: bash

  $ docker compose exec service node lib/bin/s3.js count-blobs uploaded

.. _central-install-digital-ocean-sso:

Using Single Sign-on (SSO)
--------------------------

By default, users log into Central using an email address and password. However, if Single Sign-on (SSO) is enabled, then Central will no longer manage users' passwords and will instead forward users to a separate login server. This can be a convenient option if all of your users already have accounts on a service like Google Workspace or Azure Active Directory. Under this setup, the login server is called the "identity provider." If SSO is enabled, the identity provider will manage users' passwords, not Central.

Using a separate identity provider can allow you to enforce stricter security requirements than Central does. For example, Central requires that new passwords are at least 10 characters, but it does not require other password characteristics, such as the presence of certain symbols. However, if SSO is enabled in Central, and if the identity provider is configured to require specific password characteristics, then users will need to fulfill those requirements in order to log into Central. As another example, on its own, Central does not support multi-factor authentication (MFA). However, if SSO is enabled, and if the identity provider is configured to require MFA, then users will need to complete multi-factor authentication before logging into Central.

Central is compatible with any identity provider that uses the OpenID Connect (OIDC) protocol and is configured to require user email addresses. When SSO is enabled in Central, Central does not manage passwords, but it still identifies users using their email address. Central assumes that the identity provider verifies email addresses, requiring users to prove ownership of the email address they specify. If that is not the case, then do not enable SSO in Central.

.. warning::

  If you configure an identity provider that does not require email proof of ownership, it will be possible for users to impersonate each other. This could lead to users gaining access to Central resources that they are not intended to access.

.. warning::

  Enabling SSO currently disables API access. This means you won't be able to use PowerBI, Excel, ruODK, pyODK or other such tools to directly access data on your server. You'll need to export CSVs instead.

To enable SSO in Central, you will first need to configure your identity provider. You will then need to configure Central to provide information from your identity provider, specifically the issuer URL, client ID, and client secret.

#. Follow your identity provider's documentation on configuring a new OIDC application (for example: `Google <https://developers.google.com/identity/openid-connect/openid-connect>`_, `Azure <https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app>`_, `onelogin <https://onelogin.service-now.com/support?id=kb_article&sys_id=2fd988e697b72150c90c3b0e6253af7f&kb_category=93e869b0db185340d5505eea4b961934>`_, `Auth0 <https://auth0.com/docs/get-started/applications/application-settings>`_). When prompted to specify a redirect or callback URL, provide the following (replace ``my-domain`` with your actual domain):

   .. code-block:: bash

    https://my-domain/v1/oidc/callback

#. In ``.env``, set ``OIDC_ENABLED`` to ``true``. Set ``OIDC_ISSUER_URL`` to the issuer URL that you obtained from your identity provider, ``OIDC_CLIENT_ID`` to the client ID, and ``OIDC_CLIENT_SECRET`` to the client secret.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     OIDC_ENABLED=true
     OIDC_ISSUER_URL=my-issuer-url
     OIDC_CLIENT_ID=my-client-id
     OIDC_CLIENT_SECRET=my-client-secret

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d

Two Accounts: Central and the Identity Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you enable SSO, users will use their account on the identity provider to log into Central. However, users will still have a Central account that is separate from their account on the identity provider. A Central account is not automatically created for each account on the identity provider. Instead, a Central Administrator will need to create a Central account for each user of the identity provider who should be allowed to log into Central.

Central users will be able to change their display name shown in Central and to choose a different name from what is shown in the identity provider. However, because Central identifies users by their email address, most users will not be allowed to change their email address. Only a Central Administrator will be able to change the email address associated with a Central account. That will be necessary if a user's email address changes in the identity provider. In that case, an Administrator will need to manually change the user's email address in Central to match their new address in the identity provider.

If a Central Administrator changes their own email address to one that does not match the identity provider, they may lose access to Central. If they are the only Administrator, they will need to use :ref:`the command line <central-command-line-user-set-password>` to create a new Central Administrator that they do have access to.

Logout is not centralized, which means that when a user logs out of Central, that will not log them out of the identity provider. Conversely, when a user logs out of the identity provider, that will not log them out of Central. If a user logs out of Central, then goes to log back in, they may find that login is nearly instantaneous if they are still logged into the identity provider. That is, they may find that they are not required to log into the identity provider again in order to log into Central.

Enabling SSO in an Existing Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to enable SSO for an existing Central installation, even if the installation has existing users. Because Central identifies users by their email address, the address associated with each Central account must match the address of the corresponding account on the identity provider. If the email address does not match, the user will not be able to log in.

Enabling SSO will not log out users who are already logged in. Users who are already logged into Central will not be required to log into the identity provider until they are logged out of Central.

Disabling SSO
~~~~~~~~~~~~~

It is possible to disable SSO by following the steps below. If there were users before SSO was enabled (if SSO was disabled, then enabled, then disabled again), users will be able to log into Central using their same password from before SSO was enabled. You can :ref:`reset users' passwords <central-users-web-reset-password>` after disabling SSO.

To disable SSO:

#. In ``.env``, set ``OIDC_ENABLED`` to ``false``. Clear ``OIDC_ISSUER_URL``, ``OIDC_CLIENT_ID``, and ``OIDC_CLIENT_SECRET``.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     OIDC_ENABLED=false
     OIDC_ISSUER_URL=
     OIDC_CLIENT_ID=
     OIDC_CLIENT_SECRET=

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d


.. _central-install-digital-ocean-upstream-ssl:

Using Upstream SSL
------------------

.. warning::
  We have not extensively tested this configuration and it is subject to change. Use at your own risk.

You may wish to run Central behind a reverse proxy or load balancer. In order to do that, you must disable Central's native SSL support in favor for the upstream SSL provider.

#. Edit ``.env`` file to change your SSL type and HTTP/S ports. ``HTTP_PORT`` and ``HTTPS_PORT`` are the ports exposed on your host and ``UPSTREAM_HTTPS_PORT`` is the user-facing upstream HTTPS port.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     SSL_TYPE=upstream

     HTTP_PORT=8080
     HTTPS_PORT=8443
     UPSTREAM_HTTPS_PORT=443

2. Edit ``docker-compose.yml`` to add ``UPSTREAM_HTTPS_PORT`` to the service and enketo configurations.

   .. code-block:: bash

     $ nano docker-compose.yml

   .. code-block:: bash

     service:
       environment:
         - HTTPS_PORT=${UPSTREAM_HTTPS_PORT:-443}

     ...

     enketo:
       environment:
         - HTTPS_PORT=${UPSTREAM_HTTPS_PORT:-443}

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d

.. _central-install-digital-ocean-dkim:

Using DKIM
-----------

.. warning::
  Do not follow these instructions if you are using a :ref:`custom mail server <central-install-digital-ocean-custom-mail>`.

DKIM is a protocol which is used to help verify mail server identities. Without it, your sent mail is likely to be flagged as spam.

#. Ensure that your server's name in DigitalOcean `matches your full domain name <https://www.digitalocean.com/community/questions/how-do-i-setup-a-ptr-record?comment=30810>`_, and that the `hostname does as well <https://askubuntu.com/questions/938786/how-to-permanently-change-host-name/938791#938791>`_. If you had to make changes for this step, restart the server to ensure they take effect.


#. Generate a public and private key (if one doesn't already exist).

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ ! test -s files/mail/rsa.private && openssl genrsa -out files/mail/rsa.private 1024
     $ openssl rsa -in files/mail/rsa.private -out files/mail/rsa.public -pubout -outform PEM

#. Ensure any changes to the DKIM private key are kept private.

   .. code-block:: bash

     $ git update-index --skip-worktree files/mail/rsa.private

#. Copy the contents of the public key with the boundary dashes removed.

   .. code-block:: bash

     $ cat files/mail/rsa.public | grep -v "^-"

#. Create four new DNS records in these locations:

   1. ``dkim._domainkey.DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content. Be sure to remove any newlines or line breaks.

      .. code-block:: bash

        k=rsa; p=PUBLIC-KEY-HERE

   2. ``_dmarc.DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content.

      .. code-block:: bash

        v=DMARC1; p=none
   
   3. ``DOMAIN-NAME-HERE``: create a ``TXT`` record with the following content. Get the server IP address from the DigitalOcean control panel. 

      .. code-block:: bash

        v=spf1 a mx ip4:SERVER-IP-ADDRESS-HERE -all

   4. ``DOMAIN-NAME-HERE``: create a ``MX`` record with the following content.

      .. code-block:: bash

        10 DOMAIN-NAME-HERE

#. Build and restart the mail container.

   .. code-block:: bash

     $ docker compose build mail && docker compose stop mail && docker compose up -d mail

.. _central-install-digital-ocean-enketo:

Customizing Enketo
------------------

.. warning::
  Customizing Enketo may break Central in subtle and unexpected ways. Do not make changes if you do not understand the implications of those changes.

Enketo is the software that Central uses to render forms in a web browser. It is used for form previews, web browser submission, and submission editing. Common customizations include enabling geocoding, adding analytics, and setting a default theme.

#. Read the Enketo `configuration tutorial <https://enketo.github.io/enketo-express/tutorial-10-configure.html>`_ and `default-config.json <https://github.com/enketo/enketo-express/blob/master/config/default-config.json>`_ to understand what is possible.

#. Edit the file ``files/enketo/config.json.template`` with your desired changes.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano files/enketo/config.json.template

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d

.. _central-install-digital-ocean-sentry:

Disabling or Customizing Sentry
-------------------------------

By default, we enable `Sentry error logging <https://sentry.io>`_ in Central's service container, which provides the Central team with an anonymized log of unexpected errors that occur while your server is running.  We also enable `Sentry tracing <https://docs.sentry.io/concepts/key-terms/tracing/>`_ to gather performance metrics and help our team make performance improvements.

This information is only visible to the development team and should never contain any of your user or form data, but if you feel uncomfortable with this, you can disable Sentry:

#. Edit the file ``files/service/config.json.template`` and remove the ``sentry`` lines, starting with ``"sentry": {`` through the next four lines until you remove the matching ``}``.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano files/service/config.json.template

   .. code-block:: json

     "env": {
       "domain": "https://${DOMAIN}:${HTTPS_PORT}",
       "sysadminAccount": "${SYSADMIN_EMAIL}"
     },
     "external": {
     }

#. Edit the file ``files/nginx/odk.conf.template`` and replace the ``csp-report`` lines, starting with ``location /csp-report {`` through the next two lines until you remove the matching ``}`` with:

   .. code-block:: bash

     $ nano files/service/config.json.template

   .. code-block:: bash

      location /csp-report {
        return 200 'CSP report discarded.';
        add_header Content-Type text/plain;
      }

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d

If you wish to use your own Sentry instance to receive your own errors, take these steps:

#. Create an account on `Sentry <https://sentry.io>`_, and create a new ``nodejs`` project.
#. The new project will generate a ``DSN`` in this format: ``https://SENTRY_KEY@SENTRY_ORG_SUBDOMAIN.ingest.sentry.io/SENTRY_PROJECT``.
#. In ``.env``, set ``SENTRY_SUBDOMAIN``, ``SENTRY_KEY`` and ``SENTRY_PROJECT`` to the values from step 2.

   .. code-block:: bash

     $ cd central

   .. code-block:: bash

     $ nano .env

   .. code-block:: bash

     SENTRY_ORG_SUBDOMAIN=
     SENTRY_KEY=
     SENTRY_PROJECT=

#. Build and restart all containers.

   .. code-block:: bash

     $ docker compose build && docker compose stop && docker compose up -d
