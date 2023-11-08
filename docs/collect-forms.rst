*****************************
Managing Forms in Collect
*****************************

.. seealso::

  For an overview on forms and form design, see :doc:`form-design-intro`.

.. _loading-forms-into-collect:

Downloading forms from a server
===============================

A :dfn:`blank form` or :dfn:`form definition` is what users of ODK Collect fill out. Blank forms are usually created using :doc:`XLSForm <xlsform>`.

In order to fill out forms, you must first load blank forms into the Collect App. The preferred way of doing this is by automatically matching the forms provided by the server and this is the default when using Central App Users. You can also :doc:`configure Collect <collect-configure>` so that blank forms must be manually selected and downloaded.

If you have connected ODK Collect to a :doc:`server <collect-connect>` and Collect is not configured to automatically download forms from it, you will need to download the forms that you want to use.

Select :guilabel:`Download form` on the app home screen to browse available forms and download them to your device. Select the ones you would like download, and tap :guilabel:`Get Selected`.

.. image:: /img/collect-forms/main-menu-highlight-get-blank-form.*
  :alt: The Main Menu of the Collect app. The option *Download form* has a red arrow pointing to it.
  :class: device-screen-vertical

.. image:: /img/collect-forms/get-blank-form.*
  :alt: The Get Blank Form screen in the Collect app. Several form names are listed, with checkboxes. One form's checkbox is checked. At the bottom are buttons labeled: *Select All*, *Refresh*, and *Get Selected*.
  :class: device-screen-vertical

.. note::

  Before downloading blank forms from your server to Collect, a form has to be uploaded. See :doc:`Form Management in ODK Central <central-forms>`.

.. _editing-saved-forms:

Editing drafts
================

When filling out a form, you can save it as a draft and edit it later.

The :guilabel:`Drafts` list shows all drafts by their name which can include user-provided values from inside the draft. The expression for those names is specified in the :ref:`form definition <instance-name>`. By default, drafts are sorted alphabetically by name. When the sort order is changed, the selected order is maintained the next time that the draft list is opened. You can use the magnifying glass icon to search drafts by name.

Each draft has a colored pill indicating its validation status. Drafts that have missing required questions or values that violate constraints are marked with a red :guilabel:`Errors` pill. Drafts in which all required questions have been filled out and that have no constraint violations have a blue :guilabel:`No errors` pill.

.. image:: /img/collect-forms/main-menu-drafts.*
  :alt: The Main Menu of the Collect app. The button *Drafts* has a red arrow pointing to it.
  :class: device-screen-vertical

.. image:: /img/collect-forms/drafts.*
  :alt: The Drafts screen. Several drafts are listed by name.
  :class: device-screen-vertical

.. _finalizing_drafts:

Finalizing drafts
==================

.. note::

  In Collect versions prior to v2023.3, it was possible to edit finalized forms. If your workflow involves new information that can be discovered at any time, consider configuring Collect to hide the :guilabel:`Finalize` or :guilabel:`Send` button from the form end screen (see the form entry access control section of :ref:`protected settings <admin-settings>`) and using :ref:`bulk finalization <bulk-finalizing-drafts>`.

If your device is online and Collect is configured to automatically send submissions, you can send send a filled form immediately from the form end screen by tapping the :guilabel:`Send` button. If your device is offline or Collect is not configured to automatically send submissions, you will need to mark a draft as finalized before it can be sent. Finalized forms are available from the :guilabel:`Ready to send` screen where they can be viewed or sent. You can finalize a form from the end screen by tapping the :guilabel:`Finalize` button.

.. _bulk-finalizing-drafts:

Bulk finalizing drafts
-----------------------

.. warning::

  Bulk finalization does not work with submission encryption.

If you want to continue adding information to forms up until the moment when they are sent, you will need to save them as drafts. When you're ready to send them, you could then open each draft, navigate to the form end screen, and tap the :guilabel:`Finalize` or :guilabel:`Send` button. However, this would be inconvenient if you have many drafts that are ready to be sent. In that case, you can use the option to finalize all drafts.

