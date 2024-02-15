******************************
Form Operators and Functions
******************************

:ref:`expressions` in :ref:`calculations <calculations>`, :ref:`constraints <constraints>`, and :ref:`relevants <relevants>`
can contain operators and functions.
    
.. _form-operators:

Operators
==========

.. _math-operators:
  
Math operators
---------------

.. csv-table::
  :header: , Explanation, Example
  
  \+, addition, ${salary_income} + ${self_employed_income}
  \-, subtraction, ${income} - ${expenses}
  \*, multiplication, ${bill} * 1.18
  div, division, ${percent_int} div 100 
  mod, `modulo`_ (division remainder), (${even_number} mod 2) = 0

.. _modulo: https://en.wikipedia.org/wiki/Modulo_operation

.. warning::

  Math operators only work with numbers.
  
  - The addition operator cannot be used to concatenate strings.
    Use the :func:`concat` function instead.
  - Empty values 
    (that is, :ref:`variables <variables>` referencing unanswered questions)
    are actually empty strings, 
    :ref:`and will not be automatically converted to zero (0) <empty-values>`.
  
.. _comparison-operators:
  
Comparison operators
-----------------------
  
Comparison operators are used to compare values.
The result of a comparison is always ``True`` or ``False``.
  
.. csv-table::
  :header: , Explanation, Example, Notes
  
  =, equal to, ${enrolled} = 'yes', Can compare numbers or strings.
  !=, not equal to, ${enrolled} != 'yes', Can compare numbers or strings.
  >, greater than, ${age} > 17, 
  >=, greater than or equal to, ${age} >= 18,
  <, less than, ${age} < 65, 
  <=, less than or equal to, ${age} <= 64,
  
.. warning::

  - The relational operators (``>``, ``>=``, ``<``, ``<=``)
    only work with numbers.
  - :ref:`Empty response values 
    are not automatically converted to zero (0) <empty-values>`.
  
.. _boolean-operators:
  
Boolean operators
------------------

Boolean operators combine two ``True`` or ``False`` values
into a single ``True`` or ``False`` value.

.. csv-table::
  :header: , Explanation, Example

  and, ``True`` if the expressions before and after are ``True``, ${age} > -1 and ${age} < 120
  or, ``True`` if either of the expressions before or after are ``True``, ${age} < 19 or ${age} > 64


.. _path-operators:

Path operators
-------------------

.. csv-table::
  :header: , Explanation, Example, Notes
  
  ., current question's value, . >= 18, Used in :ref:`constraints <constraints>`.
  \.\., current question's parent group, position(..), Used with :func:`position` to get a parent repeat instance's index.

.. note:: 

  Formally, these are not operators but rather XPath references 
  to the current node (``.``) and the parent node (``..``).
  :ref:`XPath paths <xpath-paths>` can be used to reference nodes of a form.
  
.. _form-functions:
  
Functions
===========

    
.. seealso:: `Functions in the ODK XForm Specification <https://getodk.github.io/xforms-spec/#xpath-functions>`_

    
.. _control-flow-functions:

Control flow
--------------

.. function:: if(expression, then, else)

  Returns ``then`` if ``expression`` evaluates to ``True``. 
  Otherwise, returns ``else``.

  
  
.. function:: position(xpath)

  Returns an integer equal to the 1-indexed position of the current node
  within the node defined by ``xpath``.
  
  Most often this is used in the form ``position(..)``
  to identify the current iteration index
  within a repeat group.  
  
  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst

.. function:: once(expression)

  Returns the value ``expression`` if the question's value is empty.
  Otherwise, returns the current value of the question.

  This can be used to ensure that a random number is only generated once,
  or to store the first value entered for a question
  in a way that is retrievable even if the response is changed later.

  .. warning::

    This function is often misunderstood. Read :ref:`when expressions are evaluated <when-expressions-are-evaluated>` to learn more.

.. _response-access-functions:
  
Accessing response values
--------------------------

.. note::

  The response from most question types
  can be accessed using :ref:`variables <variables>`.
  Functions are needed for accessing responses to 
  :ref:`multi select questions <select-functions>` and
  questions inside :ref:`repeat groups <repeat-functions>`.

