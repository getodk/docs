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

XForm XML
""""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/text_widgets/string_widget" type="string"/>
  
  <input ref="/all-widgets/text_widgets/string_widget">
     <label>String widget</label>
  </input>
  
  
  
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

XForm XML
"""""""""

.. code:: xml
  
  <bind nodeset="/all-widgets/text_widgets/string_number_widget" type="string"/>
  
  <input appearance="numbers" ref="/all-widgets/text_widgets/string_number_widget">
    <label>String number widget</label>
    <hint>text type with numbers appearance</hint>
  </input>

  
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

  
XForm XML
""""""""""

.. code:: xml

  <instance>
    <all_widgets>
      <text_widgets>
        <!-- URL is defined here. -->
        <url_widget>http://opendatakit.org/</url_widget>
      </text_widgets>
    </all_widgets>
  </instance>

  <bind nodeset="/all-widgets/text_widgets/url_widget" type="string"/>

  <input appearance="url" ref="/all-widgets/text_widgets/url_widget">
    <label>URL widget</label>
    <hint>text type with url appearance and default value of http://opendatakit.org/</hint>
  </input>

  
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

XForm XML
"""""""""""

.. code:: xml
  <bind nodeset="/all-widgets/text_widgets/ex_string_widget" type="string"/>
  
  <input appearance="ex:change.uw.android.BREATHCOUNT" ref="/all-widgets/text_widgets/ex_string_widget">
    <label>Ex string widget</label>
      <hint>text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)</hint>
  </input>
  
  
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

XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/text_widgets/ex_printer_widget" type="string"/>

  <input appearance="printer:org.opendatakit.sensors.ZebraPrinter" ref="/all-widgets/text_widgets/ex_printer_widget">
    <label>Ex printer widget</label>
    <hint>text type with printer:org.opendatakit.sensors.ZebraPrinter</hint>
  </input>

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
  
XForm XML
"""""""""""
.. code:: xml
  <bind nodeset="/all-widgets/number_widgets/integer_widget" type="int"/>

  <input ref="/all-widgets/number_widgets/integer_widget">
    <label>Integer widget</label>
    <hint>integer type with no appearance</hint>
  </input>
  
.. _external-integer-widget:

External Integer Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

Launches an external app and recieves an integer input back from the external app. If the specified external app is not available, a manual input is prompted.

.. image:: /img/form-widgets/external-integer-widget-start.* 
  :alt: The External Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Ex integer widget." The hint text is, "integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form name "Numerical widgets."
  
.. image:: /img/form-widgets/external-widget-fallback.* 
  :alt: The External Integer widget as displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, "The requested application is missing. Please manually enter the reading."
  
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint
  
  integer,ex_integer_widget,Ex integer widget,ex:change.uw.android.BREATHCOUNT,integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)
  
XForm XML
""""""""""

.. code:: xml
  
  <bind nodeset="/all-widgets/number_widgets/ex_integer_widget" type="int"/>
  
  <input appearance="ex:change.uw.android.BREATHCOUNT" ref="/all-widgets/number_widgets/ex_integer_widget">
    <label>Ex integer widget</label>
    <hint>integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)</hint>
  </input>

  
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
  
XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/number_widgets/decimal_widget" type="decimal"/>
  
  <input ref="/all-widgets/number_widgets/decimal_widget">
    <label>Decimal widget</label>
    <hint>decimal type with no appearance</hint>
  </input>
  
.. _external-decimal-widget:

External Decimal Widget
~~~~~~~~~~~~~~~~~~~~~~~~~

Launches an external app and recieves a decimal number input back from the external app. If the specified external app is not available, a manual input is prompted.

.. image:: /img/form-widgets/external-decimal-start.* 
  :alt: The External Decimal form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Ex decimal widget." The hint text is, "decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form group name "Numerical widgets."
  
.. image:: /img/form-widgets/external-decimal-fallback.* 
  :alt: The External Decimal widget displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, "The requested application is missing. Please manually enter the reading."
  
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint
  
  decimal,ex_decimal_widget,Ex decimal widget,ex:change.uw.android.BREATHCOUNT,decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)
  
XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/number_widgets/ex_decimal_widget" type="decimal"/>

  <input appearance="ex:change.uw.android.BREATHCOUNT" ref="/all-widgets/number_widgets/ex_decimal_widget">
    <label>Ex decimal widget</label>
    <hint>decimal type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)</hint>
  </input>

.. _bearing-widget:

Bearing Widget
~~~~~~~~~~~~~~~~

Captures a compass reading.

.. image:: /img/form-widgets/bearing-widget-start.* 
  :alt: The Bearing form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Beaering widget." The hint text is, "decimal type wih bearing appearance. Below that is a button labeled "Record Bearing." Above the question text is the form group name "Numericl widgets."

