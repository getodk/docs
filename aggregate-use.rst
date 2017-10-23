********************
Aggregate Usage
********************

ODK Aggregate can be used to collect data from ODK collect, filter the submitted data and export it to useful formats. It provides a mechanism for hosting the survey forms and gathering the survey results. 

When the URL to the ODK Aggregate server is first opened, you will be presented with the application page showing the :guilabel:`Submissions` and :guilabel:`Form Management` tabs. You will also see a :guilabel:`Log In` option and three help buttons.

.. image:: /img/aggregate-use/server-start.*
   :alt: Image showing tabs on Aggregate server.

.. _form-manage:

Form Management
----------------

You can add, download and delete forms, export data into useful formats, publish data into another service, manually upload submissions and view the published data. ODK Aggregate provides all these options under the :guilabel:`Form Management` tab.

.. _create-manage:

Managing forms
~~~~~~~~~~~~~~~~

You can view all your forms, add new forms, delete forms, download forms as well as restrict submissions for a form.

Click on :guilabel:`Forms list` tab to see a list of all your forms.  

.. image:: /img/aggregate-use/form-list.*
   :alt: Image showing list of all forms.

Under the :guilabel:`Form list` tab, you will see :guilabel:`Add New Form` button  to upload a new form definition to ODK Aggregate. 

.. image:: /img/aggregate-use/add-form.*
   :alt: Image showing add form button.

When you click on it a box will open asking for details of the form. :guilabel:`Form Definition` is required and :guilabel:`Media File(s)` is optional. Choose the .xml file that will be used. You can also choose the appropriate media files for the form.  

.. image:: /img/aggregate-use/add-form-options.*
   :alt: Image showing add form options.

You can manage all the forms present on your server in your form list. All options displayed in the form list are as follow:

- Click on :guilabel:`Title` to view the XML for a form. You can then download XML for that form by clicking on :guilabel:`Download XML` in the Form XML Viewer.

.. image:: /img/aggregate-use/xml-viewer.*
   :alt: Image showing xml viewer for form.

- :guilabel:`Form Id` is the unique name for the form.
- :guilabel:`Media Files` displays the count of media files you have uploaded for the form.
- :guilabel:`User` is the user who uploaded the form.
- Clicking on :guilabel:`Downloadable` checkbox enables/disables Aggregate from displaying the form to remote clients so that they can download the form.
- Clicking on :guilabel:`Accept Submissions` checkbox enables/disables Aggregate ability to accept submissions for the particular form. 

.. tip::

  Disable accepting submission by unchecking the :guilabel:`Accept Submissions` checkbox if you want to prevent users from submitting more data for a particular form.

- Click on :guilabel:`Delete` when you want to remove a form.     

.. _export-form:

Exporting form data
~~~~~~~~~~~~~~~~~~~~~~~

Click on :guilabel:`Export` option in the form list to export form into useful formats and choose the format in which you want to export data. You can also choose a filter which you have saved for the form to export only a certain subset of form. Details on :ref:`exporting data <export-data>` are given in the :ref:`data transfer <transfer-data>` section.   

.. _publish-form:

Publishing form data
~~~~~~~~~~~~~~~~~~~~~~
 
Click on :guilabel:`Publish` option in the form list to publish the form into another service. You can choose where you want to publish data and which data you want to publish. Details on :ref:`publishing data <publish-data>` are given in the :ref:`data transfer <transfer-data>` section.

.. _view-publish-data:

Viewing Published data
~~~~~~~~~~~~~~~~~~~~~~~

You can get a view of the published data you have created for a particular form by clicking on :guilabel:`Published Data`. 

.. image:: /img/aggregate-use/published-data.*
   :alt: Image showing published data.

- Select the form corresponding to the published data in the :guilabel:`Form` dropdown.
- Read the message that appears and click on :guilabel:`Purge Published Data`.
- :guilabel:`Created By` shows the email of the user who created the published file.
- :guilabel:`Status` can be `ACTIVE` (the file is ready to view) or `ESTABLISHED` (something went wrong in the process of exporting.)
- :guilabel:`Start Date` shows the time when you finished filling out the :guilabel:`Publish` form.
- :guilabel:`Action` is based on your selection of upload only, stream only, or both in the :guilabel:`Publish` form.
- :guilabel:`Type` shows the type you choose to publish your data to.
- :guilabel:`Owner` shows the owner of the published data.
- :guilabel:`Name` is the place where you published your data. If the type was a Google Fusion Table, click on the link to view the Fusion Table.
- Select delete box in the :guilabel:`Delete` column if you want to delete your published file.     

