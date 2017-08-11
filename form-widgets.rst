***************
Form Widgets
***************

This document is a list of available ODK :term:`Collect` :term:`form` :term:`widgets <widget>` (question types), with:

- examples images from the ODK Collect app
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


XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/name" type="string"/>

  <input ref="/sample-xlsform/name">
    <label>What is your name?</label>
  </input>

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

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/fruits" type="select1"/>

  <select1 ref="/sample-xlsform/fruits">
    <label>What is your favorite fruit?</label>
    <item>
      <label>apple</label>
      <value>apple</value>
    </item>
    <item>
      <label>pear</label>
      <value>pear</value>
    </item>
    <item>
      <label>peach</label>
      <value>peach</value>
    </item>
    <item>
      <label>strawberry</label>
      <value>strawberry</value>
    </item>
    <item>
      <label>pineapple</label>
      <value>pineapple</value>
    </item>
    <item>
      <label>orange</label>
      <value>orange</value>
    </item>
    <item>
      <label>grape</label>
      <value>grape</value>
    </item>
    <item>
      <label>plum</label>
      <value>plum</value>
    </item>
  </select1>

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
- The content of **name** can not have spaces.

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/veggies" type="select"/>

  <select ref="/sample-xlsform/veggies">
    <label>Which vegetables do you enjoy?</label>
    <hint>Select all that apply.</hint>
    <item>
      <label>broccoli</label>
      <value>broccoli</value>
    </item>
    <item>
      <label>carrot</label>
      <value>carrot</value>
    </item>
    <item>
      <label>spinach</label>
      <value>spinach</value>
    </item>
    <item>
      <label>tomato</label>
      <value>tomato</value>
    </item>
    <item>
      <label>bell pepper</label>
      <value>bell_pepper</value>
    </item>
    <item>
      <label>asparagus</label>
      <value>asparagus</value>
    </item>
  </select>

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

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/age" type="int"/>

  <input ref="/sample-xlsform/age">
    <label>What is your age in years?</label>
  </input>

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

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/weight" type="decimal"/>

  <input ref="/sample-xlsform/weight">
    <label>Weight in kilograms.</label>
  </input>

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

XForm XML
~~~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/current_location" type="geopoint"/>

  <input ref="/sample-xlsform/current_location">
    <label>Current location.</label>
    <hint>You might have to turn on your GPS.</hint>
  </input>

GeoTrace
-----------

A line or polygon of GPS coordinates tracking actual device movement. The user can specify one of two location-recording modes:

- Manual Mode — The user taps the device to place a marker as desired, while moving.
- Automatic Mode — The app creates a marker on a regular time interval (default: 20 second) as the user moves.


.. image:: /img/form-widgets/geotrace-start.*
  :alt: A geotrace form widget displayed in the ODK Collect app on an Android phone. The question text is "Where have you been?" and below that is a button with the label "Start GeoTrace."

.. image:: /img/form-widgets/geotrace1.*
  :alt: A modal popup over a map. The modal headline is "Zoom to..." Below that are two options: "Zoom to current location" (selected) and "Zoom to saved feature". In the bottom-right of the modal is a Cancel button.

.. image:: /img/form-widgets/geotrace2.*
  :alt: A map displayed in the ODK Collect App on an Android phone. Above the map is the instruction: Wait for lock, then tap add marker button start. On the right side are five icon buttons stacked vertically: Add marker, Zoom, Layers, Trash, Save.

.. image:: /img/form-widgets/geotrace3.*
  :alt: The same map as displayed in the previous image. Over the map is a modal popup. The modal headine is "Select GeoTrace Mode," followed by two radio-button (single select) options: Manual Mode (selected) and Automatic Mode. In the bottom-right are buttons for Cancel and Start.

.. image:: /img/form-widgets/geotrace4.*
  :alt: The same modal popup as in the previous image, but the Automatic Mode radio button is not selected. Below it are two drop-down select boxes. Their values are "20" and "seconds."

.. image:: /img/form-widgets/geotrace5.*
  :alt: The same map as displayed previosuly, but now a series of red markers form a line across the map.

.. image:: /img/form-widgets/geotrace6.*
  :alt: The same map as previously, with a new modal popup. The headlines of the modal is "Save GeoTrace as" followed by two options: Save as Polygon and Save as Polyline. In the bottom-right is a Cancel button.

.. image:: /img/form-widgets/geotrace7.*
  :alt: The Geotrace form widget, as shown previously. The question text is "Where have you been?" and the button label is "View or Change GeoTrace." Below that is a list of lat/long GPS coordinates.


XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  geotrace, trace_example, Where have you been?

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/trace_example" type="geotrace"/>

  <input ref="/sample-xlsform/trace_example">
    <label>Where have you been?</label>
  </input>

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
  :alt: The same map as displayed previosuly, but now a series of red markers form a polygon across the map.

.. image:: /img/form-widgets/geoshape4.*
  :alt: The GeoShape form widget shown previously. The question text is "Select an Area." The button label is now "View or Change GeoShape." Below the button is a list of lat/long GPS coordinates.

