XLSForm
=======

.. _xlsform-introduction:

:dfn:`XLSForm` is a standard for designing forms in Excel. XLSForms are simple to get started with and can represent complex forms. 

XLSForms can be created and edited by any application that works with ``.xlsx`` documents. This means that they are portable and can leverage many useful features commonly available in spreadsheet applications such as formulas, comments, and document versioning. 

Many users choose to use Google Sheets or Excel for the web so that they can collaborate on or publicly share their forms. The best way to get started with XLSForm is with the tutorial below.

* :doc:`XLSForm tutorial <xlsform-first-form>`

If you are more adventurous, you can skip the tutorial, make a copy of the form template below, and learn to design your form that way.

* `Google Sheet <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_ (use `File > Make a copy`)
* `Microsoft Excel (XLSX) file <https://github.com/getodk/xlsform-template/raw/main/ODK%20XLSForm%20Template.xlsx>`_

Once your form has been designed, you can :ref:`upload the XLSForm directly to your ODK Central server <central-forms-upload>`. If your ODK server does not have the latest XLSForm features or you need to temporarily preview a form in a browser, try `XLSForm Online <https://getodk.org/xlsform>`_.

The ODK documentation shows all form design examples as XLSForms and describes how XLSForms are used by ODK tools. The `All Widgets form <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ>`_ has examples of all of the different user-visible question types.

.. _survey-sheet:

The survey sheet
----------------

At minimum, an XLSForm has a sheet named **survey** to describe the types and order of fields in a form. It must have these three columns:

- ``type``: the type of the field represented by each row. Supported types and how they are displayed are described :doc:`here <form-question-types>`.
- ``name``: the name of the field represented by each row. This name will be used in your data results. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``date_of_birth``.
- ``label``: the user-visible question text for the field represented by each row. For example: ``When was ${first_name} born?`` This text can :ref:`reference other fields <variables>` or :doc:`have translations <form-language>`.

The survey sheet can have many other columns to represent different :doc:`question types <form-question-types>` and :doc:`form logic <form-logic>`. You can see the most commonly-used columns in `this template <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_.

.. _choices-sheet:

The choices sheet
-----------------

If you have :ref:`multiple choice questions <select-widgets>`, you will also need a **choices** sheet to specify choices for those questions. It must have these three columns:

- ``list_name``: The unique ID that identifies a group of choices. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``yes_no_maybe``.
- ``name``: the name of the field represented by each row. It may not contain spaces and must start with a letter or underscore. This name will be used in your data results so it's best to use a short and descriptive name (e.g., ``y`` for Yes and ``n`` for No).
- ``label``: the user-visible text for the choice represented by each row. For example: ``Yes``, ``No``, and ``Maybe``. This text can :ref:`reference other fields <variables>` or :doc:`have translations <form-language>`.

Choices with the same list name are considered part of a related set of choices and will appear together for a question. This also allows a set of choices to be reused for multiple questions (for example, yes/no questions).

.. _settings-sheet:

The settings sheet
------------------

You should also include a **settings** sheet to uniquely identify your form definition and its current version. We recommend specifying at least the following columns:

- ``form_title``: The title that will be displayed by tools that list this form.
- ``form_id``: The unique ID that identifies this form to tools that use it. It may not contain spaces and must start with a letter or underscore. Use a descriptive name less than 64 characters. For example: ``bench_inventory_2021``.
- ``version``: The unique version code that identifies the current state of the form. A common convention is to use a format like yyyymmddrr. For example, ``2017021501`` is the 1st revision from Feb 15th, 2017.
- ``instance_name``: An :ref:`expression <expressions>` that will be used to represent a specific filled form created from this form definition. For example, ``concat(${first_name}, "-", ${age})``. :ref:`Learn more <instance-name>`.

The **settings** sheet is also useful when using :ref:`multi-language forms <switching-languages>` or when defining a form with :ref:`encryption <defining-encrypted-form>`.

.. _instance-name:

Naming filled forms
~~~~~~~~~~~~~~~~~~~

In an XLSForm's **settings** sheet, you can add an ``instance_name`` column and specify an :ref:`expression <expressions>` to use a specific filled form's contents in its name. This name will be shown in several places to help guide data collection and analysis. You should pick a name that uniquely identifies the filled form and the data it had captured. For example:

- If a single filled form represents data about a real-world thing like a person or park bench, your ``instance_name`` expression should include some information to uniquely identify the thing like the person's name or the park bench's location and current status.
- If a single filled form represents data about an observation, consider including the date and time of the observation in the ``instance_name`` expression.
- If your form definition includes a repeat, consider including the repeat count in the ``instance_name`` expression.

.. _instance-name-collect:

Filled form names in Collect
""""""""""""""""""""""""""""

Each filled form is identified by its ``instance_name`` value in :doc:`Collect <collect-intro>`'s :guilabel:`Edit Saved Form`, :guilabel:`Send Finalized Form` and :guilabel:`View Sent Form` lists. 

In workflows where forms have to be be filled in multiple different steps, a useful ``instance_name`` expression will make it much easier to find which filled form to edit. If forms only have to be edited under certain conditions (e.g. not all household members were available), you can include this status in the ``instance_name``.

In the :guilabel:`View Sent Form` list, ``instance_name`` can be helpful to identify which data collection tasks have been completed. For example, if a data collector needs to interview 25 specific people and the ``instance_name`` for each filled form identifies the respondent, they can go to :guilabel:`View Sent Form` to verify which subset of interviews they have already completed. 

A sent form's ``instance_name`` is maintained after it is deleted. This makes it possible to confirm what work has been completed even if submissions are configured to :ref:`delete after send <delete-after-send>`. However, it does mean sensitive data should be avoided in ``instance_name``.

The ``instance_name`` is also used to identify filled forms in Collect's :doc:`filled form map <collect-form-map>`.

.. _instance-name-central:

Filled form names in Central
""""""""""""""""""""""""""""

Each submission in Central has its own :ref:`detail page <central-submissions-details>` which provides basic information about the submission, an activity history of action and discussion on that submission.

The title at the top is pulled from the ``instance_name`` and it makes navigation much easier to have friendly names at the top of the page and in the web browser title and tab.

.. _entities-sheet:

The entities sheet
-------------------

:doc:`Entities <central-entities>` let you share information between forms so you can collect longitudinal data, manage cases over time, and support other complex workflows.

Review the :doc:`Entities page <central-entities>` to learn more about what Entities are and how to use them.
