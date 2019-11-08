.. spelling::

  Anaranjado
  Azul
  Colores
  Español
  Nodesets
  Púrpura
  Qué
  Rojo
  Seleccione
  arctan
  arg
  bday
  bp
  br
  chkn
  colores
  fsh
  gustan
  jr
  nodeset
  prefs
  seleccionados
  te
  tres
  π
  
  
	
******************************
Form Operators and Functions
******************************

:ref:`expressions` in :ref:`calculations <calculations>`, :ref:`constraints <constraints>`, and :ref:`relevants <relevants>`
can contain operators and functions.

.. contents::
  :local:   
  :depth: 2
    
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
  \.\., current question's parent group, position(..), Used with :func:`position` to get the iteration index.

.. note:: 

  Formally, these are not operators but rather XPath references 
  to the current node (``..``) and the containing node (``.``). 
  `XPath paths`_ can be used to reference nodes of a form.
  
  .. _XPath paths: https://opendatakit.github.io/xforms-spec/#xpath-paths
    
  
.. _form-functions:
  
Functions
===========

.. contents::
  :local:
    
.. seealso:: `Functions in the ODK XForm Specification <https://opendatakit.github.io/xforms-spec/#xpath-functions>`_

    
.. _control-flow-functions:

Control flow
--------------

.. function:: if(expression, then, else)

  Returns :arg:`then` if :arg:`expression` evaluates to ``True``. 
  Otherwise, returns :arg:`else`.

  
  
.. function:: position(xpath)

  Returns an integer equal to the 1-indexed position of the current node
  within the node defined by :arg:`xpath`.
  
  Most often this is used in the form :tc:`position(..)`
  to identify the current iteration index
  within a repeat group.  
  
  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst

.. function:: once(expression)

  Returns the value :arg:`expression` if the question's value is empty.
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

  Returns ``True`` if :arg:`string` 
  is a member of :arg:`space_delimited_array`,
  otherwise returns ``False``.
  
  Commonly used to determined if a specific choice was selected
  in a :ref:`select question <select-widgets>`. 
  (This is possible because 
  a :ref:`reference to <variables>` a select question
  returns a space-delimited array of choice names.)

  .. container:: details
      
    .. include:: incl/form-examples/constraint-on-selected.rst
  
.. function:: selected-at(space_delimited_array, n)

  Returns the string at the :arg:`n`\ :sup:`th` position 
  of the :arg:`space_delimited_array`.
  (The array is zero-indexed.)
  Returns an empty string if the index does not exist.  
  
  This can be used to get the :th:`name` of a selected choice 
  from a :ref:`multi-select question <multi-select-widget>`.
  (This is possible because 
  a :ref:`reference to <variables>` a select question
  returns a space-delimited array of choice names.)
  
  .. note::
  
    If used to get a choice name from a select question,
    this function returns the :th:`name`, not the :th:`label`,
    of the selected choice.
    To get the label in the current language,
    use :func:`jr:choice-name`.
  
  .. container:: details
  
    .. image:: /img/form-functions/selected-at-0.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" Several color names are presented as options. Red, Green, and Purple are selected.

    .. image:: /img/form-functions/selected-at-1.* 
      :alt: A note widget in Collect. The label is "Selected Colors". The hint text is "red, green, purple".

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
  
    .. image:: /img/form-functions/count-selected-constraint.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" The hint text is "Select three." Four colors are selected. A message modal overlays the widget with the text "Select exactly three."

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

  Returns the label value, in the active language, associated with the :arg:`choice_name` in the list of choices for the :arg:`select_question`.
  
  .. note::
  
    You have to wrap the :arg:`select_question` reference in quotes.
    
    .. code-block:: none
    
      '${question_name}'
      
  .. container:: details  
  
    .. image:: /img/form-functions/choice-name-multi-lang-english-0.* 
      :alt: A multi-select widget in Collect. The label is "What colors do you like?" Several color names are presented as options. Red, Green, and Purple are selected.

    .. image:: /img/form-functions/choice-name-multi-lang-english-1.* 
      :alt: A note widget in Collect. The label is "Selected colors". The hint text is "Red, Green, Purple."

    .. image:: /img/form-functions/choice-name-multi-lang-spanish-0.* 
      :alt: A multi-select widget in Collect. The label is "¿Qué colores te gustan?" Several color names, in Spanish, are presented as options. Rojo, Verde, and Púrpura are selected.

    .. image:: /img/form-functions/choice-name-multi-lang-spanish-1.* 
      :alt: A note widget in Collect. The label is "Colores seleccionados." The hint text is "Rojo, Verde, Púrpura".

    .. rubric:: XLSForm

    .. csv-table::  survey
      :header: type, name, label::English, label::Español, hint::English, hint:Español, calculation

      select_multiple colors, color_prefs, What colors do you like?, ¿Qué colores te gustan?, Select three., Seleccione tres.
      calculate, color_0, , , , ,"jr:choice-name( selected-at(${color_prefs}, 0), '${color_prefs}')"
      calculate, color_1, , , , ,"jr:choice-name( selected-at(${color_prefs}, 2), '${color_prefs}')"
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
      
      Nodesets can also be created by joining two or more nodes with pipes: :tc:`/data/age | /data/name`.

        
