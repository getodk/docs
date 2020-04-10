.. _central-install:

Installing ODK Central
======================

Unlike ODK Aggregate, Central does not run on Google App Engine. Instead, it is built on a new technology called `Docker <https://en.wikipedia.org/wiki/Docker_(software)>`_, which is a new kind of virtual machine (VM) system that allows smaller image files, better performance, and better ways to define how different pieces should fit together to create a server like Central. Don't worry if you don't know what that means! We have put together step-by-step instructions for our recommended solutions below:

.. _central-install-sandbox:

Using the Sandbox
-----------------

If you only want to try ODK Central to see if it's suitable for your project, consider skipping installation altogether and using the `Sandbox installation <https://sandbox.central.opendatakit.org/>`_ we've provided for exactly this reason. Do note that since there is only one Sandbox, all Sandbox users will be able to see each others' email addresses, form definitions, and submission data, so please be careful if you have sensitive information you wish to keep secret.

Otherwise, join the `ODK Forum <https://forum.getodk.org>`_ and send a personal message to `@yanokwa <https://forum.getodk.org/u/yanokwa>`_ to gain access to the Sandbox.

.. _central-install-docker:

Installing on DigitalOcean
--------------------------

If you want your own server but you're not sure what to do, we recommend installing ODK Central on DigitalOcean, which provides an excellent starting point for Docker installations like ours. For most projects, the $5/month tier will be more than enough for your needs.

To learn more about installing on DigitalOcean, please see :doc:`here <central-install-digital-ocean>`.

.. _central-install-custom:

Installing elsewhere
--------------------

If you got excited when you heard mention of Docker above, and you already have your own destination and process for managing Docker deployments, you're all set to go. ODK Central is entirely defined via **Docker Compose**, which means the ``docker-compose`` command will be all you need to manage the entire system.

We would still recommend reviewing the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean starting from :ref:`this section <central-install-digital-ocean-build>`. In particular, you'll need to update your submodules after you clone the repository, and configure your :file:`.env` file for your installation.

Installing on Amazon EC2
~~~~~~~~~~~~~~~~~~~~~~~~

Amazon Web Services (AWS) is one of the many other options for installing Central. It's a good idea to read through the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean, as many of the steps remain the same or similar.

To obtain a server you will need to first `create an AWS account <https://aws.amazon.com/>`_. When launching your instance, select the Ubuntu Server 16.04 LTS Amazon Machine Image (AMI) in step 1. The ``t2.micro`` instance type has the 1GB of memory recommended for if you don't expect many forms to be submitted at once and you don't expect many large media attachments. When adjusting the security settings open up the ports for SSH, HTTP, and HTTPS. Once you have launched your instance, go to the Elastic IPs menu option under Network & Security, then allocate a new address and associate it with your server in order to keep the IP address for your server consistent. 

Before installing ODK Central on your server, you need to you need to install software dependencies. Install Docker. Steps 1 and 2 of this `how to install Docker on Ubuntu 16.04 tutorial <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04>`_ should walk you through the necessary commands. In step 2 add the ``ubuntu`` user to the docker group. You also need to install Docker Compose. This `how to install Docker Compose on Ubuntu 16.04 tutorial <https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04>`_ should walk you through the necessary commands. You should only need to complete step 1. You can change the version number to ``1.24.1``.

After installing Docker and Docker Compose you can follow our DigitalOcean instructions from running ``git clone https://github.com/getodk/central``. When starting up Central and copying the ``docker-compose@.service`` file, you may need to run the command with root privileges by appending ``sudo``, changing the command to ``sudo cp files/docker-compose@.service /etc/systemd/system``. Open the copied file in a text editing application, for example by typing ``sudo nano /etc/systemd/system/docker-compose@.service`` and pressing **Enter**. Change the line reading ``WorkingDirectory=/root/%i`` to be ``WorkingDirectory=/home/ubuntu/%i`` to reflect the folder where you downloaded Central. You can then run ``sudo systemctl enable docker-compose@central`` to start the service at boot, and ``sudo systemctl start docker-compose@central`` to start the service. Continue with the DigitalOcean instructions for logging into ODK Central.
