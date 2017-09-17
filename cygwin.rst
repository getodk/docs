******************************************
Working with Docs in Windows using Cygwin
******************************************

.. _cygwin-python:

Python 3
-------------------------------

You need to install `Python 3 <https://www.python.org/downloads/>`_.For instructions, see `this video <https://www.youtube.com/watch?v=oHOiqFs_x8Y>`_. Make sure to select the option "Add python to the Path", otherwise you will need to add it manually.

Install Cygwin
-------------------------------

Cygwin is a Windows implementation of many GNU/Linux commands usable from \*NIX command prompt. Download `Cygwin <https://www.cygwin.com/install.html/>`_. Once you download the setup file, refer to these `instructions <https://www.davidbaumgold.com/tutorials/set-up-python-windows/>`_.
Make sure to select a mirror site near you to save on download time. The entire list is available on the `cygwin website <https://cygwin.com/mirrors.html/>`_.You will need to install three software packages: openssh, git, and curl.

Set a symbolic link to the executable python location by using:

.. code-block:: none

  $ln -s /cygdrive/c/Python27/python.exe /usr/bin/python

.. _virtualenv:

Virtual Environment
-------------------------------

`A virtual environment <https://virtualenv.pypa.io/en/stable/userguide/>`_ is a tool to create isolated Python environments. The basic problem being addressed is one of dependencies and versions, and indirectly permissions. 

To start with the installation first create a new directory for your odkdocs work:

.. code-block:: none

  $ mkdir odk
  $ cd odk
    
You have two options: 

  - Use the native virtualenv.
  - Use virtualenvwrapper.

.. _virenv-wrapper:

Virtual Environment Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dealing with Virtualenv tool might be tiresome in windows. As a simpler alternative, you can install `virtualenvwrapper <https://pypi.python.org/pypi/virtualenvwrapper-win>`_ tool using the following command.

.. code-block:: none

  $ pip install virtualenvwrapper

Create a new virtualenv use the command:

.. code-block:: none

  $ mkvirtualenv odkenv

Once the odkenv is created, it is automatically activated, the current path in cmd will appear for example as:

.. code-block:: none

  $ (odkenv) C:/odk/docs

To deactivate the odkenv, write:

.. code-block:: none

  $ deactivate

To activate the odkenv any time:

.. code-block:: none

  $ workon odkenv

.. _native-virenv:

Native Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install virtualenv in Windows, you can use pip command, which is already shipped with Python 3.

.. code-block:: none

  $ pip install virtualenv
  

Just in case you still want to go with native virtual environment create a new Python 3 virtual environment. "odkenv" is the name of the virtualenv used here, you can add any name.

.. code-block:: none

  $ virtualenv -p <python path/python.exe> odkenv
 
After creating python3 virtualenv in the previous step, multiple files are copied into the folder odkenv.

.. code-block:: none

  $ ls odkenv

The folder Scripts contains all virtualenv controls as ".bat" files.

To activate the odkenv:

.. code-block:: none

  $ cd odkenv
  .
  .
  .
  $ cd Scripts

  $ odk/odkenv/Scripts/activate.bat


To deactivate the odkenv:

.. code-block:: none

  $ odk/odkenv/Scripts/deactivate.bat


.. _git-glfs:



Git and GLFS
-------------------------------

GitHub is an online service that lets individuals and organizations host git repositories. It also provides additional collaboration tools like issue trackers. Open Data Kit uses GitHub for its public code and documentation projects.

  - Install `Git for windows <https://git-scm.com/downloads>`_.

Make sure that git is installed properly by typing (git) in the cmd.

  - Install `GLFS <https://git-lfs.github.com/>`_.


.. _android-abd:

Android Tools
-------------------------------

Some testing and documentation tasks (including :ref:`making screenshots from ODK Collect <screenshots>`) require the :command:`adb` (`Android Debug Bridge <https://developer.android.com/studio/command-line/adb.html>`_) command line tool.

Android Studio
-------------------------------

:abbr:`ADB (Android Debug Bridge)` is part of `Android Studio <https://developer.android.com/studio/index.html>`_. This is the best way to get :command:`adb` if you plan to do any other Android development. It *should* be installed by default when you install Android Studio. To use it from the command line, you'll need to add the SDK Platform tools to your path.
.. _standalone-sdk-tools:

Standalone SDK Tools
--------------------

You can install the SDK Platform tools (including :command:`adb`) as a `standalone package <https://developer.android.com/studio/index.html#command-tools>`_. `This tutorial explains how to setup the standalone SDK tools <https://www.androidcentral.com/installing-android-sdk-windows-mac-and-linux-tutorial>`_.


Fork and Clone the ODK Docs repo
---------------------------------

From Github, fork the `ODK Docs <https://github.com/opendatakit/docs>`_. This will create a copy of the docs in your Github account called ``origin``. Move to the ODk working directory, and clone ODk Docs into your local machine.

.. code-block:: none

  $ git clone https://github.com/your-github-username/docs.git
  .
  .
  .
  $ cd Scripts


.. _remote-upstream:

Set the Upstream Remote
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

  $ git remote add upstream https://github.com/opendatakit/docs.git

.. _requirments:

Install the Requirements
------------------------

First activate odkenv:

.. code-block:: none

  $ workon odkenv

Make sure you are inside the docs folder, then run:

.. code-block:: none
 
  $ pip install -r requirements.txt

By this step, your ODKdocs environment will be ready. You can start to change and build.

You can work with any editor. You may install `Notepad++ <https://notepad-plus-plus.org/download/v7.5.1.html/>`_ to edit source files. Add it to Windows Path in order to use it from command prompt.

To edit docs files use: 

.. code-block:: none

  $ Notepad++ filename.rst

