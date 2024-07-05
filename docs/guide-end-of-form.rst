:og:image: https://docs.getodk.org/_static/img/guide-end-of-form.png

Helping data collectors take the right next step after filling a form
=====================================================================

The first step when planning to use ODK is to carefully design the workflow you would like the users of your forms to go through. This includes thinking through what they should do when they reach the end of a form or when they are interrupted and need to exit a form filling session. Should they send immediately? Should they go talk to someone? Should they save a draft?

By default, data collectors using Collect can save a form they're working on as a draft at any time and then come back to it for further editing. When they are done filling out a form, they finalize it so that it can be automatically sent to the server as soon as the device is connected to the Internet.

While these are good defaults for many contexts, some projects benefit from customizing how data collectors can interact with forms in the different states. In this guide, you will learn:

* :ref:`what the Collect form states mean <guide-end-form-states-overview>`
* :ref:`ways to customize how data collectors interact with forms <guide-end-form-customization-options>`
* :ref:`example customizations to meet the needs of common workflows <guide-end-form-common-workflows>`

.. _guide-end-form-states-overview:

Form states in Collect
----------------------------------

Filled forms in ODK Collect can be in one of three states: ``draft``, ``finalized``, or ``sent``. State changes always happen in the same order: a ``draft`` form can only transition to the ``finalized`` state and a ``finalized`` form can only transition to the ``sent`` state.

.. note::
  Prior to Collect v2024.1, ``finalized`` forms could go back to the ``draft`` state. This was removed to better satisfy the goals of the ``finalized`` state described below. If your workflow previously relied on editing finalized forms, you can use this guide, especially the :ref:`section with example workflows <guide-end-form-common-workflows>`, to design an alternative.

Draft
~~~~~~~

Draft forms can be edited at any time and can't be sent until they are finalized. ``Draft`` forms can have errors or not. This determines whether they can be finalized:

* :guilabel:`Errors`: the draft either has violated constraints or missing required questions. It can't be finalized until those errors are addressed.
* :guilabel:`No errors`: the draft can be finalized. If a form definition has no required questions and no constraints, its drafts are always marked as ``no errors``.

Errors are indicated in the :guilabel:`Drafts` list. You can also :ref:`check for errors <validate_form>` at any time while filling a form.

Finalized
~~~~~~~~~~~

Finalized forms are ready to be sent and can't be edited. The ``finalized`` state exists to:

* give data collectors control over when filled forms are queued for submission.
* reduce the risk that data collectors continue editing data after they no longer have access to the data collection subject.
* prevent edits after an important workflow step is completed (for example, supervisor review).
* let Collect do data processing with a guarantee that the data won't change (for example, creating :doc:`Entities <central-entities>`).

The ``finalized`` state is only necessary because Collect allows users to save and work with data offline. If your data collectors are guaranteed to always have connectivity, you can turn on :ref:`Auto send <guide-end-form-auto-send>` so that they never need to see filled forms in the ``finalized`` state.

Sent
~~~~~

Sent forms have been received by the server and can't be edited from Collect. The ``sent`` state exists to:

* let the user see data that they sent.
* enable troubleshooting and data recovery in case of issues with the server.

Collect can also optionally be configured to :ref:`delete submissions after send <delete-after-send>` to reduce device storage needs or ensure greater data protection.

.. _guide-end-form-customization-options:

Customization options
-------------------------

This section describes ways to customize how data collectors interact with the form states described above. These customizations let you limit what data collectors can do when they need to stop filling out a form because they've completed it or for other reasons.

The settings described can be set on a device and then :ref:`shared by QR code to other devices <sharing-settings-with-another-device>`. Alternatively, and especially if different devices need to use different App Users, you can :ref:`create your own QR codes <create-settings-qr-code>`.

To see how these options can be combined to achieve specific goals, see :ref:`the customizations for common workflows section <guide-end-form-common-workflows>`.

.. _guide-end-form-auto-send:

Auto send setting
~~~~~~~~~~~~~~~~~

We generally recommend turning on :guilabel:`auto send` in :ref:`form management settings <form-management-settings>`. When :guilabel:`auto send` is on, Collect attempts to send filled forms as soon as they are finalized. The benefits of :guilabel:`auto send` are:

* reduced risk of data collectors forgetting to send data in a timely way.
* more opportunities to retry sending. This can be very helpful on poor or intermittent Internet connections.
* less for data collectors to think about (and you can also :ref:`hide the Ready to send button <guide-end-form-hide-buttons>`).
* less chance that all data collectors send at the same time (such as the end of their work day) which could lead to network congestion or high load on the server.

One case where you may need to turn :guilabel:`auto send` off is if it's important for data collectors to send data while on a network connection that is higher bandwidth, more secure, or lower-cost. In some cases, changing the setting to ``WiFi only`` or ``Cellular only`` may address these needs.

