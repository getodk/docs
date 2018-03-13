.. spelling::

  ec
  IPv
  scp
  un

Installing on AWS (Cloud)
==========================

This document provides instructions on setting up ODK Aggregate using `Apache Tomcat <http://tomcat.apache.org/>`_ and `MySQL <https://www.mysql.com/>`_ on a Linux micro-instance on the `Amazon Web Services <https://aws.amazon.com/>`_  `EC2 infrastructure <https://aws.amazon.com/ec2/>`_.

.. admonition:: Additional Resources 

  - For more on the general set-up of Tomcat on AWS, see `Cat in the cloud Apache Tomcat Series <http://www.excelsior-usa.com/articles/tomcat-amazon-ec2-basic.html>`_.
  - For an introduction to hosting on AWS, see `Amazon’s getting-started guides <https://aws.amazon.com/documentation/gettingstarted/>`_.
  - For details on setting up ODK Aggregate on Tomcat, but not in an AWS environment, see :doc:`aggregate-tomcat`.
  
.. admonition:: Before you get started... 

  Get an Amazon Web Services account at `<http://aws.amazon.com/ec2/>`_.

    .. note::

      - You will need to confirm a working phone number. 
      - If you want to use a U.S. number but are presently overseas, you can use a Google Voice number routed to Google Chat.

1. Go to the AWS/EC2 management console and note your region (shown in the upper-left).

2. Launch a new instance with the :guilabel:`Launch Instance` button prominently displayed on the EC2 console home screen. 

   Accept the default behavior and use the quick-launch wizard.

3. For the launch configuration, choose the :guilabel:`Amazon Linux AMI: EBS-Backed (64-bit)` option. 

   This is one of the instance types that you can run on a micro-instance as part of their `free tier <http://aws.amazon.com/free/>`_. 
   
   Leave everything else with the default settings, including the instance type. The instance type will default to ``t2.micro`` which is a small, limited instance that can be run for free. For a price, you can upgrade the instance type later if you need better performance.

   .. note::

     The exact AMI name and ID will depend on your region. 

4. Create a new key pair, download the private key, and keep the private key safe. 

   This will be your only method of communicating with your new instance and **you will not be allowed to download it again**.

5. After creating the instance, add security rules for allowing both HTTP and HTTPS. 

   Choose the :guilabel:`Security Groups` tab and click on the auto-created security group associated with your new instance. This might have been called ``launch-wizard-1``. If you’re not sure, you can go to the :guilabel:`Instances` tab to see which :guilabel:`Security Group` is listed for the new instance.
  
   In the properties pane at the bottom, click on the :guilabel:`Inbound tab`, select ``HTTP`` from the :guilabel:`create a new rule` drop-down, then click :guilabel:`Add Rule`. Do the same for ``HTTPS``. Then click :guilabel:`Apply Rule Changes`.

   .. tip::

    To avoid potential problems with MTU settings and packet loss, also add a rule to allow *All ICMP*. Add a rule for both IPv4 and IPv6. After you create the new rule, click :guilabel:`Apply Rule Changes`.

   .. note::

    Tomcat defaults to listening on nonstandard ports ``8080`` and ``8443``. In this guide we provide instructions to use the standard HTTP and HTTPS ports instead. 
    
    However, if you want to leave Aggregate on the non-standard ports, you can certainly do so. In that case, simply add two additional security rules to allow access via ``8080`` and ``8443``.

6. Switch to the :guilabel:`Instances` tab, click on your instance, and note its Public DNS Address in the properties pane below. 

   This is the default address that you will use to access your instance.

7. Allocate an *elastic IP* and domain name. 

   This step is not required, but it allows you to access your Aggregate instance using a human readable URL set by you. So we recommend it.

   Navigate to Elastic IPs and click :guilabel:`Allocate New Address`. Associate it with your new instance.  Note your new IP. Also, if possible, configure DNS to route one or more names to this address. You can then use this IP and/or name to access your instance (and can forget the Public DNS Address assigned by AWS).

   .. note:: 

     The IP is free so long as you keep it associated with a running instance. If you stop your instance and do not release the IP address for others to use (in essence, wasting it), then Amazon will begin charging you for holding the unused address.

   .. tip::

     When you set up Aggregate below, you will need to configure it with the domain name you will use to access it. Thus, it is best if you configure the domain name first.

