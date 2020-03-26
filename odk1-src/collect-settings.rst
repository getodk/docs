.. spelling::
  basemap
  Basemap
  basemaps
  Basemaps
  Mapbox
  Transifex
  Unfinalized

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

  .. container:: details

    .. image:: /img/collect-settings/general-settings.*
      :alt: General settings

.. _server-settings:

Server Settings
~~~~~~~~~~~~~~~~~

Server settings :doc:`configure the connection to an <collect-connect>` :doc:`openrosa` server (:doc:`Aggregate <aggregate-intro>`, :doc:`Central <central-intro>`, etc) or a :doc:`Google Drive account <collect-connect-google>`.

To access Server Settings:
  :menuselection:`⋮ --> General Settings --> Server`

  .. container:: details

    .. image:: /img/collect-settings/server-settings.*
      :alt: Server settings

.. seealso:: :doc:`collect-connect`

.. _interface-settings:

User Interface Settings
~~~~~~~~~~~~~~~~~~~~~~~~

User Interface settings control Collect's appearance and behavior.

To access User Interface settings:
  :menuselection:`⋮ --> General Settings --> User Interface`

  .. container:: details

    .. image:: /img/collect-settings/ui-settings.*
      :alt: User Interface settings

:guilabel:`Theme`
""""""""""""""""""
  Toggles Light and Dark themes.

  .. versionadded:: 1.15

  .. container:: details

    .. image:: /img/collect-settings/light-theme-main-menu.*
      :alt: The main menu, with the light theme enabled.
      :class: side-by-side


    .. image:: /img/collect-settings/dark-theme-main-menu.*
      :alt: The main menu, with the dark theme enabled.
      :class: side-by-side

:guilabel:`Language`
"""""""""""""""""""""
  Forces the Collect interface to use a specific language. By default, Collect matches the device language. Note that this only sets the language for the Collect interface and not for form contents. For multi-language forms, the form language is set :ref:`while filling out that form <change-form-language>`. The Collect translations are provided by the ODK community through the `Transifex service <https://www.transifex.com/opendatakit/collect/>`_. You can join Transifex to add or correct translations in your language.

:guilabel:`Text font size`
""""""""""""""""""""""""""""
  Sets the size of fonts used in the form-filling interface.

:guilabel:`Navigation`
"""""""""""""""""""""""
  Sets form navigation style for moving between questions.

  Options:

  - Horizontal swiping
  - Forward and back buttons
  - Both

:guilabel:`Splash Screen`
"""""""""""""""""""""""""""
  Sets an image to display while Collect loads.

.. _mapping-settings:

Maps Settings
~~~~~~~~~~~~~~~

Maps settings configure the maps shown by the :ref:`location question types <location-widgets>`.

To access Maps settings:
  :menuselection:`⋮ --> General Settings --> Maps`

.. note::

  Prior to ODK Collect v1.23, map settings were available in the :ref:`interface-settings`. The basemap was configured by first selecting a :guilabel:`Mapping SDK` and then a :guilabel:`Basemap`.

.. _basemap-settings:

Basemap settings
""""""""""""""""""
Basemap settings configure the background of maps shown by the :ref:`location question types <location-widgets>`. Basemaps are provided by several different :guilabel:`Sources` which may each make several different map :guilabel:`Styles` available. A basemap is intended to provide details that help users orient a map and to make the map easy to use in a particular data collection environment. For example, if the data to be collected relates to elevation, consider selecting a topographic basemap.

:guilabel:`Sources`
  A basemap source provides one or more map styles:

  - :guilabel:`Google` basemap styles are used by Google Maps and other Google products.
  - :guilabel:`Mapbox` basemap styles are `used in many familiar products <https://www.mapbox.com/maps/streets/>`_.
  - :guilabel:`OpenStreetMap` provides one style which also powers `openstreetmap.org <https://www.openstreetmap.org>`_. OpenStreetMap data is used in basemaps provided by all other sources as well.
  - :guilabel:`USGS` is the United States Geological Survey. It provides `topograpic and satellite basemaps <https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer>`_ for the United States only.
  - :guilabel:`Stamen` provides `a terrain basemap with large labels <http://maps.stamen.com/terrain>`_.
  - :guilabel:`Carto` basemap styles are `designed to be used with data layers <https://carto.com/blog/getting-to-know-positron-and-dark-matter/>`_.

  .. _reference-layer-settings:

