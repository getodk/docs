.. spelling::
  openRowInitialElementKeyToValueMap
  newRowInitialElementKeyToValueMap
  exampleForm
  isSessionVariable
  keyMapLongCol
  keyMapLatCol
  keyColorRuleType
  mapListViewFileName
  listViewFileName
  defaultViewFileName
  defaultViewType
  hindi
  templatePath
  attr
  inputAttributes
  hideInContents
  detailViewFileName


ODK XLSX Converter Reference
================================

.. contents:: :local:

.. _xlsx-ref-worksheets:

Excel Worksheets
------------------------------

A workbook is composed of one or more worksheets. XLSX Converter expects the worksheets within a workbook to use the following nomenclature.

.. list-table:: Worksheet Reference Table
  :header-rows: 1

  * - Worksheet
    - Required?
    - | Description
  * - :ref:`survey <xlsx-ref-survey>`
    - Required
    - | Contains the content and control flow of the
      | survey. It contains the full list of questions
      | and determines the order in which they will be
      | asked. This worksheet can be broken into
      | different section worksheets for ease of use.
  * - :ref:`settings <xlsx-ref-settings>`
    - Required
    - | Includes such details as the form name and id,
      | as well as the default language.
  * - :ref:`properties <xlsx-ref-properties>`
    - Optional
    - | Defines the key-value properties that can
      | specify the detail, list view, and other
      | properties to use with this table. This sheet
      | should only be specified in forms whose
      | :th:`form_id` matches their :th:`table_id`.
  * - :ref:`calculates <xlsx-ref-calculates>`
    - Optional
    - | Contains the JavaScript formulas that can be
      | used in other worksheets
  * - :ref:`choices <xlsx-ref-choices>`
    - Optional
    - | Contains the sets of choices for multiple
      | choice questions. Each row represents a
      | response. Choices with the same
      | :th:`choice_list_name` are considered to be
      | part of the same choice set. Choice sets can
      | be used multiple times throughout a survey
      | (such as a yes/no choice set).
  * - :ref:`model <xlsx-ref-model>`
    - Optional
    - | Defines the table definition in cases where
      | multiple forms edit the same data table
  * - :ref:`queries <xlsx-ref-queries>`
    - Optional
    - | Gets data from an external source that can
      | be used as the choice set for multiple
      | choice or :tc:`linked_table` questions much like
      | the choices worksheet.
  * - :ref:`user_defined_section <xlsx-ref-user-defined>`
    - Optional
    - | Worksheets with custom section names can be
      | used in conjunction with the survey worksheet
      | to simplify control flow.
  * - :ref:`prompt_types <xlsx-ref-custom-prompt-types>`
    - Optional
    - | Defines custom prompt types that can be used
      | within a survey.
  * - :ref:`column_types <xlsx-ref-column-types>`
    - Optional
    - | Defines custom column types that are formulas,
      | functions, or pathnames.
  * - :ref:`framework_translations <xlsx-ref-framework-translations>`
    - Required
    - | ONLY :file:`framework.xlsx`. Translations for
      | standard prompts.
  * - :ref:`common_translations <xlsx-ref-common-translations>`
    - Optional
    - | ONLY :file:`framework.xlsx`. Application-wide
      | translations.
  * - :ref:`table_specific_translations <xlsx-ref-table-translations>`
    - Optional
    - | Only in :th:`form_id` matching :th:`table_id`.
      | Translations specific to a given :th:`table_id`.

.. note::

  Each worksheet has a set of required and optional columns. For the XLSX workbook to be valid, all entries must have legal values in the required columns. Optional columns can be left blank at any point, and omitted entirely if not used.

.. _xlsx-ref-survey:

Survey
~~~~~~~~~~~~~~~~~~~~~~~~~

All XLSX Converter form definitions require a **survey** sheet. The **survey** worksheet contains the structure and most of the content of the form. It contains the full list of questions and information about how those questions should be presented. Most rows represent a question; the rest of the rows specify control structures such as screen groups. Blank rows are ignored.

.. note::

  In this document, questions and question types will also be referred to as prompts and prompt types.

There are many prompts available for form development. Some ask the user a question and get a response, but other prompts are simply informational and referring to them as questions is not semantically correct.

