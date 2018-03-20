.. spelling::

  readme
  VirtualBox

ODK Aggregate Virtual Machine
=============================

This document provides instructions on setting up ODK Aggregate using the `ODK Aggregate VM OVA file <https://github.com/opendatakit/aggregate/releases/download/v1.5.0-beta.0/ODK-Aggregate-v1.5.0-beta.0.ova.zip>`_ and `VirtualBox <https://www.virtualbox.org>`_.

.. admonition:: Before you get started…

  - Please read this entire document before installing the virtual machine (VM). Doing so will save you a lot of time and effort.

.. _setting-up-the-virtual-machine:

Setting Up the Virtual Machine
------------------------------

1. Download and install VirtualBox from `virtualbox.org <https://www.virtualbox.org>`_.
2. Double-click `ODK-Aggregate-v1.5.0-beta.0.ova <https://github.com/opendatakit/aggregate/releases/download/v1.5.0-beta.0/ODK-Aggregate-v1.5.0-beta.0.ova.zip>`_ to import the VM. Accept the default settings.
3. After the import completes, start the VM.
4. After the VM starts, wait for Welcome to ODK Aggregate VM message to be shown.
5. Do not login into the black and white screen of the VM. Instead on your computer, open a web browser.
6. Go to the web address shown in the VM boot screen (e.g., `http://localhost:10080 <http://localhost:10080>`_). You will see the Aggregate login screen.
7. Click "Sign in with Aggregate password" and login with username and password shown below.

  - Aggregate username: aggregate
  - Aggregate password: aggregate

8. ODK Aggregate will remind you to change your administrator password. Please do so!

.. admonition:: Notes

  - If after unzipping the installer and launching the VM, a "File is busy" or "File access error" message is reported on Windows, it is likely due to improper unzipping or write permissions. Try right-clicking the zip file, then select Extract All and save the files to a folder on the Desktop.

  - If on Linux you get an error message about "PAE: Unable to boot", make sure VirtualBox has PAE/NX enabled. That setting is usually under System/Processor.

  - The ova file is the installer. Once the VM has imported, the ova file and the zip file can be deleted. It is a good idea to keep the readme (this file).

.. _securing-the-vm:

Securing the VM
---------------

Once the VM reboots, login to the command line interface with the following credentials

- Username: root
- Password: aggregate

You will be forced to change the default password on login. Please choose a secure password!

.. connecting-to-collect:

Connecting to Collect
---------------------

The VM defaults to a NAT network adapter and so you will only be able to connect to it from your computer. This is the default behavior because it is the safest configuration.

If you'd like to connect to the VM from an external device (e.g., ODK Collect on your phone or ODK Briefcase on another computer), you must change the VM's network adapter settings in VirtualBox from NAT to Bridged. You must then reboot the VM. After the reboot, the VM will then behave like any other machine on your network and get an IP address.

Now, log into the command line interface of the VM. Run the :command:`aggregate-config` script will let you set a FQDN. This FQDN is the globally accessible address that you should enter ODK Collect or ODK Briefcase if you want to download blank forms or send completed forms.

.. code-block:: console

  aggregate-config --fqdn 192.168.5.2 --http-port 1234

The form download (but not the form listing) relies on the FQDN. If you want to use Collect to interact with Aggregate, you MUST configure the FQDN.

.. admonition:: Notes

  - In order to have external servers, you have to make your VM publicly accessible on the Internet with a static IP or fully-qualified domain name. Doing this requires a fair amount of technical skill and we instead recommend you install ODK Aggregate on App Engine. Alternatively, export your data using ODK Briefcase.

  - When all fails, shutdown the VM, reboot the host computer, and restart the VM.