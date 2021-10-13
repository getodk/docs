.. spelling::
  getHashString
  getCurrentInstanceId
  tienes
  Cuántos
  años
  Cuál
  es
  su
  nombre
  newRowInitialElementKeyToValueMap
  happyBirthday
  isBirthdayToday
  getTime
  daysOld
  num
  async
  isSessionVariable
  fieldName
  openRowInitialElementKeyToValueMap
  promptTypes

Using ODK-X XLSX Converter
=============================

.. _xlsx-using:

ODK-X Survey offers a rich set of features that can be seamlessly integrated into a custom form. A lot of the functionality can be implemented solely within an Excel workbook. This guide is designed to help you take advantage of this via a guided tour of example tasks.

.. contents:: :local:

.. tip::

  For a full reference to all the functionality available, see the :doc:`xlsx-converter-reference`.

.. _xlsx-using-create-load-survey:

Creating and Loading a Form into ODK-X Survey
-------------------------------------------------

Below are the steps to create a new form from the *exampleForm*:

  1. Within the Application Designer's folder, create the following directory structure :file:`app/config/tables/your_table_id/forms/your_table_id/`
  2. Copy the :file:`exampleForm.xlsx` from :file:`app/config/tables/exampleForm/forms/exampleForm/` into this new directory.
  3. Rename the XLSX file to :file:`your_table_id.xlsx`
  4. Edit the XLSX file and on the **settings** worksheet, change the value for *table_id* to *your_table_id*. Then update the display title for the survey and the form version. Save the changes.
  5. If you have not already, run :program:`grunt` to launch the :program:`Chrome` browser and open the Application Designer home page.
  6. Navigate to the :guilabel:`XLSX Converter` tab, choose this file to convert it. Once converted, choose :guilabel:`Save to File System` and click :guilabel:`OK` on the 3 pop-ups that alert you to the saving of 3 files to the file system. The three files that are saved are:

    - :file:`app/config/tables/your_table_id/definition.csv` -- defines the user-defined columns in your table
    - :file:`app/config/tables/your_table_id/properties.csv` -- defines the appearance and available detail and list view HTML files for the table
    - :file:`app/config/tables/your_table_id/forms/your_table_id/formDef.json` -- defines the ODK-X Survey form defined by the XLSX file

  7. The first two files are written only if the form id matches the table id. That form and the XLSX file define the data table.
  8. Repeat the edit, conversion, and save steps to update the columns in your table and your survey form.
  9. Connect your device to your computer with a USB cable.
  10. In a separate :program:`command` window, navigate to the Application Designer directory and type:

  .. code-block:: console

    $ grunt adbpush

  to push the contents of the :file:`app/config` directory to your device.

  11. Start ODK-X Survey. The form should now be available in ODK-X Survey.

.. _xlsx-using-create-simple-survey:

Creating a Simple Survey Form
-----------------------------------

Typing the following in the **survey** worksheet of a workbook with an appropriate **settings** worksheet will result in a simple survey.

.. csv-table:: Creating a Simple Survey Example Form
  :header: "clause", "Condition", "type", "name", "display.prompt.text"
  :name: creating-a-simple-survey-example-form

  ,,"integer", "person_age", "How old are you?"
  "if ", "data('person_age') >= 18",
  "begin screen",
  ,,"text", "pizza_type", "What is your favorite kind of pizza?"
  ,,"integer", "num_slices", "How many slices would you like?"
  "end screen",
  "else",
  ,,"note",, "You are too young to be eating pizza"
  "end if",

The first row contains an empty clause and an empty condition column. Therefore, the :th:`display.prompt.text` will be shown on the screen, and the resulting :tc:`integer` answer will be stored in the variable :tc:`person_age`.

On the next line there is an :tc:`if` in the :th:`clause` column and :tc:`data('person_age') >= 18` in the condition column. If the answer stored in the variable :tc:`person_age` is greater than or equal to 18, the following commands should be done until either an :tc:`else` or an :tc:`end if` tag is reached. Notice the other three columns are left blank.

In the next row, there is a :tc:`begin screen` tag in the :th:`clause` column. The remaining four columns are left blank. Until an :tc:`end screen` tag is reached in the :th:`clause` column, all the following questions will be displayed on one screen. In this case, the user will be asked to input their favorite type of pizza and how many slices they would like on the same page, assuming they are 18 or older.