.. _submission-admin:

Managing Submissions manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can manually upload submissions for a form and check incomplete submissions under the :guilabel:`Submission Admin` tab. Following options are available:

.. image:: /img/aggregate-use/submission-admin.*
   :alt: Image showing submission admin tab.

- Click on :guilabel:`Manually upload submission data` to manually upload submissions.

.. image:: /img/aggregate-use/submission-upload.*
   :alt: Image showing window to manually upload submissions.

.. note::

  Submissions are located under the /odk/instances directory on the phone's sdcard. This directory will contain subdirectories with names of the form: formID_yyyy-mm-dd_hh-MM-ss. Within each of these subdirectories are the submission data file (named: formID_yyyy-mm-dd_hh-MM-ss.xml),and zero or more associated data files for the images, audio clips, video clips, etc. linked with this submission.

- Select form in the :guilabel:`Form` dropdown and click on :guilabel:`Purge Submission Data` if you want remove submission data for a particular form.

- You can also see a list of incomplete submissions for a particular form under the :guilabel:`Incomplete Submissions` list.

.. note::

  If you upload the submission, but fail to upload all media attachments, it places the submission in the incomplete submissions bucket. While it resides there, it won't be published to external servers or downloadable via ODK Briefcase.      


.. _submission-data:

Submissions
--------------

You can view the data submitted from ODK Collect here. You can filter the submissions, visualize them using pie chart, bar graph or map, export the submissions into useful formats and publish the submitted data into another service. You can also view all the exported submissions. ODK Aggregate provides all these options under the :guilabel:`Submissions` tab.

.. _filter-submission:

Filtering Submissions
~~~~~~~~~~~~~~~~~~~~~~~~

Submissions from ODK collect can be filtered to view or hide a specific subset of data by creation of filters. Filters give you the ability to see a subset of your data. You can have a single filter as well as multiple filters. If you have multiple filters applied at once, then you have a filter group. You can create and apply filters by using the options under the :guilabel:`Filter Submissions` tab.

You can create a single or multiple filters depending on the subset of data you want to view or hide. Creating a filter like `Display Rows where column Gender EQUAL male` specifies that you want to get a list of all rows where gender column has value as male i.e you want to obtain information about all male people in your data. Unless the filter is saved, it is temporary. You can save a filter to make it permanent. Any filter can be deleted if it is no longer needed.

Various options under this tab can be used as follows:

- Click on :guilabel:`Add Filter` to add filter to the data. In the :guilabel:`Create filter to` dropdown, :menuselection:`Display` or :menuselection:`Hide` will specify whether you will be selecting data to show or hide and  :menuselection:`Rows` or :menuselection:`Columns` will specify whether you will be working with the rows or columns of the table. 

.. image:: /img/aggregate-use/add-filter.*
   :alt: Image showing add filter option.

If you select :menuselection:`Rows` specify a condition you want to apply in the :guilabel:`where` box. 

.. image:: /img/aggregate-use/row-filter.*
   :alt: Image showing row selection.

If you selected :menuselection:`Columns` specify the columns you wish to display or hide in the :guilabel:`titled` box. 

.. image:: /img/aggregate-use/column-filter.*
   :alt: Image showing column selection.

- Click on :guilabel:`Save` to save the filter or filter group for future use. Clicking on :guilabel:`Save As` allows you to give a name to the filter or filter group.
- Click on :guilabel:`Delete` to delete a filter or filter group.
- You can check the :guilabel:`Display Metadata` checkbox to display or hide metadata.

.. note::

 Metadata provides information about the submissions. There will be information such as date submitted, if the data is complete, version numbers, and id numbers.

.. image:: /img/aggregate-use/filter-options.*
   :alt: Image showing save, save as, delete and display metadata options.


.. _visualize-submissions:

Visualizing Submissions
~~~~~~~~~~~~~~~~~~~~~~~~

ODK Aggregate provides a quick means for basic data visualization. This Visualize functionality is meant to provide a quick means to view early data results in meaningful ways but is not meant to provide complex data analysis functionality. You can view your data in bar graph, pie chart or on a map. 

In both Pie chart and bar graph visualization you can either count the number of times a unique answer occurs in a specified column or calculate sum of values in one column grouped by a value in another column. You can choose a column that you want to map in map visualization.

