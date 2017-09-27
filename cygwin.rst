******************************************
Working with Docs in Windows using Cygwin
******************************************

Install Cygwin
-------------------------------

Cygwin is a Windows implementation of many GNU/Linux commands usable from \*NIX command prompt. Install `cygwin <https://cygwin.com/install.html/>`_ and add its path to Windows so you can use its commands from windows command prompt.
`for instructions <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_.


.. warning::
  Make sure to select a mirror site near you to get a complete installation. The entire list is available on the `cygwin website <https://cygwin.com/mirrors.html/>`_


.. _cygwin-python:

Python 3
-------------------------------

You need to install `Python 3 <https://www.python.org/downloads/>`_. `For instructions, see <https://www.youtube.com/watch?v=oHOiqFs_x8Y>`_. Make sure to select the option "Add python to the Path", otherwise you need to install it manually.

.. _virtualenv:

Virtual Environment
-------------------------------

`A virtual environment tool <https://virtualenv.pypa.io/en/stable/userguide/>`_ creates multiple Pythons, each has its packages and dependencies.

 To install virtualenv in Windows, you can use pip command, which is already shipped with Python 3.

.. code-block:: doscon

  > pip install virtualenv

Create a new directory for your odkdocs work:

.. code-block:: doscon

  > mkdir odk
    

To work with virtualenv, you have two options:

  - Use the native virtualenv.
  - Use virtualenvwrapper on the top of virtualenv.

.. _native-virenv:

Native Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new Python 3 virtual environment, "odkenv" is the name of the virtualenv, you can choose any name.

.. code-block:: doscon

  > virtualenv -p <python path/python.exe> odkenv
 
After creating the virtualenv, multiple files are copied into the folder odkenv within your working directory.

.. code-block:: doscon

  > ls odkenv

The folder Scripts contains all virtualenv controls as ".bat" files.

To activate the odkenv:

.. code-block:: doscon

  > cd odkenv
  .
  .
  .
  > cd Scripts

  > odk/odkenv/Scripts/activate.bat


To deactivate the odkenv:

.. code-block:: doscon

 > odk/odkenv/Scripts/deactivate.bat

.. _virenv-wrapper:

Virtual Environment Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dealing with Virtualenv tool might be tiresome under windows. `virtualenvwrapper <https://pypi.python.org/pypi/virtualenvwrapper-win>`_ can be installed after installing virtualenv, which simplify working with virtual environments.
install it using the follwoing:
.. code-block:: none

  > pip install virtualenvwrapper-win
  

Create a new virtualenv use the command:

.. code-block:: doscon

  > mkvirtualenv odkenv

Once the odkenv is created, it is automatically activated, the current path in cmd will appear for example as:

.. code-block:: doscon

  (odkenv) /odk/docs

To deactivate the odkenv, write:

.. code-block:: doscon

  > deactivate

To activate the odkenv any time:

.. code-block:: doscon

  > workon odkenv

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

.. code-block:: doscon

  > git clone https://github.com/your-github-username/docs.git

.. _remote-upstream:

Set the Upstream Remote
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: doscon

  > git remote add upstream https://github.com/opendatakit/docs.git

.. _requirments:

Install the Requirements
------------------------

First activate odkenv:

.. code-block:: doscon

  > workon odkenv

Make sure you are inside the docs folder, then run:

.. code-block:: doscon
 
  $ pip install -r requirements.txt

To this step, you will have ODKdocs environment ready. You can start change and build.