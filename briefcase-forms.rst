**********************************
Briefcase Usage
**********************************

:doc:`Install Briefcase <briefcase-install>` before going through this section.

.. _pull-from-aggregate:

Pulling forms from ODK Aggregate
---------------------------------

- Open *ODK Briefcase*.
- In the window which opens up select :guilabel:`pull` tab.
- Select Aggregate 0.9.x or Aggregate 1.0 in the :guilabel:`pull data from` the drop-down.
- Enter the url of your ODK Aggregate server in :guilabel:`url` option. For instance `https://proj1.appspot.com` and click on connect.
- You can either leave the username blank if the anonymousUser is granted Data Viewer permissions or specify an ODK Aggregate user (Account Type 'ODK') that has been granted Data Viewer permissions.
- A list of forms will be displayed. Select the ones you want to pull and click on :guilabel:`pull` button at the bottom of the window. The forms will be pulled to ODK Briefcase Storage on your local system.

.. warning::

 ODK Briefcase will abort a pull attempt if the local copy of the form definition file differs in any way from the copy being pulled from the server or ODK Collect device.

.. tip::

 If the form definition has changed but the changes only affect the question text and do not alter the structure of the collected data (or change the formId or version), you can create a new ODK Briefcase Storage area, pull data into that, then manually copy the instances from there into your original storage area.


.. _push-to-aggregate:

Pushing forms to ODK Aggregate
--------------------------------

- Open *ODK Briefcase*.
- In the window which opens up select :guilabel:`push` tab.
- Select Aggregate 1.0 in the :guilabel:`push data to` drop-down.
- Enter the url of your ODK Aggregate server in :guilabel:`url` option. For instance `https://proj1.appspot.com` and click on connect.
- You can either leave the username blank if the anonymousUser is granted Data Viewer permissions or specify an ODK Aggregate user (Account Type 'ODK') that has been granted Data Viewer permissions.
- A list of forms will be displayed. Select the ones you want to push and click on :guilabel:`push` button at the bottom of the window. The forms will be pushed to ODK Aggregate Server.


.. warning::

  - ODK Briefcase will abort a push attempt if the form definition already on the ODK Aggregate server differs in any way from the form definition in the ODK Briefcase Storage area.
  - ODK Briefcase does not work with Google accounts (Account Type *Google*).


.. tip::

  - If the form definition has changed but the changes do not affect the data model, you can make a copy of the storage area, replace the copy's form definition file with that from the server, and then push the data up from this storage area copy.
  - By pulling data into the local ODK Briefcase Storage location and then pushing data up to an ODK Aggregate instance, ODK Briefcase provides a mechanism to transfer data across incompatible upgrades of ODK Aggregate.


.. _pull-from-collect:

Pulling forms from Collect
---------------------------

.. _pull-from-android2.x:

Pulling from Android 2.x and earlier device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Ensure all filled-in forms are finalized. Either delete the forms which are not finalized or delete them after making a backup copy of :file:`/sdcard/odk` directory on your device and restore that later.

.. warning::
 ODK Briefcase does not discriminate between incomplete and finalized forms on the device. It will pull all data off of the device. This can cause problems during later pushes, and, especially, if you are encrypting your finalized forms. To keep your data set clean, you must ensure that all forms are complete before being pulled off of the device.

- Connect your Android device to your computer using a USB cable and choose to mount the drive.
- Open *ODK Briefcase*.
- In the window which opens up select :guilabel:`pull` tab.
- Select `Mounted Android SD Card` in the :guilabel:`pull data from` drop-down.
- Click :guilabel:`Choose` and select the appropriate mounted SD card.
- A list of forms will be displayed. Select the ones you want to pull and click on :guilabel:`pull` button at the bottom of the window. The forms will be pulled to ODK Briefcase Storage on your local system.
- On the Android device, open ODK Collect and delete the filled-in forms.