Reference layer settings
"""""""""""""""""""""""""
Reference layer settings configure map data shown on top of the basemap. Currently, a reference layer can only be defined by an offline MBTiles file as described in :doc:`collect-offline-maps`. The reference layer will appear when the zoom level is within the range supported by the file. If a reference layer has no transparency, it will fully cover the basemap selected above and behave like an offline basemap. Vector MBTiles files will only be available in the :guilabel:`Layer data file` menu if a Mapbox basemap is selected. Raster MBTiles files will be available for any basemap source and style.

.. _form-management-settings:

Form Management Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Form Management settings control default behavior when editing, finalizing, and importing forms.

To access Form Management settings:
  :menuselection:`⋮ --> General Settings --> Form Management`

  .. container:: details

    .. image:: /img/collect-settings/form-management.png
      :alt: Form Management settings

    .. image:: /img/collect-settings/form-management2.png
      :alt: Form Management settings

.. rubric:: Form update

:guilabel:`Periodic form updates check`
""""""""""""""""""""""""""""""""""""""""
  Specifies the frequency at which the configured server should be polled for form updates.

:guilabel:`Automatic download`
"""""""""""""""""""""""""""""""
  When enabled, any form currently on the device that has a new version available on the server will be automatically downloaded.

:guilabel:`Hide old form versions`
"""""""""""""""""""""""""""""""""""
  When enabled, if there are multiple versions of the same form, only the most recently downloaded will be displayed on the :guilabel:`Fill Blank Form` screen.

.. rubric:: Form submission

:guilabel:`Auto send`
""""""""""""""""""""""
  When enabled, forms are sent immediately when they are finalized, if the device can connect to the internet. If an internet connection is not available at the time of finalization, your finalized forms will be queued to send as soon as connectivity is established.
  You can specify whether to send over WiFi, cellular data, or both.

:guilabel:`Delete after send`
""""""""""""""""""""""""""""""
  When enabled, form instances are deleted once they are sent.

.. rubric:: Form filling

:guilabel:`Default to finalized`
"""""""""""""""""""""""""""""""""
  When enabled, records are set to be finalized when saved at the end of a form-filling session. You can opt out of this at the end of filling any specific record. This is particularly important to consider when using :doc:`encrypted forms <encrypted-forms>` because encryption happens on finalization. Finalized records for encrypted forms can't be opened because they are encrypted. Records for encrypted forms that have not been finalized are not encrypted and can be edited.

:guilabel:`Constraint processing`
"""""""""""""""""""""""""""""""""""
  Sets when form responses are validated against constraints_.

  Options:

  - Upon forward swipe. (That is, right after the question is answered.)
  - At finalization.

  .. _constraints: http://xlsform.org/#constraints

:guilabel:`High res video`
"""""""""""""""""""""""""""""
  When enabled,
  :ref:`video` widgets will record high resolution video
  if possible.

:guilabel:`Image size`
""""""""""""""""""""""""
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

