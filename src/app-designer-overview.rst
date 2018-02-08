ODK Application Designer Overview
==================================

.. _app-designer-overview:

This section presents a brief overview of the features of the ODK Application Designer.

The ODK Application Designer is accessed through a :program:`Chrome` browser. Once launched, it opens :program:`Chrome` to display:

.. image:: /img/app-designer-overview/app-designer-preview.*
  :alt: The Preview tab of the Application Designer rendered in a Chrome web browser.

This screen has 6 tabs:

  - :ref:`Preview <app-designer-overview-preview>` (shown above) - used to preview ODK Survey forms and ODK Tables list-, detail- and graph- views (future). Displays these within a user-selected device geometry.
  - :ref:`Customize <app-designer-overview-customize>` - a visual style and visual theme editor. This editor immediately shows the effects of changes to specific settings in your CSS file. This functionality is undergoing changes and not recommended.
  - :ref:`XLSX Converter <app-designer-overview-xlsx>` - converts the XLSX description of a form into a :file:`formDef.json` representation used by ODK Survey.
  - :ref:`File Browser <app-designer-overview-file>` - enables browsing of the directory structure that will exist on your Android device so that you can access or view other files (currently necessary for accessing the ODK Tables list- and detail- views).
  - :ref:`Scan Form Designer <app-designer-overview-scan>` - drag-and-drop mark-sense form designer tool.

.. _app-designer-overview-preview:

Preview
-----------
The :guilabel:`Preview` tab (shown above) has several controls:

  - :guilabel:`Launch Page` -- what webpage to launch in the window below.
  - :guilabel:`Purge Database` -- during development, if you are adding new fields or changing their data types, you will need to purge the database so that the database structure can be re-generated with the proper fields and data types.
  - :guilabel:`Device Dimensions` -- what dimensions to make the window below.
  - :guilabel:`Back Button` -- this is generally only useful when viewing ODK Tables web pages.

.. warning::

  The :guilabel:`Back Button` may cause unpredictable results when used while displaying ODK Survey forms.

The Launch Page opens the ODK Survey Framework Page. This is the :file:`formDef.json` in the Android device's application frameworks folder (:file:`/sdcard/opendatakit/default/config/assets/framework/forms/framework`). The contents of this form are defined by the :file:`framework.xlsx` file in that same directory.

For example, if you click on the household test form, and click the :guilabel:`Follow Link` button on the next screen, the *Household Survey* form is launched, yielding this screen:

.. image:: /img/app-designer-overview/household-survey.*
  :alt: Rendering of a survey titled Household Survey in the Application Designer as it would appear on the Android device.

You can navigate through forms, enter and exit sub-forms, and save results just like on your Android device.

.. note::

  The development environment does not allow you to submit data to a server. ODK Deploy (currently under development, not yet released) will provide this functionality.

.. _app-designer-overview-customize:

Customize
-----------
The :guilabel:`Customize` tab contains the CSS style and theme generator:

.. image:: /img/app-designer-overview/theme-generator.*
  :alt: The theme generator tab modifying the appearance of the Example Form

Using this tool, you can change background colors, fonts, and other settings affecting the appearance of a form. The changes are reflected immediately in the form shown to the left of the toolbar.

This functionality is under active development and not currently recommended.

.. _app-designer-overview-xlsx:

XLSX Converter
-----------------
The :guilabel:`XLSX Converter` tab contains the conversion tool that transforms XLSX files produced by Excel or OpenOffice into the :file:`formDef.json` file used by ODK Survey:

.. image:: /img/app-designer-overview/xlsxconverter.*
  :alt: The XLSX Converter tab

See :doc:`xlsx-converter-intro` documentation for more information about this tool.

.. _app-designer-overview-file:

File Browser
----------------
The :guilabel:`File Browser` tab provides a view into what will become the application's directory on the phone.

.. image:: /img/app-designer-overview/file-browser.*
  :alt: The File Browser tab

.. _app-designer-overview-scan:

ODK Scan Form Designer
--------------------------
The :guilabel:`Scan Form Designer` tab presents a drag-and-drop editor for mark-sense form creation.

.. image:: /img/app-designer-overview/scan-form-designer.*
  :alt: The ODK Scan Form Designer tab

See :doc:`scan-form-designer-intro` documentation for more information about this tool.

