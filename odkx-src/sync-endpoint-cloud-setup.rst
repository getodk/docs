.. spelling::
  phpLDAPadmin
  readonly
  dns
  letsencrypt
  subdomain

.. _sync-endpoint-cloud-setup:

Setup ODK-X Sync Endpoint with Cloud Services
=============================================

This tutorial will help you launch ODK-X Sync Endpoint on a virtual machine hosted on a cloud service provider.  ODK-X Sync Endpoint communicates with your ODK-X Android applications in order to synchronize your data and application files.

| There are 3 main options that we have documented to set up ODK-X Sync Endpoint
|   :ref:`1.  DigitalOcean console <sync-endpoint-setup-digital-ocean>`
|   :ref:`2.	Azure console <sync-endpoint-setup-azure>`
|   :ref:`3.	Amazon Web Services console <sync-endpoint-setup-aws>`

.. note::
  The apps require at least *2GB* of space to run, therefore, at least *4GB* of space is recommended for the server (for example - a droplet on DigitalOcean).

.. _sync-endpoint-setup-domain:

Step 0: Acquire a domain name or subdomain
------------------------------------------

Running the ODK-X Sync Endpoint in the cloud will require access to a publicly registered domain name to allow for a secure connection between Android devices and the Sync Endpoint. Domain names can be purchased via many providers. We have used `Google Domains <https://domains.google.com/>`_, `Amazon Route 53 <https://aws.amazon.com/route53/>`_, Azure App Services Domains, and `Cloudflare Registrar <https://www.cloudflare.com/products/registrar/>`_ successfully.

If you already own a domain, you may add a subdomain record for use with Sync Endpoint without purchasing a whole new domain. Before you go on, make sure you have a domain and know how to log into your domain management console to add a DNS record!

.. note::
  Specific instructions for connecting ODK-X Sync Endpoint to your domain will vary based on your registrar and DNS provider.

.. _sync-endpoint-setup-digital-ocean:

Option 1: DigitalOcean console
-----------------------------------------------------------------------------------------

| If you'd like to set up an ODK-X server that's accessible from anywhere via the Internet, DigitalOcean provides a one-click configuration that's nicely geared with nearly all the tools you'll need to set up your new server. The only thing it doesn't do is register a domain name, which you will have to do in order to obtain a security certificate for your server. These instructions walk you through:
|   -	:ref:`Setting up a DigitalOcean account <sync-endpoint-setup-digital-ocean-account>`
|   -	:ref:`Setting up a Droplet, DigitalOcean’s name for a server you can access and manage <sync-endpoint-setup-digital-ocean-droplet>`
|   -	:ref:`Setting up a DNS record <sync-endpoint-setup-digital-ocean-dns>`
|   -	:ref:`Connecting to your Droplet <sync-endpoint-setup-digital-ocean-connecting>`
|   -	:ref:`Enabling a firewall to prevent unintended traffic <sync-endpoint-setup-digital-ocean-firewall>`
|   -	:ref:`Launching the ODK-X Server <sync-endpoint-setup-digital-ocean-launching>`

.. _sync-endpoint-setup-digital-ocean-account:

Setting up a DigitalOcean account
"""""""""""""""""""""""""""""""""""

1. If you haven’t already, create an account on `DigitalOcean <https://www.digitalocean.com>`_.

.. _sync-endpoint-setup-digital-ocean-droplet:

Setting up a Droplet
"""""""""""""""""""""""""""""

1. First, click on the :guilabel:`Create` dropdown button at the top right of the screen. Then, click on :guilabel:`Droplet` to create a droplet cloud server.

  .. image:: /img/setup-digital-ocean/create-droplet.png
   :width: 600

2. In the Distributions tab, on the :guilabel:`Create Droplet` screen; select *18.04 (LTS) x64* under the Ubuntu dropdown. Next, choose a plan and data center region based on your needs.

  .. note::
    Sync Endpoint requires more than *2GB* of space to run, this means that plans below *4GB* will not work.

  .. image:: /img/setup-digital-ocean/do-distribution.png
    :width: 600

  .. image:: /img/setup-digital-ocean/do-plan.png
    :width: 600

3. Scroll down to the :guilabel:`Select additional options`, click on the User data checkbox, copy and paste the contents of the :download:`cloud_init_DO.yml</files/cloud_init_DO.yml>` file in the text area provided.

  .. image:: /img/setup-digital-ocean/do-userdata.png
    :width: 600

  .. image:: /img/setup-digital-ocean/do-userdata2.png
    :width: 600

