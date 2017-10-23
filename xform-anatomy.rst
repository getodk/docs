****************
XForm Anatomy
****************

The purpose of this document is to provide an introduction to XForms, specifically the subset of XForms implemented by JavaRosa, so that anyone can make their own forms. There are several tools to help create your own XForms that work on JavaRosa platforms. They all allow you to create XForms, and the easier they are to use the less advanced functionality they provide. For detailed specifications, visit `ODK XForm Specifications <https://opendatakit.github.io/xforms-spec/>`_.

.. building-xforms:

Building XForms
=================

To build XForms, the most commonly used form standard is `XLSForm <https://opendatakit.org/use/xlsform/>`_, which uses an Excel spreadsheet of questions to generate the XForm file. There are many online XLSForm converters available. ODK's `Xiframe <http://opendatakit.org/xiframe/>`_ is an online XLSForm converter. Forms can be designed with Excel and XLSForm will convert them to XForms that can be used with ODK tools. `Pyxform <https://github.com/uw-ictd/pyxform>`_ is a Python library which works offline as well and can be used on the command line to convert forms. For simple form designing, `Build <https://opendatakit.org/use/build/>`_ can be used. XLSForm supports most features of the XForm specification. It is rare for ODK implementers to edit XForms manually, and doing so is highly error prone.


.. xform-file:

Overview of an XForm file
==========================

XForms consist of four major components:

- The **title** -- the name of the form. This will be shown to the user.
- The **instance** -- where your data are going to be stored. For each prompt, you need a place to store your answer.
- The **bindings** -- for each instance variable, you can include information about those data like the type (string, integer, etc.), the constraints on those data (i.e. less than 3), whether they're required or not, etc.
- The **body** -- how prompts are displayed to the user.

These are explained in the following XML example one by one.

.. code-block:: xml

  <h:html xmlns="http://www.w3.org/2002/xforms"
  xmlns:h="http://www.w3.org/1999/xhtml"
  xmlns:ev="http://www.w3.org/2001/xml-events"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:jr="http://openrosa.org/javarosa">

  <h:head>
  <h:title>Simple Form</h:title>
  <model>

  <!-- instance -->
  <instance>
   <data id="myform" >
     <meta>
       <instanceID/>
     </meta>
     <mystring/>
   </data>
  </instance>

  <!-- bindings -->
  <bind nodeset="/data/meta/instanceID" type="string" 
           readonly="true()" calculate="concat('uuid:',uuid())" />
  <bind nodeset="/data/mystring" type="string"/>

  </model>
  </h:head>

  <!-- body -->
  <h:body>
  <input ref="/data/mystring">
    <label>This is a string prompt</label>
    <hint>You don't need a hint, but you can add one</hint>
  </input>
  </h:body>

  </h:html>

Instances
----------

.. code-block:: html

  <instance>
   <data id="myform" >
    <meta>
      <instanceID/>
    </meta>
    <mystring/>
  </data>
  </instance>

Here, the first element labaled ``instance`` is the primary instance, and it has ``data`` element as its child node, and is the secondary instance in this example. This secondary instance is identified via the ``id`` attribute as the 'myform' form. This ``id`` attribute, and an optional version attribute, provide the internal unique name of this form to the software. The software only allows one form definition for each (id, version) pair.

Each blank XForm must have a completed instance within it, as it contains all the data. This instance contains two fields -- the first, called "instanceID" is nested within a ``meta`` element. The second field is called "mystring." Nesting within elements can help organize your data.

The other field, ``<mystring/>``, is where we're going to store the answers for our form instance, but it's only a placeholder. We **DO NOT** specify a data type here.

The first instance in the form represents a saved or completed version of the form. When you save a filled-in form, the XML output file will look something like this:

.. code-block:: xml

  <data id="myform" >
    <meta>
      <instanceID>uuid:23b56e39-ef50-4510-b85f-c454cd5465c1</instanceID>
    </meta>
    <mystring>Hello World!  This is my answer!</mystring>
  </data>

Beginning with ODK Collect 1.2, there can be multiple instances defined in the form. The second and subsequent instance definitions can specify static data used in filling out the form (e.g., lists of cities within each county within a given state, dosage tables). The most common use would be to present the choices in a cascading select, e.g., where you are asked to first choose a state, then the county within that state, then the city within that county. 

If you specify a value for any element of the primary instance in the original XForm, it presents that as the default answer.

.. code-block:: xml

  <mystring>Default answer</mystring>

Here, *Default answer* becomes the default value for ``<mystring>``.

Each node in the Primary Instance represents a piece of data that will be collected by the form.

