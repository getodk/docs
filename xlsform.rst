******************************
XLSForm
******************************

.. _xlsform-introduction:

:dfn:`XLSForm` (formerly XLS2Xform) is a tool to simplify the creation of forms. Forms designed with Excel can be converted to *XForms* that can be used with ODK tools.

.. note::
  
  - When this tool was renamed to XLSForm there were many changes to the syntax. The new version is mostly backwards compatible with the old syntax.
  - XLSForm works with ODK Collect version *1.1.7* or later.


Using the Application
~~~~~~~~~~~~~~~~~~~~~~~

- To design your form, you can refer to the `XLSForm form design documentation <http://xlsform.org/>`_ and check out the `sample Excel file <https://opendatakit.org/wp-content/uploads/2013/06/sample_xlsform.xls>`_.
- Once your xls form is ready, you can submit it `for conversion here <http://opendatakit.org/xiframe/>`_.

Other XLSForm converters
~~~~~~~~~~~~~~~~~~~~~~~~~

- For Windows users, a standalone (non-web-based) version of this tool (without the error report) is also available on our `downloads page here <https://opendatakit.org/downloads/download-info/xlsform-for-windows/>`_. If you use that tool, you should also download ODK Validate (`from here <https://opendatakit.org/downloads/download-info/odk-validate-2/>`_) and run the generated form through that tool to generate an error report.
- Nafundi's `XLSForm Offline <https://gumroad.com/l/xlsform-offline#/>`_ is an app for Windows and Mac that can convert and validate forms. It is always available, very fast, and easy to use.
- :ref:`pyxform <running-pyxform>` is a Python library. It works offline and can be used on the command line to convert forms.
- XLSForm is also available through `Ona <https://ona.io/home/>`_.io which requires internet connection and also makes it easy to share converted forms and collected data.

.. note::
  
  - `Enketo <https://enketo.org/>`_ previews generated from this converter will not include media.
  - Forms do not have to be uploaded to :ref:`Aggregate <aggregate-introduction>` before they are used. They can be manually added to :ref:`Collect <collect-introduction>`. Simply place them in the :file:`/odk/forms` folder on your Android device’s SD card.
  - For a simpler, more user friendly form designer, try `Build <https://opendatakit.org/use/build/>`_. For more powerful form designers, try `Kobo <http://www.kobotoolbox.org/>`_ or `enketo <https://enketo.org/>`_ or `PurcForms <https://code.google.com/archive/p/purcforms/>`_. We also have `sample forms <https://github.com/opendatakit/sample-forms/>`_ (Examples forms are not available for all the features) and `form design documentation <https://opendatakit.org/help/form-design/>`_. And in particular, `design guidelines <https://opendatakit.org/help/form-design/guidelines/>`_ if you wish to design forms manually.


