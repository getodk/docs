.. spelling::

  validator
  vN

ODK Validate
==================

:dfn:`ODK Validate` is a tool 
that ensures an XForms XML file 
conforms to the `XForms specification`_.

.. _XForms specification: https://getodk.github.io/xforms-spec/

Validate should be used to check hand-edited XForms.
It is not needed when creating forms with 
:doc:`xlsform` or :doc:`build-intro`,
unless you edit those forms manually after creating them.

.. _setting-up-validate:

Setting up Validate
----------------------

.. note:: 

  The Validate file available for download is an executable Java application. Once downloaded, it can be run directly and does not need to be installed.

.. admonition:: Before you begin...

  Make sure `Java 8` is installed on your system.
  
  .. _Java: https://java.com/en/download/


#. `Download Validate`_.

   .. _Download Validate: https://github.com/getodk/validate/releases/latest

#. If you wish, move :program:`Validate` to your :file:`Applications` directory or another suitable location.
   

.. _using-validate:

Using Validate
---------------

#. Open :program:`Validate`.
#. Find your XForms :file:`*.xml` file using :guilabel:`Choose file`, 
   and :guilabel:`Open` it.
#. Review and fix any warning messages.

   .. image:: /img/validate/invalidform.png

#. If needed, :guilabel:`Validate Again`.

   .. image:: /img/validate/validform.png

Command line
~~~~~~~~~~~~

Validating a single form:

.. code-block:: console

  $ java -jar {path/to/validate-jar-file} {path/to/xform.xml}

Validating multiple forms:

.. code-block:: console

  $ java -jar {path/to/validate-jar-file} [--fail-fast] {path/to/xform1.xml} {path/to/xform2.xml} {path/to/xform3.xml}

The optional `--fail-fast` flag tells Validate to exit on the first error rather than validating all forms and reporting an error at the end.

.. warning::

  This tool validates XML files against the XForms specification.
  It does not check every detail needed 
  to ensure smooth operation in the ODK ecosystem.
  For example, ODK Central requires that forms have a unique form ID,
  which this tool does not check.
