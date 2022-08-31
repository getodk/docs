Intro to Forms in ODK
========================

Forms provide a structured way to collect and provide information. Typically forms are used by data collectors (also called enumerators) who ask questions of and share information with participants. :ref:`Web forms <central-submissions-public-link>` can also be used for self-report. 

ODK forms can be used to do things like:

- Conduct a socioeconomic survey of households
- Collect geo-tagged plant species data at different points in time
- Record video and audio of wild animals for later identification
- Guide health workers through a medical triage protocol in multiple languages
- Deliver video-based agricultural training based on a farmer's responses to questions

Forms are made of fields of  :doc:`different types <form-question-types>` which can each collect or display one piece of information. Visible fields generally represent questions and are displayed differently based on their type.

Questions can be :ref:`grouped together <groups>` including :ref:`on one screen <field-list>`. They can also be :ref:`repeated <repeats>`. :doc:`Form logic <form-logic>`, :doc:`datasets <form-datasets>`, :ref:`hidden fields <hidden-questions>`, and :doc:`external apps <launch-apps-from-collect>` make it possible to create easy-to-use, but powerful forms that represent :doc:`complex data collector workflows <data-collector-workflows>`.

.. _excel-based-form-creation:

Excel-based form creation
-------------------------

Most ODK users design their forms in Excel or Google Sheets using :doc:`XLSForm <xlsform>`. Examples in this documentation use XLSForm notation to show form features.

.. _drag-and-drop-form-creation:

Drag-and-drop form creation
---------------------------
  
For simple forms, :doc:`build-intro` is a drag-and-drop form designer that works both online and offline.


.. note::

  The ODK ecosystems use XML form definitions following the `ODK XForms specification <https://getodk.github.io/xforms-spec/>`_, a subset of the `W3C XForms specification <https://www.w3.org/TR/xforms/>`_. The form creation tools described above convert user-friendly form definitions into XML.