8. Connect to your instance. 

   Go to the :guilabel:`Instances` tab and select :menuselection:`Connect` from the Instance Actions drop-down (alternatively, you can right-click on the instance and choose Connect). From here AWS presents you with several options.
 
   - The easiest is to connect using their Java SSH client. If you choose that option, you just have to specify the location of your private key file (created above) and AWS launches an in-browser SSH client to connect to your instance.
   - You can also select to connect with a stand-alone SSH client. If you choose this option, AWS will provide extremely helpful instructions, including an SSH command that you can cut and paste into your local command window. It will also inform you that you may need to update the permissions on your local private key file in order for the ssh client to run properly, and it will even give you the command to run (for example, :command:`chmod 400 xxx.pem`).
   - Once you connect, you will probably be told that there are new security updates to install. You can run :command:`sudo yum update` to install these updates, as it advises.

9. Transfer files to your instance. 

   When you login using ``ssh``, you will be in the (empty) ``ec2-user`` home directory. You will want to be able to transfer files between here and your local directory. You have several options.
 
    - If you’re using the command-line ssh, you can also use the command-line scp to copy files. The syntax is similar to ssh, but of course you also need to specify the source and destination file paths.
    - An easier option is to use an `FTP client <https://en.wikipedia.org/wiki/File_Transfer_Protocol>`_ like `FileZilla <https://filezilla-project.org/>`_. (You can use any FTP client, as long as it supports SFTP).
     
      - To configure FileZilla to connect to your instance, go into :menuselection:`Edit-->Settings/Preferences-->Connection-->SFTP` and add your private key to FileZilla’s keystore (it will offer to convert the key format, which you should accept). Then, go into Site Manager and create a new site. The host should be the IP, name, or Public DNS for your instance, the port can be blank, the protocol should be **SFTP – SSH File Transfer Protocol**, the login type should be Normal, and the user should be **ec2-user**. Everything else should be left at the defaults, including the password (which will be blank). When you connect, the default directory will be the ec2-user’s home directory, but you can also navigate to other directories.

10. Install Tomcat 6. 

    While logged into your ec2 instance:

    .. code-block:: console
    
      $ sudo yum install tomcat6
    
    This installs configuration files into :file:`/etc/tomcat6` and other files into :file:`/usr/share/tomcat6`. Log files go into :file:`/var/log/tomcat6`.

11. Install MySQL.

    While logged into your ec2 instance:
  
    .. code-block:: console
  
      $ sudo yum install mysql mysql-server

    Open :file:`/etc/my.cnf`. In the ``[mysqld]`` section, add:

    .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824
      
    .. note::
    
      Whatever your preferred editor, when updating files on the server, the easiest tool is probably `vim <https://en.wikipedia.org/wiki/Vim_(text_editor)>`_. This will open the file directly in your terminal.
      
      .. code-block:: console
      
        $ vi /etc/my.conf
	
      Vim can be a little tricky to use at first. There are many tutorials online. You may find `this interactive Vim introduction <http://www.openvim.com/>`_ helpful.
	
	
12. Run MySQL.

    .. code-block:: console
  
      $ sudo service mysqld start

13. Install and transfer ODK Aggregate files.

    a. First, install ODK Aggregate on your local computer (not on your AWS instance).
  
    .. note::

      During set-up, it’s important to specify that this will be a MySQL installation, and it is also very important that you specify the correct domain name or IP address that will be used to access your Aggregate server. Ideally, this will be a specific domain name that you have already mapped to an elastic IP (and can re-map later if you change the IP).

    b. The installation will create a file named :file:`create_db_and_user.sql`. Upload this to your ec2-user home directory.
    c. The installation will also create a file named :file:`ODKAggregate.war`. Rename this to :file:`ROOT.war` and upload it to the :file:`/usr/share/tomcat6/webapps` folder. If you receive a *Permission Denied* error, you might need to execute :command:`chmod -R 755` or something similar for the webapps folder.
    d. After :file:`ROOT.war` has been copied to the server, you need to make sure Tomcat has permission to use it. Run :command:`sudo chown tomcat ROOT.war` and :command:`sudo chgrp tomcat ROOT.war` in the webapps directory to ensure this is the case.

