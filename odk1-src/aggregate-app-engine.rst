:orphan:

Installing Aggregate on Google App Engine
=========================================

.. warning::

  This document only applies ODK Aggregate v1.x. See `why we are removing App Engine support <https://forum.getodk.org/t/upcoming-changes-to-aggregate/17582>`_ for more information.

.. note::

  There is no charge to set up an Aggregate server on App Engine, and lightly used instances will usually incur no charges.


.. admonition:: Before you begin...

  - Make sure Java 8.0.221 or higher is installed on your system. We recommend using `OpenJDK 11 LTS <https://adoptopenjdk.net/>`_ from AdoptOpenJDK.

  - You will need a Gmail account to use App Engine. This Gmail account will be the owner of the Google Cloud Platform project under which your App Engine will execute.

  - You will need to provide a credit card or banking details to verify your identify to the Google Cloud Platform.

  - Read the `Google Cloud Platform terms of service <https://cloud.google.com/terms/>`_.

  .. _download-aggregate-installer:

  - Download the `ODK Aggregate installer <https://github.com/getodk/aggregate/releases/latest>`_. Select the latest release for your operating system.

1. Go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner.

   .. image:: /img/aggregate-install/cloud-console.*
     :alt: An image showing the console option on the Google Cloud Platform.

#. Sign in with the Gmail/Google account you wish to use.

   .. image:: /img/aggregate-install/email-select.*
     :alt: Image showing the sign in window of Gmail.

#. If you have never configured a Google Cloud Platform project, click on :guilabel:`Create an Empty Project`.

   .. image:: /img/aggregate-install/empty-project.*
     :alt: Image showing Create an empty project option for first projects.

#. If you have configured a Google Cloud Platform project before, you may see a listing of all your projects and a button labeled :guilabel:`Create Project`. Click that button.

   If instead you see the console for one of your existing projects, click on the project name at the top of the window. In the example image below, the older project is `Project-edu`.

   .. image:: /img/aggregate-install/project.*
     :alt: Image showing previous project name `Project-edu`.

   - Upon clicking the project name, a window appears with a :guilabel:`+` symbol. Click on it to create a new project.

     .. image:: /img/aggregate-install/create-project.*
       :alt: Image showing the + sign which denotes creating a new project.

#. Name your project.

   On the project-creation popup dialog, type in a project name that makes sense to you. If you want to edit the project ID, which will be a part of your project URI, click the small :guilabel:`Edit` link. When you are done, click :guilabel:`Create`.

   .. image:: /img/aggregate-install/project-name.png
     :alt: Image showing the window to enter a project name.

   .. tip::

     You may want to use a project id that combines your organization name and the name of your data collection group or project.


#. After few seconds, you will see a notification in the top right corner of the window. Click on the notification icon and select the notification message **Create Project: project-name**. An empty project screen will open.

   .. image:: /img/aggregate-install/notification.*
     :alt: Image showing blue notification icon.

   .. image:: /img/aggregate-install/go-to-project.*
     :alt: Image showing the option to create your project.

#. Click on the menu icon (:guilabel:`☰`) to the left of :guilabel:`Google Cloud Platform` in the upper left side of the screen, and select :guilabel:`App Engine` from the dropdown menu.

   .. image:: /img/aggregate-install/app-engine.*
     :alt: Image showing App Engine option.

#. Open the :guilabel:`Select a language` menu and select :guilabel:`Java`.

   .. image:: /img/aggregate-install/language-select.*
     :alt: Image showing option to select a language.

   .. image:: /img/aggregate-install/select-java.*
     :alt: Image showing various language options to choose from.

#. Select your preferred datacenter location and click :guilabel:`Next`.

   .. image:: /img/aggregate-install/select-region.*
     :alt: Image showing options to choose a region where the server will operate.

   Google will then configure the server. This may take a moment.

    .. image:: /img/aggregate-install/prepare-engine.*
      :alt: Image showing Google configuring the server.