.. code-block:: xml

  <instance>
  <data id="myotherform" >
    <meta>
      <instanceID/>
    </meta>
    <mystring/>
    <a_number/>
    <birthday/>
    <date>2010-06-15</date>
    <select>a c</select>
    <favorite_number>7</favorite_number>
    <whatever_i_want/>
  </data>
  </instance>

.. form-bindings:

Bindings
---------

Since we have two fields, we need two bindings:

.. code-block:: html

  <bind nodeset="/data/meta/instanceID" type="string" 
           readonly="true()" calculate="concat('uuid:',uuid())" />
  <bind nodeset="/data/mystring" type="string"/>

The first binding defines how the unique identifier for a filled-in form will be constructed.

The second binding specifies that ``<mystring>`` will hold a string value. Bindings that do not specify a "type" are assumed to be strings. However, ODK Aggregate issues warnings if a type is not specified because ordering of numbers differs from ordering of strings; specifying a "type" ensures that the proper ordering is applied, i.e., "10" is ordered alphabetically less than "2", but, if these are interpreted as numbers, the order is reversed (10 is greater than 2).

Bindings are also where you specify branching, calculations, read-only fields, required fields, input constraints, etc.

Note that the binding references the instance node using an XPath expression. The expression represents the hierarchy inside the ``<instance>`` tags.

.. code-block:: xml

  <instance>
  <data>
    <mystring/> <!-- referenced as /data/mystring -->
  </data>
  </instance>

In this example, mystring is referenced by: :guilabel:`/data/mystring`.

.. form-body:

Body
-----

The body represents what should be shown to the user. In this example, we have two pieces of data in the form, but the ``<instanceID>`` is not editable by the user, so it will not appear in the rendered form. Thus, we will only have one data to be collected by the user (in the prompt), and that is for the ``<mystring>``. This is placed in the body element:

.. code-block:: xml

  <h:body>
  <input ref="/data/mystring">
    <label>This is a string prompt</string>
    <hint>You don't need a hint, but you can add one</hint>
  </input>
  </h:body>

The type of form widget is specified by the tag name of the element. Here it is shown by the ``<input>`` tag. To specify which field will store the response, we use the ``ref=""`` attribute. The ``<label>`` is what will be shown to the user as the prompt header, and the ``<hint>`` is an optional piece of text to display.

For a full list of body element types see `form body <https://opendatakit.org/help/form-design/body/>`_ or look through the `widget examples <https://docs.opendatakit.org/form-widgets/>`_.

.. adding-another-prompt

Adding another prompt
----------------------

To finish our example, we'll add another prompt to our form. We'll need to add a new element to the instance, a new binding, and a new element to the body. This time, however, we'll make the prompt required for the user to answer. Changed lines are in red. We update our form ID to reflect that this is a different form than the original one.

So our new form now looks like this:

.. code-block:: xml

  <h:html xmlns="http://www.w3.org/2002/xforms"
  xmlns:h="http://www.w3.org/1999/xhtml"
  xmlns:ev="http://www.w3.org/2001/xml-events"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:jr="http://openrosa.org/javarosa">

  <h:head>
  <h:title>Less Simple Form</h:title>
  <model>

    <instance>
      <data id="mynewform" >
        <meta>
          <instanceID/>
        </meta>
        <mystring/>
        <q2/>
      </data>
    </instance>

    <bind nodeset="/data/meta/instanceID" type="string" 
           readonly="true()" calculate="concat('uuid:',uuid())" />
    <bind nodeset="/data/mystring"/>
    <bind nodeset="/data/q2" required="true()"/>

  </model>
  </h:head>

  <h:body>
   <input ref="mystring">
     <label>This is a string prompt</label>
     <hint>You don't need a hint, but you can add one</hint>
   </input>
   <input ref="q2"> <label>This is another prompt</label> <hint>This prompt is required</hint> </input>
  </h:body>

.. xpath-expressions:

Referencing Fields with XPath expressions
------------------------------------------

If you are using XLSForm, and the groups are not repeat groups, you would just use ${fieldname} and it would be transformed into the appropriate XPath expression for that field. If you are using repeat groups, however, you need to specify which copy of the repeat group you want to reference. For that, you need to construct your own XPath expressions.

To understand XPath expressions, you need to understand how groups affect the XML file that is generated by whatever design tool you are using. The Sample Excel file (available here ) converts to an XML file that has the following submission instance structure. You can see this by running the XLSForm converter on the Excel file and opening the XML file that is generated, searching down the file for the section:

.. code-block:: xml

  <instance>
     <sample_xlsform id="sample">
          <some_text/>
          <text_image_audio_video_test/>
          <a_integer>123</a_integer>
          <a_decimal/>
          <calculate/>
          <calculate_test_output/>
          <select_example/>
          <required_text/>
          <acknowledge_test/>
          <skip_example/>
          <skipable_question/>
          <repeat_test jr:template="">
               <repeating_question/>
          </repeat_test>
          <group_test>
               <field_list_note/>
               <select_multiple_1/>
               <select_multiple_2/>
          </group_test>
          <table_list_example>
               <generated_table_list_label_21/>
               <reserved_name_for_field_list_labels_22/>
               <table_list_question_1/>
               <table_list_question_2/>
          </table_list_example>
          <select_appearance_note/>
          <labeled_select_group>
               <label_test/>
               <list-nolabel_test/>
          </labeled_select_group>
          <compact_test/>
          <data_types_note/>
          <date_test/>
          <time_test/>
          <datetime_test/>
          <geopoint_test/>
          <barcode_test/>
          <image_test/>
          <audio_test/>
          <video_test/>
          <metadata_note/>
          <start/>
          <start_test_output/>
          <end/>
          <end_test_output/>
          <today/>
          <today_test_output/>
          <deviceid/>
          <deviceid_test_output/>
          <simserial/>
          <simserial_test_output/>
          <phonenumber/>
          <phonenumber_test_output/>
          <meta>
               <instanceID/>
          </meta>
     </sample_xlsform>
  </instance>

Read up on XML to understand how to read this. The "root node" of the data submitted from ODK Collect is the node within the ``<instance> section -- <sample_xlsform>`` in this case. That name is based upon the filename that you send to XLSForm. If you change the filename, the "root node" changes and it is a different form.

The above form contains several groups (group_test, table_list_example, labeled_select_group, meta) and one repeat group (repeat_test).

To reference fields using XPath expressions, you construct a slash (/)-separated path to the field, starting with the "root node" of the form (e.g., :guilabel:`/sample_xlsform/group_test/select_multiple_1`) OR you can use an XPath expression that is relative to the current field by beginning the path with "." (a.k.a. myself) or ".." (a.k.a. my enclosing group). Relative paths generally begin with ``../`` and the ``../`` can be repeated to go to the enclosing group of the enclosing group, etc.

For the sample form above, if you wanted to refer to the value of ``select_multiple_1`` from within the field ``label_test``, you would use :guilabel:`../../group_test/select_multiple_1`.
This breaks down, when starting from :guilabel:`/sample_xlsform/labeled_select_group/label_test`:

+------------------------------------+----------------------------------------------+
| Expression:                        | Refers to:                                   |
+====================================+==============================================+
| ..                                 | /sample_xlsform/labeled_select_group         |
+------------------------------------+----------------------------------------------+
| ../..                              | /sample_xlsform                              |
+------------------------------------+----------------------------------------------+
| ../../group_test                   | /sample_lsform/group_test                    |
+------------------------------------+----------------------------------------------+
| ../../group_test/select_multiple_1 | /sample_xlsform/group_test/select_multiple_1 |
+------------------------------------+----------------------------------------------+

When working with repeat groups, you need to be careful. The XLSForm expression ``${repeating_question}`` is expanded by the XLSForm converter to: :guilabel:`/sample_xlsform/repeat_test/repeating_question`. Unfortunately, this absolute XPath refers to all the responses to this question, across all filled-in repeats. The first time through your repeat group, there will be only one answer in this set (the current repeat), and constraints using an absolute XPath or the ``${...}`` expansion will resolve to that one answer. The second time through your repeat group, there will be two possible answers in this set, and any constraints using an absolute XPath or the ``${...}`` expansion will fail because the constraint evaluator does not know which answer it should use when evaluating the constraint.

In general, the way around this is to use relative paths in your constraints. The constraints you generally want to apply are from values within the same repeat group. If you need to reference values in a repeat group from outside that repeat group, you can do this using either the ``indexed-repeat()`` function, described on the bindings page, or you can use a position qualifier. 

**IMPORTANT NOTE:** The XForm evaulator used by the ODK tools (the "javarosa" evaluator) does not support the full range of position qualifiers. You must specify the position strictly as follows.

To use a position qualifier, it must be of the form :guilabel:`...path-to-repeat-group/repeat_group[position(.)=value]/additional-path-elements`

For the sample form, to refer to the value of the repeating_question field in the 1st repeat, you would use :guilabel:`/sample_xlsform/repeat_test[position(.)=1]/repeating_question`

And to refer to the value of the repeating_question field in the 2nd repeat, you would use :guilabel:`/sample_xlsform/repeat_test[position(.)=2]/repeating_question`

