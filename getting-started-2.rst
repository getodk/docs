ODK 2.0 Getting Started Guide
===============================

.. _using-odk-2:

The ODK 2.0 tools are intended to address limitations of the existing tool set. The 2.0 Tool Suite consists of:

- :doc:`services-intro` - an application that handles database access, file access, and data synchronization services between all of the ODK 2.0 applications. It also allows you to synchronize data collected by the ODK 2.0 tools using the 2.0 protocol with an ODK Aggregate instance.
- :doc:`survey-intro` - a data collection application based upon HTML, CSS, and JavaScript.
- :doc:`tables-intro` - a data collection and visualization application running on your device.
- :doc:`cloud-endpoints-intro` - a ready-to-deploy server and data repository with enhancements to support bi-directional data synchronization across disconnected devices.
- :doc:`app-designer-intro` - a design environment for creating, customizing, and previewing your forms.
- :doc:`suitcase-intro` - a desktop tool for synchronizing data from an ODK 2.0 server so the data can be exported to CSV format.

This page provides a brief end-to-end walk-through of the ODK 2.0 tools. It will cover the following topics:

.. contents:: :local:

.. _using-odk-2-apps:

ODK Data Management Applications
----------------------------------------

The ODK 2.0 Android tools (ODK Survey, ODK Tables, ODK Services, ODK Scan, ODK Sensors Framework, and various ODK Sensor implementations) are APKs that are designed to work together to create a coherent tailored application experience for an end-user.

.. note::

  Together the ODK 2.0 tools create a platform, on top of which you can build your own data management applications.

ODK 2.0 tools access configuration files and store data under sub-directories of the :file:`opendatakit` directory in the :file:`sdcard` root directory (whether your device has a physical SD card or not): :file:`/sdcard/opendatakit`. User applications constructed using the ODK 2.0 tools are identified by the name of the sub-directory holding those configuration and data files. Thus, :file:`/sdcard/opendatakit/mytestapp` would contain all the files and data for the *mytestapp* application. The name of that sub-directory, *mytestapp,* is referred to as the **AppName** of that application. The default **AppName** for the ODK tools is *default.* However, when configured appropriately, the ODK tools can run under another **AppName**, accessing configuration and saving data in a different subdirectory under opendatakit.

This is handled in such a way that each user application is isolated from all other user applications, with separate configurations, data tables, and server settings. This allows one device to run multiple user applications built on top of the ODK 2.0 tools without any coordination among the teams developing those applications.

A major goal of the 2.0 tools was to eliminate the need for any software engineering skills (e.g., Java programming, Android software development environment, source code version control systems) when designing data management applications. The skills required to build a data management application range from scripting a form definition in XLSX (similar to constructing ODK Collect forms using XLSX files processed by the XLSForm tool), to simple web programming -- modifying boilerplate HTML and JavaScript for custom presentations of the collected data. Advanced web programmers can also easily implement entirely-custom webpages.

.. _using-odk-2-joining-a-server:

Joining a device to an Existing Aggregate Server
------------------------------------------------------

The steps for joining a device to an existing Aggregate server are very straightforward.

  #. Install the APKs your application uses.
  #. Launch the *home screen* APK, either ODK Survey or ODK Tables.
  #. Click on the three vertical dots in the upper right corner of the menu bar and choose :menuselection:`Sync` to launch the ODK Services sync activity in the context of your *home screen* APK.
  #. Configure ODK Services to point to the ODK Aggregate instance you want to join.
  #. Choose :guilabel:`Sync now` to make the device mirror the contents on that ODK Aggregate server.

