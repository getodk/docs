:og:image: https://docs.getodk.org/_static/img/xlsform-first-form.png

XLSForm Tutorial: Your first form
=================================

ODK forms are created using spreadsheets by following the rules of a standard called XLSForm. 

Using spreadsheet software to design forms is helpful because you can see a lot of information about your form on one screen, you can share your form definition with anyone, and you can use powerful spreadsheet features (formulas, drag to fill, copy and paste, automatic highlighting, and more).

Anyone who can use spreadsheet software can create a form! In less than 20 minutes, you'll build the school census survey shown below.

..  youtube:: 22l0xHxJ3vo
   :width: 100%

If you'd like a sneak peek at what the survey looks like for data collectors, try this `web preview <https://demo.getodk.cloud/-/single/uvOoPKYmRSpeUTab5bflNBBMT37L0u7?st=es1kN9UyLfov8T1SZEB8QCTw9gaGp6$s73b9muqj4czHlVown2UAcmyLt3uGNkcN>`_.

Goals
-----

In this tutorial, you'll:

* Design a short form using a variety of question types
* Use the major XLSForm logic building blocks
* Learn next steps to grow your skills

Ready to begin your XLSForm journey? Let's go!

Open the XLSForm template
-------------------------
You can use any spreadsheet software to create and update an XLSForm: Excel, Google Sheets, OpenOffice Calc, and more. Pick your favorite and open the XLSForm template:

* `Google Sheet <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_ (use `File > Make a copy`)
* `Microsoft Excel (XLSX) file <https://github.com/getodk/xlsform-template/raw/main/ODK%20XLSForm%20Template.xlsx>`_

Add a required text question
----------------------------

#. In the ``survey`` sheet, use the dropdown in the ``type`` column to select ``text``. This will create a text question that the user can answer.
#. In the ``name`` column, put the name of the field that will be used in analysis. Let's use ``school_name``
#. In the ``label`` column, put the label that you want the data collector to see: ``What is the school's name?``
#. In the ``required`` column, put ``yes`` to indicate that the question must be answered.

Add a required image question
-----------------------------

In the row below the school name question, let's add a required question to capture a picture of the school.

#. In the ``type`` column, put ``image``
#. In the ``name`` column, put ``school_front_picture``
#. In the ``label`` column, put ``Take a picture of ${school_name}``
#. Let's also add a hint to give data collectors more information about what we want to capture. In the ``hint`` column, put ``Include the front door``
#. In the ``required`` column, put ``yes``
#. In the ``parameters`` column, put ``max-pixels=1024`` to limit the length of captured image to 1024 pixels.

Add an optional location question
---------------------------------

#. In the ``type`` column, put ``geopoint``
#. In the ``name`` column, put ``school_location``
#. In the ``label`` column, put ``What is ${school_name}'s location?``

Add an integer question that only allows positive values
--------------------------------------------------------

#. In the ``type`` column, put ``integer``
#. In the ``name`` column, put ``student_count``
#. In the ``label`` column, put ``How many students are enrolled?``
#. In the ``required`` column, put ``yes``
#. Let's make sure that only positive student counts are allowed. In the ``constraint`` column, put ``. > 0`` to say that the entered value (``.``) must be greater than 0.
#. Let's give the data collector feedback if they enter a value that's not allowed. In the ``constraint_message`` column, put ``Must be a positive number``

Add a question for selecting multiple options
---------------------------------------------

Let's add a question that asks the data collector what grades are taught at the school. We'll show three grade choices (primary, middle, high), and let the data collector select one or more.

#. Go to the choices sheet. This sheet is used to specify lists of choices that will be used in select questions.
#. Add a choice for primary grades: 

   #. In the ``list_name`` column, put the name of the list that all of our choices will belong to: ``grades``
   #. In the ``name`` column, put the value that will be stored in the data that we will analyze: ``primary``
   #. In the ``label`` column, put the text that data collectors will see for the choice: ``Primary (1-5)``