Complicating all of this is the potential presence of read-only data instances within a form that are useful for cascading selects. In this case, while the absolute XPath expressions can be resolved correctly, the relative XPath expressions (those beginning with "." or ".."), when applied within one of these read-only data instances (e.g., as a filter expression), will be evaluated relative to the current node within the read-only data instance, rather than relative to the field in the data collection form.

To manage that, or to explicitly reference one of the read-only data instances, you need to use either:

+------------------------------------+---------------------------------------------------------------------------------------------------+
| Prefix:                            | Meaning:                                                                                          |
+====================================+===================================================================================================+
| current()/.                        | Reference the field ("myself") in the data collection form                                        |
+------------------------------------+---------------------------------------------------------------------------------------------------+
| current()/..                       | Reference the enclosing group of the field in the data collection form                            |
+------------------------------------+---------------------------------------------------------------------------------------------------+
| instance('name')/.                 | Reference the current group or field in the read-only data instance 'name'                        |
+------------------------------------+---------------------------------------------------------------------------------------------------+
| instance('name')/..                | Reference the enclosing group of the current group or field in the read-only data instance 'name' |
+------------------------------------+---------------------------------------------------------------------------------------------------+

The "Biggest N of Set" form exercises all of these XPath constructs. The Excel spreadsheet defining that form is `here <https://opendatakit.org/wp-content/uploads/xpath_example/NBiggestOfSet.xls>`_. After running this through the XLSForm converter, you need to hand-edit the generated XML to change one of the <output> paths to use a relative path expression. The resulting working XML file is available `here as a download <https://opendatakit.org/wp-content/uploads/xpath_example/NBiggestOfSet.xml>`_. Download and use a visual file comparison tool (such as WinDiff) to compare this working XML file against the one generated by XLSForm to see where this change needed to be made.

.. another-xpath-example:

Another XPath example
----------------------

**Problem:** You are gathering data on a farmer's plots and the crops grown in them. A plot can have multiple crops growing in it and you want to ensure that you never gather information twice for a given crop and plot.

Before looking at the explanaton please download the `XLS <https://opendatakit.org/wp-content/uploads/2016/08/OnlyOneOfSet.xls>`_ and the `XML <https://opendatakit.org/wp-content/uploads/2016/08/OnlyOneOfSet.xml>`_. files.

The XML file has been generated from the XLS file then manually edited to use the names of the chosen crop and plot in the yield question. The plot and crop selections are asked on the same screen (inside a field-list group). This is recommended since the constraint is applied on forward-swipe off of a screen. If you ask these questions on different screens, you might get odd behaviors.

The technique is to use the ``selected()`` predicate to detect whether an already-entered value matches the current ``crop_type`` field's answer. If it does, the constraint is violated:

:guilabel:`not(selected(/* accumulation of already-entered values */, .))`

Multiple-select responses are just space-separated lists of values. We can construct such a list using the join command:

:guilabel:`join(' ', /* already-entered-values */)`

giving us this constraint:

:guilabel:`not(selected(join(' ', /* already-entered-values */ ), .))`

To get the already-entered values, you need a complicated XPath expression. In this case, we are referencing the values within the existing filled-in form, so we want to refer to the ``crop_type`` values in our form. Those have this path (the first element in the path is the filename of your .xls file):

:guilabel:`/OnlyOneOfSet/plot/plot_info/crop_type`

But if we just used this, we would get the current answer PLUS the answers for all choices of plot code (Plot A, Plot B, etc.). We need to filter which repeat groups we include to construct the set of all ``crop_type`` values that we care about. To do that, we apply a filtering constraint on the repeat group:

:guilabel:`/OnlyOneOfSet/plot[ /* filtering constraint to select applicable repeats goes here */ ]/plot_info/crop_type`

And the filtering constraint is evaluated where '.' refers to the currently-under-consideration plot repeat, and we need to use current()/ to refer to the current ``crop_type`` value.

With that syntax:

- :guilabel:`current()/` -- crop_type field currently being verified
- :guilabel:`current()/../` -- plot_info field-list group containing that field
- :guilabel:`current()/../plot_code` -- the plot code (Plot A, Plot B, etc.) corresponding to the ``crop_type`` field currently being verified.
- :guilabel:`current()/../..` -- plot repeat instance of the crop_type field currently being verified.

So we have two parts to the constraint:

:guilabel:`./plot_info/plot_code=current()/../plot_code` -- select repeats with plot_code choices matching the plot_code of the current repeat.

:guilabel:`position(.) != position(current()/../..)` -- omit the current repeat from consideration. 

.. note::

  If you plan to send your data to ODK Aggregate, you'll want to read about limitations in form IDs, instance naming, string lengths and much more.














  




