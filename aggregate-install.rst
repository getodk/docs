***********************************
Aggregate Installation and Setup
***********************************

Before going through this section, make sure you have used :doc:`ODK Collect  <collect-intro>` and are familiar with how it works.

.. tip::

  - Try the ODK Aggregate `demo server <https://opendatakit.appspot.com>`_ to explore the core functionality.
  - Decide whether to install a cloud instance or a local instance. It is strongly recommended to try an App Engine cloud instance first. If you wish to host locally, see :ref:`Aggregate Deployment Planning <deployment-planning>`
  - Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility.    
  - You must also plan for the security of your data and systems. And finally, it requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer-technical-support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.

  
Install options
==================

.. toctree::
  aggregate-app-engine
  aggregate-tomcat  
  
.. _install-vm:

Installing VM (Local or Cloud)
-------------------------------

- The `ODK Aggregate VM <https://gumroad.com/l/odk-aggregate-vm>`_ is a fully-configured install of Aggregate that you can run on any computer. It requires very little setup, works well without Internet connectivity, and gives you complete control over your data collection campaign.


.. _install-aws:

Installing on AWS (Cloud)
--------------------------

Following are basic details for setting up ODK Aggregate to run on a Linux micro-instance on the Amazon Web Services EC2 infrastructure.

- First, sign up for Amazon Web Services EC2 at http://aws.amazon.com/ec2/.
- Go to the AWS/EC2 management console and note your region (shown in the upper-left).
- Launch a new instance with the Launch Instance button prominently displayed on the EC2 console home screen. Accept the default behavior and use the quick-launch wizard.

	- For the launch configuration, choose the :guilabel:`Amazon Linux AMI: EBS-Backed (64-bit)` option. (The exact AMI name and ID will depend on your region.) This is one of the instance types that you can run on a micro-instance as part of their free tier http://aws.amazon.com/free/.
	- Leave everything else at the defaults, including the instance type. The instance type will default to `t2.micro` which is a small, limited instance that can be run for free. For a price, you can upgrade the instance type later if you need better performance.
	- Create a new key pair, download the private key, and keep the private key safe. This will be your only method of communicating with your new instance and you will not be allowed to download it again.

- After creating the instance, add security rules for allowing both HTTP and HTTPS.
	- Choose the Security Groups tab and click on the auto-created security group associated with your new instance. (This might have been called *launch-wizard-1*. If you’re not sure, you can go to the Instances tab to see which Security Group is listed for the new instance.)
	- In the properties pane at the bottom, click to the Inbound tab, select HTTP from the :guilabel:`create a new rule` drop-down, then click :guilabel:`Add Rule`. Do the same for HTTPS. Then click :guilabel:`Apply Rule Changes`.
	- To avoid potential problems with MTU settings and packet loss, also add a rule to allow *All ICMP*. After you create the new rule, click :guilabel:`Apply Rule Changes`.

- Switch to the Instances tab, click on your instance, and note its Public DNS Address in the properties pane below. This is the default address that you will use to access your instance.
- Presuming that you want a friendlier way to access your instance, allocate it an *elastic IP* and domain name.
	
	- Navigate to Elastic IPs and click :guilabel:`Allocate New Address`. Associate it with your new instance.
	- Note that the IP is free so long as you keep it associated with a running instance. If you stop your instance and do not release the IP address for others to use (in essence, wasting it), then Amazon will begin charging you for holding the unused address.
	- Note your new IP. Also, if possible, configure DNS to route one or more names to this address. You can then use this IP and/or name to access your instance (and can forget the *Public DNS Address* assigned by AWS).

- Connect to your instance.
	
	- Go to the :guilabel:`Instances` tab and select :guilabel:`Connect` from the Instance Actions drop-down.
	- The easiest is to connect using their Java SSH client. If you choose that option, you just have to specify the location of your private key file (created above) and AWS launches an in-browser SSH client to connect to your instance.
	- Once you connect, you will probably be told that there are new security updates to install. You can run *sudo yum update* to install these updates, as it advises.

- Transferring files to/from your instance.
	
	- When you login via ssh, you will default to being in the (empty) ec2-user home directory. You will want to be able to transfer files between here and your local directory. You have several options.
	- f you’re using the command-line ssh, you can also use the command-line scp to copy files. The syntax is similar to ssh, but of course you also need to specify the source and destination file paths.
	- An easier option is to use an FTP program like FileZilla (as long as it supports SFTP).
	- To configure FileZilla to connect to your instance, go into *Edit…Settings/Preferences…Connection…SFTP* and add your private key to FileZilla’s keystore (it will offer to convert the key format, which you should accept). Then, go into Site Manager and create a new site. The host should be the IP, name, or Public DNS for your instance, the port can be blank, the protocol should be *SFTP – SSH File Transfer Protocol*, the login type should be Normal, and the user should be *ec2-user*. Everything else should be left at the defaults, including the password (which will be blank).

- Install Tomcat 8 

 This can be done by simply running:

  .. code-block:: console
	
	$ sudo yum install tomcat8

