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

If you have :doc:`connected ODK Collect to a server  <collect-connect>` or :doc:`Google Drive  <collect-connect-google>`:

1. Select :guilabel:`Get blank forms` on the app home screen to browse available forms and download them to your device.

   .. image:: /img/collect-forms/main-menu-highlight-get-blank-form.* 
     :alt: The Main Menu of the Collect app. The option *Get Blank Form* is circled in red.
     

  
2. Find and download forms.

   - If you are using ODK Aggregate, you will see a list of available forms. Select the ones you would like download, and tap :guilabel:`Get Selected`.

   
     .. image:: /img/collect-forms/get-blank-form.* 
       :alt: The Get Blank Form screen in the Collect app. Several form names are listed, with checkboxes. One form's checkbox is checked. At the bottom are buttons labeled: *Select All*, *Refresh*, and *Get Selected*.

       
    .. note::
        
      Before downloading blank forms from Aggregate to Collect, a form has to be uploaded. See :ref:`Form Management in ODK Aggregate <form-manage>`.
  
   - If you are using Google Drive, the **Get Blank Form** screen will display the folders in your Google Drive account and any XML documents. Select and download the forms you want.

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

.. _loading-forms-with-adb:

Loading forms with ``adb``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can load forms directly from a computer to your device via USB, using :doc:`Android Debug Bridge <collect-adb>`.

.. code-block:: none

  $ adb push path/to/form.xml /sdcard/odk/forms/form.xml

Loading forms from device storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
You can also download forms to your device via a web browser, and move them to the :file:`odk/forms/` directory, using the device's file manager (:menuselection:`Settings -> Storage & USB -> Explore`).

1. Go to the Settings menu (:guilabel:`⚙`) on your device and find :menuselection:`Storage & USB`

   .. figure:: /img/collect-forms/device-settings-storage.* 
     :alt: The Settings menu on an Android Device. The option *Storage and USB* is circled in red.
  
     The settings menu may look different on your device.

2. From the internal storage screen, select :menuselection:`Explore` to open the file manager.
     
   .. figure:: /img/collect-forms/device-settings-storage-explore.* 
     :alt: The Internal Storage settings menu on an Android device. The option *Explore* is circled in red.
  
     The :guilabel:`Explore` option opens a file manager that you can use to move forms into Collect.

Loading form media
----------------------

If a form :ref:`includes images or other media <image-options>`, those files have to be loaded to the device along with the form.

Media files should be placed in a folder labeled :file:`{form-name}-media`. 

- When using ODK Aggregate, the form upload prompt includes instructions to upload the :file:`-media` folder. The files are downloaded automatically when :ref:`fetching forms from Aggregate <in-app-get-blank-forms>`.
- When using Google Drive, the :file:`-media` folder should be uploaded to the same location as the form.
- If :ref:`loading forms directly to your device <loading-forms-directly>`, the :file:`-media` folder needs to be placed in the :file:`sdcard/odk/forms` directory, alongside the form itself.


.. _editing-saved-forms:

Editing :formstate:`Saved` forms
===================================

:formstate:`Completed` (filled-in) :term:`form instances <instance>` can be edited after they have been saved.

1. Select :guilabel:`Edit Saved Form`

   .. image:: /img/collect-forms/main-menu-edit-saved.* 
     :alt: The Main Menu of the Collect app. The option *Edit Saved Menu* is circled in red.

2. Select a form by name

   .. image:: /img/collect-forms/edit-saved-form.* 
     :alt: The Edit Saved Form screen. Several completed forms are listed by name.

This will reopen the form instance, which you are then free to edit. Form instances are listed by name, which is one reason it can be helpful to :ref:`name the form instance after filling it out <name-form-instance>`.

.. note:: 

  - :formstate:`Sent` forms will not appear in the :guilabel:`Edit Saved Forms` list.

  - :formstate:`Sent` forms, will be available for viewing in :guilabel:`View Sent Forms` list, along with the details which cannot be edited.

  - You may freely edit :formstate:`Saved` and :formstate:`Finalized` forms. 

