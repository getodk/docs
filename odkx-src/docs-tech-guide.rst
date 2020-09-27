.. spelling::

  src
  Homebrew

Docs Contributor Technical Guide
=================================

This document explains how to set up your computer
and work locally as an ODK-X Docs contributor.
Local set up includes installing some software,
and working locally involves:

- writing documentation text or code in a code editor
- using the Terminal (the "Shell" or "Command Line")

We encourage all potential contributors to try to work locally,
following this guide.

.. _docs-before-you-begin:

Before you begin
----------------

.. _learn-about-odk:

Learn a little about ODK-X
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read about the project and the community at `ODK-X's website`_.

Get started with the docs by going to the `ODK-X Docs GitHub README`_.

.. _ODK-X's website: https://odk-x.org
.. _ODK-X Docs GitHub README: https://github.com/odk-x/docs/blob/master/README.md

.. _odk-accounts:

Set up collaboration accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODK-X is a collaborative community.
Before diving in as a contributor,
set up accounts on our three main collaboration platforms,
:ref:`GitHub <get-gh-account>`,
and the :ref:`ODK-X Forum <join-forum>`

.. tip::

      As you are setting up your accounts,
      keep in mind that it is very helpful (but not required)
      to use the same (or similar) username
      on :ref:`GitHub <get-gh-account>`,
      and the :ref:`ODK-X Forum <join-forum>`.

      This makes it easy for other people to keep track of conversations
      which sometimes span multiple online platforms.

      If you are willing and able to do so,
      a profile picture in each place is also very helpful.
      (But it is okay if you are unable or uncomfortable
      adding a picture.)

#. Set up a `GitHub`_ account.

   .. _get-gh-account:

   `GitHub`_ is a popular code storage and collaboration platform.
   You will need a GitHub account to contribute to ODK-X documentation,
   or any other ODK-X projects.

   - `ODK-X on GitHub`_
   - `ODK-X Docs on GitHub`_

   .. _ODK-X on GitHub: https://github.com/odk-x/
   .. _ODK-X Docs on GitHub: https://github.com/odk-x/docs
   .. _GitHub: https://github.com/

#. Join the `ODK-X Forum`_

   .. _join-forum:

   The `ODK-X Forum`_ is the main place for
   support questions and conversations that affect the whole ODK-X community
   (users and other stake holders, as well as contributors).

   If you have a question about how to use any ODK-X software,
   or want to get connected with the larger ODK-X community,
   the forum is the best venue for that.

   .. tip::

      The forum has a search feature, and a long history of archived support posts.
      When writing new documentation about an existing feature,
      old forum posts are an excellent source for figuring out what people need to know:
      If someone has asked a question about it,
      it should probably be in the documentation.

   .. _ODK-X Forum: http://forum.odk-x.org

.. _forum-or-slack-or-gh:

.. admonition:: Should I ask in the Forum, or a GitHub issue?

   The ODK-X community talks a lot, in a lot of places.
   Sometimes it's hard to know where to ask a question.

   **Contribution-related questions and problems should be asked on Github.**
   This includes things like:

   - How do I set up my local editing environment?
   - How do I use git?
   - I'm having a merge conflict.
   - I got an error at the terminal which I don't understand.
   - How do I add a picture to a document?
   - What issue should I work on?

   **Work-specific questions and discussion should take place on the GitHub issue defining the work.**
   This includes things like:

   - I'm writing a piece of content, but I'm not sure where it should be organized.
   - I'd like to work on this feature, but I don't know how to implement it.
   - Here's my idea for solving this problem. Is that a good idea?
   - I'm going to be working on this for the next few days.
     No one else should also work on it at the same time.
   - I said I was working on this, but I didn't finish and I'm no longer working on it.

   **User-related questions and problems should be asked in the Forum.**
   (You should use the search feature first,
   since someone else may have already asked the same question.)
   This includes things like:

   - How do I install an ODK-X application?
   - How do I create a form?
   - How do I add a specific feature to a form?
   - My ODK-X application crashed.

   .. rubric:: But don't worry about posting a question in the wrong place.

   It is better to ask a question in the "wrong" venue
   than to not ask the question at all.
   Many of the same people are present in all three places,
   and we will help you wherever you happen to show up.

.. _docs-local-setup:

Initial Setup
-------------

.. note::

  We generally recommend `starting with the Docker platform`_ for editing
  docs unless you already have a Sphinx environment set up.
  Local tools and workflows presented in this guide
  are what the authors feel would be easiest
  for newcomers and those unfamiliar with open source.

  However, developer and authoring tools
  have a lot of options and alternatives.
  You should feel free to use your preferred tools.

  .. _starting with the Docker platform: https://github.com/odk-x/docs/blob/master/README.md#using-docker

