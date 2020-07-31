Connecting to a Server
========================

ODK Collect is used to complete surveys with participants. Filled surveys then need to be aggregated in a central location for review and analysis. Generally, organizations do this by configuring Collect to send forms to a server. For those working in environments without any internet connectivity, there are :ref:`other options <other-collect-server-options>`.

When you first install Collect, it connects to `a demo server <https://opendatakit.appspot.com/Aggregate.html>`_. This allows you to try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :doc:`filling them out <collect-filling-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.
  
Once you are done trying out Collect, you will need to decide on a plan for managing forms and data submissions. We typically recommend using `ODK Central <central-intro>` and configuring Collect by QR code. :doc:`ODK Central <central-intro>` provides user and project management features as well as tools for viewing and exporting data. For complex data collection projects, it is usually the right choice. Organizations with strict privacy requirements can choose to use their own infrastructure and have total control over their server configuration. However, setting up and maintaining a server can be challenging.

Simple projects can choose to send data directly to Google Sheets. Please make sure that this meets your privacy requirements.

.. toctree::
  :maxdepth: 2

  collect-connect-aggregate
  collect-connect-google

.. _other-collect-server-options:

Other options
~~~~~~~~~~~~~~~


Managing forms from an ODK Aggregate server or Google Drive is typical. However, there are other ways to use Collect.

 - :ref:`Transfer blank forms directly to your device <loading-forms-directly>`
 - :doc:`Pull completed forms directly with adb <collect-adb>`
 - :doc:`Use ODK Briefcase  <briefcase-using>`

.. - :doc:`Send submissions via SMS (text message) <collect-sms-submissions>`