.. image:: /img/aggregate-use/visualize.*
   :alt: Image showing visualize option.

Click on :guilabel:`Visualize` to visualize the submitted data. Select bar graph, pie chart or map in the :guilabel:`Type` dropdown. Further options are described as follows:

- If you choose Pie Chart, choose whether you would like to count or sum data:

      - If you select :guilabel:`Count` option, then select the column in which you want to apply this.
      - If you select :guilabel:`Sum` option, then select the column of values that you want to add and another column that you want to use to group the numbers. 
      - Then click on :guilabel:`Pie It` to get the Pie Chart.

.. image:: /img/aggregate-use/pie-chart.*
   :alt: Image showing pie chart option.

- If you choose Bar Graph, you have the same options as that in case of Pie Chart. Choose the option you want to use and then click on :guilabel:`Bar It` to get the Bar Graph.

.. image:: /img/aggregate-use/bar-graph.*
   :alt: Image showing bar graph option.

- If you choose Map, select a column that you want to map in the :guilabel:`GeoPoint to Map` dropdown. Click on :guilabel:`Map It` to get the map. You can click on a point to view a balloon with the other information supplied in the table.

.. image:: /img/aggregate-use/map.*
   :alt: Image showing map option.

.. _export-submissions:

Exporting Submissions
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/aggregate-use/export-submission.*
   :alt: Image showing export option.

.. image:: /img/aggregate-use/export-options.*
   :alt: Image showing export window.   

Click on :guilabel:`Export` option to export submitted data into useful formats and choose the format in which you want to export data. You can also choose a filter which you have saved earlier to export only a certain subset of data. Details on :ref:`exporting data <export-data>` are given in the :ref:`data transfer <transfer-data>` section.
  
.. _publish-submissions:  

Publishing Submissions
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/aggregate-use/publish-submission.*
   :alt: Image showing publish option.

.. image:: /img/aggregate-use/publish-options.*
   :alt: Image showing publish window.   

Click on :guilabel:`Publish` option to publish the submitted data into another service. You can choose where you want to publish data and which data you want to publish. Details on :ref:`publishing data <publish-data>` are given in the :ref:`data transfer <transfer-data>` section.  

.. _view-export-data:

Viewing Exported Submissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can to view the list of exported files under the :guilabel:`Exported Submissions` tab.

.. image:: /img/aggregate-use/exported-submission.*
   :alt: Image showing exported submissions.

- :guilabel:`File Type` specifies whether file is :file:`.csv` or :file:`.kml` or :file:`.json` file.
- :guilabel:`Status` will state whether the file being made is in progress, or is now available for viewing.
- :guilabel:`Time Completed` shows the time when the `Export` task is complete and the file is ready.
- Click on the link in :guilabel:`Download File` to see your exported file.
- Select delete box in the :guilabel:`Delete` column if you want to delete your exported file.

.. _site-admin:

Site Admin
------------

Click the :guilabel:`Log In` link in the upper right corner of the screen to be presented with the Log onto Aggregate screen. Choose the :guilabel:`Sign in with Aggregate password` button and enter the super-user username you specified within the installer. The initial password for this account is `aggregate`. When you log in, :guilabel:`Site Admin` will be visible to you.

.. image:: /img/aggregate-use/sign-in.*
   :alt: Image showing sign in option.

.. tip::

   - When signing in with this method, if you do not enter the password correctly, you may need to close all your browser windows and quit your browser before you can try again.
   - If the instance name of the server changes (the installer asks for this name), then the passwords for all ODK Aggregate usernames will be cleared (preventing their use) and the super-user username's password will be reset to aggregate and the above message will also be displayed. In this case, you should log in, change the super-user's password, and change the passwords for all of your ODK Aggregate usernames.
   - In April 2015, the use of Google e-mail accounts for accessing the site (via Sign in with Google) stopped working (Google turned off that functionality).  If you have an existing site running an old version of ODK Aggregate that does not have ODK Aggregate usernames configured for website access (and offers a Sign in with Google sign-in choice), you will need to upgrade to regain access to it.

.. note:: 

 Beginning with ODK Aggregate 1.3.2, upon the initial installation of the server, it is configured to allow unauthenticated (`anonymousUser`) submissions from ODK Collect and unauthenticated browser access to the submissions and forms management functionality of ODK Aggregate.

.. _permission-tab:

Permissions
~~~~~~~~~~~~~

If you have not yet changed your super-user password to something other than `aggregate`, the server will display **This server and its data are not secure! Please change the super-user's password!** at the top of the web page. 

