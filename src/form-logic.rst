.. spelling::
 
  ap
  ar
  bp
  datetime
  dir
  fave
  gndr
  kwame
  Kwame
  mngr
  onwuachi
  Onwuachi
  sophia
  timestamp
  timestamping
  dateTime

***********
Form Logic
***********

:doc:`collect-intro` supports a wide range of dynamic form behavior. 
This document covers how to specify this behavior
in your `XLSForm`_ definition.

.. seealso:: `XLSForm`_

.. _XLSForm: http://xlsform.org/

.. warning::

  Relevance, constraint and calculation evaluation :ref:`within the same screen <field-list>` is supported in Collect v1.22 and later. In earlier versions of Collect, questions tied by logic must be displayed on different screens.

.. contents:: :depth: 2
 :local:

Form logic building blocks
============================


 .. _variables:

Variables
-----------

Variables reference the value of previously answered questions.
To use a variable in XLSForm,
put the question's :th:`name` in curly brackets preceded by a dollar sign:

:tc:`${question-name}`

Variables can be used in 
:th:`label`, :th:`hint`, and :th:`repeat_count` columns, 
as well as any column that accepts an :ref:`expression <expressions>`.

.. image:: /img/form-logic/variables-0.* 
  :alt: A text widget in Collect. The question is "What is your name?" The entry field has the value "Adam".
  
.. image:: /img/form-logic/variables-1.* 
  :alt: A note widget in Collect. The text is "Hello, Adam."
  

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
  
  text, your_name, What is your name?
  note, hello_name, "Hello, ${your_name}."

You can also refer to the current question or to the current question's parent group or repeat:

.. csv-table::
  :header: , Explanation, Example, Notes
  
  ., current question's value, . >= 18, Used in :ref:`constraints <constraints>`.
  \.\., current question's parent group, position(..), Used with :func:`position` to get the iteration index.

.. _xpath-paths:

Advanced: XPath paths
~~~~~~~~~~~~~~~~~~~~~~

The ``${}`` notation in XLSForm is a convenient shortcut to refer to a specific field. When an XLSForm is converted, ``${}`` references are expanded to XPath paths which specifically describe where the field is located in the form.

Some tools like ODK Build do not support ``${}`` notation so raw XPath notation must be used. Even in XLSForm, it can be advantageous to use raw XPath notation, especially in the context of repeats or to query datasets. The ``${}`` and XPath notations can be mixed freely.

One way to think about XPath is that it sees a form or dataset like a series of folders and files on your computer. :ref:`Groups <groups>` and :ref:`repeats <repeats>` are like folders because they can contain other elements. Fields are like files and can't contain any other elements. Imagine a form with a group with name ``my_group`` which contains another group with name ``inner_group`` which contains a question with name ``q1``. The absolute path to ``q1`` is ``/data/my_group/inner_group/q1``.

The ``/data/`` in the example above indicates that this is an absolute path for an element of the form itself (as opposed to a dataset, for example). This root is named ``data`` by default but can be modified by adding a :th:`name` column in the XLSForm **settings** sheet and specifying a value below it. This is rarely needed.

XPath paths can also be relative. For example, let's say there's a ``relevance`` expression for ``q1`` in the example above and that this expression refers to a question with name ``eligible`` in the ``my_group`` group. We could refer to it using an absolute expression: ``/data/my_group/eligible``. We could also write a relative expression: ``../../eligible``. The ``..`` references the parent of the current node. Since our expression is on the node ``/data/my_group/inner_group/q1``, the first ``..`` references the group ``/data/my_group/inner_group``. We want to access a node in the ``my_group`` group so we need to go up one more level with another ``..``. The XPath path ``../../`` when used in an expression for the ``/data/my_group/inner_group/q1`` node references ``/data/my_group``. We can now go into ``my_group`` and reference the question with name ``eligible``: ``../../eligible``. Relative expressions are particularly useful in the context of repeats.

ODK tools support a subset of XPath described `in the ODK XForms specification <https://getodk.github.io/xforms-spec/#xpath-paths>`_.

.. _xpath-paths-for-repeats:

XPath paths for repeats
""""""""""""""""""""""""

When a form definition includes a :ref:`repeat <repeats>`, corresponding filled forms will have 0 or more instances of that repeat. Using the file and folder analogy described above, each repeat instance is like a folder and all of these folders have the name of the :ref:`repeat <repeats>`. Repeat instances are differentiated by their index (first, second, ...).