.. _select-functions:
  
Select questions
~~~~~~~~~~~~~~~~~~~

.. function:: selected(space_delimited_array, string)

  Returns ``True`` if ``string`` 
  is a member of ``space_delimited_array``,
  otherwise returns ``False``.
  
  Commonly used to determined if a specific choice was selected
  in a :ref:`select question <select-widgets>`. 
  (This is possible because 
  a :ref:`reference to <variables>` a select question
  returns a space-delimited array of choice names.)

  .. container:: details
      
    .. include:: incl/form-examples/constraint-on-selected.rst
  
.. function:: selected-at(space_delimited_array, n)

  Returns the string at the ``n``\ :sup:`th` position 
  of the ``space_delimited_array``.
  (The array is zero-indexed.)
  Returns an empty string if the index does not exist.  
  
  This can be used to get the ``name`` of a selected choice 
  from a :ref:`multi-select question <multi-select-widget>`.
  (This is possible because 
  a :ref:`reference to <variables>` a select question
  returns a space-delimited array of choice names.)
  
  .. note::
  
    If used to get a choice name from a select question,
    this function returns the ``name``, not the ``label``,
    of the selected choice.
    To get the label in the current language,
    use :func:`jr:choice-name`.
  
  .. container:: details
  
    .. image:: /img/form-operators-functions/selected-at-0.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" Several color names are presented as options. Red, Green, and Purple are selected.
      :class: device-screen-vertical

    .. image:: /img/form-operators-functions/selected-at-1.* 
      :alt: A note widget in Collect. The label is "Selected Colors". The hint text is "red, green, purple".
      :class: device-screen-vertical

    .. rubric:: XLSForm

    .. csv-table:: survey
      :header: type, name, label, hint, calculation

      select_multiple colors, color_prefs, What colors do you like?, Select three.
      calculate, color_0, , ,"selected-at(${color_prefs}, 0)"
      calculate, color_1, , ,"selected-at(${color_prefs}, 1)"
      calculate, color_2, , ,"selected-at(${color_prefs}, 2)"
      note, color_note, Selected colors:, ${color_0} <br> ${color_1} <br> ${color_2}  

    .. csv-table:: choices
      :header: list_name, name, label

      colors, red, Red
      colors, blue, Blue
      colors, yellow, Yellow
      colors, green, Green
      colors, orange, Orange
      colors, purple, Purple

.. function:: count-selected(multi_select_question)

  Returns the number of choices selected in ``multi_select_question``.
  
  .. container:: details
  
    .. image:: /img/form-operators-functions/count-selected-constraint.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" The hint text is "Select three." Four colors are selected. A message modal overlays the widget with the text "Select exactly three."
      :class: device-screen-vertical

    .. rubric:: XLSForm

    .. csv-table:: survey
      :header: type, name, label, hint, constraint, constraint_message

      select_multiple colors, color_prefs, What colors do you like?, Select three., count-selected(.)=3, Select exactly three.

    .. csv-table:: choices
      :header: list_name, name, label

      colors, red, Red
      colors, blue, Blue
      colors, yellow, Yellow
      colors, green, Green
      colors, orange, Orange
      colors, purple, Purple

