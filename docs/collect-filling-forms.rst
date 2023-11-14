Filling out Forms with Collect
================================

ODK Collect is used by :term:`enumerators <enumerator>` to complete survey :doc:`forms <form-design-intro>` with :term:`participants <participant>`.

.. admonition:: Before you get started...

  Before you can fill out a form, you need to :ref:`load at least one form into Collect <loading-forms-into-collect>`.
  
Select :guilabel:`Start new form` from the Main Menu. You will see a list of blank forms available on the device. Tap one to open it and start filling it out.

.. image:: /img/collect-filling-forms/main-menu-start-new-form.*
  :alt: The Main Menu of the Collect app. The first button, *Start new form*, has a red arrow pointing to it.
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/start-new-form.*
  :alt: The "Start new form" menu in the Collect app. Several form titles are listed.
  :class: device-screen-vertical
  
Answering questions
-----------------------

Free response
~~~~~~~~~~~~~~~

Free-entry text and number answers are entered using the device keyboard. The appropriate keyboard (letters or numbers) opens when the question appears.

.. video:: /vid/collect-filling-forms/keyboard-popup.mp4

  Video showing text keyboard popup when a string input is required and number keyboard popup when a number input is required.

Select response
~~~~~~~~~~~~~~~~~

Questions with response choices can be answered by touching the selected items. These include radio buttons (single-select), dropdowns (single-select), check boxes (multi-select), and image choices (single and multi-select).

.. figure:: /img/collect-filling-forms/single-select.* 
  :alt: A question screen with radio buttons (single-select).
  :class: device-screen-vertical

  Radio buttons accept one selection.
  
.. figure:: /img/collect-filling-forms/multi-select.*
  :alt: A question screen with check boxes (multi-select).
  :class: device-screen-vertical side-by-side

  Check boxes accept multiple answers.
  
.. figure:: /img/collect-filling-forms/select-image.* 
  :alt: A question screen with image choices.
  :class: device-screen-vertical


Capture answer from device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many question formats launch additional features, form widgets, or apps to collect an answer. This includes audio and video recording, signature collection, photo capture, date and time widgets, location widgets, and barcodes. 

In all cases, buttons below the question text will guide you through providing the response.

.. image:: /img/collect-filling-forms/image-widget.* 
  :alt:
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/signature-widget.* 
  :alt:
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/video-widget.* 
  :alt:
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/geopoint-widget.* 
  :alt:
  :class: device-screen-vertical
  
.. seealso::

  For a (mostly) complete guide to form question appearance, see :doc:`form-question-types`.

.. _removing_answers:

Removing answers
-------------------

To remove a response, long press on the :term:`question label`. 

.. image:: /img/collect-filling-forms/long-press-to-remove.*
  :alt: To remove an answer to a question, long press the question label and follow the on-screen prompts.
  :class: device-screen-vertical

.. _adding_repeats:

Adding instances of repeats
---------------------------

If you have a repeating group, you can add new instances of that repeat in the following ways:

1. By :ref:`navigating <navigating>` into an empty repeat, or to the next question at the very end of the repeat, you will automatically be prompted to add a new instance of that repeat.

2. By clicking the "add" button while in a repeat:

.. image:: /img/collect-forms/repeat-inline-add.*
    :alt: The "add" button displayed in form entry
    :class: device-screen-vertical

3. By clicking the "add" button in the :ref:`jump menu <jumping>`:

.. image:: /img/collect-forms/jump-button-add.*
    :alt: The "add" button displayed in the jump menu.
    :class: device-screen-vertical

.. _removing_repeats:

Removing instances of repeats
-----------------------------

If you have a repeating group, you can remove existing instances of that repeat in the following ways:

1. By long pressing on the :term:`question label` in the same way as for :ref:`removing answers <removing_answers>`

2. By clicking the "remove" button in the :ref:`jump menu <jumping>`:

.. image:: /img/collect-forms/jump-button-remove.*
    :alt: The "remove" button displayed on an Android phone.
    :class: device-screen-vertical