.. _xlsx-ref-survey-req-cols:

Required Columns
"""""""""""""""""""""""

A list of the required columns for a **survey** worksheet follows.

.. list-table:: Survey Worksheet Required Columns
  :header-rows: 1

  * - Column
    - | Description
  * - type
    - | The prompt type that will be used to display information to the user. Prompt
      | types can also be used to get data from a user.
  * - name
    - | The name of the prompt type. This name will be used throughout the workbook
      | to reference the prompt.
  * - display.prompt
    - | A string token identifying the translation entry that can define the text,
      | audio, image and video to display for this prompt.
      |
      | Alternatively, this column can be omitted and the prompt text can be
      | specified directly via the :th:`display.prompt.text` column.

.. _xlsx-ref-survey-opt-cols:

Optional Columns
"""""""""""""""""""""""

A list of the optional columns that can be incorporated into a **survey** worksheet is below.

.. list-table:: Survey Worksheet Optional Columns
  :header-rows: 1

  * - Column
    - | Description
  * - branch_label
    - | Used to identify which part of the survey to branch to when
      | used with a :tc:`goto` clause or :tc:`user_branch` prompt.
  * - calculation
    - | When used with the :tc:`assign` prompt type, assigns a value to a
      | prompt type.
  * - choice_filter
    - | Used to filter the choices of a multiple choice or
      | :tc:`linked_table` prompt.
  * - clause
    - | Used in conjunction with the :th:`condition` column to manage the
      | control flow of the survey. :th:`clause` and :th:`condition` control which
      | questions get asked in what order, if at all. The :th:`clause` column
      | contains control flow options such as :tc:`if`, and the :th:`condition`
      | column contains a predicate to determine if action will occur.
      | :tc:`if` statements always require a :th:`condition` statement. For other
      | :th:`clause` statements, a blank :th:`condition` column is assumed to
      | be true. Other commands include :tc:`begin screen`, :tc:`end screen`,
      | and :tc:`do section`.
  * - comments
    - | Never displayed to the user. Used for development purposes to
      | leave comments about the form for future reference. It is good
      | style to comment your work.
  * - condition
    - | Used with the :th:`clause` column to manage the control flow of the
      | survey. :th:`clause` and :th:`condition` control which questions get
      | asked in what order, if at all. The :th:`clause` column contains
      | control flow options such as :tc:`if`, and the :th:`condition` column
      | contains a predicate to determine if the following actions will
      | occur.
  * - constraint
    - | Takes a JavaScript expression. User cannot navigate forward
      | until the constraint evaluates to true. If left blank, its
      | default value is true.
  * - default
    - | Used to set the default value.
  * - display.constraint_message
    - | A string token identifying the translation entry with the
      | text shown to the user if the constraint is violated.
      |
      | Alternatively, this column can be omitted and this text
      | can be specified directly via the
      | :th:`display.constraint_message.text` column.
  * - display.constraint_message.text
    - | Message displayed to user if the constraint is violated.
      | Tells the user what needs to change before they can
      | continue.
  * - display.hint
    - | A string token identifying the translation entry with the text
      | to display in italics and a smaller font than
      | :th:`display.prompt.text`.
      |
      | Alternatively, this column can be omitted and this text can be
      | specified directly via the :th:`display.hint.text` column.
  * - display.hint.text
    - | Used to display text in italics and a smaller font than
      | :th:`display.prompt.text`. Can be used to provide extra instructions
      | to the user.
  * - display.prompt
    - | A string token identifying the translation entry that can define
      | the text, audio, image and video to display for this prompt.
      |
      | Alternatively, this column can be omitted and this information
      | can be specified directly via the :th:`display.prompt.*` columns.
  * - display.prompt.audio
    - | Allows the user to play an audio recording. Requires a relative
      | path to where the recording is saved. If saved in the same
      | folder as the :file:`formDef.json`, then only the filename of the
      | recording needs to be specified.
      |
      | Alternatively, this can be specified on the translations sheet
      | under the :th:`display.prompt` string token (under the
      | :th:`display.audio` column heading).
  * - display.prompt.image
    - | Used to display an image. Requires a relative path to where
      | the image is saved. If saved in the same folder as the
      | :file:`formDef.json`, then only the image file name and the
      | extension (for example :file:`.jpg`, :file:`.gif`) are needed.
      |
      | Alternatively, this can be specified on the translations sheet
      | under the :th:`display.prompt` string token (under the
      | :th:`display.image` column heading).
  * - display.prompt.text
    - | The text that the user will see for this prompt type.
      |
      | Alternatively, this can be specified on the translations sheet
      | under the :th:`display.prompt` string token (under the
      | :th:`display.text` column heading).
  * - display.prompt.video
    - | Allows the user play a video. Requires a relative path to where
      | the video is saved. If saved in the same folder as the
      | :file:`formDef.json`, then only the filename of the video needs to be
      | specified.
      |
      | Alternatively, this can be specified on the translations sheet
      | under the :th:`display.prompt` string token (under the
      | th:`display.video` column heading).
  * - display.title
    - | A string token identifying the translation entry that can
      | define the text to display for this prompt in the contents
      | screen and as the column name in ODK Tables.
      |
      | Alternatively, this column can be omitted and this information
      | can be specified directly via the :th:`display.title.text` column.
  * - display.title.text
    - | The display value the user sees when the prompt is displayed
      | in the contents screen.
      |
      | Alternatively, this can be specified on the translations sheet
      | under the :th:`display.title` string token (under the
      | th:`display.text` column heading).
  * - hideInContents
    - | Legal value is true. If true, then the prompt on the same row
      | will not be displayed on the contents screen.
  * - inputAttributes.<attr>
    - | This column can be used in conjunction with the following
      | prompt types: :tc:`string`, :tc:`text`, :tc:`integer`, :tc:`decimal`. The :code:`<attr>` can
      | specify an HTML attribute to be added to the prompt types.
      | For example, :th:`inputAttributes.min` with a value of 5 would add
      | :code:`min=”5”` into the HTML element for the prompt type.
  * - model.isSessionVariable
    - | Legal value is true. If true, then the data value for the prompt
      | will be treated as a session variable and won't be saved.
  * - required
    - | Takes a JavaScript expression. If true, the user will not be able
      | to navigate to the next screen until the question is answered.
      | If left blank, its default value is false.
  * - templatePath
    - | Must be specified if using a custom :command:`handlebars` template.
      | Requires a relative path to where the template is saved. If
      | saved in the same folder as the :file:`formDef.json`, then only the
      | filename of the template needs to be specified.
  * - value_list
    - | Must be used with the **choices** worksheet. The :th:`value_list`
      | column of the **survey** worksheet connects to the
      | :th:`choice_list_name` column on the **choices** worksheet.