.. function:: jr:choice-name(choice_name, 'select_question')

  Returns the label value, in the active language, associated with the ``choice_name`` in the list of choices for the ``select_question``.
  
  .. note::
  
    You have to wrap the ``select_question`` reference in quotes.
    
    .. code-block:: none
    
      '${question_name}'
      
  .. container:: details  
  
    .. image:: /img/form-operators-functions/choice-name-multi-lang-english-0.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" Several color names are presented as options. Red, Green, and Purple are selected.
      :class: device-screen-vertical

    .. image:: /img/form-operators-functions/choice-name-multi-lang-english-1.* 
      :alt: A note widget in Collect. The label is "Selected colors". The hint text is "Red, Green, Purple."
      :class: device-screen-vertical

    .. image:: /img/form-operators-functions/choice-name-multi-lang-spanish-0.* 
      :alt: A multi-select widget in Collect. The label is "¿Qué colores te gustan?" Several color names, in Spanish, are presented as options. Rojo, Verde, and Púrpura are selected.
      :class: device-screen-vertical

    .. image:: /img/form-operators-functions/choice-name-multi-lang-spanish-1.* 
      :alt: A note widget in Collect. The label is "Colores seleccionados." The hint text is "Rojo, Verde, Púrpura".
      :class: device-screen-vertical

    .. rubric:: XLSForm

    .. csv-table::  survey
      :header: type, name, label::English, label::Español, hint::English, hint:Español, calculation

      select_multiple colors, color_prefs, What colors do you like?, ¿Qué colores te gustan?, Select three., Seleccione tres.
      calculate, color_0, , , , ,"jr:choice-name( selected-at(${color_prefs}, 0), '${color_prefs}')"
      calculate, color_1, , , , ,"jr:choice-name( selected-at(${color_prefs}, 1), '${color_prefs}')"
      calculate, color_2, , , , ,"jr:choice-name( selected-at(${color_prefs}, 2), '${color_prefs}')"
      note, color_note, Selected colors:, Colores seleccionados:, ${color_0} <br> ${color_1} <br> ${color_2}, ${color_0} <br> ${color_1} <br> ${color_2}

    .. csv-table:: choices
      :header: list_name, name, label::English, label::Español

      colors, red, Red, Rojo
      colors, blue, Blue, Azul
      colors, yellow, Yellow, Amarillo
      colors, green, Green, Verde
      colors, orange, Orange, Anaranjado
      colors, purple, Purple, Púrpura

.. _repeat-functions:
    
Repeat groups
~~~~~~~~~~~~~~~~

.. admonition:: Helpful terms

  .. glossary::
    :sorted:

    nodeset

      A collection of XML nodes.
      In XLSForms, this is typically a collection of response values. 

      Outside a :ref:`repeat group <repeats>`, 
      :ref:`referring to a question by name <variables>`
      will return a nodeset containing all the responses to that question.
      
      Nodesets can also be created by joining two or more nodes with pipes: ``/data/age | /data/name``.

        
.. function:: indexed-repeat(name, group, i [, sub_grp, sub_i [, sub_sub_grp, sub_sub_i ]])

  Returns the response value of question ``name``
  from the repeat-group ``group``,
  in iteration ``i``.
  
  Nested repeat groups can be accessed 
  using the ``sub`` and ``sub_sub`` parameters.

  .. seealso:: :ref:`referencing-answers-in-repeats`

  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst

.. function:: count(nodeset)

  Returns the number of items in ``nodeset``. This can be used to count the number of repetitions in a :ref:`repeat group <repeats>`.

  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst
  
.. function:: count-non-empty(nodeset)

  Returns the number of non-empty members of ``nodeset``.

.. function:: sum(nodeset)

  Returns the sum of the members of ``nodeset``.
  
  Can be used to :ref:`tally responses to a repeated select question <counting-answers>`.
  
  .. container:: details
  
    .. include::  incl/form-examples/sum-to-count-responses.rst

.. function:: max(nodeset)

  Returns the largest member of ``nodeset``.
  
  .. container:: details
  
    .. rubric:: XLSForm

    .. csv-table:: survey
      :header: type, name, label, calculation

      begin_repeat, child_questions, Questions about child
      text, child_name, Child's name
      integer, child_age, Child's age
      end_repeat
      calculate, age_of_oldest_child, , max(${child_age})

.. function:: min(nodeset)

  Returns the smallest member of ``nodeset``.

  .. container:: details 
   
    .. rubric:: XLSForm

    .. csv-table:: survey
      :header: type, name, label, calculation

      begin_repeat, child_questions, Questions about child
      text, child_name, Child's name
      integer, child_age, Child's age
      end_repeat
      calculate, age_of_youngest_child, , min(${child_age}) 

      
.. warning::

  The :func:`min` and :func:`max` functions
  only work sets of numbers.
  Empty values 
  (that is, :ref:`variables <variables>` referencing unanswered questions)
  are actually empty strings, 
  :ref:`and will not be automatically converted to zero (0) <empty-values>`.
       