#. When this completes, you will be directed to begin a tutorial to install a sample application. Choose :guilabel:`Cancel Tutorial` and confirm that you want to not perform that tutorial.

   .. image:: /img/aggregate-install/cancel-tutorial.*
     :alt: Image showing option to cancel the tutorial.

#. Launch the ODK Aggregate installer on your computer. (:ref:`See download info here. <download-aggregate-installer>`)

    .. tabs::

     .. group-tab:: Linux

	Before launching, change the installer's permissions to enable running it as a program:

	1. Right click on the file.
	2. Select :menuselection:`Properties --> Permissions`.
	3. Check :guilabel:`Allow executing file as program`.

	Or, from a terminal, go to the directory where you downloaded the installer and change permissions:

	.. code-block:: console

	  $ chmod 554 "ODK Aggregate vN.N.N linux-installer.run"

	(Use actual name of the file, which will be different.)

     .. group-tab:: macOS

	1. Unzip the downloaded file before running the installer within it.
	2. When you attempt to run the installer, macOS will prevent it. Go to :menuselection:` --> System Preferences --> Security & Privacy` to enable running the installer.

     .. group-tab:: Windows

	On launch, you may need to approve running an unsigned installer.

   The installer will guide you through configuring ODK Aggregate for App Engine. Click on the :guilabel:`Forward` button each time you complete a step to move ahead.

   .. image:: /img/aggregate-install/setup.*
      :alt: Image showing the installer for ODK Aggregate.

#. Accept the license agreement.

   .. image:: /img/aggregate-install/agreement.*
     :alt: Image showing license agreement.

#. Select a parent directory under which an :file:`ODK Aggregate` directory will be created to contain the configured software. Click on the :guilabel:`folder` icon to choose a directory.

   .. image:: /img/aggregate-install/directory-setup.*
     :alt: Image showing window to choose a parent directory.

#. Select :guilabel:`Google App Engine` as the platform for the Aggregate server.

   .. image:: /img/aggregate-install/choose-platform.*
     :alt: Image displaying options to choose a platform for Aggregate.

#. Enter a name for your ODK Aggregate instance.

   .. image:: /img/aggregate-install/set-name.*
     :alt: Image showing window to select a name for your Aggregate instance.

   .. note::

    - The Aggregate instance name will be displayed to your users when they log into Aggregate using their username and password.
    - The instance name does not need to be the same as the Project Name you set in Google App Engine. However, it might be helpful to use the same name.

   .. tip::

     Including the name of your organization in the instance name can help users confirm that they have contacted the correct website.

#. Enter a superuser name in the next window.

   .. image:: /img/aggregate-install/superuser.*
    :alt: Image showing window to enter a superuser name.

   .. note::

     - The superuser will have full permissions on the system.
     - The password for this user will be set to ``aggregate`` initially.
     - Only this user will be allowed to log onto the system when Aggregate is run for the first time.
     - Upon first logging in, the superuser should change the password and complete the configuration of Aggregate by specifying additional users and what permissions they will have on the system.

#. Enter the ID of the project you created on the Google Cloud platform.

   .. image:: /img/aggregate-install/application-id.*
     :alt: Image showing project id of the project created earlier entered in the application id box.

   The installer will configure Aggregate and launch an upload tool.

   .. tip::

     Depending on your Java version, security settings may prevent the upload tool from running.
     A possible workaround is to add ``file://`` to the `Exception Site List <https://blogs.oracle.com/java-platform-group/upcoming-exception-site-list-in-7u51>`_.