4. The next step is :guilabel:`Authentication`. There are two authentication types to select from; **SSH Keys** and **Password**. We highly recommend that you use an SSH key for authentication. Copy and paste your SSH key username, and the key itself.

 Use the `following resource <https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/>`_ to learn more about creating an SSH key.

  .. image:: /img/setup-digital-ocean/do-authentication.png
   :width: 600

5. After the authentication is set up, you can choose to name the droplet; then scroll down and click the :guilabel:`Create Droplet` button. This might take a few minutes to set up.

.. _sync-endpoint-setup-digital-ocean-dns:

Setting up a DNS Record
""""""""""""""""""""""""

1. On the resources tab of the main DigitalOcean page, click on the :guilabel:`Droplet` you created.

  .. image:: /img/setup-digital-ocean/do-droplets.png
   :width: 600

2. Obtain the IP address of the droplet you created.

3. Log into your account for your domain name registrar and DNS provider. See :ref:`Acquiring a domain name<sync-endpoint-setup-domain>` for more information and a list of registrars and DNS providers.

4. Add a dns 'A' record for the domain or subdomain you would like to use for the Sync Endpoint with your droplet's IP address.

.. _sync-endpoint-setup-digital-ocean-connecting:

Connecting to your Droplet
"""""""""""""""""""""""""""""

1. On the resources tab of the main DigitalOcean page, click on the :guilabel:`Droplet` you created.

  .. image:: /img/setup-digital-ocean/do-droplets.png
   :width: 600

2. Now, click on the :guilabel:`Console` link in the upper-right corner of the page

  .. image:: /img/setup-digital-ocean/do-console.png
   :width: 600

3. A console window will now open up. If you chose the **password** authentication, you will be asked to enter your username and then asked for a password.

  .. image:: /img/setup-digital-ocean/do-console-terminal.png
   :width: 600

4. Before running our launch scripts, we need to check our logs to ensure that all the packages have been successfully installed, which should take about 2-3 minutes. The droplet may also reboot in this time.

  | Use the following command to get into the log directory.

  .. code-block:: console

    $ cd /var/log

  Now, open the log file with command:

  .. code-block:: console

    $ tail cloud-init-output.log

  If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait and check the log file again.

5. In order to run our launch scripts, we must first navigate back to
   the root directory with the following command:

  .. code-block:: console

    $ cd /root

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ ./script_to_run.sh

  The script will ask you for the server's domain and an
  administration email address to configure https on the server.

  After gathering this data the script will begin the install and you
  should see a bunch of statements executing in your console. Wait
  approximately 5-10 minutes for the installation to complete.

  .. image:: /img/setup-digital-ocean/do5.png
   :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ docker stack ls

  If there are 8 (or 7 without https) services running under the name `syncldap`, everything is running properly.

6. From the **Droplets** section of the console, obtain the IP address of the droplet you created. Now, navigate to https://[IP_ADDRESS]:40000 within your browser in order to access the services screen. It will warn you about your connection not being private but should give you the option to proceed at the bottom.

  .. image:: /img/setup-digital-ocean/do6.png
   :width: 600

  .. image:: /img/setup-digital-ocean/do7.png
   :width: 600

7. If you see the following screen after proceeding, you are good to go!

  .. image:: /img/setup-digital-ocean/do8.png
   :width: 600

8. Read our section on *Creating a Sample User* to learn how to create a user from within the admin interface. This section can be found :ref:`here <sync-endpoint-setup-create-user>`.

.. _sync-endpoint-setup-digital-ocean-firewall:

Enabling a firewall to prevent unintended traffic
"""""""""""""""""""""""""""""""""""""""""""""""""""

1. On the DigitalOcean console, click on the arrow beside the **MANAGE** dropdown and navigate to the *Networking* section. Go to the *Firewalls* section and click :guilabel:`Create Firewall`.

  .. image:: /img/setup-digital-ocean/do-networking.png
   :width: 600

2. Set a name for your firewall and modify the inbound rules to match the inbound rules specified in the picture below (SSH, HTTP, HTTPS and port for admin interface). Attach the firewall to the desired droplet. Leave the outbound rules as-is.

  .. image:: /img/setup-digital-ocean/do10.png
   :width: 600

  .. image:: /img/setup-digital-ocean/do11.png
   :width: 600

3. After going through the instructions for “Creating a Sample User,” we no longer need access to this admin interface anymore. This admin interface is running on port 40000, and in order to ensure that this admin interface is not publicly accessible to anyone, we want to remove the rule that accepts incoming traffic to that port. Go ahead and remove the following rule:

  .. image:: /img/setup-digital-ocean/do12.png
   :width: 600