In the next row, there is an :tc:`else` tag. Until :tc:`end if` is reached, anyone who did not satisfy the requirement for the :tc:`if` tag will be asked the following questions. In this case, a :tc:`note` to the user that they are too young to be eating pizza will be displayed.

.. note::
  An important thing to remember when using the clause column is when to open and close new tags. The general rule is that the most recently opened grouping is the first to be closed.

.. _xlsx-using-multi-choice:

Adding Multiple Choice Questions
-------------------------------------

There are three types of multiple choice questions supported by ODK-X Survey:

  - :tc:`select_one`
  - :tc:`select_one_with_other`
  - :tc:`select_multiple`

Multiple choice questions use the :th:`values_list` column in the **survey** worksheet. The :th:`values_list` column is what links a multiple choice question to its answer set contained on the **choices** worksheet.

The pizza survey example used earlier can be improved upon with multiple choice options. The resulting **survey** worksheet would look like this:

.. csv-table:: Adding Multiple Choice Questions Example Survey Worksheet
  :header: "clause", "Condition ", "type", "values_list ", "name", "display.prompt.text"
  :name: adding-multiple-choice-questions-example-survey-worksheet

  ,,"select_one", "yes_no", "person_age", "Are you 18 or older?"
  "if", "selected(data('person_age'), 'yes')",
  "begin screen",
  ,,"select_multiple", "topping_list", "pizza_type", "What are your favorite kind of pizza toppings (select up to 3)?"
  ,,"integer",, "num_slice", "How many slices would you like?"
  "end screen",
  "else",
  ,,"note", "You are too young to be eating pizza"
  "end if",

and the corresponding **choices** worksheet would look like this:

.. csv-table:: Adding Multiple Choice Questions Example Choices Worksheet
  :header: "choice_list_name", "data_value", "display.title.text"
  :name: adding-multiple-choice-questions-example-choices-worksheet

  "yes_no", "yes", "Yes"
  "yes_no", "no", "No"
  "topping_list", "pepperoni", "Pepperoni"
  "topping_list", "olives", "Black Olives"
  "topping_list", "onions", "Onions"
  "topping_list", "mushroom", "Mushrooms"
  "topping_list", "pepper", "Green Peppers"
  "topping_list", "bacon", "Canadian Bacon"
  "topping_list", "pineapple", "Pineapple"

Now, instead of typing their age, the user simply selects whether they are older than 18 or not. Furthermore, instead of entering the type of pizza they like, they can select from a list of toppings.

.. tip::

  Because you determine whether a question is :tc:`select_one` or :tc:`select_multiple` from the **survey** worksheet, the same choice set on the **choices** worksheet can be used for both :tc:`select_one` and :tc:`select_multiple` questions.

.. _xlsx-using-skip-logic:

Using Skip Logic
-------------------------------------

Skip logic (*Conditional Branching*) is an amazing feature in :doc:`survey-using` that changes the next prompt or screen the user sees based on their current response. This enables the form creator to give users a unique and personalized experience depending on their answers throughout the entire survey.

Skip logic is implemented using if, else, else if and end if tags. It uses the **clause** and **condition** columns in the survey worksheet, the if, else and end if tags are placed in the clause column and the conditional expressions are housed in the condition column.

Below is the survey worksheet of an example survey that implements skip logic. ODK-X has built-in `JavaScipt Operators <https://docs.odk-x.org/xlsx-converter-reference/#javascript-operators>`_ which are useful for creating complex conditional expressions.

.. csv-table:: Using Skip logic Example Survey Worksheet
  :header: "clause", "condition", "type", "values_list ", "name", "display.prompt.text"
  :name: using-skip-logic-example-survey-worksheet

  ,,"select_one", "order_list", "menu", "What would you like to get?"
  "if", "selected(data('menu'), 'doughnut') || selected(data('menu'), 'bread roll') || selected(data('menu'), 'cinnamon roll')",
  "begin screen",
  ,,"select_one", "box_list", "box", "What would you like?"
  "end if",
  "if", "selected(data('menu'), 'cake')",
  "begin screen",
  ,,"select_one", "size_list", "size", "What size of cake would you like?"
  ,,"select_one", "flavor_list", "flavor", "What cake flavor would you like?"
   "end screen",
  "end if",
  "if", "selected(data('menu'), 'cupcake')",
  "begin screen",
  ,,"select_one", "box_list", "box", "What would you like?"
  ,,"select_one", "flavor_list", "flavor", "What cake flavor would you like?"
  "end screen",
  "end if",
  ,,"note", "<h3>Order Summary for <u>{{data.name}}</u></h3>"

