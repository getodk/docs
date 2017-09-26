****************
Form Design
****************

The purpose of this document is to provide a detailed breakdown of XForms, specifically the subset of XForms implemented by JavaRosa, so that anyone can make their own forms. There are several tools to help create your own XForms that work on JavaRosa platforms. They all allow you to create XForms, and the easier they are to use the less advanced functionality they provide.

Begin with a JavaRosa-compliant automated design tool
======================================================

Use an automated tool compatible with JavaRosa to build the basic XForm. These tools understand the text internationalization features of JavaRosa XForms and can restructure your input so that the question text is grouped into an ``<itext/>`` translation block for internationalization.

We have a `form design guide <https://opendatakit.org/help/form-design/guidelines/>`_, and the JavaRosa community has a `description of the specification <https://bitbucket.org/javarosa/javarosa/wiki/xform>`_ we support and a `good tutorial <https://bitbucket.org/javarosa/javarosa/wiki/buildxforms>`_. We also have `examples of forms available <https://github.com/opendatakit/sample-forms>`_ and a simple graphical form designer `ODK Build <https://opendatakit.org/use/build/>`_. Another form builder `XLSForm <https://opendatakit.org/use/xlsform/>`_ uses an Excel spreadsheet of questions to generate the XForm file; it is more suitable when working with larger forms. `PurcForms designer <https://code.google.com/archive/p/purcforms/>`_ is another tool.

Our experience is that these form design tools can provide a good starting point, but, to enable advanced features, you will inevitably need to edit the resulting form. After hand-editing, you should verify the syntax of the form using ODK Validate.

Overview of an XForm file
==========================

XForms consist of four major components:

- The **title** -- the name of the form. This will be shown to the user.
- The **instance** -- where your data are going to be stored. For each prompt, you need a place to store your answer.
- The **bindings** -- for each instance variable, you can include information about those data like the type (string, integer, etc.), the constraints on those data (i.e. less than 3), whether they're required or not, etc.
- The **body** -- how prompts are displayed to the user.

These are explained in the following HTML example one by one.

.. code-block:: html

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

Here we have a single instance called "data". This instance is identified via the 'id' attribute as the 'myform' form. This id attribute, and an optional version attribute, provide the internal unique name of this form to the software. The software only allows one form definition for each (id, version) pair.

The form itself has two variables; the first, called "instanceID" is nested within a "meta" block. The second variable is called "mystring." Nesting within blocks can help organize your data; we could have nested "mystring" within one or more blocks. The "meta" block and "instanceID" variable are defined as part of a form design standard, and must appear as shown by OpenRosa 1.0 Metadata Schema.

We are going to compute and store a unique identifier for each filled-in form in the ``<instanceID/>`` variable. This will enable ODK Aggregate (or any back-end process) to de-duplicate submissions if, for example, the same filled-in form were somehow submitted twice.

The other variable, ``<mystring/>``, is where we're going to store the answer to our prompt, but it's only a placeholder. We **DO NOT** specify a data type here.

The first instance in the form represents a saved or completed version of the form. When you save a filled-in form, the XML output file will look something like this:

.. code-block:: xml

  <data id="myform" >
    <meta>
      <instanceID>uuid:23b56e39-ef50-4510-b85f-c454cd5465c1</instanceID>
    </meta>
    <mystring>Hello World!  This is my answer!</mystring>
  </data>

Beginning with ODK Collect 1.2, there can be multiple instances defined in the form. The second and subsequent instance definitions can specify static data used in filling out the form (e.g., lists of cities within each county within a given state, dosage tables). The most common use would be to present the choices in a cascading select, e.g., where you are asked to first choose a state, then the county within that state, then the city within that county. 

If you specify a value for :``<mystring>`` in the original XForm, it presents that as the default answer to the prompt:

.. code-block:: xml

  <mystring>Default answer</mystring>

Adding more prompts is as simple as adding more variables:

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

Bindings
---------

Since we have two variables, we need two bindings:

.. code-block:: html

  <bind nodeset="/data/meta/instanceID" type="string" 
           readonly="true()" calculate="concat('uuid:',uuid())" />
  <bind nodeset="/data/mystring" type="string"/>

The first binding defines how the unique identifier for a filled-in form will be constructed.

The second binding specifies that ``<mystring>`` will hold a string value. Bindings that do not specify a "type" are assumed to be strings. However, ODK Aggregate issues warnings if a type is not specified because ordering of numbers differs from ordering of strings; specifying a "type" ensures that the proper ordering is applied, i.e., "10" is ordered alphabetically less than "2", but, if these are interpreted as numbers, the order is reversed (10 is greater than 2).

Bindings are also where you specify branching, calculations, read-only fields, required fields, input constraints, etc.

Note that the binding references the instance node using an XPath expression. The expression represents the hierarchy inside the ``<instance>`` tags.

.. code-block:: html

  <instance>
  <data>
    <mystring/> <!-- referenced as /data/mystring -->
  </data>
  </instance>

In this example, mystring is referenced by: :guilabel:`/data/mystring`.

Body
-----

The body represents what should be shown to the user. In this example, we have two variables, but the ``<instanceID>`` variable is merely for bookkeeping. Thus, we will only have one prompt displayed to the user for the ``<mystring>`` variable. This is placed in the body element:

.. code-block:: html

  <h:body>
  <input ref="/data/mystring">
    <label>This is a string prompt</string>
    <hint>You don't need a hint, but you can add one</hint>
  </input>
  </h:body>

The type of widget/prompt to show the user is specified by the <input> tag. Where to put the data is specified by the ``ref=""`` attribute. The <label> is what will be shown to the user as the prompt header, and the ``<hint>`` is an optional piece of text to display.

For a full list of body element types see `form body <https://opendatakit.org/help/form-design/body/>`_ or look through the `widget examples <https://opendatakit.org/help/form-design/examples/>`_.

Adding another prompt
----------------------

To finish our example, we'll add another prompt to our form. We'll need to add a new element to the instance, a new binding, and a new element to the body. This time, however, we'll make the prompt required for the user to answer. Changed lines are in red. We update our form ID to reflect that this is a different form than the original one.

So our new form now looks like this:

.. code-block:: html

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

To reference fields using XPath expressions, you construct a slash (/)-separated path to the field, starting with the "root node" of the form (e.g., :guilabel:`/sample_xlsform/group_test/select_multiple_1`) OR you can use an XPath expression that is relative to the current field by beginning the path with "." (a.k.a. myself) or ".." (a.k.a. my enclosing group). This is why constraints can be written as, e.g., " . < 6 or . > 10 " -- the "." stands for myself (the value in the field that has the constraint applied to it).

Relative paths generally begin with "../" and the "../" can be repeated to go to the enclosing group of the enclosing group, etc.

For the sample form above, if you wanted to refer to the value of select_multiple_1 from within the field label_test, you would use:

:guilabel:`../../group_test/select_multiple_1`

this breaks down, when starting from /sample_xlsform/labeled_select_group/label_test :

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

When working with repeat groups, you need to be careful. The XLSForm expression ${repeating_question} is expanded by the XLSForm converter to: /sample_xlsform/repeat_test/repeating_question. Unfortunately, this absolute XPath refers to all the responses to this question, across all filled-in repeats. The first time through your repeat group, there will be only one answer in this set (the current repeat), and constraints using an absolute XPath or the ${...} expansion will resolve to that one answer. The second time through your repeat group, there will be two possible answers in this set, and any constraints using an absolute XPath or the ${...} expansion will fail because the constraint evaluator does not know which answer it should use when evaluating the constraint.

In general, the way around this is to use relative paths in your constraints. The constraints you generally want to apply are from values within the same repeat group (e.g., you want to require fieldB to be answered if the value in fieldA within that same repeat group is less than 5. 

i.e., the relevant condition on fieldB would be written: "../fieldA < 5"

If you need to reference values in a repeat group from outside that repeat group, you can do this using either the indexed-repeat() function, described on the bindings page, or you can use a position qualifier. 
















  




