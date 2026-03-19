Using regular expressions
============================

.. _regex:

Regular Expressions
---------------------

A regular expression is a special text string for describing a search pattern. You can use the :func:`regex` function in your forms to set constraints on the structure of text data input by the user.

For example, if you ask users to input codes that look like ``CAR_PRC_2015_048``, the following constraint expression would validate that structure:

.. code-block::

  regex(.,'^[A-Z]{3}+_+[A-Z]{3}+_+[0-9]{4}+_+[0-9]{3,4}$')

.. tip::

  Only ask users to type in complex codes if absolutely necessary. Consider instead building the code from the values of multiple other fields. For example, the code above could be calculated by having the user select administrative levels from friendly dropdowns, the year could be computed from metadata, and the user might be prompted for a serial code.

Some basic operations on regular expressions are:

.. startignore

#. **Boolean or**: A vertical bar separates alternatives. For example, ``gray|grey`` can match gray or grey.

#. **Grouping parentheses**: They are used to define the scope and precedence of the operators. For example, ``gray|grey`` and ``gr(a|e)y`` are equivalent patterns which both describe the set of gray or grey.

#. **Character classes**: Square brackets define a set of characters, any one of which can match at a given position.

   - ``[abc]`` matches either a, b, or c.
   - ``[a-g]`` matches any character from a to g.
   - ``[^abc]`` matches any character except a, b, or c.

#. **Quantification**: A quantifier after a character, character class, or group specifies how often that preceding element is allowed to occur.

   - The question mark indicates zero or one occurrence of the preceding element. For example, ``colou?r`` matches both color and colour.
   - The asterisk indicates zero or more occurrences of the preceding element. For example, ``ab*c`` matches ac, abc, abbc, abbbc, and so on.
   - The plus sign indicates one or more occurrences of the preceding element. For example, ``ab+c`` matches abc, abbc, abbbc, and so on, but not ac.
   - ``{n}``: The preceding item is matched exactly n times. 
   - ``{min,}``: The preceding item is matched min or more times. 
   - ``{min,max}``: The preceding item is matched at least min times, but not more than max times.

.. endignore

For a clear understanding of regular expressions, try these regex online checker tools: 

- https://regex101.com/
- https://www.regextester.com/
- https://regexr.com/

.. _tips-on-regex:

Tips on using regular expressions
----------------------------------

- Regular expressions only apply to **strings**. The function used is of the form: ``regex(string value, string expression)`` where it returns the result of regex test on provided value. If the result is true, the input value is valid and satisfies the constraint. If the result is false, input value is not valid and user may need to re-enter the input. The regex function will be placed in the constraints column in your XLSForm. 

- Be careful while setting limits on length of a constraint.
  For example, if you want to restrict a text input to a maximum of six alphabetic characters, you can do so as follows:

 In **XLSForm**:

 .. csv-table:: **Survey**
   :header: "type", "name", "label", "constraint", "constraint_message"
   :widths: auto

   "text", "ex", "Enter example", "regex(.,'^[a-zA-Z]{0,6}$')", "Input can have a maximum of 6 alphabetic characters."

 Instead if you used a constraint of the form ``regex(.,'^[a-zA-Z]{6}$')``, it would require an input of exactly six alphabetic characters.

 .. note::

  - ``.`` denotes the input string.
  - ``^`` and ``$`` denote start and end of string respectively.

- If you want to use a regular expression constraint on a number, make sure that the type of your question is **text** and appearance is **numbers** and then apply the constraint.

 The following example will validate a 10-digit North American telephone number. Separators are not required, but can include spaces, hyphens, or periods. Parentheses around the area code are also optional.

 In **XLSForm**:

 .. csv-table:: **Survey**
   :header: "type", "name", "label", "constraint", "constraint_message", "appearance"
   :widths: auto

   "text", "tel_no", "Enter your Telephone number", "regex(.,'^(([0-9]{1})*[- .(]*([0-9]{3})[- .)]*[0-9]{3}[- .]*[0-9]{4})+$')", "Telephone numbers should have 10 digits with optional separators.", "numbers"
   
- Integers are limited by binary representation to 9 decimal digits. If you want something longer (like 10 numbers) then make sure to use a text type with appearance as numbers and add a constraint restricting the input string to be a number. Constraint is required since appearance setting changes the keyboard style of the pop-up keyboard to the number keyboard when you attempt to enter data into the field but does not prevent non-numbers from being entered. This relies upon the device's keyboard supporting (See `this <http://developer.android.com/reference/android/text/InputType.html#TYPE_NUMBER_FLAG_SIGNED>`_).

 For example, a constraint of the form ``regex(.,'^[0-9]{11}$')`` will restrict the input string to be a number of exactly 11 digits.

.. note::

  Avoid placing restrictive constraints on proper nouns. These can have a wide range of structures with punctuation or characters that you may not expect. Exhaustive regex on proper nouns are often error-prone and hard to maintain.
  
  In general, complex regex patterns may cause stack overflow crashes.

.. seealso::

  You can refer `this list <https://gist.github.com/nerdsrescueme/1237767>`_ for various common regex patterns.

