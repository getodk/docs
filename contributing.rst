***************************
Contributing to ODK Docs
***************************


Authoring Tools and Environment
=====================================

ODK Documentation follows (as much as possible) the `Docs like Code <http://www.writethedocs.org/guide/docs-as-code/>`_ philosophy. This means:

- Documention source files are written in a plaintext format. (We use `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.)
- Documentation source files are kept under version control. (We use git and `Github <https://github.com/opendatakit/docs>`_.)
- Documentation is built from source to published output using a static site generator. (We use `Sphinx <http://sphinx-doc.org>`_.)
- Documentation builds are run, tested, and deployed automatically using continuous integration tools. (We use `CircleCI <https://circleci.com/>`_.)

`The Docs as Code approach has many advantages <http://hackwrite.com/posts/docs-as-code/>`_, but we are aware that this approach can feel difficult for writers who aren't used to dealing with the command line. It can also be difficult for coders who are used to this approach, but who typically use simpler authoring tools (like `Jekyll <http://jekyllrb.com>`_ and `Markdown <https://guides.github.com/features/mastering-markdown/>`_).

This section of the Contributor Guide walks through our authoring and publishing workflow and toolchain, to make it as easy possible for you to contribute.

.. warning::

  This contributor guide is written from a *nix (Bash Terminal) perspective, which works on all flavors of Linux and MacOS. If you are on Windows, you will need to:

  - adapt the commands to your environment
  - use the Linux subsystem (Windows 10)
  - use a bash terminal emulator

  Contributions to this guide with explanations and help for Windows users is greatly appreciated.

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
