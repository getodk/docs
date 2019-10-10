ODK XLSX Converter
====================

.. _xlsx-converter-intro:

:dfn:`ODK XLSX Converter` is a tool, similar to XLSForm, that converts XLSX files (created with :program:`Excel`) into ODK Survey definition files that are used by ODK Survey.

.. warning::

  Forms created with XLSX Converter are not compatible with ODK Collect. They only work with ODK Survey.

For example, a spreadsheet like this:

.. csv-table:: Example Spreadsheet
  :header: "type", "name", "display.prompt.text"

  "begin screen",
  "text", "name", "Enter name:"
  "integer", "age", "Enter age:"
  "end screen",

Will result in a survey like this:

.. image:: /img/xlsxconverter/survey-screen.*
  :alt: An example rendering of a basic XLSX file in ODK Survey
  :class: device-screen-vertical

.. tip::

  See :file:`exampleForm.xlsx` (located at the path :file:`app/config/tables/exampleForm/forms/exampleForm/` in the Application Designer) for a more extensive list of examples.

.. _xlsx-converter-intro-architect-guide:

Deployment Architect Guide
------------------------------------

.. toctree::
  :maxdepth: 2

  xlsx-converter-using
  xlsx-converter-reference

