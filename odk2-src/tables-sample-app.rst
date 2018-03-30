.. spelling::
  geotagging
  prepopulated

ODK Tables: Sample Application
===============================================

.. _tables-sample-app:

In this guide we will be demonstrating how to use ODK Tables via a guided tour of a sample application.

.. _tables-sample-app-prereqs:

Prerequisites
--------------------------------

Install ODK Tables and its prerequisites from the guide:doc:`tables-install`.


.. _tables-sample-app-overview:

Sample Application Overview
--------------------------------

We have provided a sample application to help you acquaint yourself with the various features. This sample app contains five demo apps within it.

  - **Tea Houses** - a fictional Benin Teahouse directory. It provides a broad overall view of the different view types that Tables offers.
  - **Hope Study** - a simplified subset of a perinatal follow-up application that was piloted on ODK Tables and ODK Collect (now converted to use ODK Survey). It demonstrates how Tables and Survey can be integrated.
  - **Plot** - a fictional agricultural field pest- and yield- assessment application. It demonstrates how data can be visualized and actively updated as it is collected on the device.
  - **Geotagger** - a simple geotagging application. It demonstrates a basic customization of the user interface with HTML, CSS, and JavaScript.
  - **JGI** - an app used to track the daily behavior of chimpanzees. It uses a complex, fully customized and domain specific user interface. It also demonstrates Tables collecting data for multiple data tables and rows simultaneously (as opposed to the single row editing of Survey).


.. _tables-sample-app-install:

Install the Sample Application
---------------------------------


Unlike ODK Collect, the ODK 2 tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as is the sample applications provided for :doc:`survey-intro`. This means that you can only deploy one of these sample application at a time onto a device. We also provide :ref:`instructions <survey-launching-appname>` to rename one of these so that two or more applications can co-exist and not interfere with each other on this same device.

We will use the ODK 2 synchronization mechanism to install this app. It is about 26 MB in size and takes a few minutes to download from the web.

  1. Launch ODK Tables. Press the Action Button (:guilabel:`⋮`) and press :menuselection:`Preferences` from the menu.

    .. image:: /img/tables-sample-app/tables-menu-prefs.*
      :alt: Tables Setting Button
      :class: device-screen-vertical

  2. Follow the :ref:`services-managing-server-config` instructions to set up your server.

    - Set your :guilabel:`Server URL` to :file:`https://opendatakit-tablesdemo.appspot.com`.

      .. note::

        The server URL starts with :file:`https://` not :file:`http://`. Don't forget to include the *s*.

    - Leave your authentication as :guilabel:`None (anonymous access)`.

  3. Back out until you return to Tables.
  4. Follow the :ref:`services-using-sync` instructions (see :ref:`launching from Tables <services-using-sync-launch-other>`).

    - Again, leave your user as :menuselection:`None (anonymous access)`.
    - Leave the file attachment setting to :menuselection:`Fully Sync Attachments`

After synchronization is complete, your device's configuration will exactly match that of the server. This includes both collected data and application level files (such as form definitions and HTML files). If you had nothing on your device before, your device will be populated with this data and these application files. If you already had files on this device in this application namespace they will be updated to match the server version. Any local configuration files for data tables or forms that are not present on the server will be removed from your device. Everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server.

Once the configuration and data on the device is an exact match to that of the server, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful. This will not overwrite or hurt anything to do multiple synchronizations in a row.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the Services, returning to Tables.

If the sync was successful, ODK Tables will scan through the downloaded configuration, updating its list of available forms.

  .. image:: /img/tables-sample-app/tables-sample-scan.*
    :alt: Tables Update Configuration
    :class: device-screen-vertical

After this configuration is set up, ODK Tables should now present a custom home screen with five tabs, one for each of the demos. If it does not, back out of ODK Tables and re-launch it.


.. _tables-sample-app-installing-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~~~~~~

For instructions on installing your own Tables application to a device, view the :ref:`app-designer-common-tasks-move-to-device` guide.


.. _tables-sample-app-custom-home-screen:

Custom Home Screen
-----------------------

Open Tables. If you have successfully installed the sample application, you should be presented with a custom home screen showing the five demo apps.

  .. image:: /img/tables-sample-app/tables-sample-home.*
    :alt: Tables Sample Application Home
    :class: device-screen-vertical