.. image:: /img/form-widgets/bearing-in-progress.* 
  :alt: The Bearing widget, overlaid with a model popup. The modal headline is "Loading Bearing." In the body of the modal are two fields: "Direction: W" and "Bearing: 273.001". At the bottom of the modal are Cancel and Record Bearing buttons.
  
.. image:: /img/form-widgets/bearing-finished.* 
  :alt: The Bearing widget, as displayed previously. The button's label is not "Replace bearing." Below the button is the decimal number 271.538 (the recorded bearing). 
 
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint
  
  decimal,bearing_widget,Bearing widget,bearing,decimal type with bearing appearance
  
XForm XML
"""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/number_widgets/bearing_widget" type="decimal"/>
  
  <input appearance="bearing" ref="/all-widgets/number_widgets/bearing_widget">
    <label>Bearing widget</label>
    <hint>decimal type with bearing appearance</hint>
  </input>
  
.. _image-widgets:

Image Widgets
---------------

.. _default-image-widget

Default Image Widget
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/form-widgets/default-image-widget.* 
  :alt: The default Image form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Image Widget." The hint text is, "image type with no appearance." Below that are two buttons: "Take Picture" and "Choose Image." Above the question text is the form group name "Image widgets."
  
XLSForm Rows
""""""""""""""
.. csv-table:: survey
  :header: type, name, label, hint
  
  image,image_widget,Image widget,image type with no appearance
  
XForm XML
""""""""""

.. code:: xml
  <bind nodeset="/all-widgets/image_widgets/image_widget" type="binary"/>

  <upload mediatype="image/*" ref="/all-widgets/image_widgets/image_widget">
    <label>Image widget</label>
    <hint>image type with no appearance</hint>
  </upload>

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
  
XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/image_widgets/selfie_image_widget" type="binary"/>
  
  <upload appearance="selfie" mediatype="image/*" ref="/all-widgets/image_widgets/selfie_image_widget">
    <label>Selfie widget</label>
    <hint>image type with selfie appearance</hint>
  </upload>

.. _draw-widget:

Draw Widget
~~~~~~~~~~~~~

Provides the user a drawing pad and collects the drawn image.

.. image:: /img/form-widgets/draw-widget.* 
  :alt: The Draw form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Draw widget." The hint text is "image type with draw appearance." Below that is a button labeled "Sketch Image." Above the question text is the form group name "Image widgets."
  
.. image:: /img/form-widgets/draw-in-progress.* 
  :alt: A white "drawing pad" on an Android phone, horizontally oriented (landscape mode). A simple smiley face has been drawn. In the lower right corner of the drawing pad is a plus sign (+) in a circle.
  
.. image:: /img/form-widgets/draw-options.* 
  :alt: The drawing pad as displayed in the previous image. Amenu has expanded from the lower right corner with the options: Reset, Save and Close, and Set Color.
  
.. image:: /img/form-widgets/draw-completed.* 
  :alt: The Draw widget as displayed previously. Below the "Sketch Image" button is the smiley face from the drawing pad image shown previously.

XLSForm Rows
"""""""""""""

.. csv-table:: survey

  :header: type, name, label, appearance, hint
  
  image,draw_image_widget,Draw widget ,draw,image type with draw appearance  
  
XForm XML
"""""""""""

.. code:: xml

   <bind nodeset="/all-widgets/image_widgets/draw_image_widget" type="binary"/>

   <upload appearance="draw" mediatype="image/*" ref="/all-widgets/image_widgets/draw_image_widget">
     <label>Draw widget</label>
     <hint>image type with draw appearance</hint>
   </upload>
   
.. _annotate-widget:

Annotate Widget
~~~~~~~~~~~~~~~~~~

Allows user to take or select an image and then draw on it.

.. image:: /img/form-widgets/annotate-start.* 
  :alt: The Annotate form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Annotate widget." The hint text is, "image type with anotatr appearance." There are three buttons: "Take Picture," "Choose Image," and "Markup Image." The Markup Image button is displabled. Above the question text is the form group name "Image widgets."
  
.. image:: /img/form-widgets/annotate-1.* 
  :alt: The camera view on an Android phone. In the viewer is a picture of a small saucer. Below the viewer is a blue checkmark button.
  
.. image:: /img/form-widgets/annotate-2.* 
  :alt: The Annotate form widget displayed previosuly. The Markup Image button is now enabled. Below the buttons is the picture of a saucer shown previously.
  
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

XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/image_widgets/annotate_image_widget" type="binary"/>
  
  <upload appearance="annotate" mediatype="image/*" ref="/all-widgets/image_widgets/annotate_image_widget">
    <label>Annotate widget</label>
    <hint>image type with annotate appearance</hint>
  </upload>
  
.. _signature-widget:

Signature Widget
"""""""""""""""""

Collects a signature from the user.

