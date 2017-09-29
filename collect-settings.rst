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
- :menuselection:`View Sent Form` displays the forms that have been sent.
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

.. image:: /img/collect-settings/form-management.*
  :alt: Form Management settings
  :class: device-screen-vertical

:menuselection:`Form Management` settings handle default behavior when editing, finalizing, and importing forms.

.. rubric:: Form submission

- :guilabel:`Auto send` When enabled, forms are sent immediately when finalized if the device can connect to the internet. You can specify whether to send over WiFi, cellular data, or both.
- :guilabel:`Delete after send` When checked, form instances are deleted once they are sent.

.. rubric:: Form filling

- :guilabel:`Default to finalized` When enabled, forms are automatically finalized upon reaching the end of the form. You can opt out of finalizing any form when completing it.
- :guilabel:`Constraint processing` used to select when response constraints are validated: After each swipe, or at finalization.
- :guilabel:`High res video` enables high-resolution recordings.

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

.. rubric:: User-defined

You can edit the following:

- Username
- Phone number
- Email address

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

:guilabel:`Import/Export Settings` lets you configure other devices indentical to your current device simply by scanning the QR code. The QR image presented contains all of your current General and Admin settings, including admin and server passwords. When scanned by the ODK Collect app with another device, these settings are imported.

You can also import settings from a QR code saved to the device, by selecting :guilabel:`Select Code from SD Card`

.. warning:: 

  The QR code used for settings import contains the admin and server passwords *in plain text*. To remove them from the code, :gesture:`tap` the warning on the QR code screen.

.. _user-access-control-settings:

.. rubric:: User Access Control Settings

This section allows the admin to hide menu items and settings from the user. It contains the following options:

- :guilabel:`Main Menu Settings` : Allows admin to hide some of the main-menu options from the users.
- :guilabel:`User Settings` : Allows admin to select the options that'll be visible to the users in the :guilabel:`General settings` menu.
- :guilabel:`Form Entry Settings` : Admin can configure the `form entry items` visible to the users. For example unchecking the :guilabel:`change language` option will prevent the user from changing the device language.