XLSForm Rows
~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  geoshape, shape_example, Select an area.

XForm XML
~~~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/shape_example" type="geoshape"/>

  <input ref="/sample-xlsform/shape_example">
    <label>Select an area.</label>
  </input>

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

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/birthday" type="date"/>

  <input ref="/sample-xlsform/birthday">
    <label>What is your birthday?</label>
  </input>

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

XForm XML
~~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/wakeup" type="time"/>

  <input ref="/sample-xlsform/wakeup">
    <label>What time do you usually wakeup?</label>
  </input>

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

XForm XML
~~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/previous_meal" type="dateTime"/>

  <input ref="/sample-xlsform/previous_meal">
    <label>When was the last time you ate?</label>
  </input>

.. _image:

Image
----------

An image collector. The user can choose to select an image stored on the device, or take a new picture. The example includes :term:`hint` text.

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

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/selfie" type="binary"/>

  <upload mediatype="image/*" ref="/sample-xlsform/selfie">
    <label>Please take a self portrait.</label>
    <hint>A &quot;selfie.&quot;</hint>
  </upload>

.. _audio:

Audio
--------

An audio recording collector.

.. image:: /img/form-widgets/audio-start.*
  :alt: The Audio form widget as displayed in the ODK Collect App on an Android phone. The question text is "Please record your name." There are three buttons: Record Sound, Choose Sound, and Play Sound. The "Play Sound" button is disabled.

.. need to complete the audio widget sequence of images

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  audio, name_pronounce, Please record your name.

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/name_pronounce" type="binary"/>

  <upload mediatype="audio/*" ref="/sample-xlsform/name_pronounce">
    <label>Please record your name.</label>
  </upload>

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

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/blinking" type="binary"/>

  <upload mediatype="video/*" ref="/sample-xlsform/blinking">
    <label>Please record a video of yourself blinking.</label>
    <hint>Three times is probably sufficient.</hint>
  </upload>

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

XForm XML
~~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/note_1" readonly="true()" type="string"/>

  <input ref="/sample-xlsform/note_1">
    <label>This is an example note.</label>
    <hint>The text displays, but there is no input.</hint>
  </input>

.. _barcode:

Barcode
----------

A barcode scanner.

.. note::
  Older versions of ODK Collect required a third-party app for barcode scanning. This is no longer the case. The barcode widget is fully supported on recent ODK Collect releases used on recent Android devices.

.. image:: /img/form-widgets/barcode-start.*
  :alt: The Barcode form widget as displayed in the ODK Collect app on an Android phone. The headline text reads, "Scan any barcode." Below that is an image labeled "Get Barcode."

.. image:: /img/form-widgets/barcode1.*
  :alt: A barcode scanner on a horizontally-oriented Android device. A barcode is in the viewfinder, with a thin red line across the barcode.

.. image:: /img/form-widgets/barcode2.*
  :alt: The Barcode form widget as displayed previously. The button label is now "Replace Barcode." Below the button is a string of numbers representing the decoded content of the scanned barcode.

XSLForm Rows
~~~~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  barcode, barcode_example, Scan any barcode.

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <bind nodeset="/sample-xlsform/barcode_example" type="barcode"/>
  <input ref="/sample-xlsform/barcode_example">
    <label>Scan any barcode.</label>
  </input>

.. _acknowledge:

Acknowledge
-------------

An acknowledgement prompt with single checkbox. In :term:`Aggregate`, a completed acknowledgement is stored as the string response ``OK``.

.. image:: /img/form-widgets/acknowledge.*
  :alt: The Acknowledge form widget as displayed in the ODK Collect app on an Android phone. The headline text is, "I acknowledge this acknowledgment." Below that is a single checkbox with the label, "OK. Please continue."

XLSForm Rows
~~~~~~~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label

  acknowledge, ack_sample, I acknowledge this acknowledgement.

XForm XML
~~~~~~~~~~~~~

.. code:: xml

  <bind nodeset="/sample-xlsform/ack_sample" type="string"/>

  <trigger ref="/sample-xlsform/ack_sample">
    <label>I acknowledge this acknowledgement.</label>
  </trigger>

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

Launches an external app and recieves a string input back from the external app. If the specified external app is not available, a manual input is prompted.

The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`. The rest of the :th:`appearance` string specifies the application to launch.

.. image:: /img/form-widgets/external-app-widget-start.* 
  :alt: The External App form widget, as displayed in the ODK Collect App on an Android phone. The question text is "Ex string widget." The hinst text is, "text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labelled "Launch." Above the question text is the form group name "Text widgets."

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
  :alt: The external printer widget, as displayed in the ODK Collect app on an Android phone. The question text is "Ex printer widget." The hint text is "text type with printer:org.opendatakit.sensors.ZebraPrinter." Below that is a button labeled, "Initiate Printing." Above the question text is the form gropu name "Text widgets."

XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint

   text,ex_printer_widget,Ex printer widget,printer:org.opendatakit.sensors.ZebraPrinter,text type with printer:org.opendatakit.sensors.ZebraPrinter
