****************
Form Design
****************

The purpose of this document is to provide a detailed breakdown of XForms, specifically the subset of XForms implemented by JavaRosa, so that anyone can make their own forms. As of this writing there are several tools to help create your own XForms that work on JavaRosa platforms. They all allow you to create XForms, though generally the easier they are to use the less advanced functionality they provide. This set of pages will hopefully allow you to manually edit forms to your specific needs.

Begin with a JavaRosa-compliant automated design tool
======================================================

Use an automated tool compatible with JavaRosa to build the basic XForm. These tools understand the text internationalization features of JavaRosa XForms and can restructure your input so that the question text is grouped into an :guilabel:`<itext/>` translation block for internationalization.

We have a `form design guide <https://opendatakit.org/help/form-design/guidelines/>`_, and the JavaRosa community has a `description of the specification <https://bitbucket.org/javarosa/javarosa/wiki/xform>`_ we support and a `good tutorial <https://bitbucket.org/javarosa/javarosa/wiki/buildxforms>`_. We also have `examples of forms available <https://github.com/opendatakit/sample-forms>`_. We have a simple graphical form designer `ODK Build <https://opendatakit.org/use/build/>`_. Another form builder `XLSForm <https://opendatakit.org/use/xlsform/>`_uses an Excel spreadsheet of questions to generate the XForm file; it is more suitable when working with larger forms. `PurcForms designer <https://code.google.com/archive/p/purcforms/>`_ is another tool.

Our experience is that these form design tools can provide a good starting point, but, to enable advanced features, you will inevitably need to edit the resulting form. After hand-editing, you should verify the syntax of the form using ODK Validate.

Overview of an XForm file
==========================

XForms consist of four major components:

- The title -- the name of the form. This will be shown to the user.
- The instance -- where your data are going to be stored. For each prompt, you need a place to store your answer.
- The bindings -- for each instance variable, you can include information about those data like the type (string, integer, etc.), the constraints on those data (i.e. less than 3), whether they're required or not, etc.
- The body -- how prompts are displayed to the user.

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