In the example worksheet above, the respondent can pick through a number of pastries available and select one option. The next set of questions that follow are fully dependent on the choice the user makes. For example, if the user picked Cakes; they are asked for a flavor and size they would like whereas if the user picked Doughnuts; they are asked what size of box they would like.

.. note::
  An important thing to remember when using the clause column is the opening **if** tag and the closing **end if** tags. The general rule is that all **if** tags must have a corresponding closing **end if** tag.

.. note::
  Do know that if you are using required along with skip logic, it is important that both the required and if conditionals align.

  The **required** column takes a conditional expression. If the condition resolves to true, the user will not be able to navigate to the next survey screen until the prompt is answered. If the prompt is left blank, its default value is false.

.. _xlsx-using-custom-section:

Using Custom Section Worksheets
---------------------------------------

Custom section worksheets can be added to a workbook to make the control flow of a survey more readable. We could move all the previous questions about pizza to a new worksheet and name it **Pizza**. Our **survey** worksheet would then look like this:

.. csv-table:: Custom Section Worksheets Example
  :header: "clause", "condition ", "type", "values_list ", "name", "display.prompt.text"
  :name: custom-section-worksheets-example

  "do", "section Pizza",

.. tip::
  When splitting a survey into different sections, it is wise to put a :tc:`note` before each section call with :th:`display.prompt.text` set to read *Section <name_of_section>*. This is because a :tc:`do` :tc:`section <name_of_section>` call is transparent to the user. Unless the form designer explicitly adds a :tc:`note`, the user will not realize that they entered a section.

  Also, after leaving a section, if the user swipes back, the survey will go to the row before the :tc:`do` :tc:`section` call. If the user then swipes forward at this point, the survey will go to the beginning of the section they just completed. It is often beneficial to the user to put a :tc:`note` before entering a section and before leaving a section.

.. _xlsx-using-calculations:

Using Calculations
---------------------

The **calculates** worksheet is an optional worksheet. It consists of two columns:

  - :th:`calculation_name`: Each row of the **calculates** page represents a function that can be used elsewhere in the workbook by referencing the individual :th:`calculation_name`.
  - :th:`calculation`: The calculation to be performed.

.. note::

  The :th:`calculation` column can store any valid JavaScript expression.

.. tip::

  There are also some built in functions for ODK-X Survey that can be used anywhere in the workbook. See the :ref:`Forumla Functions <xlsx-ref-formula>` for more details.

In general, calculations are referenced in the :th:`condition` column of **survey** worksheets. For example, suppose that on the **survey** page under the variable name *birthday* the user entered their birthday for a question of type :tc:`date`. The **calculates** worksheet might look like this:

.. csv-table:: Calculates Worksheet Example
  :header: "calculation_name", "calculation"
  :name: calculates-worksheet-example

  "daysOld", "(now().getTime()-new Date(data('birthday')).getTime())/1000/60/60/24"
  "isBirthdayToday", "calculates.daysOld()%365 == (now().getTime()/1000/60/60/24)%365"

and one of the **survey** worksheets may look like this:

.. csv-table:: Calculation Survey Worksheet Example
  :header: "clause", "condition", "type", "name", "display.prompt.text"
  :name: calculations-survey-worksheet-example

  "if", "calculates.isBirthdayToday()",
  ,,"note", "happyBirthday", "Happy Birthday!"
  "end if",

Notice that the <:th:`calculation_name`>s do not contain parentheses () at the end of them. However, when referencing them it is always in the format of :command:`calculates.<calculation_name>()`.

.. tip::

  Variable names have scope for the entire workbook.


The **calculates** worksheet is handy because it adds readability to a workbook. Instead of having long, complicated JavaScript calculations in the **survey** worksheets, they can be consolidated in one, easy to reference location that allows for reusability. Also notice the consistent use of camelCase for variable naming across the different worksheets.

.. _xlsx-using-queries:

Using Queries
---------------------------------

The **queries** worksheet is an optional worksheet.

For queries that get their data from external sources, the following columns should be used:

  - :th:`query_name`
  - :th:`query_type`
  - :th:`uri`
  - :th:`callback`