.. _guide-end-form-hide-buttons:

Hide :guilabel:`Drafts`, :guilabel:`Ready to Send` and/or :guilabel:`Sent` buttons from Main Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect's :ref:`protected access control settings <admin-settings>` allow you to hide certain parts of the user interface that are accessible by default. If you have strict workflow requirements such as only wanting data to be captured when the data collector is physically with the data collection subject, you can hide some or all of the :guilabel:`Drafts`, :guilabel:`Ready to send` and/or :guilabel:`Sent` buttons from the Main Menu. This is accessible from the :guilabel:`Main Menu Settings` section.

Use form design to require workflow steps before finalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before a user can finalize a form, all required questions must be answered and all answered questions must meet constraint conditions. That means you can use required questions or questions with constraints to get your users to take certain actions before finalization.

A simple example would be to ask the user to review the data they have entered and answer a yes or no question about whether they expect further edits will be needed:

.. image:: /img/guide-end-of-form/constraint-draft.* 
  :alt: The Collect app showing a question asking to review entered data. The answer "No" is selected and there is a red message asking to exit the form and save as draft.
  :class: device-screen-vertical

* :fa:`external-link` `Example of a form guiding user to save as draft <https://docs.google.com/spreadsheets/d/1h3UH1sKub2Dhc-SE8iuUk7xHvABKv0OkI_Kn3NpJc6A>`_

You can customize the prompt for your context. For example:

* "Is the patient leaving the clinic now?"
* "Will you still be able to see the trail from your next destination?"
* Suggest using the jump option (|arrow|) to review specific, important sections.

.. |arrow| image:: /img/collect-forms/jumpicon.*
    :alt: Opens the jump menu.
    :scale: 15%
    :class: icon-inline

You can also use :ref:`draft names <instance-name>` to include information about workflow steps that still need to be completed. For example, you could add a prefix to show that a draft is ready for review or has all of the first day's data.

If you use a constraint as in the above example, the user will need to come back into the draft and change their answer to the question before they can send the data.

If your users have many drafts and don't know which ones will need to be edited before submission, you can use a ``note`` without a constraint to recommend that users save as draft.

.. tip::

  In general, ``note`` form fields and ``hint`` text are powerful opportunities to guide users through your intended workflow.

The :ref:`bulk finalization <bulk-finalizing-drafts>` functionality makes it faster to send all error-free drafts once necessary edits have been made.

.. image:: /img/collect-forms/drafts-action-menu.*
  :alt: The Drafts screen. Several drafts are listed by name and the action menu is open.
  :class: device-screen-vertical

Remove :guilabel:`Finalize` / :guilabel:`Send` button from the form end screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases, you may want data collectors to always save as draft. This will allow them to continue to make edits to collected data until a certain point in time such as supervisor approval or departure from a data collection site. You can use the :ref:`protected access control settings <admin-settings>` to hide the :guilabel:`Finalize` / :guilabel:`Send` button from the form end screen.

To eventually send, someone can either show the button, or use the :guilabel:`Finalize all drafts` functionality from the :guilabel:`Drafts` list.

Remove save draft (:fa:`floppy-disk`) while filling a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect's :ref:`protected access control settings <admin-settings>` also contain a :guilabel:`Form Entry Settings` section for hiding actions available from the form filling screen. You can hide the Save (:fa:`floppy-disk`) button from the menu and from the :ref:`form exit dialog <exit-form-filling>`. This will prevent data collectors from saving as draft during a form filling session.

You may still want to allow them to save as draft from the form end screen if, for example, it's appropriate for them to make small edits after all of the initial data is captured.

.. _guide-end-form-hide-save-draft-form-end:

Remove :guilabel:`Save as draft` from the form end screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use :ref:`protected access control settings <admin-settings>` to hide the :guilabel:`Save as draft` button from the form end screen. This can be useful when you want to guarantee that data collectors go all the way to the end of a form and can't edit a completed form. You may also want to hide the :ref:`jump menu <jumping>`.

You can hide the :guilabel:`Save as draft` functionality from the form end screen and leave it in the form filling screen if you want data collectors to be able to interrupt form filling sessions in certain cases but want them to finalize as soon as all required data has been captured.

Remove :guilabel:`Finalize all drafts` from the :guilabel:`Drafts` list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to guarantee that each draft is finalized from the form end screen, you can remove :guilabel:`Finalize all drafts` from the :ref:`protected access control settings <admin-settings>`. For example, if you want data collectors to verify each submission before finalizing it, you may not want them to bulk finalize.

.. _guide-end-form-form-audit-log:

Capture data collector behavior in the form audit log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collect's :doc:`audit logging <form-audit-log>` makes it possible to capture a record of every action that a user took while filling out a form. In particular, the log tracks exiting and entering a form and can optionally :ref:`track changes <form-audit-log-change-tracking>` and capture :ref:`reasons for changes <form-audit-log-reason-for-changes>` on draft edits. Turning on audit logging can be a powerful way to verify that a desired workflow is being followed.

