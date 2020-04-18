.. spelling::
  sub-domains
  vcpu
  GB

Installing on Microsoft Azure
=============================

.. warning::

  To use this setup, you must able to link a domain name to the virtual machine's IP address. If you don’t own a domain, services such as `FreeDNS <https://freedns.afraid.org>`_ offer free sub-domains under a range of domains.


Create a VPC
------------

1. Go to the `Virtual machines <https://portal.azure.com/?l=en.en-us#blade/HubsExtension/Resources/resourceType/Microsoft.Compute%2FVirtualMachines>`_ dashboard.

2. Click on :guilabel:`Add`.

3. Ensure you have a :guilabel:`Subscription` and a :guilabel:`Resource group`. If no resource group exists, create one called `Aggregate` (or your desired name).

4. In the :guilabel:`Virtual machine name` text box, enter `Aggregate` (or your desired name).

5. Select the desired region.

    Choose a region that's close to the location where data is going to be collected.

6. In :guilabel:`Image`, select `Ubuntu 18.04 LTS`.

7. Select :guilabel:`Size` of VM you want to use.

    A minimum setup is a `B1ms` type (1 vcpu, 2 GB of memory), but you should review your requirements and choose a bigger VM according to your needs.

9. Set a :guilabel:`Authentication type` to `Password` and enter a secure :guilabel:`Username` and :guilabel:`Password`.

    Alternatively, use a SSH public key if you know what that is and how to use it.

10. Under :guilabel:`Public inbound ports`, select `Allow selected ports`.

11. In :guilabel:`Select inbound ports`, select `HTTP`, `HTTPS`, and `SSH`.

12. Click :guilabel:`Next : Disks >`.

13. Click :guilabel:`Create and attach a new disk`.

14. Select :guilabel:`Disk type` and :guilabel:`Size` of disk you want to use.

    A minimum setup is a `Standard SSD` disk type and `30 GiB` size, but you should review your requirements and adjust appropriately.

15. Click on the :guilabel:`Advanced`. It's in the tabs at the top of the screen.

16. In the :guilabel:`Cloud init` text box, paste the contents of `this Cloud-Config script <https://raw.githubusercontent.com/getodk/aggregate/master/cloud-config/azure/cloud-config.yml>`_.

17. Click :guilabel:`Next : Tags >`.

18. Add :guilabel:`Name` of `aggregate.hostname` and a :guilabel:`Value` of your domain (e.g., your.domain). This hostname will be used by the Cloud-Config script to configure your VM's HTTPS support.

19. Expand the :guilabel:`Next: Review + create`, then :guilabel:`Create`.


Set up your domain
------------------

.. tip:: Azure VPCs use IP addresses which can change if you destroy the VPC. To ensure your Aggregate install will always be reachable using the same IP address, use a static IP by following `these instructions <https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-deploy-static-pip-arm-portal>`_.

1. In `Virtual machines <https://portal.azure.com/?l=en.en-us#blade/HubsExtension/Resources/resourceType/Microsoft.Compute%2FVirtualMachines>`_ dashboard, find your VM from the list. Click on it and find the value of the :guilabel:`Public IP address` field in the overview section.

2. Take note of the IP address (e.g., 12.34.56.78) and set a *DNS A record* pointing to it.

    If you own a domain, check your domain registrar's instructions. If you don't own a domain, we recommend using `FreeDNS <https://freedns.afraid.org>`_ to get a free sub-domain.

    Your domain's *TTL* setting will affect to how much time you will have to wait until you can proceed to the next step. If your provider gives you the option of setting a TTL, use the lowest value you can.

3.  Open a web browser, and periodically check the domain until you see the Aggregate website. You won't be able to continue the install until you see the website load.


Enable HTTPS
------------

.. warning:: Azure VMs seem to be slower to install software than other cloud providers. If you are having trouble running the commands in this step, wait 15 minutes and try again.

1. Connect to your VM `via SSH <https://docs.microsoft.com/en-us/azure/virtual-machines/linux/ssh-from-windows#windows-packages-and-ssh-clients>`_.

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