.. function:: indexed-repeat(name, group, i [, sub_grp, sub_i [, sub_sub_grp, sub_sub_i ]])

  Returns the response value of question :arg:`name`
  from the repeat-group :arg:`group`,
  in iteration :arg:`i`.
  
  Nested repeat groups can be accessed 
  using the :arg:`sub` and :arg:`sub_sub` parameters.

  .. seealso:: :ref:`referencing-answers-in-repeats`

  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst

.. function:: count(nodeset)

  Returns the number of items in :arg:`nodeset`. This can be used to count the number of repetitions in a :ref:`repeat group <repeats>`.

  .. container:: details
  
    .. include:: incl/form-examples/parallel-repeats.rst
  
.. function:: count-non-empty(nodeset)

  Returns the number of non-empty members of :arg:`nodeset`.

.. function:: sum(nodeset)

  Returns the sum of the members of :arg:`nodeset`.
  
  Can be used to :ref:`tally responses to a repeated select question <counting-answers>`.
  
  .. container:: details
  
    .. include::  incl/form-examples/sum-to-count-responses.rst

.. function:: max(nodeset)

  Returns the largest member of :arg:`nodeset`.
  
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

  Returns the smallest member of :arg:`nodeset`.

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

    Returns ``True`` if :arg:`string` is an *exact and complete* match for :arg:`expression`.

  .. seealso:: :doc:`form-regex`

  .. container:: details
    
    .. include:: incl/form-examples/regex-middle-initial.rst


.. function:: contains(string, substring)

  Returns ``True`` if the :arg:`string` contains the :arg:`substring`.

.. function:: starts-with(string, substring)

  Returns ``True`` if :arg:`string` begins with :arg:`substring`.

.. function:: ends-with(string, substring)

  Returns ``True`` if the :arg:`string` ends with :arg:`substring`.


.. function:: substr(string, start[, end]) 	

  Returns the substring of :arg:`string` beginning at the index :arg:`start` and extending to (but not including) index :arg:`end` (or to the termination of :arg:`string`, if :arg:`end` is not provided). Members of :arg:`string` are zero-indexed.
  
.. function:: substring-before(string, target)

  Returns the substring of :arg:`string` *before* the first occurrence of the :arg:`target` substring. If the :arg:`target` is not found, or :arg:`string` begins with the :arg:`target` substring, then this will return an empty string.

.. function:: substring-after(string, target)

  Returns the substring of :arg:`string` *after* the first occurrence of the :arg:`target` substring. If the :arg:`target` is not found this will return an empty string.

.. function:: translate(string, fromchars, tochars)

  Returns a copy of :arg:`string`, where every occurrence of a character in :arg:`fromchars` is replaced by the corresponding character in :arg:`tochars`. If :arg:`fromchars` is longer than :arg:`tochars` then every occurrence of a character in :arg:`fromchars` that does not have a corresponding character in :arg:`tochars` will be removed.

.. function:: string-length(string)

  Returns the number of characters in :arg:`string`.

.. function:: normalize-space(string)

  Returns a string with normalized whitespace by stripping leading and trailing whitespace of :arg:`string` and replacing sequences of whitespace characters with a single space.
  
.. _string-combination-functions:
  
Combining strings
~~~~~~~~~~~~~~~~~~  

.. function:: concat(arg [, arg [, arg [, arg [...]]]])

  Concatenates one or more arguments into a single string. If any :arg:`arg` is a :term:`nodeset`, the values within the set are concatenated into a string.

  
.. function:: join(separator, nodeset)

  Joins the members of :arg:`nodeset`, using the string :arg:`separator`.

.. _string-conversion-functions:
  
Converting to and from strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: boolean-from-string(string)

  Returns ``True`` if :arg:`string` is "true" or "1".
  Otherwise, ``False``.

.. function:: string(arg)

   Converts :arg:`arg` to a string.

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

  Rounds a decimal :arg:`number` to some number of decimal :arg:`places`.

.. function:: int(number) 	

  Truncates the fractional portion of a decimal :arg:`number` to return an integer.

.. function:: number(arg)

  Converts :arg:`arg` to number value.
  
  If :arg:`arg` is a string of digits, returns the number value.
  
  If :arg:`arg` is ``True``, returns 1. If :arg:`arg` is ``False``, returns 0.
  
  If :arg:`arg` cannot be converted, returns ``NaN`` (not a number).

.. function:: digest(data, algorithm, encoding method (optional))   

  Computes and returns the hash value of the data :arg:`string` using the indicated hash algorithm :arg:`string`, and encoding this hash value using the optional encoding :arg:`string`.
  
  Options for the algorithm are :arg:`MD5`, :arg:`SHA-1`, :arg:`SHA-256`, :arg:`SHA-384`, :arg:`SHA-512`. 
  
  If the third parameter is not specified, the encoding is :arg:`base64`. Valid options for the encoding are :arg:`base64` and :arg:`hex`.

  This function can be useful if, for example, someone wants to build a unique identifier from sensitive data like a national ID number without compromising that data.
  
