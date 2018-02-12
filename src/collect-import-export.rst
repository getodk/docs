Importing and Exporting Settings
====================================

.. image:: /img/collect-settings/import-settings.*
  :alt: Import/export settings menu of ODK Collect
  :class: device-screen-vertical

QR Code
----------

QR Code or the Quick Response Code is a two dimensional barcode. QR codes can be used to configure Collect on many devices. The QR image presented contains all of your current General and Admin settings, including admin and server passwords. When this QR code is scanned from the ODK Collect app on another device, these settings are imported.

Sharing QR code
------------------

You can click on the |share| icon to share the QR code as an image. When you click on it, it displays a list of applications and services like *whatsapp*, *facebook*, *hangouts*, *bluetooth*, *MMS* to name a few, which can be used to share the QR code. This is useful when there are several different data collection sites and all devices have to be configured in the same way, in which case the QR code can be shared from one reference device. 

.. |share| image:: /img/collect-settings/share-icon.*
             :alt: Share icon for sharing the QR code. 
             :height: 43 px
             :width: 43 px

.. warning:: 
  Since the QR code may contain the admin and server passwords without encryption, you should be careful about how you share it. It is advised to not send it through an external application but through *bluetooth*, *MMS* or any other such service that doesn't allow the third party to access the data. 

Saving QR code locally
-------------------------

You can go to :menuselection:`⋮ --> Save settings to disk` to save the QR code.

.. note::

  Settings are exported and saved so that they can be loaded to other devices. When you save external settings, they are saved to :file:`/sdcard/odk/settings/collect.settings`. You can load external settings from this location to other devices as well.

  At app launch, the settings are loaded from a different location :file:`/sdcard/odk/collect.settings`, which tracks the state of your settings at all times. 

  Settings are saved to and loaded from different locations to avoid deleting the saved settings.

Importing settings from a QR saved on your device
----------------------------------------------------

You can import settings from a QR code saved on your device by clicking on :guilabel:`Select Code from SD Card` option.

Making your own QR code
---------------------------

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
------------------------------

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