For :tc:`linked_table` queries, these columns should be used:

  - :th:`query_name`
  - :th:`query_type`
  - :th:`linked_table_id`
  - :th:`linked_form_id`
  - :th:`selection`
  - :th:`selectionArgs`
  - :th:`orderBy`
  - :th:`auxillaryHash`

Each row of the queries page represents a choice set that can be used by :tc:`select` prompt types in the workbook. In general, :th:`query_name` is referenced in the :th:`values_list` column of **survey** worksheets. For example, suppose that on the **survey** page under the variable name :tc:`region` the user is asked to select the region they are from. Then the user is asked to select which country they are from. The choices for the list of countries can be filtered based on the region the user selected. The **queries** worksheet might look like this:

.. list-table:: Queries Worksheet Example
  :header-rows: 1
  :name: queries-worksheet-example

  * - query_name
    - query_type
    - uri
    - callback
  * - regions_csv
    - csv
    - "regions.csv"
    - | _.chain(context).pluck('region').uniq().map(function(region){
      |   return {data_value:region, display:{title: {text: region} } };
      | }).value()
  * - countries.csv
    - csv
    - "regions.csv"
    - | _.map(context, function(place){place.data_value = place.country;
      |   place.display = {title: {text:place.country} };
      |   return place;
      | })

The data for the queries is coming from the :file:`regions.csv` file that is located in the same directory as the :file:`formDef.json` and specified in the :th:`uri` column. Thus, the :th:`query_type` for both queries is :tc:`csv`. A snippet of the :file:`regions.csv` file looks like the following:

.. csv-table:: regions.csv
  :header: "region", "country"
  :name: regions-csv

  "Africa", "Algeria"
  "Africa", "Angola"
  "Africa", "Benin"

Knowing the structure of the :file:`regions.csv` helps in understanding the callback function provided in the :th:`callback` column. The callback function maps the results from the :file:`regions.csv` file to the :th:`data_value` and the :th:`display.prompt.text` fields using JavaScript. The **survey** worksheets may look like this:

.. csv-table:: Queries Survey Worksheet Example
  :header: "clause", "condition ", "type", "values_list ", "name", "display.prompt.text ", "choice_filter"
  :name: queries-survey-worksheet-example

  "begin screen",
  ,,"select_one_dropdown", "regions_csv", "region", "Please select your region:",
  ,,"select_one_dropdown", "countries_csv", "country", "Please select your country:", "choice_item.region === data('region')"
  "end screen",

The :th:`choice_filter` in this example ensures that the options for the :tc:`country` question will only be the countries from the previously selected region. Notice that :tc:`choice_item.region` specifies that any country with a corresponding region equal to the answer stored by the region question will be displayed.

The **queries** worksheet is powerful because it allows more flexibility in terms of where data for the survey can reside.

.. _xlsx-using-queries-linked-tables:

Linked Tables
~~~~~~~~~~~~~~~~

:th:`linked_table` is the other use for the **queries** worksheet. :th:`linked_table` allows you to launch a subform that can edit a different data table. For example, if a survey is dealing with information about households, the user may want to ask questions about the general household but also questions about specific users. :th:`linked_table` can be used to launch subforms that ask questions about the specific household members. The **survey** worksheet may look like this:

.. csv-table:: Linked Table Survey Worksheet Example
  :header: "clause", "condition", "type", "values_list", "name", "display.prompt.text ", "choice_filter"
  :name: linked-table-survey-worksheet-example

  ,,"text",, "house_id", "Input the unique household id:",
  ,,"integer",, "num_members", "How many people live in this house?",
  ,,"linked_table", "members",, "Add and enter information for the different household members",
  ,,"select_one", "members", "household_head", "Who is the household head?",

The **queries** worksheet would look like this:

.. list-table:: Linked Table Query Worksheet Example
  :header-rows: 1
  :name: linked-table-query-worksheet-example

  * - query_name
    - query_type
    - linked_form_id
    - linked_table_id
    - selection
    - selectionArgs
    - newRowInitialElementKeyToValueMap
  * - members
    - linked_table
    - members_info
    - house_members
    - house_id = ?
    - [ opendatakit.getCurrentInstanceId() ]
    - { house_id: opendatakit.getCurrentInstanceId() }

First the user enters a :tc:`house id` for the house and answers an arbitrary question about its residents. This information is stored in the data table for general household information (specified on the **settings** worksheet under :th:`table_id`). Then the user reaches a :tc:`linked_table` prompt that uses the :th:`values_list` members. This is connected to the members query on the **queries** worksheet. It links to a different survey called :tc:`members_info` that edits a different data table. The selection criteria is that the :tc:`house_id` in the :tc:`house_members` data table matches the :tc:`instanceID` of this current household.