.. image:: /img/form-widgets/signature-start.* 
  :alt: The Signature form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Signature widget." The hint text is "image type with signature appearance." Below that is a button labelled "Gather Signature." Above the question text is the form group name "Image widgets."
  
.. image:: /img/form-widgets/signature-in-progress.* 
  :alt: A drawing pad with a signature line, displayed in an Andoird phone. A signature is drawn across it. In the lower right corner is circular button marked with a plus sign (+).

.. image:: /img/form-widgets/signature-completed.* 
  :alt: The signature widget displayed previously. Below the button is the signature drawn in the previous image.
  
XLSForm Rows
"""""""""""""

.. csv-table:: table
  :header: type, name, label, appearance, hint
  
  image,signature_widget,Signature widget,signature,image type with signature appearance
  
  
XForm XML
""""""""""""

.. code:: block

  <bind nodeset="/all-widgets/image_widgets/signature_widget" type="binary"/>
  
  <upload appearance="signature" mediatype="image/*" ref="/all-widgets/image_widgets/signature_widget">
    <label>Signature widget</label>
    <hint>image type with signature appearance</hint>
  </upload>   

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
  :alt: The default Date form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Date widget." The hint text is "date type with no appearance." Below that is a button labeled "Select date." Below that is the text, "No date selected." Above the quesiton text is the form group name "Date and time widgets."
  
.. image:: /img/form-widgets/date-calendar-view.* 
  :alt: The date widget shown in the previous image, with a modal popup showing a monthyl calendar. A date is selected. At the bottom of the modal are Cancel and OK buttons.
  
.. image:: /img/form-widgets/date-completed.* 
  :alt: The date widget shown previously. Below the button is a date: Aug 11, 2017.
  
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, hint
  
  date,date_widget,Date widget,date type with no appearance

XForm XML
"""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/date_time_widgets/date_widget" type="date"/>
  
  <input ref="/all-widgets/date_time_widgets/date_widget">
    <label>Date widget</label>
    <hint>date type with no appearance</hint>
  </input>
  
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
  
XForm XML
""""""""""

.. code:: xml
  
  <bind nodeset="/all-widgets/date_time_widgets/date_widget_nocalendar" type="date"/>
  
  <input appearance="no-calendar" ref="/all-widgets/date_time_widgets/date_widget_nocalendar">
     <label>Date Widget</label>
     <hint>date type with no-calendar appearanec</hint>
  </input>
  
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
  
XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/date_time_widgets/date_widget_month_year" type="date"/>
  
  <input appearance="month-year" ref="/all-widgets/date_time_widgets/date_widget_month_year">
    <label>Date widget</label>
    <hint>date type with month-year appearance</hint>
  </input>
  
.. _year-widget:
  
Year Widget
~~~~~~~~~~~~

Collects only a year.

.. image:: /img/form-widgets/year-spinner.* 
  :alt: The Year form widget, with a model popup labeled "Select date." There is a single "spinner" type selector for year. At the bottom are Cancel ans OK buttons.
  
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint
  
  date,date_widget_year,Date widget,year,date type with year appearance
  
XForm XML
""""""""""

.. code:: xml

  <bind nodeset="/all-widgets/date_time_widgets/date_widget_year" type="date"/>

  <input appearance="year" ref="/all-widgets/date_time_widgets/date_widget_year">
    <label>Date widget</label>
    <hint>date type with year appearance</hint>
  </input>
  
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

XForm XML
"""""""""""
    
.. code:: xml

  <bind nodeset="/all-widgets/geopoint_widgets/geopoint_widget_placementmap" type="geopoint"/>
  
  <input ref="/all-widgets/geopoint_widgets/geopoint_widget">
    <label>Geopoint widget</label>
    <hint>geopoint type with no appearance</hint>
  </input>
  
.. _placement-map-widget:

Geopoint Placement Map Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A geopoint with the appearance attribute :tc:`placement-map` allows the user to select a geopoint from a map.

.. image:: /img/form-widgets/geopoint-placement-map.* 
  :alt: A map app open on an Android phone. Above the map is the message: "Long press to place mark or tap add marker button." Along the right side of the map are buttons: Add Marker, Zoom to point, Layers, Trash, Save.
 
XLSForm Rows
"""""""""""""

.. csv-table:: survey
  :header: type, name, label, appearance, hint
  
  geopoint,geopoint_widget_placementmap,Geopoint widget,placement-map,geopoint type with placement-map appearance
  
XForm XML
"""""""""""
  
.. code:: xml

  <bind nodeset="/all-widgets/geopoint_widgets/geopoint_widget_placementmap" type="geopoint"/>
      
  <input appearance="placement-map" ref="/all-widgets/geopoint_widgets/geopoint_widget_placementmap">
    <label>Geopoint widget</label>
    <hint>geopoint type with placement-map appearance</hint>
  </input>
  
  
 
