.. spelling::
  sub-domains

Installing on DigitalOcean
==========================

.. warning::

  To use this setup, you must able to link a domain name to the machine's IP address. If you don’t own a domain, services such as `FreeDNS <https://freedns.afraid.org>`_ offer free sub-domains under a range of domains.

.. tip::
  If you have not already created a DigitalOcean account, use our referral link to do so: https://m.do.co/c/39937689124c.

  DigitalOcean will give you $100 of credit to spend during the first 60 days so that you can try things out. Once you have spent $25 with them, we’ll get $25 to put towards our hosting costs.

Create your Droplet
-------------------

1.  Log into DigitalOcean and create a new Droplet.

2.  Select the distribution for your new Droplet: Select the option :guilabel:`18.04.x x64` from the Ubuntu box.

    .. image:: /img/aggregate-do/distribution.*
      :alt: Selecting the Droplet's distribution

3.  Choose a size fit for your intended usage. The :guilabel:`$5 Standard Droplet` should be enough for light Aggregate use. If you find yourself needing more, DigitalOcean makes it easy to resize to a bigger Droplet.

4.  If you would like automatic weekly backups, enable them.

5.  You will not need block storage.

6.  Choose a datacenter region physically close to where data collection
    is going to happen.

7.  Under :guilabel:`Select additional options`, check the :guilabel:`User data` checkbox. Copy and paste the contents of `this Cloud-Config script <https://raw.githubusercontent.com/opendatakit/aggregate/master/cloud-config/digital-ocean/cloud-config.yml>`_.

    .. image:: /img/aggregate-do/user-data.*
      :alt: Inserting Cloud-Config script under User Data section


8.  In the :guilabel:`Choose a hostname section`, enter the domain name (e.g., your.domain). This hostname will be used by the Cloud-Config script to configure your server’s HTTPS support.

9.  You will not need to add public SSH keys (unless you know what that is and you want to).

10. Click on the :guilabel:`Create` button. The Droplet takes a few seconds, the actual Aggregate installation will take up to 10 minutes to complete.


Set up your domain
------------------

1.  Once the Droplet is running, take note of its public IP address (e.g., 12.34.56.78) and set a *DNS A record* pointing to it.

    If you own a domain, check your domain registrar's instructions. If you don't own a domain, we recommend using `FreeDNS <https://freedns.afraid.org>`_ to get a free sub-domain.

    Your domain's *TTL* setting will affect to how much time you will have to wait until you can proceed to the next step. If your provider gives you the option of setting a TTL, use the lowest value you can.

2.  Open a web browser, and periodically check the domain until you see the Aggregate website. You won't be able to continue the install until you see the website load.

Enable HTTPS
------------

1. From the DigitalOcean Control Panel, click the name of your droplet, then select :guilabel:`Access` from the left navigation. Click the :guilabel:`Launch Console` button to open a web-based console session.

2. When the console opens, click the console screen, and at the login prompt, enter the user: `root`. Your password will be the root password that DigitalOcean emailed you.

    If you do not have the root password, click the name of your droplet, select :guilabel:`Access` from the left navigation and choose :guilabel:`Reset the root password` so that a password gets emailed to you.

    You may also login over `SSH <https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/>`_ using the :command:`ssh root@your.domain`.

3. Once you are logged in, run :command:`sudo certbot run --nginx --non-interactive --agree-tos -m YOUR_EMAIL --redirect -d YOUR_DOMAIN`.

    Be sure to replace YOUR_EMAIL and YOUR_DOMAIN with your email address and your domain.

    Lets Encrypt uses the email you provide to send notifications about expiration of certificates.

Log into Aggregate
------------------

1. Go to https://your.domain and check that Aggregate is running.

2. Login and change the administrator account's password!