Initially this list will be empty since no members have been added. The user can click on the :guilabel:`Create Instance` button to add new people for this household. The :tc:`house_id` will be set automatically for this new member via the :th:`newRowInitialElementKeyToValueMap` content, which specifies that the :tc:`house_id` field in the linked table should be initialized with the :tc:`instanceID` of the current household.

.. note::

  The selection criteria and its type (in this case, :tc:`house_id` and :tc:`text`) must be added to the model subset of the subform (members_info) in order for selection criteria to be persisted to the database and for the subform to be found by its parent form; the selection criteria cannot filter on session variables since those values are never persisted.

When the user finishes the subform, the screen will return to the same linked_table prompt. At this point, the user can continue adding more users, edit an existing member's info, or go to a different screen.

The :th:`values_list` for the :tc:`select_one` question prompt in the example above also uses the :tc:`members` query. Instead of being able to launch subforms to edit information about different members, the selection criteria is used to populate a multiple choice question. The answer to the multiple choice question is saved to the general :tc:`household` data table, not the :tc:`members` data table.

.. _xlsx-using-internationalization:

Internationalization
--------------------------

Survey offers the ability to display text in different languages. This requires usage of the **settings** worksheet to determine which language to use. However, for any language other than the default language, extra display columns need to be added. For example, if one of the non-default language options was Spanish (2-letter language code "es"), every worksheet with a :th:`display.prompt.text` column would also need a :th:`display.prompt.text.es` column. This is true for all columns that need an alternate language option.

.. csv-table:: Internationalization framework_translations Worksheet Example
  :header: "type", "name", "display.prompt.text", "display.prompt.text.es"
  :name: internationalization-framework-translations-worksheet-example

  "text", "user_name", "What is your name?", "¿Cuál es su nombre?"
  "integer", "user_age", "How old are you?", "¿Cuántos años tienes?"

The labels used in the buttons and prompts supplied by ODK-X Survey are defined in the **framework_translations** sheet of the :file:`framework.xlsx` file under :file:`config/assets/framework/forms/framework.xlsx` Simply add your language code and translations to this sheet of this XLSX file and run :guilabel:`XLSXConverter` on it to enable support of your language across all of the built-in buttons and prompts within ODK-X Survey.

.. _xlsx-using-advanced-branching:

More Advanced Branching
----------------------------

ODK-X Survey supports situations where the user needs to be in control of which survey or section of a survey they are working on. To do this, the :th:`branch_label` column is used, as well as the **choices** worksheet. It also utilizes a new question type: :tc:`user_branch`. The following example combines aforementioned surveys and allows the user to decide whether they want to fill out the survey about pizza, or the survey about birthdays.

A choice set needs to be added to the **choices** worksheet with the applicable branching options. The resulting **choices** worksheet would look like this:

.. csv-table:: Branching Choices Worksheet Example
  :header: "choice_list_name", "data_value", "display.title.text"
  :name: branching-choices-worksheet-example

  "which_form", "pizza_form", "Order pizza?"
  "which_form", "birthday_form", "Is it your birthday?"

And the **survey**  page would look like this:

.. csv-table:: Branching Survey Worksheet Example
  :header: "branch_label", "clause", "condition ", "type", "values_list ", "display.prompt.text"
  :name: branching-survey-worksheet-example

  ,,,"user_branch", "which_form", "Choose a survey to fill out"
  "pizza_form",
  ,"do section pizza",
  "birthday_form",
  ,"do section birthday",

The XLSX file would then have corresponding **section** worksheets called *pizza* and *birthday* that contain the survey examples documented earlier.

.. _xlsx-using-custom-initial:

Creating a Custom Initial Worksheet
--------------------------------------

When ODK-X Survey opens, it displays a list of the different forms available on the device. After the user has selected which type of form to work on, Survey launches the initial worksheet for that particular survey. So far the initial worksheet has not been discussed and if one is not explicitly included in the XLSX file, survey uses this default initial worksheet:

