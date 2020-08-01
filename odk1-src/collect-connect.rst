Connecting to a Server
========================

ODK Collect is used to fill forms with participants. Filled forms then need to be aggregated in a central location for review and analysis. Generally, organizations do this by configuring Collect to send forms to a server. For those working in environments without any internet connectivity, there are :ref:`other options <other-collect-server-options>`.

When you first install Collect, it connects to `a demo server <https://opendatakit.appspot.com/Aggregate.html>`_. This allows you to try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :doc:`filling them out <collect-filling-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.
  
Once you are done trying out Collect, you will need to decide on a plan for managing forms and data submissions. We typically recommend using `ODK Central <central-intro>` and configuring Collect by QR code. :doc:`ODK Central <central-intro>` provides user and project management features as well as tools for viewing and exporting data. For complex data collection projects, it is usually the right choice. Organizations with strict privacy requirements can choose to use their own infrastructure and have total control over their server configuration. However, setting up and maintaining a server can be challenging.

Simple projects without strict privacy requirements can choose to send data directly to Google Sheets.

.. _collect-connect-qr-code:

Configure server from QR code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. From the Action Button (:guilabel:`⋮`), select :menuselection:`Configure via QR code`

.. image:: /img/collect-configure/quick-qr-code.*
  :alt: Configure via QR code
  :class: device-screen-vertical

1. Position the QR code in the center of the camera field, under the red line. When the camera focuses on the code, it will beep and scan the code.

1. Collect will apply the settings from the code and go back to the landing screen.

.. seealso::

  - :doc:`central-setup`
  - :ref:`Central App Users <central-users-app-overview>`
  - :doc:`collect-import-export`


.. _other-collect-server-options:

Other options
~~~~~~~~~~~~~~~

.. toctree::
  :maxdepth: 1

  collect-connect-google
  collect-connect-aggregate
  Transfering blank and completed forms directly with adb <collect-adb>
  Using ODK Briefcase  <briefcase-using>