Briefcase vs Aggregate
=========================

.. _briefcase-points:

Briefcase
-------------

- Briefcase provides a mechanism to pull blank forms and finalized forms from ODK Collect or ODK Aggregate or any custom ODK directory into a local Briefcase storage location.
- It can push blank forms and finalized forms from Briefcase storage location to an Aggregate 1.0 instance.
- Export the finalized form to a CSV file for processing by other applications.
- It can be used to transfer data across incompatible upgrades of ODK Aggregate and it is required to decrypt any encrypted submissions.
- Briefcase is good for offline use when there is no need for a server. It is often enough for smaller projects.
- It can be used to back up all forms and submissions on Aggregate. In particular, Briefcase's :ref:`command line interface <cli-use>` makes this easier.


.. _aggregate-points:

Aggregate
------------

- Aggregate provides a ready-to-deploy server to provide blank forms to ODK Collect.
- It accepts finalized forms from ODK Collect and manages and visualizes the collected data.
- Export data as CSV file, KML file, JSON file (e.g., as CSV files for spreadsheets, or as KML files for Google Earth).
- It can be used to publish data to external systems.
- Aggregate can be used offline and locally (`ODK aggregate VM <https://gumroad.com/l/odk-aggregate-vm>`_).

.. tip::

 The ODK Aggregate VM is a fully-configured install of Aggregate that you can run on any computer. It requires very little setup, works well without Internet connectivity.


.. _briefcase-as-replacement:

ODK Briefcase as a replacement for ODK Aggregate
--------------------------------------------------

ODK Briefcase can pull data directly off ODK Collect devices but does not support pushing blank forms to ODK Collect. To use ODK Briefcase as a replacement for ODK Aggregate, you must manually install the forms on your ODK Collect device.

To manually install forms onto your ODK Collect device:

- Connect the device to your computer with a USB cable and either, for Android 2.x devices, turn on USB storage (on the Android device), or, for Android 4.x devices, choose to connect it as a Media device (on the computer).
- On the computer, copy the form definition and media folder to the :file:`/odk/forms` directory. For Mac OS/X, if it is an Android 4.x device, you will need to use `Android File Transfer <https://www.android.com/filetransfer/>`_ to accomplish this.
- On Android 2.x, turn off USB storage.
- Run ODK Collect
- Choose :guilabel:`Fill Blank Form`.

ODK Collect will scan the directory for new forms, parse them, and make them available in this list. It can take several moments for large forms to appear. When ODK Collect has completed scanning for new forms, it will display **Finished scanning**. All forms are loaded on the second line at the top of this screen.

The steps for pulling data directly into ODK Briefcase from your Android device differs between the :ref:`Android 2.x <pull-from-android2.x>` and :ref:`Android 4.x <pull-from-android4.x>` devices.