.. _uploading-forms:

Uploading Finalized Forms
===========================

Eventually, you will want to upload completed form instances for analysis and data aggregation. 

Doing this from within the Collect app marks the forms as :formstate:`sent`. :formstate:`Sent` forms are no longer editable, but they remain viewable until they are deleted. 

Uploading to Aggregate or Google Drive
----------------------------------------

If you are connected to :doc:`an ODK Aggregate server  <collect-connect-aggregate>` or :doc:`Google Drive Account  <collect-connect-google>`, use :guilabel:`Send Finalized Forms` to upload :formstate:`Finalized` form instances. 

.. image:: /img/collect-forms/main-menu-send-finalized.* 
  :alt: The Main Menu of the Collect app. The *Send Finalized Form* option is circled in red.

.. note::

  Blank values in the form are sent to google sheets as cells with a space and not as empty cells. When you are testing for empty cells, you might not get the correct results. To make sure you get the correct results, you could:

  - Use the `TRIM <https://support.google.com/docs/answer/3094140?hl=en>`_ function in the google sheets to remove the leading and trailing spaces from the cells.
  - Define empty cell in your tests to be a cell that is either empty or contains a single space.


Pulling forms with Briefcase
-------------------------------

For local form management, use :doc:`ODK Briefcase <briefcase-forms>` to pull :formstate:`Finalized` form instances to your local computer.


Pulling forms with ``adb``
----------------------------

You can copy form instances from the device using :command:`adb pull`, however this will not update the state of the form to :formstate:`Sent`.

.. _deleting-forms:

Deleting Forms
===============

You can delete :formstate:`Saved`, :formstate:`Finalized`, :formstate:`Sent`, and :formstate:`Blank` forms.

1. Select :guilabel:`Delete Saved Form` on the app home screen. 

   .. image:: /img/collect-forms/main-menu-delete-form.* 
     :alt: The Main Menu of the Collect app. The option *Delete Saved Forms* is circled in red.

2. Select the :guilabel:`Saved Forms` or :guilabel:`Blank Forms` tab.

   .. figure:: /img/collect-forms/delete-saved-forms.* 
     :alt: The Delete Saved Forms screen in the Collect app. There are two available tabs: *Saved Forms* and *Blank Forms*. The *Saved Forms* tab is active. Below that is a list of saved form instances, with checkboxes. There are buttons labeled: *Select All* and *Delete Selected*.
     
     The :guilabel:`Saved Forms` tab lists form instances that are :formstate:`saved`, :formstate:`finalized`, or :formstate:`sent`. 
     
   .. figure:: /img/collect-forms/delete-saved-forms-blank-forms.* 
     :alt: The Delete Saved Forms screen in the Collect app. There are two available tabs: *Saved Forms* and *Blank Forms*. The *Blank Forms* tab is active. Below that is a list of blank forms, with checkboxes. There are buttons labeled: *Select All* and *Delete Selected*.
     
     The :guilabel:`Blank Forms` tab lists :formstate:`blank` forms.
  
.. note:: 

  Deleted Forms are listed in the :guilabel:`View Sent Forms` page, but cannot be viewed. They are indicated with the crossed-out eye icon.

  .. image:: /img/collect-forms/deleted-form-in-view-sent-form.* 
    :alt: The View Sent Forms page in Collect app. Two sent forms are listed, but the second one, *Hypertension Screening* has been deleted. Next to the form name is an icon of an eye, crossed out. Below the form name is the note *Deleted*, along with a date and time.   
  
.. _delete-forms-adb:
      
Deleting Forms with ``adb``
-------------------------------

You can also :ref:`delete form instances directly with <deleting-forms-with-adb>` :doc:`Android Debug Bridge <collect-adb>`. They are stored in :file:`sdcard/odk/instances`, with a directory for each instance. 