.. list-table:: Custom Initial Worksheet Example
  :header-rows: 1
  :name: custom-initial-worksheet-example

  * - clause
    - Condition
    - type
    - display.prompt.text
  * - if // start
    - (opendatakit.getCurrentInstanceId() != null)
    -
    -
  * -
    -
    - opening
    - Edit form
  * - do section survey
    -
    -
    -
  * -
    -
    - finalize
    - Save form
  * - else // start
    -
    -
    -
  * -
    -
    - instances
    - Saved instances
  * - end if // start
    -
    -
    -

This checks to see if an instance of the current form has been selected :command:`(opendatakit.getCurrentInstanceId() != null)`. If it has, it opens that form. If not, it displays the instances that the user can edit. This utilizes three new types:

  - :tc:`opening`
  - :tc:`finalize`
  - :tc:`instances`

.. warning::

  When creating a custom initial worksheet, it is very important to include a finalize type. After completing a survey, it is the finalize prompt that lets the user formally finish the survey so that the results can be used.

.. _xlsx-using-validate:

Using Validate
------------------------

When users start having more control over which questions they are asked, it can lead to problems if they bypass required prompts. The validate feature allows for the form creator to require form validation in custom places. By default, the form performs a validation during the :tc:`finalize` section of the survey. However, this type of operation can be performed at multiple points throughout the survey on specific questions using the prompt type :tc:`validate` and the column :th:`validation_tags`.

The following example will collect information from a user in *section1* and *section2* and will prevent completion of *section3* if certain questions have invalid answers.

The **survey** page would look like this:

.. csv-table:: Validate Survey Worksheet Example
  :header: "branch_label", "Clause", "type", "values_list ", "display.prompt.text"
  :name: validate-survey-worksheet-example

  "welcome_screen",
  ,,"user_branch", "which_branch", "Choose the section to enter"
  ,"goto welcome_screen",
  "branch1",
  ,,"note",, "Selected Section 1"
  ,"do section section1",
  ,,"note",, "Returning from Section 1"
  ,"goto welcome_screen",
  "branch2",
  ,,"note",, "Selected Section 2"
  ,"do section section2",
  ,,"note",, "Returning from Section 2"
  ,"goto welcome_screen",
  "branch3",
  ,,"note",, "Selected Section 3"
  ,"validate user_info",
  ,"do section section3",
  ,,"note",, "Returning from Section 3"
  ,"goto welcome_screen",

The **choices** worksheet would look like this:

.. csv-table:: Validate Choices Worksheet Example
  :header: "choice_list_name", "data_value", "display.title.text"
  :name: validate-choices-worksheet-example

  "which_branch", "branch1", "Do Section 1"
  "which_branch", "branch2", "Do Section 2"
  "which_branch", "branch3", "Do Section 3"

The **section1** worksheet would look like this:

.. csv-table:: Validate Section1 Worksheet Example
  :header: "type", "name", "display.prompt.text", "required", "validation_tags"
  :name: validate-section1-worksheet-example

  "text", "user_name", "What is your name?", "TRUE", "user_info finalize"
  "integer", "user_age", "What is your age?", "TRUE", "user_info finalize"
  "note",, "Thank you for answering",

The **section2** worksheet would look like this:

.. csv-table:: Validate Section2 Worksheet Example
  :header: "type", "name", "display.prompt.text", "required", "validation_tags"
  :name: validate-section2-worksheet-example

  "text", "occupation", "What is your current occupation?", "TRUE", "user_info finalize"
  "integer", "user_age", "How long have you worked at your current job (in years)?", "TRUE", "finalize"
  "note",, "Thank you for answering",

If the user selects to do *section 3* on the welcome page, survey will jump to the :tc:`branch3` :th:`branch_label`. The first row says to validate :tc:`user_info`. Survey then checks that every question with the :th:`validation_tags` :tc:`user_info` has been answered satisfactorily. If the questions have been answered correctly, it will go on to the next line (do section *section3*). If not, it will force the user to answer the missing, tagged questions.

The use of many different :th:`validation_tags` can allow users to update information in the survey as it becomes available and to restrict questions that depend on other information. In general, the validation feature can be used to give users more control over their work while still maintaining a level of order and restriction.

.. warning::

  Like the use of :tc:`sections` and :tc:`gotos`, :tc:`validate` has no user interface. In other words, when a user runs into a :tc:`validate` call, they will have no idea unless Survey finds something wrong with the form. Whenever using :tc:`sections`, :tc:`gotos`, or :tc:`validates`, if the form designer wants the user to be aware of what is happening, a note explicitly informing the user must be added.

