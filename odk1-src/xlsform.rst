.. spelling::

  io

******************************
XLSForm
******************************

.. _xlsform-introduction:

:dfn:`XLSForm` is a tool to simplify the creation of forms. Forms designed with Excel can be converted to *XForms* that can be used with ODK tools. It is available for use as `XLSForm Online <https://opendatakit.org/xiframe/>`_ and `XLSForm Offline <https://github.com/opendatakit/xlsform-offline/releases>`_.


Using the Application
~~~~~~~~~~~~~~~~~~~~~~~

- To design your form, you can refer to the `XLSForm form design documentation <http://xlsform.org/>`_.
- Once your XLSForm is ready, you convert it with `XLSForm Online <https://opendatakit.org/xiframe/>`_ or `XLSForm Offline <https://github.com/opendatakit/xlsform-offline/releases>`_.


Other XLSForm converters
~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`pyxform <running-pyxform>` is a Python library. It works offline and can be used on the command line to convert forms.
- `Ona <https://ona.io/home/>`_, `Kobo <http://www.kobotoolbox.org/>`_, and `Enketo <https://enketo.org/>`_ also offer XLSForm support.

.. note::
  
  - Forms do not have to be uploaded to :ref:`Aggregate <aggregate-introduction>` before they are used. They can be manually added to :ref:`Collect <collect-introduction>`. Simply place them in the :file:`/odk/forms` folder on your Android device’s SD card.
