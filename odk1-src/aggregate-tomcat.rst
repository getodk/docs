.. spelling::

  databaseserver
  Glassfish
  useHttpOnly

Installing on Tomcat (Local or Cloud)
=========================================

`Apache Tomcat <http://tomcat.apache.org/>`_ is an open source Java web server that can be used to serve ODK Aggregate.

This document guides you through the installation and initial setup of a self-hosted instance of ODK Aggregate, running on Apache Tomcat with a `MySQL <https://www.mysql.com/>`_ or `PostgreSQL <https://www.postgresql.org/>`_. "Self-hosted" could mean on your own hardware or on a cloud-based server such as Amazon Web Services. (Though, for AWS in particular, we have :doc:`additional instructions <aggregate-aws>`.)

.. warning::

  Self-hosting, whether local or cloud-based, requires expertise in server maintenance, security, systems administration, and networking. If your organization does not have this expertise, we recommend using :doc:`Google App Engine <aggregate-app-engine>`.


.. note::

  - Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility. You must also plan for the security of your data and systems. 

  -  Local hosting requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer technical support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.


Considerations before you begin
----------------------------------
   
Availability
~~~~~~~~~~~~~~

Decide the availability of your server depending on how frequently you want to update and upload forms. If you do need a high-availability server, you need to talk to your Internet Service Provider (ISP) as to their availability guarantees.
   
Data Loss
~~~~~~~~~~~
   
Your tolerance to data loss will impact your backup schedule and your server hardware.  Invest in a storage system based on your tolerance to data loss. Seek technical assistance for these requirements. If you cannot tolerate any data loss, or less than 24 hours of data loss, you should invest in a RAID storage array with battery-backed controller cards. If you can tolerate a day or longer interval of data loss, be sure you have a periodic tape or other means of backup for your system that matches or is shorter than the data loss interval.
   
Dataset Size
~~~~~~~~~~~~~~
   
The quantity of data you intend to collect will affect the size of the machine required to host the ODK Aggregate instance and of your database server. For most use cases, the default size should be fine. If you are collecting more than 6000 submissions, you may need to increase the JVM size. Note that the maximum size of the JVM is limited by the size of the physical memory on your machine.
   
   
Secure and Protected Data
~~~~~~~~~~~~~~~~~~~~~~~~~~   

If you need to prevent eavesdroppers from seeing your data as it is transmitted to your ODK Aggregate instance, you need to do one of the following:

- only connect to ODK Aggregate from within your organization's network (when the ODK Collect devices are on your premises)
- obtain an SSL certificate and install it on your Tomcat server (a certificate is required to secure transmissions over `https`)
- use :doc:`encrypted-forms`

Encrypted forms can be used in conjunction with either of the first two suggestions.

If you are not using encrypted forms and are handling sensitive data, a computer security specialist should review your system and your security procedures. 

Database Systems
~~~~~~~~~~~~~~~~~~

ODK Aggregate works with any of these database servers:

- MySQL
- PostgreSQL
- Microsoft SQL Server
- Azure SQL Server

Most deployments will use either MySQL or PostgreSQL, as they are the two most prevalent open source relational database servers.

MySQL is the most popular, so you will likely find more qualified professionals to install, administer, and debug it. However, you should consider PostgreSQL if you plan to:

- collect geographic data
- use forms with a very high number of questions (over 200)

PostgreSQL has better built-in support for geographic data, and MySQL's tables have a row size limit that will affect performance for very large forms.  

.. note::

  Use of an SSL and `https` is recommended for any deployment accessed from the internet.

Installation procedure
--------------------------


1. Install Tomcat on your server.

    a. Install `Java 8 <https://java.com/en/download/>`_ or higher on your system.

       .. note::

        You generally need to launch installers with *Run as administrator* privileges (available under the right-click menu). Accept all the defaults.

    b. Add the installed Java bin directory to the `PATH variable <https://docs.oracle.com/javase/tutorial/essential/environment/paths.html>`_.
    c. Download and install `Tomcat 8 <https://tomcat.apache.org/download-80.cgi>`_

       - If using the Windows installer, change to use port 80 for the HTTP/1.1 port. If you are going to set up an SSL certificate, change the HTTPS/1.1 port to 443. Use all other defaults.
       - Verify that Tomcat 8 is running by opening a browser on this server to ``http://localhost/``. You should see the Apache Tomcat administration page. If you didn't request port 80 during the install, you will need to specify the port you chose (``http://localhost:port/``). If you didn't configure a port, the default port is 8080 (and 8443 for HTTPS).
       - **Linux Installs**

          - To ensure that the proper Java settings are found by the web server, you may need to specify the :option:`-E` flag when restarting the webserver.

            .. code-block:: console

               $ sudo apt-get install tasksel
               $ sudo tasksell install tomcat
               $ sudo apt-get install java8-jdk

          - Now open :file:`/.bashrc` with your editor and add ``export JAVA_HOME = /usr/lib/jvm/java-8-openjdk-amd64`` at the bottom of that file. Change this to whatever path is appropriate for your Java installation.

             .. code-block:: console

               $ sudo -E /etc/init.d/tomcat8 restart

             The **E** flag on the last command is critical. It forces Ubuntu to reload the environment settings for the service, causing it to pick up the new *JAVA_HOME* setting.  
    
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
  

