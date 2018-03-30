.. spelling::

  tableId

Survey formDef.json Structure
=================================

.. _formdef-spec:

.. contents:: :local:

The XSLSXConverter in the AppDesigner reads the XLSX form definition file and produces a set of output files, including :file:`formDef.json`, as described earlier in this document.

In general, users of Survey will not directly interact with this file. Instead, they would write their forms in the XLSX file. Several features of Survey support that simplified usage:

  1. custom screens and prompts can be defined in separate JavaScript files (see the earlier discussion of the Builder processing sequence). These custom prompts and screens can then be referenced by name in your XLSX form definition. This allows new widgets to be defined without extending the XLSX syntax or the XLSXConverter.
  2. if additional member variables or functions are needed in your prompt logic, you can define these simply by adding a column with that member variable name to the survey sheet. If there is a value in that field, the member variable will be created and present in the prompt instance when the form is being rendered. Use the `column_types` sheet to define the interpretation of these members (e.g., to interpret them as functions or formulas). Member variables that are objects can be created by using '.' to separate the member variable name from the field name, as is done with the `display.*` columns, which define a member variable that is an object with various fields (e.g., `display.prompt`, `display.text`, etc.). Array-valued member variables can be created using `[0]`, `[1]`, etc. to specify the values in the array.
  3. custom CSS styles and themes can be defined. Additionally, the full power of JavaScript is available when needed.

A primary goal of the :file:`formDef.json` format was to preserve enough of the original source document (XLSX) to enable that document to be roughly reconstructed. The cell locations and values of all the cells in the XLSX file are retained, but formatting and coloring of the cells is not preserved. One can theoretically write an inversion program that would take this information and reconstruct an XLSX file without formatting or cell coloring that would be functionally equivalent to the original source XLSX file. This solves a common issue in the JavaScript-based tools where the conversion process fails to preserve enough information about the source document to enable it to be recreated.

Additionally, while the XLSXConverter performs numerous cross-checks, some errors cannot be reported until the form is executed. When these occur, error messages must identify the sheet, row and column in which the error occurred so that it is easy for form designers to correct the issues.

With this understanding, the structure of the :file:`formDef.json` file consists, at the top level, of an object with 2 fields:

.. code-block:: javascript

    {
        xlsx: {...},
        specification: {...}
    }

.. _formDef-structure-xlsx:

`xlsx` Component
--------------------

Note that alternative form description environments, such as drag-and-drop form builders, are expected to produce content that might be stored under a different field name. As those other tools develop, it is expected that some error message handling will need to be revised to properly report errors against those other source descriptions.

The purpose of this component is to enable an inversion tool to generate an XLSX file that is functionally equivalent to the source XLSX that generated this :file:`formDef.json`.

.. note::

  Writing custom prompts that directly reference the content of the `xlsx` component is fragile and should be discouraged. Future versions of the Survey JavaScript framework may delete this component from the :file:`formDef.json` structure that is retained during form execution. Remember that prompts will automatically possess member values and functions that you have defined on the survey sheets, so there is little need to retrieve information by directly access the :file:`formDef.json` structure.

The `xlsx` object has field names that correspond to the names of the sheets in the originating XLSX file. Each sheet in the XLSX file is assumed to have a header row followed by data rows beneath it. The values for these sheet-name fields are arrays of objects, one or each data-row on that sheet. i.e., the header row is omitted. Each of these row objects will contain a `_row_num` field with the corresponding row number in the original XLSX file.

If a cell in the originating XLSX file's data-row was not empty, the corresponding data-row object will have a field with the column name from the header-row and this value as the field-value. For complex header-row column names, like `display.prompt.text`, the resulting data-row object will have a `display` field with an object value with a `prompt` field with an object value with a `text` field with the cell content. In cases where a value for the root cell: `display.prompt.text` and a cell field: `display.prompt.text.en` are both specified, the value in the root cell (`display.prompt.text`) will be pushed down into a `default` field.

