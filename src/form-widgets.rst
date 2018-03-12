.. spelling::

  abcd
  ack
  BREATHCOUNT
  Datetime
  dateTime
  dk
  na
  nocalendar
  nolabel
  placementmap
  uw
  ZXing

***************
Form Widgets
***************

This document is a list of available ODK :term:`Collect` :term:`form` :term:`widgets <widget>` (question types), with:

- example images from the ODK Collect app
- example Excel spreadsheet rows for creating form widgets with :term:`XLSForm`
- example :term:`ODK XForm` XML snippets

.. _basic-form-widgets:

Basic Form Widgets
=====================

This section shows examples of all the form widgets types, with no additional options displayed.

.. _string-input:

String Input
--------------

A simple text input.

.. image:: /img/form-widgets/string-input.*
  :alt: String input form widget, displayed in ODK Collect on an Android phone. The label is "What is your name?"
  :class: device-screen-vertical

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  text, name, What is your name?

.. _single-select:

Single Select
----------------

A radio-button single choice from several options.

.. image:: /img/form-widgets/single-select.*
  :alt: Single-select (radio button) form widget, displayed in ODK Collect on an Android phone. The question label is "What is your favorite fruit?" After the question is a list of fruits.
  :class: device-screen-vertical

XLSForm Rows
~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  select_one fruit_list, fruits, What is your favorite fruit?

.. csv-table:: choices
  :header: list_name, name, label

  fruit_list, apple, apple
  fruit_list, pear, pear
  fruit_list, peach, peach
  fruit_list, strawberry, strawberry
  fruit_list, pineapple, pineapple
  fruit_list, orange, orange
  fruit_list, grape, grape
  fruit_list, plum, plum

The **list_name** in the **choices** table matches the string *after* ``select_one`` in the **type** column of the **survey** table.

.. _multi-select:

Multi-select
-------------

A checkbox-list selection of multiple items. (The example includes a :term:`hint`.)

.. image:: /img/form-widgets/multi-select.*
  :alt: Multi-select (checkbox-list) form widget, displayed in ODK Collect on an Android phone. The question label is "What vegetables do you enjoy?" and the hint text "Select all the apply." After the question is a list of vegetables.
  :class: device-screen-vertical

XLSForm Rows
~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, hint

  select_multiple veggie_list, veggies, Which vegetables do you enjoy?, Select all that apply.

.. csv-table:: choices
  :header: list_name, name, label

  veggie_list, broccoli. broccoli
  veggie_list, carrot, carrot
  veggie_list, spinach, spinach
  veggie_list, tomato, tomato
  veggie_list, bell_pepper, bell pepper
  veggie_list, asparagus, asparagus


- The **list_name** in the **choices** table matches the string *after* ``select_one`` in the **type** column of the **survey** table.
- The content of **name** cannot have spaces.

.. _integer:

Integer
---------

A whole number entry input. Integer widgets will not accept decimal points.

.. image:: /img/form-widgets/integer.*
  :alt: An integer form widget displayed in ODK Collect on an Android phone. The question is "What is your age in years?" A numerical keyboard is displayed.

XLSForm Rows
~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  integer, age, What is your age in years?

.. _decimal:

Decimal
----------

A numerical entry input that will accept decimal points.

.. image:: /img/form-widgets/decimal.*
  :alt: An integer form widget displayed in ODK Collect on an Android phone. The question is "Weight in kilograms." A numerical keyboard is displayed.

XLSForm Rows
~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  decimal, weight, Weight in kilograms.

.. _geopoint:

Geopoint
------------

A single set of GPS coordinates. The example includes a :term:`hint`.

.. image:: /img/form-widgets/geopoint-start.*
  :alt: A geopoint form widget displayed in ODK Collect on an Android phone. The question headline is "Current location." Below that is the hint text "You might have to turn on your GPS," followed by a button with the label "Start GeoPoint."


.. image:: /img/form-widgets/geopoint-working.*
  :alt: A modal popup over an obscured screen. The headline of the modal is "Loading Location." The text is "Please wait. This could take a few minutes." There are two options: "Cancel" and "Save Geopoint."


.. image:: /img/form-widgets/geopoint-completed.*
  :alt: A completed geopoint form widget. It looks the same as before, but now has four fields below the button: Latitude, Longitude, Altitude, and Accuracy.


XLSForm Rows
~~~~~~~~~~~~~~~~

.. csv-table:: survey
 :header: type, name, label, hint

 geopoint, current_location, Current location., You might have to turn on your GPS.


.. _geotrace:

GeoTrace
-----------

A line or polygon of GPS coordinates tracking actual device movement. The user can specify one of two location-recording modes:

- Manual Mode — The user taps the device to place a marker as desired while moving.
- Automatic Mode — The app creates a marker on a regular time interval (default: 20 seconds) as the user moves.


.. image:: /img/form-widgets/geotrace-start.*
  :alt: A geotrace form widget displayed in the ODK Collect app on an Android phone. The question text is "Where have you been?" and below that is a button with the label "Start GeoTrace."

.. image:: /img/form-widgets/geotrace1.*
  :alt: A modal popup over a map. The modal headline is "Zoom to..." Below that are two options: "Zoom to current location" (selected) and "Zoom to saved feature". In the bottom-right of the modal is a Cancel button.

.. image:: /img/form-widgets/geotrace2.*
  :alt: A map displayed in the ODK Collect App on an Android phone. Above the map is the instruction: Wait for lock, then tap add marker button start. On the right side are five icon buttons stacked vertically: Add marker, Zoom, Layers, Trash, Save.