.. _sync-endpoint-setup-digital-ocean-launching:

Launching the ODK-X Server
"""""""""""""""""""""""""""""

1. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

  .. image:: /img/setup-digital-ocean/do13.png
   :width: 600

  Once a user has been created in the admin interface, this is the login screen that the user will use to log in and access their data.

.. _sync-endpoint-setup-azure:

Option 2: Azure console
-------------------------

| We have noticed that sync-endpoint runs the smoothest on Azure. These instructions will walk you through the following:
| -	:ref:`Setting up an Azure account <sync-endpoint-setup-azure-account>`
| -	:ref:`Setting up a virtual machine <sync-endpoint-setup-azure-vm>`
| -	:ref:`Setting up a DNS record <sync-endpoint-setup-azure-dns>`
| -	:ref:`Connecting to your virtual machine <sync-endpoint-setup-azure-connect>`
| -	:ref:`Launching the ODK-X Server <sync-endpoint-setup-azure-launch>`

.. _sync-endpoint-setup-azure-account:

Setting up an Azure account
"""""""""""""""""""""""""""""

1. If you haven’t already, create an account on `Azure <https://azure.microsoft.com/en-us/>`_.

.. _sync-endpoint-setup-azure-vm:

Setting up a virtual machine
""""""""""""""""""""""""""""

1. First, click on the :guilabel:`Virtual Machines` button underneath the **Azure Services** section on the portal. Then, click on :guilabel:`Create` to create a new virtual machine.

  .. image:: /img/setup-azure/azure1.png
   :width: 600

  .. image:: /img/setup-azure/azure2.png
   :width: 600

  .. image:: /img/setup-azure/azure3.png
   :width: 600

2. Create a new resource group to attach to this virtual machine by clicking on :guilabel:`Create new`. Additionally, enter a name for the virtual machine and make sure that *Ubuntu Server 18.04 LTS* is selected for the image name as Ubuntu Server 20.04 LTS has not been tested yet.

  .. image:: /img/setup-azure/azure4.png
    :width: 600

3. Scroll down and select your authentication type. We highly recommend that use an SSH key for authentication. Copy and paste your SSH key username, and the key itself.

  Use the `following resource <https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/>`_ to learn more about creating an SSH key.

  Alternatively, Azure now provides an option to automatically generate an SSH key pair (As highlighted in the figure below). This key .pem file can then be directly downloaded to the user's computer for future use to connect to the virtual machine.

  .. image:: /img/setup-azure/azure5.png
    :width: 600

4. Click the **Advanced** tab at the top and copy and paste the contents from the :download:`cloud_init_AZURE.yml </files/cloud_init_AZURE.yml>` file into the *Custom data* box. Finally, click :guilabel:`Review + create` to actually create the machine.
If you had generated the SSH key pair through azure automatic generate key pair option, then it now gives you a prompt to download the key (.pem) file. It is important to download it and remember the path to this file in your computer for connecting to virtual machine later.

  .. image:: /img/setup-azure/azure6.png
    :width: 600

5. In order to modify the firewall settings and change the type of incoming traffic we want to allow, we need to modify the **Networking** settings of our VM. Navigate to this section and then add an inbound security rule that matches the rule below. Leave the outbound rules as-is.

  .. image:: /img/setup-azure/azure7.png
    :width: 600

.. _sync-endpoint-setup-azure-dns:

Setting up a DNS Record
"""""""""""""""""""""""

1. Within the Virtual Machine overview section, locate the IP address
   of your machine.

  .. image:: /img/setup-azure/azure8.png
    :width: 600

2. Log into your account for your domain name registrar and DNS
   provider. See :ref:`Acquiring a domain
   name<sync-endpoint-setup-domain>` for more information and a list
   of registrars and DNS providers.

3. Add a dns 'A' record for the domain or subdomain you would like to
   use for the Sync Endpoint with your droplet's IP address.


.. _sync-endpoint-setup-azure-connect:

