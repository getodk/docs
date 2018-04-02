Getting Started Deployment Architect Guide
==========================================================

.. _architect-odk-2:

This guide is intended for Deployment Architects. A Deployment Architect is an author of a data management application or a consumer of collected data. This person might create forms and edit Javascript on their computer to deploy to the Android device. Or they might download data from the server and use Excel to perform analysis. Examples include technical staff and data analytics staff.

Other perspective definitions can be found :ref:`here <odk-2-perspectives>`.


.. contents:: :local:

.. _architect-odk-2-prereqs:

Prerequisites
------------------
 This guide continues the tour were :doc:`getting-started-2-user` left off. If you haven't yet completed that tour, do it first. When you have concluded the tour of the *Geotagger* example application's screens, return to this guide and we will turn to setting up our own ODK Aggregate server, and setting the application up to run on that server.

.. _architect-odk-2-setting-up:

Migrating / Setting-up an ODK 2 application
------------------------------------------------

Now that we have seen how a device can join an already-configured application, and synchronize its view of the data with the ODK Aggregate server hosting the application, it is time to set up our own ODK Aggregate server.

The starting point for this is to have a fully configured application on your device. Only after you have your device configured as you want it to appear, would you proceed with the following steps. In this case, we already have the device configured with the *Geotagger* demo, so let's proceed to create an ODK Aggregate server and configure it to serve that demo to your devices.

.. _architect-odk-2-setting-up-server:

Setting up the ODK Aggregate server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the instructions for :doc:`aggregate-install`. You must install the **ODK Aggregate v1.4.15** release. This is because we are transitioning away from Aggregate and towards :doc:`sync-endpoint`, but v1.4.15 will suit the purposes of this demo fine.

Once you have installed ODK Aggregate, log in with your super-user account. That process is also covered in :doc:`aggregate-install`.

Once logged in, enable the :doc:`aggregate-tables-extension`. You should grant the user account on your device the :guilabel:`Administer Tables` permissions.

.. _architect-odk-2-setting-up-reset:

Resetting the Application on the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resetting the application on the ODK Aggregate server will push the application configuration on your device up to your server, replacing the configuration that is already on your server. Once the configuration is updated, data tables on the server and device will be synced. This process does not destroy data on the server, but instead merges changes on the client with any existing data tables on the server (this enables you to update your configuration without worrying about damaging or destroying the data already captured on the server).

Return to your device, start ODK Tables:

  #. Click the diminishing-lines icon to leave the custom home screen.
  #. Click the three vertical dots and select :guilabel:`Sync` to launch ODK Services onto the sync screen.
  #. Choose :menuselection:`Settings --> Server Settings`.
  #. Edit the :guilabel:`Server URL` to be the URL for this newly configured ODK Aggregate server (https://myodk-test.appspot.com).
  #. Click on :guilabel:`Server Sign-on Credential` and choose :menuselection:`Username`.
  #. Choose :guilabel:`Username` and enter the superuser username for your ODK Aggregate server
  #. Choose :guilabel:`Server Password` and enter the ODK Aggregate server password for that superuser username.
  #. Click the back button until you have returned to the sync screen.
  #. Click on :guilabel:`Reset App Server` to push your device configuration up to your ODK Aggregate server

After this has completed, you have created your own server that replicates the configuration and contents of the https://opendatakit-simpledemo.appspot.com site. Congratulations!

.. note::

  Any device with a user account with :guilabel:`Administer Tables` permissions can reset the app server. If you configure a device with a user account (or Anonymous user) with only the :guilabel:`Synchronize Tables` permissions, they will not be able to reset the app server and will only be able to sync and join into the existing ODK 2 application on this ODK Aggregate server.

.. _architect-odk-2-config:

Configuring your Device with an Application
-----------------------------------------------

Next, we will work through the steps to configure your device with an ODK 2 application (rather than downloading an existing application from a server).

This task begins with setting up the :doc:`app-designer-intro` on your computer.

For the purposes of this tutorial, we have created a copy of the Application Designer that only contains the files for this *Geotagger* example (it is otherwise identical).

.. _architect-odk-2-config-setup-app-designer:

Setting up ODK Application Designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read the :ref:`Intro <app-designer-intro>` and :ref:`Overview <app-designer-overview>` sections to get a sense of the features and functionality of the ODK 2 Application Designer environment (we will install it below). Follow this guide to :doc:`app-designer-setup`.

Finally, follow this guide to :doc:`app-designer-launching`.

