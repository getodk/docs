Settings QR codes
========================

Collect can read settings from or write settings to a QR code. Settings QR codes can be provided by servers (like ODK Central) or can be used to share settings from one device to another.

.. _configuration-qr-code-management:

Managing and distributing settings QR codes
--------------------------------------------

.. warning::

  Settings QR codes generally include confidential information and should be kept private. Make sure to follow :doc:`Android security best practices <collect-security>`.

When using :ref:`Central App Users <central-users-app-overview>`, settings QR codes are used as `passwordless authentication <https://www.cyberark.com/what-is/passwordless-authentication/>`_. When using other servers, settings QR codes may contain plaintext passwords. Settings QR codes should be treated with the same care as passwords would be. We recommend scanning them directly from the Central user interface if possible.

In some contexts, especially on larger, remote, or regionally-distributed projects, directly scanning QR codes from Central may not be possible. Here are some alternative distribution options:

* Right-click an App User QR code in Central, save it, and send it via email, text message, WhatsApp, etc to data collectors who can then import the image into Collect.
* If a single QR code will represent a role and be shared between multiple users, you can put it on a slide or on a handout during a training. Make sure that all copies are destroyed at the end. Alternately, you can scan the code into one device and use Collect to share it with the next person who can share it on, etc. 
* If a project is intended to be used by the general public, you can post QR codes publicly in places like a billboard or on Facebook.
* If you need a large number of App Users representing individuals, use a script to bulk create App Users and generate a single document with all QR codes (`Python example <https://getodk.github.io/pyodk/examples/app_user_provisioner/app_user_provisioner/>`_).

Scanning a QR code
------------------

Settings QR codes can be scanned when adding a new Project or can be scanned to reconfigure the current Project by navigating to :guilabel:`Reconfigure with QR code` in :guilabel:`Project Management` settings.

.. note::
  QR codes contain settings with non-default values. When a code is scanned in, settings not explicitly included in the code are reset to their default values.

Importing a QR code saved on your device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can import settings from a QR code saved as a image on your device by clicking on the :fa:`ellipsis-v` icon when scanning a QR code. Then select the :guilabel:`Import QR code` option.

.. _sharing-settings-with-another-device:

Sharing settings with another device
-----------------------------------------

Navigate to :guilabel:`Reconfigure with QR code` in :guilabel:`Project Management` settings and tap :guilabel:`QR Code` to display the current Project's settings QR code. This can then be scanned by another device to either add a new Project or reconfigure the current one.

.. warning::
  Settings QR codes contain the admin and server passwords *in plain text*. To remove them from the code, tap the warning on the QR code screen.

Sharing a QR code as an image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can tap on the :fa:`share-alt` icon to share the QR code as an image. When you click on it, it displays a list of applications and services like *whatsapp*, *facebook*, *hangouts*, *bluetooth*, *MMS* which can be used to share the QR code. This is useful when there are several different data collection sites and all devices have to be configured in the same way, in which case the QR code can be shared from one reference device.

.. warning::
  Since the QR code encodes compressed plain text settings and may contain the admin and server passwords, you should be careful about how you share it. For example, if you print out the QR code and tape it on wall, someone could use a standard QR code scanner to get the admin password.

.. _create-settings-qr-code:

Making your own QR code
---------------------------

The contents of a settings QR code is a JSON object with objects for unprotected ("general") and protected ("admin") settings, as well as the project details themselves. The JSON structure is the following:

.. code-block:: JSON

  {
    "general": {
      "server_url": "https://demo.getodk.org",
      "constraint_behavior": "on_finalize"
    },
    "admin": {
      "edit_saved": false
    },
    "project": {
      "name": "QR code project",
      "icon": "Q",
      "color": "#ff0000"
    }
  }

The JSON object is compressed using `zlib <http://www.zlib.net/manual.html>`_ before building the QR code. To build your own code:

1) Write a JSON object containing the changed settings with a structure as shown above. The JSON must contain keys for ``general`` and ``admin``, even if the associated values are empty objects.
2) Compress it using zlib
3) Encode the result to Base64
4) Build a QR code from the resulting data

Python script for building settings QR codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: Python

  from base64 import b64encode
  import codecs
  import json
  import segno
  import zlib

  settings = { ... }

  qr_data = b64encode(zlib.compress(json.dumps(settings).encode("utf-8")))

  code = segno.make(qr_data, micro=False)
  code.save('settings.png', scale=5)

