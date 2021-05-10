.. spelling::

  xform
  xlsx
  yyyymmddrr
  th

XLSForm
=======

.. _xlsform-introduction:

:dfn:`XLSForm` is a standard for building forms in Excel. XLSForms are simple to get started with and can represent complex forms. 

XLSForms can be created and edited by any application that works with ``.xlsx`` documents. This means that they are portable and can leverage many useful features commonly available in spreadsheet applications such as formulas, comments and document versioning. 

Many users choose to use Google Sheets or Excel for the web so that they can collaborate on or publicly share their forms.

One way to get started is by downloading or making a copy of `this form definition template <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_. You can hover over columns to see guidance about how to use them. The `All Widgets form definition <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ>`_ shows examples of all of the different user-visible question types.

The ODK documentation shows all form design examples as XLSForms and describes how XLSForms are used by ODK tools. There is also a general tutorial for building XLSForms on the `XLSForm website <http://xlsform.org/>`_.

Once your form has been designed, you can :ref:`upload the XLSForm directly to Central <central-forms-upload>`.

.. tip::

  If your ODK server does not have the latest XLSForm features or you need to temporarily preview a form in a browser, try `XLSForm Online <https://getodk.org/xlsform>`_.

  If you need to design XLSForms offline or your form has sensitive data that you'd rather not upload into XLSForm Online, use the `pyxform <https://github.com/XLSForm/pyxform>`_ command line tool.

.. _survey-sheet:

The survey sheet
------------------

At minimum, an XLSForm has a sheet named **survey** to describe the types and order of fields in a form. It must have these three columns:

- :th:`type`: the type of the field represented by each row. Supported types and how they are displayed are described :doc:`here <form-question-types>`.
- :th:`name`: the name of the field represented by each row. This name will be used in your data results. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``date_of_birth``.
- :th:`label`: the user-visible question text for the field represented by each row. For example: ``When was ${first_name} born?`` This text can :ref:`reference other fields <variables>` or :doc:`have translations <form-language>`.

The survey sheet can have many other columns to represent different :doc:`question types <form-question-types>` and :doc:`form logic <form-logic>`. You can see the most commonly-used columns in `this template <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_.

.. _settings-sheet:

The settings sheet
--------------------

You should also include a **settings** sheet to uniquely identify your form definition and its current version. We recommend specifying at least the following columns:

- :th:`form_title`: The title that will be displayed by tools that list this form.
- :th:`form_id`: The unique ID that identifies this form to tools that use it. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``bench_inventory_2021``.
- :th:`version`: The unique version code that identifies the current state of the form. A common convention is to use a format like yyyymmddrr. For example, ``2017021501`` is the 1st revision from Feb 15th, 2017.
- :th:`instance_name`: An :ref:`expression <expressions>` that will be used to represent a specific filled form created from this form definition. For example, ``concat(${first_name}, ${age})``. :ref:`Learn more <instance-name>`.

The **settings** sheet is also useful when using :ref:`multi-language forms <switching-languages>` or when defining a form with :ref:`encryption <defining-encrypted-form>`.

.. _instance-name:

Naming filled forms
~~~~~~~~~~~~~~~~~~~~~

In an XLSForm's **settings** sheet, you can add an :th:`instance_name` column and specify an :ref:`expression <expressions>` to use a specific filled form's contents in its name. This name will be shown in several places to help guide data collection and analysis. You should pick a name that uniquely identifies the filled form and the data it had captured. For example:

- If a single filled form represents data about a real-world thing like a person or park bench, your :th:`instance_name` expression should include some information to uniquely identify the thing like the person's name or the park bench's location and current status.
- If a single filled form represents data about an observation, consider including the date and time of the observation in the :th:`instance_name` expression.
- If your form definition includes a repeat, consider including the repeat count in the :th:`instance_name` expression.

.. _instance-name-collect:

Filled form names in Collect
""""""""""""""""""""""""""""""

Each filled form is identified by its :th:`instance_name` value in :doc:`Collect <collect-intro>`'s :guilabel:`Edit Saved Form`, :guilabel:`Send Finalized Form` and :guilabel:`View Sent Form` lists. 

In workflows where forms have to be be filled in multiple different steps, a useful :th:`instance_name` expression will make it much easier to find which filled form to edit. If forms only have to be edited under certain conditions (e.g. not all household members were available), you can include this status in the :th:`instance_name`.

In the :guilabel:`View Sent Form` list, :th:`instance_name` can be helpful to identify which data collection tasks have been completed. For example, if a data collector needs to interview 25 specific people and the :th:`instance_name` for each filled form identifies the respondent, they can go to :guilabel:`View Sent Form` to verify which subset of interviews they have already completed. 

A sent form's :th:`instance_name` is maintained after it is deleted. This makes it possible to confirm what work has been completed even if submissions are configured to :ref:`delete after send <delete-after-send>`. However, it does mean sensitive data should be avoided in :th:`instance_name`.

The :th:`instance_name` is also used to identify filled forms in Collect's :doc:`filled form map <collect-form-map>`.


.. _choices-sheet:

The choices sheet
--------------------

If you have :ref:`multiple choice questions <select-widgets>`, you will also need a **choices** sheet to specify choices for those questions. It must have these three columns:

- :th:`list_name`: The unique ID that identifies a group of choices. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``yes_no_maybe``.
- :th:`name`: the name of the field represented by each row. This name will be used in your data results. It may not contain spaces and must start with a letter or underscore. For example you might use ``1`` or ``y`` for Yes and ``-1`` or ``n`` for No.
- :th:`label`: the user-visible text for the choice represented by each row. For example: ``Yes``, ``No``, and ``Maybe``. This text can :ref:`reference other fields <variables>` or :doc:`have translations <form-language>`.

Choices with the same list name are considered part of a related set of choices and will appear together for a question. This also allows a set of choices to be reused for multiple questions (for example, yes/no questions).