.. _navigating:

Navigating the form 
------------------------

.. note::
  Since Collect v1.29, both swiping and button navigation are enabled by default on new installations. Prior to Collect v1.29 or for existing installations, only swiping was enabled by default.

Swipe
~~~~~~~~~~

To move between questions, Swipe Left or Right. 

.. image:: /img/collect-filling-forms/swiping.* 
  :alt: A question screen in the Collect App. Overlaid on the screen is an icon of a hand with extended finger and arrows pointing left and right, representing a swiping gesture.
  :class: device-screen-vertical

Next and Back Buttons  
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer Next and Back buttons for navigation, you can change your navigation mode in :menuselection:`⋮ -> Project settings -> User Interface`.

1. Open the *Action Menu* (:menuselection:`⋮`)

   .. image:: /img/collect-filling-forms/question-screen-highlight-kebab.* 
     :alt: A question screen in the Collect app. The Action Menu ("kebab") in the top-right corner is circled in red.
     :class: device-screen-vertical

2. Select :menuselection:`Project settings`.

   .. image:: /img/collect-filling-forms/question-screen-highlight-general-settings.* 
     :alt: A question screen in the Collect app. The Action Menu is expanded and the option *General Settings* is circled in red.
     :class: device-screen-vertical

3. Select :menuselection:`User Interface`

   .. image:: /img/collect-filling-forms/general-settings-highlight-user-interface.* 
     :alt: The General Settings menu of the Collect app. The *User Interface* item is circled in red.
     :class: device-screen-vertical
  
4. Select :menuselection:`Navigation`

   .. image:: /img/collect-filling-forms/user-interface-highlight-navigation.* 
     :alt: The User Interface menu of the Collect app. The *Navigation* item is circled in red.
     :class: device-screen-vertical

5. Update your form navigation preference  

   .. image:: /img/collect-filling-forms/ui-navigation-buttons.* 
     :alt: The User Interface menu of the Collect app, as displayed in the previous image. There is now a modal titled *Navigation*, with radio buttons (single select) for: *Use horizontal swipes*, *Use forward/back buttons*, and *Use swipes and buttons*. The option for *Use forward/back buttons* is selected and circled in red.
     :class: device-screen-vertical
  
.. image:: /img/collect-filling-forms/question-screen-with-buttons.* 
  :alt: A question screen in the Collect App. There are now two buttons below the question text, with left (backwards) and right (forwards) buttons.
  :class: device-screen-vertical

.. _jumping:

Jumping to questions
~~~~~~~~~~~~~~~~~~~~~~
  
The arrow icon (|arrow|) in the top right corner opens the jump menu. From the jump menu, you can go to any question or go to the beginning/ending of the form.

.. |arrow| image:: /img/collect-forms/jumpicon.*
    :alt: Opens the jump menu.
    :scale: 25%
    :class: icon-inline

.. image:: /img/collect-forms/jumpscreen.*
    :alt: Screen with the arrow icon displayed in ODK Collect on an Android phone.
    :class: device-screen-vertical

.. image:: /img/collect-forms/jumpmenu.*
    :alt: Jump menu displayed in ODK Collect on an Android phone.
    :class: device-screen-vertical

If you're inside of a group of questions, you can navigate "up" in the hierarchy using the "go up" button:

.. image:: /img/collect-forms/jump-button-up.*
    :alt: The "go up" button displayed on an Android phone.
    :class: device-screen-vertical

The jump menu also provides shortcuts to :ref:`add <adding_repeats>` or :ref:`remove <removing_repeats>` instances of repeating groups.

.. note::

  If a form contains questions in a repeats, those questions will only appear in the Jump menu once an actual record is created.
 
Autoadvance Questions
~~~~~~~~~~~~~~~~~~~~~~~~

Some questions will :ref:`automatically advance to the next question <autoadvance>` after being answered.

.. video:: /vid/form-widgets/auto-advance.mp4

  Video showing auto-advance after the questions are answered.

Required Questions
~~~~~~~~~~~~~~~~~~~~~~