2. `Configure your server and network devices <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_ so that laptops or Android devices connecting to the internet from an external access point can access your server. 

   If your organization has a network or systems administrator, contact them for assistance. The steps for this are:

   - configure your server firewall to allow access
   - make your server visible on the internet (optional)
   - establish a DNS name for the server

3. `Obtain and Install an SSL certificate <https://gist.github.com/yanokwa/399a7fcbc3d9ad8a0bd3>`_ if you need secure ``https`` access.

4. Select and Install your database server.

   ODK Aggregate works with any of these database servers:

   - MySQL
   - PostgreSQL
   - Microsoft SQL Server
   - Azure SQL Server (requires Java 8)

   |
   
   - For MySQL, download and install MySQL Community Server 5.7 or higher from `MySQL download site <https://dev.mysql.com/downloads/>`_. Be sure to set a root password for the database. Stop the MySQL database server, then configure the database (via the :file:`my.cnf` or the :file:`my.ini` file) with these lines added to the [mysqld] section:

     .. code-block:: none

        character_set_server=utf8
        collation_server=utf8_unicode_ci
        max_allowed_packet=1073741824

    and restart the MySQL databaseserver. Then, download the `MySQL Connector/J`, unzip it, and copy the :file:`mysql-connector-java-x.x.x-bin.jar` file into the Tomcat server's libs directory. After copying it into that directory, you should stop and restart the Tomcat server. The `max_allowed_packet` setting defines the maximum size of the communications buffer to the server. The value used in the snippet above is 1GB, the maximum value supported. For ODK Aggregate 1.4.11 through 1.4.7, and 1.2.x, the maximum media (e.g., image or video) attachment is limited to the value you set for max_allowed_packet minus some unknown overhead -- e.g., a storage size of something less than 1GB. For ODK Aggregate 1.4.6 and earlier (excluding 1.2.x), the maximum media attachment is unlimited and the setting for max_allowed_packet does not need to be specified. For ODK Aggregate 1.4.12 and later, the max_allowed_packet value should be set to a value greater than 16842752 (this is the minimum value that should be used: 16MB plus 64kB); with that setting, media attachments of unlimited size are once again supported. If you are upgrading to a newer ODK Aggregate, you must continue to use the setting you already have, or 16842752, whichever is greater. If you experience problems uploading large attachments, change this setting to its maximum value, 1073741824. Finally, if you are using MySQL 5.7 or later, some of releases `expire all database passwords <https://dev.mysql.com/doc/refman/5.7/en/password-management.html>`_ after 360 days. Please verify the behavior of your version of MySQL and either change the password expiration policy or create a calendar reminder to change the password before it expires. For ODK Aggregate, you will need to re-run the installer to specify the new password. 

   - For PostgreSQL, download and install the appropriate binary package from `PostgreSQL download site <https://www.postgresql.org/download/>`_. Be sure to set the password for the postgres (root) user and set the default character set and collation sequence.

   - For either database, you should ensure that the default character set is configured to be UTF-8 and that the collation sequence (dictionary order) is set appropriately for your circumstances. If it isn't, any non-Latin characters may display as question marks. Refer to the character set and collation sections of your database's documentation for how to do this.
   
   - For Microsoft SQL Server or Azure SQL Server, you should configure these with UTF-8 character sets and to use Windows authentication. When using Windows authentication, the user under which the webserver executes must be granted permissions to access the SQL Server instance. The install wizard for ODK Aggregate will produce a :file:`Readme.html` file that contains additional information on how to complete the configuration of the database and webserver service.

5. Download and install `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest Featured release for your operating system.

   .. note::

     The installer will guide you through configuring ODK Aggregate for Tomcat and MySQL/PostgreSQL/SQLServer. The installer will produce a WAR file (web archive) containing the configured ODK Aggregate server, a :file:`create_db_and_user.sql` script for creating the database and user that ODK Aggregate will use to access this database, and a :file:`Readme.html` file with instructions on how to complete the installation. 

   .. tip::   
   
     - When asked for the fully qualified hostname of the ODK Aggregate server, you should enter the DNS name you established above. The install also asks for a database name, user and password. The user should not be root (MySQL) or postgres (PostgreSQL). ODK Aggregate will use this user when accessing this database (and it will only access this database). By specifying different databases and users, you can set up multiple ODK Aggregate servers that share the same database server, store their data in different databases, and operate without interfering with each other.
     - If you are upgrading to a newer version of ODK Aggregate, as long as you specify the same database name, user and password, you do not need to re-run the :file:`create_db_and_user.sql` script (it only needs to be executed once).