.. _xlsx-using-custom-prompts:

Customizing Prompts
--------------------------

There are 3 ways to customize prompts:

  - Add additional columns to your XLSX Converter form definitions like :th:`inputAttributes` to tweak existing prompts.
  - If that's too limiting, you can make a custom HTML template by setting the :th:`templatePath` column. Templates can include :code:`<script>` and :code:`<style>` tags. ODK-X Survey uses :program:`handlebars` templates. :program:`Handlebars` has a few built-in helpers for creating conditional templates and templates with repeated components: see `their documentation <http://blog.teamtreehouse.com/handlebars-js-part-2-partials-and-helpers>`_.
  - Finally, if you need to parse data from a special type of input or retain some kind of state while your widget is active, you will need to delve into the ODK-X Survey JavaScript. By providing a :file:`customPromptTypes.js` file in your form directory, you can define :program:`Backbone` views that extend the base prompts.

Our HTML page rendering uses a custom database object coupled with :program:`Backbone` views to define the event handling, validation, data model interactions, and construction of the rendering context object that is passed to :program:`Handlebars`. The :program:`Handlebars` templates make use of :program:`Bootstrap` framework for UI components.

A custom prompt type available in the Application Designer repository is :th:`async_assign`. With :th:`async_assign`, a user is able to assign a value to a prompt using data collected from a different Survey form with a different underlying database table. As the name implies, the value is assigned to the prompt asynchronously.

.. tip::
  :th:`async_assign` must be used on a screen previous to where the prompt value will be needed.

Thus, a user should not use :th:`async_assign` to assign a value to a prompt and then attempt to use the prompt within that same screen as the value may not have been assigned yet. Once the value is assigned to the prompt, it can be used in subsequent screens.

The reason for not being able to use the value of a prompt from an :th:`async_assign` within the same screen has to do with the design of Survey. Every instance of a Survey form that a user fills out creates a row in a database table. Although the database interactions in Survey are asynchronous, you are able to see your data changes on the screen immediately because the data for the row is cached in a model data structure. When :th:`async_assign` is used, the :file:`formDef.json` file for the other form is read to create a model.
After that, the database table used to store the instances for the other form is queried to return the value(s) that are relevant for the assignment. These value(s) can then be manipulated for the assignment.

.. list-table:: async_assign Types Table
  :header-rows: 1
  :name: async-assign-types-table

  * - Name
    - Return Type
    - Description
  * - async_assign_max
    - number
    - | Returns the maximum value out of all form instances
      | that meet a query criteria.
  * - async_assign_min
    - number
    - | Returns the minimum value out of all form instances
      | that meet a query criteria.
  * - async_assign_avg
    - number
    - | Returns the average of all form instances
      | that meet a query criteria.
  * - async_assign_sum
    - number
    - | Returns the sum of all form instances
      | that meet a query criteria.
  * - async_assign_total
    - number
    - | Returns the total of all form instances
      | that meet a query criteria.
  * - async_assign_count
    - number
    - | Returns the number of values from all form instances
      | that meet a query criteria.
  * - async_assign_single_string
    - string
    - | Returns the first string from a form instance
      | that meets the query criteria.

There are 2 forms that use :th:`async_assign` in the Application Designer repository – the `agriculture.xlsx <https://github.com/odk-x/app-designer/blob/master/app/config/tables/agriculture/forms/agriculture/agriculture.xlsx>`_ and the `visit.xlsx <https://github.com/odk-x/app-designer/blob/master/app/config/tables/visit/forms/visit/visit.xlsx>`_ forms. In this particular example, we will look at the usage of the :th:`async_assign_single_string` in the `visit.xlsx <https://github.com/odk-x/app-designer/blob/master/app/config/tables/visit/forms/visit/visit.xlsx>`_  form. Only the relevant portions for the example are shown.

.. csv-table:: async_assign_single_string visit survey Worksheet Excerpt
  :header: "clause", "condition", "type", "name", "values_list", "calculation", "display.prompt.text"
  :name: async-assign-single-string-visit-survey-worksheet-excerpt

  "begin screen"
  ,, "async_assign_single_string", "plant_type_query_text", "plant_type_query",,
  "end screen"
  ,, "assign", "plant_type", "data('plant_type_query_text')",,

