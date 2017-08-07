Form Widgets
===============

This document is a list of available :term:`ODK Collect` :term:`form` :term:`widgets <widget>` (question types), with:

- examples images from the ODK Collect app
- example Excel spreadsheet rows for creating form widgets with :term:`ODK XLSForm`
- example :term:`ODK XForm` XML snippets

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

.. _integer::

Integer
---------

A whole number entry input. Integer widgets will not accept decimal points.

.. image:: /img/form-widgets/integer.*
  :alt: An integer form widget displayed in the ODK Android App. The question is "What is your age in years?" A numerical keyboard is displayed.

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
  :alt: An integer form widget displayed in the ODK Android App. The question is "Weight in kilograms." A numerical keyboard is displayed.

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
