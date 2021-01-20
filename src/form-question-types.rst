.. spelling::

  abcd
  ack
  br
  BREATHCOUNT
  Codabar
  Comcond
  concat
  Datetime
  dateTime
  deviceid
  dk
  na
  nocalendar
  nolabel
  partum
  phonenumber
  placementmap
  podcast
  preg
  rect
  substr
  uw
  ZXing


Question Types
=================

:doc:`collect-intro` supports forms with a wide variety of question types.
The exact functionality and display style of each question
are specified in your `XLSForm`_ definition using the
:th:`type` and :th:`appearance` columns.

.. _XLSForm: http://xlsform.org

.. contents:: :depth: 1
  :local:

.. tip::

  You can find an XLSForm with all available question types `here <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0>`_.

  For simpler forms you can use :doc:`build-intro`, which provides a visual, drag-and-drop interface.

.. admonition:: Helpful terminology

  .. glossary::

    question

      A prompt to the user, usually requesting a response.
      Questions are written as a single line in an XLSForm,
      and usually appear on a single screen in Collect.

    widget

      A rendered question screen in Collect.
      The :th:`type` and :th:`appearance` of a question
      determine the widget that is displayed.


.. _text-widget:

Text widgets
--------------

All of the text widgets share the :tc:`text` type,
and the inputs from them are saved as literal strings.

.. warning::

  If you are using Aggregate and expect answers to be more than 255 characters, you should :doc:`increase the database field length to over 255 characters <aggregate-field-length>`.

.. contents::
 :local:

.. _text-default:

Default text widget
~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`text`
appearance
  *none*

A simple text input.

The text entry field expands as the user types, and line breaks can be included. The keyboard displayed depends on the Android device and user settings.

.. image:: /img/form-widgets/string-input.*
  :alt: Text form widget, displayed in ODK Collect on an Android phone. The label is "What is your name?"
  :class: device-screen-vertical

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance

  text, name, What is your name?,

.. _number-text-widget:

Number text widget
~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`text`
appearance
  :tc:`numbers`


A numerical input that treats the input as a string, rather than a number.

The number input accepts numerals (``0123456789``), hyphens (``-``), and decimal points (``.``). These are the only characters available on the number keypad displayed with this widget.

This is useful for phone numbers, ID numbers, IP addresses, and similar data. It can also be used in place of the :ref:`default-integer-widget` or :ref:`default-decimal-widget` if large numbers are needed. (The integer widget has a limit of nine digits, and the decimal widget has a limit of 15 characters.)

.. image:: /img/form-widgets/string-number.*
  :alt: The text widget, with numerical entry, as displayed in the ODK Collect app on an Android phone. The question text is "String number widget." The hint text is, "text type with numbers appearance." Below that is a simple input. Above the question text is the form group name "Text Widget." The Android onscreen keyboard displays a number pad.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  text,string_number_widget,String number widget,numbers,text type with numbers appearance

.. note::

  This appearance can be combined with the :ref:`thousands-sep <thousands-sep>` appearance.


.. _external-app-widget:

External app widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`text`
appearance
  :tc:`ex.*`

Launches an external app and receives a string input back from the external app. If the specified external app is not available, a manual input is prompted.

