.. spelling::

  src

Docs Technical Guide
==========================

This document explains the tools and workflows used 
when contributing to ODK Documentation.

.. note::

  Developer and authoring tools 
  have lots of options and alternatives. 
  Local tools and workflows presented in this guide 
  are what the authors feel would be easiest 
  for a non-coding contributor to set up and use.
  
  You should feel free
  to use your preferred tools.

.. _docs-as-code:

Docs as Code
----------------

ODK Documentation follows 
(as much as possible) 
the `Docs as Code`_ philosophy. 

.. _Docs as Code: http://www.writethedocs.org/guide/docs-as-code/ 

This means:

- Documentation source files are written in a plain text format. 
  (We use `reStructuredText`_.)
- Documentation source files are kept under version control.
  (We use git and `Github`_.)
- Documentation is built from source 
  to a published output using a 
  static site generator. 
  (We use `Sphinx`_.)
- Documentation builds are 
  run, tested, and deployed automatically 
  using continuous integration tools. 
  (We use `CircleCI`_.)

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Github: http://github.com
.. _Sphinx: http://sphinx-doc.org
.. _CircleCI: https://circleci.com

The 'Docs as Code' approach has many advantages, 
but we are aware that this approach can feel difficult 
for writers who aren't used to dealing with the command line. 
It can also be difficult for coders who are used to this approach, 
but who typically use simpler authoring tools 
like `Jekyll`_ and `Markdown`_. 

.. _Jekyll: http://jekyllrb.com
.. _Markdown: https://guides.github.com/features/mastering-markdown/

This section of the Contributor Guide 
walks through our authoring and publishing workflow and toolchain, 
to make it as easy as possible for you to contribute.

.. _docs-workflow-overview:

Overview of Workflow
-----------------------

When you first get started you'll need to:

1. Fork the `ODK Docs repo`_ your own Github Account
2. Clone it down to your local machine
3. Install dependencies

.. _ODK Docs repo: https://github.com/opendatakit/docs

And then each time you work you will:

1. Make a branch for a specific task
2. Make commits as you go
3. Build and view the docs locally,
   running the style guide tests.

  - Correct any errors 
    and commit those changes

4. Push your branch to your Github fork
5. Issue a pull request 
   against the current working branch 
   of the main repo (usually ``master``)
6. Pull the latest changes to ``master``
   back to your local machine from the main repo.
7. Repeat

.. _docs-dev-setup:

Setting up your Environment
----------------------------

.. _docs-terminal:

Terminal (Command Line)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  This contributor guide is written
  from a Linux/Unix (Bash terminal) perspective, 
  which is relevant to all flavors of Linux and macOS. 
  We consider the Bash terminal commands to be 
  the canonical way to build and work with the docs.

  We have also provided explanations for 
  how to adapt these commands to the Windows Command Prompt. 
  This is different than Windows Powershell, 
  and not all the commands will work in Powershell. 
  For more details on the Windows Command Prompt, 
  `see this article`__.
  
  __  https://www.lifewire.com/how-to-open-command-prompt-2618089

  If you are on a Windows machine, 
  you may prefer to use the adapted Windows instructions here.    
  Alternatively, you can follow the Bash commands:

  - use the `Linux subsystem`_ (Windows 10) 
  - use a bash terminal emulator, such as

    - :doc:`Cygwin <cygwin>`
    - `gitbash`_
  
  .. _Linux subsystem: https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/
  .. _gitbash: https://git-for-windows.github.io/
    
  The lead maintainers of this docs repo 
  are not Windows users, 
  so we rely on our contributor community 
  to keep Windows-specific information complete and accurate. 
  Contributions to this guide
  with explanations and help for Windows users 
  are greatly appreciated.

  
Contributing to the docs requires interacting with 
git, GitHub, Python, and Sphinx, 
which requires the use of the Terminal. 
This is common among Linux users. 
Mac users unfamiliar with the Terminal 
can learn more from `this tutorial`__.

__ https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855

.. _docs-python:

Python
~~~~~~~~

.. _docs-python3:

Python 3
""""""""""""

