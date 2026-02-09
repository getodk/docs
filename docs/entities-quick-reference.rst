.. spelling:word-list::
    hh
    num


Entity Quick Reference
=======================

This page provides a quick reference for how to design forms in :doc:`XLSForm </tutorial-first-form/>` for ODK that use, create, and update :doc:`Entities </entities-intro/>`.

Creating and Updating Entity Data
---------------------------------

When you are designing your form, you can specify how Entities should be created or updated from submissions.

To make a form that creates or updates Entities, there are two places to make changes in your form: the ``survey`` sheet and the ``entities`` sheet.


Survey Sheet
____________

* Add a ``save_to`` column. 
  
  * We recommend putting the ``save_to`` column to the right of the ``required`` column (instead of at the end) so it is easier to see.

* For each field you want to save to an Entity, fill out the corresponding Entity *property name* in this column.
  
  * The property name can be different from the field name.
  * Not every field needs to be saved to a property. Only make Entity properties for the fields you need in your Entity workflow.


.. note::
   Entity property names follow the same naming rules as form field names. Additionally, the property names ``name``, ``label``, and anything beginning with ``__`` (two underscores) are not allowed. 

.. rubric:: XLSForm: ``survey`` sheet with ``save_to`` column filled in with property names for certain fields

.. csv-table:: survey
  :header: type, name, label, ..., save_to

  geopoint, location, Tree Location, ..., geometry
  text, species, Tree Species, ..., species
  text, intake_notes, Intake Notes, ...,

Entities Sheet
______________

The ``entities`` sheet is included in the `XLSForm template <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_, but you can add it yourself if your form does not have one. The required column headers are ``list_name`` and ``label`` and there are several optional column headers depending on your desired functionality.

* Under ``list_name``, write the name of the Entity List to create or update Entities in

* Under ``label``, write how to build a label for each Entity
  
  * We recommend using :doc:`concat </form-logic/>` with fields from your form.
  * You can use the label to show status information about the Entity, including using emoji like ✅ or ⚪️.
  * The system does not enforce uniqueness of label values but you'll generally want to use values that you guarantee are unique through constraints or other mechanisms.

.. note::
   Currently, the ``entities`` show can only have one row because each submission can only create or update a single Entity.

Create
~~~~~~

.. csv-table:: entities
  :header: list_name, label

  trees, "concat(""Tree: "", ${species})"

Update
~~~~~~

.. csv-table:: entities
  :header: list_name, label, entity_id

  trees, "concat(""Tree: "", ${species})", ${tree}

.. note::

   When updating an Entity, the value in the ``entity_id`` column is required and must be the Entity's system ID. This generally means that you need to attach an Entity List in order to update its Entities. See the :ref:`using Entity data <quick-reference-using-entity-data>` section.

   The label can be blank if the form updates the Entity but does not change the label.

Create or update
~~~~~~~~~~~~~~~~

.. csv-table:: entities
  :header: list_name, label, create_if, update_if, entity_id

  trees, "concat(""Tree: "", ${species})", ${tree} = '', ${tree} != '', "coalesce(${tree}, uuid())"

Conditionally create
~~~~~~~~~~~~~~~~~~~~

.. csv-table:: entities
   :header: list_name, label, create_if

    trees, "concat(""Tree: "", ${species})", ${tree_cm} > 20

Conditionally update
~~~~~~~~~~~~~~~~~~~~

.. csv-table:: entities
   :header: list_name, label, entity_id, update_if

    orders, "Approved: ${existing_order}", ${existing_order}, ${status} = 'approved'

Saving the Entity ID in a Registration Form
___________________________________________

Depending on your workflow, it may be helpful to save the Entity ID (UUID) in the submission data where the Entity is created. 

.. rubric:: XLSForm: Example of saving the ID of a new Entity in the submission.

.. csv-table:: survey
   :header: type, name, calculation

   calculate, new_entity_id, ``/data/meta/entity/@id``

.. _quick-reference-using-entity-data:

Using Entity Data
-----------------

Entity Lists are used just like CSV attachments. You can use multiple Entity Lists in a single form. There are two main ways to attach an Entity List where **listname** is the name of your Entity List:

#. Use ``select_one_from_file listname.csv`` or ``select_multiple_from_file listname.csv`` 

   * The **.csv** extension after **listname** is necessary.

#. Use type :ref:`csv-external <form-datasets-attaching-csv>` with name ``listname`` (no extension)

.. note::
  When you upload your form to Central, it will check the expected attachments and automatically connect an Entity List in place of an attachment when the name matches exactly. You can check what Entity Lists your forms are using by looking at those forms' attachments on Central.

Selecting an Entity
______________________________

When you use ``select_one_from_file listname.csv``, this form field will hold the system ID of your selected Entity. This ID looks like ``4d6a1fe1-6dff-4f72-b122-1413fe9b2dd0`` and is used to uniquely identify your Entity.

.. rubric:: XLSForm: selecting an Entity with ``select_one_from_file``

.. csv-table:: survey
   :header: type, name, label

   select_one_from_file households.csv, hh_id, Select household


Looking up an Entity from an External CSV
__________________________________________

You can also identify a specific Entity using other data entered by the user, for example, a barcode number.

.. rubric:: XLSForm: selecting a household by a barcode ID

.. csv-table:: survey
   :header: type, name, label, calculation

   csv-external, households, ,
   barcode, barcode, Scan household barcode,
   calculate, hh_id, , instance("households")/root/item[hh_id=${barcode}]/name

.. note::
   Every Entity has a ``name`` property which represents its system ID. The ``calculate`` in the example above shows how to access that system ID from another unique value like a barcode number. The system ID is necessary to update the Entity.


Updating a Selected Entity
__________________________

The ID from a ``select_one_from_file`` or the ``name`` property described in the section above is the ID needed to update the Entity.

.. rubric:: XLSForm: updating a selected Entity

.. csv-table:: entities
   :header: list_name, label, entity_id

   household, ,${hh_id}

.. note::
   Note that for the example above, leaving ``label`` blank in this update form means it won't be changed when the Entity is updated.
   An update form is the only scenario in which ``label`` can be left blank.
   This form implicitly updates an Entity because ``entity_id`` is provided and ``create_if`` is not specified.
   Refer to the above  `Entities Sheet`_ section for more information.


Accessing Entity Data
_____________________


Once an Entity has been selected, you can use that Entity ID to access the properties of that Entity. You can also access the ``__version`` system property of an Entity to know how many updates have been made. 

.. rubric:: XLSForm: using the ``instance`` function to look up a property of a selected Entity

.. csv-table:: survey
   :header: type, name, label, calculation

    calculate, num_members, ,instance("households")/root/item[name=${hh_id}]/num_members



Pre-filling With Default Values
_______________________________

Note that if you are using ``select_one_from_file`` and want to use the existing value as a default, you will need to use a ``trigger`` to update the value when the Entity is selected.
This follows the pattern of using `dynamic defaults from form data </form-logic/#dynamic-defaults-from-form-data>`_.