.. image:: /img/form-widgets/geotrace3.*
  :alt: The same map as displayed in the previous image. Over the map is a modal popup. The modal headline is "Select GeoTrace Mode," followed by two radio-button (single select) options: Manual Mode (selected) and Automatic Mode. In the bottom-right are buttons for Cancel and Start.

.. image:: /img/form-widgets/geotrace4.*
  :alt: The same modal popup as in the previous image, but the Automatic Mode radio button is not selected. Below it are two drop-down select boxes. Their values are "20" and "seconds."

.. image:: /img/form-widgets/geotrace5.*
  :alt: The same map as displayed previously, but now a series of red markers form a line across the map.

.. image:: /img/form-widgets/geotrace6.*
  :alt: The same map as previously, with a new modal popup. The headline of the modal is "Save GeoTrace as" followed by two options: Save as Polygon and Save as Polyline. In the bottom-right is a Cancel button.

.. image:: /img/form-widgets/geotrace7.*
  :alt: The Geotrace form widget, as shown previously. The question text is "Where have you been?" and the button label is "View or Change GeoTrace." Below that is a list of lat/long GPS coordinates.


XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  geotrace, trace_example, Where have you been?

.. _geoshape:

GeoShape
------------

A user-entered series of GPS coordinates, forming a polygon.

.. image:: /img/form-widgets/geoshape-start.*
  :alt: The GeoShape form widget, as displayed in the ODK Collect app on an Android phone. The question text is "Select an Area." Below that is a button labeled "Start GeoShape."

.. image:: /img/form-widgets/geoshape1.*
  :alt: A modal popup over a map. The modal headline is "Zoom to..." Below that are two options: "Zoom to current location" (selected) and "Zoom to saved feature". In the bottom-right of the modal is a Cancel button.

.. image:: /img/form-widgets/geoshape2.*
  :alt: A map displayed in the ODK Collect App on an Android phone. Above the map is the instruction: "Long press to place marks." On the right side are five icon buttons stacked vertically: Add marker, Zoom, Layers, Trash, Save.

.. image:: /img/form-widgets/geoshape3.*
  :alt: The same map as displayed previously, but now a series of red markers form a polygon across the map.

.. image:: /img/form-widgets/geoshape4.*
  :alt: The GeoShape form widget shown previously. The question text is "Select an Area." The button label is now "View or Change GeoShape." Below the button is a list of lat/long GPS coordinates.

XLSForm Rows
~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  geoshape, shape_example, Select an area.

.. _date:

Date
---------

A date selector.

.. image:: /img/form-widgets/date-start.*
  :alt: The date selection form widget, as displayed in the ODK Collect app on an Android phone. The question text is "What is your birthday?" The button label is "Select date." Below that is the message "No date selected."

.. image:: /img/form-widgets/date1.*
  :alt: The same form widget screen as previously, overlaid with a modal popup calendar. The headline is a date: 2017 Tue, Aug 8. The main body shows a monthly calendar with selectable days and arrows for scrolling month-to-month. In the bottom-right are Cancel and OK buttons.

.. image:: /img/form-widgets/date-start.*
  :alt: The date selection form widget as shown previously. Below the "Select date" button is the date Aug 01, 2017.

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  date, birthday, What is your birthday?

.. _time:

Time
-------

A time selector. Captures only a specific time-of-day, not a date and time. For date and time, see :ref:`datetime`.

.. image:: /img/form-widgets/time-start.*
  :alt: The Time form widget as displayed in the ODK Collect App on an Android phone. The question text is "What time do you usually wakeup?" The button label is "Select time." Below the button is the message "No time selected."

.. image:: /img/form-widgets/time1.*
  :alt: The Time widget as displayed previously, with a modal popup. The modal headline is "Select time." The body of the modal contains scrollers for Hour, Minute, and AM/PM. At the bottom of the modal are Cancel and OK buttons.

.. image:: /img/form-widgets/time2.*
  :alt: The Time form widget as displayed previously. Below the "Select time" button is "06:30".

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  time, wakeup, What time do you usually wakeup?

.. _ethiopian-calendar:

Ethiopian Calendar
--------------------

An Ethiopian-calendar. The main calendar used in Ethiopia. Users can enter a date according to the Ethiopian calendar system, and also see the corresponding Gregorian (standard) calendar date.

.. image:: /img/form-widgets/ethiopian-start.*
  :alt: The Ethiopian calendar form widget as displayed in the ODK Collect App on an Android phone. The headline is "Ethiopian Calendar". The button label is "Select date." Below the button is the message "No date selected."

.. image:: /img/form-widgets/ethiopian2.*
  :alt: The same form widget screen as previously, overlaid with popup calendar. The modal headline is "Select date." The main body shows the ethiopian calendar and contains scrollers for Day, Month and Year. Just below the main body, date according to the Ethiopian and Gregorian calendar system can be seen. In the bottom-right are Cancel and OK buttons.

.. image:: /img/form-widgets/ethiopian3.*
  :alt: The Ethiopian calendar form widget as displayed previously. The headline is "Ethiopian Calendar". The button label is "Select date." Below the button is the message "22 Tikimt 2010 (Nov 01, 2017)."

XLSForm Rows
~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  date, ethiopian-calendar, Ethiopian Calendar


.. _datetime:

Datetime
-----------

A datetime selector. For date only, see :ref:`date`. For time only, see :ref:`time`.

