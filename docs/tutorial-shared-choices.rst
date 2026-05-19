Tutorial: share choices between forms
======================================

If you have a project with multiple forms, you probably have select questions shared between them. For example, you may have multiple forms in which a village, a plant species or a supervisor needs to be selected. All of these examples involve choices that are mostly stable over time but can still have occasional changes: a village name may change for political reasons, a new plant species may be discovered, or a supervisor may leave the project.

If you represent this kind of list as a choice list in a form or a CSV attachment, any change will need to be carefully made across all relevant forms.

Entity Lists solve this problem by letting you share Entities between forms.

In this tutorial, you will:

* Convert existing choice lists to Entity Lists
* Configure select questions to use choices from Entity Lists
* Add Entities directly in Central and with forms

We recommend working in a Central project for tests and tutorials. You could create a new project just for this tutorial or combine test forms in one big project.

Example scenario: program sites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's say that you run a multi-site program. You may have forms to:

* Register new participants
* Take attendance at events
* Provide services
* etc.

One of the first questions in all of these forms would involve selecting a site:

.. image:: /img/tutorial-shared-choices/site-selection.gif
  :class: device-screen-vertical

Here are some minimal forms you can try yourself:

*
*
*

We recommend uploading them to your test project in Central and publishing them. You can also create an App User that has access to each form to try them in Collect.

Let's say that a new site gets added. With the way these forms are structured, you would need to update all three of them! Instead, we are going to extract the lists out of the forms and replace them with a shared Entity List.

Create a new Entity List
~~~~~~~~~~~~~~~~~~~~~~~~~

Open any one of the forms for editing in your spreadsheet software. Start by copying the ``name`` and ``label`` columns from the ``choices`` sheet into a new spreadsheet document.

Then, rename the ``name`` column to ``code``. We need to do this because Entities get a default system ID made available as ``name``. In this case we also want our own codes for sites so we'll keep the column but rename it. Save this file as ``sites.csv``.

In Central, navigate to your project, go to the :guilabel:`Entity List` tab, and click on the :guilabel:`New` button. Name your new Entity List ``sites``.

.. image:: /img/tutorial-shared-choices/tutorials-project.png

Once you have created the list, you will need to tell Central the properties that each Entity in the ``sites`` list should have. Go to the :guilabel:`Properties` tab, click the :guilabel:`New` button, and add a ``code`` property. Every Entity must have a ``label`` so you don't need to explicitly add it.

You are now ready to upload the CSV you built earlier. Go back to the :guilabel:`Entities` tab and click on the :guilabel:`Upload Entities` button. After you upload the Entities, you should see your 15 sites.

Use the ``sites`` Entity List in a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are now ready to update each of your forms to use the Entity List rather than the internal choice lists.

For each form definition:

* Delete the ``sites`` choice list to avoid a conflict with the Entity List name.
* Change ``select_one sites`` to ``select_one_from_file sites.csv``.
* Add ``value=code`` to the ``parameters`` column. This will save the site code to submissions rather that the site system ID.

  .. note::
    Each site needs to have a unique code or you won't be able to know which one was selected. As the project designer, you are responsible for making sure they're unique, for example by manually checking for duplicates. Central does NOT currently enforce uniqueness for any column other than the system ID.
* Create a new draft in Central.
* In the Attachments section, click the "Link Entity List sites" button in the ``sites.csv`` row.

  .. image:: /img/tutorial-shared-choices/link-entity-list.png

* Publish the draft.

Your form now 
  
Add a site from Central
~~~~~~~~~~~~~~~~~~~~~~~

The power of a shared Entity List becomes visible when changes need to be made.

Let's say that you need to add a new site called "Tinotenda Primary School." You can now make this addition once in the shared Entity List: 

#. From your project, go to the :guilabel:`Entity Lists` tab and click into the ``sites`` list.
#. Click the :guilabel:`New Entity` button.
#. In the field for Entity Label, enter "Tinotenda Primary School".
#. In the field for code, enter "TIN"

   .. image:: /img/tutorial-shared-choices/new-entity.png

.. note::
    Remember that you are responsible for ensuring site code uniqueness.
 
Create a form to add sites
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Making changes to an Entity List in Central is convenient but it requires being granted full access to a project through the Central frontend which is not always appropriate. Another downside is that it does no validation on values that have been entered.

To provide a more structured way to add Entities which can be made available to anyone who can access a form, not just Central administrators, you can create an Entity creation form:

