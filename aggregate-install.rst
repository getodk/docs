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
  
  
.. _install-vm:

Installing VM (Local or Cloud)
-------------------------------

- The `ODK Aggregate VM <https://gumroad.com/l/odk-aggregate-vm>`_ is a fully-configured install of Aggregate that you can run on any computer. It requires very little setup, works well without Internet connectivity, and gives you complete control over your data collection campaign.

.. _install-tomcat:

Installing on Tomcat (Local or Cloud)
--------------------------------------

To run on ODK Aggregate on a Tomcat server backed with a MySQL or PostgreSQL database follow the following steps:

- Define your server requirements and install your server.
   
   - **Availability**: Decide the availability of your server depending on how frequently you want to update and upload forms. If you do need a high-availability server, you need to talk to your Internet Service Provider (ISP) as to their availability guarantees.
   - **Data Loss**: Your tolerance to data loss will impact your backup schedule and your server hardware.  Invest in a storage system based on your tolerance to data loss. Seek technical assistance for these requirements. If you cannot tolerate any data loss, or less than 24 hours of data loss, you should invest in a RAID storage array with battery-backed controller cards. If you can tolerate a day or longer interval of data loss, be sure you have a periodic tape or other means of backup for your system that matches or is shorter than the data loss interval.
   - **Dataset Size**: The quantity of data you intend to collect will affect the size of the machine required to host the ODK Aggregate instance and of your database server. For most applications, the default size should be fine. If you are collecting more than 6000 submissions, you may need to increase the JVM size. Note that the maximum size of the JVM is limited by the size of the physical memory on your machine.
   - **Secure and Protected Data**: If you need to prevent eavesdroppers from seeing your data as it is transmitted to your ODK Aggregate instance, you should either (1) only connect to ODK Aggregate from within your organization's network (when the ODK Collect devices are on your premises), (2) obtain an SSL certificate and install it on your Tomcat server (a certificate is required to secure transmissions over https:), or (3) use `Encrypted Forms <https://opendatakit.org/help/encrypted-forms/>`_. If you are not using encrypted forms and are handling sensitive data, a computer security specialist should review your system and your security procedures. When operating without an SSL certificate, do not access ODK Aggregate from a remote location when changing passwords.