14. Configure MySQL.

    a. On your AWS instance, run :file:`/usr/bin/mysql_secure_installation` to set a root password and secure your MySQL installation.
    b. Run :command:`mysql –u root -p` to log in to MySQL (specifying the password you just set), and type :command:`source ~/create_db_and_user.sql`. This will create the ODK user and database. Type :command:`quit` on the mysql prompt to quit from MySQL.
    c. Run :command:`sudo /sbin/chkconfig --levels 235 mysqld on` to auto-start MySQL whenever your instance boots up.

15. Configure Tomcat.

    a. Download the MySQL Connector/J from the `MySQL download page <http://dev.mysql.com/downloads/connector/j/)>`_. Unzip it and transfer the :file:`mysql‐connector‐java‐x.x.x‐bin.jar` file up to your instance’s :file:`/usr/share/tomcat6/lib` directory.
    b. Edit :file:`/etc/tomcat6/server.xml` in order to customize settings.
    c. Assuming that you want to run Aggregate on the standard HTTP port (80) and HTTPS port (443):

      - Change ``<Connector port="8080" protocol="HTTP/1.1"`` to ``<Connector port="8080" proxyPort="80" protocol="HTTP/1.1"`` (that is, add the ``proxyPort`` attribute).
      - If you are using SSL, also change ``<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"`` to ``<Connector port="8443" proxyPort="443" protocol="HTTP/1.1" SSLEnabled="true"``.
      - Execute the following commands to have Linux forward to the ports on which Tomcat listens:
      
       .. code-block:: console

         $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
         $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8443
         $ sudo /sbin/service iptables save

      - If you have an SSL certificate for HTTPS support:

        - Make sure that the ``<Connector port="8443"`` part of the configuration file is not commented out. If it is, un-comment it.
        - Upload your SSL keystore file and the certificate(s) to the server.
        - Install it as instructed. (If you buy from RapidSSL, for example, they provide you with Tomcat installation instructions. For example, you may need to download a special P7S certificate file, then install it on the server with :command:`keytool -import -alias YOURALIAS trustcacerts file xxxxx.p7s -keystore xxxxx.keystore`.)
        - In the ``<Connector port="8443"`` part of the configuration file, specify the location of your keystore file and password (for example: ``keystoreFile="/…/xxxxx.keystore" keystorePass="changeit"``).

    - Start Tomcat with :command:`sudo service tomcat6 start`.
    - Configure Tomcat to auto-start when the instance boots with :command:`sudo chkconfig --level 345 tomcat6 on`.

16. Login and test. 

    At this point, you should be able to login to your AWS-hosted Aggregate instance by going to its domain name or IP address in your web browser (with or without HTTPS, depending on your set-up).

    .. note::  

      For your first login, you will need to login with the Google account you specified during the Aggregate installation process. Then you can add additional users from the :guilabel:`Site Admin` tab.

    Once you have confirmed that your Aggregate instance is working, you can back it up by creating an image of the instance (an `AMI <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html>`_). 
    
    To do this, go to the :guilabel:`Instances` tab in the AWS-EC2 console, then select the :guilabel:`Create Image (EBS AMI)` Instance Action for your instance.

17. Further set-up for production servers.

    - You will want to create a system to monitor and manage the log files in :file:`/var/log/tomcat6`.
    - You will also want to create a system for regular back-ups and a plan for how to restore them when needed. This will be needed to safely back up the MySQL database, which may be in-use at any given time.

------
    
.. note::

  - The micro instance is only free for 12 months from AWS sign-up, and that you may exceed the free quotas on disk space or network bandwidth before that point (`see <http://aws.amazon.com/free/>`_).
  - You may at some point need to upgrade your instance to a standard instance if the micro instance is not providing enough performance.
