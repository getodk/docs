*****************************
Form Management
*****************************

.. seealso::

  For an overview on forms and form design, see :doc:`form-design-intro`.

.. _loading-forms-into-collect:

Loading Blank Forms
====================

A :dfn:`blank form` is a `.xml` file containing a form definition consistent with the `XForm specification <https://opendatakit.github.io/xforms-spec/>`_. Blank forms can be created using `ODK Build <https://build.opendatakit.org/>`_ or :doc:`XLSForm <xlsform>`.

In order to fill out forms with survey participants, you must first load blank forms into the Collect App.

.. _in-app-get-blank-forms:

Loading Forms from ODK Aggregate Server or Google Drive 
------------------------------------------------------------

If you have :doc:`connected ODK Collect to a server  <collect-connect>` or :doc:`Google Drive  <collect-connect-google>`, use :guilabel:`Get blank forms` on the app home screen to browse available forms and download them to your device.

.. image:: /img/collect-forms/main-menu-highlight-get-blank-form.* 
  :alt: The Main Menu of the Collect app. The option *Get Blank Form* is circled in red.

  
.. rubric:: Aggregate

If you are using ODK Aggregate, you will see a list of available forms. Select the ones you would like download, and tap :guilabel:`Get Selected`.

.. image:: /img/collect-forms/get-blank-form.* 
  :alt: The Get Blank Form screen in the Collect app. Several form names are listed, with checkboxes. One form's checkbox is checked. At the bottom are buttons labeled: *Select All*, *Refresh*, and *Get Selected*.

.. note::

  Before downloading blank forms from Aggregate to Collect, a form has to be uploaded. See :ref:`Form Management in ODK Aggregate <form-manage>`.
  
.. rubric:: Google Drive

If you are using Google Drive, the **Get Blank Form** screen will display the folders in your Google Drive account and any XML documents. Select and download the forms you want.

.. image:: /img/collect-forms/get-forms-google.* 
  :alt:


.. warning:: 

  All XML documents in Google Drive will appear in Collect. XML documents will be listed **even if they are not valid XForms**.

  .. image:: /img/collect-forms/get-blank-form-not-a-form.* 
    :alt:

  And you can actually download any XML document, **even if it isn't a real XForm**.

  .. image:: /img/collect-forms/downloading-not-a-form.* 
    :alt:

  But you can't Fill Out a non-form.  

  .. image:: /img/collect-forms/not-form-exception.* 
    :alt:

.. link to Google forms guide, once there is one

.. _loading-forms-directly:

Loading forms directly
------------------------

You can load forms directly from a computer to your device via USB, using :doc:`Android Debug Bridge <collect-adb>`.

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

You can also download forms to your device via a web browser, and move them to the :file:`odk/forms/` directory, using the device's file manager (:menuselection:`Settings -> Storage & USB -> Explore`).

Loading form media
~~~~~~~~~~~~~~~~~~~~~

If a form :ref:`includes images or other media <image-options>`, those files have to be loaded to the device along with the form.

Media files should be placed in a folder labelled :file:`{form-name}-media`. 

- When using ODK Aggregate, the form upload prompt includes instructions to upload the :file:`-media` folder. The files are downloaded automatically when :ref:`fetching forms from Aggregate <in-app-get-blank-forms>`.
- When using Google Drive, the :file:`-media` folder should be uploaded to the same location as the form.
- If :ref:`loading forms directly to your device <loading-forms-directly>`, the :file:`-media` folder needs to be placed in the :file:`sdcard/odk/forms` directory, alongside the form itself.


.. _editing-saved-forms:

Editing *Saved* forms
===========================

- From the app home screen, select :guilabel:`Edit Saved Form`. 
- From the form list, select a form by name.

This will reopen the form, which you are then free to edit.

.. note:: 

  - :formstate:`Sent` forms will not appear in the :guilabel:`Edit Saved Forms` list.

  - :formstate:`Sent` forms, will be available for viewing in :guilabel:`View Sent Forms` list, along with the details which cannot be edited.

  - You may freely edit :formstate:`Saved` and :formstate:`Finalized` forms. 

.. _uploading-forms:

Uploading Finalized Forms
===========================

If you are connected to :doc:`an ODK Aggregate server  <collect-connect-aggregate>` or :doc:`Google Drive Account  <collect-connect-google>`, use :guilabel:`Send Finalized Forms` to upload :formstate:`Finalized` form instances. 

For local form management, use :doc:`ODK Briefcase <briefcase-forms>` to pull :formstate:`Finalized` form instances to your local computer.

:formstate:`Sent` forms are no longer editable, but they remain viewable until they are deleted. 

.. note::

  Blank values in the form are sent to google sheets as cells with a space and not as empty cells. When you are testing for empty cells, you might not get the correct results. To make sure you get the correct results, you could:

  - Use the `TRIM <https://support.google.com/docs/answer/3094140?hl=en>`_ function in the google sheets to remove the leading and trailing spaces from the cells.
  - Define empty cell in your tests to be a cell that is either empty or contains a single space.

.. note:: 

  - You can copy form instances from the device using :command:`adb`, however this will not update the state of the form to :formstate:`Sent`.

.. _deleting-forms:

Deleting Forms
===============

You can delete :formstate:`Saved`, :formstate:`Finalized`, :formstate:`Sent`, and :formstate:`Blank` forms by selecting :guilabel:`Delete Saved Form` on the app home screen. This page contains two tabs, :guilabel:`Saved Forms`, which contains the list of all form instances that are saved, finalized or sent, and :guilabel:`Blank Forms`.

You can also delete form instances directly with :command:`adb`. They are stored in :file:`sdcard/odk/instances`, with a directory for each instance. 

.. note:: 

  - Deleted Forms are listed, but cannot be viewed. They are indicated with the crossed-out eye icon.