From the example, we can see that :tc:`plant_type_query_text` is assigned the value provided by :tc:`plant_type_query`. The value of :tc:`plant_type_query_text` is then used on the next screen to assign a value to :tc:`plant_type`. The **model** worksheet for the `visit.xlsx <https://github.com/odk-x/app-designer/blob/master/app/config/tables/visit/forms/visit/visit.xlsx>`_ form shows that :tc:`plant_type_query_text` is of type :tc:`string`. The relevant portion of the **model** worksheet is provided.

.. csv-table:: visit model Worksheet Excerpt
  :header: "name", "type", "isSessionVariable"
  :name: visit-model-worksheet-excerpt

  "plant_type_query_text","string", "TRUE"

The **queries** worksheet shows that the :tc:`plant_type_query` will assign the value of the :th:`fieldName` :tc:`planting` from the *plot* instance with the same :tc:`plot_id` as this *visit* instance to the :tc:`plant_type_query_text` prompt. See the relevant portion of the **queries** worksheet below.

.. csv-table:: visit queries Worksheet Excerpt
  :header: "query_name", "query_type", "linked_form_id", "linked_table_id", "selection", "selectionArgs", "fieldName", "newRowInitialElementKeyToValueMap", "openRowInitialElementKeyToValueMap"
  :name: visit-queries-worksheet-excerpt

  "plant_type_query", "linked_table", "plot", "plot", "_id = ?", "[data('plot_id')]", planting, "'{ plot_id : data('plot_id') }", "{}"


How to use :th:`async_assign`:
  1. Within *your_form* directory, include the `customPromptTypes.js <https://github.com/odk-x/app-designer/blob/master/app/config/tables/visit/forms/visit/customPromptTypes.js>`_ file. If *your_form* was named :file:`test`, your directory would be :file:`app/config/test/forms/test`.
  2. Create a folder named :file:`templates` in your :file:`app/config/your_form/forms/your_form` directory. Copy the `async_assign.handlebars <https://github.com/odk-x/app-designer/blob/master/app/config/tables/visit/forms/visit/templates/async_assign.handlebars>`_ file into this directory. In keeping with the example, this file would be :file:`app/config/test/forms/test/templates/async_assign.handlebars`.
  3. Update :file:`customPromptTypes.js` to include the path to your :file:`async_assign.handlebars` template. In keeping with the example, line 13 of :file:`customPromptTypes.js` should read :code:`templatePath: '../config/test/forms/test/templates/async_assign.handlebars',`.
  4. In your XLSX file, create a worksheet called **prompt_types**. Copy and paste the following into this worksheet:


  .. csv-table:: promptTypes Survey Worksheet
    :header: "prompt_type_name", "type"
    :name: prompt-types-survey-worksheet

    "async_assign_max","number"
    "async_assign_min","number"
    "async_assign_avg","number"
    "async_assign_sum","number"
    "async_assign_total","number"
    "async_assign_count","number"
    "async_assign_single_string","string"


  5. Now you can use the :th:`async_assign` prompt types in your form.

The :th:`async_assign` prompt types can be customized further if you are familiar with :program:`JavaScript`.

.. _xlsx-using-other-features:

Other Features
-----------------------

Different surveys and forms can also be entered using the :th:`external_link` type, the :th:`url` column, and the :th:`url.cell_type` column. To access a separate survey stored elsewhere, a local url can be specified in the format: :code:`'?' + opendatakit.getHashString('<relative path to survey>', null)`. Converting the example above to this format would leave the **choices** worksheet looking the same. However, the **survey** worksheet would look as follows:

.. list-table:: External Link Survey Worksheet Example
  :header-rows: 1
  :name: external-link-survey-worksheet-example

  * - branch_label
    - clause
    - condition
    - type
    - values_list
    - display.prompt.text
    - url
    - url.cell_type
  * -
    -
    -
    - user_branch
    - which_form
    - Choose a survey to fill out
    -
    -
  * - pizza_form
    -
    -
    -
    -
    -
    -
    -
  * -
    -
    -
    - external_link
    -
    - Open Form
    - '?' + opendatakit.getHashString('../config/tables/pizza/forms/pizza/', null)
    - formula
  * -
    - exit section
    -
    -
    -
    -
    -
    -
  * - birthday_form
    -
    -
    -
    -
    -
    -
    -
  * -
    -
    -
    - external_link
    -
    - Open Form
    - '?' + opendatakit.getHashString('../config/tables/birthdays/forms/birthday/', null)
    - formula
  * -
    - exit section
    -
    -
    -
    -
    -
    -
