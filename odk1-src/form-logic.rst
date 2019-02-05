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

.. _XPath functions: https://opendatakit.github.io/xforms-spec/#xpath-functions

.. _operators: https://opendatakit.github.io/xforms-spec/#xpath-operators

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

A common misconception is that expressions are only evaluated when a question that uses it is reached. This faulty mental model leads form designers to include functions such as :func:`random` or :func:`now` and to expect them to be evaluated exactly once. In fact, they will be re-evaluated over and over again until the form is finalized for the last time. For example, the following calculate will keep track of the last time the form was saved:

.. csv-table:: survey
  :header: type, name, label, calculation

  calculate, datetime_last_saved, , now()

The :func:`once` function prevents multiple evaluation by only evaluating the expression passed into it if the node has no value. That means the expression will be evaluated once either on form open or when any values the expression depends on are set.

Every call on :func:`now` in the form will have the same value unless the :func:`once` function is used. For example, the following calculate will keep track of the first time the form was opened:

.. csv-table:: survey
  :header: type, name, label, calculation

  calculate, datetime_first_opened, , once(now())

The following calculate will keep track of the first time the enumerator set a value for the :th:`age` question:

.. csv-table:: survey
  :header: type, name, label, calculation

  integer, age, What is your age?,
  calculate, age_timestamp, , "if(age = '', '', once(now()))"


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

To provide a default response to a question,
put the response value in the :th:`default` column.

Default values must be static values,
not expressions or variables.

.. note::

  The content of the :th:`default` row in a question
  is taken literally as the default value.
  Quotes should **not** be used to wrap string values,
  unless you actually want those quote marks to appear
  in the default response value.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, default
  
  select_one contacts, contact_method, How should we contact you?, phone_call
  
.. csv-table:: choices
  :header: list_name, name, label
  
  contacts, phone_call, Phone call
  contacts, text_message, Text message
  contacts, email, Email
  
.. tip:: 
  :name: dynamic-defaults

  You may want to use a previously entered value as a default,
  but the :th:`default` column does not accept dynamic values.
  
  To work around this, use the :th:`calculation` column instead,
  and wrap your default value expression in a :func:`once` function.
  
  .. rubric:: XLSForm
  
  .. csv-table:: survey
    :header: type, name, label, calculation
    
    text, name, Child's name,
    integer, current_age, Child's age,
    select_one gndr, gender, Gender,
    integer, malaria_age, Age at malaria diagnosis, once(${current_age}) 
    
  This solution has some limitations, though.
  
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
  
  .. _if() function: https://opendatakit.github.io/xforms-spec/#fn:if
  
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

.. rubric:: XLSForm (Question group)

.. csv-table:: survey
  :header: type, name, label

  begin_group, my_group, My text widgets
  text, question_1, Text widget 1
  text, question_2, These questions will both be grouped together
  end_group, ,

If given a :th:`label`, groups will be visible in the form path to help orient the user
(e.g. :guilabel:`My text widgets > Text widget 1`).

If given a :th:`label` and also a :th:`ref`, groups will be visible as clickable items in the jump menu:

.. image:: /img/form-logic/jump-menu-groups.*
  :alt: The jump menu with a few grouped questions.

.. warning::

  If you use ODK Build v0.3.4 or earlier, your groups will not be visible in the jump menu.
  The items inside the groups will display as if they weren't grouped at all.

Groups can also be a convenient way to :ref:`conditionally show certain questions <relevants>`.

.. _repeats:

Repeating questions and groups of questions
==============================================

.. note::
  Using repetition in a form is very powerful but can also make training and data analysis more time-consuming. Aggregate does not export repeats so Briefcase or one of the data publishers will be needed to :doc:`transfer data from Aggregate <aggregate-data-access>`. Repeats will be in their own documents and will need to be joined with their parent records for analysis.
  
  Before adding repeats to your form, consider other options:

  - if the number of repetitions is small and known ahead of time, consider "unrolling" the repeat by copying the same questions several times.
  - if the number of repetitions is large and includes many questions, consider building a separate form that enumerators fill out multiple times and link the forms with some parent key (e.g., a household ID).

  If repeats are needed, consider adding some summary calculations at the end so that analysis will not require joining the repeats with their parent records. For example, if you are gathering household information and would like to compute the total number of households visited across all enumerators, add a calculation after the repeats that counts the repetitions in each submission.

To repeat questions or groups of questions
use the :tc:`begin_repeat...end_repeat` syntax.

.. rubric:: XLSForm (Single question repeat)

.. csv-table:: survey
  :header: type, name, label 

  begin_repeat, my_repeat_group, Repeat group label
  text, repeated_question, This question will be repeated.
  end_repeat, , 

.. rubric:: XLSForm (Multi-question repeat)

.. csv-table:: survey
  :header: type, name, label 

  begin_repeat, my_repeat, Repeat group label
  note, repeated_note, These questions will be repeated as an entire group.
  text, name, What is your name?
  text, quest, What is your quest?
  text, fave_color, What is your favorite color?
  end_repeat, , 
 
  
.. _controlling-number-of-repeats:

Controlling the number of repetitions
--------------------------------------
    
.. _user-controlled-repeats:
    
User-controlled repeats
~~~~~~~~~~~~~~~~~~~~~~~~

By default,
the user controls how many times 
the questions are repeated.

Before each repetition,
the user is asked if they want to add another repeat group.

.. note::

  The :th:`label` in the :tc:`begin_repeat` row
  is shown in the **Add New Group?** message.
  
  A meaningful label will help enumerators and participants 
  navigate the form as intended.

.. figure:: /img/form-logic/repeat-iteration-modal.* 
  :alt: The Collect app. A modal dialog labeled "Add new group?" with the question: "Add a new 'repeat group label' group?" and options "Do not add" and "Add Group".
  
  The user is given the option to add each iteration.
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
  
  begin_repeat, repeat_example, repeat group label
  text, repeat_test, Question label
  end_repeat,,

.. note::

  This interaction may be confusing to users the first time they see it. If enumerators know the number of repetitions ahead of time, consider using :ref:`dynamically defined repeats <dynamically-defined-repeats>`.

.. _statically-defined-repeats:

Statically defined repeats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the :th:`repeat_count` column
to define the number of times a group will repeat.


.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, repeat_count

  begin_repeat, my_repeat, Repeat group label, 3
  note, repeated_note, These questions will be repeated as an entire group.
  text, name, What is your name?
  text, quest, What is your quest?
  text, fave_color, What is your favorite color?
  end_repeat, , 
 
.. _dynamically-defined-repeats:
 
Dynamically defined repeats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :th:`repeat_count` column can reference
:ref:`previous responses <variables>` and :ref:`calculations <calculations>`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, repeat_count
  
  integer, number_of_children, How many children do you have?
  begin_repeat, child_questions, Questions about child, ${number_of_children}
  text, child_name, Child's name,
  integer, child_age, Child's age,
  end_repeat, , , 


.. seealso:: :doc:`form-repeats`
  
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

.. _cascading select: http://xlsform.org/#cascade

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


