Application Designer Prerequisites
===================================

.. _app-designer-prereqs:

You must install the following software on your computer in order to use Application Designer:

  - |java_link| - Java is required by the Android SDK
  - |chrome_link| - Google's :program:`Chrome` browser.
  - |nodejs_link| - a framework for easily building fast, scalable applications. Download Version 6.2.2 or higher and install it from NodeJS
  - |grunt_link| - a task-based scripting environment (installation is described below).
  - |android_sdk_link| - the software development kit for Android devices (installation is described below).

.. |java_link| raw:: html

  <a href="https://java.com/en/download/" target="_blank">Java</a>

.. |chrome_link| raw:: html

  <a href="https://www.google.com/intl/en/chrome/browser/desktop/index.html" target="_blank">Chrome</a>

.. |nodejs_link| raw:: html

  <a href="https://nodejs.org/en/" target="_blank">NodeJS</a>

.. |grunt_link| raw:: html

  <a href="https://gruntjs.com/" target="_blank">Grunt</a>

.. |android_sdk_link| raw:: html

  <a href="https://developer.android.com/studio/index.html" target="_blank">Android SDK</a>

.. warning::

  It is tricky to foresee all the issues that can crop up on many different machines and setups. If something in this process does not go as expected, please check the |forum|_.

.. warning::

  Android Studio is not supported on the Windows Linux subsystem, so you will not be able to run Application Designer if you are using it. 

.. _app-designer-prereqs-java:

Java
--------
Make sure Java 8 or higher is installed on the computer you plan to use. If it is not, `download and install it <https://java.com/en/download/>`_. If you are using MacOSX, it may require special care and attention. See `MacOSX Java install <https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html>`_ and `MacOSX Java FAQ <https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_install_faq.html>`_.

.. _app-designer-prereqs-nodejs:

NodeJS
---------
You must use Version 12 or higher. To avoid directory path problems on Windows, we require :program:`npm` version 6.9 or higher (generally npm will be bundled with NodeJS installer). Follow the `instructions to install NodeJS <https://nodejs.org/en/>`_.

.. _app-designer-prereqs-nodejs-windows:

For Windows
~~~~~~~~~~~~~~~

When installing on Windows you can use an automated :program:`NodeJS` installer that uses :program:`Chocolatey`. If you chose not to let the installer use :program:`Chocolatey` to install a bunch of packages after installing :program:`NodeJS`, you will need to ensure the location of the :file:`npm` folder is added to the *PATH* variable of your system. If it is not, subsequent calls to access grunt will fail. For example: :file:`C:\\Users\\[username]\\AppData\\Roaming\\npm`.
For instructions on modifying *PATH*, see the section at the bottom of this page called Add adb to your *PATH* For Windows. Instead of navigating to the location of Android SDK, navigate to the location of the :file:`npm` folder. You can check if npm has been installed properly by executing the following command in *cmd* or *Powershell*. 

.. code-block:: console

  $ npm --version
  

.. _app-designer-prereqs-nodejs-unix:

For Mac/Unix
~~~~~~~~~~~~~~

After installing NodeJS, open a :program:`terminal` (which you can do by clicking the spotlight in the top right corner of the screen, typing :program:`terminal`, and clicking the program named :program:`Terminal`) and type:

.. code-block:: console

  $ npm --version

.. warning::

  If a number is not displayed, but you instead receive a message that the command :program:`npm` cannot be found, you will have to perform some additional configuration.

  As of this writing, by default NodeJS installs its commands into :file:`/usr/local/bin/`. In the :program:`terminal`, type:

  .. code-block:: console

    $ ls /usr/local/bin/npm

  If this command outputs something like ``/usr/local/bin/npm``, but you are still unable to run:

  .. code-block:: console

    $ npm --version

  try running:

  .. code-block:: console

    $ /usr/local/bin/npm --version

  If this is successful, then :program:`npm` is successfully installed, and you will just have to add :file:`/usr/local/bin/` to your system *PATH* variable (see below).

  If the command:

  .. code-block:: console

    $ ls /usr/local/bin/npm

  outputs a message telling you permission is denied, then you will have to change the ownership of the :file:`/usr/local/` and :file:`/usr/local/bin/` directories. On Mac, follow the `instructions to take ownership <http://osxdaily.com/2013/04/23/change-file-ownership-mac-os-x/>`_ of these directories, or to at least give yourself read permission. On other Unix systems, use the :program:`chown` command or the user-interface appropriate to your distribution to do so.

.. _app-designer-prereqs-grunt:

Grunt
---------
After installing NodeJS, install :program:`grunt` by doing the following:

.. note::

  These installation steps are copied from the `Grunt Getting Started guide <https://gruntjs.com/getting-started>`_.

On Windows, open a :program:`cmd` window (go to Start Menu, search for :program:`cmd` and open it); on MacOSX, open a :program:`terminal` window.
Within this window, type:

.. code-block:: console

  $ npm install -g grunt-cli

If the above command is unsuccessful, some machines may need to append :command:`sudo` at the beginning of the command. If :program:`grunt` is successfully installed, the following command:

.. code-block:: console

  $ grunt --version


Should display the installed version of :program:`grunt`. For example the version might be ``grunt-cli v1.2.0``

.. warning::

  If :program:`grunt` is not found, you may need to add it to the *PATH* variable of your system.

.. _app-designer-prereqs-android:

Android SDK
--------------
To install the Android SDK:

  1. Browse to the `Android SDK download page <https://developer.android.com/studio/index.html>`_.
  2. Scroll down on this page to the section labeled: *Get just the command line tools*.

  .. note::

    There no longer exists graphical tool for package management when using only the command line tools, although there is the sdkmanager CLI. You should install the full Android Studio, in which case you should follow `Google's <https://developer.android.com/studio/intro/update#sdk-manager>`_ instructions. Open the :program:`SDK Manager` from Android Studio, click :program:`Tools > SDK Manager` or click :program:`SDK Manager` in the toolbar. 


  3. Within that section, download the appropriate zipped file(s) based on your operating system.
  4. Accept the Command Line Tools terms and conditions.
  5. After the download completes, create a folder called :file:`Android` and extract the contents of the zipped folder to the :file:`\\Android` folder you created.
  6. Navigate to the :file:`cmdline-tools` folder. It should contain a :file:`\\bin` folder and a :file:`\\lib` folder and two other files :file:`NOTICE.txt` and :file:`sources.properties`.
  7. In the :file:`cmdline-tools` folder, create a new folder called :file:`latest` and move the contents of :file:`cmdline-tools` into the :file:`latest` folder. At this point, the :file:`cmdline-tools` has just one folder :file:`latest` which should contain the :file:`\\bin` and :file:`\\lib` folder and two other files :file:`NOTICE.txt` and :file:`sources.properties`.
  8. Run :program:`sdkmanager.bat --list`, this shows a list of all packages with the versions that are available be installed.
    
    - On Windows open a :program:`PowerShell` or :program:`cmd` window, whichever one you decide to go with (open the Start menu, type :program:`cmd` or :program:`PowerShell` in the search box, select and open it). Get to the :file:`\\bin` directory

    - On Mac/Unix, open a :program:`terminal` window.
  
    .. code-block:: console

      $ /Android/cmdline-tools/latest/bin>
      $ /Android/cmdline-tools/latest/bin>sdkmanager.bat --list

  9. Select the latest versions of the following packages by typing :guilabel:`sdkmanager` followed by the package path wrapped in quotes and separated by a space:

    - Android Platform-tools
    - Android Build-tools   
    
    .. code-block:: console

      $ /Android/cmdline-tools/latest/bin>sdkmanager "platform-tools" "build-tools;30.0.3"

    If there are extra packages you wish to install, you may add them by passing the package path wrapped in quotes, separated with a space. 
  
    .. code-block:: console

      $ /Android/cmdline-tools/latest/bin>sdkmanager "platform-tools" "build-tools;30.0.3" "extra-package-path"
  
  10. Accept the license agreement(s) by entering :guilabel:`y` to the :guilabel:`Accept? (y/N):` prompt.

Among many other things, this will install the Android Debug Bridge software on your computer. This tool enables the scripted pushing of files and APKs down to your Android device. See `adb (Android Debug Bridge) <https://developer.android.com/studio/command-line/adb.html>`_ for a listing of its capabilities.

Next, on Windows open a :program:`PowerShell` or :program:`cmd` window and on Mac/Unix open a :program:`terminal` window. Type:

.. code-block:: console

  $ adb version

If this displays a version string, then your installation is complete; you are done with this section and can move on to :doc:`app-designer-install`.

.. warning::

  If there is an error complaining about Java not being installed, you will need to close this :program:`cmd/PowerShell` or :program:`terminal` window and download and install Java. After installing Java, open a new :program:`cmd/PowerShell` or :program:`terminal` window and type this command again.

.. warning::

  If :program:`adb` is not found, then you need to add it to the *PATH* variable of your system.

.. _app-designer-prereqs-adb:

Add :program:`adb` to your *PATH*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _app-designer-prereqs-adb-windows:

For Windows
""""""""""""""

  #. Open a Windows File Explorer and navigate to the location of your :file:`Android` folder. This will typically be at one of: :file:`C:\\Users\\your_username\\Android` or :file:`C:\\Program Files\\Android` or :file:`C:\\Program Files (x86)\\Android`.
  #. Navigate into the :file:`platform-tools` folder.
  #. Click in the file path at the top of the File Explorer window. The path will become a selected text string. Copy it into your copy-and-paste buffer.
  #. In the File Explorer, right-click on :guilabel:`This PC`.
  #. Choose :guilabel:`Properties`. The About screen in Settings opens.
  #. Scroll down and click on :guilabel:`Advanced system setting` under :guilabel:`Related settings`. The System Properties dialog opens.
  #. Click on the :guilabel:`Environment Variables...` button at the bottom of the screen. The Environment Variables dialog opens.
  #. Select the :guilabel:`Path` variable in the bottom System variables scroll window.
  #. Click :guilabel:`Edit...`. The Edit environment variable dialog opens.
  #. Click :guilabel:`New`. A text box appears.
  #. Paste the :file:`platform-tools` directory path into the text box.
  #. Click on :guilabel:`OK` and exit all of the windows.
  #. Verify that you have made the change by closing all :program:`PowerShell` or :program:`cmd` windows and open a new one (so it picks up the change), and type

.. code-block:: console

  $ adb version

You should now see the version of the :program:`adb` tool. For example: ``Android Debug Bridge version 1.0.31``. You can now move on to :doc:`app-designer-install`.

.. _app-designer-prereqs-adb-unix:

For Mac/Unix
"""""""""""""""""""""

The *PATH* variable is nothing more than a default list of places the system looks for commands. Open a :program:`terminal`. Type:

.. code-block:: console

  $ echo $PATH

You will see a colon-separated list of folders on your computer. (echo means just print whatever comes next, and the ``${ }`` means that the system will treat *PATH* as a variable, not a program. You don't need to know this to follow these instructions, but knowledge is power.) For example, you might see something like this:

.. code-block:: console

  $ echo $PATH
    /usr/local/bin:/usr/local/sbin:/usr/bin:/bin

This means that when you type:

.. code-block:: console

  $ adb --version

the system will look for the command called :program:`adb` in the directories :file:`/usr/local/bin/`, :file:`/usr/local/sbin/`, :file:`/usr/bin/`, and :file:`/bin/`.

Note the location where you saved the Android folder. It should contain a folder called :file:`platform-tools`, which itself contains the program :program:`adb`. If this was in the folder :file:`/Users/someuser/Desktop/Android/` you should be able to run:

.. code-block:: console

  $ /Users/someuser/Desktop/Android/platform-tools/adb --version

This works because we're telling the computer exactly where the program :program:`adb` exists. By putting the :file:`platform-tools` directory on the system's *PATH* variable, we will be able to just type :program:`adb` and have the system find it in the :file:`/Users/someuser/Desktop/Android/platform-tools/` directory.

This process is more involved on Mac/Unix than on Windows. Use a text editor (not :program:`Word`, but something like :program:`TextEdit`), select the option to open a file, and browse to your home directory. You can find your home directory by typing:

.. code-block:: console

  $ echo ~

in a :program:`terminal`. ('~' is a shortcut for the home directory.) Macs use a hidden file called :file:`.bash_profile` in the home directory to set variables like *PATH*. Other Unix systems use files like :file:`.bashrc`. You might have to check the specifics for your distribution to know which you should use. Open the appropriate file. If the file does not already exist, create a new file that will be saved with the appropriate name in your home directory.

We want to add the location of the :program:`adb` tool to your *PATH* while preserving the existing *PATH* information. Assuming that your :program:`adb` program is in the :file:`/Users/someuser/Desktop/android-sdk/platform-tools/` directory, you would add the following command to the end of the :file:`.bash_profile` file:

.. code-block:: console

  $ export PATH=${PATH}:/Users/someuser/Desktop/Android/platform-tools

Save the file, close the :program:`terminal` window, open a new :program:`terminal` window, and type:

.. code-block:: console

  $ echo $PATH

You should see your old path with the new directory you added above, and you should now be able to run:

.. code-block:: console

  $ adb --version

.. tip::

  If you are going to be heavily customizing the look-and-feel of the application with a lot of external JavaScript libraries, you might also choose to install :program:`bower`.


You can now move on to :doc:`app-designer-install`.