The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`. The rest of the :th:`appearance` string specifies the application to launch.

.. seealso:: :doc:`launch-apps-from-collect`

.. image:: /img/form-widgets/external-app-widget-start.*
  :alt: The External App form widget, as displayed in the ODK Collect App on an Android phone. The question text is "Ex string widget." The hint text is, "text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form group name "Text widgets."

.. image:: /img/form-widgets/external-app-widget-fallback.*
  :alt: The External App widget as displayed earlier. The Launch button has now been disabled. Below it is a simple input. A help message displays the text, "The requested application is missing. Please manually enter the reading."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  text,ex_string_widget,Ex string widget,ex:change.uw.android.BREATHCOUNT,text type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)


.. _number-widgets:

Number widgets
---------------------

Number widgets collect and store number inputs ---
either :ref:`integers <default-integer-widget>` or
:ref:`floating-point decimals <default-decimal-widget>`.

Number values can also be captured by the :ref:`range-widgets`.

.. contents::
  :local:

.. _default-integer-widget:

Integer widget
~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`integer`
appearance
  *none*


A whole number entry input.

Integer widgets will not accept decimal points,
and the entry field has a limit of nine digits.
If you need numbers larger than nine digits,
see the :ref:`number-text-widget`.


The integer widget supports:

- :ref:`Thousands separators <thousands-sep>`
- :ref:`External apps <external-number-widget>`

.. image:: /img/form-widgets/integer.*
  :alt: An integer form widget displayed in ODK Collect on an Android phone. The question is "What is your age in years?" A numerical keyboard is displayed.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  integer, age, What is your age in years?

.. _default-decimal-widget:

Decimal widget
~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`decimal`
appearance
  *none*

A numeric input that will accept decimal points.

Decimal number entry is capped at 15 characters
(14 digits and a decimal point).
If you need numbers larger than 15 digits,
see the :ref:`number-text-widget`.

The decimal widget supports:

- :ref:`Thousands separators <thousands-sep>`
- :ref:`External apps <external-number-widget>`


.. image:: /img/form-widgets/decimal.*
  :alt: An integer form widget displayed in ODK Collect on an Android phone. The question is "Weight in kilograms." A numerical keyboard is displayed.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  decimal, weight, Weight in kilograms.

.. _numeric-appearance-attributes:

Number widget appearance options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _thousands-sep:

Thousands separator
""""""""""""""""""""

type
  :tc:`integer`, :tc:`decimal`, (:tc:`text`)
appearance
  :tc:`thousands-sep`, (:tc:`numbers`)


If :tc:`thousands-sep` is added to :th:`appearance`,
:ref:`integer <default-integer-widget>`,
:ref:`decimal <default-decimal-widget>`,
and :ref:`number text <number-text-widget>` widgets
will display their values using locale-specific thousands separators.

.. note::

  For locales that use the point separator (``.``),
  a space is used instead.

.. figure:: /img/form-widgets/integer-thousands-sep-widget.*
  :alt: An integer widget as displayed in the Collect app. The question text is "Integer widget with thousands separators". The answer value is "1,000,000". The number keyboard is active.

  The comma separator, used in English/U.S. (and others).

.. figure:: /img/form-widgets/integer-thousands-sep-widget-spaces.*
  :alt: The same image as previously, but the answer value is "1 000 000". (That is, it uses spaces instead of commas as thousand separators.

  The space separator, used in *Français*/France (and others).


.. _external-number-widget:

Number from an external app
""""""""""""""""""""""""""""

type
  :tc:`integer`, :tc:`decimal`
appearance
  :tc:`ex:*`

By specifying an external app in the :th:`appearance`,
your form can launches an external app and receive a number
(integer or decimal)
from the external app as input.
If the specified external app is not available,
a manual input is prompted.

.. image:: /img/form-widgets/external-integer-widget-start.*
  :alt: The External Integer form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Ex integer widget." The hint text is, "integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)." Below that is a button labeled "Launch." Above the question text is the form name "Numerical widgets."

.. image:: /img/form-widgets/external-widget-fallback.*
  :alt: The External Integer widget as displayed previously. The Launch button is now disabled and below it is a simple input. A help text reads, "The requested application is missing. Please manually enter the reading."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  integer,ex_integer_widget,Ex integer widget,ex:change.uw.android.BREATHCOUNT,integer type with ex:change.uw.android.BREATHCOUNT appearance (can use other external apps)

.. seealso:: :doc:`launch-apps-from-collect`


.. _date-and-time-widgets:

Date and time widgets
----------------------

.. contents::
  :local:

.. _default-date-widget:

Default date widget
~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`date`
appearance
  *none*

.. image:: /img/form-widgets/default-date-widget.*
  :alt: The default Date form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Date widget." The hint text is "date type with no appearance." Below that is a button labeled "Select date." Below that is the text, "No date selected." Above the question text is the form group name "Date and time widgets."

.. image:: /img/form-widgets/date-calendar-view.*
  :alt: The date widget shown in the previous image, with a modal popup showing a monthly calendar. A date is selected. At the bottom of the modal are Cancel and OK buttons.

.. image:: /img/form-widgets/date-completed.*
  :alt: The date widget shown previously. Below the button is a date: Aug 11, 2017.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  date,date_widget,Date widget,date type with no appearance

.. _date-no-calendar:

Date widget with spinner input
"""""""""""""""""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`no-calendar`

The :tc:`no-calendar` appearance displays a spinner-style date selection. This is especially appropriate for selecting dates more than one year in the past or future.

.. image:: /img/form-widgets/date-no-calendar-start.*
  :alt: The no-calendar Date form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Date Widget." The hint text is "date type with no-calendar appearance." Below that is a button labeled "Select date." Below the button is the text, "No date selected." Above the question text is the form group name "Date and time widgets."

.. image:: /img/form-widgets/date-no-calendar-in-progress.*
  :alt: The date widget shown previously, with a pop modal. The headline of the modal is "Select date." There are individual "spinner" style selectors for month, day, and year. At the bottom of the modal are OK and Cancel buttons.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_nocalendar,Date Widget,no-calendar,date type with no-calendar appearance

.. _date-type-month-year:

Month and year only
""""""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`month-year`

Collects only a month and year.

.. image:: /img/form-widgets/month-year-spinner.*
  :alt: The date widget, with a modal popup labeled "Select date." There are individual "Spinner" type selectors for month and year, but not for date. At the bottom are Cancel and OK buttons.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_month_year,Date widget,month-year,date type with month-year appearance


.. _year-widget:

Year only
""""""""""""

type
  :tc:`date`
appearance
  :tc:`year`

Collects only a year.

.. image:: /img/form-widgets/year-spinner.*
  :alt: The Year form widget, with a model popup labeled "Select date." There is a single "spinner" type selector for year. At the bottom are Cancel and OK buttons.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  date,date_widget_year,Date widget,year,date type with year appearance

.. _non-gregorian-date-widgets:

Date widgets with non-Gregorian calendars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect supports several non-Gregorian calendars.

.. contents::
  :local:

.. note::

  The non-Gregorian calendar is used only on input.
  The dates are converted and stored as standard Gregorian dates

.. _coptic-calendar:

Coptic calendar
"""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`coptic`

.. image:: /img/form-widgets/coptic-calendar-widget.*
  :alt:

.. _ethiopian-calendar:

Ethiopian calendar
""""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`ethiopian`

.. image:: /img/form-widgets/ethiopian-calendar-widget.*
  :alt:

.. _islamic-calendar:

Islamic calendar
""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`islamic`

.. image:: /img/form-widgets/islamic-calendar-widget.*
  :alt:

.. _bikram-sambat-calendar:

Bikram Sambat calendar
""""""""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`bikram-sambat`

.. image:: /img/form-widgets/bikram-sambat-calendar-widget.*
  :alt:

Myanmar calendar
""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`myanmar`

.. image:: /img/form-widgets/myanmar-calendar-widget.*
  :alt:

Persian calendar
""""""""""""""""""

type
  :tc:`date`
appearance
  :tc:`persian`

.. image:: /img/form-widgets/persian-calendar-widget.*
  :alt:

.. _time-widget:

Time widget
~~~~~~~~~~~~~~~~~

type
  :tc:`time`
appearance
  *none*

A time selector. Captures only a specific time-of-day, not a date and time. For date and time, see the :ref:`datetime-widget`.

The time widget does not accept any :th:`appearance` attributes.

.. note::
  :name: time-zone-note


  The time widget stores the time along with a time zone.
  This can cause unexpected behavior around `Daylight saving time`_.

  .. _Daylight saving time: https://en.wikipedia.org/wiki/Daylight_saving_time

  For example, if you record a time before the clock change,
  and then view the time after the clock change,
  it will appear to be an hour off.
  This happens because the recorded time data
  is understood as a specific moment in time
  that is being "translated" into your current, local time zone.

  A similar problem occurs when moving between geographic time zones.

  This makes the time widget unsuitable for abstract
  time-of-day questions such as *What time do you usually wake up?*
  For questions like this, you may want to use a :ref:`select-minimal`.
  You can set the options at whatever level of accuracy you need ---
  for example, 15 or 30 minute increments.
  Alternatively, you could use the select widget for hours,
  and an :ref:`default-integer-widget` for minutes.

.. image:: /img/form-widgets/time-start.*
  :alt: The Time form widget as displayed in the ODK Collect App on an Android phone. The question text is "What time do you usually wake up?" The button label is "Select time." Below the button is the message "No time selected."

.. image:: /img/form-widgets/time1.*
  :alt: The Time widget as displayed previously, with a modal popup. The modal headline is "Select time." The body of the modal contains scrollers for Hour, Minute, and AM/PM. At the bottom of the modal are Cancel and OK buttons.

.. image:: /img/form-widgets/time2.*
  :alt: The Time form widget as displayed previously. Below the "Select time" button is "06:30".

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  time, wakeup, What time do you usually wakeup?

.. _datetime-widget:

Datetime widget
~~~~~~~~~~~~~~~~~~~

A date and time selector.

For date only, see :ref:`default-date-widget`. For time only, see :ref:`time-widget`.

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

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  dateTime, previous_meal, When was the last time you ate?

.. note::

  The :ref:`datetime-widget` supports the :ref:`no-calendar <date-no-calendar>` spinner-style appearance.



.. _select-widgets:

Select widgets
-----------------

Select widgets offer the :term:`participant` options to pick from.
You can offer the participant
a :ref:`single choice <single-select-widget>`,
or the ability to :ref:`choose multiple answers <multi-select-widget>`. The order of the choices can be :ref:`randomized <randomize-choice-order>` for any of the select types described below. The list of choices available can also be :ref:`cascading-selects <filtered>` based on answers to previous quesitons.

The options for a select question are listed
on a sheet named **choices**, in your XLSForm file.
The **choices** sheet has at least three columns:

:th:`list_name`
  A set of choices for a single question share a common :th:`list_name`.
  The value of :th:`list_name` is included in the :th:`type` column
  on the **survey** sheet.

:th:`name`
  The canonical identifier for a specific choice. This value is what is stored on the completed form. If you :ref:`refer to a select response using a variable <variables>`, the :th:`name` string is returned.

  As with the **survey** sheet, :th:`name` must not include spaces.

:th:`label`
  The user-facing text displayed for the choice.

Select widgets can :ref:`include images as choices <select-columns-widget>`.

.. contents::
  :local:

.. _single-select-widget:

Single select widget
~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`select_one {list_name}`

.. image:: /img/form-widgets/default-single-select.*
  :alt: The default Single Select form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Select one widget." The hint text is "select_one type with no appearance, 4 text choices." Below that is a set of radio button selectors labeled A, B, C, and D. Above the question text is form group name "Select one widgets."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  select_one opt_abcd,select_one_widget,Select one widget,"select_one type with no appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _select-minimal:

Minimal select widget
"""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`minimal`

Adding the :tc:`minimal` appearance shows the choices in a compact way. This is particularly helpful when the list of choices is long and the select question is displayed on :ref:`the same screen as other questions <field-list>`. It is often combined with :ref:`the autocomplete appearance <select-autocomplete>`.

.. image:: /img/form-widgets/select-one-minimal-start.*
  :alt: The Single Select form widget, with minimal appearance, as displayed in the ODK Collect app on an Android phone. The question text is "Select widget." The hint text is "select_one type with minimal appearance, 4 text choices." Below that is a drop-down style select menu with the prompt "Select One Answer." Above the question text is the form group name "Select one widgets."

.. image:: /img/form-widgets/select-one-minimal-expanded.*
  :alt: The Single Select form widget, with minimal appearance, as displayed in the previously image. The select menu has expanded to show choices: A, B, C, D.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_widget,Select widget,minimal,"select_one type with minimal appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

.. _autoadvance:

Select widget with autoadvance
""""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`quick`

When the :tc:`quick` appearance is added,
the form advances immediately to the next question
once a selection is made.

.. video:: /vid/form-widgets/auto-advance.mp4

  Video showing auto-advance after the questions are answered.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_one_autoadvance_widget,Select one autoadvance widget,quick,"select_one type with quick appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

.. _select-autocomplete:

Select widget with autocomplete
""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`autocomplete`

The :tc:`autocomplete` appearance allows the enumerator to filter the list of available choices. This is especially helpful for questions with a large number of choices.

.. image:: /img/form-widgets/select-autocomplete.*
  :alt: The Select One form widget with autocomplete, as displayed in the ODK Collect app on an Android phone. The question text is "Select one widget." The hint text is, "select one type with autocomplete appearance, 4 text choices." Below that is a text input followed by four radio buttons labeled A, B, C, and D. Above the question text is the form group name "Select one widgets." The device keyboard is active.

.. image:: /img/form-widgets/select-autocomplete-filtered.*
  :alt: The Select One form widget as displayed previously. The text input contains a lowercase 'b'. There is a single radio button: B. The other three radio buttons are no longer displayed.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_one_autocomplete_widget,Select one widget,autocomplete,"select_one type with autocomplete appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _select-columns-pack-widget:

Select widget with columns-pack appearance
""""""""""""""""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  *columns-pack*

When the :tc:`columns-pack` appearance is added, the app tries to accommodate as many choices in a single line as possible. If the choice labels have different lengths, they will not be in even columns.

.. image:: /img/form-widgets/select-columns-pack.*

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one opt_abcd,select_widget,Select one widget,columns-pack,"select_one type with columns-pack appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _select-columns-widget:

Select widget with columns appearance
"""""""""""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`columns`

When the :tc:`columns` appearance is added, the app puts choices in 2, 3, 4 or 5 columns depending on the screen size.

Select widgets support image choices.
The images are referenced in the **choices** sheet,
and the image files
need to be included in the :file:`media` folder.

See :ref:`image-options` to learn more about including images in surveys.

.. image:: /img/form-widgets/select-columns.*

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,select_widget,Select one widget,columns,"select_one type with columns appearance, 4 text + image choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _select-columns-n-widget:

Select widget with columns-n appearance
"""""""""""""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`columns-n`

When the :tc:`columns-n` appearance is added, the app puts choices in n columns.

.. image:: /img/form-widgets/select-columns-n.*

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,select_widget,Select one widget,columns-2,"select_one type with columns-2 appearance, 4 text + image choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _select-no-buttons-widget:

Select widget with no-buttons appearance
""""""""""""""""""""""""""""""""""""""""""""

type
  :tc:`select_one {list_name}`
appearance
  :tc:`no-buttons`

When the :tc:`no-buttons` appearance is added, the app displays choices without the selection radio button. If images are specified for choices, only the images are displayed. This is particularly useful for building a grid of images.

.. image:: /img/form-widgets/select-no-buttons.*

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  select_one abcd_icon,select_widget,Select one widget,columns-pack no-buttons,"select_one type with columns-pack no-buttons appearance, 4 image choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  abcd_icon,a,A,a.jpg
  abcd_icon,b,B,b.jpg
  abcd_icon,c,C,c.jpg
  abcd_icon,d,D,d.jpg


.. _likert-widget:

Likert widget
""""""""""""""""""""""""""""""""""
.. versionadded:: 1.25

  `ODK Collect v1.25.0 <https://github.com/getodk/collect/releases/tag/v1.25.0>`_