If you don't know, 
check to see if you have Python 3 installed:


.. code-block:: console

  $ python3

On windows:

.. code-block:: doscon

   > python


If you get an error, 
you probably don't have it and will need to 
`install Python 3`.

.. _install Python 3: https://www.python.org/downloads/

On Windows 
make sure to select the option 
"Add python to the Path" 
while installing,
otherwise you'll need to `add it manually`__. 

__ https://youtu.be/UTUlp6L2zkw

See `this video`__ for more details.

__ https://www.youtube.com/watch?v=oHOiqFs_x8Y 

If the Python command-line interpreter starts up, 
type :py:func:`quit()` to exit.

.. _docs-venv:

Virtual Environment
""""""""""""""""""""""""

A virtual environment is a Python tool for sandboxing dependencies. 
It lets you install whatever you need for a particular project, 
without messing up any other Python environments you might need.

Check to see if you have virtualenv installed:

.. code-block:: console

  $ virtualenv

If you get a help message with information about commands, 
you have it. 
If you don't have it, 
you'll get a ``command not found`` message.

If you don't have it, 
install it using ``pip`` by running:

.. code-block:: console

  $ pip install virtualenv

Then, create a directory called :file:`odk`.
This will contain your virtualenv and the docs repo as subdirectories.

.. code-block:: console

  $ mkdir odk
  $ cd odk

Now, inside that  directory, create a python3 virtualenv.

.. code-block:: console

  $ virtualenv -p python3 odkenv

On Windows use:

.. code-block:: doscon

  > path\to\python\python -m venv odkenv

The last part, ``odkenv``, is the name of virtual environment.
It can be whatever name you'd like to call it,
but we'll use ``odkenv`` throughout these docs.

Activate your virtual environment with:

.. code-block:: console

  $ source odkenv/bin/activate

On Windows use:

.. code-block:: doscon

  > odkenv\Scripts\activate


When you are done working, deactivate it with:

.. code-block:: console

  $ deactivate


.. _docs-gh-git:

Github and git
~~~~~~~~~~~~~~~~~

`Git`_ is a distributed version control system. 
It makes it possible to track changes in files over time, 
merge changes made by different contributors, 
compare different versions of the same file, 
and revert a file to an earlier point. 

.. _git: https://git-scm.com/

Git is complicated, 
but you do not need to understand its advanced features or inner workings
to use it.

`GitHub`_ is an online service 
for hosting git repositories. 
It also provides additional collaboration tools 
like issue trackers and project boards. 
Open Data Kit uses GitHub 
for its public code and documentation projects.

.. github: http://github.com

You will need to:

1. `Install git <https://git-scm.com/downloads>`_
2. Make sure that git is installed properly by typing (git) in the terminal or command prompt

   - On Windows: If you get any errors, 
     check if your environment variables are set up correctly.
     (See `this StackOverflow answer`__ for details.)

3. Get a `GitHub`_ account. 

.. GitHub: https://github.com/

__ https://stackoverflow.com/questions/26620312/installing-git-in-path-with-github-client-for-windows#answer-34767523


.. _glfs:

GLFS
""""""

We use `Git Large File Storage (GLFS)`__
to handle large binary files 
like images and videos. 
Once installed, 
you normally won't need to do anything else. 
GLFS is largely transparent when using git.

.. _GitLFS: https://git-lfs.github.com
__ GitLFS_


1. Install GLFS__.

__ GitLFS_

