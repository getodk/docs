.. comment
   add an og image like this :og:image: https://docs.getodk.org/_static/img/tutorial-first-form.png

Entity Form Reference
=================================

This page provides a quick reference for how to design :doc:`XLSForm </tutorial-first-form/>` for ODK that use, create, and update Entities.

Creating and Updating Entity Data
---------------------------------

When you are designing your form, you can add extra information to that form that tells ODK how to use that submission data to create or update an entity. There are two places to make changes in your form: the ``survey`` sheet and the ``entities`` sheet.


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

.. comment
   todo!

* attach to form
* choice filters
* different keys
* xpath expressions to get other properties
* getting the id to reference when doing an update


Structure of an Entity
----------------------

.. comment
   todo!

* ID aka uuid, __id, name, etc.
* label
* properties
* some other system properties
