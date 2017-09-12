*****************************
Docs in Windows (Cygwin) 
*****************************

.. _cygwin-docs:

Cygwin
-------------------------------
Cygwin is windows implementation of unix-like commands. You can basically use many linux commands from windows 
command propmpt.

Install `cygwin <https://cygwin.com/install.html/>`_ and add its path into windows environmental variable.
This will allow you to `use cygwin from cmd promopt <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_.


.. _python:

Python 3
-------------------------------
You need to install `python 3 <https://www.python.org/downloads/>`_.
During the installation, you can select to set up pip tool as well as add python path to the Path environment variable.



.. _virtualenv:

Virtual Environment
-------------------------------
Virtual environment is a useful tool particularly if you work with multiple projects, each requires different dependencies and python versions. By using virtualenv, you can create seperated virtual environment and install packages as you need without affecting the main 
python installation.

To install virtualenv in windows, you can basically use pip command, which was already installed with python 3.6.2.

.. code-block:: rest

  $ pip install virtualenv

.. note::
  You need to make sure you have already installed pip in the previous step.

Create a new directory for your odkdocs work:

.. code-block:: rest

  $ mkdir odk
    
You have two options: 

  - Use the native virtualenv.
  - Use virtualenvwrapper.


.. _native-virenv:

Native virtualenv
~~~~~~~~~~~~~~~~~~~~~
Create a new python 3 virtual environment, "odkenv" is the name of the virtualenv, you are free to add your own.

.. code-block:: rest

  $ virtualenv --python=<python path/python.exe> odkenv
 
After creating python3 virtualenv in the previous step, multiple files are coppied into the folder odkenv.

.. code-block:: rest

  $ ls odkenv

The folder Scripts contains all virtualenv control as bat files.

To activate the odkenv:

.. code-block:: rest

  $ cd odkenv
  .
  .
  .
  $ cd Scripts

  $ odk/odkenv/Scripts/activate.bat


To deactivate the odkenv:

.. code-block:: rest

  $ odk/odkenv/Scripts/deactivate.bat

.. _virenv-wrapper:

Virtual Environment Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dealing with Virtualenv tool might be tiresome under windows. Thus, you are advised to install virtualenvwrapper tool using the following command.

.. code-block:: rest

  $ pip install virtualenvwrapper-win


Create a new virtualenv use the command:

.. code-block:: rest

  $ mkvirtualenv odkenv

Once the odkenv is created, it is autoamtically activated, the current path in cmd will appear for example as:

.. code-block:: rest

  $ (odkenv) C:/odk/docs

To deactivate the odkenv, write:

.. code-block:: rest

  $ deactivate

To activate the odkenv any time:

.. code-block:: rest

  $ workon odkenv

.. _git-glfs:

Git and GLFS
-------------------------------
  - Install `Git for windows <https://git-scm.com/downloads>`_.

Make sure that git is installed properly by typing (git) in the cmd.

  - Install `GLFS <https://git-lfs.github.com/>`_.


.. _andr-tools:

Android Tools
-------------------------------
Android tools (Adb) by installing `Android studio <https://developer.android.com/studio/index.html/>`_


.. _fork-clone:

Fork and Clone the docs repo
-------------------------------
From github, fork the `odk docs <https://github.com/opendatakit/docs>`_ . this will create a copy od the docs in your account called ``origin``.

Then Clone docs files into your local machine.

.. code-block:: rest

  $ cd odk
  .
  .
  .
  $ git clone https://github.com/your-github-username/docs.git


.. _remote-upstream:

Set the Upstream Remote
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: rest

  $ git remote add upstream https://github.com/opendatakit/docs.git

.. _requirs:

Install the requirements
------------------------
First activate odkenv:

.. code-block:: rest

  $ workon odkenv

Make sure you are inside the docs folder Then run:

.. code-block:: rest
 
  $ pip install -r requirements.txt

To this step, you will have ODKdocs environment ready. You can start change and build.

Install Notepad++ to edit source files in windows from :

Add `Notepad++ <https://notepad-plus-plus.org/download/v7.5.1.html/>`_ path to the enviroment variable

To edit docs files use: 

.. code-block:: rest 

  $ Notepad++ file.rst