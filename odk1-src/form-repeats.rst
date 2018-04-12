.. spelling::

  bday
  bool
  chkn
  fsh
    
	
Repeat Recipes and Tips
========================

.. _setting-max-repeats:

Setting a max limit on repetitions
----------------------------------

If you want the user to decide how many times to repeat,
but you also want to limit the maximum number of repetitions,
you have a few options.

.. _use-constraint-for-max-repeats:

Using a constraint to limit repetitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the user knows how many repetitions they will complete,
you can ask them this in a question before the repeat group
and set a constraint on that question.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, constraint, repeat_count
  
  integer, number_in_party, How many guests are in your party?, . <= 8
  note, party_names_note, Please provide details for each guest., ,
  begin_repeat, guest_details, Guest details,,${number_in_party}
  text, guest_name, Guest's name, ,
  text, guest_dietary, Does this guest have any dietary restrictions?, , 
  end_repeat,,,,
  
.. _use-relevant-for-max-repeats:
  
Using relevants to limit repetitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If asking the user ahead of time doesn't make sense,
another strategy is to manually repeat the question in the form
and use the :th:`relevant` column to 
:ref:`skip repetitions if <relevants>` the previous question is left blank.
This sets a maximum number of responses:
the number of times you included the question in the form.

To check if the previous question has a response,
:ref:`reference the question <variables>` in the :th:`relevant` column.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, relevant
  
  note, images_note, Take up to five pictures.,
  image, image_1, Image 1, 
  image, image_2, Image 2, ${image_1}
  image, image_3, Image 3, ${image_2}
  image, image_4, Image 4, ${image_3}
  image, image_5, Image 5, ${image_4}
  
  
This pattern can be combined with 
:ref:`required responses <requiring_responses>`
to enforce a minimum number of responses.


.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, required, relevant
  
  note, images_note, Take 3-5 pictures.,,
  image, image_1, Image 1, yes, 
  image, image_2, Image 2, yes,
  image, image_3, Image 3, yes,
  image, image_4, Image 4, ,${image_3}
  image, image_5, Image 5, ,${image_4}

.. _referencing-answers-in-repeats:
  
Referencing answers from repeated questions
--------------------------------------------

Within a repeat group iteration,
you can reference previous answers **in that same iteration**
:ref:`in the usual manner <variables>`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
  
  note, child_questions_note, Please provide the following details about each child in your household.
  begin_repeat, child_details, Children in household
  text, child_first_name, Name
  text, child_age, Age of ${child_first_name}
  end_repeat
  
To reference a response from a later iteration,
or from outside the loop,
use :func:`indexed-repeat` and :func:`position`.
  
.. function:: indexed-repeat(name, group, i [, sub_grp, sub_i [, sub_sub_grp, sub_sub_i [...]]])

  Returns the response value of question ``name``
  from the repeat-group ``group``,
  in iteration ``i``.
  
  Nested repeat groups can be accessed 
  using the ``sub`` and ``sub_sub`` parameters,
  which can be extended indefinitely
  to arbitrary levels of nesting.
  
.. function:: position(xpath)

  Returns an integer equal to the position of the current node
  within the node defined by ``xpath``.
  
  Most often this is used in the form ``position(..)``
  to identify the current iteration index.

.. _referencing-previous-iteration:
  
Referencing answers from the previous iteration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The index for the previous iteration of a repeat is 
``position(..) - 1``.
This could be used, for example, to provide a 
:ref:`default response <default-responses>` based on 
the previous response to the same question.

Be sure to account for the first iteration,
which doesn't have a previous response.
This may require use of a :ref:`calculations`.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, default, calculation
  
  note, child_details_note, Please provide the following details about each child.
  begin_repeat, child_details, Children in household
  text, child_name, Name
  calculate, previous_school,,"if(bool(position(..), indexed-repeat(${child_school}, ${child_details}, position(..) - 1), ''))"
  text, child_school, Current school, ${previous_school} ,

.. _referencing-responses-from-outside-repeat-loop:
  
Referencing responses from outside the repeat loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The response to a question from
any iteration of a repeat group can be referenced
from outside the repeat group with
:tc:`indexed-repeat(${question-name}, ${group-name}, index`.

.. _using-parallel-repeat-groups:

Using additional repeat groups to iterate through responses
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Sometimes it is convenient to gather an initial set of responses,
and then ask more detailed question after you have collected the whole set.

For example:

 - collecting the names of all the people in a household, and then asking questions about each person
 - collecting the names of each type of crop being grown, and then asking questions about each crop
 
This can be done by using `count()` and `position(..)` 
to iterate through a repeat group 
in a second repeat group.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, repeat_count, calculation
    
  note, person_list_note, Please list the names of the people in your household.,,
  begin_repeat, name_group, Member of household, ,
  text, name, Name, ,
  end_repeat,,,,
  begin_repeat, member_details, Details, count(${name}) ,
  calculate, current_name, , , "indexed-repeat(${name}, ${name-group}, position(..))"
  date, member_bday, Birthday of ${current_name},,
  end_repeat,,,, 
  

.. _counting-repeats-and-answers:

Counting repeats and answers
------------------------------

.. _counting-iterations:

Counting the total number of iterations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there is a required response in the repeat group,
use `count(${required-question-name})` to get the number of responses,
which will be the same as the number of iterations.

If you don't have at least one required field,
use the `max()` function and refer to a calculate row
with the calculation `position(..)`. 
This will return the highest index,
which is also the total number of iterations.

.. _counting-answers:

Counting the number of times a particular answer was given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To count the number of times
a specific response is given,
add a calculate field inside the loop
which evaluates to ``1`` or ``0`` depending on the answer.
Then, outside the loop,
calculate the :tc:`sum()` of the calculate field.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, calculation
  
  begin_repeat, guest_details, Guest details
  text, guest_name, Guest name
  select_one meal_options, meal_preference, Meal preference
  calculate, chkn, , "if(${meal_preference} == 'chicken', 1, 0 )"
  calculate, fsh, , "if(${meal_preference} == 'fish', 1, 0 )"
  calculate, veg, , "if(${meal_preference} == 'vegetarian', 1, 0 )"
  end_repeat
  calculate, chkn_count, , sum(${chkn})
  calculate, fsh_count, , sum(${fsh})
  calculate, veg_count, , sum(${veg})
 
.. csv-table:: choices
  :header: list_name, name, label
  
  meal_options, chicken, Chicken
  meal_options, fish, Fish
  meal_options, vegetarian, Vegetarian
