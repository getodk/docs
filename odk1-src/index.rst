.. Open Data Kit documentation master file, created by
   sphinx-quickstart on Wed May 24 09:46:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ODK's Docs!
======================

:dfn:`Open Data Kit` (ODK) is a suite of open source tools that help organizations collect and manage data. 

The core ODK tools are:

- :doc:`collect-intro`, an Android app that replaces paper-based forms.
- :doc:`aggregate-intro`, a proven server for data storage and analysis tool.
- :doc:`central-intro`, a modern server with a RESTful API.
- :doc:`build-intro`, a drag-and-drop form designer.
- :doc:`ODK XLSForm </xlsform>`, an Excel-based form designer.
- :doc:`briefcase-intro`, a desktop tool that pulls and exports data from Aggregate and Collect.

The specifications and libraries that power the tools are:

- :doc:`openrosa`, APIs for how ODK clients communicate with ODK servers.
- `ODK XForms spec <https://opendatakit.github.io/xforms-spec/>`_, a subset of the W3C XForms specification, for use in the ODK ecosystem.
- `ODK JavaRosa <https://github.com/opendatakit/javarosa>`_, a Java library that renders forms complying with ODK XForms.
- `XLSForm spec <https://opendatakit.github.io/xforms-spec/>`_, a high-level Excel-based form specification.
- `pyxform <https://github.com/xlsform/pyxform>`_, a Python library that converts XLSForms into ODK XForms.

For a complete list of our tools, check out `Open Data Kit on GitHub <https://github.com/opendatakit>`_.

.. _using-odk:

How is ODK used?
------------------

For a quick start, read :doc:`getting-started`. In most cases, users of ODK:

- Create survey forms using `Build <https://build.opendatakit.org/>`_ or `XLSForm <http://xlsform.org/>`_.
- :ref:`Upload forms <aggregate-add-new-forms>` to an :doc:`aggregate-intro` server.
- :ref:`Load forms <in-app-get-blank-forms>` into :doc:`collect-intro` on an Android device.
- :doc:`Use Collect to fill out forms <collect-filling-forms>` with :term:`participants <participant>`.
- :ref:`Upload survey data <uploading-forms>` from Collect to Aggregate.
- :doc:`Analyze or export data in Aggregate <aggregate-data>`.

This requires:

- :doc:`Installing Collect on a phone or other mobile device <collect-install>`
- :doc:`Installing Aggregate on a server <aggregate-install>`

While this is the *typical* use pattern, it is not the only way to do things. ODK is a very flexible set of tools, and organizations will find their own best practices for adopting it.


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
  :caption: Aggregate

  aggregate-intro
  aggregate-setup
  aggregate-use
  aggregate-best-practices

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Briefcase

  briefcase-intro
  briefcase-install
  briefcase-using
  briefcase-and-aggregate

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Central (Alpha)

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
  form-styling
  form-language
  form-operators-functions
  form-audit-log
  launch-apps-from-collect
  form-tools
  form-best-practices
  
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