type
 :tc:`select_one {list_name}`
appearance
 :tc:`likert`

A single-select question can be styled as a `Likert scale <https://en.wikipedia.org/wiki/Likert_scale>`_. Options can include text, images or both. If both are provided, images appear above text.

If adding images, note that the images are referenced in the choices sheet, and the image files need to be included in the media folder. See :ref:`image-options` to learn more about including images in choices.

.. image:: /img/form-widgets/likert_widget.*
 :alt: The Single Select form likert widget with images, as displayed in the ODK Collect app on an Android phone. The question text is, "Likert Image Widget." The hint text is, "Likert type widget with images (happy case)" Below that is a set of radio buttons labeled Strongly Disagree, Disagree, Neutral, Agree, and Strongly Agree. Below each radio button is a small icon of a face: Strongly Disagree - angry, Disagree - sad, Neutral - neutral, Agree - happy, Strongly Agree - very happy. Above the question text is the form group name "All widgets likert."

.. rubric:: XLSForm

.. csv-table:: survey
 :header: type, name, label, appearance, hint

 select_one likert,likert_widget,Likert Widget,likert,"select_one type with Likert appearance, 5 image choices (strongly_disagree.jpg, disagree.jpg, neutral.jpg, agree.jpg, strongly_agree.jpg)"

.. csv-table:: choices
 :header: list_name, name, label, media::image

 likert_widget,strongly_disagree,Strongly Disagree,strongly_disagree.jpg
 likert_widget,disagree,Disagree,disagree.jpg
 likert_widget,neutral,Neutral,neutral.jpg
 likert_widget,agree,Agree,agree.jpg
 likert_widget,strongly_agree,Strongly Agree,strongly_agree.jpg


.. _multi-select-widget:

Multi select widget
~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`select_multiple {list_name}`
appearance
  *none*

Multi select questions support multiple answers.

.. note::

  The multi select widget supports
  all of the same :th:`appearance` attributes
  as the :ref:`single-select-widget` excluding the :ref:`quick <autoadvance>` appearance:

.. image:: /img/form-widgets/default-multiselect.*
  :alt: The default multi select widget as displayed in the ODK Collect app on an Android phone. The question text is, "Multi select widget." The hint text is, "select_multiple widget with no appearance, 4 text choices." Below that are four checkbox options labeled A, B, C, and D. Above the question text is the form group label, "This section contains 'Select Multi Widgets'"

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  select_multiple opt_abcd,select_multi_widget,Multi select widget,"select_multiple type with no appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label, media::image

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

.. warning::

  If you are using Aggregate and expect users to select many options, you may need to :doc:`increase the database field length to over 255 characters <aggregate-field-length>`.


.. _image-map-select:

Image map select widget
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 1.13

type
  :tc:`select_one {list_name}`, :tc:`select_multiple {list-name}`
appearance
  :tc:`image-map`

The image map widget displays an `SVG`_ image with selectable regions.

.. _SVG: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics

To make an image with selectable regions:

#. Create or edit an :file:`.svg` source file. Include ``id`` attributes on any elements you want to be selectable.
#. In the **choices** tab of your XLSForm, put the value of the ``id`` attributes in the :th:`name` column. Add an appropriate human-friendly :th:`label` to each choice.
#. In the **survey** tab of your XLSForm, put the :file:`.svg` file name in the :th:`image` column.
#. Include the :file:`.svg` file :ref:`in your form's media folder <loading-form-media>`.

.. seealso::

  `Inkscape`_
    An open source vector graphics editor.

  `SVG Documentation`_
    From Mozilla Developer Network.

  `Free SVG Files`_
    From Wikimedia Commons.

  .. _Inkscape: https://inkscape.org
  .. _SVG Documentation: https://developer.mozilla.org/en-US/docs/Web/SVG
  .. _Free SVG Files: https://commons.wikimedia.org/wiki/Category:SVG_files

.. image:: /img/form-widgets/image-map-choose-shape-0.*
  :alt:

.. image:: /img/form-widgets/image-map-choose-shape-1.*
  :alt:

.. image:: /img/form-widgets/image-map-choose-shapes-0.*
  :alt:

.. image:: /img/form-widgets/image-map-choose-shapes-1.*
  :alt:

.. rubric:: SVG

.. code-block:: xml

  <svg width="640" height="480" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
    <title>shapes</title>
    <g>
      <title>Layer 1</title>
      <path id="path" fill="#000080" stroke="#000000" stroke-width="5" d="m125,382c33,56 -193,97 48,55c241,-42 279,-15 241,-62c-38,-47 -13,-42 -106,-40c-93,2 -183,47 -183,47z"/>
      <rect id="rect" fill="#FF0000" stroke="#000000" stroke-width="5" x="52" y="53" width="176" height="149"/>
      <ellipse id="ellipse" fill="#41A317" stroke="#000000" stroke-width="5" cx="423" cy="143" rx="107" ry="78"/>
    </g>
  </svg>

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, image

  select_one shapes, choose-shape, Choose a shape, image-map, shapes.svg
  select_multiple shapes, choose-shapes, Choose multiple shapes, image-map, shapes.svg

.. csv-table:: choices
  :header: list_name, name, label

  shapes, path, blob
  shapes, rect, rectangle
  shapes, ellipse, ellipse


.. _image-options:

Including media files in choices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As with questions themselves, choices can include :ref:`media <media>` (image, video, or audio files):

.. csv-table:: choices
  :header: list_name, name, label, media::image, media::video, media::audio

  opt_media,a,A,a.jpg
  opt_media,b,B,,b.mp4
  opt_media,c,C,,,c.mp3

.. note::

  ``select_one`` and ``select_multiple`` questions using the ``compact`` appearances will not
  display media buttons next to choices. However, if a choice has audio, it will be played when
  the choice is selected.

.. _randomize-choice-order:

Randomizing choice order
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

  Randomizing choice order support was added in Collect v1.18.2 and Aggregate v1.7.1. Form conversion requires XLSForm Online ≥ v1.2.2, XLSForm Offline ≥ v1.7.1, or pyxform ≥ v0.11.6.

To reduce bias, choice order can be randomized for any of the select question types described above. To display the choices in a different order each time the question is displayed, set **randomize** to **true** in the :th:`parameters` column of the XLSForm **survey** sheet:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, parameters, name, label

  select_one opt_abcd,randomize=true,select_one_random_widget,"Select one with random choice order set on each display"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

