Repeat Recipes and Tips
========================

.. seealso::
    :ref:`repeats` describes repeat basics.

.. _referencing-answers-in-repeats:

Referencing repeated questions from inside the repeat
-----------------------------------------------------

Within a repeat, you can reference other questions **in that same repeat instance** :ref:`in the usual manner <variables>`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label

  note, child_questions_note, Please provide the following details about each child in your household.
  begin_repeat, child_details, Children in household
  text, child_first_name, Name
  text, child_age, Age of ${child_first_name}
  end_repeat

To reference a question from a different repeat instance, or from outside the repeat, use :func:`indexed-repeat` and :func:`position`.
 
.. _referencing-responses-from-outside-repeat-loop:
  
Referencing repeated questions from outside the repeat
-------------------------------------------------------

A question in a repeat can be referenced from outside the repeat with ``indexed-repeat(${question-name}, ${repeat-name}, index)``.

.. _counting-repeats-and-answers:

Counting repeats and answers
------------------------------

.. _counting-iterations:

Counting the total number of repeat instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `count(${name-of-repeat})` to get the number of repeat instances.

.. _counting-answers:

Counting the number of times a particular answer was given
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To count the number of times
a specific response is given,
add a calculate field inside the repeat
which evaluates to ``1`` or ``0`` depending on the answer.
Then, outside the repeat,
calculate the ``sum()`` of the calculate field.

.. include::  incl/form-examples/sum-to-count-responses.rst

.. _using-parallel-repeat-groups:

Using additional repeats to follow up on repeated questions
-----------------------------------------------------------

Sometimes it is convenient to gather an initial set of responses,
and then ask more detailed question after you have collected the whole set.

For example:

 - collecting the names of all the people in a household, and then asking questions about each person
 - collecting the names of each type of crop being grown, and then asking questions about each crop

This can be done by using `count()` and `position(..)`. `count()` is used to guarantee that the second repeat has the same number of instances as the original repeat. `position(..)` provides the index of the repeat instance it was called from. This is used to refer to questions from the first repeat in the follow-up repeat.

.. include:: incl/form-examples/parallel-repeats.rst

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
and use the ``relevant`` column to 
:ref:`skip repetitions if <relevants>` the previous question is left blank.
This sets a maximum number of responses:
the number of times you included the question in the form.

To check if the previous question has a response,
:ref:`reference the question <variables>` in the ``relevant`` column.

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
:ref:`required responses <requiring-responses>`
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