.. image:: /img/aggregate-use/warning.*
   :alt: Image showing server not secure warning.

Please visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to change this user's password.  

.. image:: /img/aggregate-use/permissions.*
   :alt: Image showing permissions sub-tab.

You can specify additional usernames with browser access to the server under the :guilabel:`Permissions` sub-tab. Privileges are as follows:

- **Data Collector**: able to download forms to ODK Collect and submit data from ODK Collect to ODK Aggregate. 

.. note::

   - Only ODK accounts and the anonymousUser can be granted Data Collector rights. 
   - The anonymousUser must be granted Data Collector rights to accept submissions from unidentified sources (e.g., from ODK Collect 1.1.5 and earlier, or from ODK Collect 1.1.7 and later if not authenticating).

- **Data Viewer**: able to log onto the ODK Aggregate website, filter and view submissions, and generate csv or kml files for download.
- **Form Manager**: all the capabilities of a Data Viewer plus the abilities to upload a form definition, delete a form and its data, and upload submissions manually through the ODK Aggregate website.
- **Site Administrator**: all the capabilities of a Form Manager plus the ability to add users, set passwords, and grant these capabilities to other users.

.. image:: /img/aggregate-use/privileges.*
   :alt: Image showing privileges.

Remember to click :guilabel:`Save Changes` to make these changes take effect. You can also edit the privileges for current users.

You can upload a :file:`.csv` file of users and their capabilities as well as download the current file.

.. _preference-tab:

Preferences
~~~~~~~~~~~~

In the :guilabel:`Preferences` sub-tab under :guilabel:`Site Admin` tab, you can manage:

- Google API credentials: These credentials are used when publishing into Google services. For details on this, see :doc:`Aggregate OAuth2 info <oauth2-service>`.

.. image:: /img/aggregate-use/google-api-option.*
   :alt: Image showing google api option.

- **Enketo credentials**: These credentials are used for Enketo webforms integration. To link Enketo with Aggregate, see `this <https://accounts.enketo.org/support/aggregate/>`_.
- **ODK 2.0 App name**
      
   - *ODK Tables Synchronization Functionality* - check this to enable ODK Tables functionality i.e.  able to download, upload and alter data records within ODK Tables as restricted by table-access privileges granted to the user.

- **Aggregate features**: These settings affect the operations of the server.
   
   - *Disable faster background actions* - check this to reduce AppEngine quota usage.
   - *Skip malformed submissions* - check this to ignore corrupted submissions.

.. image:: /img/aggregate-use/preferences-options.*
   :alt: Image showing other options.   


.. _help-options:

Help Options
--------------

Aggregate provides three kinds of help accessible by pressing one of three buttons in the upper righthand corner.

The red question mark will give you instructions for the tab you are currently viewing. When you click the button, a help panel will appear at the bottom of the screen. To hide the help panel, simply click the red question mark again.

.. image:: /img/aggregate-use/question-mark-help.*
   :alt: Image showing question mark help option.

The green book will give you the most comprehensive help. When you click the button, a popup will appear providing detailed information as well as video instructions.

.. image:: /img/aggregate-use/book-help.*
   :alt: Image showing green book help option.

The blue balloon increases the amount of detail that appears describing the button's functionality when you hover over most buttons.

.. image:: /img/aggregate-use/balloon-help.*
   :alt: Image showing blue balloon help option.

.. _transfer-data:

Data Transfer using Aggregate
------------------------------

ODK Aggregate supports three primary mechanisms for data transfer:

- :ref:`Exporting <export-data>`:  one time snapshot
- :ref:`Publishing <publish-data>`: continuous streaming of submissions
- :ref:`APIs <odk-api>`: programmatic access to the data

Since ODK supports complex data structures such as question grouping, repeating questions, and multimedia, compromises have been made for each mechanism in regards to these data structures. This document explains each mechanism and what each supports.

.. _export-data:

Exporting
~~~~~~~~~~

The easiest way to get data from Aggregate is by using its ‘Export’ feature. Export allows the user to manually export all of the data (or filtered data) at any time into one of the following formats:

.. _export-to-csv:

