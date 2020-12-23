.. _central-install:

Installing Central
==================

Central is distributed and installed using `Docker <https://en.wikipedia.org/wiki/Docker_(software)>`_. Docker makes it possible to describe exactly how Central's different components should be configured no matter where it is installed. Don't worry if you don't know about Docker yet! We have put together step-by-step instructions for our recommended solutions below.

.. warning::
  Central is intended to be configured and administrated entirely with ``docker-compose stop`` and that is what we show in all our instructions. If you inadvertently do a ``docker-compose down``, it will look like you have lost your data. See :ref:`the troubleshooting section <troubleshooting-docker-compose-down>` to learn how to recover.

Using ODK Cloud (recommended)
-----------------------------

The easiest way to get a Central server is by using `ODK Cloud <https://getodk.org/#odk-cloud>`_.

ODK Cloud provides fast Central servers with regular feature updates, automatic security patches, daily backups, uptime management, enterprise security, and guaranteed support on any issues.

By choosing ODK Cloud, you are also directly supporting future development on ODK and helping make it better for everyone.

Installing on DigitalOcean
--------------------------

If you want to install Central on own server but you're not sure what cloud provider to choose, we recommend DigitalOcean. Start :ref:`here <central-install-digital-ocean>`.

.. _central-install-custom:

Installing elsewhere
--------------------

If you got excited when you saw mention of Docker above, and you already have your own destination and process for managing Docker deployments, you're all set to go. Central is entirely defined via **Docker Compose**, which means the ``docker-compose`` command will be all you need to manage the entire system.

.. warning::
  We verify each version of Central on DigitalOcean and confirm that upgrades are possible. However, we do not verify them on other cloud providers and generally can't provide free support for installations that deviate from the DigitalOcean instructions. You may find other community members able to help `on the forum <https://forum.getodk.org/>`_.

No matter where you plan to install Central, we recommend reviewing the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean starting from :ref:`this section <central-install-digital-ocean-build>`. In particular, you'll need to update your submodules after you clone the repository, and configure your :file:`.env` file for your installation.

Installing on Amazon EC2
~~~~~~~~~~~~~~~~~~~~~~~~

Amazon Web Services (AWS) is one of the many other options for installing Central. It's a good idea to read through the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean, as many of the steps remain the same or similar.

To obtain a server you will need to first `create an AWS account <https://aws.amazon.com/>`_. When launching your instance, select the Ubuntu Server 16.04 LTS Amazon Machine Image (AMI) in step 1. The ``t2.micro`` instance type has the 1GB of memory recommended for if you don't expect many forms to be submitted at once and you don't expect many large media attachments.

When adjusting the security settings open up the ports for SSH, HTTP, and HTTPS. Once you have launched your instance, go to the Elastic IPs menu option under Network & Security, then allocate a new address and associate it with your server in order to keep the IP address for your server consistent.

Before installing Central on your server, you need to install Docker and Docker Compose.

1. Docker. Steps 1 and 2 of this `how to install Docker on Ubuntu 16.04 tutorial <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04>`_ should walk you through the necessary commands. In step 2 add the ``ubuntu`` user to the Docker group.

2. Docker Compose. This `how to install Docker Compose on Ubuntu 16.04 tutorial <https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04>`_ should walk you through the necessary commands. You should only need to complete step 1. You can change the version number to ``1.24.1``.

After installing Docker and Docker Compose you can follow our DigitalOcean instructions from running ``git clone https://github.com/getodk/central``. Continue with the DigitalOcean instructions for logging into Central.

Finally, :ref:`configure an e-mail service <central-install-digital-ocean-custom-mail>` such as `Amazon SES <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html>`_ because Amazon restricts emails sent from EC2.
