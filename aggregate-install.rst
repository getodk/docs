***********************************
Aggregate Installation and Setup
***********************************

Before going through this section, make sure you have used :doc:`ODK Collect  <collect-intro>` and are familiar with how it works.

.. tip::

  - Try the ODK Aggregate `demo server <https://opendatakit.appspot.com>`_ to explore the core functionality.
  - Decide whether to install a cloud instance or a local instance. It is strongly recommended to try an App Engine cloud instance first. If you wish to host locally, see :ref:`Aggregate Deployment Planning <deployment-planning>`
  - Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility.    
  - You must also plan for the security of your data and systems. And finally, it requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer-technical-support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.

.. _install-app-engine:

Installing on App Engine
--------------------------

1. Make sure `Java 8 <https://java.com/en/download/>`_ or higher is installed on your system. See `MacOSX Java install <https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html>`_ if you are a Mac user.
2. You will need a Gmail account to use App Engine; this Gmail account will be the owner of the Google Cloud Platform `project` under which your App Engine will execute. 

.. tip::

  - Google Cloud Platform hosts projects `under these terms <https://cloud.google.com/terms/>`_.
  - There is no cost to set up these projects and App Engine projects that are lightly used will incur no charges.

3. To set up a Google Cloud Platform project, go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner.

   .. image:: /img/aggregate-install/cloud-console.*
      :alt: An image showing the console option on the Google Cloud Platform.

4. You will now be asked to provide a Gmail account which you will use throughout. Sign in with a Gmail account which you wish to use.

   .. image:: /img/aggregate-install/email-select.*
      :alt: Image showing the sign in window of Gmail.

5. If you have never configured a Google Cloud Platform project, click on :guilabel:`Create an Empty Project`.

   .. image:: /img/aggregate-install/empty-project.*
      :alt: Image showing Create an empty project option for first projects. 

6. If you have configured a Google Cloud Platform project before, this link will open onto either a page with a :guilabel:`Create Project` button and a table listing all of your projects, or it will open into one of your existing projects. In the later case, click on that project name at the top of the window. In the below image, the older project is `Project-edu`.

   .. image:: /img/aggregate-install/project.*
      :alt: Image showing previous project name `Project-edu`.

7. On clicking on the project name (In this case `Project-edu`), a window appears with a :guilabel:`+` symbol. Click on it to create a new project.   

   .. image:: /img/aggregate-install/create-project.*
      :alt: Image showing the + sign which denotes creating a new project.

8. On the project-creation pop-up dialog, type in a project name that makes sense to you. You can enter a project name and click on :guilabel:`Create` if you don't want to edit the project-id. You can choose :guilabel:`Edit` if you want to edit the project id. The project id will be the first part of the URL to your ODK Aggregate server.

   .. image:: /img/aggregate-install/project-name.png
      :alt: Image showing the window to enter a project name.

9. If you click on :guilabel:`Edit`, a window will appear where you can enter a project id. After changing the project id click on :guilabel:`Create` to create your project.

   .. image:: /img/aggregate-install/project-id.*
      :alt: Image showing the window which comes after clicking on edit option to change the project id.

   .. tip::

      You may want to use a project id that combines your organization name and the name of your data collection group or project. You may also need to accept Google's terms-and-conditions.

10. After few seconds, you will see a notification in the top right corner of the window.
  
    .. image:: /img/aggregate-install/notification.*
       :alt: Image showing blue notification icon.

11. Click on the notification icon and select the first option from the dropdown menu then. The option is labelled as *Create Project:your project name*.

    .. image:: /img/aggregate-install/go-to-project.*
       :alt: Image showing the option to create your project.      

12. Upon creating the Google Cloud Platform project, you will be on an empty-project screen, showing the project info. If you want to change any settings, click on :guilabel:`Go to project settings`. Otherwise click on the menu icon (three horizontal bars) to the left of :guilabel:`Google Cloud Platform` in the upper left side of the screen.

    .. image:: /img/aggregate-install/project-settings.*
       :alt: Image showing the project settings option and the menu option.

13. Now and select :guilabel:`App Engine` from the dropdown menu.

    .. image:: /img/aggregate-install/app-engine.*
       :alt: Image showing App Engine option.

14. Click on the :guilabel:`Select a language` dropdown under the *Your first app* heading.

    .. image:: /img/aggregate-install/language-select.*
       :alt: Image showing option to select a language.

