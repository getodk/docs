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

All of the techniques described below apply to :doc:`Entity Lists <central-entities>`. Entity Lists can be thought of as CSVs that are managed by ODK Central so that data collected by one form submission can be automatically accessible in other forms in the same project.

.. note::

  Most mobile devices released in 2019 or later can handle lists of 50,000 or more without slowing down. If you experience Collect slowing down, please share the size of the dataset, the device you are using, and any expressions that reference the dataset on `the community forum <https://forum.getodk.org/c/support/6>`_ or to support@getodk.org.

.. _selects-from-csv:

Building selects from CSV files
---------------------------------

CSV files can be used as datasets for select questions using ``select_one_from_file`` or ``select_multiple_from_file``. CSV files used this way must have ``name`` and ``label`` columns unless you use the ``parameters`` column to :ref:`customize the columns used <customizing-label-and-value>`. For each row in the dataset, the text in the value column (defaults to ``name``) will be used as the value saved when that choice is selected and the text in the label column (defaults to ``label``) will be used to display the choice. For select multiples, ``name`` must not contain spaces.

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

  Polygons and lines are only supported in Collect v2023.1.0 or later.

GeoJSON files that follow `the GeoJSON spec <https://datatracker.ietf.org/doc/html/rfc7946>`_ can be used as datasets that populate select questions using ``select_one_from_file``. Selects from GeoJSON may be styled as maps using the :ref:`map appearance <select-from-map>` but can also use any other :ref:`select appearance <select-appearances>`. In order to be used by a form, a GeoJSON file:

- must have a ``.geojson`` extension (NOT ``.json``)
- must define a single top-level `FeatureCollection <https://datatracker.ietf.org/doc/html/rfc7946#section-3.3>`_
- must include a unique identifier for each feature (by default, a top-level ``id``, falling back to an ``id`` property, or can be :ref:`configured <customizing-label-and-value>`)
- must only include features with `Point <https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.1>`_, `LineString <https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.2>`_ or `Polygon <https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3>`_ types

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

All properties are displayed by :ref:`select from map <select-from-map>` questions and can be :ref:`referenced by any part of the form <referencing-values-in-datasets>`.

A feature's ``geometry`` can be accessed as ``geometry`` and is provided in :ref:`the ODK format <location-widgets>`. Given the GeoJSON file and the form definition above, if the user selected "HR Giger Museum", the value of ``${museum}`` would be ``"fs87b"``. 

The expression ``instance('museums')/root/item[id=${museum}]/geometry`` evaluates to ``46.5841618 7.0801379 0 0`` which is a point in the ODK format.

.. _selects-from-xml:

Building selects from XML files
---------------------------------

XML files can be used as datasets that populate select questions using ``select_one_from_file`` or ``select_multiple_from_file``. This is typically less convenient than :ref:`using CSV files <selects-from-csv>`. However, knowing about the XML representation is helpful for understanding how to look up values in both CSV and XML files.

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

The ``item`` blocks are analogous to rows in the CSV representation. Each ``item`` must have at least ``name`` and ``label`` nested nodes and can have any number of additional nodes. These nodes correspond to columns in the CSV representation.

.. _referencing-values-in-datasets:

Looking up values in datasets
---------------------------------

You can look up values in internal or external datasets. You will generally do this in ``calculate`` fields but you can also look up values directly in ``label``s to show them to users or include looked up values in constraints or other expressions.

Expressions to look up values in datasets always start with ``instance("<instance name>")`` to identify which dataset is being accessed. If you have a choice list named ``places`` or an attached CSV with filename ``places.csv``, your lookup expressions will start with ``instance("places")``.

The next part of the expression is ``/root/item``. This means to consider every single **item** in your choice list or attached file.

You then generally need to have a filter in square brackets to specify which item(s) to actually use. For example, if you have a choice list or attached file named ``states`` and want to look up a value about a state that was entered by the user in a form field called ``my_state``, you would use ``name = ${my_state}`` as your filter expression. This is exactly the same kind of expression you would write as a ``choice_filter``.

Your filter expression can result in one or more items being selected. Filtering to a result that includes multiple items is particularly useful for sums and counts. For example, to count the number of states with a population above a certain threshold:

``count(instance("states")/root/item[population > ${pop_threshold}])``

To use a single value from the item(s) selected, specify which column/property to use after the filter. For example, if you want to look up the population of the state which your user filled in as ``my_state``, your full expression would be:

``instance("states")/root/item[name = ${my_state}]/population``

To get the total population across states with a population above a certain threshold:

``sum(instance("states")/root/item[population > ${pop_threshold}]/population)``

.. note::

  You don't need to deeply understand the detail of these expressions to use them effectively. If you're interested in learning more, see the section on :ref:`XPath paths <xpath-paths>`. In particular, ``/root/item`` comes from the :ref:`XML structure used to represent datasets for selects <selects-from-xml>`. If you attach custom XML files to your form, you may have a different root node name.

.. _form-datasets-attaching-csv:

Attaching CSVs for lookups without a select
---------------------------------------------

If you want to look up a value in a CSV directly without first going through a selection step, you can attach that CSV with ``csv-external``:

.. csv-table:: survey
  :header: type,name,label,calculation

  csv-external,people
  barcode,person_id,Scan person's ID card
  calculate,person_fname,,instance("people")/root/item[code=${person_id}]/fname

The example form above attaches a CSV with filename ``people.csv`` or an :doc:`entity list <central-entities>` named ``people``. It then prompts the user to scan a barcode from an ID card and uses the value from the ID card to look up the corresponding person's first name. If attaching an actual CSV file, it must have columns named ``fname`` and ``code``. Similarly, if using an entity list, that entity list must have properties named ``fname`` and ``code``.

.. note::

  To attach an XML file named ``people.xml`` instead, replace ``csv-external`` above with ``xml-external``.