Tables allows your organization to customize the home screen of your Data Management Application. By default Tables will only show a list of the data tables defined on the device (called the *Table Manager*). But with a custom home screen your organization can implement their own complex workflow and look-and-feel with HTML, CSS, and JavaScript. An example of this is what is displayed after downloading the sample application.

.. note::

  All of these screens and web pages are served directly from the device -- there is no network access. These are fully able to function in Airplane mode -- without a WiFi or internet connection.

  When you design your applications, you can either have them operate without any network access, or you can write them to access data on the internet. This becomes your design choice.


Each tab on this screen is the home page for one of the five demo applications listed above.

.. note::

  For this example we have included all five applications under the same AppName. However, typically you would give them each their own AppName to provide a clean separation of data.

.. _tables-sample-app-custom-home-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~~~~~~

For more information about custom home screens, view the :ref:`tables-using-custom-home` guide.


.. _tables-sample-app-tea-houses:

Tea Houses Demo
--------------------

For this portion of the tutorial we will explore the *Tea Houses* demo. Select the tab labeled :guilabel:`Tea` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-tea.*
    :alt: Launch Tea Houses
    :class: device-screen-vertical

The *Tea Houses* demo is a fictional collection of Tea Houses in Benin and the teas they offer.

.. _tables-sample-app-custom-view:

Custom View
~~~~~~~~~~~~~~~~~~~~~~

The first screen you will see after launching the *Tea Houses* demo is a custom view.

  .. image:: /img/tables-sample-app/tables-sample-tea-custom.*
    :alt: Tea Houses Custom Navigation
    :class: device-screen-vertical

As with the custom home screen, this custom view is rendered entirely in HTML, CSS, and JavaScript defined within the *Tea Houses* demo. It does not collect or present data, it acts as a navigation screen to allow the user to choose which of the three data set to interact with.

Custom views are not limited to navigation and workflow interfaces. They can also be used to view data, create data visualizations, and modify data in the database. The :ref:`tables-sample-app-plot` and :ref:`tables-sample-app-jgi` explore this more fully.

Press the button labeled :menuselection:`View Teas` to launch the *List View* of the available teas.

.. _tables-sample-app-custom-view-learn-more:

Learn More
""""""""""""""""""

For more information about custom views, view the :ref:`tables-using-view-data-custom` guide.


.. _tables-sample-app-list-view:

List View
~~~~~~~~~~~~~~~~~

  .. image:: /img/tables-sample-app/tables-sample-tea-list.*
    :alt: Tea Houses List View
    :class: device-screen-vertical

This screen shows a list of all teas available in the *Tea Inventory* data table. This view is customized with HTML, CSS, and JavaScript. It provides a simple way to view and navigate collected data. As new teas are added to the inventory, this list view will grow.

To see the raw data, we will switch to *Spreadsheet View*. Tap on the lined paper icon at the top of the screen. Here you’ll see all the possible view types. Select :menuselection:`Spreadsheet`.

  .. image:: /img/tables-sample-app/tables-sample-launch-spreadsheet.*
    :alt: Tea Houses Launch Spreadsheet View
    :class: device-screen-vertical

.. _tables-sample-app-list-view-learn-more:

Learn More
"""""""""""""""""""

For more information about *List Views*, view the :ref:`tables-using-view-data-list` guide.

.. _tables-sample-app-spreadsheet-view:

Spreadsheet View
~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/tables-sample-app/tables-sample-spreadsheet.*
    :alt: Tea Houses Spreadsheet View
    :class: device-screen-vertical

This view renders a full data table from the database, including all rows and columns. Unlike the views we have seen so far, this view is NOT customized via HTML, CSS, and JavaScript. This view is provided by the ODK 2 platform for convenience in viewing and editing your data directly. It is meant to be a familiar view as if you were looking at it on a spreadsheet program, such as :program:`Excel`. Each row here represents a tea, and each was a row in the *List View*.

Return to the *List View* by using the lined paper icon as before and selecting :menuselection:`List`. Tap the :menuselection:`Stonehouse` tea to launch a *Detail View* for that tea.

.. _tables-sample-app-spreadsheet-view-learn-more:

