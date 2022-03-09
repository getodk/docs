.. ODK documentation master file, created by
   sphinx-quickstart on Wed May 24 09:46:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ODK's Docs!
======================

:dfn:`ODK` is a suite of open source tools that help organizations collect and manage data.

For a quick start, read :doc:`getting-started`. In most cases, users of ODK:

- Create survey forms using the `XLSForm <http://xlsform.org/>`_ standard in Excel or `Google Sheets <https://www.google.com/sheets/>`_.
- :ref:`Upload forms <central-forms-upload>` to an :doc:`ODK Central server <central-intro>`.
- :ref:`Download forms <in-app-get-blank-forms>` into :doc:`collect-intro` on an Android device.
- :doc:`Use Collect to fill out forms <collect-filling-forms>` with :term:`participants <participant>`.
- :ref:`Upload survey data <uploading-forms>` from Collect to Central.
- :doc:`Analyze or export data from Central <central-submissions>`.

This requires:

- :doc:`Installing Collect on an Android device <collect-install>`
- :doc:`Installing Central on a server <central-setup>`

While this is the recommended workflow, it is not the only way to do things. ODK is a very flexible set of tools, and organizations will find their own best practices for adopting it.

Additional ODK tools are:

- :doc:`build-intro`, a drag-and-drop form designer. We generally recommend XLSForm for its flexibility but users only building very simple forms may prefer Build.
- :doc:`briefcase-intro`, a desktop tool that pulls and exports data from Aggregate and Collect.

The specifications and libraries that power the tools are:

- :doc:`openrosa`, APIs for how ODK clients communicate with ODK servers.
- `ODK XForms spec <https://getodk.github.io/xforms-spec/>`_, a subset of the W3C XForms specification, for use in the ODK ecosystem.
- `ODK JavaRosa <https://github.com/getodk/javarosa>`_, a Java library that renders forms complying with ODK XForms.
- `XLSForm spec <https://getodk.github.io/xforms-spec/>`_, a high-level Excel-based form specification.
- `pyxform <https://github.com/xlsform/pyxform>`_, a Python library that converts XLSForms into ODK XForms.

For a complete list of our tools, check out `ODK on GitHub <https://github.com/getodk>`_.

.. toctree::
  :maxdepth: 1
  :hidden:

  getting-started

.. toctree::
  :hidden:
  :maxdepth: 1
  :caption: Collect

  collect-intro
  collect-setup
  collect-using
  collect-best-practices

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Central

  central-intro
  central-setup
  central-using

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Form Building

  form-design-intro
  xlsform
  form-question-types
  form-logic
  form-operators-functions
  form-datasets
  form-styling
  form-language
  form-audit-log
  launch-apps-from-collect
  form-tools
  form-best-practices

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Briefcase

  briefcase-intro
  briefcase-install
  briefcase-using

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Training

  training

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Contributing

  contributing

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Developing with ODK

  openrosa
  javarosa
  launch-collect-from-app
  briefcase-api

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Integration

  encrypted-forms

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Reference

  security-privacy
  glossary
