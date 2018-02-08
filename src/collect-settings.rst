Collect Menus, Settings, and Security
=====================================


.. _main-menu:

Main Menu
-------------

.. image:: /img/collect-settings/main-menu.*
  :alt: Main menu of ODK Collect
  :class: device-screen-vertical

:menuselection:`Fill Blank Form` 
  Lists available blank forms and
  lets you select a form to begin filling out.
   
:menuselection:`Edit Saved Form` 
  Lists completed and saved forms and
  lets you select a form to edit.
   
:menuselection:`Send Finalized Form` 
  Lists finalized but unsent forms and
  lets you select forms to send to the server.

:menuselection:`View Sent Form` 
  Lists forms that have been sent, even if they were deleted. 
  
:menuselection:`Get Blank form` 
  Lists blank forms available on the server and
  lets you download them.
  
:menuselection:`Delete Saved Form` 
  Lists all the Saved and Blank Forms and
  lets you delete them.

.. _general-settings:

General Settings
--------------------

To access General Settings:
  :menuselection:`⋮ --> General Settings`

.. image:: /img/collect-settings/general-settings.*
  :alt: General settings
  :class: device-screen-vertical

.. _server-settings:

Server Settings
~~~~~~~~~~~~~~~~~

Server settings :doc:`control the connection to <collect-connect>` 
an :doc:`Aggregate <aggregate-intro>` or :doc:`openrosa` server
or a :doc:`Google Drive account <collect-connect-google>`. 

To access Server Settings:  
  :menuselection:`⋮ --> General Settings --> Server` 

  
.. image:: /img/collect-settings/server-settings.*
  :alt: Server settings
  :class: device-screen-vertical

.. seealso:: :doc:`collect-connect`

.. _interface-settings:

User Interface Settings
~~~~~~~~~~~~~~~~~~~~~~~~

User Interface settings control Collect's appearance and behavior. 

To access User Interface settings:
  :menuselection:`⋮ --> General Settings --> User Interface` 

.. image:: /img/collect-settings/ui-settings.*
  :alt: User Interface settings
  :class: device-screen-vertical

:guilabel:`Language` 
  Sets the display language.

:guilabel:`Text font size`
  Sets the display font size.
    
:guilabel:`Navigation` 
  Sets form navigation style for moving between questions.
  
  Options:

  - Horizontal swiping
  - Forward and back buttons
  - Both

:guilabel:`Splash Screen`
  Sets an image to display while Collect loads.

.. _mapping-settings:

.. rubric:: Mapping

:guilabel:`Mapping SDK` 
  Sets the app that will be used for 
  form question types that require map integration.
  
  Options:
  
  - Google Maps (default)
  - OpenStreetMap
 
  .. seealso:: :ref:`geopoint`, :ref:`geoshape`, :ref:`geotrace` 
  
  
:guilabel:`Basemap` 
  Sets the map to be displayed when the mapping app is opened. 

.. _form-management-settings:

Form Management Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Form Management settings control default behavior 
when editing, finalizing, and importing forms.

To access Form Management settings:
  :menuselection:`⋮ --> General Settings --> Form Management` 


.. image:: /img/collect-settings/form-management.png
  :alt: Form Management settings
  :class: device-screen-vertical
  
.. image:: /img/collect-settings/form-management2.png
  :alt: Form Management settings
  :class: device-screen-vertical


.. rubric:: Form submission

:guilabel:`Auto send` 
  When enabled, forms are sent immediately when they are finalized,
  if the device can connect to the internet. 
  You can specify whether to send over WiFi, cellular data, or both.
  
:guilabel:`Delete after send` 
  When enabled, form instances are deleted once they are sent.

.. rubric:: Form filling

:guilabel:`Default to finalized` 
  When enabled, forms are automatically finalized 
  upon reaching the end of the form. 
  You can opt out of this on any specific form during form completion.
  
:guilabel:`Constraint processing` 
  Sets when form responses are validated against constraints_.
  
  Options:
  
  - Upon forward swipe. (That is, right after the question is answered.)
  - At finalization.
  
  .. _constraints: http://xlsform.org/#constraints

:guilabel:`High res video` 
  When enabled, 
  :ref:`video` widgets will record high resolution video
  if possible.  

:guilabel:`Image size` 
  .. versionadded:: 1.11.0
  
  Sets the default maximum size for images added to forms,
  as measured by the number of pixels on the longest edge.
  Images larger than the maximum 
  are scaled down immediately after being added. 
  
  Options:
  
  :guilabel:`Original size from camera (default)`
    Images are unchanged when added to a form. 
    Recommended for use only when images must contain a lot of detail 
    and when the internet connection used to send submissions is fast.
  :guilabel:`Very small (640px)` 
    Recommended when images don't need to be detailed 
    or the internet connection used to send submissions is slow.
  :guilabel:`Small (1024px)`
    Sufficiently detailed for most on-screen viewing 
    but too small for printing.
  :guilabel:`Medium (2048px)`
    Sufficiently detailed for most uses, including printing.
  :guilabel:`Large (3072px)`
    Recommended when a lot of detail is needed,
    but you want to reduce the size of image files
    as much as possible.