Follow the steps described above to join the ODK Aggregate server hosting our simple demo, which uses ODK Tables as its *home_screen* APK. The detailed steps are:

  #. Download and install ODK Services, ODK Tables, and ODK Survey.
  #. Launch ODK Tables (the *home_screen* APK).
  #. Click on the three vertical dots in the upper right corner of the menu bar and choose :menuselection:`Sync` to launch the ODK Services.
  #. The default Sync Configuration should be *https://open-data-kit.appspot.com* and :menuselection:`None (anonymous access)`. You will need to change that. It will also default to :menuselection:`Fully Sync Attachments`.
  #. Click on the three vertical dots in the menu bar, select :menuselection:`Settings --> Server Settings`.
  #. Click on :menuselection:`Server URL` and replace the default server with *https://opendatakit-simpledemo.appspot.com* then click :guilabel:`OK`.
  #. Back out of settings then choose :guilabel:`Sync Now`.

The synchronization process will now occu

.. note::

  If there is an error, check to make sure the server URL is correct, then choose :guilabel:`Sync Now` again until it completes successfully.

Once successful, back out of ODK Services, returning to ODK Tables. And back out of ODK Tables. Then relaunch ODK Tables.

.. _using-odk-2-demo-tour:

Tour of the Simple Demo Application
--------------------------------------

You should now see the custom home screen for the *Geotagger* demo:

.. image:: /img/getting-started-2/geo-demo-home.*
  :alt: Geotagging Demo Home
  :class: device-screen-vertical

This demo is based upon the *geotagger* data table and form. It allows users to record the date, time, GPS coordinates, description and picture of their current location.

When you launch the demo by clicking the blue launch button, you see a map showing the collected data points, indicated with markers. By clicking on a marker, you bring its data record to the top of the list of records above the map. Clicking on the record header will expand or contract that item to show the coordinates and photo of that location. For example, if we click on the *Phinney Ridge* marker, its color changes from blue to green, and, if we then touch the *Phinney Ridge* heading, it expands to show the coordinates and image of that location:

.. image:: /img/getting-started-2/phinney-ridge.*
  :alt: Phinney Ridge
  :class: device-screen-vertical

You can add a new data record by choosing the :guilabel:`+` icon in top menu bar. This opens ODK Survey.

.. note::

  Since ODK Survey is being opened for the first time, it will initialize itself. This may take a few moments.

.. image:: /img/getting-started-2/geotagger-new-location.*
  :alt: Geotagger New Location
  :class: device-screen-vertical

Advance through and finalize this form. Upon finalizing the form, you will be returned to ODK Tables and its map view. You can then highlight the marker you added and view the image in the list view:

.. image:: /img/getting-started-2/geotagger-odk-laboratory.*
  :alt: Geotagger ODK Lab
  :class: device-screen-vertical

If you then click or tap in the list item details area (on the image), a detail view of the item will be displayed.

From here, if you were to choose the pencil icon, ODK Survey would be launched to edit this record.

You can also view the data in a list view or spreadsheet view by choosing the sheet icon in the menu bar and selecting the view you want:

.. image:: /img/getting-started-2/view-type.*
  :alt: View Types
  :class: device-screen-vertical

.. tip::

  These other views can be useful if you need to access and complete data records that do not yet have location data and cannot therefore be displayed on a map. Try these other views now.

Now back out of the *geotagger* table view and return to the custom home screen. Choose the three-horizontal-line icon on the top menu bar and choose :menuselection:`Sync`. This opens up ODK Services in its sync activity. Sync your device with the server (choose :guilabel:`Sync Noaw`). This will push your newly-added record to the server. You can see this by browsing to https://opendatakit-simpledemo.appspot.com click on the :guilabel:`ODK Tables` tab, choose the :guilabel:`View Table` sub-tab, and select the *geotagger* table.

If you then repeat these steps with a different device, you can see that the two devices can share and exchange data, and revisions to this data, whenever they synchronize to the server.

.. note::

  During this process, there are two problem-resolution screens you are likely to encounter:

    - :ref:`Checkpoint Resolution <using-odk-2-demo-tour-checkpoints>` - if ODK Survey exits without the user explicitly saving their additions or changes.
    - :ref:`Conflict Resolution <using-odk-2-demo-tour-conflicts>` - if ODK Services detects a change on the server to a data record that was also changed on the device.

.. _using-odk-2-demo-tour-checkpoints:

Checkpoint Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~

The checkpoint resolution screen is most easily triggered if you choose the :guilabel:`+` icon then back out of ODK Survey:

.. image:: /img/getting-started-2/checkpoint-resolution.*
  :alt: Checkpoint Resolution
  :class: device-screen-vertical

When presented with this screen, there are three choices:

  - Cancel and continue editing the form.
  - Ignore changes and discard the entire partially-filled-out form.
  - Save it even though it is incomplete. In this case, since there is no entered data for this record, we can ignore changes.

In rare cases, a second form of checkpoint resolution screen can be triggered. This most often happens if ODK Survey experiences a failure and closes. In this case, you may have several data records with unsaved checkpoint changes (changes that the user has not explicitly saved as incomplete or finalized). This will lead to a screen like:

.. image:: /img/getting-started-2/checkpoint-list.*
  :alt: Checkpoint List
  :class: device-screen-vertical

Clicking a row will display details about that individual checkpoint:

.. image:: /img/getting-started-2/checkpoint-detail.*
  :alt: Checkpoint Detail
  :class: device-screen-vertical

In all of these screens, you can choose whether to save the changes as incomplete or to discard them.

.. _using-odk-2-demo-tour-conflicts:

Conflict Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The conflict resolution screen is triggered when another device has edited one or more rows and synchronized its changes to the server before your edits to those same rows have been synchronized. In this case, your synchronization attempt will end with an error, and a :guilabel:`Conflicts Detected` error will appear:

.. image:: /img/getting-started-2/conflict-resolution.*
  :alt: Conflicts Resolutino
  :class: device-screen-vertical

Once you click :guilabel:`OK`, the conflict resolution screen will be presented. If there are multiple rows in conflict, this screen will display the rows that are in conflict:

.. image:: /img/getting-started-2/conflict-list.*
  :alt: Conflict List
  :class: device-screen-vertical

Clicking a row will display details about the conflict:

.. image:: /img/getting-started-2/conflict-detail.*
  :alt: Conflict Detail
  :class: device-screen-vertical

And if only a single row is in conflict, the list-of-rows screen will be bypassed.

The conflict details screen displays the values of the field(s) in conflict, with the field value on the device (Local) appearing first. In this case, the *Description* field is in conflict. The device has *Kite hill at Gasworks* and the server has *Kite Hill ... Gasworks*. You can select either to take your device values (:guilabel:`Take Local Version`) or take the server's values (:guilabel:`Take Server Version`) or pick-and-choose among the changes and merge them (the :guilabel:`Merge Changes as Indicated Below` button will be enabled after all fields have had either their Local or Server value picked for the merge). After selecting the local version or choosing to merge, you must again synchronize with the server to push that change up to the server.

.. warning::

  When you resolve a conflict, your decision does not only affect you. The value you choose becomes the new true value and the next time you sync it will be written to the server.

This concludes the tour of the *Geotagger* example application's screens, and the functionality within ODK Tables. We will now turn to setting up our own ODK Aggregate server, and setting the application up to run on that server.

.. _using-odk-2-setting-up:

Migrating / Setting-up an ODK 2.0 application
------------------------------------------------

Now that we have seen how a device can join an already-configured application, and synchronize its view of the data with the ODK Aggregate server hosting the application, it is time to set up our own ODK Aggregate server.

The starting point for this is to have a fully configured application on your device. Only after you have your device configured as you want it to appear, would you proceed with the following steps. In this case, we already have the device configured with the *Geotagger* demo, so let's proceed to create an ODK Aggregate server and configure it to serve that demo to your devices.

.. _using-odk-2-setting-up-server:

Setting up the ODK Aggregate server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the instructions for :doc:`aggregate-install`. You must install the **ODK Aggregate v1.4.15** release. This is because we are transitioning away from Aggregate and towards :doc:`sync-endpoint`, but v1.4.15 will suit the purposes of this demo just fine.

Once you have installed ODK Aggregate, log in with your super-user account. That process is also covered in :doc:`aggregate-install`.

