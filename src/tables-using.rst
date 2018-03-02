.. spelling::
  Wi
  Fi
  Goodall
  allfields


Using ODK Tables
===================

.. _tables-using:

In this guide we will be demonstrating how to use ODK Tables via a guided tour of the sample application. If you have not installed it yet, follow the instructions for :doc:`tables-install-sample`. However, this guide can also be used as a reference.

.. contents:: :local:

.. _tables-using-custom-home:

Custom Home Screen
-----------------------

ODK Tables allows you to customize the app home screen. If you supply a custom home screen (:file:`config/assets/index.html`), you will have the option of using this as the home screen of the app. This is what is displayed after downloading the demo application.

If there is no custom home screen configured, ODK Tables will display the *Table Manager* view, with the options to add new tables or data via CSVs (the :guilabel:`+` icon), export data to a CSV (the :guilabel:`->` icon), launch ODK Services (the two curved arrows icon), change app-level settings, or view the application version and license information.

From the custom home screen, you can get to the *Table Manager* view by clicking on the icon with three lines at the top right of the menu bar.

To enable or disable the use of the custom home screen, go to the *Table Manager* and click on the :guilabel:`Settings` icon. This will open a screen through-which you can access application-level settings. Click on :menuselection:`Tables-specific Settings` and then check or uncheck the :guilabel:`Use custom home screen` checkbox. This checkbox is only enabled if the :file:`config/assets/index.html` file exists. After making the selection, you will need to fully back out of the ODK Tools and re-launch ODK Tables to have it pick up the change and render the home screen.

The sample application's custom home screen has five tabs. Select the :guilabel:`Tea` tab and click :guilabel:`Launch Demo`. This will display another screen with three buttons. This is a custom layout written in HTML, CSS, and Javascript.

.. note::

  All of these screens and web pages are served directly off of the device -- there is no network access. These are fully able to function in Airplane mode -- without a Wi-Fi or internet connection.

  When you design your applications, you can either have them operate without any network access, or you can write them to access data on the internet. This becomes your design choice.

Click on the :guilabel:`View Tea Houses` button.

.. _tables-using-view-data:

Viewing Data
------------------------

Within ODK Tables, full data sets can be viewed in the following ways:

  - :ref:`List View <tables-using-view-data-list>` -- A list of items, rendered using your own customized HTML and JavaScript. Each item can be selected to display details of that item.
  - :ref:`Spreadsheet View <tables-using-view-data-spreadsheet>` -- A tabular view reminiscent of a Microsoft :program:`Excel` Spreadsheet.

    .. note::

      *Spreadsheet View*, unlike all the other options here, is rendered with Android user interfaces rather than your own customized HTML and JavaScript.

  - :ref:`Map View <tables-using-view-data-map>` -- A pap displaying data points which can be selected to display details of data associated with that data point.

Additionally, the following view options provide alternative methods of viewing data:

  - :ref:`Detail View <tables-using-view-data-detail>` -- A page that shows the details of an individual record. Often used when a single record is selected in a *List View* or a *Map View*.
  - :ref:`Detail with Sublist View <tables-using-view-data-detail-with-list>` -- A hybrid of a *Detail View* and a *List View*, using half the screen for each.
  - :ref:`Graph View <tables-using-view-data-graph>` -- A graphical rendering of data (such as a bar graph or pie chart).
  - :ref:`Navigate View <tables-using-view-data-navigate>` -- A *Map View* that adds a compass and geographic data to help the user navigate to points on the map.

Finally, if your workflow doesn't fit well into the above options, you can create your own :ref:`Custom View <tables-using-view-data-custom>`.

The following sections take you through an example of each type of view from the sample application.

.. _tables-using-view-data-list:

List View
~~~~~~~~~~~~~~~~~

After clicking on the :guilabel:`View Tea Houses` button in the :ref:`custom home screen section <tables-using-custom-home>` you are looking at a *List View* of the *Tea Houses* table. This view is designed entirely in JavaScript and HTML, and we have customized it for the *Tea Houses* table. Click on the lined paper icon at the top of the screen. Here you’ll see all the possible view types. Select :menuselection:`Spreadsheet`.

