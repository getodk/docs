************
pyxform
************

**pyxform** is a Python library that makes writing XForms for ODK Collect and enketo easy by converting XLS(X) spreadsheets into XForms. It is used as a library in a number of tools including the `ODK online converter <http://opendatakit.org/xiframe/>`_ and `Ona <https://ona.io/>`_.

.. _running-pyxform:

Running pyxform from command line
====================================
For those who want to convert forms at the command line, pyxform can be installed directly from the command line using `pip <https://en.wikipedia.org/wiki/Pip_(package_manager)>`_:

.. code-block:: console
  
  $ pip install pyxform
  
The :command:`xls2xform` command can then be used:

.. code-block:: console
  
  $ xls2xform path_to_XLSForm output_path
  
.. tip::
  
  For further queries or for more information please refer to the `Github repo <https://github.com/XLSForm/pyxform>`_.

