***************************
Contributing to ODK Docs
***************************


Authoring Tools and Environment
=====================================

.. note::

  Developer and authoring tools have lots of options and alternatives. Local tools and workflows presented in this guide are what the author feels would be easiest for a non-coding contributor to set up and use.

Docs as Code
----------------

ODK Documentation follows (as much as possible) the `Docs like Code <http://www.writethedocs.org/guide/docs-as-code/>`_ philosophy. This means:

- Documention source files are written in a plaintext format. (We use `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.)
- Documentation source files are kept under version control. (We use git and `Github <https://github.com/opendatakit/docs>`_.)
- Documentation is built from source to published output using a static site generator. (We use `Sphinx <http://sphinx-doc.org>`_.)
- Documentation builds are run, tested, and deployed automatically using continuous integration tools. (We use `CircleCI <https://circleci.com/>`_.)

`The Docs as Code approach has many advantages <http://hackwrite.com/posts/docs-as-code/>`_, but we are aware that this approach can feel difficult for writers who aren't used to dealing with the command line. It can also be difficult for coders who are used to this approach, but who typically use simpler authoring tools (like `Jekyll <http://jekyllrb.com>`_ and `Markdown <https://guides.github.com/features/mastering-markdown/>`_).

This section of the Contributor Guide walks through our authoring and publishing workflow and toolchain, to make it as easy possible for you to contribute.


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


Setting up Your Environment
----------------------------

Terminal (Command Line)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  This contributor guide is written from a *nix (Bash Terminal) perspective, which is relevant to all flavors of Linux and MacOS. If you are on Windows, you will need to do one of the following:

  - adapt the commands to your environment
  - use the `Linux subsystem (Windows 10)<https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/>`_
  - use a `bash terminal emulator <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_

  Contributions to this guide with explanations and help for Windows users is greatly appreciated.

Contributing to the docs requires interacting with git, Github, Python, and Sphinx, which requires use of the Terminal. This is common among Linux users. Mac users unfamiliar with the Terminal can learn more from `this tutorial <https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855>`_.

.. install python

Github and git
~~~~~~~~~~~~~~~~~

You will need to:

- `Install git <https://git-scm.com/downloads>`_
- `Start a GitHub account <https://github.com/>`_

.. note::

  Git is a distributed version control system. It makes it possible to track changes in files over time, merge changes made by different contributors, compare different versions of the same file, and revert a file to an earlier point. Git can be very complicated, but you do not need to understand its advanced features or inner workings to use it.

  GitHub is an online service that lets individuals and organizations host git repositories. It also provides additional collaboration tools like issue trackers. Open Data Kit uses GitHub for its public code and documentation projects.

.. python

Workflow Details
-------------------

Fork the Docs
~~~~~~~~~~~~~~

Go to the `ODK Doc repo on Github <https://github.com/opendatakit/docs>`_ and use the :guilabel:`Fork` button (top right) to create your own copy. After the process completes, you'll be looking at your own fork on Github.

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

Install Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

The first time you clone down the repo, you'll need to install the dependencies. Make sure you have your Python 3 virtual environment set up and activated and then:

.. code::

  $ pip install -r requirements.txt

.. note::

  If you are working on the design, testing, or deployment of the docs, you might find the need to install an additional PyPi package. If you do, please update the requirements.txt file with ``pip freeze > requirements.txt``. Pull Requests which change requirements.txt should include a note about why the new packages are needed.

.. note::

  If you have problems when running the Sphinx commands (see below), you may have a dependency issue. Try running ``pip install -r requirements.txt`` again.

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

Work on the Docs
~~~~~~~~~~~~~~~~~~~

- Write and edit files