Learn More
"""""""""""""""""

For more information about *Spreadsheet View*, view the :ref:`tables-using-view-data-spreadsheet` guide.

.. _tables-sample-app-detail-view:

Detail View
~~~~~~~~~~~~~~~~

  .. image:: /img/tables-sample-app/tables-sample-tea-detail.*
    :alt: Tea Houses List View
    :class: device-screen-vertical

This screen shows all the details of the *Stonehouse* tea entry in the *Tea Inventory* table. The *Tea Inventory* table's *Detail View* displays information about the tea, including whether it is available hot, iced, in bags, or loose leaf. Note that the tea type is being pulled from the *Tea Types* table, but the JavaScript is getting the information from that table to construct our view. Like the other views, we programmed this using rudimentary HTML and JavaScript, but it could be customized to look fancier or display additional information.

Next we will see a combination of the detail and list view options. Back out until you hit the custom view with the three buttons. .. _tables-sample-app-detail-view-learn-more:

.. _tables-sample-app-detail-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Detail Views*, view the :ref:`tables-using-view-data-detail` guide.


.. _tables-sample-app-detail-sublist-view:

Detail With Sublist View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the custom view with the three buttons, select :guilabel:`View Tea Houses`. This will launch another *List View*, this time showing the list of tea houses.

  .. image:: /img/tables-sample-app/tables-sample-tea-houses-list.*
    :alt: Tea Houses List View
    :class: device-screen-vertical

The *Tea Houses* table has been configured to use a *Detail With Sublist View* rather than a *Detail View*. Tap the :guilabel:`Tea for All` tea house to see this.

  .. image:: /img/tables-sample-app/tables-sample-tea-detail-sublist.*
    :alt: Tea Houses Detail With Sublist View
    :class: device-screen-vertical

This screen contains a *Detail View* webpage and a subordinate *List View*. In this case, the *Detail View* displays information on the tea house, and the *List View* displays the teas that the tea house serves. Within the *Detail View*, you can scroll down to see the information we decided to display. It is also written in HTML, CSS, and JavaScript to render these table entries. The look-and-feel is similar to the *Tea Inventory* only because that is how we coded it. Like the *List View*, we programmed this using very rudimentary HTML and JavaScript, but it could be customized to look fancier or display additional information.

Scroll to the bottom of the *Detail View* portion of the screen and you’ll see a link as a number of teas. This is using the information in the table called *Tea Inventory* to tell you how many teas this tea house offers, and has also been defined in the JavaScript.

The bottom half of the screen renders the subordinate *List View*, which shows the list of teas available at the *Tea for All* teahouse. It is a separate page that is controlled by the top half.

.. note::

  This is a simple example that has a static list. However, you could dynamically change the list that is rendered with controls in the JavaScript for the top half of the screen. For example, you could have a household detail on top, and list all family members on the bottom. You could then provide a button to change the list to only show adult family members in the list below.


Next we will see the *Map View*. Back out of the *Detail With Sublist View* to see the list of tea houses. Press the lined paper icon and choose :menuselection:`Map` from the menu.

  .. image:: /img/tables-sample-app/tables-sample-map-launch.*
    :alt: Tea Houses Launch Map View
    :class: device-screen-vertical

.. _tables-sample-app-detail-with-sublist-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Detail With Sublist Views*, view the :ref:`tables-using-view-data-detail-with-list` guide.

.. _tables-sample-app-map-view:

Map View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/tables-sample-app/tables-sample-map.*
    :alt: Tea Houses Map View
    :class: device-screen-vertical

All the fictional tea houses in Benin appear on the map. Pinch and squeeze or widen to zoom out and in, respectively. The tea house location is plotted based on what appeared in the *Location_latitude* and *Location_longitude* columns in the database. These can be viewed with the :ref:`tables-sample-app-spreadsheet-view`. When you click on a map marker, the *List View* will redraw with that marker's information at the top of the *List View*.

The *List View* at the top portion of the screen is rendered in custom HTML, CSS, and JavaScript, but the map portion is provided by the ODK 2 platform and rendered using :program:`Google Maps`.

.. _tables-sample-app-map-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Map Views*, view the :ref:`tables-using-view-data-map` guide.

.. _tables-sample-app-edit-with-survey:

Edit Row With Survey
~~~~~~~~~~~~~~~~~~~~~~~~~

The final portion of the *Tea Houses* demo will be to edit data with Survey. Return to the *List View* by using the lined paper icon as before and selecting :menuselection:`List`. Tap the :menuselection:`Tea for All` tea house to launch a *Detail With Sublist View* for that tea. Tap the pencil icon in the upper right.

  .. image:: /img/tables-sample-app/tables-sample-tea-detail-sublist-edit.*
    :alt: Tea Houses Launch Survey
    :class: device-screen-vertical

This will launch Survey to edit the *Tea for All* row in the *Tea Houses* data table.

  .. image:: /img/tables-sample-app/tables-sample-survey-launch.*
    :alt: Tea Houses Survey Tea for All
    :class: device-screen-vertical

This Survey form allows you to edit any and all of the data fields in the *Tea for All* entry. Navigate to the question that reads:

  *Which tea is the house specialty*

  .. image:: /img/tables-sample-app/tables-sample-survey-edit.*
    :alt: Tea Houses Survey Tea for All Edit
    :class: device-screen-vertical

Change the specialty to be Herbal. Complete the form and finalize the changes. When you return to the *Tea for All* detail page you will see the house specialty has been updated to Herbal.

  .. image:: /img/tables-sample-app/tables-sample-update-value.*
    :alt: Tea Houses Updated Value
    :class: device-screen-vertical

Similarly, this action can be taken from a *List View* by using the :guilabel:`+` button in the upper right.

Tables and Survey are built to integrate seamlessly. Data can be visualized in Tables and edited in Survey, with your organizations complex workflow moving between as needed. A more complex example of this will be shown later in this tutorial with the :ref:`tables-sample-app-hope`.

.. note::

  Survey is often the easiest way to edit data. However, Tables offers JavaScript APIs to directly edit data through your own custom user interfaces.


This concludes the *Tea Houses* demo. Next we will open the *Geotagger* Demo.

.. _tables-sample-app-edit-survey-learn-more:

Learn More
"""""""""""""""""""""

