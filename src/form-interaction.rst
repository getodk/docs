Interaction of constraints, relevants and read only
=========================================================

Constraints
-------------

Adding constraints to the data fields in a form ensures data quality. For example, when asking for a person’s age, you want to avoid impossible answers, like -22 or 200. Adding data constraints in your form is easy to do. You simply add a new column, called constraint, and type in the formula specifying the limits on the answer. 

If you want to include a message with your constraint, telling the user why the answer is not accepted, you can add a **constraint_message** column to your form.

In the example below, the answer for the person’s age must be less than or equal to 40. Note that . in the formula refers back to the question variable.

.. csv-table:: **Survey** 
  :header: "type", "name", "label", "constraint", "constraint_message"
  :widths: auto
 
  "integer", "age", "How old are you?", ".<=40", "Person must be 40 years old or younger to complete the survey."

For more details, refer `constraints section in XLSForm documentation <http://xlsform.org/#constraints>`_.

Relevants
-----------

Relevants are used to skip a question or make an additional question appear based on the response to a previous question. Relevants can be added to the question so that the question is asked only when the relevant is satisfied.

In the example below, school name will be asked only if age entered by the user is less than or equal to 18.

.. csv-table:: **Survey**
  :header: "type", "name", "label", "relevant"
  :widths: auto

  "integer", "age", "How old are you?"
  "text", "School", "Enter your school name", "${age} <= 18"

For more details, refer `relevants section in XLSForm documentation <http://xlsform.org/#relevant>`_.  


Read only
-------------

Adding a read only field means that a question can not be edited. Read only fields can be combined with default fields to deliver information back to a user.

.. note::
   
   Adding a default field means that a question will be pre-populated with an answer when the user first sees the question. This can help save time if the answer is one that is commonly selected or it can serve to show the user what type of answer choice is expected.

To make questions as read only, add a **read_only** column to your survey worksheet. Under that column, mark questions as read only by writing yes.   

In the example below, city is a read only value with default as California. User cannot modify this field.

.. csv-table:: **Survey**
  :header: "type", "name", "label", "read_only", "default"
  :widths: auto

  "text", "City", "Enter a city where server will operate", "yes", "California"

For more details, refer `read only section in XLSForm documentation <http://xlsform.org/#read-only>`_.  

Required
------------

Marking any question as required means the user will not be able to move on to the next question or submit the form without entering an answer for that question.

To make questions required, add a **required** column to your survey worksheet. Under that column, mark questions as required by writing yes.   

.. csv-table:: **Survey**
  :header: "type", "name", "label", "required", 
  :widths: auto

  "text", "name", "Enter your name", "yes", ""

For more details, refer `required section in XLSForm documentation <http://xlsform.org/#required>`_.  

Calculation
-------------

Your survey can perform calculations using the values of preceding questions. In most cases this will require inserting a **calculate** question. For example, in the survey below, we have calculated the tip for a meal and displayed it to the user.  

.. csv-table:: **Survey**
  :header: "type", "name", "label", "calculation"
  :widths: auto

  "decimal", "amount", "What was the price of the meal?", ""   
  "calculate", "tip", "", "${amount} * 0.18"
  "note", "display", "18% tip for your meal is: ${tip}", "" 

For more details, refer `calculation section in XLSForm documentation <http://xlsform.org/#calculation>`_. 

Tips on using above fields
----------------------------

- Constraints should only be applied to fields that can be changed. It is of no use to apply constraints to readonly fields or note fields.

.. csv-table:: **Survey**  
  :header: "type", "name", "label", "constraint", "constraint_message", "relevant", "read_only", "default", "required", "calculation"
  :widths: auto

  "text", "name", "Enter your name", "", "", "", "", "", "", "yes", ""
  "integer", "age", "Enter your age", ".<=18", "You should be below 18 years to be eligible for the survey. ", "", "", "", "", "yes", ""
  "text", "college", "College name", "${college}='IIT Roorkee'", "", "", "yes", "IIT Roorkee", "", "", ""
  "select_one yes_no", "course", "Have you chosen any courses?", "", "", "", "", "", "yes", ""
  "integer", "course_cnt", "Enter number of courses you have chosen", "1<=.<=6", "You should choose atleast 1 course and atmost 6 courses.", "${course}='yes'", "", "", "yes", ""         
  "integer", "marks", "Enter total marks obtained in all courses", "", "", "${course}='yes'", "", "", "yes", ""
  "calculate", "total", "", "", "", "${course_cnt}!=''", "", "", "", "${course_cnt}*100"
  "note", "disp_max", "Maximum marks possible are ${total}.", "${total}<${marks}", "", "${course_cnt}!=''", "", "", "", ""

In this survey table, it is of no use to include a constraint in college field since it is already fixed and user cannot modify it. Further the constraint in the note field is of no use as it will just display an note that *Maximum allowed marks are total* but will allow the user to fill the form even with more than total marks.

To prevent the user from entering more tha maximum marks, a constraint should be included in the marks field: **${marks}<=${total}** and the note should have a relevant: **${course_cnt}!='' and ${total}<${marks}**.

.. csv-table:: **Survey**  
  :header: "type", "name", "label", "constraint", "constraint_message", "relevant", "read_only", "default", "required", "calculation"
  :widths: auto

  "text", "name", "Enter your name", "", "", "", "", "", "", "yes", ""
  "integer", "age", "Enter your age", ".<=18", "You should be below 18 years to be eligible for the survey. ", "", "", "", "", "yes", ""
  "text", "college", "College name", "", "", "", "yes", "IIT Roorkee", "", "", ""
  "select_one yes_no", "course", "Have you chosen any courses?", "", "", "", "", "", "yes", ""
  "integer", "course_cnt", "Enter number of courses you have chosen", "1<=.<=6", "You should choose atleast 1 course and atmost 6 courses.", "${course}='yes'", "", "", "yes", ""         
  "integer", "marks", "Enter total marks obtained in all courses", "", "", "${course}='yes'", "", "", "yes", ""
  "calculate", "total", "", "", "", "${course_cnt}!=''", "", "", "", "${course_cnt}*100"
  "note", "disp_max", "Maximum marks possible are ${total}.", "${total}<${marks}", "", "${course_cnt}!=''", "", "", "", ""

These are the :file:`.xml` files for the above forms:

  1. :download:`example_1 </downloads/form-interaction/example_1.xml>`
  2. :download:`example_2 </downloads/form-interaction/example_2.xml>`

These are the :file:`.xlsx` files for the above forms:

  1. :download:`example_1 </downloads/form-interaction/example_1.xlsx>`
  2. :download:`example_2 </downloads/form-interaction/example_2.xlsx>`

- Whenever you perform a calculation make sure that it has proper relevants. Relevants should check that the variables required for calculation are not null and are supplied by the user. This will ensure that calculation fires only when no required variable is null and correct value is generated. In the above forms calculate field has relevant set to **${course_cnt}!=''**, so that calculate fires only when some value is entered in number of courses.  

- It is not necessary that a field which has a constraint is a required field.  It is possible to represent a case when a value may not be known but if it is known, it must meet certain characteristics. For example, if a question asks for an exam percentage, it can be left blank but if provided with an answer it should be less than or equal to 100.

.. csv-table:: **Survey**  
  :header: "type", "name", "label", "constraint", "constraint_message", "required"
  :widths: auto

  "integer", "percentage", "Enter your percentage", ".<=100", "You cannot score more than 100%", ""