Once logged in, enable the :doc:`aggregate-tables-extension`. You should grant the user account on your device the :guilabel:`Administer Tables` permissions.

.. _using-odk-2-setting-up-reset:

Resetting the Application on the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resetting the application on the ODK Aggregate server will push the application configuration on your device up to your server, replacing the configuration that is already on your server. Once the configuration is updated, data tables on the server and device will be synced. This process does not destroy data on the server, but instead merges changes on the client with any existing data tables on the server (this enables you to update your configuration without worrying about damaging or destroying the data already captured on the server).

Return to your device, start ODK Tables:

  #. Click the diminishing-lines icon to leave the custom home screen.
  #. Click the three vertical dots and select :guilabel:`Sync` to launch ODK Services onto the sync screen.
  #. Choose :menuselection:`Settings --> Server Settings`.
  #. Edit the :guilabel:`Server URL` to be the URL for this newly configured ODK Aggregate server (e.g., https://myodk-test.appspot.com).
  #. Click on :guilabel:`Server Sign-on Credential` and choose :menuselection:`Username`.
  #. Choose :guilabel:`Username` and enter the superuser username for your ODK Aggregate server
  #. Choose :guilabel:`Server Password` and enter the ODK Aggregate server password for that superuser username.
  #. Click the back button until you have returned to the sync screen.
  #. Click on :guilabel:`Reset App Server` to push your device configuration up to your ODK Aggregate server

After this has completed, you have created your own server that replicates the configuration and contents of the https://opendatakit-simpledemo.appspot.com site. Congratulations!

.. note::

  Any device with a user account with :guilabel:`Administer Tables` permissions can reset the app server. If you configure a device with a user account (or Anonymous user) with just the :guilabel:`Synchronize Tables` permissions, they will not be able to reset the app server and will just be able to sync and join into the existing ODK 2.0 application on this ODK Aggregate server.

.. _using-odk-2-config:

Configuring your Device with an Application
-----------------------------------------------

Next, we will work through the steps to configure your device with an ODK 2.0 application (rather than downloading an existing application from a server).

This task begins with setting up the :doc:`app-designer-intro` on your computer.

For the purposes of this tutorial, we have created a copy of the Application Designer that only contains the files for this *Geotagger* example (it is otherwise identical).

.. _using-odk-2-config-setup-app-designer:

Setting up ODK Application Designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read the :ref:`Intro <app-designer-intro>` and :ref:`Overview <app-designer-overview>` sections to get a sense of the features and functionality of the ODK 2.0 Application Designer environment (we will install it below). Follow this guide to :doc:`app-designer-setup`.

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

.. _using-odk-2-config-deploy:

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

  This command will force-close ODK Services, Survey, and Tables, and it will clear all ODK 2.0 data from the device. The data you are pushing will overwrite any exiting application or collected data you might have. Be sure to make backups and be sure you are ready before running this command.

This pushes the configured ODK 2.0 application within this ODK 2.0 Application Designer directory to your device. Because this is a stripped-down version of the Application Designer that only contains the simple demo files, this will copy only those files to the device. When you issue this command, the :program:`cmd` window will display a long series of commands and conclude with a display of overall progress and timings:

.. image:: /img/getting-started-2/geotagger-cmd-gruntpush.*
  :alt: Geotagger Grunt Push

Now, on your device, launch ODK Tables.

This will initiate the configuration of ODK Tables and conclude with a :guilabel:`Configuration Summary` pop-up reporting that everything was imported successfully. Click :guilabel:`OK`.

Everything should now appear as it did with the application you first joined on https://opendatakit-simpledemo.appspot.com, except you will only have the data rows configured by the ODK 2.0 Application Designer zip, and not any added or modified since that time.

.. _using-odk-2-config-reset-server:

Resetting the Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have the application running on the device, you will typically need to reset the contents of the application server. While the :guilabel:`Reset App Server` button on the device can shuffle the various supporting files between the device and the server, it will not destroy data tables that already exist on the server; this is intentional -- we want to minimize the potential for accidental loss of data.