.. image:: /img/form-widgets/datetime-start.*
  :alt: The Datetime form widget as displayed in the ODK Collect App on an Android phone. The question text is "When was the last time you ate?" Below the question are two buttons. The first button is labeled "Select date" and below it is the message "No date selected." The second button is labeled "Select time" and below it is the message "No time select."

.. image:: /img/form-widgets/datetime1.*
  :alt: The same form widget screen as previously, overlaid with a modal popup calendar. The headline is a date: 2017 Tue, Aug 8. The main body shows a monthly calendar with selectable days and arrows for scrolling month-to-month. In the bottom-right are Cancel and OK buttons.

.. image:: /img/form-widgets/datetime2.*
  :alt: The Datetime form widget as displayed previously. The question text is "When was the last time you ate?" Below the question are two buttons. The first button is labeled "Select date" and below it is the date "Aug 08, 2017" The second button is labeled "Select time" and below it is the message "No time select."

.. image:: /img/form-widgets/datetime3.*
  :alt: The Datetime widget as displayed previously, with a modal popup. The modal headline is "Select time." The body of the modal contains scrollers for Hour, Minute, and AM/PM. At the bottom of the modal are Cancel and OK buttons.

.. image:: /img/form-widgets/datetime2.*
  :alt: The Datetime form widget as displayed previously. The question text is "When was the last time you ate?" Below the question are two buttons. The first button is labeled "Select date" and below it is the date "Aug 08, 2017" The second button is labeled "Select time" and below it is the time "06:45"

XLSForm Rows
~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  dateTime, previous_meal, When was the last time you ate?

.. _image:

Image
----------

An image collector. The user can choose to select an image stored on the device or take a new picture. The example includes :term:`hint` text.

.. image:: /img/form-widgets/image-start.*
  :alt: The Image widget as displayed in the ODK Collect App on an Android phone. The question text is "Please take a self portrait." Below the question is the hint text, "A 'selfie.'" There are two buttons: Take Picture and Choose Image.

.. image:: /img/form-widgets/image1.*
  :alt: The camera app on an Android phone, with a person's face in the camera image. Below the camera image is a large, blue Checkbox button.

.. image:: /img/form-widgets/image2.*
  :alt: The Image widget as displayed previously. Below the buttons is the photo of a face from the previous camera app image.

XLSForm
~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, hint

  image, selfie, Please take a self portrait., A "selfie."


.. _audio:

Audio
--------

An audio recording collector.

.. image:: /img/form-widgets/audio-start.*
  :alt: The Audio form widget as displayed in the ODK Collect App on an Android phone. The question text is "Please record your name." There are three buttons: Record Sound, Choose Sound and Play Sound. The "Play Sound" button is disabled.

.. need to complete the audio widget sequence of images

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  audio, name_pronounce, Please record your name.

.. _video:

Video
--------

A video collector. The example includes :term:`hint` text.

.. image:: /img/form-widgets/video-start.*
  :alt: The Video form widget as displayed in the ODK Collect App on an Android phone. The question text is "Please record a video of yourself blinking." The hint text is "Three times is probably sufficient." Below that are three buttons: Record Video, Choose Video, and Play Video. The Play Video button is disabled.


.. image:: /img/form-widgets/video1.*
  :alt: The Android camera app, in video mode. A person's face is in the camera viewer. Below the camera viewer is a large, blue checkmark button.

.. image:: /img/form-widgets/video2.*
  :alt: The Video form widget as displayed previously. The question text is "Please record a video of yourself blinking." The hint text is "Three times is probably sufficient." Below that are three buttons: Record Video, Choose Video, and Play Video. All three buttons are enabled.

XSLForm Rows
~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, hint

  video, blinking, Please record a video of yourself blinking., Three times is probably sufficient.


.. _note:

Note
---------

A note to the user, accepting no input. This example includes :term:`hint` text.

.. figure:: /img/form-widgets/note.*
  :alt: The Note form widget as displayed in the ODK Collect App on an Android phone. The headline text is, "This is an example note." The hint text is, "The text displays, but there is no input."

XSLForm Rows
~~~~~~~~~~~~~~

.. csv-table::
  :header: type, name, label, hint

  note, note_1, This is an example note., "The text displays, but there is no input."


.. _barcode:

Barcode
----------

