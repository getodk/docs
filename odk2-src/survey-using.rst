.. spelling::
  prepopulated

Using ODK Survey
=======================

.. warning::

  Survey forms are defined in HTML, CSS, and JavaScript that can be edited by your organization. If the interfaces displayed in this guide do not match the form you have on your device, contact an administrator in your organization for further guidance.

.. _survey-using:

.. contents:: :local:

.. _survey-opening-form:

Opening a Form
-----------------------

The home screen of Survey displays a list of all the forms available on the device.

  .. image:: /img/survey-using/survey-home-screen.*
    :alt: Survey Form List
    :class: device-screen-vertical

.. note::

  Not all forms listed on this home screen are intended to be launched directly. Subforms will be listed on this page but are generally intended to be opened from within a parent form.

To open a form tap its name on the list. This will launch the home screen of that particular form. Below we have opened the :menuselection:`Example Form`.

  .. image:: /img/survey-using/survey-example-start.*
    :alt: Survey Example Form
    :class: device-screen-vertical

This screen shows the form name and version. It also shows a full list of saved instances of the form. For more information on viewing and editing these form instances see the section on :ref:`survey-viewing-saved`.

To start a new instance and begin filling in a form, tap the :guilabel:`Create new instance` button.

.. _survey-opening-sub-form:

Opening a Subform
~~~~~~~~~~~~~~~~~~~~~

Unlike their parents, subforms are generally not intended to be opened from the Survey home screen's form list. Instead, subforms are integrated into their parent forms and launched directly as prompts. They integrate seamlessly into their parent forms and do not need to be manually opened. They might be indicated by a :guilabel:`Create new instance` button within a form, or the form may directly launch the subform.

For example, the *Household Member Survey* is a subform of the *Household Survey* in the :ref:`Survey sample app <survey-sample-app>`.

  .. image:: /img/survey-using/survey-household-subform-launch.*
    :alt: Survey Household Subform Launcher
    :class: device-screen-vertical

This screen within the *Household Survey* shows the launcher for the *Household Member Survey* subform. Clicking :guilabel:`Create new instance` will launch the subform.

  .. image:: /img/survey-using/survey-household-member.*
    :alt: Survey Household Member Form
    :class: device-screen-vertical

This is the first page of the *Household Member Survey* subform. It displays the name of the household, **Sample House**, which was collected in its parent *Household Survey* form. After this subform has been filled in, the flow will return to the parent form.

  .. image:: /img/survey-using/survey-household-subform-one.*
    :alt: Survey Household Subform One Entry
    :class: device-screen-vertical

Completing the *Household Member Survey* subform returns us to the same screen we launched from in the *Household Survey*. The instance created by the subform is now displayed. If you tap the :guilabel:`Create new instance` button again, you can create multiple instances.

  .. image:: /img/survey-using/survey-household-subform-two.*
    :alt: Survey Household Subform Two Entry
    :class: device-screen-vertical


.. _survey-saving-instance:

Saving a Form Instance
------------------------

When saving a form instance, you can either mark it as **Finalized** or **Incomplete**.

  - **Finalized** forms indicate that they are completed and that the data should be used and aggregated.
  - **Incomplete** forms indicate that the form has been saved but it is not yet complete. This is useful if you need to stop filling out a form and return to it later, but want to keep your previously collected values.

.. note::

  Marking a form as **Finalized** does not prevent you or another user from modifying it later.

There are three ways to save a form:

  1. Navigate to the end of the form. This screen will show the buttons to save the form as :guilabel:`Finalize` or :guilabel:`Incomplete`, as described above. After choosing one of these options, Survey will return to its home screen.

    .. image:: /img/survey-using/survey-save-end.*
      :alt: Survey Save Screen
      :class: device-screen-vertical

  2. Tap the button with the name of the form in the upper left from any screen in the form. This will open a menu that provides navigation and exit options.

    - To save the form as **Incomplete** choose :menuselection:`Save Change + Exit`
    - To save the form as **Finalized** choose :menuselection:`Finalize Changes + Exit`

    .. image:: /img/survey-using/survey-save-menu.*
      :alt: Survey Save Menu
      :class: device-screen-vertical

  3. Press the Android back button. This is not the :guilabel:`Back` button provided by ODK in the upper right. This is the button to back out of apps. This will launch a menu with the option to :menuselection:`Save Changes` which will save the form as **Incomplete**.

    .. image:: /img/survey-using/survey-save-back.*
      :alt: Survey Save Back Button
      :class: device-screen-vertical

    .. note::

      This menu does not have an option to save a form as **Finalized**.