.. rubric:: Form import

:guilabel:`Import saved forms as finalized` 
  When enabled, forms added directly to the :file:`instances/` directory
  are automatically set to :formstate:`Finalized`.

.. _id-settings:

User and Device Identity Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User and device identity settings control how 
personally identifiable information and device id
are used.

To access User and device identity settings:
  :menuselection:`⋮ --> General Settings --> User and device identity`   

.. image:: /img/collect-settings/und-settings.*
  :alt: User and Device Identity Settings
  :class: device-screen-vertical

.. _form-metadata-settings:

Form metadata settings
""""""""""""""""""""""""

Form metadata settings control how identifying information
is added to the metadata of forms completed on the device.

To access form metadata settings:
  :menuselection:`⋮ --> General Settings --> User and Device Identity --> Form Metadata`
  

.. image:: /img/collect-settings/form-metadata.*
  :alt: Form Metadata Settings
  :class: device-screen-vertical

.. rubric:: User-defined

You can edit the following:

- Username
- Phone number
- Email address

.. note::

  - If no username is set here, 
    the username from :ref:`Server settings <server-settings>` 
    is used instead.
  - You can restrict editing of the username in 
    :ref:`admin settings <admin-settings>`.

.. rubric:: Device-defined

You cannot edit these:

- Device ID
- Subscriber ID
- SIM serial number

.. _usage-data-setting:

.. rubric:: Usage data

When enabled, ODK Collect sends anonymous usage and error data 
back to the ODK development team, 
which helps us improve the application.

.. _admin-settings:

Admin Settings
-----------------

Admin settings manage other settings and features,
letting you :ref:`import, export`, or :ref:`reset` settings, 
and :ref:`restricting which features are available to users of the app`.

Admin settings are useful when 
you are managing devices that will be used by many enumerators,
and you would like to limit the options available to those enumerators.

You can :ref:`password protect` the Admin setting screen,
so enumerators cannot adjust settings or access restricted features.

To access Admin settings:
  :menuselection:`⋮ --> Admin Settings`


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

.. note::

  Settings are exported and saved so that they can be loaded to other devices. When you save external settings, they are saved to :file:`/sdcard/odk/settings/collect.settings`. You can load external settings from this location to other devices as well.

  At app launch, the settings are loaded from a different location :file:`/sdcard/odk/collect.settings`, which tracks the state of your settings at all times. 

  Settings are saved to and loaded from different locations to avoid deleting the saved settings.

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

.. image:: /img/collect-settings/main-menu-settings.*
  :alt: A list of checked main menu options. The options to be hidden from the main menu can be unchecked. 
  :class: device-screen-vertical

- :guilabel:`User Settings` : Allows admin to select the options that'll be visible to the users in the :guilabel:`General Settings` menu.

.. image:: /img/collect-settings/user-settings.*
  :alt: A list of checked options available in General Settings menu. The options to be hidden from the General Settings menu can be unchecked.
  :class: device-screen-vertical

.. image:: /img/collect-settings/user-settings2.*
  :alt: Remaining options in the User Settings list.
  :class: device-screen-vertical

- :guilabel:`Form Entry Settings` : Admin can configure the `form entry items` visible to the users. For example, unchecking the :guilabel:`Change Language` option will prevent the user from changing the form language.

 .. image:: /img/collect-settings/form-entry-settings.*
   :alt: A list of checked form entry options and a Moving backwards options before the list which is checked. The options to be hidden while filling a form can be unchecked.
   :class: device-screen-vertical

 :guilabel:`Moving backwards` option in the :guilabel:`Form Entry Settings` can be unchecked to prevent the user from navigating backwards while filling a form and changing the response to a previously answered question. 

 When you uncheck this option, a message will be displayed which asks you to configure following settings:

 - Disable :guilabel:`Edit Saved Form` option in the main menu
 - Disable :guilabel:`Save Form` option in the Form entry menu
 - Disable :guilabel:`Go To Prompt` option in the Form entry menu
 - Set :guilabel:`Constraint processing` to validate upon forward swipe in the Form Management settings

 .. image:: /img/collect-settings/moving-backwards-disabled.*
   :alt: Image showing message displayed to configure other settings when Moving backwards option is unchecked.
   :class: device-screen-vertical

 If you choose :guilabel:`YES` as response, these settings will be disabled along with moving backwards and the user will not be able to bypass the moving backwards settings. When using this setting, you will generally want to set an admin password so a user can’t bypass it.

 .. note::

   When you enable the moving backwards option, you have to configure the other changed settings since they are not automatically changed back.

   .. image:: /img/collect-settings/moving-backwards-enabled.*
     :alt: Image showing message displayed to configure other settings when Moving backwards option is re-enabled.
     :class: device-screen-vertical

 If you choose :guilabel:`NO` as response, only the moving backwards option will be disabled and no other settings will be changed. User may be able to bypass the moving backwards settings using the other settings.

