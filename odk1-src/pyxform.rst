.. spelling::

  xform
  xlsx
	
************
pyxform
************

:program:`pyxform` is a Python library that makes writing XForms for ODK Collect and Enketo easy by converting Excel spreadsheets into XForms. It is used as a library in a number of tools including the `XLSForm Online <https://opendatakit.org/xiframe/>`_ and `XLSForm Offline <https://github.com/opendatakit/xlsform-offline/releases>`_.

.. _running-pyxform:

Running pyxform from command line
====================================
For those who want to convert forms at the command line, pyxform can be installed directly from the command line using `pip <https://en.wikipedia.org/wiki/Pip_(package_manager)>`_:

.. code-block:: console
  
  $ pip install pyxform
  
The :command:`xls2xform` command can then be used:

.. code-block:: console
  
  $ xls2xform path_to_XLSForm output_path
  
.. seealso:: `pyxform repo on GitHub <https://github.com/XLSForm/pyxform>`_.

.. tip::
  :name: quick-form-push

  .. rubric:: Moving quickly from XLSForm to a device

  Use :program:`pyxform` together with :doc:`adb <collect-adb>`
  to quickly convert an XLSForm and load it to a device.
  
  Once you have both tools installed,
  convert and push in a single line:
  
  .. code-block:: console
  
    $ xls2xform form-name.xlsx form-name.xml && adb push form-name.xml /sdcard/odk/forms/form-name.xml
  
  For even more efficiency,
  you can save a lot of typing 
  by adding a few lines to your :file:`.bash_profile`.
  
  .. code-block:: bash
  
    x2x () { xls2xform "$1.xlsx" "$1.xml" ; }
    pf () { adb push "$1.xml" "/sdcard/odk/forms/$1.xml" ; }
    xlpf () { x2x "$1" && pf "$1" ; }
    
  Then, from the command line:
  
  .. code-block:: console
  
    # To convert a form.
    $ x2x form-name
    
    # To push a form.
    $ pf form-name
    
    # To convert and push at once.
    $ xlpf form-name
    
   