Open the *Action Menu* (:menuselection:`⋮`) and select :guilabel:`Finalize all drafts`:

.. image:: /img/collect-forms/drafts-action-menu.*
  :alt: The Drafts screen. Several drafts are listed by name and the action menu is open.
  :class: device-screen-vertical

.. image:: /img/collect-forms/drafts-bulk-finalized.*
  :alt: The Drafts screen. Only one draft is shown and is marked as having validation errors. A message at the bottom of the screen says that 2 drafts were finalized and 1 has errors that must be addressed before finalizing.
  :class: device-screen-vertical

You will first see a confirmation dialog describing that bulk finalization cannot be undone. If you choose to bulk finalize, all drafts without errors will be finalized.

After bulk finalization is complete, you will see a message at the bottom of the screen describing how many drafts were and weren't finalized. Drafts with constraint violations or missing required questions can't be finalized and will remain in the list. Drafts with data recovered after a crash or forced quit also can't be bulk finalized, even if they are marked with :guilabel:`No errors`. You will need to open those drafts, decide whether or not to keep the recovered data, and then finalize them.

Bulk finalization will update any `end` fields in the forms but will not result in any audit log entry.

.. _uploading-forms:

Sending finalized forms
=========================

To use data collected with the Collect app, you will need to get the filled forms off of the devices. The preferred way of doing this is by automatically sending submissions to a server as soon as they are finalized and this is the default when using Central App Users. To send forms, you will first need to :doc:`configure a server <collect-connect>`.

If you are offline or have turned automatic submission off in settings, you will find finalized forms in the :guilabel:`Ready to send` list, displayed by the name that the :ref:`form definition specifies <settings-sheet>`. When there are forms that are ready to send, you will see a blue notification badge on the :guilabel:`Ready to send` button and its title will become bold.

Uploading a filled form from within the Collect app marks that form as `sent`. `Sent` forms remain viewable from the :guilabel:`Sent` list until they are deleted.

.. image:: /img/collect-forms/main-menu-ready-to-send.*
  :alt: The Main Menu of the Collect app. The *Ready to send* button has a red arrow pointing to it.
  :class: device-screen-vertical

.. _uploading-previously-sent-forms:

Sending previously-sent forms
-----------------------------

If you can't find a submission that you expect on your server or need to re-send a submission for other reasons, you can change the view of the :guilabel:`Ready to send` screen to show both sent and unsent forms.

To show sent and unsent forms:
  :menuselection:`⋮ --> Change View --> Show Sent and Unsent Forms`

.. image:: /img/collect-forms/ready-to-send-change-view.*
  :alt: The "Ready to send" screen of the Collect app. The *Change View* option has a red arrow pointing to it.
  :class: device-screen-vertical

.. _deleting-forms:

Deleting Forms
===============

You can delete filled forms in any state (`Draft`, `Finalized`, or `Sent`). Deleting a `Sent` form deletes the form contents but metadata associated with it including the deletion date and the instance name are maintained for display in the :guilabel:`Sent` list.

If your device is not configured to exactly match the forms provided by the server, you can delete `Blank` forms. When Collect is configured to exactly match the forms provided by the server, any previously-downloaded forms that is closed or deleted from the server will automatically be deleted by Collect.

When a blank form is deleted, it is completely removed from the device if it has no filled forms associated with it. However, if there are filled forms that were created with that form definition, it will be hidden from :guilabel:`Start new form` but will still be available on the device so that the remaining filled forms can be opened. Once all the related filled forms are deleted, the form definition and its media files will be permanently deleted as well. 

Select :guilabel:`Delete` from the Collect Main Menu. You can use the :guilabel:`Saved Forms` and :guilabel:`Blank Forms` tabs to toggle between a list of all filled forms in any state and a list of all blank forms.

