Form Widgets
===============

This document is a list of available :term:`ODK Collect` :term:`form` :term:`widgets <widget>` (question types), with:

- examples images from the ODK Collect app
- example Excel spreadsheet rows for creating form widgets with :term:`ODK XLSForm`
- example :term:`ODK XForm` XML snippets

.. _string-input:

String Input
--------------

.. image:: /img/form-widgets/string-input.*
  :alt: String input form widget, displayed in ODK Collect on an Android phone. The label is "What is your full name?"

XLSForm Rows
~~~~~~~~~~~~~~~

Survey
"""""""""

======  ========= ========================   =========
type    name      label                      required
======  ========= ========================   =========
string	full_name What is your full name?    true()
======  ========= ========================   =========

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/odk-example-form/full_name" required="true()" type="string"/>

  <input ref="/odk-example-form/full_name">
    <label>What is your full name?</label>
  </input>