Connecting to your virtual machine
""""""""""""""""""""""""""""""""""

1. Within the Virtual Machine overview section, locate the IP address of your machine.

  .. image:: /img/setup-azure/azure8.png
    :width: 600

2. Open up a terminal window and enter the command

  .. code-block:: console

    $ ssh -i PATH_TO_PRIVATE_KEY USERNAME@IP_ADDRESS

  The first parameter represents the *path to your private key* you used for SSH authentication (in case of automatic generation through azure, it is the path of the key pair .pem file downloaded earlier in your computer), the second parameter *the username* you used for SSH authentication, and the final parameter *the IP address* of the virtual machine.

3. Before running our launch scripts, we need to check our logs to ensure that all the packages have been successfully installed, which should take about 2-3 minutes. The virtual machine may also reboot in this time.

  | Use the following command to get into the log directory.

  .. code-block:: console

    $ cd /var/log

  Now, open the log file with command:

  .. code-block:: console

    $ tail cloud-init-output.log

  If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait and check the log again.

4. In order to run our launch scripts, we must first navigate back to
   the home directory with the following command:

  .. code-block:: console

    $ cd /home

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ sudo ./script_to_run.sh

  The script will ask you for the server's domain and some questions (as shown in the picture below) along with an administration email address to configure https on the server.

  .. image:: /img/setup-azure/azure-connecting-to-virtual-machine1.png
    :width: 600

  After gathering this data the script will begin the install and you should see a bunch of statements executing in your console. Wait approximately 5-10 minutes for the installation to complete.

  .. image:: /img/setup-azure/azure9.png
    :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ sudo docker stack ls

  To see all of the Docker processes/containers that are actively running, use the following command:

  .. code-block:: console

    $ sudo docker ps

  .. image:: /img/setup-azure/azure-connecting-to-virtual-machine2.png
    :width: 600

  If there are 9 (or 8 without https) services running under the name
  `syncldap`, everything is running properly. The following command shows all (both stopped and running) containers/processes:

  .. code-block:: console

    $ sudo docker ps -a

  .. image:: /img/setup-azure/azure-connecting-to-virtual-machine3.png
    :width: 600

5. After obtaining the IP address of the virtual machine you created, navigate to https://[IP_ADDRESS]:40000 within your browser in order to access the services screen. It will warn you about your connection not being private but should give you the option to proceed at the bottom.

  .. image:: /img/setup-azure/azure10.png
   :width: 600

6. If you see the following screen after proceeding, you are good to go!

  .. image:: /img/setup-azure/azure11.png
   :width: 600

7. Read our section on *Creating a Sample User* to learn how to create a user from within the admin interface. This section can be found :ref:`here <sync-endpoint-setup-create-user>`.

|

8. After going through the instructions for *Creating a Sample User,* we no longer need access to this admin interface anymore. This admin interface is running on port 40000, and in order to ensure that this admin interface is not publicly accessible to anyone, we want to remove the rule that accepts incoming traffic to that port. We do this the same way we added the rules above.

.. _sync-endpoint-setup-azure-launch:

Launching the ODK-X Server
"""""""""""""""""""""""""""""

1. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

  .. image:: /img/setup-azure/azure12.png
   :width: 600

  Once a user has been created in the admin interface, this is the login screen that the user will use to log in and access their data.


.. _sync-endpoint-setup-aws:

Option 3: Amazon Web Services console
---------------------------------------

| These instructions will walk you through the following:
| -	:ref:`Setting up an AWS account <sync-endpoint-setup-aws-account>`
| -	:ref:`Setting up a virtual machine <sync-endpoint-setup-aws-vm>`
| -	:ref:`Setting up a DNS record <sync-endpoint-setup-aws-dns>`
| -	:ref:`Connecting to your virtual machine <sync-endpoint-setup-aws-connect>`
| -	:ref:`Launching the ODK-X Server <sync-endpoint-setup-aws-launch>`

.. _sync-endpoint-setup-aws-account:

Setting up an AWS account
"""""""""""""""""""""""""""""

1. If you haven’t already, create an account on `Amazon Web Services <https://aws.amazon.com/>`_.

.. _sync-endpoint-setup-aws-vm:

Setting up a virtual machine
"""""""""""""""""""""""""""""

1. First, click on :guilabel:`EC2` link under the **COMPUTE** section. Then, go ahead and launch a new instance.

  .. image:: /img/setup-aws/aws1.png
   :width: 600

  .. image:: /img/setup-aws/aws2.png
   :width: 600

2. You must start by choosing an Amazon Machine Image (AMI). Scroll through the options and select *Ubuntu Server 18.04 LTS (HVM), SSD Volume Type* which should be the fifth option from the top.

  .. image:: /img/setup-aws/aws3.png
   :width: 600

3. Skip the “Choose an Instance Type” step. Instead, click on the :guilabel:`3: Configure Instance` tab at the top and then attach the :download:`cloud_init_AWS.yml</files/cloud_init_AWS.yml>` file we provided within the **User data** section under “Advanced Details.”

