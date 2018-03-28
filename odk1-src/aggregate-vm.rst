.. spelling::

  readme
  VirtualBox

ODK Aggregate Virtual Machine
=============================

This document provides instructions on setting up :doc:`aggregate-intro` using the `Aggregate VM OVA file <https://github.com/opendatakit/aggregate/releases/download/v1.5.0-beta.0/ODK-Aggregate-v1.5.0-beta.0.ova.zip>`_ and `VirtualBox <https://www.virtualbox.org>`_.

.. admonition:: Before you get started…

  - Please read this entire document before installing the virtual machine (VM). Doing so will save you a lot of time and effort.

.. _setting-up-the-virtual-machine:

Setting Up the Virtual Machine
------------------------------

1. Download and install VirtualBox from `virtualbox.org <https://www.virtualbox.org>`_.
2. Download the latest Aggregate OVA file from the `Downloads <https://opendatakit.org/downloads/>`_ page

   - Alternatively, if you're looking for a specific version of Aggregate, you can find them zipped on the `GitHub releases page <https://github.com/opendatakit/aggregate/releases>`_.

3. Double-click on the OVA file to let VirtualBox import the VM. Accept the default settings.
4. After the import completes, start the VM: select it with your mouse and click on the "Start" button on the VirtualBox top toolbar. A new black and white window will pop up.
5. After the VM starts, wait for "Welcome to ODK Aggregate VM" message to be shown.
6. Do not log into the screen of the VM. Instead, on your computer, open a web browser.
7. Go to the web address shown in the VM screen, which normally will read `http://localhost:10080 <http://localhost:10080>`_. You will see the Aggregate login screen.
8. :guilabel:`Sign in with Aggregate password`

  username: ``administrator``
  password: ``aggregate``

9. Aggregate will remind you to change your administrator user's password. Please do so!

.. admonition:: Notes

  - Read `Running your virtual machine <https://www.virtualbox.org/manual/ch01.html#idm362>`_ manual page to learn more about working with VirtualBox and your Aggregate VM.

  - Once VirtualBox has imported the VM, the zip file and the OVA file can be deleted. It is a good idea to keep the readme file for future reference.

  - The OVA files published on GitHub releases page are zipped. You will have to unzip them in order to follow the steps above.

  - Windows: if you get an error message about "File is busy" or "File access error" after launching the VM, it is likely due to improper unzipping or write permissions. Try right-clicking the zip file, then select "Extract All" and save the files to a folder on the Desktop.

  - Linux: if you get an error message about "PAE: Unable to boot", make sure VirtualBox has PAE/NX enabled. That setting is usually under System/Processor.

.. _securing-the-vm:

Securing the VM
---------------

The Aggregate VM is configured with a default root user password "aggregate". The first time you log into the command line interface, you will be forced to change it.

When you start the VM, VirtualBox opens up a new window, and the VM will boot up. Everything which would normally be seen on the virtual system's monitor is shown in the window.

When the VM has finished booting up, you will be prompted to log into the VM.

- Click on the screen to capture your mouse and keyboard
- Log into the command line interface with the following credentials:

   - Username: root
   - Password: aggregate

   You will be forced to change the default password on login. Please choose a secure password!

- Once you have logged in, you can exit the command line interface with the command :command:`exit`

.. admonition:: Notes

  - Make sure you understand how VirtualBox captures your mouse and keyboard and how to release them, reading the  `Capturing and releasing keyboard and mouse <https://www.virtualbox.org/manual/ch01.html#keyb_mouse_normal>`_ section of the VirtualBox manual.

.. connecting-to-collect:

Connecting to Collect
---------------------

The VM defaults to a NAT network adapter and so you will only be able to connect to it from your computer. This is the default behavior because it is the safest configuration.

If you'd like to connect to the VM from an external device (e.g., :doc:`collect-intro` on your phone or :doc:`briefcase-intro` on another computer), you must change the VM's network adapter settings in VirtualBox from NAT to Bridged. You must then reboot the VM. After the reboot, the VM will then behave like any other machine on your network and get an IP address.

Now, log into the command line interface of the VM. Run the :command:`aggregate-config` script will let you set a FQDN. This FQDN is the globally accessible address that you should enter Collect or Briefcase if you want to download blank forms or send completed forms.

.. code-block:: console

  aggregate-config --fqdn 192.168.5.2 --http-port 1234

The form download (but not the form listing) relies on the FQDN. If you want to use Collect to interact with Aggregate, you MUST configure the FQDN.

.. admonition:: Notes

  - In order to have external servers, you have to make your VM publicly accessible on the Internet with a static IP or fully-qualified domain name. Doing this requires a fair amount of technical skill and we instead recommend you install Aggregate on App Engine. Alternatively, export your data using Briefcase.

  - When all fails, shutdown the VM, reboot the host computer, and restart the VM.