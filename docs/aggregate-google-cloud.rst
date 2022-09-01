Installing on Google Cloud
==========================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

.. warning::

  To use this setup, you must able to link a domain name to the machine's IP address. If you don’t own a domain, services such as `FreeDNS <https://freedns.afraid.org>`_ offer free sub-domains under a range of domains.

.. tip::

  If you are new to Google Cloud, you will need to `create a Google Cloud Platform project <https://console.cloud.google.com/cloud-resource-manager>`_ and make sure `billing is enabled <https://cloud.google.com/billing/docs/how-to/modify-project>`_. 


Create an instance
------------------

1. Go to the `GCP Dashboard <https://console.cloud.google.com/compute/instances>`_.

2. Click on :guilabel:`Create`.

3. In the :guilabel:`Name` text box, enter `aggregate` (or your desired name).

4. Select the desired region and zone.

    Choose a region that's close to the location where data is going to be collected.

5. Select the instance type you want to use.

    A minimum setup is a `small` instance type (1 vCPU, 1.7 GB of memory), but you should review your requirements and choose a bigger instance type according to your needs.

6. Click on :guilabel:`Change` under the :guilabel:`Boot disk` section.

7. Select :guilabel:`Ubuntu 18.04 LTS`.

8. Set the desired storage size for your VM, and click :guilabel:`Select`.

    A minimum setup is 30 GB of storage, but you should review your requirements and adjust the value of the `Size (GiB)` field according to your needs.

9. Under the :guilabel:`Firewall` section, check :guilabel:`Allow HTTP traffic`, and :guilabel:`Allow HTTPS traffic`.

10. Expand the :guilabel:`Management, security, disks, networking, sole tenancy` section.

11. In the :guilabel:`Management` tab, under :guilabel:`Automation`, copy the contents of `this startup script <https://raw.githubusercontent.com/getodk/aggregate/master/cloud-config/google-cloud/startup-script.sh>`_ into the :guilabel:`Startup script` text box.

12. In the :guilabel:`Networking` tab, set the :guilabel:`Hostname` with the domain name (e.g., your.domain) you want to use for Aggregate. This hostname will be used by the startup script to configure your instance's HTTPS support.

13. Click on :guilabel:`Create`.


Set up your domain
------------------

.. tip:: GCP instances use IP addresses which can change if you delete the instance. To ensure your Aggregate install will always be reachable using the same IP address, use a static IP address by following `these instructions <https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#promote_ephemeral_ip>`_.

1. Go to the `GCP - VM Instances <https://console.cloud.google.com/compute/instances>`_ page and find your instance.

2. Take note of the IP address (e.g., 12.34.56.78) in the :guilabel:`External IP` column and set a *DNS A record* pointing to it.

    If you own a domain, check your domain registrar's instructions. If you don't own a domain, we recommend using `FreeDNS <https://freedns.afraid.org>`_ to get a free sub-domain.

    Your domain's *TTL* setting will affect to how much time you will have to wait until you can proceed to the next step. If your provider gives you the option of setting a TTL, use the lowest value you can.

3.  Open a web browser, and periodically check the domain until you see the Aggregate website. You won't be able to continue the install until you see the website load.


Enable HTTPS
------------

1. In `GCP - VM Instances <https://console.cloud.google.com/compute/instances>`_ page, SSH into your VM clicking the :guilabel:`SSH` button in the :guilabel:`External IP` column.

2. Once you are logged in, run :command:`sudo certbot run --nginx --non-interactive --agree-tos -m YOUR_EMAIL --redirect -d YOUR_DOMAIN`. 

    Be sure to replace YOUR_EMAIL and YOUR_DOMAIN with your email address and your domain.

    Lets Encrypt uses the email you provide to send notifications about expiration of certificates.


Log into Aggregate
------------------

1. Go to https://your.domain and check that Aggregate is running.

2. Click :guilabel:`Sign in with Aggregate password` to login with the default username and password.

    | username: ``administrator``
    | password: ``aggregate``

3. Change the administrator account's password!