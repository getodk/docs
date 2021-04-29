.. spelling::
  sub-domains
  vCPU
  GiB
  IPv

Installing on Amazon Web Services
=================================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

.. warning::

  To use this setup, you must able to link a domain name to the machine's IP address. If you don’t own a domain, services such as `FreeDNS <https://freedns.afraid.org>`_ offer free sub-domains under a range of domains.

.. tip::

  Make sure you have selected the availability zone where you want to perform your actions. You can choose the availability zone using the dropdown menu at the top-right corner of the AWS console website. Choose a region that's close to the location where data is going to be collected.


Create a VPC
------------

1. Go to the `VPC Dashboard <https://console.aws.amazon.com/vpc/home#dashboard>`_. 

2. Click on :guilabel:`Launch VPC Wizard`.

3. Follow the wizard for the :guilabel:`VPC with a Single Public Subnet` configuration.

4. Enter `aggregate-vpc` (or your desired name) in the :guilabel:`VPC Name` field.

5. Click on :guilabel:`Create VPC`.


Create a security group
-----------------------

1. Go to the `VPC - Security Groups <https://console.aws.amazon.com/vpc/home#dashboard>`_ tab.

2. Click on :guilabel:`Create security group`.

3. Follow the wizard for the :guilabel:`VPC with a Single Public Subnet` configuration.

4. Enter `aggregate-sg` (or your desired name) as the name and description. 

5. Select the VPC you previously created.

6. Click on :guilabel:`Create`.

7. Click on the newly created security group from the list, click on the :guilabel:`Inbound rules` tab, the :guilabel:`Edit rules`.

8. Add the following rules to allow SSH, HTTP, and HTTPS traffic.

    +-------+----------+
    | Type  | Source   |
    +=======+==========+
    | SSH   | Anywhere |
    +-------+----------+
    | HTTP  | Anywhere |
    +-------+----------+
    | HTTPS | Anywhere |
    +-------+----------+

9. Click on :guilabel:`Save rules`. 


Create an IAM role
------------------
The EC2 machine needs an IAM role to query its tags.

1. Go to the `IAM - Roles <https://console.aws.amazon.com/iam/home#/roles>`_ tab.

2. Click on :guilabel:`Create role`.

3. Select the :guilabel:`AWS service` box, and click on the :guilabel:`EC2` link.

4. Click on :guilabel:`Next: Permissions`.

5. Search for `AmazonEC2ReadOnlyAccess`, and select it.

6. Click on :guilabel:`Next: Tags` and do nothing.

7. Click on :guilabel:`Next: Review`.

8. Enter `aggregate-role` (or your desired name) as the name.

9. Click on :guilabel:`Create role`.


Create an EC2 machine
---------------------

1. Go to the `EC2 Dashboard <https://console.aws.amazon.com/ec2/v2/home#Home:>`_.

2. Click on :guilabel:`Launch instance`.

3. Search for the `Ubuntu Server 18.04 LTS` AMI. 

4. Select the :guilabel:`64-bit (x86)` option and click on :guilabel:`Select`.

5. Select the instance type you want to use.

    A minimum setup is a `t2.small` instance type (1 vCPU, 2GiB RAM), but you should review your requirements and choose a bigger instance type according to your needs.

6. Click on :guilabel:`Next: Configure Instance Details`.

7. Select the VPC you previously created in the :guilabel:`Network` dropdown.

8. Select `Enable` in the :guilabel:`Auto-assign Public IP` dropdown.

9. Select the IAM role you previously created in the :guilabel:`IAM role` dropdown.

10. Toggle the :guilabel:`Advanced Details` section and copy and paste the contents of `this Cloud-Config script <https://raw.githubusercontent.com/getodk/aggregate/master/cloud-config/aws/cloud-config.yml>`_.

11. Click on :guilabel:`Next: Add Storage` and edit the storage settings. 

    A minimum setup is 30 GiB of storage, but you should review your requirements and adjust the value of the `Size (GiB)` field according to your needs.
 
12. Click on :guilabel:`Next: Add Tags`.

13. Add a `aggregate.hostname` key with the domain name as the value (e.g., your.domain). This hostname will be used by the Cloud-Config script to configure your machine's HTTPS support.

14. Click on :guilabel:`Next: Configure Security Group`.

15. :guilabel:`Select an existing security group` and select the security group you previously created.

16. Click on :guilabel:`Review and Launch` and after review, click on :guilabel:`Launch`.

17. You will be offered the option of using an existing key pair or creating one. It's very important that you follow the dialog's instructions carefully to be able to access your machine once it's created.

18. When you're ready, click on :guilabel:`Launch instances`.


Set up your domain
------------------

.. tip:: EC2 machines use IP addresses which can change if you stop and start (but not reboot) the machine. To ensure your Aggregate install will always be reachable using the same IP address, use an Elastic IP by following `these instructions <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_.

1. Go to the `EC2 - Instances <https://console.aws.amazon.com/ec2/v2/home#Instances:>`_ tab and find your machine.

2. Take note of the IPv4 Public IP address (e.g., 12.34.56.78) and set a *DNS A record* pointing to it.

    After clicking on the instance from the list, look for under the Description tab at the bottom of the window. The IPv4 Public IP field is in the right column.
  
    If you own a domain, check your domain registrar's instructions. If you don't own a domain, we recommend using `FreeDNS <https://freedns.afraid.org>`_ to get a free sub-domain.

    Your domain's *TTL* setting will affect to how much time you will have to wait until you can proceed to the next step. If your provider gives you the option of setting a TTL, use the lowest value you can.

3. Open a web browser, and periodically check the domain until you see the Aggregate website. You won't be able to continue the install until you see the website load.


Enable HTTPS
------------

1. `Connect to your machine <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html?icmpid=docs_ec2_console>`_ via SSH using :command:`ssh -i /path/to/the/key.pem ubuntu@your.domain`.

    Make sure your PEM key pair file has the `correct file permissions <https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html#troubleshoot-unprotected-key>`_.

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