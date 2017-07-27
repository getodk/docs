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



Terminal (Command Line)
--------------------------

.. warning::

  This contributor guide is written from a *nix (Bash Terminal) perspective, which is relevant to all flavors of Linux and MacOS. If you are on Windows, you will need to do one of the following:

  - adapt the commands to your environment
  - use the `Linux subsystem (Windows 10)<https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/>`_
  - use a `bash terminal emulator <https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/>`_

  Contributions to this guide with explanations and help for Windows users is greatly appreciated.

Contributing to the docs requires interacting with git, Github, Python, and Sphinx, which requires use of the Terminal. This is common among Linux users. Mac users unfamiliar with the Terminal can learn more from `this tutorial <https://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855>`_.

Github and git
----------------

The general workflow for contributing to this repo is:

- Fork to your own Github Account
- Clone down to your local machine
- Work locally
  - Branch for a specific task
  - Make commits as you go
- Push your branch to your Github fork
- Issue a pull request against the current working branch of the main repo (usually ``master``)
- Pull latest back to your local machine from the main repo
- Work locally...
