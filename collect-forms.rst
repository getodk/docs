*****************************
Using ODK Collect
*****************************

.. _loading-forms-into-collect:

Loading Blank Forms
====================

A :dfn:`blank form` is a `.xml` file containing a form definition consistent with the `XForm specification <https://opendatakit.github.io/xforms-spec/>`_. Blank forms can be created using `ODK Build <https://build.opendatakit.org/>`_ or :doc:`XLSForm <xlsform>`.

In order to fill out forms with survey participants, you must first load blank forms into the Collect App.

.. _in-app-get-blank-forms:

Loading Forms from ODK Aggregate Server or Google Drive 
------------------------------------------------------------

If you have :ref:`connected ODK Collect to a server <connecting-to-server>` or :ref:`Google Drive <connecting-to-google>`, use :guilabel:`Get blank forms` on the app home screen to browse available forms and download them to your device.

.. note::

  Before downloading blank forms from Aggregate or Google Drive to Collect, those forms have to be uploaded to those locations.

  .. link to Aggregate guide, once there is one

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

.. _fill-blank-forms:

Filling out forms
===================

Once you have at least one form :ref:`loaded into ODK Collect <loading-forms-into-collect>`, you can fill out a form. 

- Select :guilabel:`Fill Blank Form` from the app home screen.
- Select the form you would like to fill out from the form list.
- Typically, you will :gesture:`swipe left` to advance forward through the question, and :gesture:`swipe right` to back up.

  - You can switch from :gesture:`Swipe` navigation to Forward/Backward buttons in :menuselection:`⋮ -> General Settings -> User Interface`
  - The |arrow| icon on the top right corner opens the jump menu. From the jump menu, you can go to any question or go to the beginning/ending of the form.

  .. |arrow| image:: /img/collect-forms/jumpicon.*
             :alt: Opens the jump menu. 

  |           

  .. image:: /img/collect-forms/jumpscreen.*
    :alt: Screen with the arrow icon displayed in ODK Collect on an Android phone. 
    :class: device-screen-vertical
  
  |

  .. image:: /img/collect-forms/jumpmenu.*
    :alt: Jump menu displayed in ODK Collect on an Android phone. 
    :class: device-screen-vertical

  |
    
  .. note::
    Jump menu only shows the questions of a looped group once an actual record is created.   
   
  - Some questions will :ref:`auto-advance <autoadvance-widget>` after being answered.
  - `Required questions <http://xlsform.org/#required>`_ will not allow you to advance unless answered.

- To **remove a response**, :gesture:`Long Press` on the :term:`question label`. 


For a (mostly) complete guide to form question appearance, see :doc:`form-widgets`.

.. _completing-form:

Completing a Form
-------------------

Once you have reached the end of a form, you will have the opportunity to *Save* and *Exit* the form. At this point, you may also:

.. _name-form-instance:

Name the form
~~~~~~~~~~~~~~~

The last form screen provides a default name for the form (defined by the form designer). You can rename it. This name only applies to that particular instance of a completed form (not to the blank form).

The Form Name identifies the form in lists throughout the app. For this reason, a meaningful name may be important to you. After you've saved the name, the form automatically moves to the :guilabel:`Send Finalized Form` section, from where you can send it.

.. _finalize-form:

Mark the form as *Finalized*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only :formstate:`Finalized` forms can be :ref:`uploaded to a server <uploading-forms>`. 

.. _editing-saved-forms:

Editing *Saved* forms
----------------------

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

If you are connected to :ref:`an ODK Aggregate server <connecting-to-aggregate>` or :ref:`Google Drive Account <connecting-to-google>`, use :guilabel:`Send Finalized Forms` to upload :formstate:`Finalized` form instances. 

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

.. _collect_menus:

Collect Menus, Settings and Security
=====================================

.. _main-menu:

Main Menu
-------------

ODK Collect's main menu contains the following options:

.. image:: /img/collect-settings/main-menu.*
  :alt: Main menu of ODK Collect
  :class: device-screen-vertical

