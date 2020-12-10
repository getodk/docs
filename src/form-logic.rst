.. spelling::
 
  ap
  ar
  bp
  datetime
  dir
  fave
  gndr
  mngr
  timestamp

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
To use a variable,
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


.. _expressions:
  
Expressions
-------------

An :dfn:`expression`, sometimes called a `formula`_,
is evaluated dynamically as a form is filled out.
It can include `XPath functions`_, `operators`_,
:ref:`values from previous responses <variables>`,
and (in some cases) :ref:`the value of the current response <constraints>`. 

.. _XPath functions: https://getodk.github.io/xforms-spec/#xpath-functions

.. _operators: https://getodk.github.io/xforms-spec/#xpath-operators

.. _formula: http://xlsform.org/#formulas

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

This is particularly important to remember when using functions that access state outside of the form such as :func:`random` or :func:`now`. The value they represent will change over and over again as an enumerator fills out a form.

The :func:`once` function prevents multiple evaluation by only evaluating the expression passed into it if the node has no value. That means the expression will be evaluated once either on form open or when any values the expression depends on are set.

Every call on :func:`now` in the form will have the same value unless the :func:`once` function is used. For example, the following calculate will keep track of the first time the form was opened:

.. csv-table:: survey
  :header: type, name, label, calculation

  calculate, datetime_first_opened, , once(now())

The following calculate will keep track of the first time the enumerator set a value for the :th:`age` question:

.. csv-table:: survey
  :header: type, name, label, calculation

  integer, age, What is your age?,
  calculate, age_timestamp, , "if(${age} = '', '', once(now()))"


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

If you put an expression in the :th:`default` column for a question, that expression will be evaluated once when a record is first created from a form definition. This allows you to use values from outside the form like the current date or the :ref:`server username <metadata>`. Dynamic defaults can't be used to set the default value of one field to the value of another field in the form. Learn about alternatives in :ref:`the tip below <defaults-from-form-data>`.

.. rubric:: XLSForm to set the current date as default

.. csv-table:: survey
  :header: type, name, label, default

  date, fever_onset, When did the fever start?, now()

In the example below, if a username is set either in the :ref:`server configuration <server-settings>` or the :ref:`metadata settings <form-metadata-settings>`, that username will be used as the default for the question asked to the enumerator.

.. rubric:: XLSForm to set the default username as the server username

.. csv-table:: survey
  :header: type, name, label, default

  username, username
  text, confirmed_username, What is your username?, ${username}

If enumerators will need to enter the same value for multiple consecutive records, dynamic defaults can be combined with :ref:`last saved <last-saved>`.

Dynamic defaults in repeats are evaluated when a new repeat instance is added.

.. tip:: 
  :name: defaults-from-form-data

  You may want to use a value filled out by the enumerator as a default for another question that the enumerator will later fill in. Dynamic defaults can't be used for this because they are evaluated once when a record is first created which is before an enumerator fills in any data.
  
  One option is to use the :th:`calculation` column and wrap your default value expression in a :func:`once` function.
  
  .. rubric:: XLSForm that uses a child's current age as the default for diagnosis age
  
  .. csv-table:: survey
    :header: type, name, label, calculation
    
    text, name, Child's name,
    integer, current_age, Child's age,
    select_one gndr, gender, Gender,
    integer, malaria_age, Age at malaria diagnosis, once(${current_age}) 
    
  This solution has some limitations:
  
  - The value of the calculated default
    will get set to the first value that the earlier question receives,
    even if it is changed before viewing the later question.
    
    Example: In the above form,
    if you enter ``8`` on :tc:`current_age`,
    then advance to gender,
    then back up and change :tc:`current_age` to ``10``,
    when you get to :tc:`malaria_age`, 
    the default value will be ``8``.
    
  - If the first earlier question has a value,
    the dependent question will also have a value ---
    :func:`once` will evaluate anytime the question's value is blank.
    
    Example: In the above form,
    if you enter ``8`` on :tc:`current_age`
    and then delete the value ``8`` when you get to :tc:`malaria_age`
    (intending to leave it blank)
    the ``8`` value will come back as the answer when you advance.
    (In this case,
    using a blank value to indicate "child does not have malaria"
    would fail.)
  
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

:tc:`. < 20 and . > 200`
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

To limit the options in a select question
based on the answer to a previous question,
use a :th:`choice_filter` row in the **survey** sheet,
and filter key columns in the **choices** sheet.

For example,
you might ask the user to select a state first,
and then only display cities within that state.
This is called a `cascading select`_,
and can be extended to any depth.
`This example form`__ shows a three-tiered cascade:
state, county, city.

.. _cascading select: http://xlsform.org/#cascading-selects

__ https://docs.google.com/spreadsheets/d/1CCjRRHCyJXaSEBHPjMWrGotnORR4BI49PoON6qK01BE/edit#gid=0

.. video:: /vid/form-logic/cascade-select.mp4

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, choice_filter
  
  select_one job_categories, job_category, Job category
  select_one job_titles, job_title, Job title, job_category=${job_category} 

.. csv-table:: choices
  :header: list_name, name, label, job_category
  
  job_categories, finance, Finance,
  job_categories, hr, Human Resources,
  job_categories, admin, Administration/Office,
  job_categories, marketing, Marketing,
  job_titles, ar, Accounts Receivable, finance
  job_titles, ap, Account Payable, finance
  job_titles, bk, Bookkeeping, finance
  job_titles, pay, Payroll, finance
  job_titles, recruiting, Recruiting, hr
  job_titles, training, Training, hr
  job_titles, retention, Retention, hr
  job_titles, asst, Office Assistant, admin
  job_titles, mngr, Office Manager, admin
  job_titles, scheduler, Scheduler, admin
  job_titles, reception, Receptionist, admin
  job_titles, creative_dir, Creative Director, marketing
  job_titles, print_design, Print Designer, marketing
  job_titles, ad_buyer, Ad Buyer, marketing
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