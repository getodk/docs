Connecting to a Server
========================

ODK Collect is used to fill forms with participants. Filled forms then need to be sent to a central location for review and analysis. Generally, organizations do this by configuring Collect to send forms to a server. For those working in environments without any internet connectivity, there are :ref:`other options <other-collect-server-options>`.

We recommend using :ref:`ODK Central <central-intro>` as your server and configuring Collect by QR code. :doc:`Central <central-intro>` provides user and project management features as well as tools for viewing and exporting data. The easiest way to get a Central server is by using `ODK Cloud <https://getodk.org/#odk-cloud>`_. If you have technical skills, you can also :doc:`self-host <central-install>` on your own infrastructure.

If you'd just like to try out ODK Collect without setting up a server, you can use the demo server which provides some sample forms. You can set this up by tapping :guilabel:`Try a demo` at the bottom of the screen when you first launch Collect. The demo project can later be :ref:`deleted <delete-project>`.

If you'd like to connect Collect to more than one server (or to the same server using different users) you can :ref:`add a new Project <collect-add-project>` for each server (or user).

.. _collect-connect-qr-code:

Configure server from QR code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. When you first launch Collect, tap on :guilabel:`Configure with QR code`.

#. Position the QR code in the center of the camera field, under the red line. When the camera focuses on the code, it will beep and scan the code.

#. Collect will apply the settings from the code and move you to the Main Menu.

.. seealso::

  - :doc:`central-install`
  - :ref:`Central App Users <central-users-app-overview>`
  - :doc:`collect-import-export`


.. _other-collect-server-options:

Configure server manually
~~~~~~~~~~~~~~~~~~~~~~~~~

If you're not using a server that uses QR codes you can still connect using a URL (and username/password if required):

#. When you first launch Collect, tap on :guilabel:`Manually enter project details`.
#. Enter the URL (and username/password if required) for you server.
#. Click :guilabel:`Add`.

Other options
~~~~~~~~~~~~~~~

.. toctree::
  :maxdepth: 1

  collect-connect-google
  Transferring blank and completed forms directly with adb <collect-adb>
  Using ODK Briefcase  <briefcase-using>
