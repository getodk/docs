Intro to Forms in ODK
========================

Forms provide a structured way to collect and provide information. Typically forms are used by :term:`enumerators <enumerator>` who ask questions of and share information with :term:`participants <participant>`. :ref:`Web forms <central-submissions-public-link>` can also be used for self-report. 

ODK forms can be used to do things like:

- Collect data about people in a pre-determined set of households
- Collect data about plant species in a particular area at different points in time
- Collect audio of animal sounds for later identification
- Guide community health workers through a diagnosis protocol
- Deliver tailored video-based agricultural training content based on a farmer's responses to questions

Forms are composed of fields of different types which can each collect or display one piece of information. Visible fields generally represent questions and are :doc:`displayed differently <form-question-types>` based on their type. Questions can be :ref:`grouped together <groups>` including :ref:`on one screen <field-list>`. They can also be :ref:`repeated <repeats>`.

:doc:`Form logic <form-logic>`, :doc:`datasets <form-datasets>` and :ref:`hidden fields <hidden-questions>` make it possible to create forms that represent complex processes.

.. _excel-based-form-creation:

Excel-based form creation
-------------------------

Most ODK users design their forms in Excel or Google Sheets using :doc:`XLSForm <xlsform>`. Examples in this documentation use XLSForm notation to show form features.

.. _drag-and-drop-form-creation:

Drag-and-drop form creation
---------------------------
  
For simple forms, :doc:`build-intro` is a drag-and-drop form designer that works both online and offline.

Technical details
------------------

The form creation tools described above convert user-friendly form definitions into XML. Form rendering or processing tools in the ODK ecosystem use XML form definitions following the `ODK XForms specification <https://getodk.github.io/xforms-spec/>`_, a subset of the `W3C XForms specification <https://www.w3.org/TR/xforms/>`_.