#. Make a copy of :ref:`the XLSForm template <xlsform-template>`, name the file ``Add site``, and open it in spreadsheet software of your choice.
#. On the ``settings`` sheet, set the form title to ``Add site`` and the form id to ``add_site``.
#. On the ``survey`` sheet, add required text questions for the label (``site_label``) and the code (``site_code``).

   .. image:: /img/tutorial-shared-choices/simple-site-add.png

This small form is enough to capture information about new sites but it doesn't yet give us a way to make that data available to our other forms. To do this, we'll need to update the form so it creates new Entities in the ``sites`` Entity List:

#. On the ``entities`` sheet, put ``sites`` in the ``list_name`` column and ``${site_label}`` in the ``label`` column. This tells ODK to use submissions to the form to create new Entities in the ``sites`` Entity List using the ``site_label`` field's value as the Entity label.
#. On the ``survey`` sheet, add a ``save_to`` column to the right of the ``required`` column.
#. In the ``save_to`` column for the ``site_code`` field, write ``code``. This tells ODK to save the value of the ``site_code`` field to the ``code`` property of the Entity created.

A big advantage of using forms to create or update Entities rather than editing them directly in Central is that you can use form logic to validate new inputs. For sites, it's important for codes to be 3 characters and unique so we can add a constraint for this:

#. Start by connecting the ``sites`` list to the form. At the bottom of the form, in the ``type`` column, put ``csv-external``, in the ``name`` column, put ``sites``.
#. Count the Entities in the ``sites`` list with the code entered in ``site_code``. 
   
   #. In the ``type`` column, put ``calculate``. 
   #. In the ``name`` column, put ``matching_code``.
   #. In the ``calculation`` column, put ``count(instance('sites')/root/item[code=${site_code}]/label)``.
#. Then update the ``constraint`` expression for the ``site_code`` field:
   ``string-length(.) = 3 and ${matching_code} = 0``
#. Add a ``constraint_message``: "Code must be unique and 3 characters long."

.. image:: /img/tutorial-shared-choices/site-add-constraint.png

.. note::

    The duplicate check only includes sites that were already registered the last time that the form got an online update. There is no protection against two data collectors adding the same site while both offline. You can train data collectors to dramatically reduce the likelihood of this happening. For example, you can tell them to only add a site they are physically at and to make sure to look for other staff members. You could also ask them to always update their forms before adding a new site.

To test Entity creation, you will need to first publish it in the project with the ``sites`` Entity List. In Central, create a new form, upload your XLSForm, and publish it. You can then give an App User access to it or try the web form.

.. video:: /vid/tutorial-shared-choices/add-site-collect.mp4

In Collect, any new site added will be immediately available to other forms, even when offline. This makes it very important that there is enough coordination between field staff to avoid duplicates! You can also introduce a server-side review step before new sites are available for other forms (see :ref:`central-entities-settings <Central Entities Settings>`).

Add sites in an existing form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want data collectors to be able to quickly add new sites without interrupting their primary action, you can add the option to create a new site directly in an existing form.

For example, start from the "Register participant" form. Add a group around the site selection and ``text`` questions for ``new_label`` and ``new_code`` in that group. The text questions should only be relevant if no existing site has been selected.

The rest of the logic is the same as in the "Add site" form above, including the ``save_to`` column for the ``new_code`` field. Your ``survey`` sheet should look like:

.. image:: /img/tutorial-shared-choices/participant-open-select.png

On the ``entities`` sheet, indicate that an Entity only needs to be created if no existing site was selected:

.. image:: /img/tutorial-shared-choices/participant-open-select-entities.png

Site selection now behaves like an open select: new values can be dynamically added to the choice list instead of selecting an existing option. This is very similar to adding an "Add site" form like we did above. Which you pick 

Your turn
~~~~~~~~~
* Require submission review before new sites are created.

* Add a ``capacity`` property to sites to keep track of how many people each site can accomodate. Fill in ``capacity`` values for existing sites using the Central interface. Extend the "Add site" form so that a capacity can be specified. Update the "Take attendance" form so that the number of attendees is capped by the site capacity. 

* Expand on the "Add site" form so that it can also be used to change a site label. It should not be possible to change existing site codes. You'll need to learn how to write forms to create or update Entities (see :ref:`quick reference <entities-quick-update>`). After giving it a try, see `an example approach <https://docs.google.com/spreadsheets/d/1hh5RQjN_4-A4cH-Lo2MYEviTxUDEei4d0v2nCp01dek>`_.