.. spelling::
  phpLDAPadmin
  readonly

Setup using Cloud Services
===========================

.. _sync-endpoint-setup-intro:

This tutorial will help you launch ODK Sync Endpoint on a virtual machine hosted on a cloud service provider.  ODK Sync Endpoint communicates with your ODK-X Android applications in order to synchronize your data and application files.  

| There are 3 main options that we have documented to set up ODK-X Sync Endpoint
| :program:`Easiest (recommended, especially for Windows machines)`
|   :ref:`1.  Using our Python script to automatically set up Virtual Machine on DigitalOcean <sync-endpoint-setup-digital-ocean>`
| :program:`More customization, setting up Virtual Machine using:`
|   :ref:`2.	Azure console <sync-endpoint-setup-azure>`
|   :ref:`3.	Amazon Web Services console <sync-endpoint-setup-aws>`


.. _sync-endpoint-setup-digital-ocean:

Option 1: Using Python script to automatically set up a virtual machine on DigitalOcean
-----------------------------------------------------------------------------------------

| If you'd like to set up an ODK server that's accessible from anywhere via the Internet, DigitalOcean provides a one-click configuration that's nicely geared with nearly all the tools you'll need to set up your new server. The only thing it doesn't do is register a domain name, which you will have to do in order to obtain a security certificate for your server. These instructions walk you through:
|   -	:ref:`Setting up a DigitalOcean account <sync-endpoint-setup-digital-ocean-account>`
|   -	:ref:`Setting up a Droplet, DigitalOcean’s name for a server you can access and manage <sync-endpoint-setup-digital-ocean-droplet>`
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

1. Use the `following link <https://www.python.org/downloads/>`_ in order to install the latest version of Python 3.0. Ensure that you are specifically installing an iteration of Python 3.0, as Python 2.0 will soon be deprecated. The installer should take about a minute to run.

  .. note::
    If using Windows, make sure to download the Windows version of Python instead.

2. Open a terminal or command line. Install module to manage DigitalOcean droplets, using command:

  .. code-block:: console
    
      $ pip3 install -U python-digitalocean

  .. note::
    Windows users also have the option of either using PuTTY_, a free SSH client, in order to install the DigitalOcean module with pip. In the case that pip is not installed, Windows users can instead refer to the installation instructions from the following_ link and run the :file:`setup.py` file to install the module instead.

  .. _PuTTY: https://www.chiark.greenend.org.uk/~sgtatham/putty/

  .. _following: https://github.com/koalalorenzo/python-digitalocean#how-to-install


3. Generate API token by logging into DigitalOcean console and clicking on :guilabel:`API` under the **MANAGE** section. Now, click on :guilabel:`Generate New Token` and enter a name. 

  .. image:: /img/setup-digital-ocean/do1.png
   :width: 600

4. Download the following :download:`pyscript_DO.py</files/pyscript_DO.py>` and :download:`cloud_init_DO.yml</files/cloud_init_DO.yml>` files we have provided and ensure that they are located in the same directory. Switch to that directory and run the following command in order to set up your droplet:

  .. code-block:: console

    $ python3 pyscript_DO.py [TOKEN] [NAME] [LOCATION]

  | **[TOKEN]** represents the token we obtained from step 3.
  | **[NAME]** represents the name that we want to give to our droplet. 
  | **[LOCATION]** represents the desired data center location, and those codes can be found `here <https://www.digitalocean.com/docs/platform/availability-matrix/>`_.


.. _sync-endpoint-setup-digital-ocean-connecting:

Connecting to your Droplet
"""""""""""""""""""""""""""""

1. From the DigitalOcean console, click on :guilabel:`Droplets` under the **MANAGE** section. 

  .. image:: /img/setup-digital-ocean/do2.png
   :width: 600

2. Now, select your droplet and click on the :guilabel:`Console` link in the upper-right.

  .. image:: /img/setup-digital-ocean/do3.png
   :width: 600
   
3. A console window will now open up. Enter your username and then you will be asked for a password. These credentials will be sent to the email associated with your DigitalOcean account. You will also be required to change the root password once you log in. 

  .. note::
    Occasionally, Control + V may not work to paste the password, so you may have to right click and select paste. 

  .. image:: /img/setup-digital-ocean/do4.png
   :width: 600

4. Before running our launch scripts, we need to check our logs to ensure that all the packages have been successfully installed, which should take about 2-3 minutes. The droplet may also reboot in this time. 

  | Use the following command to get into the log directory. 

  .. code-block:: console

    $ cd /var/log

  Now, open the log file with command:

  .. code-block:: console

    $ vi cloud-init-output.log
  
  Click :guilabel:`SHIFT + G` to scroll to the very end of the file. If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait. 

5. Use *“:q!”* to now get out of the log file. In order to run our launch scripts, we must first navigate back to the root directory with the following command:

  .. code-block:: console

    $ cd /root

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ ./script_to_run.sh

  You should see a bunch of statements executing in your console. Wait approximately 5-10 minutes. 

  .. image:: /img/setup-digital-ocean/do5.png
   :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ docker stack ls
  
  If there are 7 services running under the name `syncldap`, everything is running properly. 

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

1. On the DigitalOcean console, navigate to the *Networking* section under **MANAGE** Go to the *Firewalls* section and click :guilabel:`Create Firewall`.

  .. image:: /img/setup-digital-ocean/do9.png
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
| -	:ref:`Connecting to your virtual machine <sync-endpoint-setup-azure-connect>`
| -	:ref:`Launching the ODK-X Server <sync-endpoint-setup-azure-launch>`

.. _sync-endpoint-setup-azure-account:

Setting up an Azure account
"""""""""""""""""""""""""""""

1. If you haven’t already, create an account on `Azure <https://azure.microsoft.com/en-us/>`_.

.. _sync-endpoint-setup-azure-vm:

Setting up a virtual machine
"""""""""""""""""""""""""""""

1. First, click on the :guilabel:`Virtual Machines` button underneath the **Azure Services** section on the portal. Then, click on :guilabel:`Add` to create a new virtual machine. 

  .. image:: /img/setup-azure/azure1.png
   :width: 600
  
  .. image:: /img/setup-azure/azure2.png
   :width: 600

2. Create a new resource group to attach to this virtual machine by clicking on :guilabel:`Create new`. Additionally, enter a name for the virtual machine and make sure that *Ubuntu Server 18.04 LTS* is selected for the image name. 

  .. image:: /img/setup-azure/azure3.png
    :width: 600

3. Scroll down and select your authentication type. We highly recommend that use an SSH key for authentication. Copy and paste your SSH key username, and the key itself. 

  Use the `following resource <https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/>`_ to learn more about creating an SSH key.

  .. image:: /img/setup-azure/azure4.png
    :width: 600

4. Click the **Advanced** tab at the top and copy and paste the contents from the :download:`cloud_init_AZURE.yml </files/cloud_init_AZURE.yml>` file into the *Cloud init* box. Finally, click :guilabel:`Review + create` to actually create the machine.

  .. image:: /img/setup-azure/azure5.png
    :width: 600

5. In order to modify the firewall settings and change the type of incoming traffic we want to allow, we need to modify the **Networking** settings of our VM. Navigate to this section and then add an inbound security rule that matches the rule below. Leave the outbound rules as-is. 

  .. image:: /img/setup-azure/azure6.png
    :width: 600

.. _sync-endpoint-setup-azure-connect:

Connecting to your virtual machine
""""""""""""""""""""""""""""""""""""

1. Within the Virtual Machine overview section, locate the IP address of your machine. 

  .. image:: /img/setup-azure/azure7.png
    :width: 600

2. Open up a terminal window and enter the command 

  .. code-block:: console

    $ ssh -i PATH_TO_PRIVATE_KEY USERNAME@IP_ADDRESS

  The first parameter represents the *path to your private key* you used for SSH authentication, the second parameter *the username* you used for SSH authentication, and the final parameter *the IP address* of the virtual machine. 

3. Before running our launch scripts, we need to check our logs to ensure that all the packages have been successfully installed, which should take about 2-3 minutes. The virtual machine may also reboot in this time. 

  | Use the following command to get into the log directory. 

  .. code-block:: console

    $ cd /var/log

  Now, open the log file with command:

  .. code-block:: console

    $ vi cloud-init-output.log
  
  Click :guilabel:`SHIFT + G` to scroll to the very end of the file. If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait. 

4. Use *“:q!”* to now get out of the log file. In order to run our launch scripts, we must first navigate back to the home directory with the following command:

  .. code-block:: console

    $ cd /home

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ sudo ./script_to_run.sh

  You should see a bunch of statements executing in your console. Wait approximately 5-10 minutes. 

  .. image:: /img/setup-azure/azure8.png
    :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ docker stack ls
  
  If there are 7 services running under the name `syncldap`, everything is running properly. 

5. After obtaining the IP address of the virtual machine you created, navigate to https://[IP_ADDRESS]:40000 within your browser in order to access the services screen. It will warn you about your connection not being private but should give you the option to proceed at the bottom. 

  .. image:: /img/setup-azure/azure9.png
   :width: 600

6. If you see the following screen after proceeding, you are good to go!

  .. image:: /img/setup-azure/azure10.png
   :width: 600

7. Read our section on *Creating a Sample User* to learn how to create a user from within the admin interface. This section can be found :ref:`here <sync-endpoint-setup-create-user>`.

|

8. After going through the instructions for *Creating a Sample User,* we no longer need access to this admin interface anymore. This admin interface is running on port 40000, and in order to ensure that this admin interface is not publicly accessible to anyone, we want to remove the rule that accepts incoming traffic to that port. We do this the same way we added the rules above. 

.. _sync-endpoint-setup-azure-launch:

Launching the ODK-X Server
"""""""""""""""""""""""""""""

1. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

  .. image:: /img/setup-azure/azure11.png
   :width: 600

  Once a user has been created in the admin interface, this is the login screen that the user will use to log in and access their data. 


.. _sync-endpoint-setup-aws:

Option 3: Amazon Web Services console
---------------------------------------

| These instructions will walk you through the following:
| -	:ref:`Setting up an AWS account <sync-endpoint-setup-aws-account>`
| -	:ref:`Setting up a virtual machine <sync-endpoint-setup-aws-vm>`
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

2. You must start by choosing an Amazon Machine Image (AMI). Scroll through the options and select *Ubuntu Server 18.04 LTS (HVM), SSD Volume Type* which should be the 5th option from the top.  

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

    $ vi cloud-init-output.log
  
  Click :guilabel:`SHIFT + G` to scroll to the very end of the file. If you see the message **“The system is finally up, after X seconds”** you can proceed to the next step! Otherwise, continue to wait. 

5. Use *“:q!”* to now get out of the log file. In order to run our launch scripts, we must first navigate back to the Ubuntu directory with the following command:

  .. code-block:: console

    $ cd /home/ubuntu

  Now, we can run our build scripts with the command:

  .. code-block:: console

    $ sudo ./script_to_run.sh

  You should see a bunch of statements executing in your console. Wait approximately 5-10 minutes. 

  .. image:: /img/setup-aws/aws9.png
    :width: 600

  Once all the services have been created, we need to check if all the services are running properly with the command:

  .. code-block:: console

    $ docker stack ls
  
  If there are 7 services running under the name `syncldap`, everything is running properly. 

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

  Once a user has been created in the admin interface, this is the login screen that the user will use to log in and access their data. 

.. _sync-endpoint-setup-create-user:

Creating a Sample User
----------------------

| 1. Start by logging into the ldap-service. Copy the login below. 
|   - login DN: :guilabel:`cn=admin,dc=example,dc=org`
|   - password: :guilabel:`admin`

    .. image:: /img/setup-create-user/setup-user1.png
      :width: 600

2. Click the :guilabel:`+` sign next to **dc=example, dc=org** to expand it. Within the unfolded menu, in the **ou=people** section, click on :guilabel:`Create a child entry` (new person). 

  .. image:: /img/setup-create-user/setup-user2.png
    :width: 600

3. Then, select the :guilabel:`Generic: User Account` template. 

  .. image:: /img/setup-create-user/setup-user3.png
    :width: 600

4. Fill out information for the new user and “create object.” Assign it to the *default_prefix_synchronize_tables* group. Will need to commit (confirm) that you want to create this entry on the next screen. 

  .. image:: /img/setup-create-user/setup-user4.png
    :width: 600

  We have now created the user! We just need to add the user to the respective group from the group settings. 

5. Click the :guilabel:`+` sign next **ou=groups** to expand it. Within the unfolded menu, in the **ou=default_prefix** section, click on :guilabel:`gidNumber=503`, which is the group ID that corresponds to *default_prefix_synchronize_tables*. Groups correspond to the access permissions available to a certain user. 

  .. image:: /img/setup-create-user/setup-user5.png
    :width: 600

6. Click on :guilabel:`Add new attribute` which should show a pull-down menu and then select :guilabel:`memberUid`. Enter the `memberUid` of the user you just created, and then update the object.

  .. image:: /img/setup-create-user/setup-user6.png
    :width: 600
  
  .. image:: /img/setup-create-user/setup-user7.png
    :width: 600

7. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

  .. image:: /img/setup-create-user/setup-user8.png
    :width: 600

  .. note::
    If you are unable to log in, you may need to take the docker stack down and bring it back up again. That can be done with the following commands below:

  .. code-block:: console

    $ docker stack rm syncldap

  .. code-block:: console

    $ docker stack deploy -c /root/sync-endpoint-default-setup/docker-compose.yml syncldap