.. rubric:: XLSForm: using dynamic defaults from form data to pre-fill a field with an Entity property

.. csv-table:: survey
   :header: type, name, label, save_to, trigger, calculation

   integer, num_members, Enter number of household members, num_members, ${hh_id}, instance("households")/root/item[name=${hh_id}]/num_members



Using a Different Key
_____________________

If your Entities have a different important property used to uniquely identify them, you can save that property's value when an Entity is selected. Use the ``parameters`` column to specify a different Entity property as the value that will be saved. This is useful when you are *not* updating the Entity in the form, and just using the Entity list to manage shared data.

.. rubric:: XLSForm: saving a different property when selecting an Entity

.. csv-table:: survey
   :header: type, name, label, ..., parameters

   select_one_from_file states.csv, state, Select state, ..., value=state_id

.. note::
   With the example above, you will not be able to use that other key to update the Entity.
   This technique works best for read-only data where you are using an Entity List to manage shared data but not updating any Entity data in your form.

Structure of an Entity
----------------------

Entity ID
_________

Every Entity has an ID (a UUID) that is unique across all Entity Lists and projects within Central. We often refer to this as an Entity's system ID because it's assigned by the system and can't be changed.

In a form, this Entity ID is accessed through the ``name`` property. This is to fit in with existing CSV attachments and choice lists in which the ``name`` column represents a unique identifier for that row.

In an export and in OData, the Entity ID appears under the ``__id`` column.


Label
_____

Every Entity has a *label* (a non-empty string) that is shown in forms the same way labels for choice lists and CSV attachments are shown.


Properties
__________

Beyond the ID and Label, the properties of your Entity are up to you. Note that ``name`` and the prefix ``__`` cannot be used as property names.

Every value is stored as a string.

We recommend storing the minimal amount of data necessary to drive your workflow. 


System Properties
_________________

Every Entity has a ``__version`` number available. Additional system properties such as ``__createdAt``, ``__updatedAt``, ``__createdBy`` are also available on the Entity export and in OData.

Creating or updating multiple Entities
--------------------------------------

Create or update multiple Entities in the same list
---------------------------------------------------

To create or update multiple Entities in the same list, use a ``repeat`` on the ``survey`` sheet of your form definition to capture information about each Entity. All ``save_to`` values must be in the same repeat and your ``label`` and other expressions on the ``entities`` sheet may only reference fields in the ``repeat``. Other than that, your ``entities`` sheet will look exactly the same as with a single Entity create or update.

Create or update Entities in multiple lists
--------------------------------------------

To create or update Entities in multiple lists, add rows to your ``entities`` sheet. Each row must have a unique ``list_name`` value. That is, the only way to create or update multiple Entities in the same list is to use a ``repeat``. On the ``survey`` sheet, you must use the ``list_name`` value followed by a ``#`` as a prefix to your ``save_to`` values. For example, if you would like to write to the ``households`` and ``participants`` lists, all ``save_to`` values for ``households`` must start with ``households#`` and all ``save_to`` values for ``participants`` must start with ``participants#``.