:guilabel:`Show guidance for questions`
""""""""""""""""""""""""""""""""""""""""
  Guidance hints on questions can be used to display additional information that is not always needed. For example, they can be used to show extra instructions to be used during training or valuable only on a printout. If set to `Yes - always shown`, guidance hints will always be displayed below regular hints. If set to `Yes - collapsed`, the user will need to tap to view guidance hints.

.. rubric:: Form import

:guilabel:`Finalize forms on import`
"""""""""""""""""""""""""""""""""""""
  When enabled, forms added directly to the :file:`instances/` directory are automatically set to :formstate:`Finalized`. This is particularly relevant when putting records for an encrypted form directly to the device because encryption happens on finalization.

.. _id-settings:

User and Device Identity Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User and device identity settings control how
personally identifiable information and device ID
are used.

To access User and device identity settings:
  :menuselection:`⋮ --> General Settings --> User and device identity`

  .. container:: details

    .. image:: /img/collect-settings/und-settings.*
      :alt: User and Device Identity Settings

.. _form-metadata-settings:

Form metadata settings
""""""""""""""""""""""""

Form metadata settings control identifying information
:ref:`added to forms <metadata>` filled on the device.

To access form metadata settings:
  :menuselection:`⋮ --> General Settings --> User and Device Identity --> Form Metadata`

  .. container:: details

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
- Install ID

:guilabel:`Device ID` is currently set to the device IMEI. Starting in August 2020, Google will no longer allow Android applications to read the IMEI. At that time, the Collect-generated :guilabel:`Install ID` will be used as the :guilabel:`Device ID`. Both are currently displayed to allow organizations to transition over. :guilabel:`Install ID` can be copied by long-pressing on its text.

.. _usage-data-setting:

.. rubric:: Usage data

When enabled, ODK Collect sends anonymous usage and error data
back to the ODK development team,
which helps us improve the application.

.. _admin-settings:

Admin Settings
-----------------

Admin settings manage other settings and features,
letting you :doc:`import or export settings <collect-import-export>`,
:ref:`reset settings and delete cached data <reset-application>`,
and :ref:`restrict which features are available to users of the app <user-access-control-settings>`.

Admin settings are useful when
you are managing devices that will be used by many enumerators,
and you would like to limit the options available to those enumerators.

You can `password protect`__ the Admin setting screen,
so enumerators cannot adjust settings or access restricted features.

__ _admin-password

To access Admin settings:
  :menuselection:`⋮ --> Admin Settings`


.. image:: /img/collect-settings/admin-settings.*
  :alt: Admin settings menu
  :class: device-screen-vertical


:guilabel:`General Settings`
  Provides access to :ref:`general-settings`,
  with all items unrestricted.

.. _admin-password:

:guilabel:`Admin Password`
  Lets you password protect this screen.

.. _reset-application:

:guilabel:`Reset application`
  Lets you reset to default settings,
  delete forms, and empty caches.

:guilabel:`Import/Export settings`
  See:

  .. toctree::
    :maxdepth: 1

    collect-import-export

.. _user-access-control-settings:

.. rubric:: User Access Control Settings

:guilabel:`Main Menu Settings`
  Displays a list of :ref:`main-menu` features.
  To hide features, uncheck them.

:guilabel:`User Settings`
  Displays a list of user settings and other features
  accessible in the :ref:`general-settings` screen.
  To hide features, uncheck them.

:guilabel:`Form Entry Settings`
  Displays a list of features related to viewing and filling out forms.
  To disable features, uncheck them.

  :guilabel:`Moving backwards`
    If you disable moving backwards,
    the enumerator cannot use the back button or :gesture:`swipe right`
    to move backwards through a form.

    However, disabling this feature
    does not completely restrict a user's ability to access
    already-answered questions.
    So,
    when you uncheck this box to restrict backward movement,
    the app will suggest several additional restrictions
    which will prevent a non-admin user
    from revisiting already-asked questions:

    - Disable :guilabel:`Edit Saved Form` option in the main menu
    - Disable :guilabel:`Save Form` option in the Form entry menu
    - Disable :guilabel:`Go To Prompt` option in the Form entry menu
    - Set :guilabel:`Constraint processing` to validate upon forward swipe in the Form Management settings

    .. image:: /img/collect-settings/moving-backwards-disabled.*
      :alt: Image showing message displayed to configure other settings when Moving backwards option is unchecked.
      :class: device-screen-vertical

    Select :guilabel:`YES` to set these additional restrictions.

    .. note::

      When you enable the moving backwards option,
      you have to configure the other changed settings
      since they are not automatically changed back.
