******************************************
Working with Docs in Windows using Cygwin
******************************************

Install Cygwin
-------------------------------

Cygwin is a Windows implementation of many GNU/Linux commands usable from \*NIX command prompt. Install `cygwin <https://cygwin.com/install.html/>`_ and add its path to Windows, `for instructions <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_.

.. _cygwin-python:

Python 3
-------------------------------

You need to install `Python 3 <https://www.python.org/downloads/>`_. `For instructions, see <https://www.youtube.com/watch?v=oHOiqFs_x8Y>`_. Make sure to select the option "Add python to the Path", otherwise you need to add it manually.

.. _virtualenv:

Virtual Environment
-------------------------------

`A virtual environment to <https://virtualenv.pypa.io/en/stable/userguide/>`_ creates multiple Pythons, each has its packages and dependencies.

To install virtualenv in Windows, you can use pip command, which is already shipped with Python 3.

.. code-block:: none

  $ pip install virtualenv

Create a new directory for your odkdocs work:

.. code-block:: none

  $ mkdir odk
    
You have two options: 

  - Use the native virtualenv.
  - Use virtualenvwrapper.

.. _native-virenv:

Native Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new Python 3 virtual environment, "odkenv" is the name of the virtualenv, you can add any name.

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

.. _virenv-wrapper:

Virtual Environment Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dealing with Virtualenv tool might be tiresome under windows. For simplicity, you can install `virtualenvwrapper <https://pypi.python.org/pypi/virtualenvwrapper-win>`_ tool using the following command.

.. code-block:: none

  $ pip install virtualenvwrapper-win

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

.. _git-glfs:

Git and GLFS
-------------------------------

  - Install `Git for windows <https://git-scm.com/downloads>`_.

Make sure that git is installed properly by typing (git) in the cmd.

  - Install `GLFS <https://git-lfs.github.com/>`_.


.. _android-abd:

Android Tools
-------------------------------

Android tools (Adb) by installing `Android studio <https://developer.android.com/studio/index.html/>`_

.. _fork-clone:

Fork and Clone the ODK Docs repo
---------------------------------

From Github, fork the `ODK Docs <https://github.com/opendatakit/docs>`_. This will create a copy of the docs in your Github account called ``origin``. Move to the ODk working directory, and clone ODk Docs into your local machine.

.. code-block:: none

  $ git clone https://github.com/your-github-username/docs.git

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

To this step, you will have ODKdocs environment ready. You can start change and build.

You can work with any editor. You may install `Notepad++ <https://notepad-plus-plus.org/download/v7.5.1.html/>`_ to edit source files. Add it to Windows Path in order to use it from command prompt.

To edit docs files use: 

.. code-block:: none

  $ Notepad++ filename.rst