When writing expressions within a repeat, it can be helpful to use the position of the repeat instance an enumerator is currently filling out. This can be done by using the  :func:`position` function. One context in which this is useful is if you want to first collect a roster of people or things and then ask additional questions about each of those. As shown in the example in the :func:`position`, you can use a first repeat for the roster and then a second repeat that references items in the first repeat based on their position.

Another application of expressions that use the ``position`` function is to access a preceding repeat instance. See an example of this in :ref:`dynamic defaults in repeats <dynamic-defaults-repeats>`.

It can be useful to reference all or some repeat instances from outside the repeat. XPath notation is particularly helpful for filtering repeat instances, for example to provide a summary from data collected in repeats:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation

  begin repeat, people, Person,
  int, age, Age,
  int, pet_count, How many pets does this person have?
  end repeat, people, ,

  int, total_pets, , sum(${people}[age < 18]/pet_count)
  note, total_note, Total pets owned by children: ${total_pets}

In the path expression ``${people}[age < 18]/pet_count``, ``${people}`` uses ``${}`` notation to refer to all of the instances of the repeat. There is then a filter applied in ``[ ]`` brackets that only includes repeat instances for which the specified age was below 18. The ``/pet_count`` final part of the path specifies that for every included repeat instance, the specified value for ``pet_count`` should be used. This results in a set of ``pet_count`` values that can be used by the :func:`sum` function or other :ref:`functions that take nodeset arguments <repeat-functions>`. This same expression could be used in many different contexts. For example, it could define the :ref:`relevance <relevants>` of a group if there's a section of questions that only need to be filled out if there are more than one child-owned pets in the community.

Sometimes forms may use :ref:`groups <groups>` to organize question sections within repeats. Those groups must be accounted for in expressions. Consider a slight variation on the form above:

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation

  begin repeat, people, Person,
  begin group, basics, ,
  int, age, Age,
  end group, age, ,
  begin group extras, ,
  int, pet_count, How many pets does this person have?
  end group extras, ,
  end repeat, people, ,

  int, total_pets, , sum(${people}[basics/age < 18]/extras/pet_count)
  note, total_note, Total pets owned by children: ${total_pets}

.. _expressions:
  
Expressions
-------------

An :dfn:`expression` is evaluated dynamically as a form is filled out.
It can include `XPath functions`_, `operators`_,
:ref:`values from previous responses <variables>`,
and (in some cases) :ref:`the value of the current response <constraints>`. 

.. _XPath functions: https://getodk.github.io/xforms-spec/#xpath-functions

.. _operators: https://getodk.github.io/xforms-spec/#xpath-operators

.. rubric:: Example expressions

:tc:`${bill_amount} * 0.18`
  Multiplies the previous value :tc:`bill_amount` by 18%,
  to calculate a suitable tip.
  
:tc:`concat(${first_name}, ' ', ${last_name})`
  Concatenates two previous responses with a space between them 
  into a single string.
  
:tc:`${age} >= 18`
  Evaluates to ``True`` or ``False``, 
  depending on the value of :tc:`age`.

:tc:`round(${bill_amount} * ${tip_percent} * 0.01, 2)`
  Calculates a tip amount based on two previously entered values,
  and then rounds the result to two decimal places.

Expressions are used in:

 - :ref:`calculations`
 - :ref:`constraints`
 - :ref:`relevants`


 
.. _calculations:

Calculations
-------------

To evaluate complex expressions, 
use a :tc:`calculate` row.
Put the expression to be evaluated in the :th:`calculation` column.
Then, you can :ref:`refer to the calculated value <variables>`
using the calculate row's :th:`name`.

Expressions cannot be used in :th:`label` and :th:`hint` columns,
so if you want to display calculated values to the user,
you must first use a :tc:`calculate` row and then a variable.

.. image:: /img/form-logic/calculation-0.* 
  :alt: The decimal widget in Collect. The question label is "Bill amount". The entered value is "55.88".
  
.. image:: /img/form-logic/calculation-1.* 
  :alt: A note widget in Collect the text is: "Bill: 55.88; Tip: 10.06; Total: 65.95"

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation
  
  decimal, bill_amount, Bill amount:, 
  calculate, tip_18, , "round((${bill_amount} * 0.18),2)"
  calculate, tip_18_total, , ${bill_amount} + ${tip_18}
  note, tip_18_note, "| Bill: $${bill_amount}
  | Tip (18%): $${tip_18}
  | Total: $${tip_18_total}",

.. _last-saved:

Values from the last saved record
----------------------------------