Here is a portion of the `xlsx` structure showing the content of the first data row of the survey sheet from the example form:

.. code-block:: javascript

    "xlsx": {
        "survey": [
          {
            "type": "integer",
            "name": "default_rating",
            "display": {
              "prompt": "first_prompt",
              "hint": {
                "text": "If the form does not yet have a rating, this will be proposed for the rating value. This value is not retained in the survey result set and exists only for the duration of this survey session."
              }
            },
            "model": {
              "isSessionVariable": true
            },
            "_row_num": 2
          },
      ...

.. note::

  Recreating the XLSX file from this structure is mechanical but the reconstruction cannot preserve the order of the header columns, since that information has already been discarded.

.. _formDef-structure-specification:

`specification` Component
-----------------------------

The `specification` component of the :file:`formDef.json` object is the only part of that is active used by the Survey JavaScript framework. This component contains the following fields:

  * **column_types** -- used by builder. Can be extended by adding a `column_types` sheet in the XLSX file.
  * **settings** -- content from the settings sheet in the XLSX file. This is an object with field names corresponding to the `setting_name` on that sheet with values corresponding to the data-row matching that setting name. Retrieve a given `setting_name` via a call to :code:`opendatakit.getSettingObject(opendatakit.getCurrentFormDef(), setting_name)` There are accessor methods defined in the *opendatakit.js* JavaScript file for retrieving common settings values.
  * **choices** -- content from the choices sheet in the XLSX file. This is an object with field names corresponding to the `choice_list_name` on that sheet. The values for these fields are arrays of objects, one object per row matching that `choice_list_name` in the order in which they appear in the choices sheet. This information is returned as part of all data row fetches and queries and is accessible on the *odkData* result object via calls to :code:`resultObj.getColumnChoicesList(elementPath)` and, for individual data values, you can access the object corresponding to that data value most efficiently via :code:`resultObj.getColumnChoiceDataValueObject(elementPath, choiceDataValue)`. Within Survey, the prompts use a wrapper function: :code:`opendatakit.getChoicesDefinition(choice_list_name)` to access the choices list.  The choices field should eventually be removed as the above calls on the result object are definitive and those choice lists come from the choices sheet of the form whose formId matches the tableId. The choices sheet within each form XLSX file will be retained until the AppDesigner and XLSXConverter can become smarter.
  * **queries** -- content from the queries sheet in the XLSX file. This is an object with field names corresponding to each `query_name` on that sheet. The values for these fields are objects corresponding to the data-row matching that setting name. Retrieve a given `query_name` via a call to :code:`opendatakit.getQueriesDefinition(query_name)`
  * **calculates** -- content from the calculates sheet in the XLSX file. This is an object with field names corresponding to each `calculation_name` on that sheet. The values for these fields are objects corresponding to the data-row matching that setting name.
  * **section_names** -- an array of the survey sections from the XLSX file. This includes the synthesized *initial* sheet if one is not explicitly specified.
  * **sections** -- an object with field names corresponding to each of the `section_names`. Each such field defines the form content for that section (that sheet in the XLSX file).

After the `builder` has processed the form definition, the following fields are added:

  * **currentPromptTypes** -- a list of all standard and custom Backbone prompt classes.
  * **currenScreenTypes** -- a list of all standard and custom Backbone screen classes.

Additionally, the `builder` also scans and alters all of these fields from their original :file:`formDef.json` content by applying the `column_types` field mappings to their content.  See the *Builder* section, earlier, for how it replaces or modifies some string value content.

The following fields are present, but _are not the authoritative source for this information and **may be removed in future releases**._ They are present only to support the emulation of the Java environment when running in App Designer and are candidates for removal as that environment evolves:

  * **dataTableModel** -- the authoritative version of this content is returned in response to a database query on a table. This is used within the App Designer to emulate the Java environment.
  * **model** -- this content is an intermediate synthesis of the model sheet and all datatype attributions in the survey and survey sections. It is used to generate the :file:`definition.csv` file. And, on the Java side, that file is used to create the database table and construct the *dataTableModel* returned by the `odkData` object.
  * **properties** -- this content is used to generate the :file:`properties.csv` file and is returned through a database query as metadata by the `odkData` object. It is only used directly when rendering the *framework* form, which is only done within the App Designer.  The App Designer also uses it during database initialization.
  * **table_specific_definitions** -- this content is written to :file:`tableSpecificDefinitions.js`
  * **framework_definitions** -- this content is written to :file:`/config/assets/framework/frameworkDefinitions.js`
  * **common_definitions** -- this content is written to :file:`/config/assets/commonDefinitions.js`
  * **choices** -- as noted above, this should eventually disappear and the choices sheet should eventually only be present in the form whose formId matches the tableId. That can't happen until XLSXConverter and the AppDesigner get smarter (i.e., this will likely persist in the :file:`formDef.json` for longer than any of the above fields).

.. _formDef-structure-subcomponent:

`sections` Sub-Component
--------------------------

Each section object in the `sections` sub-component contains a heavily processed and cross-checked version of that section of the survey. These objects have the following fields:

  * **section_name** -- the section name -- i.e., the name of the sheet in the original XLSX file.
  * **nested_sections** -- a map of all the section names that are targets of `do_section` actions within this section.
  * **reachable_sections** -- a map that is the closure of all section names that can be recursively reached by all nested sections and by this section.  This is used to ensure there are no cycles among the sections.
  * **prompts** -- a list of all prompts within this section.
  * **validation_tag_map** -- a map of all validation tag names and the array of prompts that reference that tag name (and that have value constraints). Prompts can specify a list of validation tag names that will enforce the prompt's constraints by specifying a space-separated list of values for a `validation_tags` column in their XLSX sheet. Intermediate validation of some prompt values can be achieved via the `validate {tagName}` action at any point in a survey. If nothing is specified for the `validation_tags` column, the prompt is automatically added to the `finalize` validation tag, which is processed when the :guilabel:`Save as Complete` action is initiated within the form.
  * **operations** -- an array of operations that the `controller` iterates through to process this section of the form. Unless otherwise specified, processing starts at index zero in this array.
  * **branch_label_map** -- a map of all branch (go-to) label names and the index within the operation array to which they correspond.  Used to map the 'goto label' operation to a destination within the operations array.

After the `builder` has processed the form definition, the following fields are added:

  * **parsed_prompts** -- a list of Backbone instances corresponding to the extension of the referenced Backbone prompt type with the field values found in the **prompts** list.

And `builder` also scans the `operations` list applying the `column_types` rules.

During form navigation, the `parsed_prompts` list of Backbone instances will be used to render DOM content and handle events.  _The `prompts` array may be removed by the `builder` in some future release._  Each of these prompts has an XLSXConverter-generated field, `_branch_label_enclosing_screen` that identifies the branch label for the operation that will render the screen containing this prompt. This is used during validation to map back from the prompt whose constraints are violated to the `begin_screen` operation that will render the screen containing that prompt. Prompts also have `_row_num` and `__rowNum_` fields that reference the XLSX row in the section that defines the prompt and the line number within the section (one less than the XLSX row number due to the presence of the header row), respectively. These are used for reporting exceptions during form loading and processing (i.e., malformed formulas, etc.).

.. _formDef-structure-sub-sub-element:

`operations` Sub-Sub-Element
------------------------------

Each element in the `operations` array describes an action the `controller` should execute when processing the form. The 10 primitive operation types were described in an earlier section. Below are brief examples of these various primitive operations.

Within all operations objects:

  1. an `operationIdx` field contains the index into the `operations` array under which this operation object is stored.
  2. the `_token_type` field contains the operation type.
  3. the `_row_num` field contains the (first) row in the section that corresponds to this action. i.e., if a screen contained multiple prompts, this would be the row containing the *begin screen* action.

Here are specifics for each operation type:

.. _formDef-structure-sub-sub-element-assign:

assign
"""""""""""

*assign* actions can appear within *begin screen* ... *end screen* regions or outside of them. If they appear outside of them, they are interpreted as a separate operation by the `controller`. Here is an example of such an assign action:

.. code-block:: javascript

      {
        "type": "assign",
        "name": "default_rating",
        "calculation": 8,
        "_row_num": 2,
        "__rowNum__": 1,
        "_token_type": "assign",
        "operationIdx": 0
      },

The key fields in this are:

  1. `name` -- the field (session variable or a field in the data row) to assign.
  2. `calculation` -- the expression to evaluate and assign in the field. This is converted by `builder` into a JavaScript function (i.e., transforming it into: :code:`function() { return (8); }` which is then evaluated).

.. _formDef-structure-sub-sub-element-begin-screen:

begin_screen
""""""""""""""""""

This is an example of a `begin_screen` operation object:

.. code-block:: javascript

          {
            "clause": "begin screen",
            "_row_num": 20,
            "__rowNum__": 19,
            "_token_type": "begin_screen",
            "_end_screen_clause": {
              "clause": "end screen",
              "_row_num": 23,
              "__rowNum__": 22,
              "_token_type": "end_screen"
            },
            "_screen_block": "function() {var activePromptIndicies = [];\nassign('coffee_today', (( data('coffee_today') == null ) ? data('avg_coffee') : data('coffee_today')));\nactivePromptIndicies.push(11);\n\nreturn activePromptIndicies;\n}\n",
            "operationIdx": 22
          },

In addition to the standard fields, this contains:
  * `clause` -- the action clause that this corresponds to. If this were generated by a lone prompt, the `clause` field would be missing.
  * `_end_screen_clause` -- the clause that marks the *end screen* statement.
  * `_screen_block` -- this field will be processed by `builder` to generate a JavaScript function. It encapsulates any assign operations and any if-then-else logic within the *begin screen* ... *end screen* region that determined which prompts should be shown on that screen. The function returns an array of the prompt indices that should be rendered at this time.

Note that the above example shows how an if-then-else clause and assign action are transformed into a `_screen_block`

Here is another example, this one for a prompt that is not wrapped by a *begin screen* ... *end screen* action:

.. code-block:: javascript

          {
            "_row_num": 2,
            "_token_type": "begin_screen",
            "_screen_block": "function() {var activePromptIndicies = [];\nactivePromptIndicies.push(0);\n\nreturn activePromptIndicies;\n}\n",
            "operationIdx": 0
          },

.. _formDef-structure-sub-sub-element-goto-label:

goto_label
""""""""""""""""

If-then-else clauses outside of *begin screen* ... *end screen* regions are converted into branch labels and conditional and unconditional *goto_label* commands. Additionally, users may explicitly jump to a label using a *goto* clause in the XLSX file (and do that conditionally if they specify a *condition* predicate). Here is an example of a conditional `goto_label` operation object generated from an `if` clause.

.. code-block:: javascript

          {
            "clause": "if",
            "condition": "selected(data('examples'), 'intents')",
            "_row_num": 4,
            "__rowNum__": 3,
            "_token_type": "goto_label",
            "_branch_label": "_then4",
            "operationIdx": 2
          },

The key fields for this are:
  * `condition` -- present if the goto is conditional. If present, this is converted by `builder` into a JavaScript function.
  * `_branch_label` -- where the goto should jump to.

Here is another example of an unconditional goto generated as a result of an *end if* clause:

.. code-block:: javascript

          {
            "clause": "end if",
            "_token_type": "goto_label",
            "_branch_label": "_else9",
            "_row_num": 9,
            "operationIdx": 3
          },

.. _formDef-structure-sub-sub-element-do-section:

do_section
""""""""""""""""

Here is an example of a *do_section* operation:

.. code-block:: javascript

      {
        "clause": "do section household",
        "_row_num": 2,
        "__rowNum__": 1,
        "_token_type": "do_section",
        "_do_section_name": "household",
        "operationIdx": 0
      },

The key field here is:

  `_do_section_name` which identifies the section name that should be jumped into.

.. _formDef-structure-sub-sub-element-exit-section:

exit_section
""""""""""""""""""

Here is an example of an *exit_section* operation:

.. code-block:: javascript

      {
        "_token_type": "exit_section",
        "clause": "exit section",
        "_row_num": 7,
        "operationIdx": 3
      },

.. _formDef-structure-sub-sub-element-back-history:

back_in_history
""""""""""""""""""

This is primarily used as a pseudo-instruction (an instruction injected into the operation stream) when the user hits the *Back* button or swipes backward. This is also emitted as a real operation when a *back* clause is specified in the XLSX file. Used in that manner, it can create a "dead-end" screen that the user cannot swipe through (they can only go backward) and can be useful when presenting a user with a *user_branch* prompt (where the user must choose the next action and there is no default action).

.. code-block:: javascript

      {
        "clause": "back",
        "_row_num": 4,
        "__rowNum__": 3,
        "_token_type": "back_in_history",
        "operationIdx": 3
      },

.. _formDef-structure-sub-sub-element-advance:

advance
""""""""""""""""""

This is only used as a pseudo-instruction (an instruction injected into the operation stream) when the user hits the :guilabel:`Next` button or swipes forward.

.. _formDef-structure-sub-sub-element-validate:

validate
""""""""""""""

This is an example of a *validate* operation:

.. code-block:: javascript

      {
        "clause": "validate user_info",
        "_row_num": 12,
        "__rowNum__": 11,
        "_token_type": "validate",
        "_sweep_name": "user_info",
        "operationIdx": 7
      },

Partial validation of a form is one of the advanced features of Survey. In this instance, only the fields tagged with the *user_info* validation tag will be verified. The key field for this operation is:

  `_sweep_name` -- the name of a validation tag. Any fields that have this name in their space-separated list of validation tags under the *validation_tags* column in the XLSX file will have their constraints validated.

If a field has a constraint but no values under the *validation_tags* column, *finalize* will automatically be assumed to be in that list. 'validate finalize' is called when a form is saved-as-complete.

.. _formDef-structure-sub-sub-element-resume:

resume
""""""""""""""

None of our examples explicitly use this clause in the XLSX file. However, it is used in the construction of the default Contents screen handler for a section which is emitted if the form designer did not specify their own '_contents' branch label and define their own screen for this purpose. Choosing to view the contents screen causes a jump to the '_contents' branch. The default implementation of that branch is a *begin_screen* operation to display the Contents screen followed by a *resume*. The default Contents screen has its `hideInBackHistory` field set to true. This causes that screen to not be saved in the back history. When a user swipes forward, the *resume* operation will scan backward to the screen before the Contents screen (since it is skipped) and will render that screen (returning the user to the screen they were last at).

.. code-block:: javascript

      {
        "_token_type": "resume",
        "clause": "resume",
        "_row_num": 9,
        "operationIdx": 12
      }

.. _formDef-structure-sub-sub-element-save-and-terminate:

save_and_terminate
"""""""""""""""""""""

This is not explicitly used in our examples, but it is used within the automatically-generated 'initial' section if the user has not defined their own. This operation corresponds to a 'save and terminate' clause. That clause takes a 'condition' expression that indicates whether the content should be saved-as-complete or saved-as-incomplete (this clause does not itself determine the validation status and hence completeness of the data).  Because of this, any save-as-complete action should be preceded by a 'validate finalize' clause to ensure that the form is validated. After saving the form contents, the Survey window is then closed.

.. code-block:: javascript

     {
        "_token_type": "save_and_terminate",
        "clause": "save and terminate",
        "calculation": true,
        "_row_num": 9,
        "screen": {
          "hideInBackHistory": true
        },
        "operationIdx": 11
      },




