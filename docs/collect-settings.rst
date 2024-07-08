Using Collect Settings
=====================================

Collect has many settings to support a number of different data collection workflows. Settings are specific to each :doc:`project <collect-projects>` and are separated into :ref:`general <general-settings>` and :ref:`protected <admin-settings>` settings. Protected settings make it possible to remove access to certain parts of Collect and can be :ref:`password-protected <admin-password>`.

Settings for the current project are accessed from the project list dialog:
  :menuselection:`Project Icon --> Settings`

  .. container:: details

    .. image:: /img/collect-settings/settings.*
      :alt: Access settings by tapping the project icon and then the Settings button
      :class: device-screen-vertical

.. _general-settings:

General Settings
--------------------

.. _server-settings:

Server Settings
~~~~~~~~~~~~~~~~~

Server settings :doc:`configure the connection to an <collect-connect>` :doc:`openrosa` server (:doc:`Central <central-intro>`, etc).

To access Server Settings:
  :menuselection:`Project Icon --> Settings --> Server`

  .. container:: details

    .. image:: /img/collect-settings/server-settings.*
      :alt: Server settings
      :class: device-screen-vertical

.. seealso:: :doc:`collect-connect`


Project Display Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Project display settings control the name of the current project as well as the appearance of its icon in the upper right of the main screen.

To access Project Display Settings:
:menuselection:`Project Icon --> Settings --> Project Display`

  .. container:: details
    
    .. image:: /img/collect-settings/project-display.*
      :alt: Project display settings
      :class: device-screen-vertical

.. seealso:: :doc:`collect-projects`

.. _interface-settings:

User Interface Settings
~~~~~~~~~~~~~~~~~~~~~~~~

User Interface settings control Collect's appearance and behavior.

To access User Interface settings:
  :menuselection:`Project Icon --> Settings --> User interface`

  .. container:: details

    .. image:: /img/collect-settings/ui-settings.*
      :alt: User Interface settings
      :class: device-screen-vertical

:guilabel:`Theme`
""""""""""""""""""
  Selects the color scheme the app will use. The default :guilabel:`Use device theme` option (added in ODK Collect v2021.3) uses the device's color theme (based on the the :guilabel:`Dark theme` system setting in Android 10 and above).

  .. container:: details

    .. image:: /img/collect-settings/light-theme-main-menu.*
      :alt: The main menu, with the light theme enabled.
      :class: device-screen-vertical side-by-side


    .. image:: /img/collect-settings/dark-theme-main-menu.*
      :alt: The main menu, with the dark theme enabled.
      :class: device-screen-vertical side-by-side

:guilabel:`Language`
"""""""""""""""""""""
  Forces the Collect interface to use a specific language. By default, Collect matches the device language. Note that this only sets the language for the Collect user interface and not for the form. For :doc:`forms with multiple languages <form-language>`, the form language is set :ref:`while filling out the form <change-form-language>`.

  .. note::

    Collect's translations are provided by the ODK community through the `Transifex service <https://www.transifex.com/getodk/collect/>`_. You can join Transifex to add or correct translations in your language.

:guilabel:`Text font size`
""""""""""""""""""""""""""""
  Sets the size of fonts used in the form-filling interface.

.. _navigation:

:guilabel:`Navigation`
"""""""""""""""""""""""
  Sets navigation style for moving between questions in a form.

  Options:

  - Horizontal swiping
  - Forward and back buttons
  - Both (default)

.. _mapping-settings:

Maps Settings
~~~~~~~~~~~~~~~

Maps settings configure the maps shown by the :ref:`location question types <location-widgets>`.

To access Maps settings:
  :menuselection:`Project Icon --> Settings --> Maps`

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
  :menuselection:`Project Icon --> Settings --> Form management`

  .. container:: details

    .. image:: /img/collect-settings/form-management.png
      :alt: Form Management settings
      :class: device-screen-vertical

    .. image:: /img/collect-settings/form-management2.png
      :alt: Form Management settings
      :class: device-screen-vertical

.. rubric:: Form update

.. _blank-form-update-mode:

:guilabel:`Blank form update mode`
"""""""""""""""""""""""""""""""""""

