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
  
