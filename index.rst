.. Open Data Kit documentation master file, created by
   sphinx-quickstart on Wed May 24 09:46:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Open Data Kit's documentation!
=========================================

:dfn:`Open Data Kit` (ODK) is a suite of open source applications that help organizations engaged in enumerator-mediated data collection. ODK tools assist with the collection and management of survey data using digital forms. These include the primary ODK applications:

- :doc:`collect-intro`, an Android mobile app that replaces paper-based forms.
- :doc:`aggregate-guide`, a server-side data storage and analysis tool.

Also part of the ODK suite are several tools that support form creation and data management:

- **ODK Build** lets you design forms with a drag-and-drop form interface.
- **ODK Validate** validates forms against the ODK XForms specification.
- **ODK Form Uploader** uploads blank forms and their media files to ODK Aggregate.
- **ODK Briefcase** packages and transfers data between instances of Collect and Aggregate.

ODK also maintains libraries and specifications that support these applications.

- **ODK XForm** is a subset of the W3 XForm specification, for use in the ODK ecosystem.
- **ODK JavaRosa** is a Java library that renders forms complying with the ODK XForm specification.
- **XLSForm** defines an Excel format for designing forms.


For a complete list of our projects, check out `Open Data Kit on Github <https://github.com/opendatakit>`_.


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

  aggregate-guide
  aggregate-install
  aggregate-deployment-planning
  aggregate-use
  aggregate-upgrade
  aggregate-backup
  form-uploader
  oauth2-service
  visualize
  aggregate-limitations

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Briefcase

  briefcase-guide
  briefcase-install
  briefcase-forms
  briefcase-vs-aggregate

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Form Building

  form-design-intro
  odk-build
  xlsform
  form-widgets
  form-interaction
  form-update
  pyxform
  validate
  launch-apps-from-collect
  
.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Contributing 

  contributing
  cygwin
  contributing-tips
  style-guide

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
  verify-downloads
  faq
  glossary
