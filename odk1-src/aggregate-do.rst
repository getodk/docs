.. spelling::

  textbox
  rsa
  org
  subdomains

Installing on DigitalOcean (Cloud)
==================================

This document provides instructions on setting up ODK Aggregate using a `CloudConfig  stack <https://cloudinit.readthedocs.io/en/latest/>`_ on a Ubuntu 18.04 Droplet in `DigitalOcean <https://www.digitalocean.com/>`_.

.. admonition:: Before you get started...

  You will need to set up and provide a DNS domain name to complete the deployment.

Requirements
------------

- Select the Ubuntu 18.04 distribution for your new Droplet
- Be able to link a domain name to the Droplet's IP address

Instructions
------------

If you haven't already created an account, use this link to do so: `https://m.do.co/c/39937689124c <https://m.do.co/c/39937689124c>`_

DigitalOcean will give you $100 of credit to spend during the first 60 days so that you can try things out and select what better fits to your workload.

.. admonition:: If something goes wrong...

  Sometimes this process can fail due to issues with third party services such as GitHub, or the Ubuntu package repositories. Often, the easiest way to solve this is to delete the Droplet and start the process again.

  You can also ask for help in the `Support forum <https://forum.opendatakit.org/c/support>`_.

1 - Create your Droplet
~~~~~~~~~~~~~~~~~~~~~~~

- Head to https://www.digitalocean.com and log in.

- Start the process to create a new Droplet

- Select the distribution for your new Droplet: Select the option `18.04` from the Ubuntu box.

  .. image:: https://github.com/opendatakit/aggregate/raw/master/cloud-config/digital-ocean/README_assets/DO_ubuntu_distribution_selection.png

- Choose a size fit for your intended usage. The standard $5 droplet size should be enough for light ODK Aggregate operations, although you might need to choose bigger sizes for extra storage, or if you expect a more intensive usage.

  ODK Aggregate will exclusively use the storage built into your droplet. Don't enable any extra block storage.

- Choose a datacenter region close to where data collection is going to happen.

- Check the `User Data` checkbox under the `Select additional options` section.

  Download `this CloudConfig script <https://raw.githubusercontent.com/opendatakit/aggregate/master/cloud-config/assets/cloud-config.tpl>`_ and copy its contents in the text box.

  .. image:: https://github.com/opendatakit/aggregate/raw/master/cloud-config/digital-ocean/README_assets/DO_user_data_and_cloud_config.png

- Use the domain you want to use as the Droplet's name on the `Choose a hostname` section.

  .. warning::

    This data will be used by the Cloud-Config script to configure your server's domain name. You have to use the same domain to enable SSL in step 4.


- Click on the `create` button

Although the creation of the Droplet itself takes just some seconds to complete, **the actual ODK Aggregate installation will take up to 10 minutes to complete**.

In the mean time, you can continue with the next steps.

2 - Set up your domain
~~~~~~~~~~~~~~~~~~~~~~

Once the Droplet is running, take note of its public IP address and set a *DNS A record* pointing to it:

- DigitalOcean `How to manage DNS records - A records <https://www.digitalocean.com/docs/networking/dns/how-to/manage-records/#a-records>`_

- Check your provider's instructions if your domain is not hosted or managed by DigitalOcean

.. note::

  - If you don't own a domain, services such as `FreeDNS <https://freedns.afraid.org>`_ offer creating subdomains under a range of domains for free.

  - Your domain's TTL setting (which oftentimes is fixed by your provider) will affect to how much time you will have to wait until you can proceed to step 5. A TTL value of `3600` means that a change will take up to one hour (3 600 seconds) to propagate.

    If your provider gives you the option of setting a TTL, use the lowest value you can.

.. warning::

  You won't be able to continue the installation process until the changes to the domain have been propagated

3 - Wait until the installation of ODK Aggregate is completed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open a web browser, and check periodically the domain you've configured until you see the ODK Aggregate website showing up.

4 - Enable SSL
~~~~~~~~~~~~~~

- SSH into your Droplet using `ssh root@your.domain.com`
- Run the command:

  .. code-block:: console

    certbot run --nginx --non-interactive --agree-tos -m {YOUR_EMAIL} --redirect -d {THE_DOMAIN}

  Be sure to replace `{YOUR_EMAIL}` and `{THE_DOMAIN}` with the actual values you want to use. LetsEncrypt uses the email you provide to send notifications about expiration of certificates.

5 - Check Aggregate
~~~~~~~~~~~~~~~~~~~

- Go to https::{THE_DOMAIN} and check that Aggregate is running.

.. tip::

  Don't forget to change the administrator account's password