.. note::

  Whenever you are developing an application, and have found a need to add a new column to an existing table, you will need to manually delete the data tables from the server before using the :guilabel:`Reset App Server` button from the device.

Open a browser window to the server, log in with a user that has :guilabel:`Administer Tables` or :guilabel:`Site Admin` privileges.

Navigate to the :guilabel:`ODK Tables / Current Tables` sub-tab.

Delete each of the tables here. In this case, there will be only one, *Geotagger*. The server will now have a set of App-Level files but no data tables, forms for those tables, or data files. Except for the app-level files, it is clean.

.. note::

  If your table has a large number of configuration files or data rows, the server may time out during the deletion process. In this case, the next time you try to create the table on the server, it will resume the deletion process, and potentially time out again until such time as it is able to finish the deletion; only then will it re-create the table.

Now, from your device, launch ODK Tables, click on the sync icon (two curved arrows) to launch ODK Services, make sure you are loggin in as a user with :guilabel:`Administer Tables` or :guilabel:`Site Admin` privileges, and choose :guilabel:`Reset App Server`.

The synchronization process will create the tables and push your content up to this server. Note that the server now only contains the data rows present on the device -- it no longer has any of the additional data records from the demo site.

You have now successfully set up the Application Designer, used it to deploy an application to a device, and, from that device, configured an ODK Aggregate server to supply that application to other devices you join to that server.

.. _using-odk-2-modify:

Modifying an ODK 2.0 application
-------------------------------------

The final task is to modify the *Geotagger* example by adding a new data field to it.


The overall development process is:

  #. :ref:`Revise the data entry form <using-odk-2-modify-data-entry>`
  #. :ref:`Update the initialization files needed by ODK Tables <using-odk-2-modify-init>`
  #. :ref:`Update the preloaded data values as needed <using-odk-2-modify-preload>`
  #. :ref:`Update the HTML to include the new field <using-odk-2-modify-html>`

And then follow the steps in the preceding section to deploy the modified application to the device and push the application up to an ODK Aggregate server.

.. _using-odk-2-modify-data-entry:

Modifying the data entry form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return to your :program:`cmd` window and once again launch the ODK 2.0 Application Designer environment (and a :program:`Chrome` browser) by typing:

.. code-block:: console

  $ grunt

Now, open a file browser and navigate to the directory where you downloaded the Application Designer. Then navigate within that directory to :file:`app/config/tables/geotagger`. Rename the :file:`properties.csv` and :file:`definition.csv` files in this directory to :file:`orig.properties.csv` and :file:`orig.definition.csv`. These were the initialization files needed by ODK Tables and they will need to be regenerated because we are altering the data table to incorporate an additional question.

Navigate within that directory to :file:`app/config/tables/geotagger/forms/geotagger`. Open the :file:`geotagger.xlsx` file in :program:`Excel` (or :program:`OpenOffice`). This is the form definition used by ODK Survey.

We will be adding a question to ask the user what direction they were facing when they took the photo. For this example, we will be collecting a text response. A more realistic modification might restrict the user to a set of choices (North, Northwest, West, Southwest, South, etc.).

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
    - Enter the direction in which the photo was taken (North, South, East, West, etc.)

Save your changes and go back to the Application Designer. Click on the tab that says :guilabel:`XLSX Converter`. Choose this XLSX file or use your file browser to drag and drop the :file:`geotagger.xlsx` file onto this screen (dragging and dropping is not supported on all operating systems).

You should now see some JSON in the output window. Hit the :guilabel:`Save to File System` button. This will display three pop-up notifications announcing that the Application Designer is

  1. Writing the updated ODK Survey form definition into the :file:`formDef.json` file in the same location as the :file:`geotagger.xlsx` file.
  2. Updating the :file:`definition.csv` file.
  3. Updating the :file:`properties.csv` file.

.. note::

  The :file:`definition.csv` and :file:`properties.csv` files are updated because the *form_id* is the same as the *table_id*.