For more information about launching Survey from Tables, view the :ref:`tables-using-edit-survey` guide.

.. _tables-sample-app-geotagger:

Geotagger Demo
---------------------

For this portion of the tutorial we will explore the *Geotagger* demo. Select the tab labeled :guilabel:`Geo` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-geo.*
    :alt: Launch Geotagger
    :class: device-screen-vertical

The *Geotagger* demo is a mapping of sites around the city of Seattle (and anywhere else anyone has recorded and uploaded to the server).

.. _tables-sample-app-navigate-view:

Navigate View
~~~~~~~~~~~~~~~~~~~~~

After launching the *Geotagger* demo app, you will see a *Map View* of the points in Seattle, or possibly a larger space. To switch to *Navigate View*, tap the lined paper icon in the upper right and choose :menuselection:`Navigate`.

  .. image:: /img/tables-sample-app/tables-sample-launch-navigate.*
    :alt: Launch Navigate
    :class: device-screen-vertical

You will see the same map on the bottom portion of the screen, but the top will be replaced by a compass and heading readouts.

  .. image:: /img/tables-sample-app/tables-sample-navigate-no-point.*
    :alt: Tables Sample Navigate View
    :class: device-screen-vertical

As you turn the compass should update. If you select a point, the compass will add an arrow pointing towards the selected point from your current orientation. The :guilabel:`Distance` and :guilabel:`Heading` values should fill in as well, and update as you move around.

  .. image:: /img/tables-sample-app/tables-sample-navigate-point.*
    :alt: Tables Sample Navigate View
    :class: device-screen-vertical

The *Navigate View* can be useful if you have loaded geopoints into your database (either preloaded or collected in the field) and you need to find your way to these points. It can be integrated into other workflows to navigate a worker to a point and then launch them into another data collection activity.

.. tip::

  The *Geotagger* demo also has a more complex *Map View* example. If you select *Map View* and tap on a map marker, that location will be highlighted in the *List View* on the top of the screen and it will expand to give you more information about it. This more sophisticated behavior is all performed in the JavaScript and HTML files.

Next launch the *Plot* Demo.

.. _tables-sample-app-navigate-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Navigate View*, view the :ref:`tables-using-view-data-navigate` guide.


.. _tables-sample-app-plot:

Plot Demo
---------------------

For this portion of the tutorial we will explore the *Plot* demo. Select the tab labeled :guilabel:`Plot` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-plot.*
    :alt: Launch Plot Demo
    :class: device-screen-vertical