15. Now choose *Java*.

    .. image:: /img/aggregate-install/select-java.*
       :alt: Image showing various language options to choose from.

16. Select the datacenter location where this server will operate and click :guilabel:`Next`.

    .. image:: /img/aggregate-install/select-region.*
       :alt: Image showing options to choose a region where the server will operate.

17. Google will then begin configuring the server.

    .. image:: /img/aggregate-install/prepare-engine.*
       :alt: Image showing Google configuring the server.

18. When this completes, you will be directed to begin a tutorial to install a sample application. Choose :guilabel:`Cancel Tutorial` and confirm that you want to not perform that tutorial.

    .. image:: /img/aggregate-install/cancel-tutorial.*
       :alt: Image showing option to cancel the tutorial.

19. Download `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest release for your operating system.

    .. tip::

      - You can :doc:`verify the download <verify-downloads>` using *SHA256 signatures*.
      - If you are running OSX, you must unzip the downloaded file before running the installer within it.
      - If you are on MacOSX Mountain Lion or onward, you will need to fiddle with `GateKeeper settings <http://osxdaily.com/2012/07/27/app-cant-be-opened-because-it-is-from-an-unidentified-developer/>`_ in order to run the installer.
      - If you are on Windows 10, you will need to approve running an unsigned installer.
      - If you are on Linux, you will need to change the downloaded file's permissions to enable running it as a program. Right click on the file and click on :guilabel:`Properties`. Click on :guilabel:`Permissions` tab. Now check the box labelled as :guilabel:`Allow executing file as program`. Now double click on the file to run it.

20. The installer will guide you through configuring ODK Aggregate for App Engine. Click on :guilabel:`Forward` button each time you complete a step to move ahead.

    .. image:: /img/aggregate-install/setup.*
       :alt: Image showing the installer for ODK Aggregate.

21. Accept the license agreement and click on :guilabel:`Forward` button.

    .. image:: /img/aggregate-install/agreement.*
       :alt: Image showing license agreement.

22. Select a parent directory under which an *ODK Aggregate* directory will be created to contain the configured software. Click on the :guilabel:`folder` icon to choose a directory.

    .. image:: /img/aggregate-install/directory-setup.*
       :alt: Image showing window to choose a parent directory. 

23. In the next window choose *Google App Engine* as the platform for the Aggregate server.

    .. image:: /img/aggregate-install/choose-platform.*
       :alt: Image displaying options to choose a platform for Aggregate.

24. Enter a name for your ODK Aggregate instance.

    .. image:: /img/aggregate-install/set-name.*
       :alt: Image showing window to select a name for your Aggregate instance.

    .. note::    
   
      The ODK Aggregate instance name will be displayed to your users when they log into ODK Aggregate using their username and password.

    .. tip::
   
      Including the name of your organization in the instance name can help users confirm that they have contacted the correct website.

25. Enter a superuser name in the next window.

    .. image:: /img/aggregate-install/superuser.*
       :alt: Image showing window to enter a superuser name.

    .. note::
   
      - The user with the superuser account will have full permissions on the system.
      - The password for this user will be set to **aggregate** initially.
      - Only this user will be allowed to log onto the system when ODK Aggregate is run for the first time.
      - Upon first logging in, the superuser should change the password and complete the configuration of ODK Aggregate by specifying additional users and what permissions they will have on the system.

26. In the next window enter the project id of the project you created on the Google Cloud platform.

    .. image:: /img/aggregate-install/application-id.*
       :alt: Image showing project id of the project created earlier entered in the application id box.

27. Now the installer will configure Aggregate and launch a upload tool.  

    .. tip::

      Beginning with Java 7 Update 51, there are security level settings that may prevent the upload tool from running. A reported workaround is to add the *file: path* (e.g., :file:```file:///```) to the Exception Site list.

28. Enter the Gmail account in the upload tool that you specified to use the App Engine. This will enable the :guilabel:`Get Token` button.

    .. image:: /img/aggregate-install/get-token.*
       :alt: Image showing the window for upload tool to enter the email id and get a token.