.. warning::

  Support for last-saved was added in Collect v1.21.0. Form conversion requires XLSForm Online ≥ v2.0.0 or pyxform ≥ v1.0.0. Using older versions will have unpredictable results.

You can refer to values from the last saved record of this form definition:

:tc:`${last-saved#question-name}`

This can be very useful when an enumerator has to enter the same value for multiple consecutive records. An example of this would be entering in the same district for a series of households.

.. rubric:: XLSForm that shows using a last-saved value as a dynamic default

.. csv-table:: survey
  :header: type, name, label, default

  text, street, Street, ${last-saved#street}

The value is pulled from the last saved record. This is often the most recently created record but it could also be a previously-existing record that was edited and saved. For the first record ever saved for a form definition, the last saved value for any field will be blank.

Questions of any type can have their defaults set based on the last saved record. References to the last saved record can be used as part of any expression wherever expressions are allowed.

.. _form-logic-gotchas:

Form logic gotchas
-------------------  

.. _when-expressions-are-evaluated:

When expressions are evaluated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every expression is constantly re-evaluated as an enumerator progresses through a form. This is an important mental model to have and can explain sometimes unexpected behavior. More specifically, expressions are re-evaluated when:

- a form is opened
- the value of any question in the form changes
- a repeat group is added or deleted
- a form is saved or finalized

This is particularly important to remember when using functions that access state outside of the form such as :func:`random` or :func:`now`. The value they represent may change as the conditions listed above take place.

To control when an expression is evaluated, use :ref:`dynamic defaults <dynamic-defaults>` or :ref:`trigger calculations on value change <triggering_calculations_on_value_change>`. Dynamic defaults are evaluated exactly once on form load or repeat creation.

.. _empty-values:
  
Empty values in math
~~~~~~~~~~~~~~~~~~~~~

Unanswered :ref:`number questions <number-widgets>` are nil.
That is, they have no value.
When a :ref:`variable <variables>` referencing an empty value is used 
in a math :ref:`operator <math-operators>` 
or :ref:`function <math-functions>`,
it is treated as Not a Number (``NaN``).
The empty value **will not** be converted to zero.
The result of a calculation including ``NaN`` 
will also be ``NaN``, 
which may not be the behavior you want or expect.

To convert empty values to zero,
use either the :func:`coalesce` function
or the :func:`if` function.

.. code-block:: none

  coalesce(${potentially_empty_value}, 0)

.. code-block:: none

  if(${potentially_empty_value}="", 0, ${potentially_empty_value})
  
.. _requiring-responses:

Requiring responses
=====================

By default,
users are able to skip questions in a form.
To make a question required,
put :tc:`yes` in the :th:`required` column.

Required questions are marked with a small asterisk
to the left of the question label.
You can optionally include a :th:`required_message`
which will be displayed to the user who tries to advance the form
without answering the question.

.. image:: /img/form-logic/required-0.* 
  :alt:

.. image:: /img/form-logic/required-1.* 
  :alt: 

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, required, required_message
  
  text, name, What is your name?, yes, Please answer the question.


.. _default-responses:
  
Setting default responses
===========================

To provide a default response to a question, put a value in the :th:`default` column. Defaults are set when a record is first created from a form definition. Defaults can either be fixed values (:ref:`static defaults <static-defaults>`) or the result of some expression (:ref:`dynamic defaults <dynamic-defaults>`).

.. _static-defaults:

Static defaults
----------------

The text in the :th:`default` column for a question is taken literally as the default value. Quotes should **not** be used to wrap values, unless you actually want those quote marks to appear in the default response value.

In the example below, the "Phone call" option with underlying value ``phone_call`` will be selected when the question is first displayed. The enumerator can either keep that selection or change it.

.. rubric:: XLSForm to select "Phone call" as the default contact method

.. csv-table:: survey
  :header: type, name, label, default

  select_one contacts, contact_method, How should we contact you?, phone_call

.. csv-table:: choices
  :header: list_name, name, label

  contacts, phone_call, Phone call
  contacts, text_message, Text message
  contacts, email, Email

.. _dynamic-defaults:

Dynamic defaults
----------------

.. warning::
  
  Support for :ref:`dynamic defaults <dynamic-defaults>` was added in Collect v1.24.0. Form conversion requires XLSForm Online ≥ v2.0.0 or pyxform ≥ v1.0.0. Using older versions will have unpredictable results.

If you put an expression in the :th:`default` column for a question, that expression will be evaluated once when a record is first created from a form definition. This allows you to use values from outside the form like the current date or the :ref:`server username <metadata>`. Dynamic defaults as described in this section are evaluated once on record creation. See below for using :ref:`dynamic defaults in repeats <dynamic-defaults-repeats>` or setting the :ref:`default value of one field to the value of another field in the form <defaults-from-form-data>`.

.. rubric:: XLSForm to set the current date as default

.. csv-table:: survey
  :header: type, name, label, default

  date, fever_onset, When did the fever start?, now()

In the example below, if a username is set either in the :ref:`server configuration <server-settings>` or the :ref:`metadata settings <form-metadata-settings>`, that username will be used as the default for the question asked to the enumerator.

.. rubric:: XLSForm to confirm metadata like username

.. csv-table:: survey
  :header: type, name, label, default

  username, username
  text, confirmed_username, What is your username?, ${username}

.. tip::
  If enumerators will need to enter the same value for multiple consecutive records, dynamic defaults can be combined with :ref:`last saved <last-saved>`. For example, if enumerators are collecting data about trees and trees of the same kind grow together, you can use the last saved tree species as the default for new records.

.. _dynamic-defaults-repeats:

Dynamic defaults in repeats
---------------------------

Dynamic defaults in repeats are evaluated when a new repeat instance is added.

One powerful technique is to use a value from a previous repeat instance as a default for the current repeat instance. For example, you could use the tree species specified for the last visited tree as the default species for the next tree.

.. note::
  
  If you are collecting data about multiple entities such as trees, you can choose to use repeats or to use one form record per entity. See :ref:`the repeats section <repeats>` for more information on making that decision. If you use one form record per entity, you can use :ref:`last saved <last-saved>` to get the same behavior as described in this section.

.. rubric:: XLSForm to set a default value based on the last repeat instance

.. csv-table:: survey
  :header: type, name, label, default

  begin_repeat, tree, Tree
  text, species, Species, ${tree}[position() = position(current()/..) - 1]/species

In the default expression above, ``${tree}`` is a reference to the repeat. The expression ``[position() = position(current()/..) - 1]`` in brackets says to filter the list of possible ``tree`` repeat instances to only include the one with a position that is one less than the current repeat's position. Finally, ``/species`` specifies that the ``species`` question from the repeat should be used. This is a mix of XLSForm's ``${}`` shortcut syntax for specifying question names and raw `XPath syntax <https://getodk.github.io/xforms-spec/#xpath-paths>`_.

.. _defaults-from-form-data:

Dynamic defaults from form data
-------------------------------

.. warning::
  
  Support for :ref:`dynamic defaults <dynamic-defaults>` from form data was added in Collect v1.24.0. Form conversion requires XLSForm Online ≥ v2.2.0 or pyxform ≥ v1.2.0. Using older versions will have unpredictable results.

It can be helpful to use a value filled out by the enumerator as a default for another question that the enumerator will later fill in. Dynamic defaults as described above can't be used for this because they are evaluated on form or repeat creation, before any data is filled in.

You also **can't use the calculation column on its own for this** because the expression in the :th:`calculation` would be evaluated on form save and replace any changes the enumerator has made. Instead, use a combination of :th:`calculation` and :th:`trigger`. The question reference in the :th:`trigger` column will ensure that your :th:`calculation` is only evaluated when that reference changes.

.. rubric:: XLSForm that uses current age as the default for diagnosis age

.. csv-table:: survey
  :header: type, name, label, calculation, trigger
  
  text, name, Child's name,
  integer, current_age, Child's age,
  select_one gndr, gender, Gender,
  integer, diagnosis_age, Age at malaria diagnosis, ${current_age}, ${current_age}

In the example above, ``${current_age}`` in the :th:`trigger` column means that when the value of the ``current_age`` question is changed by the enumerator, the :th:`calculation` for the ``diagnosis_age`` question will be evaluated. In this case, this means the new value for ``current_age`` will replace the current value for ``diagnosis_age``. If the enumerator then changes the value for ``diagnosis_age``, this value will be retained unless the value for ``current_age`` is changed again.

Another option for the scenario above is to clear out the value for ``diagnosis_age`` when ``current_age`` changes. Making ``diagnosis_age`` a required question will force the enumerator to update ``diagnosis_age`` if ``current_age`` is corrected.

.. rubric:: XLSForm that clears diagnosis age if current age is updated

.. csv-table:: survey
  :header: type, name, label, required, calculation, trigger
  
  text, name, Child's name,
  integer, current_age, Child's age,
  select_one gndr, gender, Gender,
  integer, diagnosis_age, Age at malaria diagnosis, true(), '', ${current_age}

In the example above, ``diagnosis_age`` is cleared any time the value of the ``current_age`` question is changed.

This kind of default is particularly useful if a form is being filled in about entities that there is already some knowledge about. For example, if you have a list of people to interview and you know their phone numbers, you may want to use the known phone number as a default and allow the enumerator to update it as needed.

.. rubric:: XLSForm that looks up default values based on a selection

.. csv-table:: survey
  :header: type, name, label, calculation, trigger, choice_filter

  select_one participants, participant, Participant, , ,true()
  text, phone_number, Phone number, instance('participants')/root/item[name=${participant}]/phone_number, ${participant}

.. csv-table:: choices
  :header: list_name, name, label, phone_number
  
  participants, kwame_onwuachi, Kwame Onwuachi, +1-850-555-0168
  participants, sophia_roe, Sophia Roe, +36 55 562 079

In the example above, when a participant is selected, his or her phone number is populated as a default and can be updated as needed. If the selected participant changes, the phone number is replaced.

.. note::

  The ``true()`` in the :th:`choice_filter` column for the ``select_one`` in the example above is necessary to be able to look up participants' phone numbers. This is currently needed to overcome a ``pyxform`` bug.

.. _triggering_calculations_on_value_change:

Triggering calculations on value change
===========================================

.. warning::
  
  Support for triggering calculations on value change was added in Collect v1.24.0. Form conversion requires XLSForm Online ≥ v2.2.0 or pyxform ≥ v1.2.0. Using older versions will have unpredictable results.

:ref:`Calculations <calculations>` are recomputed any time one of the values in its expression changes. For example, if your form includes the calculation `${q1} + ${q2}`, it will be recomputed any time either of the values for `${q1}` or `${q2}` changes.

Calculations can also be triggered when a value not involved in the calculation changes. This uses the same ``trigger`` column as  :ref:`defaults from form data <defaults-from-form-data>`. It is particularly useful for triggering calculations that involve values not in the form like random numbers or time.

.. _lightweight_timestamping:

Lightweight timestamping
-------------------------------

Knowing how long an enumerator spent answering a question can help with quality control and training. ODK Collect provides an :doc:`audit log <form-audit-log>` that contains rich information about how an enumerator navigated a form. This log is captured as a separate file and can be complex to analyze. A simpler alternative is to capture timestamps when specific questions' values change. This is similar to the ``start`` and ``end`` timestamp :ref:`metadata types <metadata>`.

.. rubric:: Capturing last update timestamps

.. csv-table:: survey
  :header: type, name, label, calculation, trigger

  string, name, Name,,
  dateTime, name_last_update_time,, now(), ${name}
  string, life_story, Life story,,
  dateTime, life_story_last_update_time,, now(), ${life_story}

In the example above, the ``name_last_update_time`` field will be populated with the current time whenever the enumerator changes the value of the ``name`` question. 

You can also capture the first time a question's value is changed using an ``if`` in the `calculation`:

.. rubric:: Capturing first update timestamps

.. csv-table:: survey
  :header: type, name, label, calculation, trigger

  string, name, Name,,
  dateTime, name_first_update_time,, "if(${name_first_update_time}='', now(), ${name_first_update_time})", ${name}
  string, life_story, Life story,,
  dateTime, life_story_first_update_time,, "if(${life_story_first_update_time}='', now(), ${life_story_first_update_time})", ${life_story}

.. _constraints:

Validating and restricting responses
=========================================

To validate or restrict response values,
use the :th:`constraint` column.
The :th:`constraint` expression will be evaluated
when the user advances to the next screen.
If the expression evaluates to ``True``,
the form advances as usual.
If ``False``, 
the form does not advance
and the :th:`constraint_message` is displayed.

The entered value of the response is represented in the expression
with a single dot (``.``).

Constraint expressions often use comparison `operators`_ 
and :doc:`regular expressions <form-regex>`. 
For example:

:tc:`. >= 18`
  True if response is greater than or equal to 18.

:tc:`. > 20 and . < 200`
  True if the response is between 20 and 200.
  
:tc:`regex(.,'\p{L}+')`
  True if the response only contains letters, without spaces, separators, or numbers.
  
:tc:`not(contains(., 'prohibited'))`
  True if the substring ``prohibited`` does not appear in the response.

.. note::

  Constraints are not evaluated if the response is left blank.
  To restrict empty responses, 
  :ref:`make the question required <requiring-responses>`.
  
.. seealso:: :doc:`form-regex`  
  
.. include:: incl/form-examples/regex-middle-initial.rst
  
.. _read-only:
  
Read-only questions
---------------------  
    
To completely restrict user-entry, 
use the :th:`read_only` column with a value of :tc:`yes`.
This is usually combined with a :ref:`default response <default-responses>`,
which is often :ref:`calculated <calculations>` 
based on :ref:`previous responses <variables>`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, read_only, default, calculation

  decimal, salary_income, Income from salary,,,
  decimal, self_income, Income from self-employment,,,
  decimal, other_income, Other income,,,
  calculate, income_sum, , , , "${salary_income} + ${self_income} + ${other_income}"
  decimal, total_income, Total income, yes, ${income_sum}, 

    
    
.. _relevants:

Conditionally showing questions
=================================

The :th:`relevant` column can be used to
show or hide
questions and groups of questions
based on previous responses.

If the expression in the :th:`relevant` column
evaluates to ``True``, 
the question or group is shown.
If ``False``, 
the question is skipped.

Often, comparison `operators`_ are used in relevance expressions. For example:

:tc:`${age} <= 5`
  True if :tc:`age` is five or less.
  
:tc:`${has_children} = 'yes'`
  True if the answer to :tc:`has_children` was ``yes``.
  
Relevance expressions can also use :ref:`functions <form-functions>`.
For example:

:tc:`selected(${allergies}, 'peanut')`
  True if ``peanut`` was selected
  in the :ref:`multi-select-widget` named :tc:`allergies`.
  
:tc:`contains(${haystack}, 'needle')`
  True if the exact string ``needle`` 
  is contained anywhere inside the response to :tc:`haystack`.
  
:tc:`count-selected(${toppings}) > 5`
  True if more than five options were selected
  in the :ref:`multi-select-widget` named :tc:`toppings`.

.. _simple-conditional-example:

Simple example
---------------

.. video:: /vid/form-logic/conditional-simple.mp4
  :loop: true
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, relevant
  
  select_one yes_no, watch_sports, Do you watch sports?, 
  text, favorite_team, What is your favorite team?, ${watch_sports} = 'yes'
  
.. csv-table:: choices
  :header: list_name, name, label
  
  yes_no, yes, Yes
  yes_no, no, No

.. _complex-conditional-example:
  
Complex example
------------------

.. include:: incl/form-examples/constraint-on-selected.rst

.. warning::

  Calculations are evaluated regardless of their relevance.
  
  For example, 
  if you have a :tc:`calculate` widget
  that adds together two previous responses,
  you cannot use :th:`relevant` to skip in the case of missing values.
  (Missing values will cause an error.)
  
  Instead,
  use the `if() function`_ to check for the existence of a value,
  and put your calculation inside the ``then`` argument.
  
  .. _if() function: https://getodk.github.io/xforms-spec/#fn:if
  
  For example,
  when adding together fields ``a`` and ``b``:
  
  .. code-block:: none
  
    if(${a} != '' and ${b} != '', ${a} + ${b}, '')
    
  In context:
  
  .. csv-table::
    :header: type, name, label, calculation
    
    integer, a, a =, 
    integer, b, b =,
    calculate, a_plus_b, ,"if(${a} != '' and ${b} != '', ${a} + ${b}, '')"
    note, display_sum, a + b = ${a_plus_b}, 	

.. _groups:

Groups of questions
====================

To group questions, use the :tc:`begin_group...end_group` syntax.

.. rubric:: XLSForm --- Question group

.. csv-table:: survey
  :header: type, name, label

  begin_group, my_group, My text widgets
  text, question_1, Text widget 1
  text, question_2, These questions will both be grouped together
  end_group, ,

If given a :th:`label`, groups will be visible in the form path to help orient the user
(e.g. :guilabel:`My text widgets > Text widget 1`). Labeled groups will also be visible as clickable items in the jump menu:

.. image:: /img/form-logic/jump-menu-groups.*
  :alt: The jump menu with a few grouped questions.

.. warning::

  If you use ODK Build v0.3.4 or earlier, your groups will not be visible in the jump menu.
  The items inside the groups will display as if they weren't grouped at all.

Groups without labels can be helpful for organizing questions in a way that's invisible to the user. This technique can be helpful for internal organization of the form. These groups can also be a convenient way to :ref:`conditionally show certain questions <relevants>`.

.. _repeats:

Repeating questions
=====================
You can ask the same question or questions multiple times by wrapping them in :tc:`begin_repeat...end_repeat`. By default, enumerators are asked before each repetition whether they would like to add another repeat. It is also possible to :ref:`determine the number of repetitions ahead of time <statically-defined-repeats>` which can make the user interaction more intuitive. You can also :ref:`add repeats as long as a condition is met <repeat_based_on_condition>`.

.. rubric:: XLSForm --- Repeating one or more questions

.. csv-table:: survey
  :header: type, name, label 

  begin_repeat, my_repeat, repeat group label
  note, repeated_note, All of these questions will be repeated.
  text, name, What is your name?
  text, quest, What is your quest?
  text, fave_color, What is your favorite color?
  end_repeat, , 

.. warning::

  Displaying repeating questions :ref:`on the same screen <field-list>` (inside a :tc:`field-list` group) is not supported.

.. seealso::
    :doc:`form-repeats` describes strategies to address common repetition scenarios.

.. tip::
  Using repetition in a form is very powerful but can also make training and data analysis more time-consuming. Repeats exported from Central or Briefcase will be in their own files and will need to be joined with their parent records for analysis.

  Before adding repeats to your form, consider other options:

  - if the number of repetitions is small and known ahead of time, consider "unrolling" the repeat by copying the same questions several times.
  - if the number of repetitions is large and includes many questions, consider building a separate form that enumerators fill out multiple times and link the forms with some parent key (e.g., a household ID).

  If repeats are needed, consider adding some summary calculations at the end so that analysis will not require joining the repeats with their parent records. For example, if you are gathering household information and would like to compute the total number of households visited across all enumerators, add a calculation after the repeats that counts the repetitions in each submission.
 
  
.. _controlling-number-of-repeats:

Controlling the number of repetitions
--------------------------------------
    
.. _user-controlled-repeats:
    
User-controlled repeats
~~~~~~~~~~~~~~~~~~~~~~~~

By default, the enumerator controls how many times the questions are repeated.

Before each repetition, the user is asked if they want to add another.

.. note::

  The :th:`label` in the :tc:`begin_repeat` row is shown in quotes in the **Add ...?** message.
  
  A meaningful label will help enumerators and participants navigate the form as intended. We generally recommend using a singular noun or noun phrase such as "observation" or "household member".

  This interaction may be confusing to users the first time they see it. If enumerators know the number of repetitions ahead of time, consider using a :ref:`dynamically defined repeat count <dynamically-defined-repeats>`.

.. figure:: /img/form-logic/repeat-iteration-modal.* 
  :alt: The Collect app. A modal dialog with the question: "Add "Person"?" and options "Do not add" and "Add".
  
  The user is given the option to add each repetition.

.. tip::

  The :ref:`jump <jumping>` menu also provides shortcuts to :ref:`add <adding_repeats>` or :ref:`remove <removing_repeats>` repeat instances.

.. _statically-defined-repeats:

Fixed repeat count
~~~~~~~~~~~~~~~~~~~~

Use the :th:`repeat_count` column to define the number of times that questions will repeat.


.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, repeat_count

  begin_repeat, my_repeat, Repeat group label, 3
  note, repeated_note, These questions will be repeated exactly three times.
  text, name, What is your name?
  text, quest, What is your quest?
  text, fave_color, What is your favorite color?
  end_repeat, , 

.. _dynamically-defined-repeats:
 
Dynamically defined repeat count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :th:`repeat_count` column can reference :ref:`previous responses <variables>` and :ref:`calculations <calculations>`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, repeat_count
  
  integer, number_of_children, How many children do you have?
  begin_repeat, child_questions, Questions about child, ${number_of_children}
  text, child_name, Child's name,
  integer, child_age, Child's age,
  end_repeat, , , 

.. _repeat_based_on_condition:

Repeating as long as a condition is met
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the enumerator won't know how many repetitions are needed ahead of time, you can still avoid the "Add ...?" dialog by using the answer to a question to decide whether another repeat instance should be added. In the example below, repeated questions about plants will be asked as long as the user answers "yes" to the last question.

.. csv-table:: survey
  :header: type, name, label, calculation, repeat_count
  
  calculate, count, , count(${plant})
  begin_repeat, plant, Plant, , if(${count} = 0 or ${plant}[position()=${count}]/more_plants = 'yes', ${count} + 1, ${count})
  text, species, Species,
  integer, estimated_size, Estimated size,
  select_one yes_no, more_plants, Are there more plants in this area?,
  end_repeat, , , ,

.. csv-table:: choices
  :header: list_name, name, label
  
  yes_no, yes, Yes
  yes_no, no, No

This works by maintaining a :func:`count` of the existing repetitions and either making :th:`repeat_count` one more than that if the continuing condition is met or keeping the :th:`repeat_count` the same if the ending condition is met. 

In the `repeat_count` expression, `${count} = 0` ensures that there is always at least one repeat instance created. The continuing condition is `${plant}[position()=${count}]/more_plants = 'yes'` which means "the answer to `more_plants` was `yes` the last time it was asked." The expression `position()=${count}` uses the :func:`position` function to select the last plant that was added. Adding `/more_plants` to the end of that selects the `more_plants` question.

.. _zero-repetitions:

Repeating zero or more times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it only makes sense to collect information represented by the questions in a repeat under certain conditions. If the number of total repetitions is known ahead of time, use :ref:`dynamically-defined-repeats` and allow a count of 0. If the count is not known ahead of time, :ref:`relevants` can be used to represent 0 or more repetitions. In the example below, questions about trees will only be asked if the user indicates that there are trees to survey.

.. csv-table:: survey
  :header: type, name, label, relevant
  
  select_one yes_no, trees_present, Are there any trees in this area?,
  begin_repeat, tree, Tree, ${trees_present} = 'yes'
  text, species, Species,
  integer, estimated_age, Estimated age,
  end_repeat, , , ,

.. csv-table:: choices
  :header: list_name, name, label
  
  yes_no, yes, Yes
  yes_no, no, No

.. _cascading-selects:
  
Filtering options in select questions
===============================================

To limit the options in a select question based on the answer to a previous question, specify an expression in the :th:`choice_filter` column of the **survey** sheet. This expression will refer to one or more column in the **choices** sheet that the dataset should be filtered by.

For example, you might ask your enumerators to select a state first, and then only display cities within that state. This is referred to as a "cascading select" and can be extended to any depth. The example below has two levels: job category and job title.

The :th:`choice_filter` expression for the second select in the example is ``cat=${job_category}``. ``cat`` is the name of a column in the **choices** sheet and ``${job_category}`` refers to the first select question in the form. The filter expression says to only include rows whose ``cat`` column value exactly matches the value selected by the enumerator as ``${job_category}``.

Any expression that evaluates to ``True`` or ``False`` can be used as a :th:`choice_filter`. For example, you could add a ``location`` column to the **choices** sheet and also ask the user to enter a location they want to consider jobs in. If the new location question on the **survey** sheet is named ``${job_location}``, the choice filter would be ``cat=${job_category} and location=${job_location}``. Another example of a complex choice filter is one that uses :ref:`text comparison functions <string-comparison-functions>` to match labels that start with a certain value. Consider, for example, ``starts-with(label, ${search_value})`` where ``search_value`` is the name of a text question defined on the **survey** sheet.

.. video:: /vid/form-logic/cascade-select.mp4

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, choice_filter
  
  select_one job_categories, job_category, Job category
  select_one job_titles, job_title, Job title, cat=${job_category}

.. csv-table:: choices
  :header: list_name, name, label, cat
  
  job_categories, finance, Finance,
  job_categories, hr, Human Resources,
  job_categories, admin, Administration/Office,
  job_categories, marketing, Marketing,
  job_titles, ar, Accounts Receivable, finance
  job_titles, pay, Payroll, finance
  job_titles, recruiting, Recruiting, hr
  job_titles, training, Training, hr
  job_titles, retention, Retention, hr
  job_titles, asst, Office Assistant, admin
  job_titles, mngr, Office Manager, admin
  job_titles, reception, Receptionist, admin
  job_titles, creative_dir, Creative Director, marketing
  job_titles, copywriter, Copywriter, marketing


.. _generating-select-ones-from-repeats:

Generating select ones from repeats
========================================

If you use a repeat, you can generate a follow-up ``select_one`` question using values from the repeat. For example, if you collect information about several household members in a repeat, you can then show a select one with all household members' names. To do this, add a question of type ``select_one`` followed by the name of the question in the repeat that you want to use for the select options.

.. csv-table:: survey
  :header: type, name, label, required, choice_filter
  
  begin_repeat, person, Person
  text, person_name, Person's name?, true()
  integer, person_age, ${person_name}'s age?, true()
  end_repeat, person
  
  select_one ${person_name}, tallest, Select the tallest person
  select_one ${person_name}, tallest_child, Select the tallest person under 18., ${person_age} < 18

As shown in the example above, you can combine this with other select features such as :ref:`filtering <cascading-selects>`. Note that in the example above, the question used as select option text is ``required``. If a question used to generate a ``select_one`` is not required and it is left blank for some repeat instances, those repeat instances will not be included in the select.
