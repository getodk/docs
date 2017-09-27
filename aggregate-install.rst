***********************************
Aggregate Installation and Setup
***********************************

Before going through this section, make sure you have used :doc:`ODK Collect <collect-guide>` and are familiar with how it works.

.. tip::

  - Try the ODK Aggregate `demo server <https://opendatakit.appspot.com>`_ to explore the core functionality.
  - Decide whether to install a cloud instance or a local instance. It is strongly recommended to try an App Engine cloud instance first. If you wish to host locally, see `Aggregate Deployment Planning <https://opendatakit.org/use/aggregate/deployment-planning/>`_
  - Local hosting implies that you are taking ownership of the off-site back-up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility.    
  - You must also plan for the security of your data and systems. And finally, it requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer-technical-support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.

.. _install-app-engine:

Installing on App Engine
--------------------------

- Make sure `Java 8 <https://java.com/en/download/>`_ or higher is installed on your system.See `MacOSX Java install <https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html>`_ if you are a Mac user.
- You will need a Gmail account to use App Engine; this Gmail account will be the owner of the Google Cloud Platform `project` under which your App Engine will execute. 

.. tip::

  - Google Cloud Platform hosts projects `under these terms <https://cloud.google.com/terms/>`_.
  - There is no cost to set up these projects and App Engine projects that are lightly used will incur no charges.

- To set up a Google Cloud Platform project, go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner.

.. image:: /img/aggregate-install/cloud-console.*
   :alt: An image showing the console option on the Google Cloud Platform.

- You will now be asked to provide a gmail account which you will use throughout.Sign in with a gmail account which you wish to use.

.. image:: /img/aggregate-install/email-select.*
   :alt: Image showing the sign in window of Gmail.

- If you have never configured a Google Cloud Platform project, click on :guilabel:`Create an Empty Project`.

.. image:: /img/aggregate-install/empty-project.*
   :alt: Image showing Create a empty project option for first projects. 

- If you have configured a Google Cloud Platform project before, this link will open onto either a page with a :guilabel:`Create Project` button and a table listing all of your projects, or it will open into one of your existing projects. In the later case, click on that project name at the top of the window.In the below image, the older project is `Project 123`.

.. image:: /img/aggregate-install/project.*
   :alt: Image showing previous project name `Project123`.

- On clicking on the project name (In this case `Project123`), a window appears with a :guilabel:`+` symbol. Click on it to create a new project.   

.. image:: /img/aggregate-install/create-project.*
   :alt: Image showing the `+` sign which denotes creating a new project.

- On the project-creation pop-up dialog, type in a project name that makes sense to you.You can enter a project name and click on :guilabel:`Create` if you don't want to edit the project-id.You can choose :guilabel:`Edit` if you want to edit the project id. The project id will be the first part of the URL to your ODK Aggregate server.

.. image:: /img/aggregate-install/project-name.png
   :alt: Image showing the window to enter a project name.

- If you click on :guilabel:`Edit`, a window will appear where you can enter a project id. After changing the project id click on :guilabel:`Create` to create your project.

.. image:: /img/aggregate-install/project-id.*
   :alt: Image showing the window which comes after clicking on edit option to change the project id.

.. tip::

   You may want to use a project id that combines your organization name and the name of your data collection group or project. You may also need to accept Google's terms-and-conditions.

- After few seconds, you will see a notification in the top right corner of the window.
  
.. image:: /img/aggregate-install/notification.*
   :alt: Image showing blue notification icon.

- Click on the notification icon and select the first option from the dropdown menu then. Thw option is labelled as `Create Project:your project name`.

.. image:: /img/aggregate-install/go-to-project.*
   :alt: Image showing the option to create your project.      

- Upon creating the Google Cloud Platform project, you will be on an empty-project screen, showing the project info. If you want to change any settings, click on :guilabel:`Go to project settings`. Otherwise click on the menu icon (three horizontal bars) to the left of :guilabel:`Google Cloud Platform` in the upper left side of the screen.

.. image:: /img/aggregate-install/project-settings.*
   :alt: Image showing the project settings option and the menu option.