- Configure Tomcat

	- Download the MySQL Connector/J from the MySQL download site <http://dev.mysql.com/downloads/connector/j/>_, unzip it, and transfer the :file:`mysql‐connector‐java‐x.x.x‐bin.jar` file up to your instance’s :file:`/usr/share/tomcat8/lib` directory.
	- Edit :file:`/etc/tomcat8/server.xml` in order to customize settings. (If you’re not used to Linux text editors, you can always download the file, edit it, and upload it back.)
	- Assuming that you want to run Aggregate on the standard HTTP port (80) and HTTPS port (443):
	- Change “<Connector port="8080" protocol="HTTP/1.1"” to “<Connector port="8080" proxyPort="80" protocol="HTTP/1.1"” (i.e., add the proxyPort attribute).
	- If you are using SSL, also change “<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"” to “<Connector port="8443" proxyPort="443" protocol="HTTP/1.1" SSLEnabled="true"”.
	- Execute the following commands to have Linux forward to the ports on which Tomcat listens:
		
		.. code-block:: console

		 $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
		 $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8443
		 $ sudo /sbin/service iptables save 

	- If you have an SSL certificate for HTTPS support

		- Make sure that the “<Connector port="8443"” part of the configuration file is not commented out. If it is, un-comment it.
		- Upload your SSL keystore file and the certificate(s) to the server.
		- Install it as instructed. (If you buy from RapidSSL, for example, they provide you with Tomcat installation instructions. E.g., you may need to download a special P7S certificate file, then install it on the server with “keytool -import -alias YOURALIAS -trustcacerts -file xxxxx.p7s -keystore xxxxx.keystore”).
		- In the “<Connector port="8443"” part of the configuration file, specify the location of your keystore file and password (e.g., "keystoreFile="/…/xxxxx.keystore" keystorePass="changeit"”).		

	
	- Start Tomcat

	  This can be done simply running:

	   .. code-block:: console

	     $ sudo service tomcat8 start

 
	- Configure Tomcat to auto-start when the instance boots with `sudo chkconfig --level 345 tomcat8 on`.   
		     


- Install MySQL

  This can be done by simply running:

   .. code-block:: console
	
	 $ sudo yum install mysql mysql-server


- Configure MySQL

  Use vi or an editor to edit :file:`/etc/my.cnf` (e.g., "sudo vi /etc/my.cnf"). In the [mysqld] section, add (the max_allowed_packet allows up to a 4GB file attachment):

    .. code-block:: none

        character_set_server=utf8
        collation_server=utf8_unicode_ci
        max_allowed_packet=1073741824

- Run MySQL

  To run MySQL:

   .. code-block:: console
	
	 $ sudo service mysqld start

- Install and transfer ODK Aggregate files.
	
	- First, install `ODK Aggregate <https://opendatakit.org/downloads/>`_ on your local computer (not on your AWS instance).
	- During set-up, it’s important to specify that this will be a MySQL installation, and it is also very important that you specify the correct domain name or IP address that will be used to access your Aggregate server. Ideally, this will be a specific domain name that you have already mapped to an elastic IP (and can re-map later if you change the IP).
	- The installation will create a :file:`create_db_and_user.sql` file. Upload this to your ec2-user home directory. 
	- The installation will also create an ODKAggregate.war file. Rename this to ROOT.war and upload it to the :file:`/usr/share/tomcat8/webapps` folder. If you receive a `Permission Denied` error, you might need to execute `chmod -R 755` or something similar for the webapps folder.
	- After ROOT.war has been copied to the server, you need to make sure tomcat has permission to use it. Run *sudo chown tomcat ROOT.war* and *sudo chgrp tomcat ROOT.war* in the webapps directory to ensure this is the case.

- Configure MySQL

	- On your AWS instance, run */usr/bin/mysql_secure_installation* to set a root password and generally secure your MySQL installation.
	- Then, run *mysql –u root -p* to log in to MySQL (specifying the password you just set), and type *source ~/create_db_and_user.sql*. This will create the ODK user and database. Type *quit* on the mysql prompt to quit from MySQL.
	- Finally, run *sudo /sbin/chkconfig --levels 235 mysqld on* to auto-start MySQL whenever your instance boots up.


- Login and test.
	
	- At this point, you should be able to login to your AWS-hosted Aggregate instance by going to its name or IP in your web browser (with or without HTTPS, depending on your set-up).
	- For your first login, you will need to login with the Google account you specified during the Aggregate installation process. Then you can add additional users from the Site Admin tab.

- Once you have confirmed that your Aggregate instance is working, you can back it up by creating an image of the instance (an AMI). You can do this by going to the Instances tab in the AWS-EC2 console, then selecting the :guilabel:`Create Image (EBS AMI)` Instance Action for your instance.

For screenshots and more on the general set-up of Tomcat on AWS, see the excellent three-part *Cat in the Cloud: Apache Tomcat in Amazon EC2* series at http://www.excelsior-usa.com/articles/tomcat-amazon-ec2-basic.html. Amazon’s getting-started guides are also quite helpful: http://aws.amazon.com/documentation/gettingstarted/.