.. warning::
 ODK Briefcase cannot discriminate between duplicates of the same filled-in form. After you pull the data into ODK Briefcase, it is important that you delete it from ODK Collect. Otherwise, the next time you follow this process, you will end up with two copies of the filled-in forms from the first pull, etc.

.. _pull-from-android4.x:

Pulling from Android 4.x and later device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Ensure all filled-in forms are finalized. Either delete the forms which are not finalized or delete them after making a backup copy of :file:`/sdcard/odk` directory on your device and restore that later.
- Create a zip of the entire :file:`odk` directory using an application like `OI File Manager <https://play.google.com/store/apps/details?id=org.openintents.filemanager>`_.
- Connect your Android device to your computer using a USB cable and choose to mount it as a Media device.
- Copy that zip file from the mounted MTP/Android device to a local hard drive.
- Once it is copied onto your local hard drive, unzip the file of the 'odk' directory.
- Open *ODK Briefcase*.
- In the window which opens up select :guilabel:`pull` tab.
- Select *Custom Path to ODK Directory* in the :guilabel:`pull data from` drop-down.
- Select the unzipped :file:`odk` folder that you copied onto your local hard drive.
- Click on :guilabel:`pull` button at the bottom of the window and the filled-in submissions that were copied off of the device will be loaded into ODK Briefcase's storage location.
- On the Android device, open ODK Collect and delete the filled-in forms.


.. tip::
 - You can use the *Custom path to ODK Directory* any time you want to pull forms from custom location.
 - You can confirm that the forms have been successfully pulled into ODK Briefcase by confirming a successful pull status or by verifying the data appearing in a CSV export file.

.. warning::
 - ODK Briefcase does not work with the USB-mounted Media device (MTP) protocol, which replaced the USB-mounted drive protocol on Android 4.x devices.
 - ODK Briefcase does not support pushing blank forms to ODK Collect. You can manually install the forms on your ODK Collect device.


.. _export-forms:

Export forms to CSV
---------------------

- Open *ODK Briefcase*.
- In the window which opens up select :guilabel:`export` tab.
- Select the form you wish to export from the :guilabel:`form` dropdown. It displays a list of all forms on your ODK Briefcase Storage.
- Specify the location where you wish to export form as csv on your system in the :guilabel:`Export Directory` option.
- Click on :guilabel:`Export` at the bottom of the window.


.. _cli-use:

Working with command line
----------------------------

In Briefcase v1.4.4 and later, there is a scriptable command line interface.

Pulling form data from Aggregate Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: console

  $ java -jar "ODK Briefcase v1.4.4 Production.jar" --form_id market_prices --storage_directory ~/Desktop --aggregate_url https://my_server.appspot.com --odk_username my_username --odk_password my_password

This command pulls form data with id market_prices from Aggregate server at `https://my_server.appspot.com` and stores data in Briefcase's storage directory on the :file:`~/Desktop`

Pulling form data from ODK Collect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: console

  $ java -jar "ODK Briefcase v1.4.4 Production.jar" --form_id market_prices --storage_directory ~/Desktop --odk_directory ~/Desktop/odk

This command pulls form data with id market_prices from Collect's odk folder at :file:`~/Desktop/odk` and store data in Briefcase's storage directory on the :file:`~/Desktop`

Export form data
~~~~~~~~~~~~~~~~~~~~
.. code-block:: console

  $ java -jar "ODK Briefcase v1.4.4 Production.jar" --form_id market_prices --storage_directory ~/Desktop --export_directory ~/Desktop --export_filename market_prices.csv

This command exports form data with id market_prices from Briefcase's storage directory on the :file:`~/Desktop` and write CSV file to :file:`~/Desktop/market_prices.csv`


To get help about the command line operation type :command:`java -jar path_to_jar -help`.

.. code-block:: console

  $ java -jar "/home/pc123/Desktop/ODK Briefcase v1.8.0 Production.jar" -help
