.. spelling::

  Tecno
  Infinix


Troubleshooting
=====================

In this guide, we cover the likely problems you *might* encounter installing and configuring the ODK-X basic tools. The ODK-X basic tools are ODK-X Services, ODK-X Tables and ODK-X Survey. 

Do ensure that you have followed all the instructions for installation stated in the :doc:`basics-install` page.

.. _troubleshoot-devices:

Devices
--------------------

This section covers issues that are specific to the Android device you are working with and how to solve these problems.

.. note::
  The ODK-X basic tools require an Android device with a version 4.4 or higher operating system. 
    
Certain **Tecno** and **Infinix** devices run specific system settings which prevent applications from running in the background to conserve battery life. For the ODK-X applications to work, they need to be able to run in the device background. 

You will typically run into issues as a result of these devices' system setting. Users with these devices will notice that the Survey and Tables applications do not start and the screens are stuck on a configuring loop.

To solve for this, you have to enable :guilabel:`Auto-start` for the ODK-X applications on your device.

.. _tecno-infinix-devices:

For Tecno and Infinix devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Open :guilabel:`Phone Master`.
  2. On the :guilabel:`Toolbox` page, navigate to :guilabel:`Auto-Start management`.
  3. Scroll to find the ODK-X applications installed and toggle on to enable Auto-start.
   