.. _string-functions:
  
Strings
--------

.. _string-comparison-functions:

Searching and matching strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. function:: regex(string, expression)

    Returns ``True`` if ``string`` is an *exact and complete* match for ``expression``.

  .. seealso:: :doc:`form-regex`

  .. container:: details
    
    .. include:: incl/form-examples/regex-middle-initial.rst


.. function:: contains(string, substring)

  Returns ``True`` if the ``string`` contains the ``substring``.

.. function:: starts-with(string, substring)

  Returns ``True`` if ``string`` begins with ``substring``.

.. function:: ends-with(string, substring)

  Returns ``True`` if the ``string`` ends with ``substring``.


.. function:: substr(string, start[, end]) 	

  Returns the substring of ``string`` beginning at the index ``start`` and extending to (but not including) index ``end`` (or to the termination of ``string``, if ``end`` is not provided). Members of ``string`` are zero-indexed.
  
.. function:: substring-before(string, target)

  Returns the substring of ``string`` *before* the first occurrence of the ``target`` substring. If the ``target`` is not found, or ``string`` begins with the ``target`` substring, then this will return an empty string.

.. function:: substring-after(string, target)

  Returns the substring of ``string`` *after* the first occurrence of the ``target`` substring. If the ``target`` is not found this will return an empty string.

.. function:: translate(string, fromchars, tochars)

  Returns a copy of ``string``, where every occurrence of a character in ``fromchars`` is replaced by the corresponding character in ``tochars``. If ``fromchars`` is longer than ``tochars`` then every occurrence of a character in ``fromchars`` that does not have a corresponding character in ``tochars`` will be removed.

.. function:: string-length(string)

  Returns the number of characters in ``string``. If no value is passed in, returns the number of characters in the value of the question that this function call is tied to which can be useful in a ``constraint`` expression.

.. function:: normalize-space(string)

  Returns a string with normalized whitespace by stripping leading and trailing whitespace of ``string`` and replacing sequences of whitespace characters with a single space. If no value is passed in, normalizes whitespace of the value of the question that this function call is tied to.
  
.. _string-combination-functions:
  
Combining strings
~~~~~~~~~~~~~~~~~~  

.. function:: concat(arg [, arg [, arg [, arg [...]]]])

  Concatenates one or more arguments into a single string. If any ``arg`` is a :term:`nodeset`, the values within the set are concatenated into a string.

  
.. function:: join(separator, nodeset)

  Joins the members of ``nodeset``, using the string ``separator``.

.. _string-conversion-functions:
  
Converting to and from strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: boolean-from-string(string)

  Returns ``True`` if ``string`` is "true" or "1".
  Otherwise, ``False``.

.. function:: string(arg)

   Converts ``arg`` to a string.

.. _math-functions:
  
Math 
------

.. warning::

  Math functions (except :func:`number`) only work with number values.
  
  You can use :func:`number` to convert a string of digits to a number,
  but it is usually better to :ref:`get a number value directly <number-widgets>`.
  
  Empty values 
  (that is, :ref:`variables <variables>` referencing unanswered questions)
  are actually empty strings, 
  :ref:`and will not be automatically converted to zero (0) <empty-values>`.
  
.. _number-functions:

Number handling
~~~~~~~~~~~~~~~~~

.. function:: round(number, places)

  Rounds a decimal ``number`` to some number of decimal ``places``.

.. function:: int(number) 	

  Truncates the fractional portion of a decimal ``number`` to return an integer.

.. function:: number(arg)

  Converts ``arg`` to number value.
  
  If ``arg`` is a string of digits, returns the number value.
  
  If ``arg`` is ``True``, returns 1. If ``arg`` is ``False``, returns 0.
  
  If ``arg`` cannot be converted, returns ``NaN`` (not a number).

