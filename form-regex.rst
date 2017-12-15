Using regular expressions
============================

.. _regex:

Regular Expressions
---------------------

A regular expression is a special text string for describing a search pattern. Some basic operations on regular expressions are:

1. **Boolean or**: A vertical bar separates alternatives. For example, *gray|grey* can match *gray* or *grey*. 
2. **Grouping Parentheses**: They are used to define the scope and precedence of the operators. For example, *gray|grey* and *gr(a|e)y* are equivalent patterns which both describe the set of *gray* or *grey*.
3. **Quantification**: A quantifier after a token (such as a character) or group specifies how often that preceding element is allowed to occur. 

    - Square brackets indicate the occurrence of elements within. For example, **[abc]** matches either a, b or c character, **[a-g]** matches any character from a to g, **[^abc]** matches any character except a,b or c.
    - The question mark indicates zero or one occurrence of the preceding element. For example, **colou?r** matches both *color* and *colour*.
    - The asterisk indicates zero or more occurrences of the preceding element. For example, **ab*c** matches *ac*, *abc*, *abbc*, *abbbc*, and so on.
    - The plus sign indicates one or more occurrences of the preceding element. For example, **ab+c** matches *abc*, *abbc*, *abbbc*, and so on, but not *ac*.
    - {n}: The preceding item is matched exactly n times. 
    - {min,}:	The preceding item is matched min or more times. 
    - {min,max}: The preceding item is matched at least min times, but not more than max times. 


For more details on regular expressions, refer `this site <https://regex101.com/>`_.   

.. _tips-on-regex:

Tips on using regular expressions
----------------------------------

- Regular expressions only apply to **strings**. The function used is of the form: ``regex(string value, string expression)`` where it returns the result of regex test on provided value. 

- Be careful while setting limits on length of a constraint.
  For example, if you want to restrict an input to a maximum of six alphabets, you can do so as follows:

 In **XLSForm**:

 .. csv-table:: **Survey**
   :header: "type", "name", "label", "constraint", "constraint_message"
   :widths: auto

   "text", "ex", "Enter example", "regex(.,'^[a-zA-Z]{0,6}$')", "Input can have a maximum of 6 characters."

 In **XForm XML**:

 .. code-block:: xml

   <bind constraint="Regex(.,'^[a-zA-Z]{0,6}$')" jr:constraintMsg="Input can have a maximum of 6 characters." nodeset="/regex_ex/ex" type="string"/>

   <input ref="/regex_ex/ex">
      <label>Enter example</label>
    </input>

 Instead if you used a constraint of the form ``regex(.,'^[a-zA-Z]{6}$')``, it would require an input of exactly six characters.

 .. note::

   **^**  and **$** denote start and end of string respectively.

- If you want to use a regular expression constraint on a number, first of all, make sure that the type of your question is **text** and appearance is **numbers** and then apply the constraint. 

 For example, to restrict the telephone numbers to have exactly 10 digits:

 In **XLSForm**:

 .. csv-table:: **Survey**
   :header: "type", "name", "label", "constraint", "constraint_message", "appearance"
   :widths: auto

   "text", "tel_no", "Enter your Telephone number", "regex(.,'^[0-9]{10}$')", "Telephone numbers should have 10 digits", "numbers"

 In **XForm XML**:

 .. code-block:: xml
     
   <bind constraint="Regex(.,'^[0-9]{10}$')" jr:constraintMsg="Telephone numbers should have 10 digits" nodeset="/regex_ex/tel_no" type="string"/> 
   
   <input appearance="numbers" ref="/regex_ex/tel_no">
      <label>Enter your Telephone number"</label>
   </input>

 .. note::

   - An other alternative to this would be to use a regular expression of the form: ``regex(string(.),'...')``. But this should be avoided since the value of *string(.)* would be after whatever you entered was converted to an integer. So if you entered 0004, string(.) would be just 4.
   - Remember that integers are limited by binary representation to 9 decimal digits. If you want something longer (e.g., 10 numbers) then make sure to use a text type with appearance as numbers.  
   - Appearance setting changes the Keyboard style of the pop-up keyboard to the number keyboard when you attempt to enter data into the field. It does not prevent non-numbers from being entered. This relies upon the device's keyboard supporting (See `this <http://developer.android.com/reference/android/text/InputType.html#TYPE_NUMBER_FLAG_SIGNED>`_). You need to add a constraint restricting the input string to be a number. 

- Avoid using complex regex patterns as that may cause stack overflow crashes. Also, avoid placing constraints on names since your regex will certainly not capture all the punctuation or random characters that names can contain.  