In the example above, each time the question is displayed, the choices will be in a different order. It is often preferable to pick one order that the choices will always be displayed in for a given filled form. This can be accomplished by setting an integer seed for the randomization.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, parameters, name, label, calculation

  calculate,,my_seed,,"once(substr(decimal-date-time(now()), 10))"
  select_one opt_abcd,"randomize=true,seed=${my_seed}",select_one_widget,Select one with random choice order set once per filled form

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D

This seed can also be used to recreate the order choices were displayed in. See `the XForms spec <https://getodk.github.io/xforms-spec/#fn:randomize>`_ for a description of the randomization algorithm used.

.. note::

  In the example above, the integer seed is created from the last 8 numbers of the :func:`decimal-date-time()` which is unlikely to repeat across devices. In the seed expression, :func:`once` is important because it makes sure the seed is not changed if the same filled form is opened more than once.

.. _or-other:

Including "other" as a choice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the **survey** sheet, in the :th:`type` column,
after the type and the list_name,
you can add :tc:`or_other`.
This will add "Other" as an additional option to your choice list.
The :th:`name` value of the choice when selected will be :tc:`other`.


.. _rank-widget:

Rank widget
-----------------

The rank widget allows the user to order options from a list. The value saved in the form and sent to the server is a space-separated ordered list of the options.

Like with :ref:`select-widgets`, the options are listed on a sheet named **choices** in an XLSForm.

To change the order of the options in the list, tap the :guilabel:`Rank items` button. In the resulting dialog, long press on an item and once it gets a border around it, drag it up or down to change the order. If no :ref:`default <default-responses>` is provided, the value for the question is blank until the user taps :guilabel:`OK` in the ranking dialog.

type
  :tc:`rank {list_name}`

.. image:: /img/form-widgets/rank-blank.*
  :alt: The rank widget, as displayed in the ODK Collect app on an Android phone. The question text is "Rank widget." The hint text is "rank type with no appearance, 4 text choices. Long press on a choice and drag it to change its position." Below that is a button with label "Rank items."

.. image:: /img/form-widgets/rank-drag.*
  :alt: The rank widget, as displayed in the ODK Collect app on an Android phone. The question text is "Rank widget." The hint text is "rank type with no appearance, 4 text choices. Long press on a choice and drag it to change its position." A dialog is open showing the options to rank. The B option has a border around it and is being moved into position 4.

.. image:: /img/form-widgets/rank-ordered.*
 :alt: The rank widget, as displayed in the ODK Collect app on an Android phone. The question text is "Rank widget." The hint text is "rank type with no appearance, 4 text choices. Long press on a choice and drag it to change its position." Below that is a button with label "Rank items." Below the button is the current order of the options.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  rank opt_abcd,rank_widget,Rank widget,"rank type with no appearance, 4 text choices"

.. csv-table:: choices
  :header: list_name, name, label

  opt_abcd,a,A
  opt_abcd,b,B
  opt_abcd,c,C
  opt_abcd,d,D


.. _location-widgets:

Location widgets
------------------

Location widgets capture one or more points representing locations on Earth. Each point is represented as four numbers separated by spaces: latitude, longitude, altitude in meters, and accuracy radius in meters.

For example, if a Collect user captured a point while at the coordinates 12°22'17.0"N 1°31'10.9"W, with a reported accuracy radius of 17.4 meters, and at 305 meters above sea level, the geopoint representation would be:

`12.371400 -1.519700 305 17.4`

Multiple points that form lines or shapes are separated by semicolons.

.. note::

  The accuracy radius is an estimate of what Android calls the `radius of 68% confidence <https://developer.android.com/reference/android/location/Location.html#getAccuracy()>`_: there is a 68% chance that the true location falls within this radius. This is an estimate reported by the Android system based on the available sensors (GPS, network, etc). The accuracy radius itself may be more or less reliable depending on the sensor(s) used and current conditions. Learn more about getting more accurate locations :doc:`here <collect-location>`.

.. contents::
  :local:

.. _geopoint-widget:

Geopoint widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`geopoint`
appearance
  *none*

Captures the current geolocation from the device.

For a geopoint with a user-selected location,
see :ref:`placement-map-widget`

.. tip::

  .. versionadded:: 1.15

  While determining the current coordinates,
  you will see a dialog box displaying:

  - Number of satellites found
  - Elapsed time

  To get an accurate fix on your location,
  the device must find at least four (4) satellites.
  If the device can not find at least four satellites,
  make sure there is nothing obstructing the device's view of the sky.

  If you have problems with the geopoint widget,
  be sure to note the elapsed time
  and accuracy (if applicable),
  so that you can share it with your support staff
  or with the |forum|_.

.. image:: /img/form-widgets/default-geopoint.*
  :alt: The default Geopoint form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Geopoint widget." The hint text is "geopoint type with no appearance." Below that is a button labeled "Start Geopoint." Below the button are completed fields for Latitude, Longitude, Altitude, and Accuracy.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  geopoint,geopoint_widget,Geopoint widget,geopoint type with no appearance


.. _geopoint-maps:

Geopoint with map display
"""""""""""""""""""""""""""""

type
  :tc:`geopoint`
appearance
  :tc:`maps`

The default :ref:`geopoint-widget` does not display a map to the user. When the appearance attribute is :tc:`maps`, the widget displays a map to help the user get oriented and confirm that the selected point is correct and sufficiently accurate.

When the device's geolocation is available, it is displayed on the map by a blue cross. A blue shaded circle around the cross represents the accuracy radius of the geolocation. The "add marker" button at the top right of the screen can be tapped to add a point at the location indicated by the middle of the blue cross. The selected point is represented by a small circle with a red outline.

When the map view is opened again with a selected point, the map is centered on that point. To change the selection, first tap the "trash" icon and then select a new point.

For a geopoint with a location that the user can manually select or adjust, see :ref:`placement-map-widget`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  geopoint,geopoint_widget_maps,Geopoint widget,maps,geopoint type with maps appearance

.. _placement-map-widget:

Geopoint with user-selected location
""""""""""""""""""""""""""""""""""""""

type
  :tc:`geopoint`
appearance
  :tc:`placement-map`

The default :ref:`geopoint-widget` does not allow the user to place the point anywhere other than the device's current geolocation.

A geopoint with the appearance attribute :tc:`placement-map` allows the user to select any point from a map. The user can either long press to place the point anywhere, or, if the device knows its geolocation, tap on the "add point" button at the top right of the screen. The selected point is represented by a small circle with a red outline (see arrow in screenshot).

The save button saves the selected point and returns to the question screen. If the point was selected by long pressing, the accuracy radius and altitude will both be 0. If the device's geolocation was selected, the accuracy radius will be greater than 0.

When the map view is opened again with an existing point, the map is centered on the selected point. To change the selection, first tap the "trash" icon and then select a new point.

.. image:: /img/form-widgets/geopoint-placement-map.*
  :alt: A map opens on an Android phone. Above the map is the message: "Long press to place mark or tap add marker button." Along the right side of the map are buttons: Add point, Delete point, Zoom to geolocation, Layers, Trash, Save. A small circle with red outline identifies the selected location. An arrow points to that point.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  geopoint,geopoint_widget_placementmap,Geopoint widget,placement-map,geopoint type with placement-map appearance

.. _geotrace-widget:

Geotrace widget
~~~~~~~~~~~~~~~~~

type
  :tc:`geotrace`
appearance
  *none*

A series of points. Identical to :ref:`geoshape <geoshape-widget>` except that the first and last point may be different and at least 2 points are required.

Points can be entered either by tapping the screen to place each point, or by taking readings of the device's geolocation over time. On a map, each coordinate is represented by small circles with red outlines. These are connected by red lines.

To collect a geotrace, first select the location-recording mode by tapping the "add point" button in the upper right side of the screen. The selected mode will be displayed in the gray bar at the bottom of the screen. While point collection is ongoing, the "add marker" button changes to a "pause" button. The "back arrow" button can be used to remove the last-entered point either when actively collecting points or when paused. Any point can be manually moved at any time by tapping on it and dragging it. The mode can only be changed if an existing line is first cleared by tapping the "trash" button. Recording must be paused to clear the existing line.

.. tip::
  Points that were entered by tapping or adjusted by dragging will always have an accuracy radius of 0. Points that were read from the device location will never have an accuracy radius of 0.

Once the trace has been saved, the coordinates of its points will be displayed on the question screen. The trace can be opened for manual editing by tapping to add more points, moving existing points or deleting the last-added point. After a trace has been saved once, it cannot be added to in manual or automatic location recording modes.

The three location recording modes are:

Placement by tapping
  The user taps the device to place points.

Manual location recording
  The user chooses when to tap the "record a point" button at the top of the screen to capture the device geolocation at that moment.

Automatic location recording
  The user is prompted to select a recording interval and accuracy requirement. If the accuracy requirement is set to None, points are always collected at the recording interval. If the accuracy requirement is set to any other value, a point will only be captured if it meets the requirement. For example, given a recording interval of 20s and an accuracy requirement of 10m, the app places a point at the device location every 20s if the location is accurate to 10m or better.

.. warning::

  If you are using Aggregate and you would like to collect more than 5 points at a time, you should :doc:`increase the database field length to over 255 characters <aggregate-field-length>`. Otherwise, additional points will be lost.

.. image:: /img/form-widgets/geotrace-question.*
  :alt: A geotrace form widget displayed in the ODK Collect app on an Android phone. The question text is "Where have you been?" and below that is a button with the label "Start GeoTrace."

.. image:: /img/form-widgets/geotrace-collected.*
  :alt: A map displayed in the ODK Collect App on an Android phone. Above the map is a green bar showing current location accuracy radius. On the right side are six icon buttons stacked vertically: Add point, Delete point, Zoom to geolocation, Layers, Trash, Save. A series of markers form a line across the map.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  geotrace, trace_example, Where have you been?

.. _geoshape-widget:

Geoshape
~~~~~~~~~

type
  :tc:`geoshape`
appearance
  *none*

A series of points that form a closed polygon. Identical to :ref:`geotrace <geotrace-widget>` except that the first and last point are always the same and at least 3 points are required.

Points can be entered either by tapping the screen to place each point, or by taking readings of the device's geolocation over time. On a map, each coordinate is represented by small circles with red outlines. These are connected by red lines.

To collect a geoshape, first select the location-recording mode by tapping the "add point" button in the upper right side of the screen. The selected mode will be displayed in the gray bar at the bottom of the screen. While point collection is ongoing, the "add marker" button changes to a "pause" button. The "back arrow" button can be used to remove the last-entered point either when actively collecting points or when paused. Any point can be manually moved at any time by tapping on it and dragging it. The mode can only be changed if an existing line is first cleared by tapping the "trash" button. Recording must be paused to clear the existing line.

.. tip::
  Points that were entered by tapping or adjusted by dragging will always have an accuracy radius of 0. Points that were read from the device location will never have an accuracy radius of 0.

Once the shape has been saved, the coordinates of its points will be displayed on the question screen. The shape can be opened for manual editing by tapping to add more points, moving existing points or deleting the last-added point. After a shape has been saved once, it cannot be added to in manual or automatic location recording modes.

The three location recording modes are:

Placement by tapping
  The user taps the device to place points.

Manual location recording
  The user chooses when to tap the "record a point" button at the top of the screen to capture the device geolocation at that moment.

Automatic location recording
  The user is prompted to select a recording interval and accuracy requirement. If the accuracy requirement is set to None, points are always collected at the recording interval. If the accuracy requirement is set to any other value, a point will only be captured if it meets the requirement. For example, given a recording interval of 20s and an accuracy requirement of 10m, the app places a point at the device location every 20s if the location is accurate to 10m or better.

.. warning::

  If you are using Aggregate and you would like to collect more than 5 points at a time, you should :doc:`increase the database field length to over 255 characters <aggregate-field-length>`. Otherwise, additional points will be lost.

.. image:: /img/form-widgets/geoshape-question.*
  :alt: A geoshape form widget displayed in the ODK Collect app on an Android phone. The question text is "Select an Area." Below that is a button labeled "Start GeoShape."


.. image:: /img/form-widgets/geoshape-collected.*
  :alt: A map displayed in the ODK Collect App on an Android phone. Above the map is a green bar showing current location accuracy radius. On the right side are six icon buttons stacked vertically: Add point, Delete point, Zoom, Layers, Trash, Save.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  geoshape, shape_example, Select an area

.. _geoshape-area:

Calculating the area of a geoshape
"""""""""""""""""""""""""""""""""""