.. seealso:: :func:`count`, :func:`max`, :func:`min`, :func:`number`
  
.. _calculation-functions:
  
Calculation
~~~~~~~~~~~~~

.. function:: pow(number, power)

  Raises a :arg:`number` to a :arg:`power`.

.. function:: log(number)

  Returns the natural log of :arg:`number`.

.. function:: log10(number)

  Returns the base-10 log of :arg:`number`.

.. function:: abs(number)

  Returns the absolute value of :arg:`number`.

.. function:: sin(number)

  Returns the sine of :arg:`number`.

.. function:: cos(number)

  Returns the cosine of :arg:`number`.
  
.. function:: tan(number)

  Returns the tangent of :arg:`number`.

.. function:: asin(number)

  Returns the arc sine of :arg:`number`.
  
.. function:: acos(number)

  Returns the arc cosine of :arg:`number`.

.. function:: atan(number)

  Returns the arctan of :arg:`number`.

.. function:: atan2(y,x)

  Returns the multi-valued inverse tangent of :arg:`y`, :arg:`x`.

.. function:: sqrt(number) 

  Returns the square root of :arg:`number`.

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

  Converts :arg:`dateTime` value to the number of days since January 1, 1970 (the `Unix Epoch`_).
  
  This is the inverse of :func:`date`.

.. function:: date(days)

  Converts an integer representing a number of :arg:`days` from January 1, 1970 (the `Unix Epoch`_) to a standard date value.

  .. _Unix Epoch: https://en.wikipedia.org/wiki/Unix_time
    
  This is the inverse of :func:`decimal-date-time`.

    
.. function:: decimal-time(time)

  Converts :arg:`time` to a number representing a fractional day.
  For example, noon is 0.5 and 6:00 PM is 0.75.


.. _date-time-formatting-functions:

Formatting dates and times for display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
  
.. function:: format-date(date, format)

  Returns :arg:`date` as a string formatted as defined by :arg:`format`.
  
  .. container:: details
  
    The following identifiers are used in the :arg:`format` string:

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

  Returns :arg:`dateTime` as a string formatted as defined by :arg:`format`.

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
  of either a :arg:`nodeset` of geopoints or a :arg:`geoshape` value.
  
  It takes into account the circumference of the Earth around the Equator but does not take altitude into account.

.. function:: distance(nodeset | geoshape | geotrace)

  Returns the distance, in meters, of either:
  
  - a :arg:`nodeset` of geopoints
  - the perimeter of a :arg:`geoshape`
  - the length of a :arg:`geotrace` value
  
  It takes into account the circumference of the Earth around the Equator and does not take altitude into account.

.. _utility-functions:

Utility
---------

.. function:: random()

  Returns a random number between 0.0 (inclusive) and 1.0 (exclusive).

  .. warning::

    This function is often misused. Read :ref:`when expressions are evaluated <when-expressions-are-evaluated>` to learn more.


.. function:: randomize(nodeset[, seed]) 	

  Returns a shuffled :arg:`nodeset`.
  
  A shuffle with a numeric :arg:`seed` is deterministic and reproducible.
  
  The primary use for this function is to randomize the order of choices for a select question. The :ref:`documentation on select widgets <randomize-choice-order>` describes how this is done in XLSForm.

  :func:`randomize` can only be used in a context where a :arg:`nodeset` is accepted. Note that questions of type **calculate** cannot reference a :arg:`nodeset`.
    
.. function:: uuid([length]) 	

  Without argument, returns a random `RFC 4122 version 4 compliant UUID`__. 
  
  __ https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)
  
  With an argument it returns a random GUID of specified :arg:`length`.  

    
.. function:: boolean(arg) 

  Returns ``True`` if :arg:`arg` is:
  
  - a number other than zero
  - a non-empty string
  - a non-empty collection
  - a comparison or expressions that evaluates to ``True``.
   
  Returns ``False`` if :arg:`arg` is:
  
  - the number 0
  - an empty string
  - an empty collection
  - a comparison or expression that evaluates to ``False``.

    
.. function:: not(arg)

  Returns the opposite of :func:`boolean(arg) <boolean>`.

  
.. function:: coalesce(arg, arg) 	

  Returns first non-empty value of the two :arg:`arg`\ s.
  Returns an empty string if both are empty or non-existent.

  
.. function:: checklist(min, max, response[, response[, response [, ... ]]])

  Returns ``True`` if the number of :arg:`response`\ s that are exactly the string "yes" is between :arg:`min` and :arg:`max`, inclusive.  
  
  Set :arg:`min` or :arg:`max` to ``-1`` to make the argument not applicable.

.. function:: weighted-checklist(min, max, reponse, weight[, response, weight[, response, weight[, response, weight[, ... ]]])

  Returns ``True`` if 
  the sum of the :arg:`weight`\ s 
  of each :arg:`response` that is exactly the string "yes"
  is between :arg:`min` and :arg:`max`, inclusive.
  
  Set :arg:`min` or :arg:`max` to ``-1`` to make the argument not 

  
.. function:: true()

  Evaluates to ``True``.

.. function:: false()

  Evaluates to ``False``.
  
  