.. _tables-using-view-data-spreadsheet:

Spreadsheet View
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This takes you to a familiar view as if you were looking at it on a spreadsheet. Each row here represents a tea house, and each was a row in the *List View*. The thin column on the left is called the *status column*: it will show a different color based on the status of that row.

  - White (clear) -- The row is downloaded from the server and has not been modified.
  - Yellow -- The row is modified.
  - Green -- The row is entirely-new row
  - Black -- The row is deleted. It will show as black until you sync with the server and publish those changes.

Select the lined paper icon again, and select :menuselection:`Map`.

.. _tables-using-view-data-map:

Map View
~~~~~~~~~~~~~~~~~~~~~

All the fictional tea houses in Benin appear on the map. Pinch and squeeze or widen to zoom out and in, respectively. The tea house location is plotted based on what appeared in the *Location_latitude* and *Location_longitude* columns in the *Spreadsheet View*. When you click on a map marker, the *List View* will redraw with that marker's information at the top of the *List View*.

Click on an entry and you will be taken to a *Detail with Sublist View*.

.. _tables-using-view-data-detail-with-list:

Detail with Sublist View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tea houses shows individual tea houses using the *Detail with Sublist View*. This renders the screen as a *Detail View* webpage and a subordinate *List View*. In this case, the *Detail View* displays information on the tea house, and the *List View* displays the teas that the tea house serves. Within the *Detail View*, you can scroll down to see the information we decided to display. Like the *List View*, we programmed this using very rudimentary HTML and JavaScript, but it could be customized to look fancier or display additional information.

Scroll to the bottom and you’ll see a link as a number of teas. This is using the information in the table called *Tea Inventory* to tell you how many teas this tea house offers, and has also been defined in the JavaScript.

The subordinate list webpage displays a list of all of these teas. Click on one, and you will now be in a *Detail View* for that tea inventory item.

.. _tables-using-view-data-detail:

Detail View
~~~~~~~~~~~~~~~~~~

The tea inventory *Detail View* displays information about the tea, including whether it is available hot, iced, in bags, or loose leaf. Note that the tea type is being pulled from the *Tea Types* table, but the JavaScript is getting the information from that table to construct our view. Like the other views, we programmed this using very rudimentary HTML and JavaScript, but it could be customized to look fancier or display additional information.

Hit the device’s back button until you are back to the home screen.

.. _tables-using-view-data-graph:

Graph View
~~~~~~~~~~~~~~~~~~~~~~~~~

*List Views* can use JavaScript packages like D3 to render data graphically. Launch the *Plot Demo*, choose :guilabel:`View Plots`, and choose :guilabel:`Puerto Madero` to see a bar graph of corn crop heights across different visits to this farm. That graph was rendered using D3. That library can render scatter plots, line graphs, graphs with error bars and many other visualizations.

.. _tables-using-view-data-navigate:

Navigate View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These views render similarly to the *Map View*, but will use show a compass, bearing, and heading towards a point selected from the map. Back out of the *Plot Demo* and launch the *Geotagger Demo*. From the view options in the upper right, change the selection from *Map View* to *Navigate View* to see the same map of points, but with the navigation user interface replacing the list on the top portion of the screen. Select different points and walk around to see the navigation information update in real time.

.. _tables-using-view-data-custom:

Custom Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The previous view examples cover common workflows. However, any arbitrary web based user interface can be constructed and rendered within Tables. Third party libraries, such as *Math.js* or *Snap.js*, can also be included. See more in the :ref:`App Designer user guide <app-designer-common-tasks-design-view>`.

.. tip::

  These views are not restricted to viewing data. Data can be edited by calling the provided Javascript APIs (see :ref:`Understanding the Web File <app-designer-common-tasks-understanding-web-file>`).

.. _tables-using-view-data-custom-non-form-entry:

Non-form-based data entry
"""""""""""""""""""""""""""""""""

Finally, back out of the *Plot Demo* and choose *JGI*.

The *JGI* (Jane Goodall Institute) demo app is a portion of a chimpanzee interaction tracking app that field researchers can use to record the activities of a designated ("followed") chimp and its interactions with nearby chimpanzees at 15-minute intervals.

Choose :guilabel:`New Follow`. Fill in the form fields, and click :guilabel:`Begin`. And begin recording interactions of this chimp with other known chimps in that group. These fields are all filled-in using hand-written HTML -- not ODK Survey. ODK Survey would be too scripted and confining for this type of dynamic interaction record.

.. note::

  ODK Survey is not necessary for data collection. It is, however, more convenient in most cases.

.. _tables-using-edit-row:

Edit a row with Survey
--------------------------

.. _table-using-edit-row-tea-house:

Simple Example: Tea Houses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch the *Tea Houses* demo again. Follow the directions above to navigate to a *Detail with Sublist View* of a tea house.

At the top of the screen you will see a pencil icon. Click on this to open ODK Survey to edit the row using the *Tea Houses* form. This is possible because that form has been specified as the form to use when editing rows in this table.

.. _table-using-edit-row-hope-study:

Complex Example: Hope Study
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A more complex example of this same flow is in the *Hope Demo*. Back out of the *Tea Houses* demo, back to the custom home screen and select the *Hope Demo* and launch it. Choose :guilabel:`Screen Female Client`. This launches an ODK Survey form for entering a new client into the *Hope Study*. Either complete an entry or back out of that form and choose to :guilabel:`Ignore Changes` to leave ODK Survey without adding a new client.

Choose :guilabel:`Follow Up with Existing Client` to see a *List View* of clients who have already been entered into the study. Choosing one of these displays a *Detail View* that allows you to access client or partner forms for that individual. You can also click on the pencil icon at the top of that *Detail View* screen to launch an ODK Survey form within-which you can view or change any of the information for that client. Clicking on the top right button with the form name opens a drop-down menu from which you can choose :guilabel:`Contents` to see a summary of all the form's fields and their values.

.. _tables-using-geo-tagger:

Another Map example: Geo Tagger
---------------------------------

Another example demo app, *Geotagger*, is also included in the sample application. It contains information and pictures from various places around Seattle. The HTML and JavaScript files associated with this table are slightly more sophisticated, and will give you an idea of the customization you can achieve using Tables.

From the custom home screen, click on the :guilabel:`Geo` tab, and click on the :guilabel:`Launch Demo` button.

This directly opens the *Geotagger* dataset in the *Map View*. The data represent several places around Seattle. Click on :guilabel:`Phinney Ridge`, and the item will expand to give you more information. This more sophisticated behavior is all performed in the JavaScript and HTML file, which you can find in :file:`config/tables/geotagger/html/geo_list.html` as well as :file:`config/tables/geotagger/js/geo_list.js`.

Click on the picture and you’ll be taken to a *Detail View* of the *Phinney Ridge* entry. This *Detail View* is also fancier than those in the :*Tea Time in Benin* example. This file is located in :guilabel:`config/tables/geotagger/html/geo_detail.html`.

Press the device’s back button to go back to the *Map View*. We’re going to add an entry for your current location. Press the plus icon at the top of the screen and you’ll be taken to ODK Survey.

Fill out the form, and at the last screen of the form and press :guilabel:`Finalizer`. You’ll now see your new entry in the list. Navigate to the *Detail View* and you’ll see it works there as well. If you go back to *List View* and change to *Spreadsheet View*, you’ll see it there as well.

.. _tables-using-adding-tables:

Adding Your Own Tables
------------------------------

The creation of data tables is handled within the App Designer. ODK Tables can display and present data, but cannot create Tables on the fly. This enables the ODK Services application to enforce that the configuration of the device (its tables, HTML files, etc.) are identical to those on the server.

.. _tables-using-adding-tables-app-designer:

Initialize from ODK Application Designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the Application Designer documentation for :ref:`designing a form <app-designer-common-tasks-designing-a-form>` to describe a new data table.

.. _tables-using-import-data:

Import Data into a Table from a CSV
-----------------------------------------

This section assumes you have already created the table into which you are importing data.

Once you have created the table, you can load data from a CSV into it by choosing the plus :guilabel:`'+` icon on the *Table Manager* screen.

A CSV is a comma-separated values file. It is a common way to transport tabular data between different programs. Microsoft :program:`Excel` can save and open CSV files, as can :program:`Open Office` and a variety of other programs. Tables expects a certain format of the data in order to import the data correctly: the first line must be the comma-separated list of column names. The remaining lines must be the data for each of the corresponding columns.

For example, assume you wanted to load data into table of people's names, with column (field) names of :th:`Name` and :th:`Age`. In addition to those columns, your CSV file must also specify the unique row id (:th:`instance id`) for each data row (the :th:`_id` column); you can also specify the creator of the row, the time of creation, and other information. But, at a minimum, the file should look like:

.. code-block:: none

  _id,Name,Age
  myUniqueIdforSam,Sam,27

This can be achieved by creating a spreadsheet in a spreadsheet editor and saving it as a CSV, or by copying the above text into a text editor and saving it with a :file:`.csv` extension.

The upload process is as follows:

  #. Place the CSV file onto the device and place it in the :file:`config/assets/csv/` directory with a filename of :file:`tableid.csv`. For example, :file:`/sdcard/opendatakit/default/config/assets/csv/people.csv` would be the CSV file for the *people* table.
  #. Launch ODK Tables and navigate to the *Table Manager* screen.
  #. Press the plus :guilabel:`+` button at the top of the *Table Manager* screen.
  #. Press :guilabel:`Select CSV File to Import`.

    .. note::

      You must have installed OI File Manager from the Play Store.

  #. Find your file, select it, and press :guilabel:`Pick file`.
  #. Press :guilabel:`Append to an Existing Table`.

The data will be read from the file and appended to your data table.

.. warning::

  Prior to any deployment, you should sync your device to your server and export the data table and copy the exported CSV file back on top of the simple CSV file that you created above.

  This ensures that the additional fields required by the ODK tools are properly populated and that a server-managed revision number is added to the data rows so that all devices will have the same internal ids for all of your data rows. This eliminates the possibility of the :file:`tables.init` mechanism introducing duplicate records and speeds the sync process and minimizes the occurrence of conflicts across the devices when these devices first sync to the server.

.. warning::

  Specifying the values for the :th:`_id` column is important. Otherwise, each device, when it loads the CSV file, would assign different unique ids for each of the rows, causing much duplication and confusion.

.. _tables-using-export-data:

Exporting Tables to CSV
----------------------------

You can export any of your tables to a CSV file and associated supporting files. These files will be written to the :file:`output/csv` directory.

A Tables-exported CSV includes all the metadata needed to allow the table to be imported with exactly the same status settings, file associations and metadata settings on another device. Exporting produces the following files:

  - file:`tableid.definition.csv` -- this defines the data table's structure. It specifies the columns and their column types and is a copy of the file found under :file:`config/tables/tableId/`
  - file:`tableid.properties.csv` -- this defines the column heading names, translations, and the HTML files associated with *List Views*, *Detail Views*, *Map Views*, and so on, and is a copy of the file found under :file:`config/tables/tableId/`
  - file:`tableid.csv` -- this holds the data file that you can import to recreate the contents of your data table
  - file:`tableId` -- this holds an instances folder that holds folders named after each row id (the row id is cleaned up to remove any invalid filename characters such as slashes and colons). Each of those folders contains the row-level attachments for that row id.

To export a table:

  #. Launch ODK Tables and navigate to the *Table Manager* screen (if you have a custom home screen, click the icon at the top right with the three increasingly-wide lines).
  #. Press the arrow :guilabel:`->` icon at the top of the *Table Manager* screen.
  #. Select the table you want to export.
  #. Optionally specify a qualifier that will be inserted into the filenames of the emitted files before the :file:`.csv` extension.
  #. Press :guilabel:`Export`.

For example, if you were to export the *geotagger* table and specified *demo* as a qualifier, the following files would be written:

  - :file:`output/csv/geotagger.demo.definition.csv`
  - :file:`output/csv/geotagger.demo.properties.csv`
  - :file:`output/csv/geotagger.demo.csv/geotagger.demo.csv`
  - :file:`output/csv/geotagger/instances/1f9e.../137...jpg`
  - :file:`output/csv/geotagger/instances/...`

.. _tables-using-config-at-startup:

Configuring an App at Startup
-----------------------------------

If you are installing Tables on a new device and don’t have a server set up from which to pull the data (see the :ref:`advanced section about syncing <tables-using-syncing>`, you can alternatively configure Tables to import data at startup. This is useful during forms development, as you can simply push the form definitions, HTML and JavaScript for your application data down to the phone from your computer and launch ODK Tables, and it will load data from CSV files into your data tables.

The configuration file must be titled :file:`tables.init` and placed in the :file:`/sdcard/odk/tables/config/assets` directory. Below is the complete contents of the :file:`tables.init` file distributed with the sample application:

.. code-block:: none

  table_keys=teaHouses, teaTypes, teaInventory, teaHousesEditable, geotagger, plot, plotVisits, femaleClients, maleClients, geopoints, follow
  teaHouses.filename=config/assets/csv/Tea_houses.updated.csv
  teaTypes.filename=config/assets/csv/Tea_types.updated.csv
  teaInventory.filename=config/assets/csv/Tea_inventory.updated.csv
  teaHousesEditable.filename=config/assets/csv/Tea_houses_editable.updated.csv
  geotagger.filename=config/assets/csv/geotagger.updated.csv
  plotVisits.filename=config/assets/csv/visit.example.csv
  plot.filename=config/assets/csv/plot.example.csv
  femaleClients.filename=config/assets/csv/femaleClients.allfields.csv
  maleClients.filename=config/assets/csv/maleClients.allfields.csv
  geopoints.filename=config/assets/csv/geopoints.allfields.csv
  follow.filename=config/assets/csv/follow.updated.csv

The table_keys key contains a comma and space separated list of table keys. Each table key can then have a :file:`.filename` that indicate the filename of the CSV data that should be imported; this file should be under the :file:`config/assets/csv` directory and the name should begin with the **tableId**, followed by an optional qualifier (for example, allfields), and end with :file:`.csv`. If there are row-level file attachments for the table, they would be placed in a **tableId** file within the :file:`csv` directory. Each row-level file attachment filename is relative to the folder for that row's id. If the rows :th:`_id` column was *myUniqueIdForSam*, then the filenames in the data table for row-level attachments for that row would be relative to :file:`/sdcard/opendatakit/default/config/assets/csv/tableId/instances/myUniqueIdForSam/`.

.. note::

  Any table ids appearing in this file must already have their table definitions and metadata values defined in the definition.csv and properties.csv files within their corresponding :file:`config/tables/tableId` directory.

.. tip::

  Only one attempt is made to read and import data at start-up. If that attempt fails, some or all tables may not be initialized or may be partially initialized. You can trigger a re-processing of this file by going to :guilabel:`Settings` and clicking :guilabel:`Reset configuration` then exiting the ODK tool and re-opening it.

As mentioned earlier, this file is never uploaded to the server. After you have created your user application and loaded data onto your device using this mechanism, resetting the app server will push all the configuration files and all of data (the data rows loaded by the :file:`tables.init` script) up to the server (except for this :file:`tables.init` file). Other devices that synchronize with the server will retrieve all of those data rows during the data-row synchronization phase. There is no need for the devices that synchronize with the server to have a copy of the :file:`tables.init` file and independently perform these actions.

.. _tables-using-syncing:

Syncing--Advanced
--------------------------

The final thing you might like to try is synchronizing data to the cloud. See the instructions in the :ref:`ODK Services user guide <services-using-sync>`.
