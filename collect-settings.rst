Collect Settings and Security
================================

Settings are accessible from the :guiselect:`⋮` menu.

.. _general-settings:

General Settings
-----------------

.. _server-settings:

Server Settings
~~~~~~~~~~~~~~~~~

:menuselection:`Server` settings manage the connection to an ODK Aggregate server or Google Drive account for form management.

See :ref:`connecting-to-server` for more details.

.. _interface-settings:

User Interface Settings
~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`User Interface` settings define how the app looks and behaves. It includes settings for:

- :guilabel:`Language`
- :guilabel:`Text font size`
- :guilabel:`Navigation` (Swiping or Buttons)
- :guilabel:`Splash Screen` (an image to display while Collect loads)

.. _mapping-settings:

Mapping
"""""""""

Map setting are included on the :menuselection:`User Interface` settings page.

- :guilabel:`Mapping SDK` sets the app used for :ref:`geopoint`, :ref:`geoshape`, and :ref:`geotrace` :docs:`form-widgets`. Options are Google Maps (default) and OpenStreetMap.
- :guilabel:`Basemap` sets the specific map used when opening the mapping app. 

.. _form-management-settings:

Form Management Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`Form Management` settings handle default behavior when editing, finalizing, and importing forms.

- :guilabel:`Auto send` When enabled, forms are sent immediately when finalized if the device can connect to the internet. You can specify whether to send over WiFi, cell data, or both.
- :guilabel:`Delete after send` When enabled, form instances are deleted once they are sent.

.. rubric:: Form filling

- :guilabel:`Default to finalized` When enabled, forms are automatically finalized upon reaching the end of the form. You can opt out of finalizing any form when completing it.
- :guilabel:`Constraint processing` sets when response constraints are validated: When advancing through the form, or at finalization.
- :guilabel:`High res video` enables high resolution recordings.

.. rubric:: Form import

- :guilabel:`Import saved forms as finalized` When enabled, forms added directly to the :file:`instances/` directory are automatically set to :formstate:`Finalized`.

.. _id-settings:

User and Device Identity Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _form-metadata-settings:

Form Metadata Settings
""""""""""""""""""""""""

:menuselection:`User and Device Identity -> Form Metadata` sets identity values which are added to the metadata of forms completed on the device.

.. rubric:: User-defined

You can edit the following:

- :guilabel:`Username`
- :guilabel:`Phone number`
- :guilabel:`Email address`

.. rubric:: Device-defined

You cannot edit these:

- Device ID
- Subscriber ID
- SIM serial number

.. _usage-data-setting:

Usage Data
"""""""""""""

When enabled, ODK Collect sends usage and error data back to the ODK development team, which helps us improve the application.

Usage data is anonymized.

.. _admin-settings:

Admin Settings
-----------------

.. _admin-security:

Admin Security
~~~~~~~~~~~~~~~~

Admin settings can be **password protected**. If you set an :guilabel:`Admin Password` in the Admin settings screen, you will need to re-enter that password to access Admin settings in the future.

Admin settings allow you to :ref:`restrict which General Settings are seen by users <user-access-control-settings>`. To access those settings as an Admin (and see all of them), :gesture:`tap` :guilabel:`General Settings` from the Admin settings page.

.. _import-export-settings:

Import/Export settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Import/Export Settings` lets you copy settings quickly from one device to another, using a QR code. The QR image presented contains all of your current General and Admin settings, including admin and server passwords. When scanned by the ODK Collect app with another device, these settings are imported.

You can also import settings from a QR code saved to the device, by selecting :guilabel:`Select Code from SD Card`

.. warning:: 

  The QR code used for settings import contains the admin and server passwords *in plain text*. To remove them from the code, :gesture:`tap` the warning on the QR code screen.

.. _user-access-control-settings:

User Access Control Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section allows the admin to hide menu items and settings from the user.