- Now and select :guilabel:`App Engine` from the dropdown menu.

.. image:: /img/aggregate-install/app-engine.*
   :alt: Image showing App Engine option.

- Click on the :guilabel:`Select a language` dropdown under the `Your first app` heading.

.. image:: /img/aggregate-install/language-select.*
   :alt: Image showing option to select a language.

- Now choose `Java`.

.. image:: /img/aggregate-install/select-java.*
   :alt: Image showing various language options to choose from.

- Select the datacenter location where this server will operate and click :guilabel:`Next`.

.. image:: /img/aggregate-install/select-region.*
   :alt: Image showing options to choose a region where the server will operate.

- Google will then begin configuring the server.

.. image:: /img/aggregate-install/prepare-engine.*
   :alt: Image showing Google configuring the server.

- When this completes, you will be directed to begin a tutorial to install a sample application. Choose :guilabel:`Cancel Tutorial` and confirm that you want to not perform that tutorial.

.. image:: /img/aggregate-install/cancel-tutorial.*
   :alt: Image showing option to cancel the tutorial.

- Download `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest release for your operating system.

.. tip::

   - You can verify the download using `SHA256 signatures` as described at the top of the downloads page.
   - If you are running OSX, you must unzip the downloaded file before running the installer within it.
   - If you are on MacOSX Mountain Lion or onward, you will need to fiddle with `GateKeeper settings <http://osxdaily.com/2012/07/27/app-cant-be-opened-because-it-is-from-an-unidentified-developer/>`_ in order to run the installer.
   - If you are on Windows 10, you will need to approve running an unsigned installer.
   - If you are on Linux, you will need to change the downloaded file's permissions to enable running it as a program. Right click on the file and click on :guilabel:`Properties`. Click on :guilabel:`Permissions` tab. Now check the box labelled as :guilabel:`Allow executing file as program`. Now double click on the file to run it.

- The installer will guide you through configuring ODK Aggregate for App Engine. Click on :guilabel:`Forward` button each time you complete a step to move ahead.

.. image:: /img/aggregate-install/setup.*
   :alt: Image showing the installer for ODK Aggregate.

- Accept the license agreement and click on :guilabel:`Forward` button.

.. image:: /img/aggregate-install/agreement.*
   :alt: Image showing license agreement.

- Select a parent directory under which an `ODK Aggregate` directory will be created to contain the configured software.Click on the :guilabel:`folder` icon to choose a directory.

.. image:: /img/aggregate-install/directory-setup.*
   :alt: Image showing window to choose a parent directory. 

- In the next window choose `Google App Engine` as the platform for Aggregate server.

.. image:: /img/aggregate-install/choose-platform.*
   :alt: Image displaying options to choose a platform for Aggregate.

- Enter a name for your ODK Aggregate instance.

.. image:: /img/aggregate-install/set-name.*
   :alt: Image showing window to select a name for your Aggregate instance.

.. note::    
   
   The ODK Aggregate instance name will be displayed to your users when they log into ODK Aggregate using their username and password.

.. tip::
   
   Including the name of your organization in the instance name can help users confirm that they have contacted the correct website.

- Enter a superuser name in the next window.

.. image:: /img/aggregate-install/superuser.*
   :alt: Image showing window to enter a superuser name.

.. note::
   
   - The user with the superuser account will have full permissions on the system.
   - The password for this user will be set to `aggregate` initially.
   - Only this user will be allowed to log onto the system when ODK Aggregate is run for the first time.
   - Upon first logging in, the superuser should change the password and complete the configuration of ODK Aggregate by specifying additional users and what permissions they will have on the system.

- In the next window enter the project id of the project you created on the Google Cloud platform.

.. image:: /img/aggregate-install/application-id.*
   :alt: Image showing project id of the project created earlier entered in the application id box.

- Now the installer will configure Aggregate and launch a upload tool.  