- :menuselection:`Fill Blank Form` allows you to fill any blank form already there in your data collection.
- :menuselection:`Edit Saved Form` looks for forms you've saved, lists them and allows you to edit them.
- :menuselection:`Send Finalized Form` lists all the finalized forms and gives you an option to send them.
- :menuselection:`View Sent Form` displays the forms that have been sent even if they were deleted.
- :menuselection:`Get Blank form` lists all available ODK :term:`Collect` :term:`form` :term:`widget` (question types). The details about which are available on :ref:`basic-form-widgets`.
- :menuselection:`Delete Saved Form` lists all the Saved and Blank Forms and allows you to delete them.

.. _general-settings:

General Settings
--------------------

General Settings are accessible from the :guilabel:`⋮` menu on the top-right corner. 

.. image:: /img/collect-settings/general-settings.*
  :alt: General settings
  :class: device-screen-vertical

It allows us to configure the following:

.. _server-settings:

Server Settings
~~~~~~~~~~~~~~~~~

.. image:: /img/collect-settings/server-settings.*
  :alt: Server settings
  :class: device-screen-vertical

:menuselection:`Server` settings manage the connection to an ODK Aggregate server or Google Drive account for form management.

See :ref:`connecting-to-server` for more details.

.. _interface-settings:

User Interface Settings
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-settings/ui-settings.*
  :alt: User Interface settings
  :class: device-screen-vertical

:menuselection:`User Interface` settings allow us to customize the way our app looks and behaves. It includes settings for:

- :guilabel:`Language` - Allows us to select the device language from 49 available options.
- :guilabel:`Text font size` - Lets us select the font-size.
- :guilabel:`Navigation` (Swiping or Buttons) - Allows us to select the navigation method(swipes, buttons or both).
- :guilabel:`Splash Screen` - An image to display when the Collect application loads.

:menuselection:`User Interface` settings page also consists of the Mapping Settings. 

.. _mapping-settings:

.. rubric:: Mapping

Map settings are included on the :menuselection:`User Interface` settings page.

- :guilabel:`Mapping SDK` sets the app used for :ref:`geopoint`, :ref:`geoshape`, and :ref:`geotrace` :doc:`form-widgets`. Options are Google Maps (default) and OpenStreetMap.
- :guilabel:`Basemap` sets the specific map used when opening the mapping app. 

.. _form-management-settings:

Form Management Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-settings/form-management.png
  :alt: Form Management settings
  :class: device-screen-vertical
  
.. image:: /img/collect-settings/form-management2.png
  :alt: Form Management settings
  :class: device-screen-vertical


:menuselection:`Form Management` settings handle default behavior when editing, finalizing, and importing forms.

.. rubric:: Form submission

- :guilabel:`Auto send` When enabled, forms are sent immediately when finalized if the device can connect to the internet. You can specify whether to send over WiFi, cellular data, or both.
- :guilabel:`Delete after send` When checked, form instances are deleted once they are sent.

.. rubric:: Form filling

- :guilabel:`Default to finalized` When enabled, forms are automatically finalized upon reaching the end of the form. You can opt out of finalizing any form when completing it.
- :guilabel:`Constraint processing` used to select when response constraints are validated: After each swipe, or at finalization.
- :guilabel:`High res video` enables or disables high-resolution video recordings if supported by the video application used.
- :guilabel:`Image size` (v1.11.0+) specifies the maximum number of pixels for the long edge of all images added to forms. Images are scaled down immediately after being added. This setting can be overridden at the form question level. There are five size options available:

  - :guilabel:`Original size from camera (default)`: images are unchanged when added to a form. Used when images must contain a lot of detail or when the internet connection used to send submissions is fast.
  - :guilabel:`Very small (640px)`: used when images don't need to be detailed and the internet connection used to send submissions is slow.
  - :guilabel:`Small (1024px)`: sufficiently detailed for most on-screen viewing but too small for printing.
  - :guilabel:`Medium (2048px)`: sufficiently detailed for most uses including printing.
  - :guilabel:`Large (3072px)`: used when a lot of detail is needed.

.. rubric:: Form import

- :guilabel:`Import saved forms as finalized` When enabled, forms added directly to the :file:`instances/` directory are automatically set to :formstate:`Finalized`.

.. _id-settings:

User and Device Identity Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-settings/und-settings.*
  :alt: User and Device Identity Settings
  :class: device-screen-vertical

.. _form-metadata-settings:

Form Metadata Settings
""""""""""""""""""""""""

:menuselection:`User and Device Identity -> Form Metadata` sets identity values which are added to the metadata of forms completed on the device.