.. image:: /img/collect-forms/main-menu-delete-form.*
  :alt: The Main Menu of the Collect app. The option *Delete forms* has an arrow pointing to it.
  :class: device-screen-vertical

.. image:: /img/collect-forms/delete-saved-forms.*
  :alt: The Delete Saved Forms screen in the Collect app. There are two available tabs: *Saved Forms* and *Blank Forms*. The *Saved Forms* tab is active. Below that is a list of saved form instances, with checkboxes. There are buttons labeled: *Select All* and *Delete Selected*.
  :class: device-screen-vertical

.. note::

  When sent forms are deleted, they are listed in the :guilabel:`Sent` page, but are grayed out and can't be viewed. This lets you see confirmation of filled forms that have been sent without keeping all of the data on the device.

  .. image:: /img/collect-forms/deleted-forms-in-sent.*
    :alt: The Sent page in Collect app. Three sent forms are listed, and the second and third have been deleted. They are both grayed out and below the form names is the note *Deleted*, along with a date and time.
    :class: device-screen-vertical

.. _managing-forms-without-server:

Managing forms without a server
================================

If you are working entirely offline with a small group of data collectors, you may find it convenient to manage forms by plugging devices into a computer rather than using a server. 

These approaches can also be helpful in case of problems that require troubleshooting.

.. _loading-forms-directly:

Loading Forms directly
------------------------

.. _loading-forms-with-adb:

Loading forms with ``adb``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can load forms directly from a computer to your device's :ref:`Collect directory <collect-directory>` via USB, using :doc:`Android Debug Bridge <collect-adb>`.

.. code-block:: none

  $ adb push path/to/form.xml <collect-directory>/forms/form.xml

.. _loading-forms-from-device-storage:

Loading forms from device storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also download forms to your device via a web browser, and move them to the :file:`forms/` directory, using the device's file manager (:menuselection:`Settings -> Storage & USB -> Explore`).

1. Go to the Settings menu (:guilabel:`⚙`) on your device and find :menuselection:`Storage & USB`. The settings menu may look different on your device.

   .. image:: /img/collect-forms/device-settings-storage.*
     :alt: The Settings menu on an Android Device. The option *Storage and USB* is circled in red.
     :class: device-screen-vertical

2. From the internal storage screen, select :menuselection:`Explore` to open the file manager. The :guilabel:`Explore` option opens a file manager that you can use to move forms into Collect.

   .. image:: /img/collect-forms/device-settings-storage-explore.*
     :alt: The Internal Storage settings menu on an Android device. The option *Explore* is circled in red.
     :class: device-screen-vertical

.. _loading-form-media:

Loading form media
----------------------

If a form :ref:`includes images or other media <media>`, those files have to be loaded to the device along with the form.

Media files must be placed in a folder labeled :file:`{form-name}-media`.

- When using ODK Central, first upload your form definition. Central will then prompt you to :ref:`add media files <central-forms-attachments>` if necessary. The files are downloaded automatically when :ref:`fetching blank forms <loading-forms-into-collect>`.
- If :ref:`loading forms directly to your device <loading-forms-directly>`, the :file:`-media` folder needs to be placed in the :file:`forms` subdirectory of :ref:`your Collect directory <collect-directory>`, alongside the form itself.

.. _pulling-forms-with-briefcase:

Pulling Forms into Briefcase
-----------------------------

:doc:`ODK Briefcase  <briefcase-using>` is a desktop application that can be used to pull filled forms to your local computer. You will first need to :ref:`transfer the filled forms to your computer <pull-from-collect>`. This will not update the state of the form to `Sent`.

.. _delete-forms-adb:

Deleting Forms with ``adb``
-------------------------------

You can also :ref:`delete form instances directly with <deleting-forms-with-adb>` :doc:`Android Debug Bridge <collect-adb>`. They are stored in the :file:`instances` subdirectory of :ref:`your Collect directory <collect-directory>`, with a directory for each instance.