29. Click the :guilabel:`Get Token` button. Two things happen after this:

  a. Your default browser will open to a Google site (accounts.google.com) where you are asked to choose a Gmail account (select the account specified by you to use the App Engine), and then approve allowing *Google App Engine appcfg* to view and manage your AppEngine instances and datastores. Click :guilabel:`Allow`. This will take you to a screen with instructions to copy a code.
  b. At the same time, a pop-up dialog should be displayed by the upload tool. 

     .. tip::

       - If the pop-up dialog does not show, close the upload tool and open a file browser or Finder window in the directory you specified for the installer to place its files. Navigate to the ODK Aggregate directory.
       - If on Windows, double-click the :file:`ODKAggregateAppEngineUpdater.jar` file. 
       - If on Mac OSX, double-click the uploadAggregateToAppEngine.app file. 
       - If on Linux, open a bash shell and run uploadAggregateToAppEngine.sh. These should all re-launch the upload tool. 
       - Re-enter the e-mail address, and once again click :guilabel:`Get Token`. The pop-up dialog should now appear.

30. Copy the code from the browser into the upload tool's pop-up dialog and click :guilabel:`OK`.

    .. image:: /img/aggregate-install/token.*
       :alt: Image showing pop-up dialog to enter a token.

    .. tip::
    
      The text box on Google's site is not as wide as the code; be sure to copy the entire code.

31. The output should look something like that in the image.
  
    .. image:: /img/aggregate-install/success-output.*
      :alt: Image showing output for a successful result.

    .. tip::
  
      - If the output does not look like that, you may have delayed too long between getting the code and pasting it into the tool. Click :guilabel:`Delete Token` and try again.
      - If you see a failure message in the output window, then it is likely that you have several different Gmail accounts and Google has gotten confused during the token-issuing process. In this case, when the browser window opens, before selecting an account, copy the URL, open a Private Browsing or Incognito Window in your browser, and paste the URL into that. Then proceed to get the token, etc. This should fix this issue.

32. Now click :guilabel:`Upload ODK Aggregate`.

    .. image:: /img/aggregate-install/upload.*
      :alt: Image showing successful output and upload option.

    .. note::

      - Clicking on :guilabel:`Upload ODK Aggregate` will spew a very long list of progress messages into the Output window. The `listBackends :` and `deleteBackendBackground :` sections may report "500 Internal Server Error" and Severe errors, and Warnings about the use of Backends, a deprecated feature. This is expected. Here is a list of few of those errors:
   
      .. code-block:: none

        listBackends : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

      .. code-block:: none
       
        listBackends! : WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&   
        listBackends! : 500 Internal Server Error

      .. code-block:: none
   
        listBackends : Unable to list backends: Error posting to URL: https://appengine.google.com/api/backends/list?app_id=project-123-181306&
        listBackends : 500 Internal Server Error

      .. code-block:: none
   
        deleteBackendBackground : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

      .. code-block:: none
   
        deleteBackendBackground!: WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&
        deleteBackendBackground!: 400 Bad Request      

      .. code-block:: none
      
        deleteBackendBackground : Unable to delete backend: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306& 
        deleteBackendBackground : 400 Bad Request     
           

      - Toward the bottom, the *update :* section should not report errors and at the end, a *status : Action Succeeded!* line should be written. This indicates that the upload completed successfully. 
      - To get a more clear view, you can see an `example log <https://opendatakit.org/wp-content/uploads/Apr2016-GoogleCloud/exampleUploadScriptOutput.txt>`_. 
   
    
33. Once the updater script has run and uploaded the ODK Aggregate configuration to App Engine, return to the Google Cloud Platform console. With the console displaying your project, click on the menu icon (three horizontal bars) to the right of *Google Cloud Platform* in the upper left side of the screen and select App Engine from the menu.

34. Click on :guilabel:`ALLOW` in the next window.

    .. image:: /img/aggregate-install/allow.*
       :alt: Image showing window asking for App Engine Permissions.

35. Click on the project-id URL in the top right corner of the window.

    .. image:: /img/aggregate-install/project-aggregate.*
       :alt: Image showing a window where server url is displayed on top right corner.

36. You will go to now your ODK Aggregate server. You can click on :guilabel:`Log In` to log in, enter the ODK Aggregate username (superuser) that you specified within the installer (the initial password for this username will be aggregate) and access the site administration screens for your server.  

    .. image:: /img/aggregate-install/server.*
       :alt: Image showing ODK Aggregate server and log in option.

.. _change-size:

Changing size of App Engine Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have many form definitions on your server, you may get better performance and reduce the likelihood of data corruption if you increase the size of your server.