type
  :tc:`calculate`
calculation
  :tc:`area(${geoshape})`

The :tc:`area()` function calculates the land area,
in square meters,
of a polygon defined in a :ref:`geoshape-widget`.
The value will be included in your completed survey data,
and can also be used in later widgets in the form.

.. image:: /img/form-widgets/area-calc-0.*
  :alt: The geoshape widget. The question label is "Record a geoshape". The button label is "Start GeoShape".

.. image:: /img/form-widgets/area-calc-1.*
  :alt: A map with four pins defining an area around a city block.

.. image:: /img/form-widgets/area-calc-2.*
  :alt: The geoshape widget with a series of lat/long coordinates.

.. image:: /img/form-widgets/area-calc-3.*
  :alt: A note widget. "The area of the recorded geoshape is 19322 square meters."

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, calculation

  geoshape, shape, Record a Geoshape,
  calculate, shape_area, ,area(${shape})
  calculate, rounded_shape_area, ,"round(${shape_area}, 2)"
  note, shape_area_note, "| The area of the recorded geoshape is:
  | ${rounded_shape_area} m²",

.. _bearing-widget:

Bearing widget
~~~~~~~~~~~~~~~~

type
  :tc:`decimal`
appearance
  :tc:`bearing`

Captures a compass reading, which is stored as a decimal.

.. image:: /img/form-widgets/bearing-widget-start.*
  :alt: The Bearing form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Bearing widget." The hint text is, "decimal type with bearing appearance. Below that is a button labeled "Record Bearing." Above the question text is the form group name "Numeric widgets."

.. image:: /img/form-widgets/bearing-in-progress.*
  :alt: The Bearing widget, overlaid with a model popup. The modal headline is "Loading Bearing." In the body of the modal are two fields: "Direction: W" and "Bearing: 273.001". At the bottom of the modal are Cancel and Record Bearing buttons.

.. image:: /img/form-widgets/bearing-finished.*
  :alt: The Bearing widget, as displayed previously. The button's label is not "Replace bearing." Below the button is the decimal number 271.538 (the recorded bearing).

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  decimal,bearing_widget,Bearing widget,bearing,decimal type with bearing appearance


.. _openmapkit-widget:

OpenMapKit widget
~~~~~~~~~~~~~~~~~~~~~~~~

`OpenMapKit`_ allows you to add questions about
OpenStreetMap features in a Collect-rendered form.

For more details, see the `OpenMapKit`_ documentation.

.. _OpenMapKit: http://www.openmapkit.org


.. _image-widgets:

Image widgets
---------------

.. tip::
  Image files can be very large. We recommend always including :ref:`a maximum image size in form design <scaling-down-images>`. Also, consider making test submissions to your server with the Internet conditions you expect when gathering data to make sure that you can send files of the size you expect.

.. contents::
 :local:

.. _default-image-widget:

Default image widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`image`
appearance
  *none*

Captures an image from the device. The user can choose to take a new picture with the device camera, or select an image from the device photo gallery.

.. image:: /img/form-widgets/default-image-widget.*
  :alt: The default Image form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Image Widget." The hint text is, "image type with no appearance." Below that are two buttons: "Take Picture" and "Choose Image." Above the question text is the form group name "Image widgets."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  image,image_widget,Image widget,image type with no appearance

.. add entire photo cycle

.. _annotate-widget:

Image widget with annotation
"""""""""""""""""""""""""""""

type
  :tc:`image`
appearance
  :tc:`annotate`

Adding the :tc:`annotate` appearance allows the user to draw on the image before submitting it.

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

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  image,annotate_image_widget,Annotate widget,annotate,image type with annotate appearance

.. _new-image-widget:

Image widget with required new image
""""""""""""""""""""""""""""""""""""""""

type
  :tc:`image`
appearance
  :tc:`new`

An image widget that does not include a :guilabel:`Choose Image` button. This requires the user to take a new picture.

.. image:: /img/form-widgets/new-image-widget.*
  :alt: The new image widget, as displayed in the ODK Collect app on Android. It is largely identical to the previous image widget, except that there is only a Take Picture button, and there is no Choose Image button.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, appearance, hint

  image, image_widget_no_choose, Image widget without Choose button, new, image type with new appearance (can also be added with annotate appearance and on audio and video types)


.. _self-portrait-image-widget:

Self portrait (*selfie*) image widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`image`
appearance
  :tc:`new-front`

Takes a picture using the front-facing ("selfie") camera. The :guilabel:`Choose image` button is not displayed.

.. versionchanged:: 1.15

  Prior to v1.15, the appearance attribute for this was :tc:`selfie`.
  The old appearance attribute will continue to work on existing forms, but new forms should use the :tc:`new-front` appearance.


.. image:: /img/form-question-types/self-portrait-0.*
 :alt: The self portrait widget in Collect. The label text is "Self portrait (selfie) widget)". The hint text is "Image type with new-front appearance". There is a button labeled "Take Picture".

