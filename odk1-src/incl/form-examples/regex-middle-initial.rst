.. image:: /img/form-logic/constraint-message.* 
  :alt: A text widget in Collect. The question text is "What is your middle initial?" The entered value is "Michael". Over the widget is an alert message: "Just the first letter."
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, constraint, constraint_message
  
  text, middle_initial, What is your middle initial?, "regex(., '\p{L}')", Just the first letter.