.. image:: /img/collect-settings/form-metadata.*
  :alt: Form Metadata Settings
  :class: device-screen-vertical

.. rubric:: User-defined

You can edit the following:

- Username
- Phone number
- Email address

.. note::

  - If no username is set in Form metadata settings, server username in :ref:`Server settings <server-settings>` is used by default in the form.
  - If username is defined in Form metadata settings as well as in Server settings, username from Form metadata would be visible in form.
  - If you want to ensure that form metadata username can't be changed, you can use the :ref:`admin settings <admin-settings>`.

.. rubric:: Device-defined

You cannot edit these:

- Device ID
- Subscriber ID
- SIM serial number

.. _usage-data-setting:

.. rubric:: Usage data

When enabled, ODK Collect sends usage and error data back to the ODK development team, which helps us improve the application.

Usage data is anonymized.

.. _admin-settings:

Admin Settings
-----------------

.. note::
  Admin settings can be **password protected**. If you set an :guilabel:`Admin Password` in the Admin settings screen, you will need to re-enter that password to access Admin settings in the future.

.. image:: /img/collect-settings/admin-settings.*
  :alt: Admin settings menu
  :class: device-screen-vertical
.. _admin-security:

Admin Security
~~~~~~~~~~~~~~~~

Admin settings allow you to :ref:`restrict which General Settings are seen by users <user-access-control-settings>`. To access those settings as an Admin (and see all of them), :gesture:`tap` :guilabel:`General Settings` from the Admin settings page.

.. _import-export-settings:

Import/Export settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

When you click on the :guilabel:`Import/Export Settings`, you see a QR Code and a few options. 

.. image:: /img/collect-settings/import-settings.*
  :alt: Import/export settings menu of ODK Collect
  :class: device-screen-vertical

QR Code
""""""""

QR Code or the Quick Response Code is a two dimensional barcode. QR codes can be used to configure Collect on many devices. The QR image presented contains all of your current General and Admin settings, including admin and server passwords. When this QR code is scanned from the ODK Collect app on another device, these settings are imported.

Sharing QR code
""""""""""""""""

You can click on the |share| icon to share the QR code as an image. When you click on it, it displays a list of applications and services like *whatsapp*, *facebook*, *hangouts*, *bluetooth*, *MMS* to name a few, which can be used to share the QR code. This is useful when there are several different data collection sites and all devices have to be configured in the same way, in which case the QR code can be shared from one reference device. 

.. |share| image:: /img/collect-settings/share-icon.*
             :alt: Share icon for sharing the QR code. 
             :height: 43 px
             :width: 43 px

.. warning:: 
  Since the QR code may contain the admin and server passwords without encryption, you should be careful about how you share it. It is advised to not send it through an external application but through *bluetooth*, *MMS* or any other such service that doesn't allow the third party to access the data. 

Saving QR code locally
""""""""""""""""""""""""

You can go to :menuselection:`⋮ --> Save settings to disk` to save the QR code.  

Importing settings from a QR saved on your device
"""""""""""""""""""""""""""""""""""""""""""""""""""""

You can import settings from a QR code saved on your device by clicking on :guilabel:`Select Code from SD Card` option.

Making your own QR code
""""""""""""""""""""""""""

QR code is a JSON object with a structure as shown below:

.. code-block:: JSON

  {
    "general": {
      "protocol": "google_sheets",
      "constraint_behavior": "on_finalize"
    },
    "admin": {
      "edit_saved": false
    }
  }

The JSON object isn't encrypted but is compressed using `zlib <http://www.zlib.net/manual.html>`_ before encoding into QRCode. Therefore the creation process can be summarized as follows:

1) Write a JSON object containing the changed settings with a structure as shown above. 
2) Compress it using zlib.
3) Encode into QR code. 

After you finish generating the QR code, you can transfer it to your device and then import it by clicking on :guilabel:`Select Code from SD Card`  option.

List of keys for all settings
""""""""""""""""""""""""""""""

Following is the list of keys for all settings and the set of values they can take:

.. code-block:: javascript

  {
    "admin" : { 

      // Stores the admin password 
      "admin_password": Boolean,
      "admin_pw": String,
   
      // User access control to the main menu. The default value is true. 
      "edit_saved": Boolean,
      "send_finalized": Boolean,
      "view_sent": Boolean,
      "get_blank": Boolean,
      "delete_saved": Boolean,
   
      // User access control to form entry
      "save_mid": Boolean,
      "jump_to": Boolean,
      "change_language": Boolean,
      "access_settings": Boolean,
      "save_as": Boolean,
      "mark_as_finalized": Boolean,
   
      // User access control settings for General settings
      "change_autosend": Boolean,
      "change_navigation": Boolean,
      "change_constraint_behavior": Boolean,
      "change_font_size": Boolean,
      "change_app_language": Boolean,
      "instance_form_sync": Boolean,
      "default_to_finalized": Boolean,
      "delete_after_send": Boolean,
      "high_resolution": Boolean,
      "image_size": Boolean,
      "show_splash_screen": Boolean,
      "show_map_sdk": Boolean,
      "show_map_basemap": Boolean,
      "analytics" : Boolean,
      "change_form_metadata": Boolean,
      "change_server": Boolean,

      // Server
      "import_settings": Boolean,
      "change_server": Boolean,
      "change_protocol_settings": Boolean,

      },

    "general" : {

      // Server settings
      "protocol": {"odk_default", "google_sheets", "other"},
      // Aggregate specific key
      "server_url": String,
      // Google sheets specific keys
      "selected_google_account": String,
      "google_sheets_url": String,
      "username": String,
      "password": String,
      // Other specific keys
      "formlist_url": String,
      "submission_url": String,
      
      // User interface
      "app_language": { "en", "af", "am", "ar", "bn", "ca", "cs", "de", "es", "km", 
           "et", "fa", "fi", "fr", "ha", "hi", "hu", "in", "it", "ja", "ka", "zu",
           "lt", "mg", "mr", "my", "ml", "nb", "nl", "no", "pl", "ps", "pt", "ro",
           "ru", "so","sq", "sw", "ta", "ti", "tl", "tr", "uk", "ur", "vi", "zh"
           },
      "font_size": {13, 17, 21, 25, 29},
      "navigation": {"swipe" ,"buttons" ,"swipe_buttons"},
      "showSplash": Boolean,
      "splashPath": String, // If showSplash is true, then you specify the path of image here.
      "map_sdk_behavior": {"google_maps", "osmdroid"},
      // if map_sdk_behavior is google_maps, then map_basemap_behavior can take the following values:
      "map_basemap_behavior": {"streets", "satellite", "terrain", "hybrid"},
      // if map_sdk_behavior is osmdroid, then map_basemap_behavior can take the following values:
      "map_basemap_behavior": { "openmap_streets", "openmap_usgs_topo", 
                                "openmap_usgs_sat", "openmap_stamen_terrain",
                                "openmap_cartodb_positron", "openmap_cartodb_darkmatter"
                            },
      
      // Form submission
      "delete_send": Boolean,
      "autosend": Boolean,
      "autosend_wifi": Boolean,
      "autosend_network": Boolean,
      
      // Form filling
      "constraint_behavior": {"on_swipe", "on_finalize"},
      "default_to_finalized": Boolean,
      "high_resolution": Boolean,
      "image_size": {"original", "small", "very_small", "medium", "large"},

      // Form import
      "instance_sync": Boolean,

      // User and Device identity
      "form_metadata": String,
      "metadata_migrated": Boolean,
      "metadata_username": String,
      "metadata_phonenumber": String,
      "metadata_email": String,
      "analytics": Boolean, // Anonymous usage data
                  
    },

  }

.. note::
  The subkeys in the general key can be a part of the admin key too. 

.. note::
  QR code only contains settings whose values are not the default values because of the constraints on the amount of data a QR code can hold.

.. warning:: 
  The QR code used for settings-import contains the admin and server passwords *in plain text*. To remove them from the code, :gesture:`tap` the warning on the QR code screen.

.. _user-access-control-settings:

User Access Control Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section allows the admin to hide menu items and settings from the user. It contains the following options:

- :guilabel:`Main Menu Settings` : Allows admin to hide some of the main-menu options from the users.
- :guilabel:`User Settings` : Allows admin to select the options that'll be visible to the users in the :guilabel:`General settings` menu.
- :guilabel:`Form Entry Settings` : Admin can configure the `form entry items` visible to the users. For example unchecking the :guilabel:`change language` option will prevent the user from changing the device language.
