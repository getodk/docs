Installing the Virtual Machine
==============================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

This document provides instructions for installing :doc:`aggregate-intro` using the Virtual Machine (VM) and `VirtualBox <https://www.virtualbox.org>`_.

.. _setting-up-the-vm:

Setting up the VM
-----------------

1. Download and install `VirtualBox <https://www.virtualbox.org>`_.
2. Download the latest Aggregate VM from the `GitHub releases page <https://github.com/getodk/aggregate/releases>`_ and unzip the file.
3. Double-click the OVA file inside the zip to let VirtualBox import the VM. Accept the default settings.
4. After the import completes, start the VM. Select it with your mouse and click on the :guilabel:`Start` button on the VirtualBox top toolbar. A new black and white window will open.
5. After the VM starts, wait for **Welcome to ODK Aggregate VM** message to appear.
6. Do not log into the screen of the VM. Instead, on your computer, open a web browser.
7. Go to the web address shown in the VM screen. (Usually `http://localhost:10080 <http://localhost:10080>`_.) If everything worked, you will see the Aggregate login screen.
8. :guilabel:`Sign in with Aggregate password`

   | username: ``administrator``
   | password: ``aggregate``

9. Aggregate will remind you to change your administrator user's password. Please choose a secure password!

.. tip::

  Once VirtualBox has imported the VM, the zip file and the OVA file can be deleted.

.. note::

  - Read the `Running your virtual machine <https://www.virtualbox.org/manual/ch01.html#idm362>`_ manual page to learn more about working with VirtualBox and your Aggregate VM.

  - Windows: if you get an VirtualBox error message with "File is busy" or "File access error" after launching the VM, it is likely due to improper unzipping or write permissions. Try right-clicking the zip file, then select "Extract All" and save the files to a folder on the Desktop.

  - Linux: if you get a VirtualBox error message about "PAE: Unable to boot", make sure VirtualBox has PAE/NX enabled. That setting is usually under System/Processor.

.. _securing-the-vm:

Securing the VM
---------------

The Aggregate VM is configured with a default root user password which is not secure. Before using the VM with important data, we recommend you log in and change the default password.

1. Start the VM. When the VM has finished booting up, you will be prompted to log into the VM.
2. Click on the screen to capture your mouse and keyboard.
3. Log into the command line interface with the following credentials:

  | username: ``root``
  | password: ``aggregate``

4. You will be forced to change the default password the first time you login. Please choose a secure password!
5. Once you have logged in, you can exit the command line interface with the :command:`exit` command.

.. note::

  Make sure you `understand how VirtualBox captures your mouse and keyboard and how to release them <https://www.virtualbox.org/manual/ch01.html#keyb_mouse_normal>`_.

.. _connecting-to-the-vm-from-external-apps:

Connecting to the VM from external apps
---------------------------------------

The VM defaults to a NAT network adapter, so you will only be able to connect to it from your computer. This is the default behavior because it is the safest configuration.

If you'd like to connect to the VM from an external device (for example, :doc:`collect-intro` on your phone or :doc:`briefcase-intro` on another computer), you must set a fully qualified domain name (FQDN) or globally accessible address.

.. tip::

  Aggregate's form download (but not form listing) relies on the FQDN. If you want to use Collect and Briefcase to interact with Aggregate, you must set the FQDN.

To set the FQDN, do the following:

1. :ref:`Secure the VM <securing-the-vm>`.
2. Change the VM's network adapter settings in VirtualBox from NAT to Bridged and reset/reboot the VM.
3. After the reset/reboot, the VM will behave like any other machine on your network and get an IP address from your router. The IP address will be shown to you after the **Welcome to ODK Aggregate VM** message.
4. Log into the command line interface of the VM and run the :command:`aggregate-config` script to set a fully qualified domain name (FQDN) using the IP address that was shown to you (e.g., ``192.168.5.2``).

  .. code-block:: console

    aggregate-config --fqdn 192.168.5.2 --http-port 8080 --https-port 8443 --net-mode bridge

5. After the configuration, use your host computer or any other computer on your network to log into Aggregate at the FQDN and port (e.g., ``http://192.168.5.2:8080``).

.. note::

  Learn more about `VirtualBox's networking <https://www.virtualbox.org/manual/ch06.html>`_ options.