.. note::

   - Data corruption is generally caused by the premature termination of an action (e.g., saving of a submission) because it took longer than the allotted time. The likelihood of data corruption occurring is tied to the quantity of form definitions on the server, the size of the individual submissions, the number of devices simultaneously submitting data, and the speed of the network. Increasing the web server size enables it to handle larger workloads faster, which can reduce the likelihood of hitting this time limit thereby avoiding data corruption.
   - For data corruption caused by slow network speeds, you might also be able to change more aspects of the App Engine configuration (specified in these files) to make your web server always-available and to replace it with a Bx instance that does not have an automatic request time limit (the documentation provided by Google is currently unclear on whether this is still possible with the new services constructions).

To change Google App Engine configuration, you must edit the configuration files produced by the installer and re-run the uploader script to push the changes to Google's servers. There are two server settings that can be changed:
  
- **Web Server Size**: The web server handles all browser interactions and all data-submission and form-download requests from ODK Collect and ODK Briefcase. Increasing the size of the web server should reduce the likelihood of data corruption if it is not caused by slow network speeds. To change the Google App Engine web server size, go to the folder you specified to the installer. Within that folder, navigate to :file:`ODKAggregate/default/WEB-INF`. Within that directory, there will be a file :file:`appengine-web.xml`. Open that file in a text editor like Notepad++ or Notepad. The file contents will look something like:

 .. code-block:: xml

   <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
     <application>opendatakit-simpledemo</application>
     <module>default</module>
     <version>1</version>

  	 <instance-class>F2</instance-class>
   ...
 
 To change the size of the web server, replace **F2** with a different instance class size. There are several different instance classes available. Select from among the instance classes beginning with the letter **F**. See `instance classes <https://cloud.google.com/appengine/docs/about-the-standard-environment#instance_classes>`_  for their descriptions or search for `Google AppEngine instance classes standard environment` on the web. Then re-run the upload tool within the ODKAggregate folder either by double-clicking the :file:`ODKAggregateAppEngineUpdater.jar` file (Windows), or double-clicking the :file:`uploadAggregateToAppEngine.app` file (Mac OSX), or double-clicking the :file:`uploadAggregateToAppEngine.sh` file (linux). Once you have uploaded these changes to App Engine, your server will be running on the instance size that you have specified.

- **Background Server Size**: App Engine deployments use a "background" copy of the website to process long-running actions like generating CSV and KML files for export and for publishing all accumulated data to an external server. If you experience difficulty exporting to CSV or KML, the size of that server will also need to be updated. In that case, go to :file:`ODKAggregate/background/WEB-INF`. Within that directory, there will be a slightly different file with the same :file:`appengine-web.xml` filename. Open that file in a text editor like Notepad++ or Notepad. The file contents will look something like:

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

To run on ODK Aggregate on a Tomcat server backed with a MySQL or PostgreSQL database follow the following steps:

1. Define your server requirements and install your server.
   
   - **Availability**: Decide the availability of your server depending on how frequently you want to update and upload forms. If you do need a high-availability server, you need to talk to your Internet Service Provider (ISP) as to their availability guarantees.
   - **Data Loss**: Your tolerance to data loss will impact your backup schedule and your server hardware.  Invest in a storage system based on your tolerance to data loss. Seek technical assistance for these requirements. If you cannot tolerate any data loss, or less than 24 hours of data loss, you should invest in a RAID storage array with battery-backed controller cards. If you can tolerate a day or longer interval of data loss, be sure you have a periodic tape or other means of backup for your system that matches or is shorter than the data loss interval.
   - **Dataset Size**: The quantity of data you intend to collect will affect the size of the machine required to host the ODK Aggregate instance and of your database server. For most applications, the default size should be fine. If you are collecting more than 6000 submissions, you may need to increase the JVM size. Note that the maximum size of the JVM is limited by the size of the physical memory on your machine.
   - **Secure and Protected Data**: If you need to prevent eavesdroppers from seeing your data as it is transmitted to your ODK Aggregate instance, you should either (1) only connect to ODK Aggregate from within your organization's network (when the ODK Collect devices are on your premises), (2) obtain an SSL certificate and install it on your Tomcat server (a certificate is required to secure transmissions over https:), or (3) use `Encrypted Forms <https://opendatakit.org/help/encrypted-forms/>`_. If you are not using encrypted forms and are handling sensitive data, a computer security specialist should review your system and your security procedures. When operating without an SSL certificate, do not access ODK Aggregate from a remote location when changing passwords.

