.. _central-install:

Installing ODK Central
=======================

There are two ways to get access to a Central install. You can pay for official managed hosting on ODK Cloud, or if you are technical, you can self-host Central for free on your own infrastructure.

The software is the same either way you choose, but there are important trade-offs to consider.

.. toctree::
  :maxdepth: 2
  :hidden:

  Getting ODK Cloud <https://getodk.org#pricing>
  central-install-digital-ocean

.. _odk-cloud:

ODK Cloud (recommended)
-----------------------

If you are looking for the fastest and easiest way to run Central, use `ODK Cloud <https://getodk.org/#pricing>`_. ODK Cloud is official managed hosting of Central on ODK's fast, reliable, and secure infrastructure.

* ODK Cloud is fully-managed and fully-supported, so no technical skills are required.
* ODK Cloud has guaranteed and hassle-free levels of speed, reliability, and security.
* ODK Cloud directly funds continued work on ODK's software, community, and ecosystem.

.. _central-sysreqs:

System Requirements
-------------------

Central is designed to be speedy, but even more importantly it is robust. There is very very little chance it will mishandle or corrupt your data even if it is run on a weak machine and runs into extreme traffic. That said, if you will be installing it yourself you may wish to have an idea of its system requirements.

We have done some work to benchmark Central to verify these claims, and produce some guideline numbers. Every circumstance is different, and a lot will depend on your form design, your geographic location, and other factors. But in general, on the second-cheapest DigitalOcean configuration at time of writing ($10/month, 2 GB memory in 2018), we found the following:

 - A 250 question form without attachments could support 500 devices simultaneously uploading many submissions without issues, at a rate of roughly 41.2 submissions per second.
 - A larger 5000 question form, without attachments, could also support 500 devices submitting data at once, but runs more slowly (~12 submissions/second) and fails about one submission in every 1000 (which can then be re-submitted without issues).
 - Including attachments slows the process down, since there is more data to shuffle around. Realistically, the number of concurrent users supported in this scenario will decrease simply because Internet bandwidth in and out of Central will limit the number of submissions it can see at a time. But we have tried situations featuring 5 MB submissions with 50 devices at once without seeing issues (though for the mentioned reasons the response rate drops to between 1 and 2 submissions/second). Additionally, data exports with attachments take longer and are more memory-intensive.

 When you are planning for your installation and selecting a destination to deploy Central to, keep these numbers in mind. If 500 people submitting data *all at the same time* is a distant scenario, you can probably get by with a lower-performance option. If your deployment is larger than these numbers, consider bumping up to a more powerful machine. If you aren't sure, ask around in the forums.

.. _self-hosting:

Self-hosting
------------

If you are comfortable with Linux server administration, you can self-host Central for free. And while Central is available at no cost, please account for your infrastructure expenses and the time needed for ongoing maintenance.

.. note::
  To self-host Central, you must have a domain name (e.g., `central.example.com`) mapped to your server. For security reasons, Central will not work with just an IP address (e.g., `93.184.216.34`).

.. tip::
  We offer ODK Support packages for large organizations who have a compliance or legal need to self-host, but don't want their staff to take on the added cost and responsibility of keeping a Central install fast, reliable, and secure. Pricing starts at $19K/year. Email `support\@getodk.org <mailto:support\@getodk.org?subject=ODK\ Self-Host\ Support\ pricing>`_ for a quote.

Installing on DigitalOcean
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to self-host but you're not sure what cloud provider to choose, we recommend DigitalOcean. Start :ref:`here <central-install-digital-ocean>`.

.. _central-install-custom:

Installing elsewhere
~~~~~~~~~~~~~~~~~~~~

Central is entirely defined via **Docker Compose**, which means the ``docker compose`` command will be all you need to manage the entire system.

.. warning::
  We verify each version of Central on DigitalOcean and confirm that upgrades are possible. However, we do not verify them on other cloud providers and generally can't provide free support for installations that deviate from the DigitalOcean instructions. You may find other community members able to help `on the forum <https://forum.getodk.org/>`_.

No matter where you plan to install Central, we recommend reviewing the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean starting from :ref:`this section <central-install-digital-ocean-build>`. In particular, you'll need to update your submodules after you clone the repository, and configure your :file:`.env` file for your installation.

Installing on AWS
"""""""""""""""""

Amazon Web Services (AWS) is one of the many other options for installing Central. It's a good idea to read through the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean, as many of the steps remain the same or similar.

To obtain a server you will need to first `create an AWS account <https://aws.amazon.com/>`_. When launching your instance, select the Ubuntu Server 20.04 LTS AMI in step 1. The ``t2.micro`` instance type has the 1 GB of memory recommended for if you don't expect many forms to be submitted at once and you don't expect many large media attachments. Regardless of how much memory you select, we also recommend 1 GB of swap and a minimum of 15 GB of disk storage.

When adjusting the security settings open up the ports for SSH, HTTP, and HTTPS. Once you have launched your instance, go to the Elastic IPs menu option under Network & Security, then allocate a new address and associate it with your server in order to keep the IP address for your server consistent.

Before installing Central on your server, you need to install Docker and Docker Compose. Follow the instructions below.

1. `Install Docker Engine on Ubuntu <https://docs.docker.com/engine/install/ubuntu/>`_. 

2. `Install Docker Compose <https://docs.docker.com/compose/install/>`_. 

After installing Docker and Docker Compose you can follow our DigitalOcean instructions from running ``git clone https://github.com/getodk/central``. Continue with the DigitalOcean instructions for logging into Central.

Finally, :ref:`configure an e-mail service <central-install-digital-ocean-custom-mail>` such as `Amazon SES <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html>`_ because Amazon restricts emails sent from EC2.

Installing on Windows
"""""""""""""""""""""
We strongly recommend using Linux, preferably the latest Ubuntu Server LTS, as the host operating system (natively or in a virtual machine) for your Central install. 

If you wish to use Windows as the host, it's a good idea to read through the :doc:`instructions we've provided <central-install-digital-ocean>` for DigitalOcean, as many of the steps remain the same or similar.

The major differences are that you'll first need to install Git, Node.js, Docker, and Docker Compose. You'll also need to clone the Central repository with the correct line endings: ``git clone -c core.autocrlf=false https://github.com/getodk/central``.