- Install Tomcat on your server.

    - Install `Java 8 <https://java.com/en/download/>`_ or higher on your system.

    .. note::

        You generally need to launch installers with Run as administrator privileges (available under the right-click menu). Accept all the defaults.

    - Add the installed Java bin directory to the `PATH variable <https://docs.oracle.com/javase/tutorial/essential/environment/paths.html>`_.
    - Download and install `Tomcat 8 <https://tomcat.apache.org/download-80.cgi>`_

    .. tip::

     - If using the Windows installer, change to use port 80 for the HTTP/1.1 port. If you are going to set up an SSL certificate, change the HTTPS/1.1 port to 443. Use all other defaults.
     - Verify that Tomcat 8 is running by opening a browser on this server to *http://localhost/* You should see the Apache Tomcat administration page. If you didn't request port 80 during the install, you will need to specify the port you chose (*http://localhost:port/*). If you didn't configure a port, the default port is 8080 (and 8443 for HTTPS).
     - **Linux Installs**

       - To ensure that the proper java settings are found by the web server, you may need to specify the **-E** flag when restarting the webserver. Example -

        .. code-block:: console

          $ sudo apt-get install tasksel
          $ sudo tasksell install tomcat
          $ sudo apt-get install java8-jdk

       - Now open :file:`/.bashrc` with your editor and add: export JAVA_HOME = :file:`/usr/lib/jvm/java-7-openjdk-amd64` at the bottom of that file. Change this to whatever path is appropriate for your java installation.  

        .. code-block:: console

          $ sudo -E /etc/init.d/tomcat8 restart

       - The **E** flag on the last command is critical. It forces Ubuntu to reload the environment settings for the service, causing it to pick up the new *JAVA_HOME* setting.  
    
     - Apply or change the administrator password for Tomcat; the administration functions should be secured.
     - ODK Aggregate v1.4.13 and higher are supported on Tomcat 8.0; these newer releases should also work, without modification on other webservers.
     - Prior to ODK Aggregate v1.4.13, we only supported Tomcat 6. Tomcat 7, Tomcat 8, Glassfish and Jetty require additional configuration steps to run ODK Aggregate v1.4.12 and earlier. All of these webservers require configuration settings to enable cookies under HTTPS.

      - **For Tomcat 7**: Edit :file:`context.xml` (under Tomcat 7's conf directory) to have the attribute 'useHttpOnly' set to false. 

       .. code-block:: xml

         <Context useHttpOnly="false">

      - **For Tomcat 8**: My ODK Aggregate file is installed as :file:`/var/lib/tomcat8/webapps/ODKAggregate.war`. The following content needed to be placed in the file :file:`webapps/ODKAggregate/META-INF/context.xml` (this is within the expanded content of the war file, once the Tomcat 8 server has exploded it).

       .. code-block:: xml

         <Context path="" useHttpOnly="false" />

      - **For Glassfish 4**: Add :file:`glassfish-web.xml` under ODK Aggregate's WEB-INF directory with the content:

       .. code-block:: xml

         <?xml version="1.0" encoding="UTF-8"?>
         <glassfish-web-app>
             <session-config>
                 <cookie-properties>
                     <property name="cookieHttpOnly" value="false" />
                 </cookie-properties>
             </session-config>
         </glassfish-web-app>

      - **For Jetty**: Add :file:`jetty-web.xml` under ODK Aggregate's WEB-INF directory with the content:

       .. code-block:: xml

         <?xml version="1.0"  encoding="ISO-8859-1"?>
         <!DOCTYPE Configure PUBLIC "-//Jetty//Configure//EN" "http://www.eclipse.org/jetty/configure.dtd">

         <Configure class="org.eclipse.jetty.webapp.WebAppContext">
              <Get name="sessionHandler">
                  <Get name="sessionManager">
                      <Set name="secureCookies" type="boolean">true</Set>
                  </Get>
              </Get>
         </Configure>
  

- `Configure your server and network devices <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_ so that laptops or Android devices connecting to the internet from an external access point can access your server. If your organization has a network or systems administrator, contact them for assistance. The steps for this are:

   - configure your server firewall to allow access
   - make your server visible on the internet (optional)
   - establish a DNS name for the server

- `Obtain and Install <https://gist.github.com/yanokwa/399a7fcbc3d9ad8a0bd3>`_ an SSL certificate if you need secure (https:) access.

- Select and Install your database server (MySQL or PostgreSQL or Microsoft SQL Server or Azure SQL Server).

   - ODK Aggregate works with any of these database servers:

      - MySQL
      - PostgreSQL
      - Microsoft SQL Server
      - Azure SQL Server (requires Java 8)

   - A database server manages one or more databases. The database server stores and retrieves data from tables within these databases.
   - For MySQL, download and install MySQL Community Server 5.7 or higher from `MySQL download site <https://dev.mysql.com/downloads/>`_. Be sure to set a root password for the database. Stop the MySQL database server, then configure the database (via the :file:`my.cnf` or the :file:`my.ini` file) with these lines added to the [mysqld] section:

     .. code-block:: none

        character_set_server=utf8
        collation_server=utf8_unicode_ci
        max_allowed_packet=1073741824

    and restart the MySQL databaseserver. Then, download the `MySQL Connector/J`, unzip it, and copy the :file:`mysql-connector-java-x.x.x-bin.jar` file into the Tomcat server's libs directory. After copying it into that directory, you should stop and restart the Tomcat server. The `max_allowed_packet` setting defines the maximum size of the communications buffer to the server. The value used in the snippet above is 1GB, the maximum value supported. For ODK Aggregate 1.4.11 through 1.4.7, and 1.2.x, the maximum media (e.g., image or video) attachment is limited to the value you set for max_allowed_packet minus some unknown overhead -- e.g., a storage size of something less than 1GB. For ODK Aggregate 1.4.6 and earlier (excluding 1.2.x), the maximum media attachment is unlimited and the setting for max_allowed_packet does not need to be specified. For ODK Aggregate 1.4.12 and later, the max_allowed_packet value should be set to a value greater than 16842752 (this is the minimum value that should be used: 16MB plus 64kB); with that setting, media attachments of unlimited size are once again supported. If you are upgrading to a newer ODK Aggregate, you must continue to use the setting you already have, or 16842752, whichever is greater. If you experience problems uploading large attachments, change this setting to its maximum value, 1073741824. Finally, if you are using MySQL 5.7 or later, some of releases `expire all database passwords <https://dev.mysql.com/doc/refman/5.7/en/password-management.html>`_ after 360 days. Please verify the behavior of your version of MySQL and either change the password expiration policy or create a calendar reminder to change the password before it expires. For ODK Aggregate, you will need to re-run the installer to specify the new password. 

   - For PostgreSQL, download and install the appropriate binary package from `PostgreSQL download site <https://www.postgresql.org/download/>`_. Be sure to set the password for the postgres (root) user and set the default character set and collation sequence.
   - For either database, you should ensure that the default character set is configured to be UTF-8 and that the collation sequence (dictionary order) is set appropriately for your circumstances. If it isn't, any non-Latin characters may display as question marks. Refer to the character set and collation sections of your database's documentation for how to do this.
   - For Microsoft SQL Server or Azure SQL Server, you should configure these with UTF-8 character sets and to use Windows authentication. When using Windows authentication, the user under which the webserver executes must be granted permissions to access the SQL Server instance. The install wizard for ODK Aggregate will produce a :file:`Readme.html` file that contains additional information on how to complete the configuration of the database and webserver service.

- Download and install `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest Featured release for your operating system.

.. note::

   The installer will guide you through configuring ODK Aggregate for Tomcat and MySQL/PostgreSQL/SQLServer. The installer will produce a WAR file (web archive) containing the configured ODK Aggregate server, a :file:`create_db_and_user.sql` script for creating the database and user that ODK Aggregate will use to access this database, and a :file:`Readme.html` file with instructions on how to complete the installation. 

.. tip::   
   
   - When asked for the fully qualified hostname of the ODK Aggregate server, you should enter the DNS name you established above. The install also asks for a database name, user and password. The user should not be root (MySQL) or postgres (PostgreSQL). ODK Aggregate will use this user when accessing this database (and it will only access this database). By specifying different databases and users, you can set up multiple ODK Aggregate servers that share the same database server, store their data in different databases, and operate without interfering with each other.
   - If you are upgrading to a newer version of ODK Aggregate, as long as you specify the same database name, user and password, you do not need to re-run the :file:`create_db_and_user.sql` script (it only needs to be executed once).

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



