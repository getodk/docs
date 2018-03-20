:orphan:
	
Printing Labels with the Printer Widget
==========================================

The :ref:`print-widget` can be used to print labels 
directly from Collect to 
`a Zebra MZ or iMZ label printer <https://www.zebra.com/us/en/products/printers/mobile/mz-series.html>`_.

.. image:: /img/printer-widget/printed-labels.*
  :alt: Two paper labels. One label has a 1D barcode and some text. The other has a QR code and some text.

.. admonition:: Requirements

  The print widget requires two additional apps to be installed on your device:
  
  - `ODK Sensors Framework <https://play.google.com/store/apps/details?id=org.opendatakit.sensors>`_
  - `ODK Zebra Printer Driver <https://play.google.com/store/apps/details?id=org.opendatakit.sensors.drivers.zebra.bt>`_

  
Labels contain one or more of the following:

- 1D Barcode, encoding a number
- QR Code, encoding text
- Text

These three components always appear in this order.
Their conent is specified 
in the :th:`Calculate` column of the XLSForm,
using a :tc:`concatenate()` formula.
The three components are included as strings, 
separated by ``'<br>'``, 
the XML line break tag.

.. csv-table:: survey
  :header: type, name, label, appearance, calculation

   text,printer_widget, Printer widget,printer:org.opendatakit.sensors.ZebraPrinter, "concat('123456789','<br>’,'QRCODE','<br>','Text')"

To exclude any of the label components,
put an empty string in its place.
For example, to print only a QRCODE, with no barcode or text:

.. csv-table::
  :header: calculation
  
  "concat('','<br>','QRCODE content here','<br>','')"
  
Or, to print only the barcode and text:

.. csv-table::
  :header: calculation
  
  "concat('1234567890','<br>','','<br>','Some text.')"
  
Including data from previous questions
----------------------------------------

Typically, labels are used to print data from previous questions.

For example, 
you might print a label with the name 
of the survey :term:`participant`:

.. csv-table::
  :header: type, name, label, appearance, calculation
  
  text, full_name, Participant Name, , 
  text, print_name_label, Print Name Label, printer:org.opendatakit.sensors.ZebraPrinter, "concat('','<br>','${full_name}',<br>,'${full_name}')"
