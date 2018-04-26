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