The *Plot* demo is a fictional collection of crop data and graphs of that data.

.. _tables-sample-app-graph-view:

Graph View
~~~~~~~~~~~~~~~~~~~~~

After launching the *Plot* demo app, you will see a custom view that lets you select which crop data you want to see. Choose :guilabel:`View Plots`.

  .. image:: /img/tables-sample-app/tables-sample-plot-chooser.*
    :alt: Tables Sample Plot Selection
    :class: device-screen-vertical

The next screen is a *Map View* of the different sites in the records.

  .. image:: /img/tables-sample-app/tables-sample-plot-map.*
    :alt: Tables Sample Plot Map View
    :class: device-screen-vertical

Each site is meant to represent an area where crop growth and health is being tracked. This provides a convenient view of the locations of the sample sites, and would be a good use for the *Navigation View* if a user had trouble finding one of the sites. Choose the :menuselection:`Ungoni` site.

  .. image:: /img/tables-sample-app/tables-sample-plot-graph-original.*
    :alt: Tables Sample Plot Graph View
    :class: device-screen-vertical

The screen shows a *Graph View* of the crop height data collected for the *Ungoni* site. The bar graph shows corn crop heights across three different visits to this farm.

.. tip::

  The graph was rendered using the :program:`D3` JavaScript library. That library can render scatter plots, line graphs, graphs with error bars, and many other visualizations.

.. _tables-sample-app-graph-update:

Updated Graph View
""""""""""""""""""""""""""

The graph was rendered on the device based on collected data. If new data is collected this graph will be updated. To demonstrate that, let's perform a new visit. Scroll down the page and press the :guilabel:`New Visit` button.

  .. image:: /img/tables-sample-app/tables-sample-plot-graph-new-visit.*
    :alt: Tables Sample Plot New Visit
    :class: device-screen-vertical

This will launch Survey to a form that the *Plot* application specified. Advance through the form. Notice that some of the fields are prepopulated, such as the plot being observed. Be sure to leave that set to :menuselection:`Ungoni`.

When you reach the prompt asking for crop height, enter: `130`.

  .. image:: /img/tables-sample-app/tables-sample-plot-survey.*
    :alt: Tables Sample Plot Survey
    :class: device-screen-vertical

Advance through the rest of the form, entering any data you like. Finalize the changes. When you return to the *Graph View* notice that a new visit has been added to the graph.

  .. image:: /img/tables-sample-app/tables-sample-plot-updated.*
    :alt: Tables Sample Plot Updated
    :class: device-screen-vertical

Tour the rest of the *Plot* demo to see a variety of other *Graph Views*. These are all rendered in custom JavaScript, and could be customized to your organization's unique needs.

Next launch the *JGI* Demo to see a demo of data collection directly through Tables.

.. _tables-sample-app-graph-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Graph View*, view the :ref:`tables-using-view-data-graph` guide.


.. _tables-sample-app-jgi:

JGI Demo
---------------------

For this portion of the tutorial we will explore the *JGI* demo. Select the tab labeled :guilabel:`JGI` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-jgi.*
    :alt: Launch JGI Demo
    :class: device-screen-vertical

The *JGI* demo is a prototype of an application used by the *Jane Goodall Institute* to collect information about Chimpanzee behavior in the field.

.. _tables-sample-app-non-form-data:

Non-Form-Based Data Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After launching the *JGI* demo app, you will see a custom view where you can choose to continue or start a new :guilabel:`Follow`. Choose :guilabel:`New Follow`.

  .. image:: /img/tables-sample-app/tables-sample-jgi-nav.*
    :alt: Tables Sample JGI New Follow
    :class: device-screen-vertical

The next screen will prompt you to enter data about the *Follow* you are about to perform.

  .. image:: /img/tables-sample-app/tables-sample-jgi-metadata.*
    :alt: Tables Sample JGI New Follow Data
    :class: device-screen-vertical

Note that we haven't launched Survey, this data is being collected by custom fields written in HTML, CSS, and JavaScript and rendered directly in the Tables view. Additionally, this data is not being used to create a single row in a single data table, it is going to be used by the following screen's JavaScript code to write to multiple rows in multiple data tables.

