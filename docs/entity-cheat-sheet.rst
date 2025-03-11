.. spelling:word-list::
    hh
    num

.. comment
   add an og image like this :og:image: https://docs.getodk.org/_static/img/tutorial-first-form.png

Entity Cheat Sheet
=================================

This page provides a quick reference for how to design forms in :doc:`XLSForm </tutorial-first-form/>` for ODK that use, create, and update Entities.

Creating and Updating Entity Data
---------------------------------

When you are designing your form, you can specify how transform submissions into entities. (Learn more about entities :doc:`here </entities-intro/>`.)

To make a form that creates or updates entities, there are two places to make changes in your form: the ``survey`` sheet and the ``entities`` sheet.


Survey Sheet
____________

* Add a ``save_to`` column. 
  
  * We recommend putting the ``save_to`` column to the right of the ``required`` column (instead of at the end) so it is easier to see.

* For each field you want to save to an entity, fill out the corresponding entity *property name* in this column. 
  
  * The property name can be different from the field name.
  * Not every field needs to be saved to a property. Only fill out the fields you need for your entity workflow.


.. note::
   Entity property names follow the same naming rules as form field names. Additionally, the property names ``name``, ``label``, and anything beginning with ``__`` (two underscores) are not allowed. 


.. list-table:: Example ``survey`` sheet with ``save_to`` column filled in with property names for certain fields 
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
     - ...
     - ``save_to``
   * - geopoint
     - location
     - Tree Location
     - ...
     - location
   * - text
     - species
     - Tree Species
     - ...
     - species
   * - text
     - intake_notes
     - Intake Notes
     - ...
     - 

Entities Sheet
______________

The ``entities`` sheet is included in the XLSForm template, but you can add it yourself if your form does not have one. The required column headers include ``list_name`` and ``label`` but there are several optional column headers depending on your desired functionality.


* Under ``list_name``, write the name of your entity list.

* Under ``label``, write how to build a label for each entity.
  
  * We recommend using :doc:`concat </form-logic/>` with fields from your form.
  * The label can be blank if the form updates the entity but does not change the label.

.. list-table:: Minimal ``entities`` sheet for creating an entity
   :widths: 50 50
   :header-rows: 1

   * - ``list_name``
     - ``label``
   * - trees
     - concat("Tree: ", ${species})

* **Optional** 

  * Column header ``create_if`` with a boolean expression.
  * Column header ``update_if`` with a boolean expression.
  * Column header ``entity_id`` with the ID of an existing entity to update.

    * Use ``coalesce(${existing_item},uuid())`` if designing a form that both creates and updates entities. 



.. list-table:: Example ``entities`` sheet for conditionally creating an entity
   :widths: 30 40 30
   :header-rows: 1

   * - ``list_name``
     - ``label``
     - ``create_if``
   * - trees
     - concat("Tree: ", ${species})
     - ${tree_cm} > 20

.. list-table:: Example ``entities`` sheet for conditionally updating an entity
   :widths: 20 30 30 20
   :header-rows: 1

   * - ``list_name``
     - ``label``
     - ``update_if``
     - ``entity_id``
   * - orders
     - concat("Approved: ", ${existing_order})
     - ${status} = 'approved'
     - ${existing_order}

.. list-table:: Example ``entities`` sheet for creating and updating entities in the same form
   :widths: 10 15 25 25 25
   :header-rows: 1

   * - ``list_name``
     - ``label``
     - ``create_if``
     - ``update_if``
     - ``entity_id``
   * - trees
     - concat("Tree:", ${species})
     - ${create_or_update} = 'create'
     - ${create_or_update} = 'update'
     - coalesce(${existing_item}, uuid())

.. note::
   Current limitation: Only one entity list can be updated per form and each submission can only create or update a single entity.


Using Entity Data
-----------------

Entity lists are used just like CSV attachments. You can use multiple entity lists in a single form. There are two main ways to attach an entity list where **listname** is the name of your entity list:

#. Use ``select_one_from_file listname.csv`` or ``select_multiple_from_file listname.csv`` 

   * The **.csv** extension after **listname** is necessary.

#. Use ``csv-external`` with ``listname``

.. note::
  When you upload your form to Central, it will check the expected attachments and automatically connect an entity list in place of an attachment when the name matches exactly. You can check what entity lists your forms are using by looking at those forms' attachments on Central.


Selecting an Entity
______________________________

When you use ``select_one_from_file listname.csv``, this form field you write in the ``name`` column will hold the ID of your selected entity. This ID is the UUID that Central uses to uniquely track the entity, e.g. ``4d6a1fe1-6dff-4f72-b122-1413fe9b2dd0``. You might notice UUIDs like this in your submission data.

.. list-table:: Example ``survey`` sheet for selecting an entity with ``select_one_from_file``.
   :widths: 40 30 30
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
   * - select_one_from_file households.csv
     - hh_id
     - Select household


Looking up an Entity from an External CSV
______________________________________

Another way to choose an entity from a list is by another key. Note that the ``calculate`` to get the ``name`` (also referred to as Entity ID or UUID) is only required if you need to update the entity. 

.. list-table:: Example of selecting a household by a barcode ID.
   :widths: 40 20 10 30
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
     - ``calculation``
   * - csv-external
     - households
     - 
     - 
   * - barcode
     - barcode
     - Scan household barcode
     -
   * - calculate
     - hh_id
     - 
     - instance("households")/root/item[id=${barcode}]/name



Updating a Selected Entity
__________________________

This UUID is the ID that Central needs when updating the entity.

.. list-table:: Example ``entities`` sheet for updating a selected entity.
   :widths: 40 30 30
   :header-rows: 1

   * - ``list_name``
     - ``label``
     - ``entity_id``
   * - households
     - 
     - ${hh_id}



Accessing Entity Data
_____________________


Once an entity has been selected, you can use that entity ID to access the properties of that entity. You can also access the ``__version`` system property of an entity to know how many updates have been made. 

.. list-table:: Example 
   :widths: 30 30 10 30
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
     - ``calculation``
   * - calculate
     - num_members
     - 
     - instance("households")/root/item[name=${hh_id}]/num_members




Pre-filling With Default Values
_______________________________

Note that if you want to use the existing value as a default, you will need to use a ``trigger`` to update the value when the entity is selected.

.. list-table:: Example 
   :widths: 10 10 10 10 10 10
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
     - ``save_to``
     - ``trigger``
     - ``calculation``
   * - integer
     - num_members
     - Enter number of household members
     - num_members
     - ${hh_id}
     - instance("households")/root/item[name=${hh_id}]/num_members



Using a Different Key
_____________________

If your entities have a different important key, you can use the ``parameters`` column to specify a different entity property as the key. This is useful when you are *not* updating the entity in the form, and just using the entity list to manage shared data.

.. list-table:: Example 
   :widths: 10 20 20 10 20
   :header-rows: 1

   * - ``type``
     - ``name``
     - ``label``
     - ...
     - ``parameters``
   * - select_one_from_file states.csv
     - state
     - Select state
     - ...
     - value=state_id



Structure of an Entity
----------------------

Entity ID
_________

Every entity has an ID (a UUID) that is unique across all entity lists and projects within Central. 

In a form, this entity ID is accessed through the ``name`` property. This is to fit in with existing CSV attachments and choice lists in which the ``name`` column represents a unique identifier for that row.

In an export and in OData, the entity ID appears under the ``__id`` column.


Label
_____

Every entity has a label (a non-empty string) that is shown in forms the same way labels for choice lists and CSV attachments are shown.


Properties
__________

Beyond the ID and Label, the properties of your entity are up to you. Note that ``name`` and the prefix ``__`` cannot be used as property names.

Every value is stored as a string.

We recommend storing the minimal amount of data necessary to drive your workflow. 


System Properties
_________________

Every entity has a ``__version`` number available. Additional system properties such as ``__createdAt``, ``__updatedAt``, ``_createdBy`` are also available on the entity export and in OData.
