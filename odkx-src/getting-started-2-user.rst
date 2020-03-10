Getting Started User Guide
=====================================

.. _using-odk-2:

A major goal of these ODK-X tools was to eliminate the need for any software engineering skills (for example: Java programming, Android software development environment, source code version control systems) when designing data management applications. The skills required to build a data management application range from scripting a form definition in XLSX (similar to constructing ODK Collect forms using XLSX files processed by the XLSForm tool), to simple web programming -- modifying boilerplate HTML and JavaScript for custom presentations of the collected data. Advanced web programmers can also easily implement entirely custom web pages.

The ODK-X tools are intended to address limitations of the existing tool set. The ODK-X Tool Suite consists of:

- :doc:`survey-intro` - a data collection application based upon HTML, CSS, and JavaScript.
- :doc:`tables-intro` - a data collection and visualization application running on your device.
- :doc:`services-intro` - an application that handles database access, file access, and data synchronization services between all of the ODK-X applications. It also allows you to synchronize data collected by the ODK-X tools using the 2 protocol with an ODK Aggregate instance.
- :doc:`app-designer-intro` - a design environment for creating, customizing, and previewing your forms.
- :doc:`cloud-endpoints-intro` - a ready-to-deploy server and data repository with enhancements to support bi-directional data synchronization across disconnected devices.
- :doc:`suitcase-intro` - a desktop tool for synchronizing data from an ODK-X server so the data can be exported to CSV format.

This page provides a brief end-to-end walk-through of the ODK-X tools. It will cover the following topics:

.. contents:: :local:

.. _using-odk-2-apps:

ODK-X Data Management Applications
----------------------------------------

The ODK-X Android tools (ODK-X Survey, ODK-X Tables, ODK-X Services, ODK-X Scan, ODK-X Sensors Framework, and various ODK-X Sensor implementations) are Android Application Packages (APKs) that are designed to work together to create a coherent tailored application experience for an end-user.

.. note::

  Together the ODK-X tools create a platform, on top of which you can build your own data management applications.

ODK-X tools access configuration files and store data under sub-directories of the :file:`opendatakit` directory in the :file:`sdcard` root directory (whether your device has a physical SD card or not): :file:`/sdcard/opendatakit`. User applications constructed using the ODK-X tools are identified by the name of the sub-directory holding those configuration and data files. Thus, :file:`/sdcard/opendatakit/mytestapp` would contain all the files and data for the *mytestapp* application, where *mytestapp,* is the **AppName** of that application. The default **AppName** for the ODK-X tools is *default.* However, when configured appropriately, the ODK-X tools can run under another **AppName**, accessing configuration and saving data in a different subdirectory under opendatakit.

This is handled in such a way that each user application is isolated from all other user applications, with separate configurations, data tables, and server settings. This allows one device to run multiple user applications built on top of the ODK-X tools without any coordination among the teams developing those applications.

.. _using-odk-2-joining-a-server:

Joining a device to an Existing Aggregate Server
------------------------------------------------------

We will use a Server called Aggregate to get the data for a demo application that we will walk through.

The steps for joining a device to an existing Aggregate server are straightforward.

  #. Install the APKs your application uses.
  #. Launch the *home screen* APK, either ODK-X Survey or ODK-X Tables.
  #. Click on the circular arrows button to launch the ODK-X Services sync activity in the context of your *home screen* APK.
  #. Configure ODK-X Services to point to the ODK Aggregate instance you want to join.
  #. Choose :guilabel:`Sync now` to make the device mirror the contents on that ODK Aggregate server.

Follow the steps described above to join the ODK Aggregate server hosting our simple demo, which uses ODK-X Tables as its *home_screen* APK. The detailed steps are:

  #. Download and install ODK-X Services, ODK-X Tables, and ODK-X Survey.
  #. Launch ODK-X Tables (the *home_screen* APK).
  #. Click on the circular arrows button to launch the ODK-X Services.
  #. The default Sync Configuration should be *https://open-data-kit.appspot.com* and :menuselection:`None (anonymous access)`. You will need to change that. It will also default to :menuselection:`Fully Sync Attachments`.
  #. Click on the gear - shaped button in the menu bar, then select :menuselection:`Server Settings` in the pop-up screen.
  #. Click on :menuselection:`Server URL` and replace the default server with *https://opendatakit-simpledemo.appspot.com* then click :guilabel:`OK`.
  #. Back out of settings then choose :guilabel:`Sync Now`.

The synchronization process will now occur.

.. note::

  If there is an error, check to make sure the server URL is correct, then choose :guilabel:`Sync Now` again until it completes successfully.

Once successful, back out of ODK-X Services, returning to ODK-X Tables. And back out of ODK-X Tables. Then relaunch ODK-X Tables.