2. Install Tomcat on your server.

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
          $ sudo tasksel install tomcat
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
  

3. `Configure your server and network devices <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_ so that laptops or Android devices connecting to the internet from an external access point can access your server. If your organization has a network or systems administrator, contact them for assistance. The steps for this are:

  - configure your server firewall to allow access
  - make your server visible on the internet (optional)
  - establish a DNS name for the server

4. `Obtain and Install <https://gist.github.com/yanokwa/399a7fcbc3d9ad8a0bd3>`_ an SSL certificate if you need secure (https:) access.

5. Select and Install your database server (MySQL or PostgreSQL or Microsoft SQL Server or Azure SQL Server).

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

6. Download and install `ODK Aggregate <https://opendatakit.org/downloads/>`_. Select the latest Featured release for your operating system.

   .. note::

      The installer will guide you through configuring ODK Aggregate for Tomcat and MySQL/PostgreSQL/SQLServer. The installer will produce a WAR file (web archive) containing the configured ODK Aggregate server, a :file:`create_db_and_user.sql` script for creating the database and user that ODK Aggregate will use to access this database, and a :file:`Readme.html` file with instructions on how to complete the installation. 

   .. tip::   
   
      - When asked for the fully qualified hostname of the ODK Aggregate server, you should enter the DNS name you established above. The install also asks for a database name, user and password. The user should not be root (MySQL) or postgres (PostgreSQL). ODK Aggregate will use this user when accessing this database (and it will only access this database). By specifying different databases and users, you can set up multiple ODK Aggregate servers that share the same database server, store their data in different databases, and operate without interfering with each other.
      - If you are upgrading to a newer version of ODK Aggregate, as long as you specify the same database name, user and password, you do not need to re-run the :file:`create_db_and_user.sql` script (it only needs to be executed once).

.. _install-aws:

Installing on AWS (Cloud)
--------------------------

Following are basic details on setting up ODK Aggregate to run on a Linux micro-instance on the Amazon Web Services EC2 infrastructure. 

For screenshots and more on the general set-up of Tomcat on AWS, see the excellent three-part `Cat in the cloud Apache Tomcat Series <http://www.excelsior-usa.com/articles/tomcat-amazon-ec2-basic.html>`_. `Amazon’s getting-started guides <https://aws.amazon.com/documentation/gettingstarted/>`_ are also quite helpful.

1. First, sign up for Amazon Web Services EC2 at `<http://aws.amazon.com/ec2/>`_.

   .. note::

    - You will need to confirm a working phone number. 
    - If you want to use a U.S. number but are presently overseas, you can use a Google Voice number routed to Google Chat.

2. Go to the AWS/EC2 management console and note your region (shown in the upper-left).
3. Launch a new instance with the :guilabel:`Launch Instance` button prominently displayed on the EC2 console home screen. Accept the default behavior and use the quick-launch wizard.
4. For the launch configuration, choose the :guilabel:`Amazon Linux AMI: EBS-Backed (64-bit)` option. This is one of the instance types that you can run on a micro-instance as part of their `free tier <http://aws.amazon.com/free/>`_. Leave everything else at the defaults, including the instance type. The instance type will default to *t2.micro* which is a small, limited instance that can be run for free. For a price, you can upgrade the instance type later if you need better performance.

   .. note::

     The exact AMI name and ID will depend on your region. 

5. Create a new key pair, download the private key, and keep the private key safe. This will be your only method of communicating with your new instance and you will not be allowed to download it again.
6. After creating the instance, add security rules for allowing both HTTP and HTTPS. Choose the :guilabel:`Security Groups` tab and click on the auto-created security group associated with your new instance. This might have been called *launch-wizard-1*. If you’re not sure, you can go to the Instances tab to see which Security Group is listed for the new instance.
  
   In the properties pane at the bottom, click on the :guilabel:`Inbound tab`, select HTTP from the :guilabel:`create a new rule` drop-down, then click :guilabel:`Add Rule`. Do the same for HTTPS. Then click :guilabel:`Apply Rule Changes`.

   .. tip::

    To avoid potential problems with MTU settings and packet loss, also add a rule to allow *All ICMP*. Add a rule for both IPv4 and IPv6. After you create the new rule, click :guilabel:`Apply Rule Changes`.

   .. note::

    Tomcat defaults to listening on nonstandard ports 8080 and 8443. Below will be instructions to use the standard HTTP and HTTPS ports instead. However, if you want to leave Aggregate on the non-standard ports, you can certainly do so; in that case, simply add two additional security rules to allow access via 8080 and 8443.