Specifies how blank forms should be updated:

  :guilabel:`Manual`
    The default mode in Collect. Enumerators manually manage blank forms on the device using :guilabel:`Get Blank Form` and :guilabel:`Delete Saved Form`.
  :guilabel:`Previously downloaded forms only`
    Enumerators will receive a notification when one or more forms on the device have an update available to their form definition or media files. Tapping on the notification will go to :guilabel:`Get Blank Form` where the user can choose to download some or all of the updated forms.
  :guilabel:`Exactly match server`
    Collect will automatically download and update forms based on what's on the server. In addition, forms not on the server will be deleted from Collect. This mode hides :guilabel:`Get Blank Form` and the :guilabel:`Blank Forms` tab in :guilabel:`Delete Saved Form` as they are not required. The enumerator can trigger an update from the server on the :guilabel:`Fill Blank Form` screen. Filled instances of blank forms deleted during server updates will still be editable. This is the default when using a Central App User.

.. tip::

  If your server is configured to provide the exact set of forms enumerators need and you'd like to ensure they always have the most up to date versions on device then we recommend using :guilabel:`Exactly match server`.

  However, if your server is set up to provide forms that aren't relevant to every enumerator then we recommend using :guilabel:`Previously downloaded forms only` (ideally with :guilabel:`Automatic download`) so that enumerators are still notified when the forms they do use are updated.

  :guilabel:`Manually` makes the most sense when forms only need to be downloaded once and will never change or if you are extremely bandwidth-limited.

:guilabel:`Automatic update frequency`
""""""""""""""""""""""""""""""""""""""""
  Specifies how frequently Collect should check for updates to the forms on the server when using :guilabel:`Previously downloaded forms only` or :guilabel:`Exactly match server`. This option is not available if :guilabel:`Manually` is selected.

:guilabel:`Automatic download`
"""""""""""""""""""""""""""""""
  Only available if :guilabel:`Previously downloaded forms only` is selected. When :guilabel:`Automatic download` is enabled, the form update check will trigger an automatic download of any forms on the device that have updated definitions or media files. The user will receive a notification when the automatic download completes with either a success or failure. Tapping on the notification will go to :guilabel:`Get Blank Form` where the user will see success or failure messages for each form for which an update was attempted.

:guilabel:`Hide old form versions`
"""""""""""""""""""""""""""""""""""
  When enabled, if there are multiple versions of the same form, only the most recently downloaded will be displayed on the :guilabel:`Fill Blank Form` screen.

.. rubric:: Form submission

.. _auto-send:

:guilabel:`Auto send`
""""""""""""""""""""""
  When enabled, forms are sent immediately when they are finalized, if the device can connect to the Internet. If an Internet connection is not available at the time of finalization, your finalized forms will be queued to send as soon as connectivity is established. You can specify whether to send over WiFi, cellular data, or both.

.. _delete-after-send:

:guilabel:`Delete after send`
""""""""""""""""""""""""""""""
  When enabled, filled forms are deleted as soon as they are sent. This deletes the form data but leaves the forms :ref:`listed in the Sent form list <instance-name>`.

:guilabel:`Constraint processing`
"""""""""""""""""""""""""""""""""""
  Sets when form responses are validated against :ref:`constraints <constraints>`.

  Options:

  - Upon forward swipe. (That is, right after the question is answered.)
  - At finalization.

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
  :guilabel:`Very small (640 px)`
    Recommended when images don't need to be detailed
    or the internet connection used to send submissions is slow.
  :guilabel:`Small (1024 px)`
    Sufficiently detailed for most on-screen viewing
    but too small for printing.
  :guilabel:`Medium (2048 px)`
    Sufficiently detailed for most uses, including printing.
  :guilabel:`Large (3072 px)`
    Recommended when a lot of detail is needed,
    but you want to reduce the size of image files
    as much as possible.