.. _using-odk-2-demo-tour:

Tour of the Simple Demo Application
--------------------------------------

You should now see the custom home screen for the *Geotagger* demo:

.. image:: /img/getting-started-2/geo-demo-home.*
  :alt: Geotagging Demo Home
  :class: device-screen-vertical

This demo is based upon the *geotagger* data table and form. It allows users to record the date, time, GPS coordinates, description, and picture of their current location.

When you launch the demo by clicking the blue launch button, you see a map showing the collected data points, indicated with markers. By clicking on a marker, you bring its data record to the top of the list of records above the map. Clicking on the record header will expand or contract that item to show the coordinates and photo of that location. For example, if we click on the *Phinney Ridge* marker, its color changes from blue to green, and, if we then touch the *Phinney Ridge* heading, it expands to show the coordinates and image of that location:

.. image:: /img/getting-started-2/phinney-ridge.*
  :alt: Phinney Ridge
  :class: device-screen-vertical

You can add a new data record by choosing the :guilabel:`+` icon in top menu bar. This opens ODK-X Survey.

.. note::

  Since ODK-X Survey is being opened for the first time, it will initialize itself. This may take a few moments.

.. image:: /img/getting-started-2/geotagger-new-location.*
  :alt: Geotagger New Location
  :class: device-screen-vertical

Advance through and finalize this form. Upon finalizing the form, you will be returned to ODK-X Tables and its map view. You can then highlight the marker you added and view the image in the list view:

.. image:: /img/getting-started-2/geotagger-odk-laboratory.*
  :alt: Geotagger ODK Lab
  :class: device-screen-vertical

If you then click or tap in the list item details area (on the image), a detail view of the item will be displayed.

From here, if you were to choose the pencil icon, ODK-X Survey would be launched to edit this record.

You can also view the data in a list view or spreadsheet view by choosing the sheet icon in the menu bar and selecting the view you want:

.. image:: /img/getting-started-2/view-type.*
  :alt: View Types
  :class: device-screen-vertical

.. tip::

  These other views can be useful if you need to access and complete data records that do not yet have location data and cannot therefore be displayed on a map. Try these other views now.

Now back out of the *geotagger* table view and return to the custom home screen. Choose the three-horizontal-line icon on the top menu bar and choose :menuselection:`Sync`. This opens up ODK-X Services in its sync activity. Sync your device with the server (choose :guilabel:`Sync Noaw`). This will push your newly added record to the server. You can see this by browsing to https://opendatakit-simpledemo.appspot.com click on the :guilabel:`ODK-X Tables` tab, choose the :guilabel:`View Table` sub-tab, and select the *geotagger* table.

If you then repeat these steps with a different device, you can see that the two devices can share and exchange data, and revisions to this data, whenever they synchronize to the server.

.. note::

  During this process, there are two problem-resolution screens you are likely to encounter:

    - :ref:`Checkpoint Resolution <using-odk-2-demo-tour-checkpoints>` - if ODK-X Survey exits without the user explicitly saving their additions or changes.
    - :ref:`Conflict Resolution <using-odk-2-demo-tour-conflicts>` - if ODK-X Services detects a change on the server to a data record that was also changed on the device.

.. _using-odk-2-demo-tour-checkpoints:

Checkpoint Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~

The checkpoint resolution screen can be triggered a variety of ways. For this tour, choose the :guilabel:`+` icon then back out of ODK-X Survey:

.. image:: /img/getting-started-2/checkpoint-resolution.*
  :alt: Checkpoint Resolution
  :class: device-screen-vertical

When presented with this screen, there are three choices:

  - Cancel and continue editing the form.
  - Ignore changes and discard the entire partially filled-out form.
  - Save it even though it is incomplete. In this case, since there is no entered data for this record, we can ignore changes.

In rare cases, a second form of checkpoint resolution screen can be triggered. This most often happens if ODK-X Survey experiences a failure and closes. In this case, you may have several data records with unsaved checkpoint changes (changes that the user has not explicitly saved as incomplete or finalized). This will lead to a screen like:

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

This concludes the tour of the *Geotagger* example application's screens, and the functionality within ODK-X Tables. For larger tours of sample applications, try the :doc:`survey-sample-app` and :doc:`tables-sample-app`.

.. _user-odkx-next:

Next Steps
-----------------------

Users can browse the user guides for the Android tools. Tables and Survey's documentation each guide you through the use of sample application to better familiarize with the workflow of each tool.

  - :doc:`survey-intro`
  - :doc:`tables-intro`
  - :doc:`services-intro`


Those interested in building applications should continue this tour in the :doc:`getting-started-2-architect`.