CSV (comma separated values)
"""""""""""""""""""""""""""""

CSV files are a text only, tabular representation of the data. Multimedia files are represented by including standard web links to the files. Repeats are also represented with links to the underlying data. Grouping information is not preserved. Metadata is only preserved if a filter is created with the metadata.

To download CSV files of forms with repeats, consider using ODK Briefcase instead of ODK Aggregate's export functionality. Instead of repeats that are represented with links to the underlying data, ODK Briefcase will export a set of CSV files, one for each repeating group. ODK Briefcase will also export any multimedia as files (e.g., pictures will get exported as JPEGs). The only metadata that is preserved is the submission date in the CSV is preserved, but the XML files that ODK Briefcase downloads has all form metadata.

.. note::

 To import CSVs into Excel, you cannot download and open in one step; nor can you double-click on the CSV. You must open Excel and choose Import. If you are asked, the file origin or encoding is UTF-8.

.. _export-to-json:

JSON
""""""""

JSON is a text only representation of the data in a key:value format. Multimedia files are represented by including standard web links to the files. Repeating data is preserved, but grouping information not related to repeats is not. Metadata is only preserved if a filter is created with the metadata.

.. _export-to-kml:

KML (Keyhole Markup Language)
""""""""""""""""""""""""""""""

KML is a text only representation of the data similar to XML, but used for mapping applications like Google Earth. Multimedia files are represented by including standard web links to the files hosted on the server. Pictures will appear embedded in popup windows (when pushpins are clicked) in programs that render .kml files. Repeats and grouping information is not preserved. Metadata is only preserved if a filter is created with the metadata.

.. csv-table:: **Export Data Summary**
   :header: "Format", "Groups", "Repeats", "Multimedia", "Metadata"
   :widths: auto

   "CSV(Aggregate)", "not preserved", "links to", "links to", "preservable"
   "CSV(Briefcase)", "not preserved", "split into separate CSVs", "exported as files", "only submission date"
   "JSON", "not preserved", "preserved", "links to", "preservable"
   "KML", "not preserved", "not preserved", "links to", "preservable"

.. _publish-data:

Publishing
~~~~~~~~~~~~

Aggregate provides mechanism for either bulk publishing data to another service, or for streaming incoming data to a service as it is received, or both. 

.. warning::

  Under certain failure conditions, the downstream service can receive multiple copies of a given submission. This is known, expected, behavior. 

.. tip::

  - Duplicates typically occur if the downstream service is slow to respond or acknowledge a request. 
  - It is your responsibility to detect and eliminate these duplicates should they occur (they will always have exactly the same information in all fields). 

.. note::

  - If ODK Aggregate aborts its publishing attempt before it gets an acknowledgement, it will re-send the submission a short time later. If the downstream server successfully processed the first request, the re-send of that same submission can cause a duplicate record of it to appear in the downstream system. The instance ID of the submission will appear as the metainstanceid column in Google Sheets and as the *meta-instance-id* column in Google Fusion tables.
  - When the downstream server fails to respond or responds with an error code, ODK Aggregate first delays a re-send for 60 seconds, and, if that also fails, it then backs off its publishing attempts, and will re-send at either 7.5-minute or 15-minute intervals until the downstream service successfully responds, after which ODK Aggregate will resume its normal publishing behavior.  

Aggregate currently supports publishing data to the following services or in the following formats:

.. _fusion-table:

Google Fusion Tables
"""""""""""""""""""""

Fusion Tables is an experimental data visualization web application to gather, visualize, and share larger data tables. Multimedia files are represented by including standard web links to the files. Repeating groups of questions are split into separate tables. All metadata is preserved. Fusion Tables is hosted in Google’s cloud infrastructure. We know of no row limit, but one may exist. Fusion Tables also has an API that can be used to export/publish data.   

.. warning::

  Non-repeating grouping information is not preserved. This implies that if your form has a non-repeating group `purchaser` and a second non-repeating group `supplier` and within each of these groups, you have a `name` field, then when you publish to Fusion Tables, there will be two columns called `name`. Unfortunately, that badly confuses Fusion Tables, and generally results in data not transferring successfully into Fusion Tables. 

.. tip::

  The solution is to the problem in above example is to design your forms with field names like `purchaser_name` and `supplier_name`.

.. _google-spreadsheet:

