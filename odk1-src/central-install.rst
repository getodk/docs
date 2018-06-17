.. _central-install:

Installing ODK Central
======================

Unlike ODK Aggregate, Central does not run on Google App Engine. Instead, it is built on a new technology called `Docker <https://en.wikipedia.org/wiki/Docker_(software)>`_, which is a new kind of virtual machine (VM) system that allows smaller image files, better performance, and better ways to define how different pieces should fit together to create a server like Central. Don't worry if you don't know what that means! We have put together step-by-step instructions for our recommended solutions below:

.. _central-install-sandbox:

Using the Sandbox
-----------------

If you only want to try ODK Central to see if it's suitable for your project, consider skipping installation altogether and using the `Sandbox installation <https://sandbox.central.opendatakit.org/>`_ we've provided for exactly this reason. Do note that since there is only one Sandbox, all Sandbox users will be able to see each others' email addresses, form definitions, and submission data, so please be careful if you have sensitive information you wish to keep secret.

Otherwise, private message `Yaw Anokwa on the Open Data Kit Forum <https://forum.opendatakit.org/u/yanokwa>`_ to gain access to the Sandbox.

.. _central-install-docker:

Installing on DigitalOcean
--------------------------

If you want your own server but you're not sure what to do, we recommend installing ODK Central on DigitalOcean, which provides an excellent starting point for Docker installations like ours. For most projects, the $5/month tier will be more than enough for your needs.

To learn more about installing on DigitalOcean, please see the instructions `here <https://github.com/opendatakit/central#running-on-digitalocean>`_.

.. _central-install-custom:

Installing elsewhere
--------------------

If you got excited when you heard the word "Docker" above, and you already have your own destination and process for managing Docker deployments, you're all set to go. ODK Central is entirely defined via **Docker Compose**, which means the ``docker-compose`` command will be all you need to manage the entire system.

We would still recommend reviewing the `instructions we've provided <https://github.com/opendatakit/central#running-on-digitalocean>`_ for DigitalOcean starting from step 9. In particular, you'll need to update your submodules after you clone the repository, and configure your :file:`.env` file for your installation.