Captures the text from a barcode using the device camera. Supported barcode formats are described [here](https://github.com/zxing/zxing/#supported-formats). Non-printing control codes are removed.

The flash can be used as a light source when scanning barcodes in a poorly-lit environment.

.. note::
  Barcode scanning is built into ODK Collect versions 1.7.0 and greater. Versions of ODK Collect prior to 1.7.0 require the [ZXing app](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) to be installed.

.. image:: /img/form-widgets/barcode-start.*
  :alt: The Barcode form widget as displayed in the ODK Collect app on an Android phone. The headline text reads, "Scan any barcode." Below that is an image labeled "Get Barcode."

.. image:: /img/form-widgets/barcode1.*
  :alt: A barcode scanner on an Android device. A barcode is in the viewfinder, with a thin blue line across the barcode.

.. image:: /img/form-widgets/barcode2.*
  :alt: The Barcode form widget as displayed previously. The button label is now "Replace Barcode." Below the button is a string of numbers representing the decoded content of the scanned barcode.

XSLForm Rows
~~~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  barcode, barcode_example, Scan any barcode.

.. _acknowledge:

Acknowledge
-------------

An acknowledgment prompt with a single checkbox. In :term:`Aggregate`, a completed acknowledgment is stored as the string response ``OK``.

.. image:: /img/form-widgets/acknowledge.*
  :alt: The Acknowledge form widget as displayed in the ODK Collect app on an Android phone. The headline text is, "I acknowledge this acknowledgment." Below that is a single checkbox with the label, "OK. Please continue."

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  acknowledge, ack_sample, I acknowledge this acknowledgment.

.. _appearance:

Widget Formatting with Appearance
==================================

In your :term:`xlsform` sheet, you can optionally specify an :th:`appearance` column. This will affect widget display and functionality in :term:`Collect`.

.. _text-widgets:

Text Widgets
-------------

.. _text-default:

Default Appearance
~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/text-no-appearance.*
  :alt: The default String widget, as displayed in the ODK Collect app on an Android phone. The question text is "String Widget." Below that is a simple text input. Above the question text is the form group name, "Text widgets."


XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label

  text,string_widget,String widget


.. _string-number:

String Number
~~~~~~~~~~~~~~~

A numerical input that treats the input as a string, rather than a number.

.. image:: /img/form-widgets/string-number.*
  :alt: The text widget, with numerical entry, as displayed in the ODK Collect app on an Android phone. The question text is "String number widget." The hint text is, "text type with numbers appearance." Below that is a simple input. Above the question text is the form group name "Text Widget." The Android onscreen keyboard displays a number pad.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  text,string_number_widget,String number widget,numbers,text type with numbers appearance


.. _url-widget:

URL Widget
~~~~~~~~~~~~

Provides a link which the user can open from the survey. Takes no input.

The URL to open is specified with :th:`default`.

.. image:: /img/form-widgets/url-widget.*
  :alt: The URL form widget, as displayed in the ODK Collect app on an Android phone. The question text is "URL Widget." The hint text is "text type with url appearance and default value of http://opendatakit.org/" Below that is a button labeled, "Open URL." Below the button is the URL, "http://opendatakit.org/" Above the question text is the form group name "Text widgets."

XLSForm Rows
"""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint, default

  text,url_widget,URL widget,url,text type with url appearance and default value of http://opendatakit.org/,http://opendatakit.org/




.. _external-app-widget:

External App String Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launches an external app and receives a string input back from the external app. If the specified external app is not available, a manual input is prompted.

The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`. The rest of the :th:`appearance` string specifies the application to launch.

.. image:: /img/form-widgets/external-app-widget-start.*
  :alt: The External App form widget, as displayed in the ODK Collect App on an Android phone. The question text is "Ex string widget." The hinst text is, "text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form group name "Text widgets."

.. image:: /img/form-widgets/external-app-widget-fallback.*
  :alt: The External App widget as displayed earlier. The Launch button has now been disabled. Below it is a simple input. A help message displays the text, "The requested application is missing. Please manually enter the reading."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  text,ex_string_widget,Ex string widget,ex:change.uw.android.BREATHCOUNT,text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)


.. _external-printer-widget:

External Printer Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

Connects to an external printer. See `printing widget <https://opendatakit.org/help/form-design/examples/#printing_widgets>`_ for complete details.

.. pull printing widget detail into its own doc in this repo

.. image:: /img/form-widgets/printer-widget.*
  :alt: The external printer widget, as displayed in the ODK Collect app on an Android phone. The question text is "Ex printer widget." The hint text is "text type with printer:org.opendatakit.sensors.ZebraPrinter." Below that is a button labeled, "Initiate Printing." Above the question text is the form group name "Text widgets."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

   text,ex_printer_widget,Ex printer widget,printer:org.opendatakit.sensors.ZebraPrinter,text type with printer:org.opendatakit.sensors.ZebraPrinter


.. _number-widget:

Number Widgets
---------------

.. _default-integer-widget:

Default Integer Widget
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-integer-widget.*
  :alt: The default Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Integer Widget." The hint text is "integer type with no appearance." Below that is a simple input. The numerical keypad is active. Above the question text is the form group name "Numerical widgets."

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  integer,integer_widget,Integer widget,integer type with no appearance

.. _external-integer-widget:

External Integer Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

Launches an external app and receives an integer input back from the external app. If the specified external app is not available, a manual input is prompted.

.. image:: /img/form-widgets/external-integer-widget-start.*
  :alt: The External Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Ex integer widget." The hint text is, "integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form name "Numerical widgets."

.. image:: /img/form-widgets/external-widget-fallback.*
  :alt: The External Integer widget as displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, "The requested application is missing. Please manually enter the reading."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  integer,ex_integer_widget,Ex integer widget,ex:change.uw.android.BREATHCOUNT,integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)

.. _default-decimal-widget:

Default Decimal Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-decimal-widget.*
  :alt: The default Decimal form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Decimal widget." The hint text is "decimal type with no appearance." Below that is a simple input. The number pad is active. Above the question text is the form group name "Numerical widgets."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  decimal,decimal_widget,Decimal widget,decimal type with no appearance

.. _external-decimal-widget:

External Decimal Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

Launches an external app and receives a decimal number input back from the external app. If the specified external app is not available, a manual input is prompted.

.. image:: /img/form-widgets/external-decimal-start.*
  :alt: The External Decimal form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Ex decimal widget." The hint text is, "decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form group name "Numerical widgets."

.. image:: /img/form-widgets/external-decimal-fallback.*
  :alt: The External Decimal widget displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, "The requested application is missing. Please manually enter the reading."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  decimal,ex_decimal_widget,Ex decimal widget,ex:change.uw.android.BREATHCOUNT,decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)

.. _bearing-widget:

Bearing Widget
~~~~~~~~~~~~~~~~

Captures a compass reading.

.. image:: /img/form-widgets/bearing-widget-start.*
  :alt: The Bearing form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Bearing widget." The hint text is, "decimal type with bearing appearance. Below that is a button labeled "Record Bearing." Above the question text is the form group name "Numericl widgets."

.. image:: /img/form-widgets/bearing-in-progress.*
  :alt: The Bearing widget, overlaid with a model popup. The modal headline is "Loading Bearing." In the body of the modal are two fields: "Direction: W" and "Bearing: 273.001". At the bottom of the modal are Cancel and Record Bearing buttons.

.. image:: /img/form-widgets/bearing-finished.*
  :alt: The Bearing widget, as displayed previously. The button's label is not "Replace bearing." Below the button is the decimal number 271.538 (the recorded bearing).

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  decimal,bearing_widget,Bearing widget,bearing,decimal type with bearing appearance


.. _image-widgets:

Image Widgets
---------------

.. _default-image-widget:

Default Image Widget
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-image-widget.*
  :alt: The default Image form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Image Widget." The hint text is, "image type with no appearance." Below that are two buttons: "Take Picture" and "Choose Image." Above the question text is the form group name "Image widgets."

XLSForm Rows
""""""""""""""
.. csv-table:: survey
  :header: type, name, label, hint

  image,image_widget,Image widget,image type with no appearance


.. _selfie-widget:

Selfie Widget
~~~~~~~~~~~~~~~

Takes a picture using the front-facing ("selfie") camera. The "Choose picture" button is not displayed.

.. image:: /img/form-widgets/selfie-start.*
  :alt: The Selfie form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Selfie widget." The hint text is, "image type with selfie appearance." There is a single button, labeled "Take Picture." Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/selfie-in-progress.*
  :alt: A camera view on an Android phone. A person is taking a self-portrait.

.. image:: /img/form-widgets/selfie-complete.*
  :alt: The Selfie form widget as displayed previously. Below the button is the self-portrait from the previous image.

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  image,selfie_image_widget,Selfie widget,selfie,image type with selfie appearance


.. _draw-widget:

Draw Widget
~~~~~~~~~~~~~

Provides the user a drawing pad and collects the drawn image.

.. image:: /img/form-widgets/draw-widget.*
  :alt: The Draw form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Draw widget." The hint text is "image type with draw appearance." Below that is a button labeled "Sketch Image." Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/draw-in-progress.*
  :alt: A white "drawing pad" on an Android phone, horizontally oriented (landscape mode). A simple smiley face has been drawn. In the lower right corner of the drawing pad is a plus sign (+) in a circle.

.. image:: /img/form-widgets/draw-options.*
  :alt: The drawing pad as displayed in the previous image. A menu has expanded from the lower right corner with the options: Reset, Save and Close, and Set Color.

.. image:: /img/form-widgets/draw-completed.*
  :alt: The Draw widget as displayed previously. Below the "Sketch Image" button is the smiley face from the drawing pad image shown previously.

XLSForm Rows
"""""""""""""

.. csv-table:: survey

  :header: type, name, label, appearance, hint

  image,draw_image_widget,Draw widget ,draw,image type with draw appearance

.. _annotate-widget:

Annotate Widget
~~~~~~~~~~~~~~~~~~

Allows the user to take or select an image and then draw on it.

.. image:: /img/form-widgets/annotate-start.*
  :alt: The Annotate form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Annotate widget." The hint text is, "image type with annotate appearance." There are three buttons: "Take Picture," "Choose Image," and "Markup Image." The Markup Image button is disabled. Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/annotate-1.*
  :alt: The camera view on an Android phone. In the viewer is a picture of a small saucer. Below the viewer is a blue checkmark button.

.. image:: /img/form-widgets/annotate-2.*
  :alt: The Annotate form widget displayed previously. The Markup Image button is now enabled. Below the buttons is the picture of a saucer shown previously.

.. image:: /img/form-widgets/annotate-3.*
  :alt: The image of a saucer on a drawing pad, with a poorly-drawn cup of tea drawn over it. In the lower right corner is a plus sign (+) in a circle.

.. image:: /img/form-widgets/annotate-4.*
  :alt: The same picture shown in the previous image. The menu in the bottom right corner has expanded to show the options: Reset, Save and Close, and Set Color.

.. image:: /img/form-widgets/annotate-5.*
  :alt: The Annotate form widget shown previously. The drawn-on picture is below the buttons.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  image,annotate_image_widget,Annotate widget,annotate,image type with annotate appearance

.. _signature-widget:

Signature Widget
"""""""""""""""""

Collects a signature from the user.

.. image:: /img/form-widgets/signature-start.*
  :alt: The Signature form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Signature widget." The hint text is "image type with signature appearance." Below that is a button labeled "Gather Signature." Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/signature-in-progress.*
  :alt: A drawing pad with a signature line, displayed on an Android phone. A signature is drawn across it. In the lower right corner is circular button marked with a plus sign (+).

.. image:: /img/form-widgets/signature-completed.*
  :alt: The signature widget displayed previously. Below the button is the signature drawn in the previous image.

XLSForm Rows
"""""""""""""

.. csv-table:: table
  :header: type, name, label, appearance, hint

  image,signature_widget,Signature widget,signature,image type with signature appearance


.. _media-widgets:

Media Widgets
---------------

The media widgets do not accept any appearance attributes. They are documented in :ref:`basic-form-widgets` above:

- :ref:`barcode`
- :ref:`audio`
- :ref:`video`

.. _date-and-time-widgets:

Date and Time Widgets
----------------------

.. _default-date-widget:

Default Date Widget
~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-date-widget.*
  :alt: The default Date form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Date widget." The hint text is "date type with no appearance." Below that is a button labeled "Select date." Below that is the text, "No date selected." Above the question text is the form group name "Date and time widgets."

.. image:: /img/form-widgets/date-calendar-view.*
  :alt: The date widget shown in the previous image, with a modal popup showing a monthly calendar. A date is selected. At the bottom of the modal are Cancel and OK buttons.

.. image:: /img/form-widgets/date-completed.*
  :alt: The date widget shown previously. Below the button is a date: Aug 11, 2017.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  date,date_widget,Date widget,date type with no appearance

.. _date-no-calendar:

Date, No Calendar
~~~~~~~~~~~~~~~~~~~

The :tc:`no-calendar` appearance displays a "spinner" type date selection. This is especially appropriate for selecting dates more than in the past.

.. image:: /img/form-widgets/date-no-calendar-start.*
  :alt: The no-calendar Date form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Date Widget." The hint text is "date type with no-calendar appearance." Below that is a button labeled "Select date." Below the button is the text, "No date selected." Above the question text is the form group name "Date and time widgets."

.. image:: /img/form-widgets/date-no-calendar-in-progress.*
  :alt: The date widget shown previously, with a pop modal. The headline of the modal is "Select date." There are individual "spinner" style selectors for month, day, and year. At the bottom of the modal are OK and Cancel buttons.

XSLForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_nocalendar,Date Widget,no-calendar,date type with no-calendar appearance

.. _date-type-month-year:

Month and Year Widget
~~~~~~~~~~~~~~~~~~~~~~

Collects only a month and year.

.. image:: /img/form-widgets/month-year-spinner.*
  :alt: The date widget, with a modal popup labeled "Select date." There are individual "Spinner" type selectors for month and year, but not for date. At the bottom are Cancel and OK buttons.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_month_year,Date widget,month-year,date type with month-year appearance


.. _year-widget:

Year Widget
~~~~~~~~~~~~

Collects only a year.

.. image:: /img/form-widgets/year-spinner.*
  :alt: The Year form widget, with a model popup labeled "Select date." There is a single "spinner" type selector for year. At the bottom are Cancel and OK buttons.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_year,Date widget,year,date type with year appearance

.. _time-widgets:

Time Widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :tc:`time` widget does not accept an appearance attribute.

See :ref:`basic-form-widgets` for details on:

- :ref:`time`
- :ref:`datetime`

The :ref:`datetime` widget accepts a :tc:`no-calendar` appearance. This changes the date selector to the "spinner" style shown in :ref:`date-no-calendar`.

.. _gps-widgets:

GPS Widgets
------------

.. _default-geopoint:

Default Geopoint
~~~~~~~~~~~~~~~~~~

The default :ref:`geopoint` widget collects the current GPS position (if available) from the device.

.. image:: /img/form-widgets/default-geopoint.*
  :alt: The default Geopoint form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Geopoint widget." The hint text is "geopoint type with no appearance." Below that is a button labeled "Start Geopoint." Below the button are completed fields for Latitude, Longitude, Altitude, and Accuracy.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  geopoint,geopoint_widget,Geopoint widget,geopoint type with no appearance


.. _placement-map-widget:

Geopoint Placement Map Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A geopoint with the appearance attribute :tc:`placement-map` allows the user to select a geopoint from a map.

.. image:: /img/form-widgets/geopoint-placement-map.*
  :alt: A map app opens on an Android phone. Above the map is the message: "Long press to place mark or tap add marker button." Along the right side of the map are buttons: Add Marker, Zoom to point, Layers, Trash, Save.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  geopoint,geopoint_widget_placementmap,Geopoint widget,placement-map,geopoint type with placement-map appearance


.. _geopoint-maps:

Geopoint with Map
~~~~~~~~~~~~~~~~~~~~~~

The default :ref:`geopoint` widget does not display a map to the user. With the added :tc:`maps` appearance attribute, a map of the recorded location is shown to the user. The user cannot select a different location on the map. (See :ref:`placement-map-widget` for a geopoint with a user-selected location.)

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  geopoint,geopoint_widget_maps,Geopoint widget,maps,geopoint type with maps appearance

.. _default-geoshape-geotrace:

Geoshape and Geotrace
~~~~~~~~~~~~~~~~~~~~~~

The :ref:`geopoint` and :ref:`geotrace` widgets do not accept any appearance attributes.

.. _single-select-widgets:

Single Select Widgets
----------------------

.. _default-select-one:

Default Single Select
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-single-select.*
  :alt: The default Single Select form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Select one widget." The hint text is "select_one type with no appearance, 4 text choices." Below that is a set of radio button selectors labeled A, B, C, and D. Above the question text is form group name "Select one widgets."

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  select_one opt_abcd,select_one_widget,Select one widget,"select_one type with no appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _spinner-widget:

Spinner Widget
~~~~~~~~~~~~~~~

Adding the :tc:`minimal` appearance attribute places the choices into a drop-down style menu.

.. image:: /img/form-widgets/select-one-minimal-start.*
  :alt: The Single Select form widget, with minimal appearance, as displayed in the ODK Collect app on an Android phone. The question text is "Spinner widget." The hint text is "select_one type with minimal appearance, 4 text choices." Below that is a drop-down style select menu with the prompt "Select One Answer." Above the question text is the form group name "Select one widgets."

.. image:: /img/form-widgets/select-one-minimal-expanded.*
  :alt: The Single Select form widget, wih minimal appearance, as displayed in the previously image. The select menu has expanded to show choices: A, B, C, D, and Remove Response.

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,spinner_widget,Spinner widget,minimal,"select_one type with minimal appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _autoadvance-widget:

Autoadvance Widget
~~~~~~~~~~~~~~~~~~~~~

Advances immediately to the next question once a selection is made.

.. video:: /vid/form-widgets/auto-advance.mp4

  Video showing auto-advance after the questions are answered.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_one_autoadvance_widget,Select one autoadvance widget,quick,"select_one type with quick appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _select-search-widget:

Select with Search Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of radio buttons with a search and filter function.

.. image:: /img/form-widgets/select-search-start.*
  :alt: The Select One form widget with search, as displayed in the ODK Collect app on an Android phone. The question text is, "Select one search widget." The hint text is, "select one type with search appearance, 4 text choices." Below that is a text input above four radio buttons labeled A, B, C, and D. Above the question text is the form group name, "Select one widgets." The phone's keyboard is active.

.. image:: /img/form-widgets/select-one-search-searching.*
  :alt: The Select One form widget as displayed previously. The text input contains a lowercase 'b'. There is a single radio button: B. The other three radio buttons are no longer displayed.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_one_search_widget,Select one search widget,search,"select_one type with search appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

.. _select-autocomplete:

Select with Autocomplete Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of radio buttons with a search and filter function. The search input has an autocomplete feature.

.. image:: /img/form-widgets/select-autocomplete.*
  :alt: The Select One form widget with autocomplete, as displayed in the ODK Collect app on an Android phone. The question text is "Select one search widget." The hint text is, "select one type with autocomplete appearance, 4 text choices." Below that is a text input followed by four radio buttons labeled A, B, C, and D. Above the question text is the form group name "Select one widgets." The device keyboard is active.

.. image:: /img/form-widgets/select-autocomplete-filtered.*
  :alt: The Select One form widget as displayed previously. The text input contains a lowercase 'b'. There is a single radio button: B. The other three radio buttons are no longer displayed.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_one_autocomplete_widget,Select one search widget,autocomplete,"select_one type with autocomplete appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D



.. _select-image-widget:

Default Single Select with Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set of radio buttons with text labels and accompanying images.

See :ref:`image-options` to learn more about including images in surveys.

.. image:: /img/form-widgets/default-single-image-select.*
  :alt: The Single Select form widget with images, as displayed in the ODK Collect app on an Android phone. The question text is, "Grid select one widget." The hint text is, "select_one type with no appearance, 4 image choices (a.jpg, b.jpb, c.jpg, d.jpg)." Below that is a set of radio buttons labeled A, B, C, and D. Below each radio button is a small icon of an animal: A - whale, B - frog, C - alligator, D - eagle. Above the question text is the form group name "Select one widgets."

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,grid_widget,Grid select one widget,,"select_one type with no appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _compact-single-image-select:

Compact Single Select with Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Image options are placed on a single line.

.. image:: /img/form-widgets/single-select-compact.*
  :alt: The compact Single Select form widget with images, as displayed in the ODK Collect app on an Android phone. The question text is "Grid select one widget." The hint text is, "select_one with compact appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)." Below that are four small animal icons arranged on a single line. Above the question text is the form group name "Select one widgets."

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,grid_widget_compact,Grid select one widget,compact,"select_one type with compact appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _compact-2:

Compact Single Select with Images, width specified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the :tc:`compact-{x}` style, you can specify the number of images to display on each row. To display two images on each row, specify an :th:`appearance` of :tc:`compact-2`.

.. image:: /img/form-widgets/single-image-select-compact-2.*
  :alt: The single select form widget with images and appearance of 'compact-2,' as displayed in the ODK Collect app on an Android phone. The question text is, "Grid select one widget." The hint text is "select_one type with compact-2 appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)." Below that are four animal icons arranged in a two-by-two grid. Above the question text is the form group name "Select one widgets."

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,grid_widget_compact2,Grid select one widget,compact-2,"select_one type with compact-2 appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg

.. _quickcompact-widget:

Compact Single Select with Images and Autoadvance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :tc:`quickcompact` appearance attribute combines the design of the :ref:`compact-single-image-select` widget with the :ref:`autoadvance-widget` functionality.

.. video:: /vid/form-widgets/quickcompact.mp4

  Video showing Compact single select widget and auto-advance after the question is answered.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,grid_widget_quickcompact,Grid select one widget,quickcompact,"select_one type with quickcompact appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _quickcompact-2-widget:

Compact Single Select with Images and Autoadvance, width specified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As with :ref:`compact <compact-2>`, you can specify a width when using :tc:`quickcompact`. To display two images on each row, set the :th:`appearance` attribute to :tc:`quickcompact-2`.

.. video:: /vid/form-widgets/quickcompact2.mp4

  Video showing Compact-2 widget and auto-advance after the question is answered.

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,grid_widget_quickcompact2,Grid select one widget,quickcompact-2,"select_one type with quickcompact-2 appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _multiselect-widgets:

Multiselect Widgets
---------------------

.. _default-multi-select:

Default Multiselect Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-multiselect.*
  :alt: The default Multiselect widget as displayed in the ODK Collect app on an Android phone. The question text is, "Multiselect widget." The hint text is, "select_one widget with no appearance, 4 text choices." Below that are four checkbox options labeled A, B, C, and D. Above the question text is the form group label, "This section contains 'Select Multi Widgets'"

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint

  select_multiple opt_abcd,select_multi_widget,Multi select widget,"select_multiple type with no appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _compact-multi-widget:

Compact Multiselect with Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/compact-multiselect.*
  :alt: The compact multiselect form widget with image options, as displayed in the ODK Collect app on Android phone. The question text is "Grid select multiple widget." The hint text is select_multiple type with compact appearance, 4 image choices." Below that are four small animal icons in a single row. Above the question text is the section label "This section contains 'Select Multi Widgets.'"

.. image:: /img/form-widgets/compact-multiselect-selected.*
  :alt: The compact multiselect as shown in the previous image. Two of the small animal icons are outlined with an orange border, indicating they have been selected.

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_multiple abcd_icon,grid_multi_widget_compact,Grid select multiple widget,compact,"select_multiple type with compact appearance, 4 image choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _multi-image-compact-2:

Compact Multiselect with Image Choices, style 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/multi-image-compact-2.*
  :alt: The multiselect form widget with images and appearance of 'compact-2,' as displayed in the ODK Collect app on an Android phone. The question text is, "Grid select multiple widget." The hint text is "select_one type with compact-2 appearance, 4 image choices (a.jpg, b.jpg, c.jpg, d.jpg)." Below that are four animal icons arranged in a two-by-two grid. Above the question text is the form group label "This section contains 'Select multi Widgets.'"

.. image:: /img/form-widgets/multi-image-compact-2-selected.*
  :alt: The compact multiselect widget shown previously. Two of the animal icons are outlined with an orange border, indicating they have been selected.


XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_multiple abcd_icon,grid_multi_widget_compact2,Grid select multiple widget,compact-2,"select_multiple type with compact-2 appearance, 4 image choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg

.. _spinner-widget-multi:

Multiselect Spinner Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding the :tc:`minimal` appearance attribute places the choices into a drop-down style menu.

.. image:: /img/form-widgets/multiselect-minimal-start.*
  :alt: The Multiselect form widget, with minimal appearance, as displayed in the ODK Collect app on an Android phone. The question text is "Spinner widget: select multiple." The hint text is "select_multiple type with minimal appearance, 4 text choices." Below that is a drop-down style select menu with the prompt "Select Answer." Above the question text is the form group name "This section contains 'Select Multi Widget.'"

.. image:: /img/form-widgets/multiselect-minimal-expanded.*
  :alt: The multiselect form widget, wih minimal appearance, as displayed in the previous image. The select menu has expanded to show choices: A, B, C, D. In the lower right corner is a button labeled OK.

XLSForm Rows
""""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_multiple opt_abcd,spinner_multi_widget,Spinner widget: select multiple,minimal,"select_multiple type with minimal appearance, 4 image choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _field-list:

Field List
-------------

The :tc:`field-list` appearance attribute, applied to a group of questions, displays them all on a single screen.

.. image:: /img/form-widgets/field-list-1.*
  :alt: A field-list group of questions, as displayed in the ODK Collect app on an Android phone. Six questions are displayed. Below each, the answer choices are arranged in a row.

.. image:: /img/form-widgets/field-list-2.*
  :alt: The continuation of the previous image.

XLSForm Rows
~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  begin_group,table_list_test,List group,field-list,
  select_one yes_no,table_list_test_label,Label widget,label,"Show only the labels of these options and not the inputs (type=select_one yes_no, appearance=label)"
  select_multiple yes_no,table_list_test_label_2,Label multi widget,label,"Show only the labels of these options and not the inputs (type=select_multiple yes_no, appearance=label)"
  select_one yes_no,table_list_1,List widget,list-nolabel,"Show only the inputs of these options and not the labels (type=select_one yes_no, appearance=list-nolabel)"
  select_multiple yes_no,table_list_2,List multi widget,list-nolabel,"Show only the inputs of these options and not the labels (type=select_multiple yes_no, appearance=list-nolabel)"
  select_one yes_no,list_widget,List widget,list,"This is a normal list widget with (type = select_one, appearance = list)"
  select_multiple yes_no,list_multi_widget,List multi widget,list,"This is a normal list widget with (type = select_multiple, appearance = list)"
  end_group

.. csv-table:: choices
  :header: list_name, name, label

  yes_no,yes,Yes
  yes_no,no,No
  yes_no,dk,Don't Know
  yes_no,na,Not Applicable

.. _trigger:

Trigger Widget
---------------

"Trigger" is another name for the :ref:`acknowledge` widget. The example shown here includes the :th:`required` attribute.

.. image:: /img/form-widgets/trigger.*
  :alt: The Trigger (or "Acknowledge") form widget as displayed in the ODK Collect App on an Android phone. The question text is, "Trigger widget." The hint text is, "Prompts for confirmation. Useful to combine with required or relevant. (type=trigger)" Below that is a single checkbox labeled, "OK. Please continue." The checkbox is unchecked.

.. image:: /img/form-widgets/trigger-sorry.*
  :alt: The Trigger widget shown previously. An error text reads, "Sorry, this response is required."

.. image:: /img/form-widgets/trigger-selected.*
  :alt: The Trigger widget shown previously. The checkbox is now checked.

XLSForm Rows
~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, hint, required

  trigger,my_trigger,Trigger widget,Prompts for confirmation. Useful to combine with required or relevant. (type=trigger),true()


.. _image-options:

Including Images as Choices
=============================

To include images as choices for select questions, specify the file name in the **choices** worksheet, in a column labeled :th:`media::image`. The media files must be uploaded to the Android device in the :file:`/sdcard/odk/forms/` directory, in a folder labeled :file:`{form-name}-media`. When uploading a form to ODK Aggregate, a second upload prompt will allow you to upload your files directory.