Before you begin working the first time
you will need to install a few tools
on your computer.


You should only need to do this one time
on any computer.

#. Find and open a terminal or command line.

   .. tabs::

      .. group-tab:: Windows

         .. rubric:: Windows versions prior to Windows 10

         Use `Windows PowerShell`_. (Not the DOS Prompt.)

         .. _Windows PowerShell: https://docs.microsoft.com/en-us/powershell/scripting/getting-started/getting-started-with-windows-powershel

         We recommend using the :program:`Windows PowerShell ISE`.

         During initial setup (this section of the guide)
         you will need to `Run as Administrator`_.

         .. _Run as Administrator: https://docs.microsoft.com/en-us/powershell/scripting/setup/starting-windows-powershell?view=powershell-6#with-administrative-privileges-run-as-administrator

         Throughout the rest of the instructions in this guide,
         follow the instructions labeled **PowerShell** or **Windows**.

         .. rubric:: Windows 10

         In Windows 10, you have a choice:

         - Use the Powershell (as described above)
         - Use the `Windows Subsystem for Linux`_.

         .. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10

         If you decide to use the Powershell,
         follow the **Powershell** or **Windows** instructions
         throughout the contributor guides.

         If you decide to use the Linux subsystem,
         follow the **Bash** or **Windows** instructions
         throughout the contributor guide.

	  .. note::

		 Computers with the Windows 10 Home operating system are incapable of
		 installing some of the tools necessary to edit the docs. Other Windows
		 operating systems, such as Windows 10 Enterprise or Pro, can be used
		 to edit the docs.

      .. group-tab:: Mac

         Use the :program:`Terminal` app,
         or another Bash-like shell.

         .. image:: /img/docs-tech-guide/terminal-icon.*
            :alt: The Terminal Icon in Mac OS.

         If you've never used it before,
         the Terminal is probably in the :guilabel:`Other` directory
         in your App collection.

         Follow the **Bash** or **Mac** instructions
         throughout the contributor guide.

         .. admonition:: Optional: Install Homebrew

            `Homebrew`_ is a package manager for Mac OS.
            It makes it easier to install other apps and tools
            from the command line.

            Follow the `installation instructions`_.

            .. _Homebrew: https://brew.sh/
            .. _installation instructions: Homebrew

      .. group-tab:: Linux

         Use a Bash-like shell of your choosing,
         and follow the **Bash** or **Linux** instructions
         throughout the contributor guide.

         You will also need to be familiar with
         the relevant package manager for your system.

   .. admonition: Understanding terminal commands
      :name: understanding-terminal

      When you open the Terminal or PowerShell,
      you will see a bunch of symbols that include
      your username and computer name.
      This is called the :term:`prompt`.
      You type commands after the prompt,
      and hit :kbd:`RETURN` or :kbd:`ENTER` to run that command.

      Everybody's prompt looks different,
      so we can't make our documentation match what you see.
      Instead, we use the ``$`` symbol to represent the Bash prompt
      and the ``>`` symbol to represent the PowerShell prompt.
      The text that follows the ``$`` or ``>`` symbol
      is the command you need to type or copy.

      Below the command, there is sometimes output from the command.

      .. tabs::

         .. group-tab:: bash

            .. code-block::

               $ command is here - type this
               Output is here. Don't type this.

         .. group-tab:: PowerShell

            .. code-block::

               > command is here - type this
               Output is here. Don't type this.

      Not all commands have output,
      and we don't always include the output in our documentation
      unless it is relevant.
      It it is a good idea to glance at your own terminals output
      for unexpected errors.

      To make things more clear,
      the docs will additionally prefix the prompt with a
      :term:`path` (showing what directory you are in)
      whenever that is important.

      .. tabs::

         .. group-tab:: bash

            .. code-block::

               /odk-docs/ $ command is here - type this
               Output is here. Don't type this.

         .. group-tab:: PowerShell

            .. code-block::

               /odk-docs/ > command is here - type this
               Output is here. Don't type this.

#. Install git.

   Git is a version control system.
   It helps us keep track of changes to the documentation.
   (Similar to the undo history in a document editing program.)

   .. tabs::

      .. group-tab:: Linux

         Use your distribution's package management system
         to `install git on Linux`_.

         .. _install git on Linux: https://git-scm.com/download/linux

      .. group-tab:: Mac

         .. rubric:: Option 1: Download an installer

         #. Download the `git installer for Mac`_.
         #. Open the installer package.
         #. Follow the prompts.
         #. Accept any default settings.

         .. _git installer for Mac: https://git-scm.com/download/mac

         .. rubric:: Option 2: Use Homebrew to install git

         .. code:: console

            $ brew install git

      .. group-tab:: Windows

         #. Download the `git installer for Windows`_.
         #. Open the installer package.
         #. Follow the prompts.
         #. Accept any default settings.

         .. _git installer for Windows: https://git-scm.com/download/windows

