Updating forms
=================

.. _change-existing:

Making changes to existing form
---------------------------------

Certain changes which don't involve adding or removing a question can be made without needing to replace the existing forms. The kind of changes are:

- Changing the text or translation of a label
- Changing validations, calculations, relevants
- Changing options for a select_one or select_multiple
- Changing the order of questions
- Adding translations
- Updating media including CSVs for your form

For such changes you can update the version and re-upload the form. 

.. note::

  - If you add new media files or update existing media files for your form without any change in the form definition file or :file:`.xml` file, you don't need to change the version.
  - If you have used external select and add, update or delete the choices in external :file:`.csv` file without any change in the form definition file or :file:`.xml` file, you don't need to change the version. For more details on using external choices in your form, see `this <http://xlsform.org/#external>`_

.. tip::

  Form version in XLSForm is a string of up to 10 numbers that describes this revision. Revised form definitions must have alphabetically greater versions than previous ones. A common convention is to use strings of the form **yyyymmddrr**. For example, 2017120701 is the 1st revision from Dec 7th, 2017. 

For example:

.. csv-table:: **Survey**  
  :header: "type", "name", "label", "constraint", "constraint_message", "relevant", "read_only", "default", "required", "calculation"
  :widths: auto

  "text", "name", "Enter your name", "", "", "", "", "", "yes", ""
  "integer", "sid", "Enter your student id", "", "", "", "", "", "yes", ""
  "integer", "age", "Enter your age", ".<=18", "You should be below 18 years to be eligible for the survey.", "", "", "", "yes", ""
  "select_one dept", "course", "In which department have you chosen courses?", "", "", "", "", "", "yes", ""
  "integer", "course_cnt", "Enter number of courses you have chosen", "1<=.<=6", "You should choose atleast 1 course and atmost 6 courses.", "${course}!='none'", "", "", "yes", ""         
  "integer", "marks", "Enter total marks obtained in all courses", "", "", "${course}!='none'", "", "", "yes", ""
  "calculate", "total", "", "", "", "${course_cnt}!=''", "", "", "", "${course_cnt}*100"
  
.. csv-table:: **Choices**
  :header: "list name", "name", "label"
  :widths: auto

  "dept", "Physics", "PHY"
  "dept", "Maths", "MAT"
  "dept", "Chemsitry", "CHEM"
  "dept", "none", "none"

.. csv-table:: **Settings**
  :header: "form_title", "form_id", "default_language", "version"    
  :widths: auto

  "Example_form", "example_id", "English", "2017120700"

If you want to make the following changes to the above form:

- Add a Spanish translation
- Change the relative order of first and second question
- Change age constraint from **18** to **20**
- Change the sid field to not required
- Change label for third question from **In which department have you chosen courses?** to **Name of Department**.
- Change the calculation from **${course_cnt}*100** to **${course_cnt}*50**
- Change the relevant for calculate to **${course}!='none' and ${course_cnt}!=''**
- Change the list name in choices from **dept** to **dept_name**
- Add a new choice in deptartment list as **Computer**
- Change **Maths** to **Mathematics** and **MAT** to **MATHS** in choices

These changes can be made as:

.. csv-table:: **Survey**  
  :header: "type", "name", "label::English (en)", "label::Español (es)", "constraint", "constraint_message", "relevant", "read_only", "default", "required", "calculation"
  :widths: auto

  "integer", "sid", "Enter your student id", "Ingrese su identificación de estudiante", "", "", "", "", "", "no", ""
  "text", "name", "Enter your name", "Introduzca su nombre", "", "", "", "", "", "yes", ""
  "integer", "age", "Enter your age", "Introduzca su edad", ".<=20", "You should be below 20 years to be eligible for the survey.", "", "", "", "yes", ""
  "select_one dept_name", "course", "Name of Department", "Nombre del departamento", "", "", "", "", "", "yes", ""
  "integer", "course_cnt", "Enter number of courses you have chosen", "Ingresa el número de cursos que has elegido", "1<=.<=6", "You should choose atleast 1 course and atmost 6 courses.", "${course}!='none'", "", "", "yes", ""         
  "integer", "marks", "Enter total marks obtained in all courses", "Ingrese las calificaciones totales obtenidas en todos los cursos", "", "", "${course}!='none'", "", "", "yes", ""
  "calculate", "total", "", "", "", "", "${course}!='none' and ${course_cnt}!=''", "", "", "", "${course_cnt}*50"

.. csv-table:: **Choices**
  :header: "list name", "name", "label"
  :widths: auto

  "dept_name", "Physics", "PHY"
  "dept_name", "Mathematics", "MATHS"
  "dept_name", "Chemsitry", "CHEM"
  "dept_name", "Computer", "COMP"
  "dept_name", "none", "none"

.. csv-table:: **Settings**
  :header: "form_title", "form_id", "default_language", "version"    
  :widths: auto

  "Example_form", "example_id", "English", "2017120701"

These are the :file:`.xml` files for the above forms:

  1. :download:`example_form_v1.0 </downloads/form-update/example_form_v1.0.xml>`
  2. :download:`example_form_v1.1 </downloads/form-update/example_form_v1.1.xml>`

These are the :file:`.xlsx` files for the above forms:

  1. :download:`example_form_v1.0 </downloads/form-update/example_form_v1.0.xlsx>`
  2. :download:`example_form_v1.1 </downloads/form-update/example_form_v1.1.xlsx>`

.. note::

  You cannot change the question type or name, form id and title. 
  Example: In above form you cannot change the type from **select_one** to **select_multiple** or change name from **dept** to **department**.

.. note::

  ODK Collect treats different versions of the same form completely independently. It won't explicitly notify the users of the existence of new versions. When a user tries to get new blank forms, a form with updated version will be selected by default in the list but there will be no explicit notification unless a user tries to get new blank forms.

  .. image:: /img/form-update/get-new-version.png
   :alt: Image showing new version 2017120708 selected in the list of forms to be downloaded.
   :class: device-screen-vertical

  |

  Both versions of the form exist in the device of the user and the user will be allowed to fill an older version and submit the form to the Aggregate server. You will need to manually delete an older version from your device. 

  .. image:: /img/form-update/two-version-form.png
   :alt: Image showing two versions 2017120700 and 2017120701 in the form list.
   :class: device-screen-vertical

.. _replace-form:

Replacing existing form
---------------------------

If you need to make deeper changes like changing question type, name, form id, form title etc then you will need to create a new form with the required changes.

Once you will modify your form, the data you will collect will be stored under that new form. However, you do not need to delete the previous form, instead, you may change the name of the new form. For example, if you had form name as **Example_form**, the revised form can be named as **Example_form_1.1**. Additionally, on your Aggregate restrict the previous form by unchecking :guilabel:`Downloadable` and :guilabel:`Accept Submissions` options.

.. warning::

  If you make changes like changing a question type or name with the same form id and title and update the version, you won't be able to re-upload the form. Aggregate will reject the form upload with an error message.  

  .. image:: /img/form-update/update-error.png
    :alt: Image showing error message when trying to re-upload a form with changed question type or name.