:ref:`Required questions <requiring-responses>` will not allow you to advance unless answered.

.. image:: /img/form-question-types/trigger-sorry.*
  :alt: A question screen in the Collect app. An error text reads, "Sorry, this response is required."
  :class: device-screen-vertical

.. _change-form-language:  

Changing language of a form
-----------------------------

If a form is available in multiple languages, you can choose a language in which you want the questions to appear. 

Open the *Action Menu* (:menuselection:`⋮`) and select :guilabel:`Change Language`.

.. image:: /img/collect-filling-forms/question-screen-highlight-kebab.* 
  :alt: A question screen in the Collect app. The Action Menu ("kebab") in the top-right corner is circled in red.
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/question-screen-highlight-change-language.* 
  :alt: A question screen in the Collect app. The Action Menu is expanded and the option *Change Language* is circled in red.
  :class: device-screen-vertical

.. note::

  The :guilabel:`Change Language` option is only visible if a form is available in more than one language.  
  
3. Select the language you want the form questions to appear in.

   .. image:: /img/collect-filling-forms/choose-language.* 
     :alt: A modal titled *Change Language*, with radio buttons (single select) for languages: *English* and *French* and a CANCEL button. The option for *English* is selected.
     :class: device-screen-vertical

.. _validate_form:  

Check for errors during form entry
---------------------------------------

As of Collect v2023.2.0, you can check a form for errors (validate it) during the form entry process at any stage.

Open the *Action Menu* (:menuselection:`⋮`) and select :guilabel:`Check for errors`.

.. image:: /img/collect-filling-forms/question-screen-highlight-kebab.* 
  :alt: A question screen in the Collect app. The Action Menu ("kebab") in the top-right corner is circled in red.
  :class: device-screen-vertical

.. image:: /img/collect-filling-forms/question-screen-highlight-check-for-errors.* 
  :alt: A question screen in the Collect app. The Action Menu is expanded and the option *Check for errors* is circled in red.
  :class: device-screen-vertical

In case of any errors, you will be automatically redirected to the first question that contains an error. Otherwise, a snackbar displaying a success message will be shown.

.. _save-partial-filled-form:

Saving a partially filled form
--------------------------------

If you wish to save a partially filled form, you can click on the save icon (|save|) beside the form name.

.. |save| image:: /img/collect-filling-forms/saveicon.*
             :alt: Saves a form. 

 
.. image:: /img/collect-filling-forms/save-partial-filled-form.*
    :alt: Screen with the save icon displayed in ODK Collect on an Android phone. 
    :class: device-screen-vertical
  
To :ref:`edit the saved form <editing-saved-forms>`, select :menuselection:`Edit Saved Form` in the Main Menu and select the form you wish to edit.

.. _completing-form:

The form end screen
-------------------

Forms end with a standard screen that displays the name of the filled form and options to save as draft or indicate that the form is ready to send. The filled form name displayed in the "You are at the end of" message is :ref:`set by the form definition <instance-name>` and uses values from the filled form.


.. image:: /img/collect-filling-forms/save-and-exit.* 
  :alt: The end of a survey in the Collect app. The headline is *You are at the end of Section 55: 212 observations.* Below that is a message describing that forms can't be edited after submission. Then there is a "Save as draft" button and a "Send" button.
  :class: device-screen-vertical

If you tap the :guilabel:`Save as draft` button, the form will be saved and available for more editing from the :guilabel:`Drafts` screen.

The :guilabel:`Send` button will be displayed if finalized forms are :ref:`configured to send automatically <blank-form-update-mode>` and the device is online. If finalized forms are not configured to send automatically or the device is offline, the button label will be :guilabel:`Finalize` instead. Tapping on the :guilabel:`Send` button immediately attempts a submission. Tapping on the :guilabel:`Finalize` button marks the form as `Finalized` which makes it available from the :guilabel:`Ready to send` screen and prevents further editing. If finalized forms are configured to send automatically, it will be sent as soon as a connection becomes available.