If successful, the :program:`cmd` window (on Windows) should display some status messages. Below is a screen-shot of my :program:`cmd` window beginning with a :program:`dir` of the contents of the directory, and running :program:`grunt` in that directory:

.. image:: /img/getting-started-2/geotagger-cmd-window.*
  :alt: Geotagger Command Window

And a :program:`Chrome` browser window should open to display:

.. image:: /img/getting-started-2/geotagger-chrome-window.*
  :alt: Geotagger Chrome Window

If a :program:`Chrome` browser does not open, try manually launching it and opening http://localhost:8000/index.html.

You can further verify that the Application Designer works by clicking on the :guilabel:`Geotagger` button, then clicking on :guilabel:`Follow link`. This opens the *Geotagger* form on your computer, and simulates all the features available to you on your device.

You can also try other things, like choosing different device dimensions to see how the form renders on different screen geometries.

We will return to this design environment later.

.. _architect-odk-2-config-deploy:

Deploying to the Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have the design environment installed and functioning, and because that environment has a copy of the fully-configured *Geotagger* application that is running on https://opendatakit-simpledemo.appspot.com (minus any data that users have submitted to the server), we can work through the steps of deploying that application to your device, and then resetting your server to push that configuration up to your server.


First, confirm that your device has :guilabel:`USB debugging` enabled inside your device's :guilabel:`Settings`. This checkbox is in different places on different devices and may be hidden by default on some. See this guide to `USB debuggin on Android <https://www.phonearena.com/news/How-to-enable-USB-debugging-on-Android_id53909>`_ for instructions.

Return to the :program:`cmd` window on your computer. :kbd:`Control-C` to stop the :program:`grunt` command that popped-open the :program:`Chrome` browser. On Windows, you will be asked to confirm this ``Terminate batch job (Y/N)?``. Enter ``Y`` to confirm.

Connect your device to your computer via USB. Wait for the storage connection to be established (on Windows, this will generally pop up a file browser or an options box that enables you to select a file browser).

At the command prompt, type:

.. code-block:: console

  $ grunt adbpush

.. warning::

  This command will force-close ODK Services, Survey, and Tables, and it will clear all ODK 2 data from the device. The data you are pushing will overwrite any exiting application or collected data you might have. Be sure to make backups and be sure you are ready before running this command.

This pushes the configured ODK 2 application within this ODK 2 Application Designer directory to your device. Because this is a stripped-down version of the Application Designer that only contains the simple demo files, this will copy only those files to the device. When you issue this command, the :program:`cmd` window will display a long series of commands and conclude with a display of overall progress and timings:

.. image:: /img/getting-started-2/geotagger-cmd-gruntpush.*
  :alt: Geotagger Grunt Push

Now, on your device, launch ODK Tables.

This will initiate the configuration of ODK Tables and conclude with a :guilabel:`Configuration Summary` pop-up reporting that everything was imported successfully. Click :guilabel:`OK`.

Everything should now appear as it did with the application you first joined on https://opendatakit-simpledemo.appspot.com, except you will only have the data rows configured by the ODK 2 Application Designer zip, and not any added or modified since that time.

.. _architect-odk-2-config-reset-server:

Resetting the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the application running on the device, you will typically need to reset the contents of the application server. While the :guilabel:`Reset App Server` button on the device can shuffle the various supporting files between the device and the server, it will not destroy data tables that already exist on the server. This is intentional -- we want to minimize the potential for accidental loss of data.

.. note::

  Whenever you are developing an application, and have found a need to add a new column to an existing table, you will need to manually delete the data tables from the server before using the :guilabel:`Reset App Server` button from the device.

Open a browser window to the server, log in with a user that has :guilabel:`Administer Tables` or :guilabel:`Site Admin` privileges.

Navigate to the :guilabel:`ODK Tables / Current Tables` sub-tab.

Delete each of the tables here. In this case, there will be only one, *Geotagger*. The server will now have a set of App-Level files but no data tables, forms for those tables, or data files. Except for the app-level files, it is clean.

.. note::

  If your table has a large number of configuration files or data rows, the server may time out during the deletion process. In this case, the next time you try to create the table on the server, it will resume the deletion process, and potentially time out again until such time as it is able to finish the deletion. Only then will it re-create the table.

Now, from your device, launch ODK Tables, click on the sync icon (two curved arrows) to launch ODK Services, make sure you are logging in as a user with :guilabel:`Administer Tables` or :guilabel:`Site Admin` privileges, and choose :guilabel:`Reset App Server`.