#. Add a choice for middle grades:

   #. In the ``list_name`` column, put ``grades`` to put this choice in the same list as above.
   #. In the ``name`` column, put ``middle``
   #. In the ``label`` column, put ``Middle (6-8)``
#. Add a choice for high grades:

   #. In the ``list_name`` column, put ``grades`` to put this choice in the same list as above.
   #. In the ``name`` column, put ``high``
   #. In the ``label`` column, put ``High (9-12)``
#. Go back to the ``survey`` sheet.
#. In the row after the ``student_count`` question, put ``select_multiple grades`` in the ``type`` column.
  
   .. note::
     Your spreadsheet software will show a validation warning because it doesn't know about your list name (``grades``). That's expected for select questions and can be safely ignored.

#. In the ``name`` column, put ``grades_taught``
#. In the ``label`` column, put ``What grades are taught?``
#. In the ``required`` column, put ``yes``
#. Let's make the choices appear horizontally next to each other. In the ``appearance`` column, put ``columns``

Add a question that is shown depending on a previous answer
-----------------------------------------------------------

#. In the ``type`` column, put ``text``
#. In the ``name`` column, put ``advanced_math``
#. In the ``label`` column, put ``What is the most advanced math class available?``
#. In the ``required`` column, put ``yes``
#. Let's make this question appear only if the school teaches high school grades. In the ``relevant`` column, put ``selected(${grades_taught}, 'high')``

Specify the form's title and ID
-------------------------------

#. Go to the ``settings`` sheet.
#. In the ``form_title`` column, put a title that people who interact with this form should see: ``Verdant school district census 2023``
#. In the ``form_id`` column, put an ID that uniquely identifies this form: ``school_census_23``
#. In the ``instance_name`` column, put a name that identifies each submission of this form: ``${school_name}``

Try your form in Central
------------------------

.. note::
   Don't yet have an ODK Central server? :ref:`getting-started-get-central` or use `XLSForm Online <https://getodk.org/xlsform>`_ to try your form in a web browser.

#. Save or download your form as an XLSX file.
#. Log into your Central server.
#. If you don't already have a Project, create one and give it a name.
#. Click on the New button next to ``Forms``.
#. Drag and drop your XLSX file onto the file uploader.
   
   .. image:: /img/xlsform-first-form/school-census-upload.*
     :scale: 30%
     :alt: ODK Central's form upload dialog.

#. Click the :guilabel:`Preview` button to see your form in your web browser 🎉
  
   .. image:: /img/xlsform-first-form/school-census-draft.*
     :alt: ODK Central showing a draft of the school census form. There's a red box around the Preview button with an arrow pointing to it.

   .. image:: /img/xlsform-first-form/school-census-preview.*
     :alt: ODK Central showing a web preview of the school census form.
     :align: center

#. To see the form in the `ODK Collect mobile app <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_, click on the :guilabel:`Testing` tab and scan the QR code with Collect.

Your turn
----------

#. Can you make the location question required?
#. Can you make the grade level question show only if more than 100 students are enrolled?
#. Can you show the grade level options vertically rather than horizontally? (Hint: The vertical layout is the default appearance for selects)

Next steps
----------
Congratulations! You've now designed a form that uses most of the XLSForm building blocks. Below are more resources to grow your skills.

* Deepen your understanding

  * :doc:`XLSForm introduction <xlsform>`
  * :doc:`Question types <form-question-types>`
  * :ref:`Required questions <requiring-responses>`
  * :ref:`Constraints on user input <constraints>`
  * :ref:`Selects <select-widgets>`
  * :ref:`Relevance <relevants>`

* Broaden your knowledge

  * :ref:`groups`
  * :doc:`form-styling`
  * :doc:`form-language`
  * :doc:`form-operators-functions`

* :doc:`ODK Collect introduction <collect-intro>`