7. Switch to the :guilabel:`Instances` tab, click on your instance, and note its Public DNS Address in the properties pane below. This is the default address that you will use to access your instance.
8. Presuming that you want a friendlier way to access your instance, allocate it an *elastic IP* and domain name. Navigate to Elastic IPs and click :guilabel:`Allocate New Address`. Associate it with your new instance.  Note your new IP. Also, if possible, configure DNS to route one or more names to this address. You can then use this IP and/or name to access your instance (and can forget the Public DNS Address assigned by AWS).

   .. note:: 

     The IP is free so long as you keep it associated with a running instance. If you stop your instance and do not release the IP address for others to use (in essence, wasting it), then Amazon will begin charging you for holding the unused address.

   .. tip::

     When you set up Aggregate below, you will need to configure it with the domain name you will use to access it. Thus, it is best if you configure the domain name first.

9. Connect to your instance. Go to the :guilabel:`Instances` tab and select :menuselection:`Connect` from the Instance Actions drop-down (alternatively, you can right-click on the instance and choose Connect). From here AWS presents you with several options.
 
   - The easiest is to connect using their Java SSH client. If you choose that option, you just have to specify the location of your private key file (created above) and AWS launches an in-browser SSH client to connect to your instance.
   - You can also select to connect with a stand-alone SSH client. If you choose this option, AWS will provide extremely helpful instructions, including an SSH command that you can cut and paste into your local command window. It will also inform you that you may need to update the permissions on your local private key file in order for the ssh client to run properly, and it will even give you the command to run (e.g., :command:`chmod 400 xxx.pem`).
   - Once you connect, you will probably be told that there are new security updates to install. You can run :command:`sudo yum update` to install these updates, as it advises.

10. Transfer files to/from your instance. When you login via ssh, you will default to being in the (empty) ec2-user home directory. You will want to be able to transfer files between here and your local directory. You have several options.
 
    - If you’re using the command-line ssh, you can also use the command-line scp to copy files. The syntax is similar to ssh, but of course you also need to specify the source and destination file paths.
    - An easier option is to use an FTP program like FileZilla (as long as it supports SFTP). To configure FileZilla to connect to your instance, go into :menuselection:`Edit-->Settings/Preferences-->Connection-->SFTP` and add your private key to FileZilla’s keystore (it will offer to convert the key format, which you should accept). Then, go into Site Manager and create a new site. The host should be the IP, name, or Public DNS for your instance, the port can be blank, the protocol should be **SFTP – SSH File Transfer Protocol**, the login type should be Normal, and the user should be **ec2-user**. Everything else should be left at the defaults, including the password (which will be blank). When you connect, the default directory will be the ec2-user’s home directory, but you can also navigate to other directories.

11. Install Tomcat 6. This can be done by running :command:`sudo yum install tomcat6`. This installs configuration files into :file:`/etc/tomcat6` and other files into :file:`/usr/share/tomcat6`. Log files go into :file:`/var/log/tomcat6`.

12. Install MySQL. This can be done by running:

 .. code-block:: console
  
   $ sudo yum install mysql mysql-server

 Now use vi or an editor to edit :file:`/etc/my.cnf` (e.g., :command:`sudo vi /etc/my.cnf`). In the [mysqld] section, add (the max_allowed_packet allows up to a 4GB file attachment):

 .. code-block:: none

   character_set_server=utf8
   collation_server=utf8_unicode_ci
   max_allowed_packet=1073741824

13. Run MySQL. To run MySQL:

   .. code-block:: console
  
     $ sudo service mysqld start