The synchronization process will create the tables and push your content up to this server. Note that the server now only contains the data rows present on the device -- it no longer has any of the additional data records from the demo site.

You have now successfully set up the Application Designer, used it to deploy an application to a device, and, from that device, configured an ODK Aggregate server to supply that application to other devices you join to that server.

.. _architect-odk-2-modify:

Modifying an ODK 2 application
-------------------------------------

The final task is to modify the *Geotagger* example by adding a new data field to it.


The overall development process is:

  #. :ref:`Revise the data entry form <architect-odk-2-modify-data-entry>`
  #. :ref:`Update the initialization files needed by ODK Tables <architect-odk-2-modify-init>`
  #. :ref:`Update the preloaded data values as needed <architect-odk-2-modify-preload>`
  #. :ref:`Update the HTML to include the new field <architect-odk-2-modify-html>`

And then follow the steps in the preceding section to deploy the modified application to the device and push the application up to an ODK Aggregate server.

.. _architect-odk-2-modify-data-entry:

Modifying the data entry form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return to your :program:`cmd` window and once again launch the ODK 2 Application Designer environment (and a :program:`Chrome` browser) by typing:

.. code-block:: console

  $ grunt

Now, open a file browser and navigate to the directory where you downloaded the Application Designer. Then navigate within that directory to :file:`app/config/tables/geotagger`. Rename the :file:`properties.csv` and :file:`definition.csv` files in this directory to :file:`orig.properties.csv` and :file:`orig.definition.csv`. These were the initialization files needed by ODK Tables and they will need to be regenerated because we are altering the data table to incorporate an additional question.

Navigate within that directory to :file:`app/config/tables/geotagger/forms/geotagger`. Open the :file:`geotagger.xlsx` file in :program:`Excel` (or :program:`OpenOffice`). This is the form definition used by ODK Survey.

We will be adding a question to ask the user what direction they were facing when they took the photo. For this example, we will be collecting a text response. A more realistic modification might restrict the user to a set of choices (North, Northwest, West, Southwest, South, and so on).

On the survey worksheet, after the image-capture prompt, add a row that looks like the following.

.. list-table:: New Survey Row
  :header-rows: 1

  * - type
    - name
    - display.text
    - display.hint
  * - string
    - Direction
    - Image Direction
    - Enter the direction in which the photo was taken (North, South, East, West, and so on)

Save your changes and go back to the Application Designer. Click on the tab that says :guilabel:`XLSX Converter`. Choose this XLSX file or use your file browser to drag and drop the :file:`geotagger.xlsx` file onto this screen (dragging and dropping is not supported on all operating systems).

You should now see some JSON in the output window. Hit the :guilabel:`Save to File System` button. This will display three pop-up notifications announcing that the Application Designer is

  1. Writing the updated ODK Survey form definition into the :file:`formDef.json` file in the same location as the :file:`geotagger.xlsx` file.
  2. Updating the :file:`definition.csv` file.
  3. Updating the :file:`properties.csv` file.

.. note::

  The :file:`definition.csv` and :file:`properties.csv` files are updated because the *form_id* is the same as the *table_id*.

Go back to the :program:`Chrome` Browser and click on the :guilabel:`Preview` tab. Click on :guilabel:`Purge Database`. This will delete the earlier *Geotagger* data table -- a necessary step because we are adding a :th:`Direction` column to that data table. Select :guilabel:`Geotagger` if you do not already have that form open.

Create a new instance of *Geotagger* and advance through it (this will create the data table with the new :th:`Direction` column). Confirm that the new question is displayed. Note that the date and description are required fields and will generate error pop-ups if you attempt to advance through those prompts without supplying a value.

You have now successfully modified the form.

.. _architect-odk-2-modify-init:

Updating the Initialization Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fortunately, because the geotagger *formId* matches the *tableId*, by using the :guilabel:`Save to File System` button on the CSV, the tool will automatically regenerate the :file:`definition.csv` and :file:`properties.csv` files for this form. Furthermore, the configuration that ODK Tables uses to specify what HTML files to use for the list, detail, and map views are all specified within the XLSX file on the properties sheet. No manual actions are required!

Now, deploy your updated application to your device. Launch ODK Tables to initialize and load your application. Confirm that when you edit a data row that you are now asked for the direction in which the photo was taken.

.. _architect-odk-2-modify-preload:

Updating the Preloaded Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point, we have added the new field to the data table, but have not yet updated the initial set of *Geotagger* locations with values for that field.