#. Install Git LFS

   Git Large File Storage (Git LFS) is a tool that helps us
   manage images, videos, and other files which are neither text nor code.

   .. tabs::

      .. group-tab:: Linux

         Use your distribution's package management system
         to `install Git LFS on Linux`_.

         .. _install Git LFS on Linux: https://github.com/git-lfs/git-lfs/wiki/Installation

         After initial installation by the package manager,
         complete the install by running:

         .. code:: console

            $ git lfs install

      .. group-tab:: Mac

         .. Option 1: Download an Installer

         #. `Download Git LFS from the Git LFS website`_.
         #. Open the downloaded installer.
         #. Follow the prompts.
         #. Accept any default settings.
         #. Open the Terminal and add LFS to git:

            .. code:: console

               $ git lfs install

         .. _Download Git LFS from the Git LFS website: https://git-lfs.github.com/

         .. rubric:: Option 2: Use Homebrew to install Git LFS.

         .. code:: console

            $ brew install git-lfs
            $ git lfs install

      .. group-tab:: Windows

         #. `Download Git LFS from the Git LFS website`_.
         #. Open the downloaded installer.
         #. Follow the prompts.
         #. Accept any default settings.
         #. Open Powershell and add LFS to git:

            .. code:: powershell

               > git lfs install

         .. _Download Git LFS from the Git LFS website: https://git-lfs.github.com/

#. Install Python 3

   `Python`_ is a programming language.

   .. _Python: https://www.python.org/

   Most of the ODK-X Docs tools are written in Python,
   so you need it installed on your computer in order to use those tools.
   (Don't worry. You don't need to know how to program in Python.)

   We require Python 3, version 3.6 or later.

   .. tabs::

      .. group-tab:: Linux

         Use your distribution's package management system
         to `install Python 3.6+ on Linux`_.

         (For more help,
         see `Installing Python on Linux`_.)

         .. _install Python 3.6+ on Linux: https://docs.python-guide.org/starting/install3/linux/
         .. _Installing Python on Linux: https://realpython.com/installing-python/#linux

      .. group-tab:: Mac

         .. tip::

            Mac OS includes a legacy (outdated) version of Python.
            It's best to just ignore it.

         .. rubric:: Option 1: Use the Python Installer for Mac

         #. Download the latest `Python installer for Mac`_.

            .. _mac-64-or-32:

            .. admonition:: 64-bit or 32-bit?

               Python provides 64-bit and 32-bit installers.
               You probably need the 64-bit installer.

               If you are running a relatively recent Mac OS update
               (Mountain Lion or later — any Mac from the last several years)
               the 64-bit installer is for you.

               If you have an older Mac,
               and are unsure if it can run a 64-bit installer,
               `check the processor details`_ in :menuselection:` -> About This Mac`.

               .. _check the processor details: https://www.alesis.com/kb/article/1616#mac

         #. Open the Installer.
         #. Follow the prompts.
         #. Accept the default settings.
         #. Open the Terminal to see if Python installed properly.

            .. code:: console

               $ python3 --version
               Python 3.7.0

            The output from :command:`python3 --version` might be a little different,
            but it should be higher than ``3.6``.

            If you get an error here, something went wrong.
            Try running the installer again.
            If the problem persists, and you can't debug it yourself,
            asks us about it on |forum|_.

         .. _Python installer for Mac: https://www.python.org/downloads/mac-osx/

         .. rubric:: Option 2: Use Homebrew to install Python 3.6+

         .. code:: console

            $ brew install python
            .
            .
            .
            $ python3 --version
            Python 3.7.0

         The output from :command:`python3 --version` might be a little different,
         but it should be higher than ``3.6``.

         If you get an error here, something went wrong.
         Try running :command:`brew install python` again.
         If the problem persists, and you can't debug it yourself,
         asks us about it on |forum|_.

      .. group-tab:: Windows

         #. Go to the `Python Releases for Windows`_ page.
         #. Under the latest numbered release for Python 3, find and download the
            :program:`Windows x86-64 web-based installer` (for a 64-bit system)
            or the :program:`Windows x86 web-based installer` (for a 32-bit system).

            .. _win-64-or-32:
            .. admonition:: 64-bit or 32-bit?

               Well over 90% of computers running Windows are 64-bit.
               So you probably need the 64-bit version.

               If you are running a very old or low-powered computer,
               and you are unsure if it is 64-bit or 32-bit,
               you can use `this guide from HP` (which will work for other computer brands)
               to find that information.

               .. _this guide from HP: https://support.hp.com/us-en/document/c02002390

         #. Open the downloaded installer.
         #. Follow the prompts.
         #. Accept all default settings.
         #. Open Powershell and make sure the installation completed.

            .. code:: powershell

               > python --version
               Python 3.7.0

            The output from :command:`python --version` might be a little different,
            but it should be whatever numbered version you downloaded.

            If you get an error here, something went wrong.
            Try running the installer again.
            You may also have to add Python to your Windows search path.
            You can do this by going to
            :menuselection:`Advanced System Settings -> Environmental Variables -> Edit System Variables`,
            then adding the path to the directory containing Python.
            If the problem persists, and you can't debug it yourself,
            asks us about it on |forum|_.

         .. _Python Releases for Windows: https://www.python.org/downloads/windows/

