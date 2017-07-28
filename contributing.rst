***************************
Contributing to ODK Docs
***************************

.. docs-tech-guide:

Authoring Tools and Environment
=====================================

.. note::

  Developer and authoring tools have lots of options and alternatives. Local tools and workflows presented in this guide are what the author feels would be easiest for a non-coding contributor to set up and use.

.. _docs-as-code:

Docs as Code
----------------

ODK Documentation follows (as much as possible) the `Docs like Code <http://www.writethedocs.org/guide/docs-as-code/>`_ philosophy. This means:

- Documention source files are written in a plaintext format. (We use `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.)
- Documentation source files are kept under version control. (We use git and `Github <https://github.com/opendatakit/docs>`_.)
- Documentation is built from source to published output using a static site generator. (We use `Sphinx <http://sphinx-doc.org>`_.)
- Documentation builds are run, tested, and deployed automatically using continuous integration tools. (We use `CircleCI <https://circleci.com/>`_.)

`The Docs as Code approach has many advantages <http://hackwrite.com/posts/docs-as-code/>`_, but we are aware that this approach can feel difficult for writers who aren't used to dealing with the command line. It can also be difficult for coders who are used to this approach, but who typically use simpler authoring tools (like `Jekyll <http://jekyllrb.com>`_ and `Markdown <https://guides.github.com/features/mastering-markdown/>`_).

This section of the Contributor Guide walks through our authoring and publishing workflow and toolchain, to make it as easy possible for you to contribute.

.. _docs-workflow-overview:

Overview of Workflow
-----------------------

When you first get started you'll need to:

- Fork to your own Github Account
- Clone down to your local machine
- Install dependencies

And then each time you work you will:

- Branch for a specific task
- Make commits as you go
- Build and view the docs locally
  - Correct any errors and commit
- Push your branch to your Github fork
- Issue a pull request against the current working branch of the main repo (usually ``master``)
- Pull latest back to your local machine from the main repo
- Repeat.

.. _docs-dev-setup:

Setting up Your Environment
----------------------------

.. _docs-terminal:

Terminal (Command Line)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  This contributor guide is written from a \*nix (Bash Terminal) perspective, which is relevant to all flavors of Linux and MacOS. If you are on Windows, you will need to do one of the following:

  - adapt the commands to your environment
  - use the `Linux subsystem (Windows 10) <https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/>`_
  - use a `bash terminal emulator <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_

  Contributions to this guide with explanations and help for Windows users is greatly appreciated.

Contributing to the docs requires interacting with git, Github, Python, and Sphinx, which requires use of the Terminal. This is common among Linux users. Mac users unfamiliar with the Terminal can learn more from `this tutorial <https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855>`_.

.. _docs-python:

Python
~~~~~~~~

.. _docs-python3:

Python 3
'''''''''''

If you don't know, check to see if you have Python 3 installed:

.. code::

  $ python3

If you get an error, you probably don't and will need to `install Python 3 <https://www.python.org/downloads/>`_. If the Python command-line interpreter starts up, type ``quit()`` to exit.

.. _docs-venv:

Virtual Environment
''''''''''''''''''''''

A virtual environment is a Python tool for sandboxing dependencies. It lets you install whatever you need for a particular project, without messing up any other Python environments you might need.

Check to see if you have virtualenv installed:

.. code::

  $ virtualenv

If you get a help message with information about commands, you have it. If you don't have it, you'll get a ``command not found`` message.

If you don't have it, the easiest way to get it is to use pip:

.. code::

  $ pip install virtualenv

Then, create an ODK "master" directory. This will contain your virtualenv as a subdirectory and the docs repo as a subdirectory.

.. code::

  $ mkdir odk
  $ cd odk

Now, inside that odk directory, create a python3 virtualenv.

.. code::

  $ virtualenv -p python3 odkenv

The last part, ``odkenv`` can be whatever name you'd like to call it.

Activate your virtural environement with:

.. code::

  $ source odkenv/bin/activate

And, when you are done working, deactivate it with:

.. code::

  $ deactivate


.. _docs-gh-git:

Github and git
~~~~~~~~~~~~~~~~~

Git is a distributed version control system. It makes it possible to track changes in files over time, merge changes made by different contributors, compare different versions of the same file, and revert a file to an earlier point. Git can be very complicated, but you do not need to understand its advanced features or inner workings to use it.

GitHub is an online service that lets individuals and organizations host git repositories. It also provides additional collaboration tools like issue trackers. Open Data Kit uses GitHub for its public code and documentation projects.

You will need to:

- `Install git <https://git-scm.com/downloads>`_
- `Start a GitHub account <https://github.com/>`_

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

.. code::

  $ git clone https://github.com/your-gh-username/docs.git
  .
  .
  .
  $ cd docs

The rest of the documentation assumes you are in the directory for the repo (the directory containing ``conf.py`` and ``index.rst``).

.. tip::
  - The ``clone`` command creates a new directory inside the current one. So you do not need to create a new `odk-docs` directory first.
  - As noted above, we recommend an `odk` master directory that holds your virtualenv directory and your git repo. So you would be in that odk directory when you clone down the repo.

.. _upstream-the-docs:

Set the Upstream Remote
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you clone down a repo, the local copy calls your GitHub copy ``origin``. You should also set ``upstream`` as the name of the original, main GitHub repo.

.. code::

  $ git remote add upstream https://github.com/opendatakit/docs.git

.. _install-doc-dependencies:

Install Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

The first time you clone down the repo, you'll need to install the dependencies. Make sure you have your Python 3 virtual environment set up and activated and then:

.. code::

  $ pip install -r requirements.txt

.. note::

  If you are working on the design, testing, or deployment of the docs, you might find the need to install an additional PyPi package. If you do, please update the requirements.txt file with ``pip freeze > requirements.txt``. Pull Requests which change requirements.txt should include a note about why the new packages are needed.

.. note::

  If you have problems when running the Sphinx commands (see below), you may have a dependency issue. Try running ``pip install -r requirements.txt`` again.

.. _docs-workflow-details:

Workflow Details
-------------------

.. _git-pull-the-docs:

Pull in Updates from Upstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You probably won't need to do this the first time, but you should always pull in any changes from the main repo before working.

.. code::

  $ git pull upstream

.. _git-branch-the-docs:

Make a New Branch
~~~~~~~~~~~~~~~~~~~

Choose a specific, deliverable task to work on. This should be an `active issue from our issue tracker on GitHub <https://github.com/opendatakit/docs/issues>`_.

Create a new branch in which you will work on this specific issue. The branch name should briefly describe what you are doing. For example, the original author of this contributor guide worked in a branch he called ``contributing``.

.. code::

  $ git checkout -b branch-name

.. tip::

  Branch names should be short, lowercase, and use hyphens for separators.

  Good branch names:

  - ``getting-started-guide``
  - ``conributing``
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

.. code::

  $ sphinx-build -b html . build

This calls the sphinx-build utility. The ``-b`` switch specifies the builder, which in this case is ``html`` -- as opposed to other builders like ``pdf``. The ``.`` refers to the current directory (the build source) and ``build`` refers to the target of the build (the built files will be put into a directory labeled ``build``).

When you run the build, you may see error or warning messages. These indicate potential problems with the documentation, like:

- syntax errors
- broken links
- terms not included in the glossary

Error and warning messages include a file name and line number for tracking them down. Try to resolve all your errors and warnings before issuing a pull request. However, if this is not possible, please add a note in your pull request. **If you submit a pull request that will create build errors, you must include a note mentioning what those errors are, and why thy are ok to leave in.**


To view the documentation in your web browser, you can use Python's built-in webserver.

.. code::

  $ cd build
  $ python -m http.server 8000

Then open your browser and go to `http://localhost:8000 <http://localhost:8000>`_.

Read through your doc edits in the browser and correct any issues in your source files. You'll need to shut down the web server (:kbd:`CTRL C`) before rebuilding, then return to the main directory of the repo ( ``cd ..`` ).

It's a good idea to delete the ``build`` directory before each rebuild.

.. code::

  $ rm -rf build
  $ sphinx-build -b html . build

.. _push-the-docs:

Push Your Branch
~~~~~~~~~~~~~~~~~~

Once your work on the issue is completed, push your branch to your GitHub repo.

The first time you do this on any branch, you'll need to specify the branch name:

.. code::

  $ git push origin branch-name

After that, you can just:

.. code::

  $ git push

(Note: ``origin`` is the local label for your GitHub fork.)

.. _pr-the-docs:

Issue a Pull Request
~~~~~~~~~~~~~~~~~~~~~~

A pull request (or PR) is a request from you to the ODK Docs maintainers, for us to pull in your changes to the main repo.

Go the `main docs repo on GitHub <https://github.com/opendatakit/docs>`. You'll see a message there referencing your recently pushed branches. Select :guilabel:`Compare & pull request` to start a pull request.

Follow GitHub's instructions. The :guilabel:`Base fork` should be the main repo, and :guilabel:`base` should be ``master``. Your repo and working fork should be listed beside them. (This should all populate by default, but you should double check.) If there is a green **Able to be merged** message, you can proceed.

You must include a PR comment. Things to include:

- A summary of what you did.
- A note about anything that probably should have been done, but you didn't do.
- A note about any new work this PR will create.
- The issue number you are working on. If the PR completes the issue, include the text ``Closes #`` and the issue number.
- A note about any errors or warnings, and why you did not or could not resolve them.
- A note justifying any changes to requirements.txt
- A note about any difficulties, questions, or concerns that came up while working on this issue.

Complete the pull request. The maintainers will review it as quickly as possible. If there's any problems the maintainers can't deal with, they will reach out to you.

.. _keep-working-the-docs:

Keep Going
~~~~~~~~~~~

Once the PR is merged, you'll need to pull in the changes from the main repo ( ``upstream`` ) into your local copy.

.. code::

  $ git checkout master
  $ git pull upstream master

Then you should push those change to your copy on GitHub ( ``origin`` ).

.. code::

  $ git push

If you want to delete your branch from before, you can do that:

.. code::

  $ git branch -d branch-name

Now you can find a new issue to work on, create a new branch, and get to work...