.. _survey-viewing-saved:

Viewing Saved Form Instances
-----------------------------------------------

A list of previously saved form instances is viewable on the home screen of each form. Open the desired form (instructions in the :ref:`survey-opening-form` guide) to see this list.

  .. warning::

    This list of saved form instances is not limited to those collected on your device. After synchronization this will include all form instances from all devices that have synced with the server. Take care not to edit form instances that you should not be editing.

    To protect against unauthorized edits, see :doc:`data-permission-filters`.

  .. image:: /img/survey-using/survey-instance-list.*
    :alt: Survey Edit Instance
    :class: device-screen-vertical

This list of instances is ordered reverse chronologically by the last save date, with the most recently edited form instance on top and the oldest form instance at the bottom. These instances are marked as either **Finalized** or **Incomplete** (see :ref:`survey-saving-instance` for definitions).

.. _survey-edit-saved:

Editing Saved Form Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To edit a form instance, tap the pencil icon next to the instance in the instance list on the form home screen.

  .. image:: /img/survey-using/survey-instance-list-edit.*
    :alt: Survey Instance List
    :class: device-screen-vertical

This will launch that instance with all collected values prepopulated. When you save this form as either **Finalized** or **Incomplete**, that state will overwrite the previous state of **Finalized** or **Incomplete**. The updated form instance will now be the most recently edited form and appear at the top of the list.

.. _survey-delete-saved:

Deleting Saved Form Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete a form instance, tap the :guilabel:`X` icon next to the instance in the instance list on the form home screen.

  .. image:: /img/survey-using/survey-instance-list-delete.*
    :alt: Survey Delete Instance
    :class: device-screen-vertical

.. _survey-navigating:

Navigating a Form
-----------------------

Forms in Survey are defined in HTML, CSS, and JavaScript. A default look-and-feel, along with an extensive selection of prompt widgets, is provided by the ODK 2 framework, but this can be customized by your organization. This guide assumes you are using the default look-and-feel.

  - To advance to the next prompt in a form, press the :guilabel:`Next` button in the upper right.

      .. image:: /img/survey-using/survey-navigate-forward.*
        :alt: Survey Next Button
        :class: device-screen-vertical

  - To go backward to the previous prompt, press the :guilabel:`Back` button in the upper right.

      .. image:: /img/survey-using/survey-navigate-back.*
        :alt: Survey Back Button
        :class: device-screen-vertical

  - To navigate to a specific prompt, press the button on the upper left with the form name to show the menu. Tap the button labeled :guilabel:`Contents`.

      .. image:: /img/survey-using/survey-navigate-menu.*
        :alt: Survey Menu
        :class: device-screen-vertical

    This will bring up a menu with a full list of fields and their recorded values. Tap the desired field to navigate to it in the form.

      .. image:: /img/survey-using/survey-navigate-menu-list.*
        :alt: Survey Navigation Menu
        :class: device-screen-vertical

Every change you make to the data in the form is written immediately to the database as a **checkpoint** save.

.. _survey-using-syncing:

Syncing Forms and Data
--------------------------

See the instructions in the :ref:`ODK Services user guide <services-using-sync>`.

.. warning::

  If a data table has any checkpoint saves (for example, caused by form crashes), the data table will not be synchronized. Checkpoints must be resolved before sync can proceed. The user must open a form on the problem table and either delete the checkpoint or edit the checkpoint. If editing, after that is complete they must save is as either incomplete or finalized. Once the checkpoints are eliminated, the user can initiate another synchronization, and the data in this table will then be synchronized with the information on the server.

