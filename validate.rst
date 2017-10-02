************************
ODK Form Validate
************************
Building a form is an essential step in ODK data collection project. You can use any tool you prefer for that, but you need to make sure that your form is compatible with ODK.
ODK Validate ensures that you have an OpenRosa compliant XForm, which prepares your form for deployment on ODK tools. 



Installation
--------------

- You need to have `java <https://java.com/en/download/>`_.
- Download ODK Validate tool `from <https://opendatakit.org/downloads/download-info/odk-validate-2/>`_ (:file:`ODK Validate vN.N.N.jar` is a `Java ARchive <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>`_),it doesn't require installation. 
- To run the tool, just click on ODK Validate vN.N.N.jar, you will see the following image:

.. image:: /img/validate/validate.png
 
``vN.N.N`` refers to the current version of ODK Validate. The `download page <https://opendatakit.org/downloads/download-info/odk-validate-2/>`_ describes new features added to the current version.  
  

.. warning::

  If you couldn't open the jar file, try to use the command line:
  
  .. code-block:: none
  
    java -jar path_to_jar
  
.. tip::

  In Windows, you can select and drop the jar file to get the full path for the command above.
     
  
Usage
-------

- Build your ODK form using either `ODK Build <https://build.opendatakit.org/>`_ or `XLSForm <http://docs.opendatakit.org/xlsform/>`_.

- `Convert the form into XML format <http://opendatakit.org/xiframe/>`_, and save it to your local machine.

- Open ODk Validate tool and from :guilabel:`choose file`, select your XML form. 

- The form will be validated automatically at the first time, and you can check if any error occurs.
  
  
.. tip::
 
  - If you see errors, try to correct the source file, and try to validate the form again. 
  - When you validate a form, the tool parses the XML script and checks it against `ODK XForms specifications <https://opendatakit.github.io/xforms-spec/>`_.
  
The following images illustrate two examples of:

1) a valid form

2) an invalid form
 
.. image:: /img/validate/validform.png
    
  
.. image:: /img/validate/invalidform.png
 
.. note::

  ODK has a few additional restrictions that may not be tested by this tool. In particular, a form id must be defined for the form to work in Aggregate.