:guilabel:`Show guidance for questions`
""""""""""""""""""""""""""""""""""""""""
  Guidance hints on questions can be used to display additional information that is not always needed. For example, they can be used to show extra instructions to be used during training or valuable only on a printout. If set to `Yes - always shown`, guidance hints will always be displayed below regular hints. If set to `Yes - collapsed`, the user will need to tap to view guidance hints.

.. _use-external-app-for-audio-recording:

:guilabel:`Use external app for audio recording`
""""""""""""""""""""""""""""""""""""""""""""""""
  By default, an internal recorder is used for audio recording. Check this setting to use the external audio application instead. When unchecked, recordings will be created as mono ``.m4a`` files using the ``AAC`` codec with a sample rate of 32 kHz and a bitrate of 64 kbps. This corresponds to a file size of about 30 MB/hour. We typically recommend configuring audio quality :ref:`in the form definition <customizing-audio-quality>` instead of using this setting but it can be useful for older forms that can't be modified.

.. rubric:: Form import

:guilabel:`Finalize forms on import`
"""""""""""""""""""""""""""""""""""""
  When enabled, forms added directly to the :file:`instances/` directory are automatically set to `Finalized`. This is particularly relevant when putting records for an encrypted form directly to the device because encryption happens on finalization.

.. _id-settings:

User and Device Identity Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User and device identity settings control how
personally identifiable information and device ID
are used.

To access User and device identity settings:
  :menuselection:`Project Icon --> Settings --> User and device identity`

  .. container:: details

    .. image:: /img/collect-settings/und-settings.*
      :alt: User and Device Identity Settings
      :class: device-screen-vertical

.. _form-metadata-settings:

Form metadata settings
""""""""""""""""""""""""

Form metadata settings control identifying information
:ref:`added to forms <metadata>` filled on the device.

To access form metadata settings:
  :menuselection:`Project Icon --> Settings --> User and Device Identity --> Form Metadata`

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
    :ref:`Protected settings <admin-settings>`.

.. rubric:: Device-defined

You cannot edit these:

- Device ID

:guilabel:`Device ID` is currently set to the Collect-generated :guilabel:`Install ID`.

.. _usage-data-setting:

.. rubric:: Usage data

When enabled, ODK Collect sends anonymous usage and error data
back to the ODK development team,
which helps us improve the application.

.. _admin-settings:

Protected Settings
--------------------

Protected settings manage other settings and features, letting you :doc:`import or export settings <collect-import-export>`, :ref:`reset settings and delete cached data <reset-application>`, and :ref:`restrict which features are available to users of the app <user-access-control-settings>`.

Protected settings are useful when you would like to limit the options available to enumerators so that they must follow a specific workflow.

You can :ref:`password protect <admin-password>` the protected settings, so enumerators cannot adjust settings or access restricted features.

.. _admin-password:

:guilabel:`Set admin password`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  If a password is set, when settings are opened, the :guilabel:`Protected` section will only contain :guilabel:`Unlock protected settings`. Tapping on that will display a dialog to provide the admin password. Before the correct admin password is provided, access controls will be in place and some settings may be hidden. Saving a blank password disables password protection.

.. _project-management-settings:

:guilabel:`Project management`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Reconfigure with QR code`
  Replace all settings from those in a QR code. See :doc:`configuring Collect via QR code <collect-import-export>`.

.. _reset-application:

:guilabel:`Reset`
  Reset to default settings, delete forms, and empty caches. There is a prompt to select which aspects of the project to reset.

.. _delete-project:

:guilabel:`Delete`
  Delete the current project.

.. _user-access-control-settings:

:guilabel:`Access control`
~~~~~~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Main Menu Settings`
"""""""""""""""""""""""""""""""
Displays a list of buttons shown on the main screen. To prevent access to certain features, uncheck them and their button will be hidden.

:guilabel:`User Settings`
"""""""""""""""""""""""""""""""
Displays a list of user settings and other features accessible in the :ref:`settings <general-settings>` screen. To hide features, uncheck them.

.. _form-entry-settings:

:guilabel:`Form Entry Settings`
"""""""""""""""""""""""""""""""

Displays a list of features related to viewing and filling out forms. To disable features, uncheck them.
  
.. _moving-backwards-setting:

:guilabel:`Moving backwards`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you disable moving backwards, the enumerator cannot use the back button or swipe right to move backwards through a form.

However, disabling this feature does not completely restrict a user's ability to access already-answered questions. So, when you uncheck this box to restrict backward movement, the app will suggest several additional restrictions which will prevent a non-admin user from revisiting already-asked questions:

- Disable :guilabel:`Edit Draft` option in the main menu
- Disable :guilabel:`Save as draft` option in the Form entry menu
- Disable :guilabel:`Go To Prompt` option in the Form entry menu
- Set :guilabel:`Constraint processing` to validate upon forward swipe in the Form Management settings

.. image:: /img/collect-settings/moving-backwards-disabled.*
  :alt: Image showing message displayed to configure other settings when Moving backwards option is unchecked.
  :class: device-screen-vertical

Select :guilabel:`YES` to set these additional restrictions.

.. note::

  When you enable the moving backwards option, you have to configure the other changed settings since they are not automatically changed back.
