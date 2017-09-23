.. Open Data Kit documentation master file, created by
   sphinx-quickstart on Wed May 24 09:46:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Open Data Kit's documentation!
=========================================

:dfn:`Open Data Kit` (ODK) is a suite of open source applications that help organizations engaged in enumerator-mediated data collection. ODK tools assist with the collection and management of survey data using mobile forms. These include the primary ODK applications:

- **ODK Collect**, an Android mobile app that replaces paper-based forms.
- **ODK Aggregate**, a server-side data storage and analysis tool.

Also part of the ODK suite are several tools that support form creation and data management:

- **ODK Build** lets you design forms with a drag-and-drop form interface.
- **ODK XLSForm** lets you design forms in Excel.
- **ODK Validate** validates forms against the ODK XForms specification.
- **ODK Form Uploader** uploads blank forms and their media files to ODK Aggregate.
- **ODK Briefcase** packages and transfers data between instances of Collect and Aggregate.

ODK also maintains libraries and specifications that support these applications.

- **ODK XForm** is a subset of the W3 XForm specification, for use in the ODK ecosystem.
- **ODK JavaRosa** is a Java library that renders forms complying with the ODK XForm specification.

For a complete list of our projects, check out `Open Data Kit on Github <https://github.com/opendatakit>`_.


.. toctree::
  :maxdepth: 1 
  :hidden:

  getting-started

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Collect

  collect-guide
  collect-install
  collect-settings
  collect-forms
  collect-adb
  
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Briefcase

   briefcase-guide
   briefcase-install
   briefcase-forms
   briefcase-vs-aggregate.rst

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Form Building

  form-widgets
  javarosa
  
.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Contributing 

  contributing
  cygwin
  
.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Reference
  
  glossary