Return to your :file:`Application Designer` directory. Recall that when an ODK Tables application first starts up, it reads the :file:`assets/tables.init` file. That file identifies CSV files within :file:`config/assets/csv` that should be imported into the data tables upon first start-up. Read more about importing data into a table from a CSV in the :ref:`ODK Tables guide <tables-managing-import-data>`.

In this example application, the file being imported is :file:`config/assets/csv/geotagger.updated.csv`. If we wanted to, we could edit this file, add a column for the new data field (:th:`Direction`), and supply values for this field for all of the data rows that form the initial set of *Geotagger* locations.

Alternatively, we can return to the device and use the CSV export functionality within ODK Tables to export the CSV file (into :file:`/sdcard/opendatakit/default/output/csv`). Then pull it off the device and overwrite the CSV file under the Application Designer at :file:`app/config/assets/csv/geotagger.updated.csv`. Finally, open that file and fill in values for the :th:`Direction` column.

.. warning::

  Some CSV editors, like :program:`Office` or :program:`OpenOffice`, may convert or alter the content inappropriately when you save changes. If your edits cause the device to fail to initialize the data fields, you may need to make this edit manually using a less-sophisticated tool or choose different options when saving your changes.

.. _architect-odk-2-modify-html:

Updating the HTML files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two areas where image information is displayed, one is in the list view, where you can expand or collapse an item, and the other is in the detail view, which is opened when you click or tap on an expanded item in the list view. We will only modify this detail view to report the image direction. A more comprehensive edit would likely also update the expanded item within the list view.

To determine all the HTML files, we can begin with the files referenced in the :file:`properties.csv` file we recently finished editing. Looking again at that file, we see three files referenced:

  - :file:`tables/geotagger/html/geo_list.html`
  - :file:`tables/geotagger/html/geo_list_thumbnail.html`
  - :file:`tables/geotagger/html/geo_detail.html`

Each of these files, or the JavaScript within them, might open or reference other files that might need to be updated. The above files are simply the ones we know are reachable. In general, files for displaying table-specific data are under the :file:`config/tables/tableid` directory. In this example, we will modify the last of these files and its associated JavaScript file.

Open a file browser and navigate to the directory where you downloaded the Application Designer. Then navigate within that directory to :file:`app/config/tables/geotagger/html`. Open :file:`geo_detail.html` in a text editor. Insert a line that defines a *DIR* element above the *Latitude* line in the HTML body region. This will be where we will display the value of the *Direction* field. For example:

.. code-block:: html

  <h1><span id="TITLE"></span></h1>
  <p>Image Direction: <span id="DIR"></span></p>
  <p>Latitude: <span id="FIELD_1"></span></p>

Save the file. Now, navigate to :file:`app/config/tables/geotagger/js`. Open :file:`geo_detail.js` in a text editor. Navigate down to the bottom of the :code:`display()` JavaScript function (to line 44). And add before the closing bracket:

.. code-block:: javascript

  var dir = geoDetailResultSet.get("Direction");
  document.getElementById("DIR").innerHTML = dir;

Save the file. Once again, push the application to the device. Confirm that when you expand a item in the map list window, and then tap on that expanded item, that it now shows *Image Direction:*. (See example below.)

.. image:: /img/getting-started-2/geotagger-image-dir.*
  :alt: Geotagging Image Direction
  :class: device-screen-vertical

Congratulations, you have successfully modified this ODK 2 application to add a new data field and display it as a field in the HTML detail-view page.

You could now log onto your server, delete the geotagger table, reset your server, and start collecting geopoints with the new image direction field.

.. _architect-odk2-next:

Next Steps
-----------------------

Survey and Tables each have a basic sample application that walks through their features:

  - :doc:`survey-sample-app`
  - :doc:`tables-sample-app`


To get started building applications, first set up the :doc:`app-designer-intro`. After you have familiarized yourself with that tool, you can try building and deploying an application:

  - :doc:`build-app`

A more complete guide to using ODK XLSX Converter is provided in the :doc:`xlsx-converter-intro` documentation. More details about Tables web views are available in :doc:`tables-web-pages` and :doc:`injected-interfaces`.

For examples of real world applications and details about they are implemented, try out the: :doc:`reference-apps`.

We also provide guides geared towards Deployment Architects for each of the Android and Desktop tools.

  - :doc:`survey-managing`
  - :doc:`tables-managing`
  - :doc:`services-managing`
  - :doc:`scan-managing`

However the user guides for these tools are also useful for everyone.

Finally, to expand your knowledge of the more advanced features of the platform, such as data permission filters, read the :doc:`advanced-topics-architect`.