.. image:: /img/form-question-types/self-portrait-1.*
 :alt: The camera screen on a device, taking a self-portrait of a person.

.. image:: /img/form-question-types/self-portrait-2.*
 :alt: The self portrait widget as described above. Below the button is the self-portrait image captured in the previous image.


.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint, appearance

  image, self-portrait, Self portrait (*selfie*) widget, image type with new-front appearance, new-front



.. _draw-widget:

Draw widget
~~~~~~~~~~~~~

type
  :tc:`image`
appearance
  :tc:`draw`


Provides the user a drawing pad and collects the drawn image.

.. image:: /img/form-widgets/draw-widget.*
  :alt: The Draw form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Draw widget." The hint text is "image type with draw appearance." Below that is a button labeled "Sketch Image." Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/draw-in-progress.*
  :alt: A white "drawing pad" on an Android phone, horizontally oriented (landscape mode). A simple smiley face has been drawn. In the lower right corner of the drawing pad is a plus sign (+) in a circle.

.. image:: /img/form-widgets/draw-options.*
  :alt: The drawing pad as displayed in the previous image. A menu has expanded from the lower right corner with the options: Reset, Save and Close, and Set Color.

.. image:: /img/form-widgets/draw-completed.*
  :alt: The Draw widget as displayed previously. Below the "Sketch Image" button is the smiley face from the drawing pad image shown previously.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  image,draw_image_widget,Draw widget ,draw,image type with draw appearance

.. _scaling-down-images:

Scaling down images
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Images created with any of the image widgets described above can be automatically scaled down on save by using the ``max-pixels`` parameter. If the long edge of the image is larger than the maximum size specified, the image is resized proportionally so that the long edge matches the provided pixel value. This is useful to reduce the upload size when bandwidth is limited.

Available in Collect since v1.10.0 and in XLSForm since 7/2018.

.. rubric:: XLSForm

In the parameters column, write ``max-pixels=`` followed by the desired maximum length of the long edge in pixels.

.. csv-table:: survey
  :header: type, name, label, parameters, hint

  image,my_scaled_image,Scaled image,max-pixels=1024,image scaled to a max long edge of 1024 pixels


.. _audio:

Audio widget
----------------

type
  :tc:`audio`
appearance
  :tc:`none`

Records audio using the device's microphone or a connected external microphone. By default, an :ref:`external application <external-audio-app>` is used. Starting with Collect v1.29, you can also use :ref:`built-in recording <built-in-audio-recording>`.

.. image:: /img/form-widgets/audio-start.*
  :alt: The Audio form widget as displayed in the ODK Collect App on an Android phone. The question text is "What does it sound like?" There are two buttons: Record Sound and Choose Sound.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  audio, bird_recording, What does it sound like?

.. tip::

  Audio files can be very large so if you record audio in your form, make sure that you consider your audio quality settings. Also, consider making test submissions to your server with the Internet conditions you expect when gathering data to make sure that you can send files of the size you expect.

  Android devices can make many sounds during use and these will be included in recordings. We recommend turning off sounds from button presses, camera shutters and notifications before recording.

.. _built-in-audio-recording:

Using the built-in audio recorder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 1.29

  `ODK Collect v1.29.0 <https://github.com/getodk/collect/releases/tag/v1.29.0>`_

The built-in audio recorder makes it possible to capture audio without having to install an external app. It also enables recording while filling out other questions and is designed to continue recording even if the user switches to another app or if the phone screen is locked. To use the built-in audio recorder, :ref:`specify the desired audio quality <customizing-audio-quality>` for each audio question in your form. You can also :ref:`configure Collect to always use the built-in recorder <use-external-app-for-audio-recording>`.

.. image:: /img/form-widgets/built-in-recorder.*
  :alt: The built-in recorder as displayed in the ODK Collect App on an Android phone. The user interface is described below.

When built-in audio recording is enabled and recording is initiated, a recording control bar appears at at the top of the screen. At the top left of this bar is an icon to represent whether recording is currently ongoing or paused (1). To the right of this icon is the current length of the recording (2).

.. warning::

  Pause is only available on Android 7.0 and above. On lower Android versions, the pause button is hidden.

At the right of the control bar are a pause button (3) and a stop button (4). When the pause button is tapped, recording is temporarily suspended and the button icon changes to a microphone. When the microphone is tapped, recording is resumed. Recording can be paused and resumed as many times as desired. When the stop button is tapped, the recording is ended and can no longer be modified.

Recording status is also displayed below the audio question text. There is a time representing the current length of the recording (5) and a diagram (6) representing the volume of the recording over time. The diagram provides confirmation that the microphone is working and can help a user ensure an even, sufficient volume.

Other questions can be included on the same screen as a built-in recording question. As shown in the screenshot above, this makes it possible to capture quantitative content while recording. To achieve this, put the questions in a :ref:`field list <field-list>`.

During recording, the user is prevented from leaving the current question screen. However, it is safe to use other applications or to lock the device screen.

Once recording is stopped, the control bar disappears. The recording is made available for playback below the question text.

To replace the audio captured, first delete the current file and then record again.

In some rare cases such as the device running out of space, the recording may complete successfully but not be attached to the form. If this happens, a dialog will be displayed explaining that the file is available but needs to be accessed manually. You can find these files in the ``recordings`` folder of the :ref:`Collect directory <collect-directory>`. This folder is never cleared so consider emptying it yourself once you have retrieved its files.

.. _customizing-audio-quality:

Customizing audio quality
~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 1.29

  `ODK Collect v1.29.0 <https://github.com/getodk/collect/releases/tag/v1.29.0>`_, `pyxform` v1.3.0, `XLSForm Online` v2.3.0

The quality of audio recordings can be customized using the ``quality`` parameter. If a ``quality`` is specified, the built-in recorder is always used, regardless of Collect settings. If no ``quality`` is specified and Collect is :ref:`configured to use the built-in recorder <use-external-app-for-audio-recording>`, ``normal`` is used. The available quality values are:

.. list-table::
   :header-rows: 1

   * - Value
     - Extension
     - Encoding
     - Bit rate
     - Sample rate
     - File size
   * - normal
     - .m4a
     - AAC
     - 64kbps
     - 32kHz
     - ~30MB/hour
   * - low
     - .m4a
     - AAC
     - 24kbps
     - 32kHz
     - ~11MB/hour
   * - voice-only
     - .amr
     - AMR
     - 12.2kbps
     - 8kHz
     - ~5MB/hour

.. tip::

  We'd recommend only using ``voice-only`` for one-on-one interviews in a quiet place as otherwise there might be too much detail loss. ``low`` will sound compressed but speech is generally intelligible, even if multiple people are talking at once. ``normal`` is similar to typical podcast settings and will sound good on most devices.

  It's a good idea to test the different qualities out with the device (and any other equipment) you'll be using in the field to see which one fits your use case and setup best.

.. rubric:: XLSForm

In the parameters column, write ``quality=`` followed by the desired value.

.. csv-table:: survey
 :header: type, name, label, parameters

 audio,voice_only_audio,Voice audio,quality=voice-only

