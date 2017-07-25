Getting Started Guide
=========================

.. _what-is-odk:
What is ODK?
--------------

Open Data Kit (ODK) is a suite of open source applications that help organizations collect and manage survey data using mobile forms. These include the primary ODK applications:

- **ODK Collect**, an Android mobile app that replaces paper-based forms.
- **ODK Aggregate**, a server-side data storage and analysis tool.

Also part of the ODK suite are several tools that support form creation and data management:

- **ODK Build** lets you design forms with a drag-and-drop form interface.
- **ODK XLSForm** lets you design forms in Excel.
- **ODK Validate** validates forms against the ODK XForms specification.
- **ODK Form Uploader** uploads blank forms and their media files to ODK Aggregate.
- **ODK Briefcase** packages and transfers data between instances of Collect and Aggregate.

ODK also maintains several specifications and tools that support these applications. For a complete list of our projects, check out `Open Data Kit on Github <https://github.com/opendatakit>`_.

.. _using-odk:
Using ODK
-----------

In most cases, users of ODK:

- Create survey forms using `Build <https://build.opendatakit.org/>`_ or `XLSForm <http://xlsform.org/>`_
- Upload forms to an Aggregate server
- Load forms into Collect on an Android phone
- Use Collect to fill out forms with :term:`subjects <subject>`
- Upload survey data from Collect to Aggregate
- Analyse or export data in Aggregate

This requires:

- :ref:`Installing Collect on a phone or other mobile device <install-collect>`
- :ref:`Installing Aggregate on a server <install-aggregate>`

.. tip::

  While this is the *typical* use pattern, it is not the only way to do things. For example:

  - Forms can be created using tools other than Build or XLSForm
  - Forms can be uploaded directly to Collect, without using Aggregate

  ODK is a very flexible set of tools, and orgnizations will find their own best practices for adopting it.