Go back to the :program:`Chrome` Browser and click on the :guilabel:`Preview` tab. Click on :guilabel:`Purge Database`. This will delete the earlier *Geotagger* data table -- a necessary step because we are adding a :th:`Direction` column to that data table. Select :guilabel:`Geotagger` if you do not already have that form open.

Create a new instance of *Geotagger* and advance through it (this will create the data table with the new :th:`Direction` column); confirm that the new question is displayed. Note that the date and description are required fields and will generate error pop-ups if you attempt to advance through those prompts without supplying a value.

You have now successfully modified the form.

.. _using-odk-2-modify-init:

Updating the Initialization Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fortunately, because the geotagger *formId* matches the *tableId*, by simply using the :guilabel:`Save to File System` button on the CSV, the tool will automatically regenerate the :file:`definition.csv` and :file:`properties.csv` files for this form. Furthermore, the configuration that ODK Tables uses to specify what HTML files to use for the list, detail, and map views are all specified within the XLSX file on the properties sheet. No manual actions are required!

Now, deploy your updated application to your device; launch ODK Tables to initialize and load your application. Confirm that when you edit a data row that you are now asked for the direction in which the photo was taken.

.. _using-odk-2-modify-preload:

Updating the Preloaded Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point, we have added the new field to the data table, but have not yet updated the initial set of *Geotagger* locations with values for that field.

Return to your :file:`Application Designer` directory. Recall that when an ODK Tables application first starts up, it reads the :file:`assets/tables.init` file; that file identifies CSV files within :file:`config/assets/csv` that should be imported into the data tables upon first start-up. Read more about importing data into a table from a CSV in the :ref:`ODK Tables guide <tables-using-import-data>`.

In this example application, the file being imported is :file:`config/assets/csv/geotagger.updated.csv`. If we wanted to, we could edit this file, add a column for the new data field (:th:`Direction`), and supply values for this field for all of the data rows that form the initial set of *Geotagger* locations.

Alternatively, we can return to the device and use the CSV export functionality within ODK Tables to export the CSV file (into :file:`/sdcard/opendatakit/default/output/csv`); then pull it off of the device and overwrite the CSV file under the Application Designer at :file:`app/config/assets/csv/geotagger.updated.csv`. Finally, open that file and fill in values for the :th:`Direction` column.

.. warning::

  Some CSV editors, like :program:`Office` or :program:`OpenOffice`, may convert or alter the content inappropriately when you save changes. If your edits cause the device to fail to initialize the data fields, you may need to make this edit manually using a less-sophisticated tool or choose different options when saving your changes.

.. _using-odk-2-modify-html:

Updating the HTML files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two areas where image information is displayed, one is in the list view, where you can expand or collapse an item, and the other is in the detail view, which is opened when you click or tap on an expanded item in the list view. We will only modify this detail view to report the image direction; a more comprehensive edit would likely also update the expanded item within the list view.

To determine all the HTML files, we can begin with the files referenced in the :file:`properties.csv` file we just finished editing. Looking again at that file, we see three files referenced:

  - :file:`tables/geotagger/html/geo_list.html`
  - :file:`tables/geotagger/html/geo_list_thumbnail.html`
  - :file:`tables/geotagger/html/geo_detail.html`

Each of these files, or the JavaScript within them, might open or reference other files that might need to be updated. The above files are simply the ones we know are reachable. In general, files for displaying table-specific data are under the :file:`config/tables/tableid` directory. In this example, we will just modify the last of these files and its associated JavaScript file.

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

Congratulations, you have successfully modified this ODK 2.0 application to add a new data field and display it as a field in the HTML detail-view page.

You could now log onto your server, delete the geotagger table, reset your server, and start collecting geopoints with the new image direction field.

.. _using-odk-2-next:

Next Steps
-----------------------

The XLSX file format and the supplied prompt types are described in the :doc:`xlsx-converter-intro` documentation. The tools allow arbitrary customization and the definition of new prompt types.