Changing audio quality during form entry
"""""""""""""""""""""""""""""""""""""""""

If it's a possibility that an individual question could need different qualities depending on context you can use :ref:`relevance <relevants>` to switch between them:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, parameters, relevance

  select_one, yes_no, is_quiet, Are you currently in a quiet location with only one person speaking at a time?

  audio recording_voice_only, Please record, quality='voice-only',, ${is_quiet} = 'yes'
  audio recording_normal, Please record, quality='normal',, ${is_quiet} = 'no'

.. csv-table:: choices
  :header: list_name, name, label

  yes_no, yes, Yes
  yes_no, no, No

.. _external-audio-app:

Recording with an external app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting ``quality`` to ``external`` will use an external app to record audio rather than use Collect's built in recording features. Some Android devices provide a default application for audio recording. Others do not, and the user will need to install an audio recording app.

There are many apps available for this, including:

- `Axet Audio Recorder (open source) <https://play.google.com/store/apps/details?id=com.github.axet.audiorecorder>`_
- `RecForge II <https://play.google.com/store/apps/details?id=dje073.android.modernrecforge>`_

Any app that responds to
``android.provider.MediaStore.Audio.Media.RECORD_SOUND_ACTION``
will be compatible.

.. _video:

Video widgets
----------------

.. tip::
  Video files can be very large. We recommend configuring video options for every device you intend to use for data collection. Also make submissions to your server with the Internet conditions you expect when gathering data to make sure that you can send files of the size you expect. Note that Central :ref:`has a 100MB file upload size limit by default <file-upload-fails-with-413>`.

.. contents::
 :local:

.. _default-video-widget:

Default video widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Records video, using the device camera.

.. image:: /img/form-widgets/video-start.*
  :alt: The Video form widget as displayed in the ODK Collect App on an Android phone. The question text is "Please record a video of yourself blinking." The hint text is "Three times is probably sufficient." Below that are three buttons: Record Video, Choose Video, and Play Video. The Play Video button is disabled.


.. image:: /img/form-widgets/video1.*
  :alt: The Android camera app, in video mode. A person's face is in the camera viewer. Below the camera viewer is a large, blue checkmark button.

.. image:: /img/form-widgets/video2.*
  :alt: The Video form widget as displayed previously. The question text is "Please record a video of yourself blinking." The hint text is "Three times is probably sufficient." Below that are three buttons: Record Video, Choose Video, and Play Video. All three buttons are enabled.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  video, blinking, Please record a video of yourself blinking., Three times is probably sufficient.


.. _self-portrait-video-widget:

Self portrait (*selfie*) video widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Records video, using the front-facing ("selfie") camera. The :guilabel:`Choose Video` button is not displayed.

.. image:: /img/form-widgets/selfie-video-widget.*
  :alt: The Self portrait (*selfie*) video widget form widget as displayed in the ODK Collect App on an Android phone. The question text is "Self portrait (*selfie*) video widget". The hint text is "video type with new-front appearance". Below that are two buttons: Record Video and Play Video. The Play Video button is disabled.

.. image:: /img/form-widgets/selfie-video-widget-recording.*
  :alt: The camera view with a person's face.

.. image:: /img/form-widgets/selfie-video-widget-recorded.*
  :alt: The Self portrait (*selfie*) video widget form widget as displayed previously. The question text is "Self portrait (*selfie*) video widget". The hint text is "video type with new-front appearance". Below that are two buttons: Record Video and Play Video. Both buttons are enabled.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint

  video, selfie-video, Self portrait (*selfie*) video widget, new-front, video type with new-front appearance

.. _file-upload:

File upload widget
--------------------

.. versionadded:: 1.15

  `ODK Collect v1.15.0 <https://github.com/getodk/collect/releases/tag/v1.15.0>`_

Uploads any file from the device to the form.

.. warning::

  Users can upload **any** file type,
  which includes potentially malicious files.
  You should not include this widget
  unless you trust the people using the form.

  Even then, you should take precautions
  before downloading or opening files.

  - Run an antimalware scan.
  - Verify the file is a type you expect
    (such as a :file:`.pdf` document),
    and not a `potentially dangerous file`_
    (such as :file:`.exe` or :file:`.ini`).

  .. _potentially dangerous file: https://support.symantec.com/en_US/article.INFO3768.html

.. image:: /img/form-question-types/file-upload-widget.*
  :alt: The file upload widget in Collect.
       The question label is "Select a file to upload."
       Below that is a button labeled "Choose File".

.. image:: /img/form-question-types/file-upload-open-from.*
  :alt: A  file selection screen on an Android device.
	A sidebar overlay is labeled "Open from".
	This sidebar has several file locations such as "Recent", "Google Drive", "Images", "Downloads".

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  file, some-file, Select a file to upload.


.. _barcode:

Barcode widget
----------------

Scans, decodes, and captures the content of a barcode, using the device camera.

The following barcode formats are supported:

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- Codabar
- ITF
- RSS-14
- RSS-Expanded
- QR Code
- Data Matrix
- Aztec (beta)
- PDF 417 (beta)
- MaxiCode

.. note::
  Barcode scanning is built into Collect versions 1.7.0 and greater.

  Versions of Collect prior to 1.7.0 require the `Barcode Scanner app`_ to be installed.

.. _Barcode Scanner app: https://play.google.com/store/apps/details?id=com.google.zxing.client.android

.. contents::
 :local:

.. _default-barcode-widget:

Default barcode widget
~~~~~~~~~~~~~~~~~~~~~~~~

The flash can be used as a light source when scanning barcodes in a poorly lit environment.

.. image:: /img/form-widgets/barcode-start.*
  :alt: The Barcode form widget as displayed in the ODK Collect app on an Android phone. The headline text reads, "Scan any barcode." Below that is an image labeled "Get Barcode."

.. image:: /img/form-widgets/barcode1.*
  :alt: A barcode scanner on an Android device. A barcode is in the viewfinder, with a thin blue line across the barcode.

.. image:: /img/form-widgets/barcode2.*
  :alt: The Barcode form widget as displayed previously. The button label is now "Replace Barcode." Below the button is a string of numbers representing the decoded content of the scanned barcode.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  barcode, barcode_example, Scan any barcode.


.. _self-portrait-barcode-widget:

Self portrait (*selfie*) barcode widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases a front camera may work better. The flash can't be used in this case.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance

  barcode, barcode_example, Scan any barcode., front

.. _range-widgets:

Range widgets
----------------

Range widgets allow the user to select numbers from within a range that is visually represented as a number line. The parameters of the range widget are defined by :tc:`start`, :tc:`end`, and :tc:`step` values defined in the :th:`parameters` column of your XLSForm. The parameter values can be integers or decimals.

.. contents::
  :local:

.. _range-widget-integers:

Default range widget with integers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`range`
appearance
  *none*

If all three parameter values are integers,
the input will be stored as an integer.

.. image:: /img/form-widgets/range-integer-default-widget.*
  :alt: The range widget, as displayed in the ODK Collect app on Android. The question text is "Range integer widget". The main part of the widget shows a horizontal line labeled "1" on the left end and "10" on the right. There are ten points on the line.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, parameters

  range, range_integer_widget, Range integer widget,,range integer widget with no appearance, start=1;end=10;step=1

.. _range-widget-decimal:

Default range widget with decimals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`range`
appearance
  *none*

If any of the parameter values are decimals,
the input will be stored as a decimal.

.. image:: /img/form-widgets/range-decimal-default-widget.*
  :alt: The range widget as displayed previously. The number selection choices range from 1.5 to 5.5, and the selection line is horizontal.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, parameters

  range, range_decimal_widget, Range decimal widget,,range decimal widget with no appearance, start=1.5;end=5.5;step=0.5

.. _vertical-range-widget:

Vertical range widget
~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`range`
appearance
  :tc:`vertical`

To display the range widget's number line vertically,
use the :tc:`vertical` appearance.
Both integers and decimals are supported.

.. image:: /img/form-widgets/range-integer-vertical-widget.*
  :alt: The range widget, as displayed in the previous image, but the range number line is vertical instead of horizontal.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, parameters

  range, range_integer_widget_vertical, Range vertical integer widget, vertical, range integer widget with vertical appearance, start=1;end=10;step=1

.. _range-picker-widget:

Range widget with picker
~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`range`
appearance
  :tc:`picker`

When the :tc:`picker` appearance is added, the range widget is displayed with a spinner-style select menu in a dialog. The value between horizontal lines is the selected value. Users can scroll the spinner up and down or can tap on the value above to go up by one and on the value below to go down by one.

.. image:: /img/form-widgets/range-widget-picker-0.*
  :alt: The range picker widget, as displayed in the ODK Collect app. The question label is "Range picker integer widget". There is a button labeled "Select Value".

.. image:: /img/form-widgets/range-widget-picker-1.*
  :alt: The range widget as shown in the previous image. Over it is a modal window labeled "Number Picker", with a spinner-style number select. Below are buttons for OK and CANCEL.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, parameters

  range, range_integer_widget_picker, Range picker integer widget, picker, range integer widget with picker appearance, start=1;end=10;step=1

.. _range-rating-widget:

Range widget with rating
~~~~~~~~~~~~~~~~~~~~~~~~~~~

type
  :tc:`range`
appearance
  :tc:`rating`

When the :tc:`rating` appearance is added, the range widget is displayed with stars having equal spacing. Number of stars is calculated using the `end` parameter. When the user taps on an empty star, the stars up to and including that star will be filled. If the stars don't fit in the device width, they will wrap onto additional lines.

.. image:: /img/form-widgets/range-widget-rating.*
  :alt: The range rating widget, as displayed in the ODK Collect app. The question label is "Range rating integer widget".

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, parameters

  range, range_integer_widget_rating, Range rating widget, rating, range integer widget with rating appearance, end=9


.. _note-widget:

Note widget
-------------

type
  :tc:`note`
appearance
  *none*


A note to the user, accepting no input. This example includes :term:`hint` text.

.. figure:: /img/form-widgets/note.*
  :alt: The Note form widget as displayed in the ODK Collect App on an Android phone. The headline text is, "This is an example note." The hint text is, "The text displays, but there is no input."

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, hint

  note, note_1, This is an example note., "The text displays, but there is no input."


.. _url-widget:

URL widget
--------------

type
  :tc:`text`
appearance
  :tc:`url`

Provides a link which the user can open from the survey.
Takes no input.

The URL to open is specified with :th:`default`.

.. image:: /img/form-widgets/url-widget.*
  :alt: The URL form widget, as displayed in the ODK Collect app on an Android phone. The question text is "URL Widget." The hint text is "text type with url appearance and default value of http://getodk.org/" Below that is a button labeled, "Open URL." Below the button is the URL, "http://getodk.org/" Above the question text is the form group name "Text widgets."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, hint, default

  text,url_widget,URL widget,url,text type with url appearance and default value of http://getodk.org/,http://getodk.org/


.. _print-widget:

Printer widget
------------------

type
  :tc:`text`
appearance
  :tc:`printer:org.opendatakit.sensors.ZebraPrinter`

Connects to an external label printer, and prints labels that can contain a barcode, a QR code, or text.

See :doc:`printer-widget` for complete details.

.. image:: /img/form-widgets/printer-widget.*
  :alt: The external printer widget, as displayed in the ODK Collect app on an Android phone. The question text is "Ex printer widget." The hint text is "text type with printer:org.opendatakit.sensors.ZebraPrinter." Below that is a button labeled, "Initiate Printing." Above the question text is the form group name "Text widgets."

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance, calculation

   text,ex_printer_widget,Ex printer widget,printer:org.opendatakit.sensors.ZebraPrinter, "concat('123456789','<br>’,'QR CODE','<br>','Text')"

.. _trigger-widget:

Trigger/acknowledge widget
-----------------------------

type
  :tc:`trigger`, :tc:`acknowledge`
appearance
  *none*

The trigger widget,
also known as the acknowledge widget,
presents a single checkbox.

A completed trigger response is stored as the string ``OK``.

The example shown here includes the :th:`required` attribute.

.. image:: /img/form-widgets/trigger.*
  :alt: The Trigger (or "Acknowledge") form widget as displayed in the ODK Collect App on an Android phone. The question text is, "Trigger widget." The hint text is, "Prompts for confirmation. Useful to combine with required or relevant. (type=trigger)" Below that is a single checkbox labeled, "OK. Please continue." The checkbox is unchecked.

.. image:: /img/form-widgets/trigger-sorry.*
  :alt: The Trigger widget shown previously. An error text reads, "Sorry, this response is required."

.. image:: /img/form-widgets/trigger-selected.*
  :alt: The Trigger widget shown previously. The checkbox is now checked.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint, required

  trigger,my_trigger,Trigger widget,Prompts for confirmation. Useful to combine with required or relevant. (type=trigger),true()


.. _signature-widget:

Signature widget
------------------

type
  :tc:`image`
appearance
  :tc:`signature`

Collects a signature from the user.

.. image:: /img/form-widgets/signature-start.*
  :alt: The Signature form widget, as displayed in the ODK Collect app on an Android phone. The question text is, "Signature widget." The hint text is "image type with signature appearance." Below that is a button labeled "Gather Signature." Above the question text is the form group name "Image widgets."

.. image:: /img/form-widgets/signature-in-progress.*
  :alt: A drawing pad with a signature line, displayed on an Android phone. A signature is drawn across it. In the lower right corner is circular button marked with a plus sign (+).

.. image:: /img/form-widgets/signature-completed.*
  :alt: The signature widget displayed previously. Below the button is the signature drawn in the previous image.

.. rubric:: XLSForm

.. csv-table:: table
  :header: type, name, label, appearance, hint

  image,signature_widget,Signature widget,signature,image type with signature appearance

.. _hidden-questions:

Hidden questions
------------------

Not all question types render as visible widgets in Collect.
These questions do collect and store values,
which are accessible as :ref:`variables <variables>`
and available in Aggregate and other data analysis tools.

.. contents::
  :local:

.. _metadata:

Metadata
~~~~~~~~~~

Metadata questions capture information about the device or a survey collection event and are not visible to the user.

A more complete record of user behavior within a form can be generated by enabling :doc:`form audit logging <form-audit-log>`.

These items are dependent on the survey collection event:

- :tc:`start` --- The datetime the survey was started in ISO 8601 format (e.g., 2019-09-27T09:45:10.854-07:00).
- :tc:`end` --- The last datetime the survey was saved in ISO 8601 format.
- :tc:`today` --- The date the survey was started in ISO 8601 format (e.g, 2019-09-27).
- :tc:`start-geopoint` --- The geolocation when the survey was started. :ref:`Read more <metadata-start-geopoint>`.

This item is defined at installation time and cannot be changed:

- :tc:`deviceid`

These items are defined in Collect,
and :ref:`can be edited in Settings <form-metadata-settings>`:

- :tc:`username`
- :tc:`phonenumber`

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name

  start,start
  end,end
  today,today
  deviceid,deviceid
  username,username
  phonenumber,phonenumber
  start-geopoint,start-geopoint

.. _metadata-start-geopoint:

Geolocation at survey start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::
  :ref:`Audit log geolocation tracking <audit-geolocation-tracking>`

.. note::
  Geolocation at survey start was added in Collect v1.23 and Aggregate v2.0.4/v1.7.4. Form conversion requires XLSForm Online ≥ v1.6.1, XLSForm Offline ≥ v1.11.1 or pyxform ≥ v0.15.1.

The :tc:`start-geopoint` question type is used to capture a single geolocation in :ref:`geopoint format <location-widgets>` when the survey is first started. Questions of type :tc:`start-geopoint` may be given any allowable name. Although it is possible to have more than one :tc:`start-geopoint` question in a form, all will have the same value.

Any time a survey with a `start-geopoint` question is opened in Collect, the enumerator will see a warning that the form tracks device location. If the device battery is low, or if location tracking needs to be turned off for any reason, you can tap :menuselection:`⋮ --> Track location` or turn off location providers in Android.

The first time that a survey with a `start-geopoint` question is opened, Collect will attempt to read the device's geolocation. The geolocation reading with the highest accuracy received in a 20-second window will be recorded. A location icon will be displayed in the Android status bar while the geolocation is being requested by Collect.

Geolocation is read using data from GPS, WiFi and possibly other signals so this feature should work in most environments.

If geolocation information is unavailable, the question will be left blank. Reasons for a blank value may include the enumerator turning off location providers, Collect not having location permissions, Google Play Services not being installed, the GPS not having satellite lock and more. No troubleshooting information is provided in the form submission.

Including a `start-geopoint` question may make it faster to get high-accuracy geolocation readings for other :ref:`location question types <location-widgets>` by "warming" the GPS.

.. _calculate-question:

Calculate
~~~~~~~~~~~

type
  :tc:`calculate`

Calculate questions let you evaluate complex :ref:`expressions <expressions>`,
storing the values for later use.

For more details, see :ref:`calculations`.

--------

.. _field-list:

Grouping multiple widgets on the same screen
------------------------------------------------

type
  :tc:`begin_group`
appearance
  :tc:`field-list`

The :tc:`field-list` appearance attribute, applied to a group of widgets, displays them all on a single screen.

.. warning::

  Relevance, constraint and calculation evaluation within the same screen is supported in Collect v1.22 and later.

.. warning::

  Displaying :ref:`repeats` on the same screen (inside a :tc:`field-list` group) is not supported.

.. seealso::

  :ref:`groups` and :ref:`repeats`.

.. _select-grid:

Grid of selects on the same screen
------------------------------------

If you have multiple select questions with the same choices, it can be helpful to group them on one screen.

.. image:: /img/form-widgets/select-grid.*
  :alt: A field-list group of questions, as displayed in the ODK Collect app on an Android phone. A grid of questions representing underlying conditions are displayed. For eacn condition, there are radio buttons to indicate 'Yes' or 'No'.


To do this, put your select questions in a :tc:`field-list` group and use the following :th:`appearance` attributes:

:tc:`label`
  Only the option labels are displayed, without checkboxes. This is used for the top row with the 'Yes' and 'No' options in the example above.
:tc:`list-nolabel`
  Only checkboxes or radio buttons are displayed, without their labels. This is used for the question rows in the example above.
:tc:`list`
  The labels are displayed along with checkboxes for multi-select questions and radio buttons for single-select questions. You could use this instead of having a :tc:`label` row to keep the option labels closer to the checkboxes or radio buttons.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, appearance

  begin_group, underlying_conditions, Underlying conditions, field-list
  select_one, yes_no, condition_labels, Conditions, label
  select_one, yes_no, Comcond_preg, Pregnancy, list-nolabel
  select_one, yes_no, Comcond_partum, Post-partum (< 6 weeks), list-nolabel
  end_group, underlying_conditions

.. csv-table:: choices
  :header: list_name, name, label

  yes_no, yes, Yes
  yes_no, no, No
