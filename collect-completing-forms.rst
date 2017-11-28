Filling out Forms with Collect
================================

ODK Collect is used by :term:`enumerators <enumerator>` to complete survey :doc:`forms <form-design-intro>` with :term:`participants <participant>`.

.. admonition:: Before you get started...

  Before you can fill out a form, you need to :ref:`load at least one form into Collect <loading-forms-into-collect>`.
  
  
Select :guilabel:`Fill Blank Form` from the Main Menu
----------------------------------------------------------

.. image:: /img/collect-completing-forms/main-menu-fill-blank-form.* 
  :alt: The Main Menu of the Collect app. The first menu option, *Fill Blank Form*, is circled in red.

Select a form to fill out from the form list
------------------------------------------------

.. image:: /img/collect-completing-forms/fill-blank-forms.* 
  :alt: The Fill Blank Form menu in the Collect app. Several form titles are listed: *All widgets*, *Demo Survey*, *Form Design Tips by Nafundi*, *Hypertension Screening*, *Sample XLSForm*.

  
Answering questions
-----------------------

.. rubric:: Free response

Free-entry text and number answers are entered using the device keyboard. The appropriate keyboard (letters or numbers) opens when the question appears.

.. raw:: html

  <video controls muted style="max-width:100%">
    <source src="/collect-completing-forms/keyboard-popup.mp4">
  </video>

.. rubric:: Select response

Questions with response choices can be answered by touching the selected items. These include radio buttons (single-select), dropdowns (single-select), check boxes (multi-select), and images choices (single and multi-select).

.. figure:: /img/collect-completing-forms/single-select.* 
  :alt: A question screen with radio buttons (single-select).

  Radio buttons accept one selection.
  

.. figure:: /img/collect-completing-forms/multi-select.gif 
  :alt: A question screen with check boxes (multi-select).
  
  Check boxes accept multiple answers.
  
.. figure:: /img/collect-completing-forms/select-image.* 
  :alt: A question screen with image choices.
  
  Select images by touching them.

.. rubric:: Capture answer from device

Many question formats launch additional features, form widgets, or apps to collect an answer. This includes audio and video recording, signature collection, photo capture, date and time widgets, geolocation widgets, and barcodes. 

In all cases, buttons below the question text will guide you through providing the response.

.. image:: /img/collect-completing-forms/image-widget.* 
  :alt:
  
.. image:: /img/collect-completing-forms/signature-widget.* 
  :alt:
  
.. image:: /img/collect-completing-forms/video-widget.* 
  :alt:
  
.. image:: /img/collect-completing-forms/geopoint-widget.* 
  :alt:
  
.. seealso::

  For a (mostly) complete guide to form question appearance, see :doc:`form-widgets`.


Removing answers
~~~~~~~~~~~~~~~~~~~

To **remove a response**, :gesture:`Long Press` on the :term:`question label`. 

.. image:: /img/collect-completing-forms/long-press-to-remove.gif 
  :alt: To remove an answer to a question, long press the question label and follow the on-screen prompts. 

  
Navigating the form 
------------------------

Swipe
~~~~~~~~~~

To move between questions, :gesture:`Swipe Left or Right`. 

.. image:: /img/collect-completing-forms/swiping.* 
  :alt: A question screen in the Collect App. Overlaid on the screen is an icon of a hand with extended finger and arrows pointing left and right, representing a swiping gesture.


.. raw:: html

  <video controls muted style="max-width:100%">
    <source src="/collect-completing-forms/swipe-example.mp4">
  </video>

Left and Right Buttons  
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer Forward and Back buttons for navigation, you can switch to that in :menuselection:`⋮ -> General Settings -> User Interface`.

.. image:: /img/collect-completing-forms/question-screen-highlight-kebab.* 
  :alt: A question screen in the Collect app. The Action Menu ("kebab") in the top-right corner is circled in red.
  
.. image:: /img/collect-completing-forms/question-screen-highlight-general-settings.* 
  :alt: A question screen in the Collect app. The Action Menu is expanded and the option *General Settings* is circled in red.
  
.. image:: /img/collect-completing-forms/general-settings-highlight-user-interface.* 
  :alt: The General Settings menu of the Collect app. The *User Interface* item is circled in red.
  
.. image:: /img/collect-completing-forms/user-interface-highlight-navigation.* 
  :alt: The User Interface menu of the Collect app. The *Navigation* item is circled in red.
  
.. image:: /img/collect-completing-forms/ui-navigation-buttons.* 
  :alt: The User Interface menu of the Collect app, as displayed in the previous image. There is now a modal titled *Navigation*, with radio buttons (single select) for: *Use horizontal swipes*, *Use forward/back buttons*, and *Use swipes and buttons*. The option for *Use forward/back buttons* is selected and circled in red.
  
.. image:: /img/collect-completing-forms/question-screen-with-buttons.* 
  :alt: A question screen in the Collect App. There are now two buttons below the question text, with left (backwards) and right (forwards) buttons.
 

Jumping to questions
~~~~~~~~~~~~~~~~~~~~~~
  
The arrow icon (|arrow|) in the top right corner opens the jump menu. From the jump menu, you can go to any question or go to the beginning/ending of the form.

.. |arrow| image:: /img/collect-forms/jumpicon.*
             :alt: Opens the jump menu. 

 
.. image:: /img/collect-forms/jumpscreen.*
    :alt: Screen with the arrow icon displayed in ODK Collect on an Android phone. 
    :class: device-screen-vertical
  
.. image:: /img/collect-forms/jumpmenu.*
    :alt: Jump menu displayed in ODK Collect on an Android phone. 
    :class: device-screen-vertical
 
.. note::

  If a form contains questions in a looped group, those questions will only appear in the Jump menu once an actual record is created.
 
Autoadvance Questions
~~~~~~~~~~~~~~~~~~~~~~~~

Some questions will :ref:`auto-advance <autoadvance-widget>` after being answered.

.. raw:: html

  <video controls muted style="max-width:100%">
    <source src="/form-widgets/auto-advance.mp4">
  </video>


Required Questions
~~~~~~~~~~~~~~~~~~~~~~

`Required questions <http://xlsform.org/#required>`_ will not allow you to advance unless answered.

.. image:: /img/form-widgets/trigger-sorry.*
  :alt: A question screen in the Collect app. An error text reads, "Sorry, this response is required."


.. _completing-form:

Completing a Form
-------------------

Once you have reached the end of a form, you will have the opportunity to *Save* and *Exit* the form. 


.. image:: /img/collect-completing-forms/save-and-exit.* 
  :alt: The end of a survey in the Collect app. The headline is *You are at the end of Demo Survey.* Below that is a text field labeled *Name this form*, with the value 'Demo Survey'. Then an unchecked checkbox labeled *Mark form as finalized*. Below all that is a button labeled *Save Form and Exit*.

At this point, you may also:

.. _name-form-instance:

Name the form
~~~~~~~~~~~~~~~

The last form screen provides a default name for the form (defined by the form designer). You can rename it. This name only applies to that particular instance of a completed form (not to the blank form).

.. image:: /img/collect-completing-forms/rename-form.gif 
  :alt: To rename the form instance, touch the form name in the last screen of the survey.
  
The Form Name identifies the form in lists throughout the app. For this reason, a meaningful name may be important to you. After you've saved the name, the form automatically moves to the :guilabel:`Send Finalized Form` section, from where you can send it.

.. _finalize-form:

Mark the form as *Finalized*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-completing-forms/mark-form-as-finalized.* 
  :alt:

Only :formstate:`Finalized` forms can be :ref:`uploaded to a server <uploading-forms>`. 

