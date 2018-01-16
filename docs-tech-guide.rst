Docs Technical Guide
==========================

This document explains the tools and workflows used when contributing to ODK Documentation.

.. note::

  Developer and authoring tools have lots of options and alternatives. Local tools and workflows presented in this guide are what the authors feel would be easiest for a non-coding contributor to set up and use. 

.. _docs-as-code:

Docs as Code
----------------

ODK Documentation follows (as much as possible) the `Docs like Code <http://www.writethedocs.org/guide/docs-as-code/>`_ philosophy. This means:

- Documentation source files are written in a plain text format. (We use `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.)
- Documentation source files are kept under version control. (We use git and `Github <https://github.com/opendatakit/docs>`_.)
- Documentation is built from source to published output using a static site generator. (We use `Sphinx <http://sphinx-doc.org>`_.)
- Documentation builds are run, tested, and deployed automatically using continuous integration tools. (We use `CircleCI <https://circleci.com/>`_.)

`The 'Docs as Code' approach has many advantages <http://hackwrite.com/posts/docs-as-code/>`_, but we are aware that this approach can feel difficult for writers who aren't used to dealing with the command line. It can also be difficult for coders who are used to this approach, but who typically use simpler authoring tools (like `Jekyll <http://jekyllrb.com>`_ and `Markdown <https://guides.github.com/features/mastering-markdown/>`_).

This section of the Contributor Guide walks through our authoring and publishing workflow and toolchain, to make it as easy as possible for you to contribute.

.. _docs-workflow-overview:

Overview of Workflow
-----------------------

When you first get started you'll need to:

- Fork to your own Github Account
- Clone it down to your local machine
- Install dependencies

And then each time you work you will:

- Make a branch for a specific task
- Make commits as you go
- Build and view the docs locally
  - Correct any errors and commit
- Push your branch to your Github fork
- Issue a pull request against the current working branch of the main repo (usually ``master``)
- Pull latest back to your local machine from the main repo
- Repeat

.. _docs-dev-setup:

Setting up your Environment
----------------------------

.. _docs-terminal:

Terminal (Command Line)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  This contributor guide is written primarily from a \*nix (Bash Terminal) perspective, which is relevant to all flavors of Linux and MacOS. We consider the Bash terminal commands to be the "canonical" way to build and work with the docs.

  We have also provided explanations for how to adapt these commands to the Windows Command Prompt. (This is different than Windows Powershell, and not all the commands will work in Powershell. For more details on the Windows Command Prompt, `see this article <https://www.lifewire.com/how-to-open-command-prompt-2618089>`_

  If you are on a Windows machine, you may prefer to use the adapted Windows instructions here. Alternatively, you can follow the Bash commands:

  - use the `Linux subsystem (Windows 10) <https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/>`_
  - use a bash terminal emulator, such as

    - :doc:`Cygwin <cygwin>`
    - `gitbash <https://git-for-windows.github.io/>`_

  The lead maintainers of this docs repo are not Windows users, so we rely on our contributor community to keep Windows-specific information complete and accurate. Contributions to this guide with explanations and help for Windows users are greatly appreciated.

Contributing to the docs requires interacting with git, Github, Python, and Sphinx, which requires the use of the Terminal. This is common among Linux users. Mac users unfamiliar with the Terminal can learn more from `this tutorial <https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855>`_.

.. _docs-python:

Python
~~~~~~~~

.. _docs-python3:

Python 3
""""""""""""

If you don't know, check to see if you have Python 3 installed:


.. code-block:: console

  $ python3

On windows:

.. code-block:: doscon

   > python


If you get an error, you probably don't have it and will need to `install Python 3 <https://www.python.org/downloads/>`_.

On Windows make sure to select the option "Add python to the Path", while installing (see `instructions <https://www.youtube.com/watch?v=oHOiqFs_x8Y>`_ ) otherwise you need to add it `manually <https://youtu.be/UTUlp6L2zkw>`_ .

If the Python command-line interpreter starts up, type ``quit()`` to exit.

.. _docs-venv:

Virtual Environment
""""""""""""""""""""""""

A virtual environment is a Python tool for sandboxing dependencies. It lets you install whatever you need for a particular project, without messing up any other Python environments you might need.

Check to see if you have virtualenv installed:

.. code-block:: console

  $ virtualenv

If you get a help message with information about commands, you have it. If you don't have it, you'll get a ``command not found`` message.

In case you don't have it, install it using ``pip`` by running:

.. code-block:: console

  $ pip install virtualenv

Then, create an ODK "master" directory. This will contain your virtualenv and the docs repo as subdirectories.

.. code-block:: console

  $ mkdir odk
  $ cd odk

Now, inside that odk directory, create a python3 virtualenv.

.. code-block:: console

  $ virtualenv -p python3 odkenv

On Windows use:

.. code-block:: doscon

  > path\to\python\python -m venv odkenv
  (e.g C:\python36\python -m venv odkenv)

The last part, ``odkenv`` can be whatever name you'd like to call it.

Activate your virtual environment with:

.. code-block:: console

  $ source odkenv/bin/activate

On Windows use:

.. code-block:: doscon

  > odkenv\Scripts\activate


And, when you are done working, deactivate it with:

.. code-block:: console

  $ deactivate


.. _docs-gh-git:

Github and git
~~~~~~~~~~~~~~~~~

Git is a distributed version control system. It makes it possible to track changes in files over time, merge changes made by different contributors, compare different versions of the same file, and revert a file to an earlier point. Git can be very complicated, but you do not need to understand its advanced features or inner workings to use it.

GitHub is an online service that lets individuals and organizations host git repositories. It also provides additional collaboration tools like issue trackers. Open Data Kit uses GitHub for its public code and documentation projects.

You will need to:

- `Install git <https://git-scm.com/downloads>`_
-  Make sure that git is installed properly by typing (git) in the terminal or command prompt

   - On windows if you get any error check if environment variables are set up correctly(`see instructions <https://stackoverflow.com/questions/26620312/installing-git-in-path-with-github-client-for-windows#answer-34767523>`_)

- `Start a GitHub account <https://github.com/>`_

.. glfs

GLFS
""""""

We use `Git Large File Storage (GLFS)  <https://git-lfs.github.com/>`_ to handle large binary files like images and videos. Once installed, you normally won't need to do anything else. GLFS is largely transparent when using git.

- `Install GLFS <https://git-lfs.github.com/>`_


.. warning::

  **On Windows**

  Make sure :file:`git-lfs.exe` and  :file:`git.exe` are under the same "master" directory on Windows. (See `this page <https://github.com/git-lfs/git-lfs/issues/919>`_ for reference.

GLFS tracks binary files as defined in the :file:`.gitattributes` file `in the repo <https://github.com/opendatakit/docs/blob/master/.gitattributes>`_. Most common binary file formats are already listed, but there might be others we haven't thought of yet.

If you are adding binary files to the repo, and they are in formats not already tracked, **it is your responsibility to make sure they are tracked.** To make sure they are properly tracked, add the file type to GLFS. You can do this by editing :file:`.gitattributes` directly.

.. code-block:: none

  # file type section heading
  *.{extension-to-track} filter=lfs diff=lfs merge=lfs -text

You can also use the command line.

.. code-block:: console

  $ glfs track *.{file-extension}

This will add a line to :file:`.gitattributes`.

We would also appreciate it if you would keep that file organized by placing the new file format declaration in the appropriate section, or creating a new section as needed.

.. warning::

  Updates to :file:`.gitattributes` must be done in a commit before the commit that adds the new binary files.

  **We will not accept Pull Requests that include binary files untracked by GLFS.**


.. _android-tools:

Android Tools
~~~~~~~~~~~~~~~~~

Some testing and documentation tasks (including :ref:`making screenshots from ODK Collect <screenshots>`) require the :doc:`Android Debug Bridge <collect-adb>`) command line tool. You can either install Android Studio or install ADB as standalone SDK tool.

Android Studio
""""""""""""""""""

:abbr:`ADB (Android Debug Bridge)` is part of `Android Studio <https://developer.android.com/studio/index.html>`_. This is the best way to get :command:`adb` if you plan to do any other Android development. It *should* be installed by default when you install Android Studio. To use it from the command line, you'll need to add the SDK Platform tools to your path.

On Mac, add the following to your :file:`.bash_profile`

.. note::

    On Windows, you have to run Android Studio once to complete the Installation of ADB. The tool can be found in :file:`C:/Users/your user name/AppData/Local/Android/sdk/platform-tools`. You need to add it to the environment variable path, use the following command:

    .. code-block:: none

        set PATH=%PATH%;C:\Users\your user name\AppData\Local\Android\sdk\platform-tools


.. code-block:: sh

  export PATH=$PATH:~/Library/Android/sdk/tools/

.. warning::

  The path specified above assumes a default installation of Android Studio. You may have put Android Studio in a different location.

.. help for linux and windows users here would be good...

.. _docs-workflow-setup:

Getting Ready to Work
-----------------------

.. _fork-the-docs:

Fork the Docs
~~~~~~~~~~~~~~

Go to the `ODK Doc repo on Github <https://github.com/opendatakit/docs>`_ and use the :guilabel:`Fork` button (top right) to create your own copy. After the process completes, you'll be looking at your own fork on Github.

.. _clone-the-docs:

Clone Down to Local
~~~~~~~~~~~~~~~~~~~~~

From your own form of the repo on Github, select the :guilabel:`Clone or download` button. Copy the URI from the text box that opens up. It will be something like: ``https://github.com/your-gh-username/docs.git``

Open your terminal, and `cd` to your preferred directory. Then `git clone` the repo:

.. code-block:: console

  $ git clone https://github.com/your-github-username/docs.git
  .
  .
  .
  $ cd docs

The rest of the documentation assumes you are in the directory for the repo (the directory containing ``conf.py`` and ``index.rst``).

.. tip::
  - The ``clone`` command creates a new directory inside the current one. So you do not need to create a new `odk-docs` directory first.
  - As noted above, we recommend a master :file:`odk` directory that holds your virtualenv directory and your git repo in two separate subdirectories. So you would be in that master :file:`odk` directory when you clone down the repo.
  - Double check that right folders are in the right places

  .. code-block:: none

    - odk/
      - odkenv/
      - docs/

.. _upstream-the-docs:

Set the Upstream Remote
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you clone down a repo, the local copy calls your GitHub copy ``origin``. You should also set ``upstream`` as the name of the original, main GitHub repo.


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

The first time you clone down the repo, you'll need to install the dependencies. Make sure you have your Python 3 virtual environment set up and activated in the docs repo and then:

.. code-block:: console

  $ pip install -r requirements.txt

.. note::

  If you are working on the design, testing, or deployment of the docs, you might find the need to install an additional PyPi package. If you do, please update the requirements.txt file with ``pip freeze > requirements.txt``. Pull Requests which change :file:`requirements.txt` should include a note about why the new packages are needed.

.. note::

  If you have problems when running the Sphinx commands (see below), you may have a dependency issue. Try running ``pip install -r requirements.txt`` again.

.. _docs-workflow-details:

Workflow Details
-------------------

.. _git-pull-the-docs:

Pull in Updates from Upstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You probably won't need to do this the first time, but you should always pull in any changes from the main repository before working.


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

Choose a specific, deliverable task to work on. This should be an `active issue from our issue tracker on GitHub <https://github.com/opendatakit/docs/issues>`_.

Create a new branch in which you will work on this specific issue. The branch name should briefly describe what you are doing. For example, the original author of this contributor guide worked in a branch he called ``contributing``. Also, make sure that all the branches are derived from the ``master`` branch to avoid intermixing of commits.

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

.. links to style guidelines, rst syntax, etc...

.. _build-the-docs:

Build, View, and Debug
~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation into a viewable website:

.. code-block:: console

  $ sphinx-build -b dirhtml . build

This calls the sphinx-build utility. The :option:`-b` switch specifies the builder, which in this case is ``html`` -- as opposed to other builders like ``pdf``. The ``.`` refers to the current directory (the build source) and ``build`` refers to the target of the build (the built files will be put into a directory labeled ``build``).

When you run the build, you may see error or warning messages. These indicate potential problems with the documentation, like:

- syntax errors
- broken links
- terms not included in the glossary

Error and warning messages include a file name and line number for tracking them down. Try to resolve all your errors and warnings before issuing a pull request. However, if this is not possible, please add a note in your pull request so that we can help you debug the problem.

**We will not merge Pull Requests that have warnings or errors in them.**

.. note::

  Because of `a bug in Sphinx <https://github.com/sphinx-doc/sphinx/issues/2617>`_, the line numbers in error and warning messages will be off by the length of `rst_prolog` in :file:`conf.py`.


To view the documentation in your web browser, you can use Python's built-in web server.

.. code-block:: console

  $ cd build
  $ python -m http.server 8000

Then open your browser and go to `http://localhost:8000 <http://localhost:8000>`_.

Read through your doc edits in the browser and correct any issues in your source files. You'll need to shut down the web server (:kbd:`CTRL C`) before rebuilding, then return to the main directory of the repo ( ``cd ..`` ).

It's a good idea to delete the ``build`` directory before each rebuild.

.. code-block:: console

  $ rm -rf build
  $ sphinx-build -b dirhtml . build

.. tip::

  The script ``b.sh`` is a utility script that can be run to build the directory. It not only saves typing effort but will also become the canonical build script for us, so it's good to get used to it from now.

.. _push-the-docs:

Push Your Branch
~~~~~~~~~~~~~~~~~~

Once your work on the issue is completed, add the files you've changed or created additionally, and write a relevant commit message describing the changes.

.. code-block:: console

  $ git add my_changed_files
  $ git commit -m "A small but relevant commit message"

Then it's time to push the changes. The first time you do this on any branch, you'll need to specify the branch name:

.. code-block:: console

  $ git push origin branch-name

After that, you can just:

.. code-block:: console

  $ git push


(Note: ``origin`` is the local label for your GitHub fork.)

.. _pr-the-docs:

Issue a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

A pull request (or PR) is a request from you to the ODK Docs maintainers, for us to pull in your changes to the main repo.

Go the `main docs repo on GitHub <https://github.com/opendatakit/docs>`_. You'll see a message there referencing your recently pushed branches. Select :guilabel:`Compare & pull request` to start a pull request.

Follow GitHub's instructions. The :guilabel:`Base fork` should be the main repo, and :guilabel:`base` should be ``master``. Your repo and working fork should be listed beside them. (This should all populate by default, but you should double check.) If there is a green **Able to be merged** message, you can proceed.

You must include a PR comment. Things to include:

- A summary of what you did.
- A note about anything that probably should have been done, but you didn't do.
- A note about any new work this PR will create.
- The issue number you are working on. If the PR completes the issue, include the text ``Closes #`` and the issue number.
- A note about any errors or warnings, and why you did not or could not resolve them.
- A note justifying any changes to requirements.txt
- A note about any difficulties, questions, or concerns that came up while working on this issue.

Complete the pull request. The maintainers will review it as quickly as possible. If there are any problems the maintainers can't deal with, they will reach out to you.

.. note::

   If you happen to rename any document file(:file:`*.rst`), then be sure that you add the redirect in your PR.

   To add the redirect go to :file:`s3_website.yml` and uncomment the **redirects:** line. Add a mapping from the old file name to the new file name below the **redirects:** line, one mapping per line. Several examples of how to format these are shown in the comments.

   For example you rename a file to :file:`newcheck.rst` from :file:`oldcheck.rst`, then to add the redirect:

   .. code-block:: yaml

     redirects:
      /oldcheck: /newcheck


.. _keep-working-the-docs:

Keep Going
~~~~~~~~~~~

Once the PR is merged, you'll need to pull in the changes from the main repo ( ``upstream`` ) into your local copy.

.. code-block:: console

  $ git checkout master
  $ git pull upstream master

Then you should push those change to your copy on GitHub ( ``origin`` ).

.. code-block:: console

  $ git push

If you want to delete your branch from before, you can do that:

.. code-block:: console

  $ git branch -d branch-name

Now you can find a new issue to work on, create a new branch, and get to work...