.. tip::

   Beginning with Java 7 Update 51, there are security level settings that may prevent the upload tool from running. A reported work-around is to add the file: path (e.g., file:///) to the Exception Site list.

- Enter the gmail account in the upload tool that you specified to use the App Engine. This will enable the :guilabel:`Get Token` button.

.. image:: /img/aggregate-install/get-token.*
   :alt: Image showing the window for upload tool to enter the email id and get a token.

- Click the :guilabel:`Get Token` button.Two things happen after this:-

    - Your default browser will open to a Google site (accounts.google.com) where you are asked to choose a gmail account (select the account specified by you to use the App Engine), and then approve allowing "Google App Engine appcfg" to View and manage your AppEngine instances and datastores. Click :guilabel:`Allow`. This will take you to a screen with instructions to copy a code.
    - At the same time, a pop-up dialog should be displayed by the upload tool. 

    .. tip::

      - If the pop-up dialog does not show, close the upload tool and open a file browser or Finder window on the directory you specified for the installer to place its files. Navigate into the ODK Aggregate directory.
      - If on Windows, double-click the :file:`ODKAggregateAppEngineUpdater.jar` file. 
      - If on Mac OSX, double-click the uploadAggregateToAppEngine.app file. 
      - If on Linux, open a bash shell and run uploadAggregateToAppEngine.sh. These should all re-launch the upload tool. 
      - Re-enter the e-mail address, and once again click :guilabel:`Get Token`. The pop-up dialog should now appear.

- Copy the code from the browser into the upload tool's pop-up dialog and click :guilabel:`OK`.

.. image:: /img/aggregate-install/token.*
   :alt: Image showing pop up dialog to enter a token.

.. tip::
    
   The text box on Google's site is not as wide as the code; be sure to copy the entire code.

- The output should look something like that in the image.
  
.. image:: /img/aggregate-install/success-output.*
   :alt: Image showing ouyput for a successful result.

.. tip::
  
   - If the output does not look like that, you may have delayed too long between getting the code and pasting it into the tool. Click :guilabel:`Delete Token` and try again.
   - If you see a failure message in the output window, then it is likely that you have several different gmail accounts and Google has gotten confused during the token-issuing process. In this case, when the browser window opens, before selecting an account, copy the URL, open a Private Browsing or Incognito Window in your browser, and paste the URL into that. Then proceed to get the token, etc. This should fix this issue.

- Now click :guilabel:`Upload ODK Aggregate`.

.. image:: /img/aggregate-install/upload.*
   :alt: Image showing successful output and upload option.

.. note::

   - Clicking on :guilabel:`Upload ODK Aggregate` will spew a very long list of progress messages into the Output window. The `listBackends :` and `deleteBackendBackground :` sections may report "500 Internal Server Error" and Severe errors, and Warnings about the use of Backends, a deprecated feature. This is expected.
   - Toward the bottom, the update : section should not report errors and at the end, a `status : Action Succeeded!` line should be written. This indicates that the upload completed successfully. 

- Once the updater script has run and uploaded the ODK Aggregate configuration to App Engine, return to the Google Cloud Platform console. With the console displaying your project, click on the menu icon (three horizontal bars) to the right of `Google Cloud Platform` in the upper left side of the screen and select App Engine from the menu.

- Click on :guilabel:`ALLOW` in the next window.

.. image:: /img/aggregate-install/allow.*
   :alt: Image showing window asking for App Engine Permissions.

- Click on the project-id URL in the top right corner of the window.

.. image:: /img/aggregate-install/project-aggregate.*
   :alt: Image showing a window where server url is displayed on top right corner.

-  You will go to now your ODK Aggregate server. Youu can click on :guilabel:`Log In` to log in, enter the ODK Aggregate username (superuser) that you specified within the installer (the initial password for this username will be aggregate) and access the site administration screens for your server.  

.. image:: /img/aggregate-install/server.*
   :alt: Image showing ODK Aggregate server and log in option.

.. _change-size:

Changing size of App Engine Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have many form definitions on your server, you may get better performance and reduce the likelihood for data corruption if you increase the size of your server.

.. note::

   - Data corruption is generally caused by the premature termination of an action (e.g., saving of a submission) because it took longer than the allotted time. The likelihood of data corruption occurring is tied to the quantity of form definitions on the server, the size of the individual submissions, the number of devices simultaneously submitting data, and the speed of the network. Increasing the web server size enables it to handle larger workloads faster, which can reduce the likelihood of hitting this time limit thereby avoiding data corruption.
   - For data corruption caused by slow network speeds, you might also be able to change more aspects of the App Engine configuration (specified in these files) to make your web server always-available and to replace it with a Bx instance that does not have an automatic request time limit (the documentation provided by Google is currently unclear on whether this is still possible with the new services constructions).

To change Google App Engine configuration, you must edit the configuration files produced by the installer and re-run the uploader script to push the changes to Google's servers. There are two server settings that can be changed:-
  
- `Web Server Size` :- The web server handles all browser interactions and all data-submission and form-download requests from ODK Collect and ODK Briefcase. Increasing the size of the web server should reduce the likelihood of data corruption if it is not caused by slow network speeds. To change the Google App Engine web server size, go to the folder you specified to the installer. Within that folder, navigate to :file:`ODKAggregate/default/WEB-INF`. Within that directory, there will be a file :file:`appengine-web.xml`. Open that file in a text editor like Notepad++ or Notepad. The file contents will look something like :-

 .. code-block:: xml

   <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
     <application>opendatakit-simpledemo</application>
     <module>default</module>
     <version>1</version>

  	 <instance-class>F2</instance-class>
   ...
 
 To change the size of the web server, replace **F2** with a different instance class size. There are several different instance classes available. Select from among the instance classes beginning with the letter **F**. See `instance classes <https://cloud.google.com/appengine/docs/about-the-standard-environment#instance_classes>`_  for their descriptions or search for `Google AppEngine instance classes standard environment` on the web. Then re-run the upload tool within the ODKAggregate folder either by double-clicking the :file:`ODKAggregateAppEngineUpdater.jar` file (Windows), or double-clicking the :file:`uploadAggregateToAppEngine.app` file (Mac OSX), or double-clicking the :file:`uploadAggregateToAppEngine.sh` file (linux). Once you have uploaded these changes to App Engine, your server will be running on the instance size that you have specified.

- `Background Server Size` :- App Engine deployments use a "background" copy of the website to process long-running actions like generating CSV and KML files for export and for publishing all accumulated data to an external server. If you experience difficulty exporting to CSV or KML, the size of that server will also need to be updated. In that case, go to :file:`ODKAggregate/background/WEB-INF`. Within that directory, there will be a slightly different file with the same :file:`appengine-web.xml` filename. Open that file in a text editor like Notepad++ or Notepad. The file contents will look something like :-

 .. code-block:: xml

     <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        <application>opendatakit-simpledemo</application>
        <module>background</module>
        <version>1</version>
	  
  	    <instance-class>B2</instance-class>
     ...

 To change the size of the server, replace **B2** with a different instance class size. There are several different instance classes available. Select from among the instance classes beginning with the letter **B**. See instance classes for their descriptions or search for `Google AppEngine instance classes standard environment` on the web as described in Web Server Size. And, as above, re-run the upload tool to make these changes take effect on Google's servers.

.. _install-vm:

Installing VM (Local or Cloud)
-------------------------------

- The `ODK Aggregate VM <https://gumroad.com/l/odk-aggregate-vm>`_ is a fully-configured install of Aggregate that you can run on any computer. It requires very little setup, works well without Internet connectivity, and gives you complete control over your data collection campaign.

.. _install-tomcat:

Installing on Tomcat (Local or Cloud)
--------------------------------------

To run on ODK Aggregate on a Tomcat server backed with a MySQL or PostgreSQL database follow the following steps:-

- Define your server requirements and install your server.
   
   **Server Requirements**
   
   - `Availability` :-  Decide the availability of your server depending on how frequently you want to update and upload forms. If you do need a high-availability server, you need to talk to your Internet Service Provider (ISP) as to their availability guarantees.
   - `Data Loss` :- Your tolerance to data loss will impact your backup schedule and your server hardware.  Invest in a storage system based on your tolerance to data loss. Seek technical assistance for these requirements.If you cannot tolerate any data loss, or less than 24 hours of data loss, you should invest in a RAID storage array with battery-backed controller cards. If you can tolerate a day or longer interval of data loss, be sure you have a periodic tape or other means of backup for your system that matches or is shorter than the data loss interval.
   - `Dataset Size` :- The quantity of data you intend to collect will affect the size of the machine required to host the ODK Aggregate instance and of your database server. For most applications, the default size should be fine. If you are collecting more than 6000 submissions, you may need to increase the JVM size. Note that the maximum size of the JVM is limited by the size of the physical memory on your machine.
   - `Secure and Protected Data` :- If you need to prevent eavesdroppers from seeing your data as it is transmitted to your ODK Aggregate instance, you should either (1) only connect to ODK Aggregate from within your organization's network (when the ODK Collect devices are on your premises), (2) obtain an SSL certificate and install it on your Tomcat server (a certificate is required to secure transmissions over https:), or (3) use `Encrypted Forms <https://opendatakit.org/help/encrypted-forms/>`_. If you are not using encrypted forms and are handling sensitive data, a computer security specialist should review your system and your security procedures. When operating without an SSL certificate, do not access ODK Aggregate from a remote location when changing passwords.

- Install Tomcat on your server.

    - Install `Java 8 <https://java.com/en/download/>`_ or higher on your system.

    .. note::

        You generally need to launch installers with Run as administrator privileges (available under the right-click menu).Accept all the defaults.

    - Add the installed Java bin directory to the `PATH variable <https://docs.oracle.com/javase/tutorial/essential/environment/paths.html>`_.
    - Download and install `Tomcat 8 <https://tomcat.apache.org/download-80.cgi>`_

    .. tip::

     - If using the Windows installer, change to use port 80 for the HTTP/1.1 port. If you are going to set up an SSL certificate, change the HTTPS/1.1 port to 443. Use all other defaults.
     - Verify that Tomcat 8 is running by opening a browser on this server to `http://localhost/` You should see the Apache Tomcat administration page. If you didn't request port 80 during the install, you will need to specify the port you chose (`http://localhost:port/`). If you didn't configure a port, the default port is 8080 (and 8443 for HTTPS).
     - **Linux Installs**

       - To ensure that the proper java settings are found by the web server, you may need to specify the '-E' flag when restarting the webserver. Example -

        .. code-block:: console

          $ sudo apt-get install tasksel
          $ sudo tasksell install tomcat
          $ sudo apt-get install java8-jdk

       - Now open :file:`/.bashrc` with your editor and add: export JAVA_HOME = :file:`/usr/lib/jvm/java-7-openjdk-amd64` at the bottom of that file. Change this to whatever path is appropriate for your java installation.  

        .. code-block:: console

          $ sudo -E /etc/init.d/tomcat8 restart

       - The `E` flag on the last command is critical. It forces Ubuntu to reload the environment settings for the service, causing it to pick up the new `JAVA_HOME` setting.  
    
     - Apply or change the administrator password for Tomcat; the administration functions should be secured.
     - ODK Aggregate v1.4.13 and higher are supported on Tomcat 8.0; these newer releases should also work, without modification on other webservers.
     - Prior to ODK Aggregate v1.4.13, we only supported Tomcat 6. Tomcat 7, Tomcat 8, Glassfish and Jetty require additional configuration steps to run ODK Aggregate v1.4.12 and earlier. All of these webservers require configuration settings to enable cookies under HTTPS.

      - `For Tomcat 7` :- Edit :file:`context.xml` (under Tomcat 7's conf directory) to have the attribute 'useHttpOnly' set to false. 

       .. code-block:: xml

         <Context useHttpOnly="false">

      - `For Tomcat 8` :- My ODK Aggregate file is installed as :file:`/var/lib/tomcat8/webapps/ODKAggregate.war`. The following content needed to be placed in the file :file:`webapps/ODKAggregate/META-INF/context.xml` (this is within the expanded content of the war file, once the Tomcat 8 server has exploded it).

       .. code-block:: xml

         <Context path="" useHttpOnly="false" />

      - `For Glassfish 4` :- Add :file:`glassfish-web.xml` under ODK Aggregate's WEB-INF directory with the content:

       .. code-block:: xml

         <?xml version="1.0" encoding="UTF-8"?>
         <glassfish-web-app>
             <session-config>
                 <cookie-properties>
                     <property name="cookieHttpOnly" value="false" />
                 </cookie-properties>
             </session-config>
         </glassfish-web-app>

      - `For Jetty` :- Add :file:`jetty-web.xml` under ODK Aggregate's WEB-INF directory with the content:

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
  

- `Configure your server and network devices <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_ so that laptops or Android devices connecting to the internet from an external access point can access your server. If your organization has a network or systems administrator, contact them for assistance. The steps for this are :-

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

    and restart the MySQL databaseserver. Then, download the `MySQL Connector/J`, unzip it, and copy the :file:`mysql-connector-java-x.x.x-bin.jar` file into the Tomcat server's libs directory. After copying it into that directory, you should stop and restart the Tomcat server. The `max_allowed_packet` setting defines the maximum size of the communications buffer to the server. The value used in the snippet above is 1GB, the maximum value supported. For ODK Aggregate 1.4.11 through 1.4.7, and 1.2.x, the maximum media (e.g., image or video) attachment is limited to the value you set for max_allowed_packet minus some unknown overhead -- e.g., a storage size of something less than 1GB. For ODK Aggregate 1.4.6 and earlier (excluding 1.2.x), the maximum media attachment is unlimited and the setting for max_allowed_packet does not need to be specified. For ODK Aggregate 1.4.12 and later, the max_allowed_packet value should be set to a value greater than 16842752 (this is the minimum value that should be used: 16MB plus 64kB); with that setting, media attachments of unlimited size are once again supported. If you are upgrading to a newer ODK Aggregate, you must continue to use the setting you already have, or 16842752, whichever is greater. If you experience problems uploading large attachments, change this setting to its maximum value, 1073741824.Finally, if you are using MySQL 5.7 or later, some of releases `expire all database passwords <https://dev.mysql.com/doc/refman/5.7/en/password-management.html>`_ after 360 days. Please verify the behavior of your version of MySQL and either change the password expiration policy or create a calendar reminder to change the password before it expires. For ODK Aggregate, you will need to re-run the installer to specify the new password. 

   - For PostgreSQL, download and install the appropriate binary package from `PostgreSQL download site <https://www.postgresql.org/download/>`_. Be sure to set the password for the postgres (root) user and set the default character set and collation sequence.
   - For either database, you should ensure that the default character set is configured to be UTF-8 and that the collation sequence (dictionary order) is set appropriately for your circumstances. If it isn't, any non-Latin characters may display as question marks. Refer to the character set and collation sections of your database's documentation for how to do this.
   - For Microsoft SQL Server or Azure SQL Server, you should configure these with UTF-8 character sets and to use Windows authentication. When using Windows authentication, the user under which the webserver executes must be granted permissions to access the SQL Server instance. The install wizard for ODK Aggregate will produce a Readme.html file that contains additional information on how to complete the configuration of the database and webserver service.

- Download and install `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest Featured release for your operating system.

.. note::

   The installer will guide you through configuring ODK Aggregate for Tomcat and MySQL/PostgreSQL/SQLServer. The installer will produce a WAR file (web archive) containing the configured ODK Aggregate server, a :file:`create_db_and_user.sql` script for creating the database and user that ODK Aggregate will use to access this database, and a :file:`Readme.html` file with instructions on how to complete the installation. 

.. tip::   
   
   - When asked for the fully qualified hostname of the ODK Aggregate server, you should enter the DNS name you established above. The install also asks for a database name, user and password. The user should not be root (MySQL) or postgres (PostgreSQL). ODK Aggregate will use this user when accessing this database (and it will only access this database). By specifying different databases and users, you can set up multiple ODK Aggregate servers that share the same database server, store their data in different databases, and operate without interfering with each other.
   - If you are upgrading to a newer version of ODK Aggregate, as long as you specify the same database name, user and password, you do not need to re-run the create_db_and_user.sql script (it only needs to be executed once).

