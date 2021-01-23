.. spelling::

  Aba
  aba
  Abia
  abia
  afikpo
  Afikpo
  amasiri
  Ebonyi
  ebonyi
  Ezeke
  ezeke
  Eziama
  eziama
  lga
  lgas
  Poperi
  poperi
  Umuogor
  umuogor

************************
Form Datasets
************************

ODK forms can use datasets in a variety of ways. These datasets can be either internal or external to the form.

Internal datasets are defined in the **choices** sheet of an XLSForm and are typically used to define the choices for :ref:`selects <select-widgets>`. These can also be used to look up values.

External datasets can be useful when:
  * data comes from another system. Using data files attached to the form generally requires fewer steps than adding the data to a form definition.
  * data changes frequently. One or more data file attached to the form can be updated without modifying the form definition.
  * data is reused between forms. It may be easier to attach the same data file to multiple forms instead of copying the data into all the form definitions.
  * the same forms are used in different contexts. For example, the exact same form definition could be used in multiple countries with different data files listing regions, local products, etc.

.. _selects-from-csv:

Building selects from CSV files
---------------------------------

CSV files can be used as datasets for select questions using ``select_one_from_file`` or ``select_multiple_from_file``. CSV files used this way must have :th:`name` and :th:`label` columns. For each row in the dataset, the text in the :th:`name` column will be used as the value saved when that option is selected and the text in the :th:`label` column will be used to display the option. For select multiples, :th:`name` must not contain spaces.

These files may also have any number of additional columns used in :ref:`choice filters <cascading-selects>` or other expressions. The example below uses one select from internal choices followed by selects from two different external CSV files.

.. csv-table:: survey
  :header: type, name, label, choice_filter

  select_one states, state, State,
  select_one_from_file lgas.csv, local_gov_area, Local Government Area, state=${state}
  select_multiple_from_file wards.csv, wards, Wards, lga=${local_gov_area}

.. csv-table:: choices
  :header: list_name, name, label, population

  states, abia, Abia, 4112230
  states, ebonyi, Ebonyi, 2176947

.. csv-table:: lgas.csv
  :header: name, label, state

  aba_n, Aba North, abia
  aba_s, Aba South, abia
  afikpo_n, Afikpo North, ebonyi

.. csv-table:: wards.csv
  :header: name, label, lga

  eziama, Eziama, aba_n
  umuogor, Umuogor, aba_n
  ezeke_amasiri, Ezeke amasiri, afikpo_n
  poperi_amasiri, Poperi amasiri, afikpo_n

.. _selects-from-xml:

Building selects from XML files
---------------------------------

XML files can be used as datasets that populate select questions using ``select_one_from_file`` or ``select_multiple_from_file``. This is typically less convenient than :ref:`using CSV files <selects-from-csv>`. However, knowing about the XML representation is helpful for understanding how to reference values in both CSV and XML files.

XML files used for selects must have the following structure and can have any number of ``item`` blocks:

  .. code-block:: xml

    <root>
      <item>
        <name>...</name>
        <label>...</label>
        ...
      </item>
      ...
    </root>

The ``item`` blocks are analogous to rows in the CSV representation. Each ``item`` must have at least :th:`name` and :th:`label` nested nodes and can have any number of additional nodes. These nodes correspond to columns in the CSV representation.

.. _referencing-values-in-datasets:

Referencing values in datasets
---------------------------------

:ref:`Xpath paths <xpath-paths>` can be used to reference values in internal or external datasets. These paths will start with a call on the ``instance(<instance name>)`` function to identify which dataset is being accessed. The next part of the path is generally `/root/item` because of the `XML structure used to represent datasets for selects <selects-from-xml>`. The only exception is when using custom XML files which may have arbitrary schemas if not used for selects.

For internal datasets, the instance name is the ``list_name`` specified on the **choices** sheet. For example, to look up a state population given the form :ref:`above <selects-from-csv>`, the instance name to use is ``states``. The expression would be ``instance("states")/root/item[name=${state}]/population``. To understand this expression better, read the section on :ref:`Xpath paths <xpath-paths>`.

For external datasets, the instance name is the filename specified in the ``select_one_from_file`` or ``select_multiple_from_file`` declaration without the file extension. For example, to look up a ward's label given the form :ref:`above <selects-from-csv>`, the instance name to use is ``wards`` because the filename referenced is ``wards.csv``. The expression would be ``instance("wards")/root/item[name=${ward}]/label``.