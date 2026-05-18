Tutorial: Household survey and follow-up
=========================================

In this tutorial you will build a workflow where:

- newly identified households are registered in the field
- households are revisited up to three times if the household head is unavailable
- households that decline participation are not revisited
- household members with urgent needs can be followed up with immediately

By the end, you will understand:

- how Entities support operational fieldwork
- how Entities track current status over time
- how linked Entities can represent real-world relationships
- how a single submission can create multiple related Entities

.. note::

   This workflow is more complex than a one-time survey because it supports operational fieldwork across multiple visits.

   In exchange for that complexity, field teams can:

   - track household status in real time
   - manage revisit attempts
   - avoid duplicate registration
   - immediately follow up with vulnerable household members

   Projects that only require one-time data collection may not need Entities.

The workflow
-------------

A fieldworker visits a household and records:

- household information
- a roster of household members

Submitting the form will create:

- a household Entity
- multiple household member Entities

.. mermaid::
    :align: center

    flowchart LR
        H[(households)]
        M[(members)]

        H -.- |1 → many | M

Before You Start
----------------

You will need:

- ODK Central v2025.4.4+ with Entities enabled
- ODK Collect v2026.1+
- basic familiarity with :doc:`XLSForm <xlsform>` and :doc:`ODK Entities <entities-intro>`

Step 1: Create the Household Registration Form
----------------------------------------------

Make a copy of :ref:`the XLSForm template <xlsform-template>` in spreadsheet software of your choice. Name the document ``Household registration``.

Add these questions:

.. csv-table::
   :header: type, name, label

   select_one_from_file communities, community, Community
   geopoint, location, Capture location of primary entrance
   text, hh_head, Name of head of household
   text, phone, Best phone number
   integer, members, Including yourself, how many people regularly sleep and eat their meals here?

Next, add a ``repeat`` for household members, noticing the ``repeat_count`` column:

.. csv-table::
   :header: type, name, label, repeat_count

   begin_repeat, member, Household member, ${members}
   text, member_name, Member name
   date, dob, Date of birth
   end_repeat,,

Your form now captures:

- one household
- many household members

This would be enough if your project goal was simply to get information about households that are available when an enumerator first encounters them. However, if it's important to track missed encounters and plan for revisits, we need a way to keep track of household status.

One option would be for data collectors to keep track of missed households in a parallel system like a piece of paper or a notes app. A more structured alternative would be to represent households as Entities that can be created, updated and accessed by forms. That will make it possible for our registration form to also be aware of missed households and encourage their revisit.

.. note:: 
    
    In ODK, Entities represent the *current known state* of a real-world object such as a household, person, farm, or facility. You can think of an Entity List as a spreadsheet with each row being an Entity.

Step 2: Configure the Household Entity
--------------------------------------

Open the ``settings`` sheet and configure the form to create a Household
Entity.

Example:

.. csv-table::
   :header: form_title, form_id, entity_list_name

   Household Registration, household-registration, households

Then configure the household Entity properties:

.. csv-table::
   :header: entity_create?, entity_label, entity_id

   true, ${household_name}, ${household_id}

After submission:

- one Entity will be added to the ``households`` Entity List
- the Entity label will use the household name
- the Entity ID will use the household ID

Step 3: Configure Member Entity Creation
----------------------------------------

Now configure the repeat group so each repeat instance creates a Member
Entity.

Add Entity metadata columns to the repeat questions.

Example:

.. csv-table::
   :header: type, name, label, entities:saveto, entities:create?, entities:id

   text, member_id, Member ID,,true,${member_id}
   text, member_name, Member name,name,,
   integer, age, Age,age,,

.. important::

   Each repeat instance creates one Member Entity.

   If the repeat contains three members, the submission creates three Member
   Entities.

Next, add a property that links each member to its household.

Add a hidden field outside the repeat:

.. csv-table::
   :header: type, name, calculation

   calculate, household_ref, ${household_id}

Then save that value into each Member Entity:

.. csv-table::
   :header: type, name, label, entities:saveto

   calculate, household_ref,,household_id

This creates a parent-child relationship between:

- Household Entities
- Member Entities

Step 4: Upload the Form
-----------------------

Upload the form to your project in ODK Central.

After upload, open the ``Entities`` page.

You should see two Entity Lists:

- households
- members

At this point both lists are empty.

Step 5: Submit Your First Household
-----------------------------------

Open the form in ODK Collect and submit:

.. code-block:: text

   Household ID: HH-001
   Household name: Garcia Household
   Village: North District

Add two household members:

.. code-block:: text

   Member 1
   --------
   Member ID: M-001
   Member name: Ana Garcia
   Age: 34

   Member 2
   --------
   Member ID: M-002
   Member name: Luis Garcia
   Age: 12

Send the finalized form to Central.

Step 6: Inspect the Created Entities
------------------------------------

Open the ``households`` Entity List.

You should see:

.. code-block:: text

   HH-001 | Garcia Household

Now open the ``members`` Entity List.

You should see:

.. code-block:: text

   M-001 | Ana Garcia
   M-002 | Luis Garcia

Inspect one of the Member Entities.

It should include a property linking it to the household:

.. code-block:: text

   household_id = HH-001

.. mermaid::

   flowchart LR

      A[(HH-001)]
      --> B[(M-001)]

      A --> C[(M-002)]

.. note::

   The single form submission created three linked Entities:

   - 1 Household Entity
   - 2 Member Entities

Step 7: Update Existing Entities
--------------------------------

Now create a follow-up form that updates household information.

Add a select question that chooses an existing household Entity:

.. csv-table::
   :header: type, name, label

   select_one_from_file households, household, Select household

Add a question for an updated phone number:

.. csv-table::
   :header: type, name, label

   text, phone, Phone number

Configure the form to update the selected Entity.

After submission, the Household Entity will contain the latest phone number.

.. important::

   Form submissions remain historical records.

   Entities store the latest known state.

What You Learned
----------------

In this tutorial you learned how to:

- create multiple Entities from one submission
- use repeat groups to generate Entities
- create links between Entities
- model household/member relationships
- update Entities over time

Next Steps
----------

You can extend this pattern to support:

- longitudinal health visits
- agricultural monitoring
- census operations
- school enrollment tracking
- case management workflows