Google Spreadsheets
"""""""""""""""""""""

Spreadsheets is Google’s cloud-hosted spreadsheet solution. Multimedia files are represented by including standard web links to the files. Repeats are also represented with links to the underlying data. All metadata is preserved. Spreadsheets has a 400,000 cell limit, above which errors will be reported. Spreadsheets also has an API that can be used to export/publish data. Similar to Google Fusion tables, non-repeating grouping information is not preserved.

.. _json-server:

JSON Server
""""""""""""

JSON preserves grouping and repeat structures. The user can choose to let multimedia files be represented as web links or embedded as base64 encoded strings. All metadata is preserved.

.. _google-map-engine:

Google Maps Engine
""""""""""""""""""""

Maps Engine is a cloud-hosted service to easily create and share maps. Multimedia files are represented by including standard web links to the files. Grouping information is preserved in the variable names. Repeating groups are forbidden and submissions must have at least one geopoint. Maps Engine also has an API that can be used to export/publish data.

.. _redcap-server:

RedCap Server
""""""""""""""

RedCap servers ignore grouping and repeating information. Multimedia files are sent as binary form elements in POST.

.. _ohmag-json-server:

Ohmage JSON Server
""""""""""""""""""

Ohmage JSON preserves grouping and repeat structures. Multimedia files are sent as binary form elements in POST.

For more details on JSON Server, RedCap Server and Ohmage JSON Server see `Aggregate Publishers Implementation Details <https://github.com/opendatakit/opendatakit/wiki/Aggregate-Publishers-Implementation-Details>`_

.. csv-table:: **Publish data Summary**
   :header: "Service", "Groups", "Repeats", "Multimedia", "Metadata"
   :widths: auto

   "Google Fusion Tables", "not preserved", "split into separate tables", "links to", "preserved"
   "Google Spreadsheets", "not preserved", "links to", "links to", "preserved"
   "JSON Server", "preserved", "preserved", "links to or embedded as base64", "preserved"
   "Google Maps Engine", "preserved", "forbidden", "links to", "not preserved"
   "RedCap Server", "not preserved", "not preserved", "binary elements in POST"
   "Ohmage JSON Server", "preserved", "preserved", "binary elements in POST" 

.. _odk-api:

APIs
~~~~~   

ODK has public APIs defined for sending data to and from its various components. This section gives references to those API implementations that can be used for connecting new applications to the ODK ecosystem.

.. _briefcase-cli:

Briefcase CLI
""""""""""""""

ODK Briefcase 1.4.4 introduces a new Command Line Interface (CLI) to automate downloading forms from ODK Aggregate (or ODK Collect) and exporting the forms to an Excel-compatible format like CSV. For more details, see :ref:`Working with command line on Briefcase <cli-use>`.

.. _briefacse-aggregate-api:

Briefcase-Aggregate API
"""""""""""""""""""""""""

ODK Briefcase uses an API that external applications can use to pull all data from and push data to ODK Aggregate. 

Interfaces used during pull actions are:

- OpenRosa Form Discovery API
- download forms and media files using URLs form discovery
- ``view/submissionList`` to obtain a chunk of submission keys
- ``view/downloadSubmission`` to download an individual submission

Interfaces used during push actions are:

- ``formUpload`` to upload a form and its media files to ODK Aggregate
- ``view/submissionList`` to obtain a chunk of submission keys   
- OpenRosa Form Submission/Overwite API (with extensions)

For more details, see `Briefcase Aggregate API <https://github.com/opendatakit/opendatakit/wiki/Briefcase-Aggregate-API>`_.

.. _collect-aggregate-api:

Collect-Aggregate API
"""""""""""""""""""""""

Collect and Aggregate define APIs for pulling form information from Aggregate to Collect, and for sending collected form data from Collect to Aggregate.

For details, see these links:

- https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI
- https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI
- https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI

.. _direct-database:

Direct database connection
"""""""""""""""""""""""""""

If you are running on a Tomcat server, you have access to the underlying MySQL or PostgreSQL tables. The structure of those tables are documented at `Aggregate Database Structure <https://github.com/opendatakit/opendatakit/wiki/Aggregate-Database-Structure>`_.

.. warning::

  This is a fragile way to pull data from Aggregate because table structure could change between versions. Moreover, changing any of this data could corrupt your Aggregate install.

.. _media-access:

Accessing Media
~~~~~~~~~~~~~~~~~~

Many of the export and publishing options provide a URL to the media (image, audio or video) without providing the content itself. To enable the viewing (following) of this link without requiring a log-in:

- Go to the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab.
- Check the checkbox for: `Allow anonymous retrieval of images, audio and video data (needed for GoogleEarth balloon displays)`.
- Click the :guilabel:`Save Changes` button.

This allows anyone to view the media files on your server. Even though you are granting anyone access to this information, it is still quite secure because the users would need to have a valid URL.