You can use this approach as part of automating a broader process. For example, see `this example from the pyodk documentation <https://getodk.github.io/pyodk/examples/app_user_provisioner/app_user_provisioner/>`_ which creates App Users in Central, assigns forms to them, builds QR codes, and produces a PDF of all the codes.

List of keys for all settings
------------------------------

Here are the keys for all settings and the set of values they can take:

.. code-block:: javascript

  {
    "project": {
      "name": String,
      "icon": String,
      "color": String
    },

    "admin" : {
      "admin_pw": String,

      // User access control to the main menu. The default value is true.
      "edit_saved": Boolean,
      "send_finalized": Boolean,
      "view_sent": Boolean,
      "get_blank": Boolean,
      "delete_saved": Boolean,
      "qr_code_scanner": Boolean,

      "change_server": Boolean,
      "change_app_theme": Boolean,
      "change_app_language": Boolean,
      "change_font_size": Boolean,
      "change_navigation": Boolean,
      "maps": Boolean,
      "periodic_form_updates_check": Boolean,
      "automatic_update": Boolean,
      "hide_old_form_versions": Boolean,
      "change_autosend": Boolean,
      "delete_after_send": Boolean,
      "default_to_finalized": Boolean,
      "change_constraint_behavior": Boolean,
      "high_resolution": Boolean,
      "image_size": Boolean,
      "guidance_hint": Boolean,
      "external_app_recording": Boolean,

      "instance_form_sync": Boolean,
      "change_form_metadata": Boolean,
      "analytics" : Boolean,

      "moving_backwards": Boolean
      "access_settings": Boolean,
      "change_language": Boolean,
      "jump_to": Boolean,
      "save_mid": Boolean,
      "save_as": Boolean,
      "mark_as_finalized": Boolean,
    },

    "general" : {

      // Server
      "protocol": {"odk_default"},
      "server_url": String,
      "username": String,
      "password": String,
      "formlist_url": String,
      "submission_url": String,

      // User interface
      "appTheme": {"light_theme", "dark_theme"},
      "app_language": BCP 47 language codes. The ones supported by Collect are: {"af", "am", "ar", "bg", "bn", "ca", "cs", "da", "de", "en", "es", "et", "fa", "fi", "fr", "hi", "in", "it", "ja", "ka", "km", "ln", "lo_LA", "lt", "mg", "ml", "mr", "ms", "my", "ne_NP", "nl", "no", "pl", "ps", "pt", "ro", "ru", "rw", "si", "sl", "so", "sq", "sr", "sv_SE", "sw", "sw_KE", "te", "th_TH", "ti", "tl", "tr", "uk", "ur", "ur_PK", "vi", "zh", "zu"},
      "font_size": {13, 17, 21, 25, 29},
      "navigation": {"swipe" ,"buttons" ,"swipe_buttons"},

      // Maps
      "basemap_source": {"google", "mapbox", "osm", "usgs", "stamen", "carto"},
      "google_map_style": {1, 2, 3, 4},
      "mapbox_map_style": {"mapbox://styles/mapbox/light-v10", "mapbox://styles/mapbox/dark-v10", "mapbox://styles/mapbox/satellite-v9", "mapbox://styles/mapbox/satellite-streets-v11", "mapbox://styles/mapbox/outdoors-v11"},
      "usgs_map_style": {"topographic", "hybrid", "satellite"},
      "carto_map_style": {"positron", "dark_matter"},
      "reference_layer": String, // Absolute path to mbtiles file

      // Form management
      "form_update_mode": {"manual", "previously_downloaded", "match_exactly"},
      "periodic_form_updates_check": {"every_fifteen_minutes", "every_one_hour", "every_six_hours", "every_24_hours"},
      "automatic_update": Boolean,
      "hide_old_form_versions": Boolean,
      "autosend": {"off", "wifi_only", "cellular_only", "wifi_and_cellular"},
      "delete_send": Boolean,
      "default_completed": Boolean,
      "constraint_behavior": {"on_swipe", "on_finalize"},
      "high_resolution": Boolean,
      "image_size": {"original", "small", "very_small", "medium", "large"},
      "external_app_recording": Boolean,
      "guidance_hint": {"no", "yes", "yes_collapsed"},
      "instance_sync": Boolean,

      // User and device identity
      "analytics": Boolean,
      "metadata_username": String,
      "metadata_phonenumber": String,
      "metadata_email": String,
    },
  }