The amount of data captured by audit logging can appear overwhelming but it's not necessary to carefully analyze the logs to get value out of them. First, the very act of communicating to data collectors that their actions are being logged for quality assurance will make data collectors more mindful of how they interact with forms. Additionally, manually looking through the log for specific submissions during training or for submissions with unexpected data can provide valuable insights.

.. _guide-end-form-admin-password:

Set an admin password
~~~~~~~~~~~~~~~~~~~~~

If your data collectors are likely to want to change some of the settings that are important for your project, you can :ref:`specify an admin password <admin-password>` that will be required to view and change protected settings. If you do this, you will generally want to also hide all :guilabel:`User Settings` that are important for your project.

In many cases, the admin password will never need to be used: its purpose is only to lock down settings. In that case, it can be complex and hard to remember. In some cases, it may be necessary for someone in the field such as a supervisor to be able to change settings. In that case, it should be set to something relatively easy to communicate and enter.

.. _guide-end-form-common-workflows:

Customizations for common workflows
------------------------------------

Some questions to ask yourself and your data collectors as you design your workflow are:

* Is it possible for a data collector to reach the end of the form but still have information to fill in?
* What should happen if a data collector is interrupted while filling out a form?
* How capable are data collectors of remembering a workflow?
* How many times will data collectors repeat the same workflow?
* How capable are data collectors of making independent decisions when faced with unexpected situations like an interview being interrupted?
* How trusted and well-trained are data collectors? Are they likely to want to "cheat" in some way to save time and/or effort?
* Will data collectors be in a distracting or stressful environment that could reduce their usual abilities?
* What are the consequences of incorrect data being sent? What are the next steps if that happens and is detected?
* How much workflow support do data collectors want to be included in the form(s) they use?

As you answer these questions, you will get a clearer sense of what needs to happen when data collectors need to exit a form. This section includes some common workflow patterns and how to use the tools outlined above to support them. Many of these ideas can be combined if your workflow has aspects of more than one of these patterns.

No edits allowed after leaving data collection subject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In many workflows, it's important to guarantee that data is not changed after the data collector no longer has access to the data collection subject. For example, a nurse administering a vaccine should generally capture all data about that vaccination encounter while their patient is with them. They should not rely on their memory to fill in details after the encounter. To guarantee that data collectors have to fill out the form in one session:

* Remove :guilabel:`Save as draft` from the form end screen and :fa:`floppy-disk` from the form filling experience and form exit dialog.
* Hide the :guilabel:`Drafts` button from the Main Menu.
* (Generally) Turn on :guilabel:`Auto send`.
* (If data is highly sensitive or devices are not trusted) Turn on :guilabel:`Delete after send`.
* (If data collection must be linear) :ref:`Disable moving backwards <moving-backwards-setting>`.
* (If data collectors may be tempted to change settings) Set an admin password and hide :guilabel:`User Settings` set above.

When data collectors reach the form end screen, they only have the option to :guilabel:`Finalize`. If they are interrupted during a form filling session, they need to exit and discard changes or rely on automatic data backups and recovery (the partially-filled form will open automatically when they open the same blank form again).

.. note::
  If you would like to allow edits but they are generally strongly discouraged, you could leave the option to save as draft from the form filling experience and use :ref:`audit logging <guide-end-form-form-audit-log>` with change tracking and reasons for change to get more information on edits that are made.

Edits are needed to specific, known drafts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Saving as draft and making edits can be an expected and important part of a workflow. For example:

* some specific filled forms may require adding details that were initially unavailable.
* a form may capture data from multiple days.
* tasks like transcribing an audio recording may be needed.

This can generally be addressed in form design by using required questions. You can also use a ``note``, a ``hint``, or a ``required_message`` to prompt users to exit the form and :guilabel:`Save as draft` at known points of the form.

If you have designed your form so that it's only possible to reach the form end screen once all necessary tasks are complete, you may want to :ref:`hide the Save as draft button from the form end screen <guide-end-form-hide-save-draft-form-end>`. It can be easier for data collectors to take the right action if they always use the back button to save as draft and only use the form end screen to finalize/send.

Edits are needed but it's unknown in advance to which drafts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In other workflows, it is not known ahead of time which drafts will be edited. For example:

* a data collection subject may be observable at different times or from different angles, revealing new information.
* self-review to fix small mistakes like typos may be encouraged.

.. warning::
  Although self-review can be a powerful way to catch mistakes, it can also lead to accidental data fabrication. If you are considering this kind of workflow in a context where the data collection subject will no longer be available, consider running an experiment to measure whether allowing later edits improves or harms data quality. You may find it useful to turn on Collect's :ref:`audit logging <guide-end-form-form-audit-log>` and specifically to configure :ref:`change tracking <form-audit-log-change-tracking>`.

