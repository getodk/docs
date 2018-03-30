ODK Scan
============

.. _scan-intro:

.. warning::

  ODK Scan is not yet fully released! It is not guaranteed to work at the same quality level as ODK Survey, Tables, Services, or the rest of the release ODK 2 tools.

  It is currently at the **Release Candidate** stage, which mean does not have support for deployments, but the ODK core team does guarantee a migration path (possibly with many tedious manual steps) into future releases.

:dfn:`ODK Scan` is an Android application that uses the device’s camera and specialized code to automatically digitize written data from paper forms. Using the app, users take pictures of paper forms and ODK Scan detects and collects the fill-in bubble, checkbox, and written number data. It also saves image snippets of handwritten text and displays them on the screen for easy data entry. The digitized data can then be validated, exported, saved into a database, and used for custom data reports. This workflow from paper form to digital database occurs in five processes and is supported through the use of ODK suite tool

.. image:: /img/scan-intro/scan-process.*
  :alt: The ODK Scan Process

.. _scan-intro-user-guide:

User Guide
----------------------------

.. toctree::
  :maxdepth: 2

  scan-install
  scan-using

.. _scan-intro-architect-guide:

Deployment Architect Guide
----------------------------

.. toctree::
  :maxdepth: 2

  scan-managing
  scan-data