When you have filled in these data fields, press :guilabel:`Begin`. This will show start the *Follow* workflow.

  .. image:: /img/tables-sample-app/tables-sample-jgi-follow.*
    :alt: Tables Sample JGI Follow Screen
    :class: device-screen-vertical

This screen is hard not intuitive for a new user to understand. It is highly customized to the specifications of the *Jane Goodall Institute's* workflow. They originally used large paper notebooks with grids. They would check boxes on the grid based on observed chimpanzee behavior according to their own data collection protocols. This screen renders that same grid digitally and gives a worker access to dozens of fields simultaneously. Survey, Collect, or other form based data entry models would be too scripted and confining for this type of dynamic interaction record. Furthermore, this screen will advance to a new data point every 15 minutes. This is another workflow necessity that is only possible because of customized JavaScript.

Finally launch the *Hope* Demo.

.. _tables-sample-app-non-form-data-learn-more:

Learn More
"""""""""""""""""""""

For more information about customized forms of data entry, view the :ref:`tables-using-edit-custom` guide.

.. _tables-sample-app-hope:

Hope Demo
---------------------

For this portion of the tutorial we will explore the *Hope* demo. Select the tab labeled :guilabel:`Hope` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-hope.*
    :alt: Launch Hope Demo
    :class: device-screen-vertical

The *Hope* demo is a complex, longitudinal medical survey involving mothers with HIV.

.. _tables-sample-app-integrate-with-survey:

Integrate With Survey
~~~~~~~~~~~~~~~~~~~~~~~~~

After launching the *Hope* demo app, you will see a custom view that lets you choose whether you are visiting with a new client or following up with an existing client. This study involves multiple visits from the same patient that occur over a period of months during and after the mother's pregnancy. Let's imagine that a client with ID number *44176* has come in for a 6 week follow up visit.

Select :guilabel:`Follow Up with Existing Client`.

  .. image:: /img/tables-sample-app/tables-sample-hope-nav.*
    :alt: Tables Sample Hope Naviation Screen
    :class: device-screen-vertical

This will open a *List View* that shows all the registered clients in the system (registered using the :guilabel:`Screen Female Client` option from the previous screen).

  .. image:: /img/tables-sample-app/tables-sample-hope-list.*
    :alt: Tables Sample Hope Client List
    :class: device-screen-vertical

On the top of the screen is a search field that is custom written in HTML, CSS, and JavaScript. Use this to enter the client ID of the patient we imagine to be interviewing: *44176*. After pressing :guilabel:`Search` the desired client should be visible.

  .. image:: /img/tables-sample-app/tables-sample-hope-search.*
    :alt: Tables Sample Hope Search Results
    :class: device-screen-vertical

Select client *44716* to see a *Detail View* of that patient.

  .. image:: /img/tables-sample-app/tables-sample-hope-detail.*
    :alt: Tables Sample Hope Client Detail
    :class: device-screen-vertical

This page is a *Detail View*, but most of the collected data about this patient is not shown. Instead, links to the follow up Survey forms are provided to make follow up visits run smoothly. If you needed to update the patient's information, you could tap the pencil icon in the top right to launch the Survey form containing all of that patient's data.

Tap :guilabel:`Client Forms` and choose :guilabel:`Six Week Follow-Up`. This will launch the Survey to the specific form containing the six week follow-up questionnaire.

  .. image:: /img/tables-sample-app/tables-sample-hope-six-weeks.*
    :alt: Tables Sample Hope Six Week Follow Up Survey
    :class: device-screen-vertical

This demo imitates a single visit. Next you can try to emulate the full length of the study for a single patient from the initial screening through all the follow up visits. Notice that the *Graph Views* will update with this new information as well.

.. _tables-sample-app-hope-edit-survey-learn-more:

Learn More
"""""""""""""""""""""

For more information about integrating Survey and Tables, view the :ref:`tables-using-edit-data` guide.


.. _tables-sample-app-explore:

Explore the Sample Application
---------------------------------

This concludes the guided tour of the sample application for Tables. However, this is far from a complete reference. Please continue to explore the demo applications to learn more about the tool's capabilities.

You can find a more detailed user guide for Tables here: :doc:`tables-using`. And you can find a more detailed guide to managing Tables for Deployment Architects here: :doc:`tables-managing`. You can also find the source code for the demo applications in this tutorial in the Github repository for `App Designer <https://github.com/opendatakit/app-designer/>`_.