.. function:: digest(data, algorithm, encoding method (optional))   

  Computes and returns the hash value of the data ``string`` using the indicated hash algorithm ``string``, and encoding this hash value using the optional encoding ``string``.
  
  Options for the algorithm are ``MD5``, ``SHA-1``, ``SHA-256``, ``SHA-384``, ``SHA-512``. 
  
  If the third parameter is not specified, the encoding is ``base64``. Valid options for the encoding are ``base64`` and ``hex``.

  This function can be useful if, for example, someone wants to build a unique identifier from sensitive data like a national ID number without compromising that data.
  
.. seealso:: :func:`count`, :func:`max`, :func:`min`, :func:`number`

.. function:: base64-decode(string)

  Decodes all bytes from the input using the Base64 encoding scheme, assuming that the encoded bytes represent UTF-8 characters. Returns a UTF-8 character string.
  
.. _calculation-functions:
  
Calculation
~~~~~~~~~~~~~

.. function:: pow(number, power)

  Raises a ``number`` to a ``power``.

.. function:: log(number)

  Returns the natural log of ``number``.

.. function:: log10(number)

  Returns the base-10 log of ``number``.

.. function:: abs(number)

  Returns the absolute value of ``number``.

.. function:: sin(number)

  Returns the sine of ``number``.

.. function:: cos(number)

  Returns the cosine of ``number``.
  
.. function:: tan(number)

  Returns the tangent of ``number``.

.. function:: asin(number)

  Returns the arc sine of ``number``.
  
.. function:: acos(number)

  Returns the arc cosine of ``number``.

.. function:: atan(number)

  Returns the arctan of ``number``.

.. function:: atan2(y,x)

  Returns the multi-valued inverse tangent of ``y``, ``x``.

.. function:: sqrt(number) 

  Returns the square root of ``number``.

.. function:: exp(x) 

  Returns ``e^x``.

.. function:: exp10(x)

  Returns ``10^x``.

.. function:: pi()

  Returns an approximation of the mathematical constant π.

  
.. _date-time-functions:
    
Date and time
----------------

.. function:: today()

  Returns the current date without a time component.

.. function:: now()

  Returns the current datetime in `ISO 8601 format`_, including the timezone.
  
  .. _ISO 8601 format: https://en.wikipedia.org/wiki/ISO_8601

  .. warning::

    This function is often misused. Read :ref:`when expressions are evaluated <when-expressions-are-evaluated>` to learn more.

.. _date-time-conversion-functions:
  
Converting dates and time
~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
.. function:: decimal-date-time(dateTime)

  Converts ``dateTime`` value to the number of days since January 1, 1970 (the `Unix Epoch`_).
  
  This is the inverse of :func:`date`.

.. function:: date(days)

  Converts an integer representing a number of ``days`` from January 1, 1970 (the `Unix Epoch`_) to a standard date value.

  .. _Unix Epoch: https://en.wikipedia.org/wiki/Unix_time
    
  This is the inverse of :func:`decimal-date-time`.

    
.. function:: decimal-time(time)

  Converts ``time`` to a number representing a fractional day.
  For example, noon is 0.5 and 6:00 PM is 0.75.


.. _date-time-formatting-functions:

Formatting dates and times for display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
  
.. function:: format-date(date, format)

  Returns ``date`` as a string formatted as defined by ``format``.
  
  .. container:: details
  
    The following identifiers are used in the ``format`` string:

    .. csv-table::

      %Y, 4-digit year
      %y, 2-digit year
      %m, 0-padded month
      %n, numeric month
      %b, "short text month (Jan, Feb, Mar...)" 
      %d, 0-padded day of month
      %e, day of month
      %a, "short text day (Sun, Mon, Tue...)."

    .. note:: 
    
      Month and day abbreviations are language and locale specific. If form locale can be determined, that locale will be used. Otherwise, the device locale will be used.
  
.. function:: format-date-time(dateTime, format)

  Returns ``dateTime`` as a string formatted as defined by ``format``.

  .. container:: details
  
    The identifiers list in :func:`format-date` are available, 
    plus the following:

    .. csv-table::

      %H, 0-padded hour (24-hr time)
      %h, hour (24-hr time)
      %M, 0-padded minute
      %S, 0-padded second
      %3, 0-padded millisecond ticks.

.. _geography-functions:
    
Geography
------------