|

4. Click on the :guilabel:`6. Configure Security Group` tab in order to modify the firewall rules and control the traffic for the instance. Create a new security group and modify the rules to match the rules specified below, then click :guilabel:`Review and Launch`.

  .. image:: /img/setup-aws/aws4.png
   :width: 600

5. Review the Instance Launch and then click :guilabel:`Launch`. Now, create a new key pair to access your instance via SSH and make sure to download it to a secure location. Finally, click :guilabel:`Launch Instances`!

  .. image:: /img/setup-aws/aws5.png
   :width: 600

.. _sync-endpoint-setup-aws-dns:

Setting up a DNS Record
"""""""""""""""""""""""

1. From the EC2 dashboard and click on :guilabel:`Running instances`.

  .. image:: /img/setup-aws/aws6.png
   :width: 600

2. Select the instance you just created, and obtain its public IP address.

3. Log into your account for your domain name registrar and DNS provider. See :ref:`Acquiring a domain name<sync-endpoint-setup-domain>` for more information and a list of registrars and DNS providers.

4. Add a dns 'A' record for the domain or subdomain you would like to use for the Sync Endpoint with your droplet's IP address.


.. _sync-endpoint-setup-aws-connect:

Connecting to your virtual machine
""""""""""""""""""""""""""""""""""""

1. Go back to the EC2 dashboard and click on :guilabel:`Running instances`.

  .. image:: /img/setup-aws/aws6.png
   :width: 600

2. Select the instance that you want to connect to and then click :guilabel:`Connect`.

  .. image:: /img/setup-aws/aws7.png
   :width: 600

3. Open up a terminal window and enter the following command to change key permissions.

  .. code-block:: console

    $ chmod 400 KEY_NAME.pem

  Now, use the following command in order to SSH into your virtual machine.

  .. image:: /img/setup-aws/aws8.png
   :width: 600

  .. code-block:: console

    $ ssh -i “KEY_NAME.pem” PUBLIC_DNS

4. Before running our launch scripts, we need to check our logs to ensure that all the packages have been successfully installed, which should take about 2-3 minutes. The virtual machine may also reboot in this time.

  | Use the following command to get into the log directory.

  .. code-block:: console

    $ cd /var/log

  Now, open the log file with command:

  .. code-block:: console

    $ tail cloud-init-output.log

  If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait and check the log again.

5. In order to run our launch scripts, we must first navigate back to the Ubuntu directory with the following command:

  .. code-block:: console

    $ cd /home/ubuntu

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ sudo ./script_to_run.sh

  The script will ask you for the server's domain and an administration email address to configure https on the server.

  After gathering this data the script will begin the install and you should see a bunch of statements executing in your console. Wait approximately 5-10 minutes for the installation to complete.

  .. image:: /img/setup-aws/aws9.png
    :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ docker stack ls

  If there are 8 (or 7 without https) services running under the name
  `syncldap`, everything is running properly.

6. After obtaining the IP address of the virtual machine you created, navigate to https://[IP_ADDRESS]:40000 within your browser in order to access the services screen. It will warn you about your connection not being private but should give you the option to proceed at the bottom.

  .. image:: /img/setup-aws/aws10.png
   :width: 600

7. If you see the following screen after proceeding, you are good to go!

  .. image:: /img/setup-aws/aws11.png
   :width: 600

8. Read our section on *Creating a Sample User* to learn how to create a user from within the admin interface. This section can be found :ref:`here <sync-endpoint-setup-create-user>`.

|

9. After going through the instructions for *Creating a Sample User,* we no longer need access to this admin interface anymore. This admin interface is running on port 40000, and in order to ensure that this admin interface is not publicly accessible to anyone, we want to remove the rule that accepts incoming traffic to that port. We do this the same way we added the rules above.

.. _sync-endpoint-setup-aws-launch:

Launching the ODK-X Server
"""""""""""""""""""""""""""""

1. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

  .. image:: /img/setup-azure/azure11.png
   :width: 600

.. note::
    If you are unable to log in, you may need to take the docker stack down and bring it back up again. That can be done with the following commands below:

.. code-block:: console

    $ docker stack rm syncldap

.. code-block:: console

    $ docker stack deploy -c /root/sync-endpoint-default-setup/docker-compose.yml syncldap

.. _sync-anonymous-cloud:

Anonymous Access for ODK-X Sync Endpoint Cloud
----------------------------------------------
To Enable or Disable Anonymous User Access for your ODK-X Sync Endpoint follow :ref:`these instructions <sync-anonymous>`.
