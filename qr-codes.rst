***********************************************
Configure Collect on many devices with QR codes
***********************************************

This document lists the ways in which QR codes can be used to configure same settings across many devices.

.. _using-qr-codes-through-app:

Using QR codes through the app
==============================

This section will cover the steps required to set up and use QR codes through the app itself.

- The first step to using QR code configuration is to choose one device to be the reference. 
- On that device, set up the general and admin settings as desired. 
- Once the reference device is set up, go to :guilabel:`Admin Settings` > Import/Export settings. 
- You should see a QR code representing all the settings on that device.

Now the reference device is set up, and the next steps require the devices which need to be configured.

- The most common next step will be to take all of the devices that need to be configured and open up Admin Settings > Import/Export settings > Scan code. 

This will show a QR code scanner that you can use to scan the code from the reference device. Once the code is successfully scanned, Collect will return to the landing screen with a message saying settings were successfully loaded.

.. _share-barcode-as-an-image:

Share generated Barcode as an image
===================================

This section defines another possible way to use the QR code, by sending it to other devices as an image.  one person could generate the code and then send it to several different data collection sites to make sure all devices are configured in the same way. To share the barcode from the reference device:

- Go to :guilabel:`Admin Settings` > Import/Export settings.
- Tap on the three dots at the upper right corner.
- Tap on Share and select how you would like to share it.

.. note::
  
  The barcode contains all of the settings in clear text. That means that if passwords are included, anyone with access to the code could have access to the passwords.

.. _generate-qr-codes-programmatically:

Generate QR codes programmatically
==================================

This section explains how QR codes are generated programmatically, as form of json. For example, a QR code uses a json representation of the settings with a structure like the following:

.. code-block:: json

  {
  "general": {
    "protocol": "google_sheets",
    "constraint_behavior": "on_finalize"
  },
  "admin": {
    "edit_saved": false }
  }


There is no encryption, the json is just compressed with zlib.


