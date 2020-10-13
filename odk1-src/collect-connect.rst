Connecting to a Server
========================

ODK Collect is used to fill forms with participants. Filled forms then need to be sent to a central location for review and analysis. Generally, organizations do this by configuring Collect to send forms to a server. For those working in environments without any internet connectivity, there are :ref:`other options <other-collect-server-options>`.

When you first install Collect, it connects to a demo server. This allows you to try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :doc:`filling them out <collect-filling-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.
  
Once you are done trying out Collect, you will need a plan for managing forms and data submissions. We recommend using :ref:`ODK Central <central-intro>` and configuring Collect by QR code. :doc:`Central <central-intro>` provides user and project management features as well as tools for viewing and exporting data. For complex data collection projects, it is usually the right choice. Organizations can choose to use their own infrastructure and have total control over their server configuration. However, setting up and maintaining a server requires technical skills.

Simple projects can choose to send data directly to Google Sheets.

.. _collect-connect-qr-code:

Configure server from QR code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. From the Action Button (:guilabel:`⋮`), select :menuselection:`Configure via QR code`

    .. image:: /img/collect-configure/quick-qr-code.*
      :alt: Configure via QR code
      :class: device-screen-vertical

#. Position the QR code in the center of the camera field, under the red line. When the camera focuses on the code, it will beep and scan the code.

#. Collect will apply the settings from the code and go back to the landing screen.

.. seealso::

  - :doc:`central-setup`
  - :ref:`Central App Users <central-users-app-overview>`
  - :doc:`collect-import-export`


.. _other-collect-server-options:

Configure server from settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`


   .. image:: /img/collect-connect/main-menu-highlight-kebab.*
     :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red.

   .. image:: /img/collect-connect/kebab-menu-general-settings.*
     :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.

#. Select :guilabel:`Server`

   .. image:: /img/collect-connect/general-settings-server.*
     :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

#. Make sure :guilabel:`ODK` is selected under :guilabel:`Type` and then fill in the :guilabel:`URL`, :guilabel:`Username` and :guilabel:`Password` for your server:

   .. image:: /img/collect-connect/server-settings-odk.*
     :alt: The Server Settings screen in the Collect app. Below the *Type* option there are three items labeled *URL*, *Username*, and *Password*.

Other options
~~~~~~~~~~~~~~~

.. toctree::
  :maxdepth: 1

  collect-connect-google
  Transfering blank and completed forms directly with adb <collect-adb>
  Using ODK Briefcase  <briefcase-using>