.. _xlsx-ref-survey-prompt-types:

Prompt Types
"""""""""""""""""""""""""""""

The following prompt types are available in ODK Survey.

.. list-table:: Survey Prompt Types
  :header-rows: 1

  * - Prompt Type
    - | Description
  * - acknowledge
    - | Used to display a message to the user and have them click a checkbox
      | to acknowledge that they have read the message.
  * - assign
    - | Used for internal assignment of a variable.
  * - audio
    - | Used to capture an audio recording.
  * - barcode
    - | Used to capture a barcode.
  * - date
    - | Uses a date picker widget to capture a date.
  * - datetime
    - | Uses a date time picker widget to capture a date and time.
  * - decimal
    - | Used to display a message to the user and have them enter a decimal.
  * - geopoint
    - | Used to capture a GPS location.
  * - image
    - | Used to capture an image.
  * - integer
    - | Used to display a message to the user and have them enter an integer
  * - linked_table
    - | Used to display the instances of table and allows the user to add
      | another instance, edit an existing instance, or delete an instance.
  * - note
    - | Used to display a message to the user.
  * - select_multiple
    - | Used to ask the user a multiple choice question and allows the user
      | to click multiple checkboxes.
  * - select_multiple_grid
    - | Used to ask the user a multiple choice question, displays the
      | choices to the user in a grid, and allows the user to click
      | multiple grid items.
  * - select_multiple_inline
    - | Used to ask the user a multiple choice question, displays the
      | choices to the user inline, and allows the user to click multiple
      | items.
  * - select_one
    - | Used to ask the user a multiple choice question and allows the user
      | to click one item.
  * - select_one_dropdown
    - | Used to ask the user a multiple choice question and allows the user
      | to select one item from a dropdown box.
  * - select_one_grid
    - | Used to ask the user a multiple choice question and allows the user
      | to select one item from a grid.
  * - select_one_inline
    - | Used to ask the user a multiple choice question, displays the choices
      | to the users inline, and allows the user to click one item.
  * - select_one_with_other
    - | Used to ask the user a multiple choice question, displays the choices
      | to the user, and allows the user to click one item. One of the
      | choices provided is an other option which if clicked provides a text
      | box for the user to enter a value.
  * - string
    - | Used to ask the user a question and allows them to enter a string.
  * - text
    - | Used to ask the user a question and allows them to enter text.
  * - time
    - | Uses a time picker widget to capture a time.
  * - user_branch
    - | Used to allow the user to pick which section of the form they would
      | like to enter.
  * - video
    - | Used to capture a video.

.. _xlsx-ref-settings:

Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Settings Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - setting_name
    - | The name of the setting within the form
  * - value
    - | The value for the setting
  * - display.title
    - | A string token identifying the translation entry with the text shown to the user
      | when the (survey) title is displayed.
      |
      | Alternatively, this column can be omitted and this text can be specified directly
      | via the :th:`display.title.text` column.
  * - display.locale
    - | A string token identifying the translation entry with the text shown to the user
      | when the translation locale is displayed.
      |
      | Alternatively, this column can be omitted and this text can be specified directly
      | via the :th:`display.locale.text` column.

Available :th:`setting_name` values that can be used:

.. list-table:: :th:`setting_name` values
  :header-rows: 1

  * - | Value
    - | Required?
    - | Description
  * - table_id
    - | Required
    - | The unique id of the table that the form data gets
      | stored in.
  * - survey
    - | Required
    - | Specify the title of the form via content of the
      | :th:`display.title.text` column. That value will
      | appear as the title to the user.
  * - form_id
    - | Optional
    - | A unique identifier for the form. Default value is
      | the unique id that ODK Survey uses to identify the
      | form.
  * - form_version
    - | Optional
    - | A value used for version control of the form. The
      | recommended format is yearmonthday (for example:
      | 20131212 to say the 12th of December 2013).
  * - <section_name>
    - | Optional
    - | Used with :th:`display.title.text` to set how the
      | section name will appear to the user on the contents
      | screen.
  * - instance_name
    - | Optional
    - | Used to display the name of saved instances of the form.
      | This must be the name of a prompt type from the **survey**
      | worksheet.
  * - default
    - | Optional
    - | Used with :th:`display.prompt.text` (no qualifier), or
      | other fields to set the default translation of a UI
      | element. Specify label under :th:`display.locale.text`
  * - <language>
    - | Optional
    - | Used with :th:`display.prompt.text.<language>`, or
      | other fiels to set other language options in the form.

A sample **settings** worksheet might look like this:

.. list-table:: Settings Worksheet Example
  :header-rows: 1

  * - setting_name
    - Value
    - :th:`display.title.text`
    - display.locale.text
    - display.locale.text.hindi
  * - table_id
    - sample_form
    -
    -
    -
  * - form_version
    - 20130819
    -
    -
    -
  * - survey
    -
    - Sample Form
    -
    -
  * - default
    -
    -
    - English
    - English (as Hindi name)
  * - hindi
    -
    -
    - Hindi
    - Hindi (as Hindi name)

.. tip::

  If the survey has been broken up into multiple worksheets, each worksheet can be assigned its own title by adding a row for it and filling in the :th:`display.title.text` column.

.. tip::

  In the case of multiple languages, the :th:`display.locale.text` column determines how the different language options are presented to the user.

.. _xlsx-ref-properties:

Properties
~~~~~~~~~~~~~~~~~~~~~~~~~

This holds the key-value settings for specifying detail and list views, and other parameters.
The columns in this sheet are:

.. list-table:: Properties Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - partition
    - | The class of property to set
  * - aspect
    - |
  * - key
    - | The name of the property to set
  * - type
    - | Valid options: object, array, rowpath, configpath, string, integer, number, boolean
  * - value
    - | The value of the property to set

For example, the following configuration specifies that the default view for the table is the list view (HTML). It also defines the detail view, list view, and map view HTML files. And, for the map view, it defines the color rule to apply to the pins in the map view and the latitude and longitude columns to use in displaying those pins.

.. list-table:: Properties Worksheet Example Table
  : header-rows: 1

  * - partition
    - aspect
    - key
    - type
    - value
  * - Table
    - default
    - defaultViewType
    - string
    - LIST
  * - Table
    - default
    - detailViewFileName
    - string
    - config/tables/Tea_houses/html/Tea_houses_detail.html
  * - Table
    - default
    - listViewFileName
    - string
    - config/tables/Tea_houses/html/Tea_houses_list.html
  * - Table
    - default
    - mapListViewFileName
    - string
    - config/tables/Tea_houses/html/Tea_houses_list.html
  * - TableMapFragment
    - default
    - keyColorRuleType
    - string
    - None
  * - TableMapFragment
    - default
    - keyMapLatCol
    - string
    - Location_latitude
  * - TableMapFragment
    - default
    - keyMapLongCol
    - string
    - Location_longitude

.. _xlsx-ref-calculates:

Calculates
~~~~~~~~~~~~~~~~~~~~~~~~~

The **calculates** worksheet is an optional worksheet.

.. list-table:: Calculates Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - calculation_name
    - | The name used to reference the calculation in other worksheets.
  * - calculation
    - | The JavaScriptf forumla to be evaluated.


Each row of the **calculates** page represents a function that can be used elsewhere in the workbook by referencing the individual :th:`calculation_name`. The :th:`calculation` column can store any valid JavaScript expression. In general,

.. note::

  Calculations are referenced in the :th:`condition` column of **survey** worksheets.

.. tip::

  There are  built in functions for ODK Survey that can be used anywhere in the workbook. See the :ref:`Forumla Functions <xlsx-ref-formula>` section for more details.

If a complex calculation is required, you can access the full power of Javascript and the :program:`jquery.js` (that is: :code:`$.some_func(...)` ) and :program:`underscore.js` (that is: :code:`_.some_func(...)` ) libraries. Internally, the calculate column is wrapped and evaluated as a Javascript function:

.. code-block:: javascript

  function() {
      return (YOUR_CALCULATE_COLUMN_CONTENT_HERE);
  }

You can write your own code to perform a join via defining and invoking an anonymous function in your calculate. Here is an example:

.. code-block:: javascript

  (function() {
      var result = "";
      _.each(data('valueListField'), function(element) {
          result = result + ", " + element;
      });
      return result.substring(2);
  }) ()

This defines a function and then invokes it. The available functions within a calculates expression are the following:

.. list-table:: Available Calculates Functions
  :header-rows: 1

  * - Function
    - | Description
    - Usage
  * - :code:`data(fieldName)`
    - | Retrieve the value stored under this fieldName
    - :code:`data('myField')`
  * - :code:`metadata(instanceMetadataFieldName)`
    - | Retrieve value stored under this name
    - :code:`metadata('_group_modify')`
  * - :code:`selected(promptValue, qValue)`
    - | Test whether qValue occurs within a select-multiple
    - :code:`selected(data('mySelectMultipleField'),'myChoiceDataValue')`
  * - :code:`countSelected(promptValue)`
    - | Count the number of selections in a select-multiple
    - :code:`countSelected(data('mySelectMultipleField'))`
  * - :code:`equivalent(promptValue1, promptValue2, ...)`
    - | Test if values are equivalent
    - :code:`equivalent(data('promptA'), data('promptB'))`
  * - :code:`not(conditional)`
    - | Negate a condition ( equivalent to !(conditional) )
    - :code:`not(data('fieldA') === data('fieldB'))`
  * - :code:`now()`
    - | Return the current time
    -
  * - :code:`isFinalized()`
    - | Return whether or not the current row is finalized
    -
  * - :code:`assign(fieldName, value)`
    - | Store value in fieldName and return value.
    - :code:`(8 + assign('myField', 5))*10`

Additionally, the following functions are also available, but are generally not useful in calculates. They are used within template helper functions (:file:`…/system/survey/js/handlebarsHelpers.js`).

.. list-table:: Template Helper Functions
  :header-rows: 1

  * - Function
    - | Description
    - Usage
  * - :code:`getCurrentLocale()`
    - | Return the currently-active locale
    -
  * - :code:`localize(locale, displayProperty)`
    - | Localize the given display.xxx text
    - :code:`localize(getCurrentLocale(), display.hint)`
  * - :code:`width(string)`
    - | Determine the rendered width of a string
    -
  * - :code:`expandFormDirRelativeUrlPath(content)`
    - | Return url for a file within the form directory.
    -

And, finally, you can also reference the *opendatakit* object (that is: :code:`opendatakit.some_func(...)` ) within these functions (:file:`system/survey/js/opendatakit.js`).


.. _xlsx-ref-choices:

Choices
~~~~~~~~~~~~~~~~~~~~~~~~~

The **choices** sheet allows you to specify the set of choices for multiple choice prompts.

.. list-table:: Choices Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - choice_list_name
    - | The name used to reference the set of choices. This name must be the same
      | as the :th:`values_list` in the **survey** worksheet.
  * - data_value
    - | The value that gets stored as the user’s response.
  * - display.title
    - | A string token identifying the translation entry with the text shown to
      | the user for this choice value.
      |
      | Alternatively, this column can be omitted and this text can be
      | specified directly via the :th:`display.title.text` column.
  * - display.title.text
    - | The text that the user sees for this choice.
  * - display.title.image
    - | An image that the user will see associated with a particular choice.

.. _xlsx-ref-model:

Model
~~~~~~~~~~~~~~~~~~~~~~~~~

The **model** sheet is an optional sheet that allows you to specify the data model for the :th:`table_id` specified in the **settings** worksheet.

.. list-table:: Model Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - name
    - | The name of the data field to be used in :th:`table_id`
  * - type
    - | The type of data that can be put into this :th:`data_field` of the table.
  * - isSessionVariable
    - | Whether or not this field is a session variable
      | (not persisted -- defaults to false).

Many more columns can be specified, including a :th:`default` column or, as shown in the exampleForm, a :th:`default[0]` column to initialize the first element (index zero) of a select multiple field. Default values cannot be calculates and must be simple literal values (integers, numbers and strings).

.. _xlsx-ref-queries:

Queries
~~~~~~~~~~~~~~~~~~~~~~~~~

The **queries** worksheet is an optional sheet that allows you to request data from external sources for use in :tc:`select` prompts. These are some of the things you can do with queries:

  - Connect to website APIs.
  - Get data from external Android Applications via file content providers.
  - Get data from a linked table
  - Open CSV files included in the survey's directory.
  - Pass key-value maps to :th:`linked_table` forms when creating or opening that form.

.. list-table:: Queries Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - query_name
    - | The name used to reference the information returned by
      | the query.
  * - query_type
    - | Legal value are :tc:`ajax`, :tc:`csv`, and :tc:`linked_table`.
      | Used to specify the provenance of the query data.
  * - uri
    - | Used by :tc:`ajax` and :tc:`csv` queries. The uri to use
      | for an :tc:`ajax` query or the name of the CSV file to
      | use relative to the location of the :file:`formDef.json`
      | file.
  * - callback
    - | Used by :tc:`ajax` and :tc:`csv` queries. The function
      | that will be used to map the query results to the set of
      | choices for a multiple choice prompt.
  * - linked_table_id
    - | Used by :tc:`linked_table` queries. The :th:`table_id`
      | used to identify the table that the data will come
      | from. This should match the :th:`table_id` provided
      | in the **settings** worksheet.
  * - linked_form_id
    - | Used by :tc:`linked_table` queries. The id of the form
      | that will be used to get the results for the
      | :tc:`linked_table`. This value should match the
      | :th:`form_id` value in the **settings** worksheet.
  * - selection
    - | Used by :tc:`linked_table` queries to filter results
      | when used with :tc:`selectionArgs`. Specifies the
      | conditions that must be true for the results to be
      | selected but must have :tc:`selectionArgs` to work.
  * - selectionArgs
    - | Used by :tc:`linked_table` queries to filter results
      | when used with :th:`selection`. The arguments to be
      | used in the :th:`selection` described above.
  * - orderBy
    - | Used by :tc:`linked_table` queries to specify the
      | order in which results should be returned.
  * - newRowInitialElementKeyToValueMap
    - | Used by :tc:`linked_table` queries. A Javascript
      | object containing key value pairs used to assign
      | initial values when creating a new row in the
      | linked table. The key is the element name in the
      | linked form. The value is the initial value to
      | assign to the element.
  * - openRowInitialElementKeyToValueMap
    - | Used by :tc:`linked_table` queries. A JavaScript
      | object containing key value pairs used to assign
      | initial values when opening an existing row in the
      | linked table. The key is the element name in the
      | linked form. The value is the initial value to
      | assign to the element.

The two columns :th:`newRowInitialElementKeyToValueMap` and :th:`openRowInitialElementKeyToValueMap` allow you to pass information from your originating form into the linked form. The element keys in these maps correspond to the element keys in the linked form (not the current form). These can refer to any of the form's fields; commonly, the values you would pass into the :th:`openRowInitialElementKeyToValueMap` would refer to session variables. You would typically pass the :th:`instanceID` of the originating form (that is: :code:`opendatakit.getInstanceID()` ) into the linked form when creating it so that you can store that id in a field in that linked table, thereby tying the newly-created row in that table back to the originating form's row.

.. _xlsx-ref-user-defined:

User Defined Section
~~~~~~~~~~~~~~~~~~~~~~~~~

A custom named section is essentially a subset of the **survey** worksheet. Thus, all of the columns that were described in the :ref:`survey <xlsx-ref-survey>` section are applicable in a custom section worksheet. However, the following worksheet names are reserved and cannot be used to name a custom section worksheet:

  - settings
  - properties
  - choices
  - queries
  - calculates
  - column_types
  - prompt_types
  - model
  - framework_translations
  - common_translations
  - table_specific_translations

.. _xlsx-ref-custom-prompt-types:

Custom prompt_types
~~~~~~~~~~~~~~~~~~~~~~~~~

Custom prompts can be created within the survey. The **prompt_types** worksheet can be used to specify the custom prompts so that they will be recognized by Survey.

.. list-table:: prompt_types Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - prompt_type_name
    - | The name that will be used to reference the prompt_type
  * - type
    - | The type of object that will be used to store the data received by the user
      | for this prompt type.

.. _xlsx-ref-column-types:

column_types
~~~~~~~~~~~~~~~~~~~~~~~~~

Custom columns can be used within a workbook that are used to store functions, formulas, and path names. The **column_types** worksheet can be used to specify these custom columns.

.. list-table:: prompt_types Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - column_type_name
    - | The name that will be used to reference the column.
  * - type
    - | The type of information that will be stored in the column (i.e. function,
      | formula, app_path_localized).

.. _xlsx-ref-framework-translations:

framework_translations
~~~~~~~~~~~~~~~~~~~~~~~~~

The **framework_translations** sheet is only present in the :file:`framework.xlsx file`. It defines the translations for all of the standard prompts provided by the ODK 2 framework.

.. list-table:: framework_translations Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - string_token
    - | The name that will be used string to be translated.
  * - text.<locale>
    - | The value of the translated text string.  There can be as many of these
      | columns as you want translated languages (such as :th:`text.default`, :th:`text.gr`,
      | :th:`text.es`).
  * - image.<locale>
    - | The value of the image url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`image.default`, :th:`image.gr`, :th:`image.es`).
  * - audio.<locale>
    - | The value of the audio url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`audio.default`, :th:`audio.gr`, :th:`audio.es`).
  * - video.<locale>
    - | The value of the videourl fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`video.default`, :th:`video.gr`, :th:`video.es`).

The locale code should generally be the 2-letter language code, or, if necessary, the *language_COUNTRY* naming used by Android can be used to identify a specific language variant. For example: *en_US*, *en_UK* for US English and UK English, respectively.

.. _xlsx-ref-common-translations:

common_translations
~~~~~~~~~~~~~~~~~~~~~~~~~

The **common_translations** sheet is optional. It should only be present in the :file:`framework.xlsx` file. It can be used by application designers to define translations used across multiple forms and web pages in an application.

The format for this sheet is the same as that for the **framework_translations** sheet.

.. list-table:: framework_translations Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - string_token
    - | The name that will be used string to be translated.
  * - text.<locale>
    - | The value of the translated text string.  There can be as many of these
      | columns as you want translated languages (such as :th:`text.default`, :th:`text.gr`,
      | :th:`text.es`).
  * - image.<locale>
    - | The value of the image url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`image.default`, :th:`image.gr`, :th:`image.es`).
  * - audio.<locale>
    - | The value of the audio url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`audio.default`, :th:`audio.gr`, :th:`audio.es`).
  * - video.<locale>
    - | The value of the videourl fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`video.default`, :th:`video.gr`, :th:`video.es`).

The locale code should generally be the 2-letter language code, or, if necessary, the *language_COUNTRY* naming used by Android can be used to identify a specific language variant. For example: *en_US*, *en_UK* for US English and UK English, respectively.

.. _xlsx-ref-table-translations:

table_specific_translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **table_specific_translations** sheet is optional. It should only be present in the XLSX file whose :th:`form_id` matches the :th:`table_id`. It defines translations that are available to all forms and web pages specific to that table id.

.. list-table:: framework_translations Worksheet Columns
  :header-rows: 1

  * - Column
    - | Description
  * - string_token
    - | The name that will be used string to be translated.
  * - text.<locale>
    - | The value of the translated text string.  There can be as many of these
      | columns as you want translated languages (such as :th:`text.default`, :th:`text.gr`,
      | :th:`text.es`).
  * - image.<locale>
    - | The value of the image url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`image.default`, :th:`image.gr`, :th:`image.es`).
  * - audio.<locale>
    - | The value of the audio url fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`audio.default`, :th:`audio.gr`, :th:`audio.es`).
  * - video.<locale>
    - | The value of the videourl fragment relative to the appName directory
      | for this locale.  There can be as many of these columns as you want
      | translated languages (i.e. :th:`video.default`, :th:`video.gr`, :th:`video.es`).

The locale code should generally be the 2-letter language code, or, if necessary, the *language_COUNTRY* naming used by Android can be used to identify a specific language variant. For example: *en_US*, *en_UK* for US English and UK English, respectively.

.. _xlsx-ref-built-in:

Built-in Functionality
--------------------------

The :program:`jquery` and :program:`underscore` libraries are available when defining calculates expressions.

ODK Survey exposes built-in functionality through formula functions to decrease form development time.

.. _xlsx-ref-formula:

Formula Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

The following formula functions can be used to simplify calculations or expressions.

.. list-table:: Built in formula functions
  :header-rows: 1

  * - Name
    - | Description
    - Example
  * - :code:`assign`
    - | Assignment operator that will assign the value
      | to the field and return the value
    - :code:`assign('fieldname',value)`
  * - :code:`countSelected`
    - | Returns the number of items selected from a
      | :tc:`select_multiple` prompt
    - :code:`countSelected(data(‘options’))`
  * - :code:`data`
    - | Returns the value of a field or session variable.
    - :code:`data(‘options’)`
  * - :code:`equivalent`
    - | Check to see if two values are equivalent
    - :code:`equivalent(data(‘option1’), data(‘option2’))`
  * - :code:`isFinalized`
    - | Returns true if this submission is finalized
    - :code:`isFinalized()`
  * - :code:`localize`
    - | Localizes the text passed in.
    - :code:`localize(data('options'))`
  * - :code:`metadata`
    - | Returns a metadata field of this row
    - :code:`metadata(‘_group_read_only’)`
  * - :code:`not`
    - | Negates the argument passed in.
    - :code:`not(selected(data('examples'), 'label_features'))`
  * - :code:`now`
    - | Returns the current date
    - :code:`now().getDay()`
  * - :code:`selected`
    - | Returns true if the value selected from a :tc:`select`
      | prompt is equal to the second argument passed
      | into the function.
    - :code:`selected(data('visited_continents'), 'NorthAmerica')`

And, additionally, the *opendatakit* object is also available for use in calculates expressions.

.. warning::

  The *opendatakit* object contains many useful functions but these should be considered internal methods subject to change. When upgrading, be sure to confirm that the methods you use have not disappeared!