.. function:: area(nodeset | geoshape) 	

  Returns the area, in square meters, 
  of either a ``nodeset`` of geopoints or a ``geoshape`` value.
  
  It takes into account the circumference of the Earth around the Equator but does not take altitude into account.
  
.. function:: distance(nodeset | geoshape | geotrace)

  Returns the distance, in meters, of either:
  
  - a ``nodeset`` of geopoints

  .. csv-table:: survey
    :header: type, name, label, calculation

    begin_repeat, points,
    geopoint, point, Record a Geopoint
    end_repeat, ,
    calculate, calculated_distance, , distance(${point})
    note, display_distance, Calculated distance: ${calculated_distance}

  - the perimeter of a ``geoshape``

  .. csv-table:: survey
    :header: type, name, label, calculation

    geoshape, shape, Record a Geoshape
    calculate, calculated_distance, , distance(${shape})
    note, display_distance, Calculated distance: ${calculated_distance}
    
  - the length of a ``geotrace`` value

  .. csv-table:: survey
    :header: type, name, label, calculation

    geotrace, trace, Record a Geotrace
    calculate, calculated_distance, , distance(${trace})
    note, display_distance, Calculated distance: ${calculated_distance}

  - concatenated geopoints

  .. csv-table:: survey
    :header: type, name, label, calculation

    geopoint, point1, Record a Geopoint
    geopoint, point2, Record a Geopoint
    calculate, concatenated_points, , "concat(${point1},' ; ', ${point2})"
    calculate, calculated_distance, , distance(${concatenated_points})
    note, display_distance, Calculated distance: ${calculated_distance}
  
  It takes into account the circumference of the Earth around the Equator and does not take altitude into account.

.. _utility-functions:

Utility
---------

.. function:: random()

  Returns a random number between 0.0 (inclusive) and 1.0 (exclusive).

  .. warning::

    This function is often misused. Read :ref:`when expressions are evaluated <when-expressions-are-evaluated>` to learn more.


.. function:: randomize(nodeset[, seed]) 	

  Returns a shuffled ``nodeset``.
  
  A shuffle with a numeric ``seed`` is deterministic and reproducible.
  
  The primary use for this function is to randomize the order of choices for a select question. The :ref:`documentation on select widgets <randomize-choice-order>` describes how this is done in XLSForm.

  :func:`randomize` can only be used in a context where a ``nodeset`` is accepted. Note that questions of type **calculate** cannot reference a ``nodeset``.
    
.. function:: uuid([length]) 	

  Without argument, returns a random `RFC 4122 version 4 compliant UUID`__. 
  
  __ https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
  
  With an argument it returns a random GUID of specified ``length``.  

    
.. function:: boolean(arg) 

  Returns ``True`` if ``arg`` is:
  
  - a number other than zero
  - a non-empty string
  - a non-empty collection
  - a comparison or expressions that evaluates to ``True``.
   
  Returns ``False`` if ``arg`` is:
  
  - the number 0
  - an empty string
  - an empty collection
  - a comparison or expression that evaluates to ``False``.

    
.. function:: not(arg)

  Returns the opposite of :func:`boolean(arg) <boolean>`.

  
.. function:: coalesce(arg1, arg2)

  Returns first non-empty value of the two ``arg``\ s.
  Returns an empty string if both are empty or non-existent.

  
.. function:: checklist(min, max, response[, response[, response [, ... ]]])

  Returns ``True`` if the number of ``response``\ s that are exactly the string "yes" is between ``min`` and ``max``, inclusive.  
  
  Set ``min`` or ``max`` to ``-1`` to make the argument not applicable.

.. function:: weighted-checklist(min, max, reponse, weight[, response, weight[, response, weight[, response, weight[, ... ]]])

  Returns ``True`` if 
  the sum of the ``weight``\ s 
  of each ``response`` that is exactly the string "yes"
  is between ``min`` and ``max``, inclusive.
  
  Set ``min`` or ``max`` to ``-1`` to make the argument not 

  
.. function:: true()

  Evaluates to ``True``.

.. function:: false()

  Evaluates to ``False``.
  
  