To support this need, you can take the :guilabel:`Finalize` / :guilabel:`Send` button off the form end screen and require that data collectors always use :ref:`bulk finalization <bulk-finalizing-drafts>`:

* Remove :guilabel:`Finalize` from the :ref:`form end screen <completing-form>`.
* (If data collectors may be tempted to change settings) Set an admin password.
* (If it's important to be able to block finalization of specific filled forms) Add a required yes or no question asking whether further edits are needed with a constraint that the answer must be ``No``.
* Train data collectors on using :ref:`bulk finalization <bulk-finalizing-drafts>`.

When data collectors reach the :ref:`form end screen <completing-form>`, they only have the option of saving as draft. They can then make edits from the :guilabel:`Drafts` list as needed. 

When they are ready to send multiple drafts, they go to :guilabel:`Drafts` and tap on the :guilabel:`Finalize all drafts` menu item. All forms marked with ``no errors`` are finalized and sent. If there are certain drafts that have ``no errors`` but may not yet be ready to send, data collectors can edit those drafts to cause a validation error and make sure they can't be finalized. This is most convenient to do with a yes or no question asking whether further edits are needed.

Supervisor review required before submission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Having a trusted supervisor do an in-field review of filled in forms before submission can increase data collectors' attention to detail and help catch missing or incorrect data. You can decide when this review happens: it could be the data collector's responsibility to connect with their supervisor at some frequency or the supervisor could be the one who initiates review. This process can be written into the form or communicated separately such as during a training.

You will generally want to design the form so it enforces the review process and require that the supervisor fill out some questions in the form. For example:

* Add a checklist of actions the supervisor needs to take with an option to check each one off.
* Ask the reviewer to type in their name.
* Ask the reviewer to type in a special code which they don't show to data collectors (use the :guilabel:`Delete after send` setting so data collectors can't view the code in sent forms).
* Ask the reviewer to scan a barcode that only they have access to
* Ask the reviewer to add their signature.

.. image:: /img/guide-end-of-form/reviewer-checklist.* 
  :alt: The Collect app showing a list of questions for a reviewer.
  :class: device-screen-vertical

.. image:: /img/guide-end-of-form/reviewer-code.* 
  :alt: The Collect app showing a screen for a reviewer to enter their information and sign off on the submission.
  :class: device-screen-vertical

* :fa:`external-link` `Example of a form requiring review <https://docs.google.com/spreadsheets/d/1o17pQIYtwVnc1vxxJ4EVE-874SaN6N0fQ_FU9wvo6-I>`_

You can :ref:`name drafts <instance-name>` so it is easier to see from the :guilabel:`Drafts` list which drafts are ready for review and which need further editing.

.. image:: /img/guide-end-of-form/reviewer-drafts.* 
  :alt: The Collect app showing the draft list with some drafts marked as "ready for review" and others as "edits needed".
  :class: device-screen-vertical

When a reviewer finishes reviewing a draft, they can immediately finalize it so it can be sent.

Only trusted reviewers can send
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to guarantee that a trusted reviewer sends all forms, you can disable data collectors' access to finalize forms:

* Remove :guilabel:`Finalize` from the form end screen.
* Remove :guilabel:`Finalize all drafts` from the :guilabel:`Drafts` list.
* Set an admin password and communicate it to trusted reviewers.
* (Optional) Hide the :guilabel:`Ready to send` button from the main menu (forms will only be listed there if auto send is off or if the device is offline).

Train data collectors to go to a reviewer periodically. This could be at a set time every day, once a week, after a certain number of drafts are saved, etc. The reviewer can make any edits they want, possibly using special review-related questions as described above. When all draft submissions are ready to send, they:

* Go to protected settings.
* Enter the admin password.
* Change the setting to show the :guilabel:`Finalize all drafts` option.
* Navigate to :guilabel:`Drafts`.
* :guilabel:`Finalize all drafts`.
* Make sure that auto send runs or go to :guilabel:`Ready to send` and send all forms.
* Go to protected settings.
* Enter the admin password.
* Hide the :guilabel:`Finalize all drafts` option.

Next steps
----------

In this guide, you deepened your understanding of the states that filled forms can have in Collect. You then learned some ways to customize how data collectors can interact with filled forms in different states and applied those approaches to specific workflows.

Here are some things to consider doing next:

- Think about the workflows that you use ODK to support. Could any of the approaches described in this guide reduce data collection errors or reduce the need for training?
- If your workflow doesn't quite match any of the ones described above, consider sharing it `on the forum <https://forum.getodk.org/c/support/6>`_. We can discuss how to best support it and consider adding it to this guide.
- Read the reference on :doc:`Collect settings <collect-settings>`.
