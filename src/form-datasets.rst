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
  geojson
  Giger
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

Internal datasets are defined in the **choices** sheet of an XLSForm and are typically used as choices for :ref:`selects <select-widgets>`. You can also define a dataset in the **choices** sheet to :ref:`look up values <referencing-values-in-datasets>` based on user input. Learn how to define internal datasets in the section on :ref:`selects <select-widgets>`.

External datasets are useful when:

  * data comes from another system. Using data files attached to the form generally requires fewer steps than adding the data to a form definition.
  * data changes frequently. One or more data file attached to the form can be updated without modifying the form definition.
  * data is reused between forms. It may be easier to attach the same data file to multiple forms instead of copying the data into all the form definitions.
  * the same forms are used in different contexts. For example, the exact same form definition could be used in multiple countries with different data files listing regions, local products, etc.

.. note::

  Most mobile devices released in 2019 or later can handle lists of 50,000 or more without slowdowns. If you experience slowdowns, please share the size of the dataset, the device you are using, and any expressions that reference the dataset on `the community forum <https://forum.getodk.org/c/support/6>`_ or to support@getodk.org.


.. _selects-from-csv:

Building selects from CSV files
---------------------------------

CSV files can be used as datasets for select questions using ``select_one_from_file`` or ``select_multiple_from_file``. CSV files used this way must have :th:`name` and :th:`label` columns unless you use the :th:`parameters` column to :ref:`customize the columns used <customizing-label-and-value>`. For each row in the dataset, the text in the value column (defaults to :th:`name`) will be used as the value saved when that choice is selected and the text in the label column (defaults to :th:`label`) will be used to display the choice. For select multiples, :th:`name` must not contain spaces.

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

.. _selects-from-geojson:

Building selects from GeoJSON files
------------------------------------

*New in* `ODK Collect v2022.2.0 <https://github.com/getodk/collect/releases/tag/v2022.2.0>`_, `ODK Central v1.4.0 <https://forum.getodk.org/t/odk-central-v1-4/36886>`_

.. warning::
  GeoJSON attachments are not yet available in web forms (Enketo).


GeoJSON files that follow `the GeoJSON spec <https://datatracker.ietf.org/doc/html/rfc7946>`_ can be used as datasets that populate select questions using ``select_one_from_file``. Selects from GeoJSON may be styled as maps using the :ref:`map appearance <select-from-map>` but can also use any other :ref:`select appearance <select-appearances>`. In order to be used by a form, a GeoJSON file:

- *MUST* have a ``.geojson`` extension (NOT ``.json``)
- *MUST* define a single top-level `FeatureCollection <https://datatracker.ietf.org/doc/html/rfc7946#section-3.3>`_
- *MUST* include a unique identifier for each feature (by default, a top-level :th:`id`, falling back to an :th:`id` property, or can be :ref:`configured <customizing-label-and-value>`)
- *MUST* only include features with `Point geometry <https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.1>`_

.. csv-table:: survey
  :header: type, name, label

  select_one_from_file museums.geojson,museum,Select the museum closest to you

GeoJSON files referenced in forms can have any number of ``features`` and any number of custom ``properties``.

.. code-block:: json

    {
      "type": "FeatureCollection",
      "features": [
          {
              "type": "Feature",
              "geometry": {
                  "type": "Point",
                  "coordinates": [
                      7.0801379,
                      46.5841618
                  ]
              },
              "properties": {
                  "id": "fs87b",
                  "title": "HR Giger Museum",
                  "annual_visits": 40000
              }
          }
      ]
    }

Custom properties such as ``annual_visits`` above are displayed by :ref:`selects from map <select-from-map>`. All properties can be :ref:`referenced by any part of the form <referencing-values-in-datasets>`.

A feature's :th:`geometry` can be accessed as ``geometry`` and is provided in :ref:`the ODK format <location-widgets>`. Given the GeoJSON file and the form definition above, if the user selected "HR Giger Museum", the value of ``${museum}`` would be ``"fs87b"``. The expression ``instance('museums')/root/item[id=${museum}]/geometry`` would evaluate to ``46.5841618 7.0801379 0 0`` which is a point in :ref:`the ODK format <location-widgets>`.


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

:ref:`XPath paths <xpath-paths>` can be used to reference values in internal or external datasets. These paths will start with the ``instance(<instance name>)`` function to identify which dataset is being accessed. The next part of the path is generally ``/root/item`` because of the :ref:`XML structure used to represent datasets for selects <selects-from-xml>`. The only exception is when using custom XML files which may have arbitrary schemas if not used for selects.

For internal datasets, the instance name is the ``list_name`` specified on the **choices** sheet. For example, to reference the population of the selected state given the form :ref:`above <selects-from-csv>`, the instance name to use is ``states``. The expression would be ``instance("states")/root/item[name = ${state}]/population``. To understand this expression better, read the section on :ref:`XPath paths <xpath-paths>` and especially the subsection about :ref:`XPath paths for filtering <xpath-predicates-for-filtering>`. You could also do things like count the number of states with a population above a certain threshold using an expression like ``count(instance("states")/root/item[population > ${pop_threshold}])``.

.. note::

  Due to a pyxform limitation, it is necessary for there to be some value in the `choice_filter` column (for at least one question) when referencing internal datasets. If none of the questions in your form need filtering, put `true()` as the `choice_filter` value.

For external datasets, the instance name is the filename specified in the ``select_one_from_file`` or ``select_multiple_from_file`` declaration without the file extension. For example, to look up a ward's label given the form :ref:`above <selects-from-csv>`, the instance name to use is ``wards`` because the filename referenced is ``wards.csv``. The expression would be ``instance("wards")/root/item[name = ${ward}]/label``. 
