.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, repeat_count, calculation
    
  note, person_list_note, Please list the names of the people in your household.,,
  begin_repeat, person, Member of household, ,
  text, name, Name, ,
  end_repeat,,,,
  begin_repeat, person_details, Details, count(${person}) ,
  calculate, current_name, , , "indexed-repeat(${name}, ${person}, position(..))"
  date, member_bday, Birthday of ${current_name},,
  end_repeat,,,, 
  