#. Enter the Gmail account that you specified when setting up the App Engine project and click the :guilabel:`Get Token` button.

   .. image:: /img/aggregate-install/get-token.*
     :alt: Image showing the window for upload tool to enter the email id and get a token.

   Your default browser will open a Google dialog screen asking you to choose a Gmail account. Select the account you specified earlier when setting up App Engine, and then allow *Google App Engine appcfg* to view and manage your App Engine instances and datastores. Click :guilabel:`Allow`. This will take you to a screen with instructions to copy a code.

   .. image:: /img/aggregate-install/allow.*
     :alt: Image showing window asking for App Engine Permissions.

   At the same time, the install wizard should display a popup dialog box.

   .. tip::

     If the popup dialog does not appear, relaunch the upload tool:

     .. tabs::

       .. group-tab:: Linux

	 1. Close the upload tool.
	 2. Open a terminal.
	 3. :command:`cd` to the directory you specified earlier.
	 4. run :file:`uploadAggregateToAppEngine.sh`

       .. group-tab:: macOS

	 1. Close the upload tool.
	 2. Open a Finder window.
	 3. Navigate to the directory you specified earlier.
	 4. Run :program:`uploadAggregateToAppEngine.app`

       .. group-tab:: Windows

	 1. Close the upload tool.
	 2. Open a file explorer window.
	 3. Navigate to the directory you specified earlier.
	 4. Double-click :program:`ODKAggregateAppEngineUpdater.jar`

     Re-enter the email address, and click :guilabel:`Get Token` again.
     The popup dialog should now appear.

#. Copy the code from the browser into the installer's popup dialog and click :guilabel:`OK`.

    .. image:: /img/aggregate-install/token.*
      :alt: Image showing pop-up dialog to enter a token.

    .. tip::

      The text box on Google's site is not as wide as the code. Be sure to copy the entire code.

#. If everything went well, you should see a status message letting you know the ``Action Succeeded``.

   .. image:: /img/aggregate-install/success-output.*
     :alt: Image showing output for a successful result.

   .. tip::

     - If the output does not look like that, you may have waited too long between getting the code and pasting it into the tool. Click :guilabel:`Delete Token` and try again.

     - If you see a failure message in the output window, it is likely that you have several different Gmail accounts and Google has gotten confused during the token-issuing process. In you suspect this is the case, click :guilabel:`Delete Token` and try again:

       1. When the browser window opens, before selecting an account, copy the URL.
       2. Open a Private Browsing or Incognito Window in your browser.
       3. Paste the URL into the private window.
       4. Proceed with the other steps as above.

#. Click :guilabel:`Upload ODK Aggregate`.

   .. image:: /img/aggregate-install/upload.*
     :alt: Image showing successful output and upload option.

   Clicking on :guilabel:`Upload ODK Aggregate` will generate a long list of progress messages in the Output window. You will see a number of warnings and errors. Don't worry, this is expected.

   For reference, here is a list of few of those errors:

   .. code-block:: none
     :class: details

       listBackends : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

       listBackends! : WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&
       listBackends! : 500 Internal Server Error

       listBackends : Unable to list backends: Error posting to URL: https://appengine.google.com/api/backends/list?app_id=project-123-181306&
       listBackends : 500 Internal Server Error

       deleteBackendBackground : Warning: This application uses Backends, a deprecated feature that has been replaced by Modules, which offers additional functionality. Please convert your backends to modules as described at: https://developers.google.com/appengine/docs/java/modules/converting.

       deleteBackendBackground!: WARNING: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&
       deleteBackendBackground!: 400 Bad Request

       deleteBackendBackground : Unable to delete backend: Error posting to URL: https://appengine.google.com/api/backends/delete?backend=background&app_id=project-123-181306&
       deleteBackendBackground : 400 Bad Request


#. Finally, you should see the message ``status : Action Succeeded!``.

#. Once the installer has run and uploaded the ODK Aggregate configuration to App Engine, return to the Google Cloud Platform console.

#. Open your Aggregate server from your project's screen, by selecting :menuselection:`☰ --> App Engine` and clicking on the project's URI.

   .. image:: /img/aggregate-install/project-aggregate.*
     :alt: Image showing a window where server URI is displayed on top right corner.

#. :guilabel:`Log In` with the superuser username that you specified in the installer (the initial password for this username will be ``aggregate``), and access the site administration screens for your server.

   .. image:: /img/aggregate-install/server.*
     :alt: Image showing ODK Aggregate server and log in option.

#. Go to :menuselection:`Site Admin -> Permissions` to change your password. You can also add additional users.