#. Set up your working directory

   In whatever directory (folder) on your computer where you organize projects,
   create a new directory for ODK-X,
   and then navigate to that directory.
   (We recommend calling this directory :file:`odk`,
   and the rest of the guide will assume that's what you called it.)

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            $ mkdir odk
            $ cd odk
            /odk/ $

      .. group-tab:: PowerShell

         .. code:: powershell

            > mkdir odk
            > cd odk
            /odk/ >

   For the rest of this guide,
   we assume you are in the :file:`/odk/` directory,
   or a subdirectory of it.

#. Set up a virtual environment

   A `virtual environment`_ is a Python construct
   that lets you download and install tools for a specific project
   without installing them for your entire computer.

   .. _virtual environment: https://docs.python.org/3/tutorial/venv.html

   #. Create the virtual environment.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               /odk/ $ python3 -m venv odkenv

         .. group-tab:: PowerShell

            .. code:: powershell

               /odk/ > python -m venv odkenv

   #. Activate the virtual environment.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               /odk/ $ source odkenv/bin/activate
               (odkenv) /odk/ $

         .. group-tab:: PowerShell

            .. code:: console

               /odk/ > source odkenv/bin/activate
               (odkenv) /odk/ >

      The ``(odkenv)`` before the prompt shows that the virtual environment is active.
      You will need to have this active any time you are working on the docs.

      If the file cannot be found, your activate file may be located under odkenv/scripts/activate.

      Later, to deactivate the virtual environment:

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/ $ deactivate
               /odk/ $

         .. group-tab:: PowerShell

            .. code:: console

               (odkenv) /odk/ > deactivate
               /odk/ >


#. Fork the ODK-X Docs repository to your own GitHub account.

   .. _fork-the-docs:

   A :dfn:`repository` (:dfn:`repo`) is a store of all the code and text for a project.
   The `ODK-X Docs repo`_ is kept at GitHub.

   On GitHub, a :dfn:`fork` is a copy of a repo,
   cloned from one user to another.
   In order to work on ODK-X Docs,
   you will create your own fork.

   #. Go to the `ODK-X Docs repo`_ on GitHub.
   #. Use the :guilabel:`Fork` button (top right) to create your own copy.
   #. After the process completes, you'll be looking at your own fork on GitHub.

   .. _ODK-X Docs repo: https://github.com/odk-x/docs

#. Clone down your copy to your local computer

   .. _clone-the-docs:

   #. From your own fork of the repo on GitHub, select the :guilabel:`Clone or download` button.
   #. Copy the URI from the text box that opens.
      It will be something like:
      ``https://github.com/your-gh-username/docs.git``

   #. Use your terminal to clone the repository.

      You should already be in the :file:`odk` directory,
      with the virtual environment active.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/ $ git clone https://github.com/your-github-username/docs.git
               .
               .
               .
               (odkenv) /odk/ $ cd docs
               (odkenv) /odk/docs/ $

         .. group-tab:: Powershell

            .. code:: powershell

               (odkenv) /odk/ > git clone https://github.com/your-github-username/docs.git
               .
               .
               .
               (odkenv) /odk/ > cd docs
               (odkenv) /odk/docs/ >

            .. warning::

               Some of the git commands produce meaningless errors in PowerShell.
               If you get an error when using git, but everything seems to work otherwise,
               ignore the error.

         .. note::

            This will cause your computer to download the entire ODK-X Docs repository,
            including a large number of images.
            It will take several minutes to complete.

      .. admonition:: Your local directory

         If you followed the instructions,
         you should now have the following directory structure:

         -  :file:`odk`

            - :file:`docs`
            - :file:`odkenv`

         The :file:`odkenv` directory stores your virtual environment,
         and you should not need to open it or directly view its content.
         Just ignore it.

         The :file:`docs` directory is your copy of the ODK-X Docs repo.
         You will do most of your work in this directory.

         If you need to download or create additional files
         which are not actually a part of the ODK-X Docs repository,
         keep them out of the :file:`docs` directory.

         You can use the main :file:`odk` directory
         for any other files you need to work on.
         (For example,
         you may want to create a directory called :file:`odk/forms`
         to hold XLSForm and XForm files.)

#. Set the upstream remote

   .. _upstream-the-docs:

   In git, a :dfn:`remote` is a copy of a repo somewhere else.
   From your local computer's point of view,
   your online copy at GitHub is a remote.

   When you cloned down a repo,
   your local copy gives your GitHub copy the name ``origin``.

   You also need to give the primary ODK-X Docs repo a name,
   and our convention is to name it ``upstream``.

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git remote add upstream https://github.com/odk-x/docs.git
            (odkenv) /odk/docs/ $ git remote -v
            origin https://github.com/your-github-username/docs.git (fetch)
            origin https://github.com/your-github-username/docs.git (push)
            upstream https://github.com/odk-x/docs.git (fetch)
            upstream https://github.com/odk-x/docs.git (push)


      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > git remote add upstream https://github.com/odk-x/docs.git
            (odkenv) /odk/docs/ > git remote -v
            origin https://github.com/your-github-username/docs.git (fetch)
            origin https://github.com/your-github-username/docs.git (push)
            upstream https://github.com/odk-x/docs.git (fetch)
            upstream https://github.com/odk-x/docs.git (push)

   If everything went right,
   you should see output similar to what is shown above.

#. Install Python tools with pip

   .. _install-doc-dependencies:

   `Pip`_ is a package management tool that comes with Python.
   We use it to download and install our documentation tools.
   These Python tools are listed in :file:`requirements.txt`.

   .. _Pip: https://pip.pypa.io/en/stable/user_guide/

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ pip install --upgrade pip
            (odkenv) /odk/docs/ $ pip install -r requirements.txt

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > pip install --upgrade pip
            (odkenv) /odk/docs/ > pip install -r requirements.txt

   The first command `upgrades pip`_ itself to the latest version.
   Then second checks :file:`requirements.txt` and installs everything listed in it.
   This will take several moments.

   .. _upgrades pip: https://pip.pypa.io/en/stable/installing/#upgrading-pip

   .. note::

      If you are ever running one of the build commands shown below
      and it fails with a message that includes ``ModuleNotFoundError``,
      there might be changes to :file:`requirements.txt`
      since you originally ran :command:`pip install -r requirement.txt`.
      Run the installation again
      and then retry your build.

#. Choose a text/code editor

   .. _choose-editor:

   The documentation source files are written in a plain text format called `reStructuredText`_.
   This means special formatting (bullets, headers, bold text) is represented by visible characters,
   not hidden behind a graphical display.
   When working on a documentation file,
   you see and write something that looks like:

   .. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html

   .. code:: rst

      #. Choose a text/code editor

         The documentation source files
         are written in a plain text format called `reStructuredText`_.

         .. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html

   You cannot write and edit these files
   in a typical document preparation program like :program:`MS Word` or :program:`Google Docs`.
   Instead, you need a coding editor.

   There are a lot of editors,
   and people who use them often have very strong opinions about them.
   You are free to choose any editor you like.

   If you've never used an editor before,
   you might want to start with one of the easier and more popular ones:

   - `Atom <https://atom.io/>`_
   - `Sublime <https://www.sublimetext.com/>`_
   - `VS Code <https://code.visualstudio.com/>`_
   - `Notepad++ <https://notepad-plus-plus.org/>`_ (Windows only)

   Most of these have plugins that will make writing reStructuredText easier
   by color-coding the markup.

This completes the setup of your local working environment.
Take a break before diving into how you actually work.

.. _docs-workflow-details:

Working on the docs
-------------------

#. Find an issue to work on.

   Work on ODK-X Docs is planned using the GitHub repository's `issue tracker`_.

   #. Browse the `issue tracker`_ and find one you may want to work on.
   #. Make sure you understand the goal of the project.
      If the goal isn't clear, ask.
      If there is anything in the issue that doesn't make sense, ask about it.
      Feel free to make suggestions about how something could be accomplished.
   #. If you decide to work on an issue,
      assign yourself to it by writing **@opendatakit-bot claim** in a comment.
   #. If the issue requires a novel or creative solution not defined in the issue already
      (we've stated a problem and you think you know a way to fix it)
      write a comment describing your plan.
      It is a good idea to get feedback on an idea before working on it.
      Often, other contributors can provide additional context
      about why a particular solution may or may not work.

   .. _issue tracker: https://github.com/odk-x/docs/issues

   .. admonition:: Your first issue

      The very first issue you should work on as a new ODK-X Docs contributor is
      `Issue 19 --- Line Edits`_.
      The issue is very simple:

      1. Find a typo.
      2. Fix the typo.

      This will help you get used to working with the documentation tools,
      and helps us get rid of the inevitable errors that creep in to our writing.

      .. _Issue 19 --- Line Edits: https://github.com/odk-x/docs/issues/19

#. Make sure you are on the master branch

   .. _check-at-master:

   A branch is a named sequence of changes representing work on the repo.
   For example, if you were going to work on `Issue 19 --- Line Edits`_,
   you would create a new branch called ``line-edits`` to hold that work.
   When you were done,
   you would merge those changes back to the main branch,
   which we call ``master``.

   The first time you clone the docs repo and start working,
   you will be on the `master` branch.

   Each time you come back to starting work on a new issue,
   make sure you are on the ``master`` branch before continuing.

   #. Check the current branch with :command:`git branch`.
      This will output a list of branches, with a star next to the current one.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/docs/ $ git branch
                  branch-name
                  branch-name
                  branch-name
                * master
                  branch-name

         .. group-tab:: PowerShell

            .. code:: powershell

               (odkenv) /odk/docs/ > git branch
                  branch-name
                  branch-name
                  branch-name
                * master
                  branch-name

   #. If you are not on master, switch to master with :command:`git checkout`.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/docs/ $  git checkout master
               Switched to branch 'master'
               Your branch is up to date with 'origin/master'.

         .. group-tab:: PowerShell

            .. code:: powershell

               (odkenv) /odk/docs/ >  git checkout master
               Switched to branch 'master'
               Your branch is up to date with 'origin/master'.

#. Pull in changes from upstream

   .. _git-pull-the-docs:

   Other people are constantly making changes to the docs,
   so you need to keep your local copy up to date.

   Before you start working, use :command:`git pull`
   to pull in the changes from the upstream repository's master branch.
   Then, just to be sure, you can use :command:`git status`
   to make sure everything is up to date.

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git pull upstream master
            (odkenv) /odk/docs/ $ git status
            On branch master
            Your branch is up to date with 'origin/master'.

            nothing to commit, working tree clean

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > git pull upstream master
            (odkenv) /odk/docs/ > git status
            On branch master
            Your branch is up to date with 'origin/master'.

            nothing to commit, working tree clean

         .. warning::

            Some git commands (including :command:`git pull` and :command:`git checkout`)
            send error messages to PowerShell even when they work correctly.
            If everything seems to be working,
            you can ignore these.

#. Create a new branch for your work.

   .. _git-branch-the-docs:

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git checkout -b branch-name
            Switched to a new branch 'branch-name'

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > git checkout -b branch-name
            Switched to a new branch 'branch-name'

   Branch names should be short, lowercase, and use hyphens as separators.
   They do not need to carry a lot of information (like your name or the date).

   Good branch names:

   - ``getting-started-guide``
   - ``contributing``
   - ``fix-issue-13``

   Bad branch names:

   - ``getting started guide``
   - ``Getting started guide``
   - ``Getting_started_guide``
   - ``writing-the-getting-started-guide-adammichaelwood-july-2017-draft``

#. Work on the documentation

   .. _write-the-docs:

   Finally, you can open an :ref:`editor of your choice <choose-editor>`
   and work on the documentation.

   The source files for documentation text are in these directory:

   :file:`odkx-src`
      Files for the pages at https://docs.odk-x.org/

   If you're going to write or edit documentation text, please read:

   - :doc:`docs-syntax-guide`
   - :doc:`docs-style-guide`

   If you're working on code or deployment, please read:

   - :doc:`docs-developer-guide`

#. Local checks

   .. _test-the-docs:

   Once you have worked on the documentation,
   we want to make sure your contribution
   will get accepted and published right away.

   To ensure your changes will pass all the deployment tests,
   you should run the tests locally first
   and correct any problems.

    .. tabs::

       .. group-tab:: Bash

          .. code:: console

             (odkenv) /odk/docs/ $ make odkx-check

       .. group-tab:: PowerShell

          .. code:: powershell

             (odkenv) /odk/docs/ > rm -r -fo tmpx-src
             (odkenv) /odk/docs/ > rm -r -fo odkx-build
             (odkenv) /odk/docs/ > Copy-Item odkx-src -Destination tmpx-src -Recurse
             (odkenv) /odk/docs/ > sphinx-build -b spelling tmpx-src odkx-build/spelling
             (odkenv) /odk/docs/ > python util/check-spelling-output.py odkx-build


    This will send some output to the terminal,
    which will include mentions of any words not in the dictionary.

    -  If the flagged words are really misspellings, correct them.

    -  If the flagged words are not misspelled, and *should* be in the dictionary
       add them to :file:`spelling_wordlist.txt`.

    -  If the flagged words are not misspelled, but *should not* be in the dictionary
       (for example, they are non-words that make sense on a single page for a specific reason)
       add them at the top of the file in which they are being used,
       before the title heading:

       .. code:: rst

          .. spelling::

             abc
             def
             exe
             functool

          This Is The Page Title
          ======================

    When adding new words to :file:`spelling_wordlist.txt` or the top of a document file,
    please keep the words in alphabetical order.

#. Build and check

   .. _build-the-docs:

   We use a Python tool called `Sphinx`_
   to compile all the :file:`.rst` files into a working website.

   .. _Sphinx: http://www.sphinx-doc.org

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            make odkx

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > rm -r -fo tmpx-src
            (odkenv) /odk/docs/ > rm -r -fo odkx-build
            (odkenv) /odk/docs/ > Copy-Item odkx-src -Destination tmpx-src -Recurse
            (odkenv) /odk/docs/ > sphinx-build -b dirhtml tmpx-src odkx-build

   This generates a lot of output.
   Near the end of the output you may see a statement like:

   .. code-block:: none

      build succeeded, 18 warnings.

   Those warnings are problems with the text
   which you need to fix before submitting your changes.
   Scroll up in the terminal to find each warning,
   so that you can address it in the source files.

   A Sphinx warning looks like this:

   .. code-block:: none

      /path/to/file-name.rst:LINENUMBER: WARNING: warning message

      short excerpt from the file

   This tells you what file the problem is in,
   the approximate line number,
   and the nature of the problem.
   Usually that is enough to fix it.
   If you can not figure out the meaning of a particular warning,
   you can always ask about it on the |forum|_.

   .. note::

      Because of a `bug in Sphinx`_
      the line numbers in error and warning messages
      will be off by about 15 lines
      (the length of ``rst_prolog`` in :file:`conf.py`).

      .. _bug in Sphinx: https://github.com/sphinx-doc/sphinx/issues/2617

   As you fix each warning,
   run the build again to see if it disappears from the output.

   .. note::

      The warning messages will refer to the file name
      using the temporary directory path :file:`tmp1-src` or :file:`tmpx-src`.
      You need to correct the problems in the real source directory
      (:file:`odkx-src`).

   .. admonition:: When you just can't fix the error...

      If you've done your best and asked on the |forum|_,
      and you still cannot correct the warning,
      stop worrying about it and skip to the next step.
      When you submit your changes on GitHub,
      include a note about the warning.
      Other contributors will help solve the problem before merging.

   Once you've corrected all the warnings that can be corrected...

#. Serve the documentation website locally and view it.

   .. _serve-the-docs-locally:

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ python -m http.server -d odkx-build 8000
            Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > python -m http.server -d odkx-build 8000
            Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)

   #. Open your browser and go to http://localhost:8000.
   #. Read through your doc edits in the browser.
   #. Go back to the source files to correct any errors you find.
   #. Go to your terminal, and press :kbd:`CTRL C` to shut down the local web server.
   #. Re-run the build and serve steps.
   #. Continue proofreading.

   Once you are reasonably sure your changes are ready...

#. Commit your changes to your local repository.

   .. _commit-the-docs:

   A :dfn:`commit` is snapshot of your working files in a particular state,
   along with a record of all the changes that led up to that state.
   That snapshot is what you will submit to the main repository.

   .. note::

      We explain how to do a commit at this step
      because you need to do it before you can submit your changes.
      However, you don't have to wait until you are done to commit.
      You can commit as many times as you like while working.

      This can be especially helpful if you are working on a complicated set of changes,
      over several working sessions.

   #. Stage the files for commit with :command:`git add`.

      To stage all changes for commit:

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/docs/ $ git add -A

         .. group-tab:: PowerShell

            .. code:: powershell

               (odkenv) /odk/docs/ > git add -A

   #. Commit the staged files with :command:`git commit`.

      .. tabs::

         .. group-tab:: Bash

            .. code:: console

               (odkenv) /odk/docs/ $ git commit -m "Write a commit message here."

         .. group-tab:: PowerShell

            .. code:: powershell

               (odkenv) /odk/docs/ > git commit -m "Write a commit message here."

      Your commit message needs to be wrapped in quote marks.
      It should, in a sentence or less, explain your work.

#. Push your committed changes to your GitHub repo with :command:`git push`.

   .. _push-the-docs:

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git push origin branch-name

      .. group-tab:: PowerShell

         .. code:: powershell

            (odkenv) /odk/docs/ > git push origin branch-name

         .. warning::

            The :command:`git push` command produces meaningless errors in PowerShell.
            If you get an error when using :command:`git push`,
            but everything seems to work otherwise,
            ignore the error.

      .. tip::

         You may be prompted to enter your GitHub username and password.
         When entering your password, the cursor won't move ---
         it will look like you aren't entering anything,
         even though you are.

         To avoid having to retype these every time,
         you can `store your GitHub credentials locally`_.

         .. _store your GitHub credentials locally:
            https://help.github.com/articles/caching-your-github-password-in-git/

#. Issue a pull request from your GitHub repo to the main ODK-X Docs repo.

   .. _pr-the-docs:

   A :dfn:`pull request` (or PR)
   is a request from you to the ODK-X Docs maintainers
   to pull in your changes to the main repo.

   #. Go to the `ODK-X Docs repo on GitHub`_.
      (Make sure you are logged in.)

      .. _ODK-X Docs repo on GitHub: https://github.com/odk-x/docs

   #. Find the message near the top of the page that mentions your recent pushed branches.
      Select :guilabel:`Compare & pull request` to start a pull request.
   #. Follow GitHub's instructions to start the pull request.

      These details should fill-in automatically,
      but be sure to double-check them:

      - :guilabel:`Base fork` should be the main repo (``opendatakit/docs``).
      - :guilabel:`base` should be ``master``.
      - Your repo and working branch name should be listed beside them.

      You will see either a green **Able to be merged** message
      or a message informing that the branch can not be merged.
      You can proceed in either case.
      If the branch cannot be merged,
      the maintainers will work with you to resolve the problem.

   #. Write a PR message explaining your work.

      The PR message field includes a template to remind you of what to include.
      Fill in the template and delete any sections which are not applicable.

      A good PR message includes:

      - The issue number you are working on.
        (Write ``closes #123`` if the PR completes the work for the issue.
        If there's still work to do, write ``addresses #123``.)
      - A summary of what you did.
      - Details of work that still needs to be done.
      - Details of new work created or implied by this PR.
      - Details of any unresolved errors or warnings,
        including details of what you tried.
      - Justification for any changes to :file:`requirements.txt`.
      - Details of any difficulties, questions, or concerns
        that came up while working on this issue.

   #. Submit your pull request.

   The maintainers and other contributors will review your PR as quickly as possible.
   They may request changes to your work.
   If changes are needed:

      #. **Don't worry.**
         Revision is a normal part of technical writing,
         and everyone (even the project's founders and leaders)
         has their work reviewed and are frequently asked to revise it.
      #. Work on the files again locally.
         (Use :command:`git branch` to make sure you are still in the same working branch.)
      #. :ref:`Stage and commit <commit-the-docs>` your changes locally again
         (:command:`git add -A`; :command:`git commit -m "Commit message"`).
      #. :ref:`Push your commit <push-the-docs>` (:command:`git push origin branch-name`).
      #. Your new commits will automatically update the PR.
         Do not start a new PR.

   Once everything has been approved,
   the changes will be merged in and will appear on :doc:`this website <index>`.
   At that point... congratulations!
   You are now a contributor to ODK-X.

.. _keep-working-the-docs:

The next time you work
----------------------

We hope that contributing to ODK-X Docs is a rewarding experience
and that you'll want to keep going.
Each time you start work on a new issue
the process is the same as outline above.

Here are a few things to keep in mind when you start your next contribution.

#. Return to ``master`` with :command:`git checkout master`.

   New work is done on new branches which are started from master.
   So, before you start a new branch, return to the master branch.

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git checkout master

      .. group-tab:: PowerShell

         .. code:: console

            (odkenv) /odk/docs/ > git checkout master

#. Pull in changes with :command:`git pull upstream master`.

   You need to start your new work from
   the latest version of everyone else's work.

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git pull upstream master

      .. group-tab:: PowerShell

         .. code:: console

            (odkenv) /odk/docs/ > git pull upstream master

#. Update the master branch of your online GitHub repository.

   .. tabs::

      .. group-tab:: Bash

         .. code:: console

            (odkenv) /odk/docs/ $ git push origin master

      .. group-tab:: PowerShell

         .. code:: console

            (odkenv) /odk/docs/ > git push origin master

#. Find a `new issue to work on`_.
#. `Start a new branch for your work <git-branch-the-docs>`_ with :command:`git checkout -b branch-name`.

.. _new issue to work on: https://github.com/odk-x/docs/issues/

.. _keep-improving:

Keep improving
--------------

As you are getting comfortable with the contribution process,
take a few minutes to read our :doc:`contributing-tips`.
You may also want to dig deeper into the
:doc:`docs-style-guide` and the :doc:`docs-syntax-guide`.
(And if you are writing code,
check out the :doc:`docs-developer-guide`.)

And don't forget to join us on the |forum|_.

ODK-X is a community,
and we depend on each other's work.
Thank you for your contribution to ODK-X Docs
and your presence in this community.