14. Install and transfer ODK Aggregate files.

    - First, install ODK Aggregate on your local computer (not on your AWS instance).
  
    .. note::
  

      During set-up, it’s important to specify that this will be a MySQL installation, and it is also very important that you specify the correct domain name or IP address that will be used to access your Aggregate server. Ideally, this will be a specific domain name that you have already mapped to an elastic IP (and can re-map later if you change the IP).

    - The installation will create a :file:`create_db_and_user.sql` file. Upload this to your ec2-user home directory as described in point 10.
    - The installation will also create an :file:`ODKAggregate.war` file. Rename this to :file:`ROOT.war` and upload it to the :file:`/usr/share/tomcat6/webapps` folder. If you receive a *Permission Denied* error, you might need to execute :command:`chmod -R 755` or something similar for the webapps folder.
    - After :file:`ROOT.war` has been copied to the server, you need to make sure tomcat has permission to use it. Run :command:`sudo chown tomcat ROOT.war` and :command:`sudo chgrp tomcat ROOT.war` in the webapps directory to ensure this is the case.

15. Configure MySQL.

    - On your AWS instance, run :file:`/usr/bin/mysql_secure_installation` to set a root password and generally secure your MySQL installation.
    - Then, run :command:`mysql –u root -p` to log in to MySQL (specifying the password you just set), and type :command:`source ~/create_db_and_user.sql`. This will create the ODK user and database. Type :command:`quit` on the mysql prompt to quit from MySQL.
    - Finally, run :command:`sudo /sbin/chkconfig --levels 235 mysqld on` to auto-start MySQL whenever your instance boots up.

16. Configure Tomcat.

    - Download the MySQL Connector/J from the `MySQL download page <http://dev.mysql.com/downloads/connector/j/)>`_ unzip it, and transfer the :file:`mysql‐connector‐java‐x.x.x‐bin.jar` file up to your instance’s :file:`/usr/share/tomcat6/lib` directory.
    - Edit :file:`/etc/tomcat6/server.xml` in order to customize settings. (If you’re not used to Linux text editors, you can always download the file, edit it, and upload it back.)
    - Assuming that you want to run Aggregate on the standard HTTP port (80) and HTTPS port (443):

      - Change “<Connector port="8080" protocol="HTTP/1.1"” to “<Connector port="8080" proxyPort="80" protocol="HTTP/1.1"” (i.e., add the proxyPort attribute).
      - If you are using SSL, also change “<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true"” to “<Connector port="8443" proxyPort="443" protocol="HTTP/1.1" SSLEnabled="true"”.
      - Execute the following commands to have Linux forward to the ports on which Tomcat listens:
      
       .. code-block:: console

         $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
         $ sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8443
         $ sudo /sbin/service iptables save

      - If you have an SSL certificate for HTTPS support:

        - Make sure that the “<Connector port="8443"” part of the configuration file is not commented out. If it is, un-comment it.
        - Upload your SSL keystore file and the certificate(s) to the server.
        - Install it as instructed. (If you buy from RapidSSL, for example, they provide you with Tomcat installation instructions. E.g., you may need to download a special P7S certificate file, then install it on the server with “keytool -import -alias YOURALIAS trustcacerts file xxxxx.p7s -keystore xxxxx.keystore”.)
        - In the “<Connector port="8443"” part of the configuration file, specify the location of your keystore file and password (e.g., “keystoreFile="/…/xxxxx.keystore" keystorePass="changeit"”).

    - Start Tomcat with :command:`sudo service tomcat6 start`.
    - Configure Tomcat to auto-start when the instance boots with :command:`sudo chkconfig --level 345 tomcat6 on`.

17. Login and test. At this point, you should be able to login to your AWS-hosted Aggregate instance by going to its name or IP in your web browser (with or without HTTPS, depending on your set-up).

    .. note::  

      For your first login, you will need to login with the Google account you specified during the Aggregate installation process. Then you can add additional users from the :guilabel:`Site Admin` tab.

    Once you have confirmed that your Aggregate instance is working, you can back it up by creating an image of the instance (an AMI). You can do this by going to the :guilabel:`Instances` tab in the AWS-EC2 console, then selecting the :guilabel:`Create Image (EBS AMI)` Instance Action for your instance.

18. Further set-up for production servers:

  - You will want to create a system to monitor and manage the log files in :file:`/var/log/tomcat6`.
  - You will also want to create a system for regular back-ups and a plan for how to restore them when needed. This will be needed to safely back up the MySQL database, which may be in-use at any given time.

  .. note::

    - The micro instance is only free for 12 months from AWS sign-up, and that you may exceed the free quotas on disk space or network bandwidth before that point (`see <http://aws.amazon.com/free/>`_).
    - You may at some point need to upgrade your instance to a standard instance if the micro instance is not providing enough performance.