.. warning::

  **On Windows**

  Make sure :file:`git-lfs.exe` and  :file:`git.exe` are under the same main  directory on Windows. (See `this page <https://github.com/git-lfs/git-lfs/issues/919>`_ for reference.

GLFS tracks binary files as defined in the :file:`.gitattributes` file `in the repo <https://github.com/opendatakit/docs/blob/master/.gitattributes>`_. Most common binary file formats are already listed, but there might be others we haven't thought of yet.

.. _adding-new-glfs-formats:

Adding new file formats to GLFS tracking
'''''''''''''''''''''''''''''''''''''''''''''

If you are adding binary files to the repo, 
and they are in formats not already tracked, 
**it is your responsibility to make sure they are tracked by GLFS.** 

To make sure they are properly tracked, 
add them to the :file:`.gitattributes` file.

.. code-block:: none

  # file type section heading
  *.{extension-to-track} filter=lfs diff=lfs merge=lfs -text

You can also use the command line.

.. code-block:: console

  $ glfs track *.{file-extension}

This will add a line to :file:`.gitattributes`.

.. note:: 

  Please keep :file:`.gitattributes` organized 
  by placing the new file format declaration 
  in the appropriate section, 
  or creating a new section as needed.

.. warning::

  Updates to :file:`.gitattributes` must be done 
  in a commit before the commit 
  that adds the new binary files.

  We will not accept Pull Requests 
  that include binary files untracked by GLFS.


.. _android-tools:

Android Tools
~~~~~~~~~~~~~~~~~

Some testing and documentation tasks 
(including :ref:`making screenshots from ODK Collect <screenshots>`)
require the `Android Debug Bridge <https://developer.android.com/studio/command-line/adb.html>`_ command line tool.
You can either install Android Studio 
or install ADB as standalone SDK tool.

.. _android-studio:

Android Studio
""""""""""""""""""

:abbr:`ADB (Android Debug Bridge)` is part of `Android Studio`_,
and is typically installed by default when you install Android Studio. 

.. _Android Studio: https://developer.android.com/studio/index.html

This is the best way to get :command:`adb` 
if you plan to do any other Android development. 
To use it from the command line, 
add the SDK Platform tools to your path.

On Mac, add the following to your :file:`.bash_profile`

.. code-block:: sh

  export PATH=$PATH:~/Library/Android/sdk/tools/


.. note::

    On Windows, 
    you have to run Android Studio once 
    to complete the installation of ADB. 
    The tool can be found in
    :file:`C:/Users/user-name/AppData/Local/Android/sdk/platform-tools`. 
    To add it to the environment variable path, 
    use the following command:

    .. code-block:: none

      set PATH=%PATH%;C:\Users\your user name\AppData\Local\Android\sdk\platform-tools



.. warning::

  The path specified above 
  assumes a default installation of Android Studio. 
  You may have put Android Studio in a different location.


.. _docs-workflow-setup:

Getting ready to work
-----------------------

.. _fork-the-docs:

Fork the docs
~~~~~~~~~~~~~~

Go to the `ODK Doc repo on GitHub`__ 
and use the :guilabel:`Fork` button (top right) 
to create your own copy. 
After the process completes, 
you'll be looking at your own fork on GitHub.

__ https://github.com/opendatakit/docs

.. _clone-the-docs:

Clone to local
~~~~~~~~~~~~~~~~

From your own fork of the repo on GitHub, 
select the :guilabel:`Clone or download` button. 
Copy the URI from the text box that opens up. 
It will be something like: 
``https://github.com/your-gh-username/docs.git``

Open your terminal, 
and `cd` to your preferred directory. 
Then `git clone` the repo:

.. code-block:: console

  $ git clone https://github.com/your-github-username/docs.git
  .
  .
  .
  $ cd docs

The rest of the documentation assumes 
you are in the directory for the repo 
(the directory containing ``conf.py`` and ``index.rst``).

.. tip::

  - The ``clone`` command creates a new directory inside the current one.
    So you do not need to create a new `odk-docs` directory first.
  - As noted above,
    we recommend a master :file:`odk` directory 
    that holds your virtualenv directory and your git repo 
    in two separate subdirectories. 
    So you would be in that master :file:`odk` directory 
    when you clone down the repo.
  - Double check that the right folders are in the right places

  .. code-block:: none

    - odk/
      - odkenv/
      - docs/

.. _upstream-the-docs:

Set the upstream remote
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you clone down a repo, 
the local copy calls your GitHub copy ``origin``. 
You should also set ``upstream`` 
as the name of the  main ODK Docs GitHub repo.

.. code-block:: console

  $ git remote add upstream https://github.com/opendatakit/docs.git

Or in Windows:

.. code-block:: doscon

  > git remote add upstream https://github.com/opendatakit/docs.git

Run ``git remote -v`` to check the status, you should see something like this:

.. code-block:: console

  $ origin https://github.com/your-github-username/docs.git (fetch)
  $ origin https://github.com/your-github-username/docs.git (push)
  $ upstream https://github.com/opendatakit/docs.git (fetch)
  $ upstream https://github.com/opendatakit/docs.git (push)

.. _install-doc-dependencies:

Install Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

The first time you clone down the repo, 
you need to install the dependencies. 
Make sure you have your Python 3 virtual environment 
set up and activated, then:

.. code-block:: console

  $ pip install -r requirements.txt

.. note::

  If you are working on 
  the design, testing, or deployment of the docs, 
  you might find the need to install an additional PyPi package. 
  If you do, 
  please update the :file:`requirements.txt` file with 
  :command:`pip freeze > requirements.txt`. 
  Pull Requests which change :file:`requirements.txt` 
  should include a note about why the new packages are needed.

.. note::

  If you have problems when running the Sphinx commands (see below), 
  you may have a dependency issue. 
  Try running :command:`pip install -r requirements.txt` again.

.. _docs-workflow-details:

Workflow details
-------------------

.. _git-pull-the-docs:

Pull in changes from upstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As other people make changes to the docs,
you need to keep your local copy up to date.

You probably won't need to do this the first time, 
but you should always pull in any changes from the main repository
before working.


.. code-block:: console

  $ git pull upstream

.. note::

  If you get this message:

  .. code-block:: none

        You asked to pull from the remote 'upstream', but did not specify a branch.
        Because this is not the default configured remote for your current branch,
        you must specify a branch on the command line.


  Try running ``git pull upstream master`` instead.

.. _git-branch-the-docs:

Make a New Branch
~~~~~~~~~~~~~~~~~~~

Choose a specific, deliverable task to work on. 
This should be an `active issue from our issue tracker on GitHub`__. 

__ https://github.com/opendatakit/docs/issues

Create a new branch in which you will work on this specific issue. 
The branch name should briefly describe what you are doing. 
For example, 
the original author of this contributor guide 
worked in a branch called ``contributing``. 

Also, 
make sure that all the branches are derived from ``master``,
to avoid mixing up work from different issues commits.

.. code-block:: console

  $ git checkout -b branch-name

.. tip::

  Branch names should be short, lowercase, and use hyphens for separators.

  Good branch names:

  - ``getting-started-guide``
  - ``contributing``
  - ``fix-issue-13``

  Bad branch names:

  - ``getting started guide``
  - ``Getting started guide``
  - ``Getting_started_guide``
  - ``writing-the-getting-started-guide-adammichaelwood-july-2017-draft``

.. _write-the-docs:

Work on the Docs
~~~~~~~~~~~~~~~~~~~

Write and edit files in your favorite editor.


.. note::

  To work on ODK Docs, 
  you need to work in a code editor.

  If you've never used a code editor before, 
  you should know that they are a little different
  than other writing environments
  like MS Word or your email editor.
  
  People have strong opinions about code editors,
  and nearly everyone who uses them regularly has a favorite.
  
  If you're new to using an editor, 
  you might want to try `Atom`_ or `Sublime`_,
  which are both popular and easy to use, 
  and they both have decent support for reStructuredText syntax.
  
  .. _Atom: https://atom.io/
  .. _Sublime: https://www.sublimetext.com/
  
  

.. _build-the-docs:

Build, View, and Debug
~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation into a viewable website:

.. code-block:: console

  $ sphinx-build -b dirhtml src build

This calls the sphinx-build utility. 
The :option:`-b` switch specifies the builder, 
which in this case is ``html``. 
``src`` refers to the src directory which contains all :file:`.rst` files (the build source) 
and ``build`` refers to the target of the build 
(the built files will be put into a directory labeled :file:`build`).

When you run the build, 
you may see error or warning messages. 
These indicate potential problems with the documentation, like:

- syntax errors
- broken links
- terms not included in the glossary

Error and warning messages 
include a file name and line number for tracking them down. 
Try to resolve all your errors and warnings 
before issuing a pull request. 
If this is not possible, 
please add a note in your pull request 
so that we can help you debug the problem.

**We will not merge Pull Requests that have warnings or errors in them.**

.. note::

  Because of `a bug in Sphinx`__ 
  the line numbers in error and warning messages 
  will be off by the length of `rst_prolog` in :file:`conf.py`.

__ https://github.com/sphinx-doc/sphinx/issues/2617

To view the documentation in your web browser, 
you can use Python's built-in web server.

.. code-block:: console

  $ cd build
  $ python -m http.server 8000

Then open your browser and go to http://localhost:8000 

Read through your doc edits in the browser 
and correct any issues in your source files. 
You'll need to shut down the web server (:kbd:`CTRL C`) 
before rebuilding, 
then return to the main directory of the repo ( :command:`cd ..` ).

It's a good idea to delete the ``build`` directory before each rebuild.

.. code-block:: console

  $ rm -rf build
  $ sphinx-build -b dirhtml . build

.. tip::

  The script :file:`b.sh` automatically runs all the build commands.
  It saves typing.
  In the future, 
  it will also become the canonical build script for ODK Docs,
  including additional tests and other build tasks.

.. _push-the-docs:

Push Your Branch
~~~~~~~~~~~~~~~~~~

Once your work on the issue is completed, 
add the files you've changed or created, 
and write a relevant commit message describing the changes.

.. code-block:: console

  $ git add my_changed_files
  $ git commit -m "A small but relevant commit message"

Then, push the changes. 
The first time you do this on any branch, 
you'll need to specify the branch name:

.. code-block:: console

  $ git push origin branch-name

After that, you only need to use the :command:`push` command:

.. code-block:: console

  $ git push


.. note:: ``origin`` is the local label for your GitHub fork.

.. _pr-the-docs:

Issue a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

A :dfn:`pull request` (or PR) 
is a request from you to the ODK Docs maintainers, 
for us to pull in your changes to the main repo.

Go the `main docs repo on GitHub`__. 
You'll see a message there referencing your recently pushed branches. Select :guilabel:`Compare & pull request` to start a pull request.

__ https://github.com/opendatakit/docs>

Follow GitHub's instructions. 
The :guilabel:`Base fork` should be the main repo, 
and :guilabel:`base` should be ``master``. 
Your repo and working fork should be listed beside them. 
(This should all populate by default, 
but be sure to double check.) 
If there is a green **Able to be merged** message, 
you can proceed.

You must include a PR comment. Things to include:

- A summary of what you did.
- A note about anything that probably should have been done, 
  but you didn't do.
- A note about any new work this PR will create.
- The issue number you are working on. 
  If the PR completes the issue, 
  include the text ``Closes #`` and the issue number.
- A note about any errors or warnings, 
  and why you did not or could not resolve them.
- A note justifying any changes to :file:`requirements.txt`.
- A note about any difficulties, questions, or concerns 
  that came up while working on this issue.

Complete the pull request. 
The maintainers will review it as quickly as possible. 
If there are any problems the maintainers can't deal with, 
they will reach out to you.

.. note::

   If you happen to rename any document file (:file:`*.rst`), 
   then be sure that you add the redirect in your PR.

   To add the redirect go to :file:`s3_website.yml`, 
   and add a mapping from the old file name to the new file name 
   below the **redirects:** line, one mapping per line. 
    
   If you have renamed :file:`old-name.rst` to :file:`new-name.rst`:

   .. code-block:: yaml

     redirects:
      old-name/index.html: new-name
      
   Notice the inclusion of ``/index.html`` on the left side.


.. _keep-working-the-docs:

Keep Going
~~~~~~~~~~~

Once the PR is merged, 
you'll need to pull in the changes from the main repo ( ``upstream`` )
into your local copy.

.. code-block:: console

  $ git checkout master
  $ git pull upstream master

Then you should push those change to your copy on GitHub ( ``origin`` ).

.. code-block:: console

  $ git push

If you want to delete your branch from before, you can do that:

.. code-block:: console

  $ git branch -d branch-name

Now you can find a new issue to work on, 
create a new branch, 
and get to work again.
