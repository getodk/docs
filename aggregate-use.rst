********************
Aggregate Usage
********************

.. _general-guide:

General Instructions
-----------------------

.. image:: /img/aggregate-use/general-tabs.*
   :alt: Image showing different tabs in Aggregate Server.

- When the URL to the ODK Aggregate server is first opened, you will be presented with the application page showing the :guilabel:`Submissions` and :guilabel:`Form Management` tabs.

.. note:: 
 Beginning with ODK Aggregate 1.3.2, upon the initial installation of the server, it is configured to allow unauthenticated (`anonymousUser`) submissions from ODK Collect and unauthenticated browser access to the submissions and forms management functionality of ODK Aggregate.

.. tip::
  In April 2015, the use of Google e-mail accounts for accessing the site (via Sign in with Google) stopped working (Google turned off that functionality).  If you have an existing site running an old version of ODK Aggregate that does not have ODK Aggregate usernames configured for website access (and offers a Sign in with Google sign-in choice), you will need to upgrade to regain access to it.

- If you have not yet changed your super-user password to something other than aggregate, the server will display **This server and its data are not secure! Please change the super-user's password!** at the top of the web page. Please visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to change this user's password.  

.. tip::
   - If the :guilabel:`Site Admin` tab is not visible, click the :guilabel:`Log In` link in the upper right corner of the screen to be presented with the Log onto Aggregate screen. Choose the :guilabel:`Sign in with Aggregate password` button and enter the super-user username you specified within the installer. The initial password for this account is `aggregate`. When signing in with this method, if you do not enter the password correctly, you may need to close all your browser windows and quit your browser before you can try again.
   - If the instance name of the server changes (the installer asks for this name), then the passwords for all ODK Aggregate usernames will be cleared (preventing their use) and the super-user username's password will be reset to aggregate and the above message will also be displayed. In this case, you should log in, change the super-user's password, and change the passwords for all of your ODK Aggregate usernames.

- Use the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to specify additional usernames with browser access to the server. For each user you add, select whether they have access to the submitted data (Data Viewer privileges), the ability to upload forms and export or publish data (Form Management), or the ability to manage site access and users (Site Admin) privileges. Remember to click :guilabel:`Save Changes` to make these changes take effect. 

.. image:: /img/aggregate-use/site-admin.*
   :alt: Image showing Site Admin tab.

.. tip::

  - For each username you define, remember to Change Password to assign a password; by default, usernames are created with unusable passwords. 
  - Granting any of these privileges to the anonymousUser enables browser access to these functions without first logging in. When restricting access you must remove these privileges from the `anonymousUser`.

- Aggregate provides three kinds of help accessible by pressing one of three buttons in the upper righthand corner.

   - The red question mark will give you instructions for the tab you are currently viewing. When you click the button, a help panel will appear at the bottom of the screen. To hide the help panel, simply click the red question mark again. 
   - The green book will give you the most comprehensive help. When you click the button, a popup will appear providing detailed information as well as video instructions.
   - The blue balloon increases the amount of detail that appears describing the button's functionality when you hover over most buttons.

  

.. _form-manage-tab:

Form Management
------------------

This section describes various features in the :guilabel:`Form Management` tab. You can manage all your forms here.

.. image:: /img/aggregate-use/form-manage.*
   :alt: Image showing Form Management tab.

.. image:: /img/aggregate-use/xml-viewer.*
   :alt: Image showing XML viewer.

.. image:: /img/aggregate-use/publish.*
   :alt: Image showing publish feature.          

- Click on :guilabel:`Forms list` tab to see a list of all your forms. 

    - Click on :guilabel:`Add New Form` button  to upload a new form definition to ODK Aggregate. `Form Definition` is required and `Media File(s)` is optional. Choose the .xml file that will be used. You can also choose the appropriate media files for the form.  
    - Click on :guilabel:`Title` to view the XML for a form. You can then download XML for that form by clicking on :guilabel:`Download XML` in the Form XML Viewer.
    - :guilabel:`Form Id` is the unique name for the form.
    - :guilabel:`Media Files` displays the count of media files you have uploaded for the form.
    - :guilabel:`User` is the user who uploaded the form.
    - Clicking on :guilabel:`Downloadable` checkbox enables/disables Aggregate from displaying the form to remote clients so that they can download the form.
    - Clicking on :guilabel:`Accept Submissions` checkbox enables/disables Aggregate ability to accept submissions for the particular form. 

    .. tip::

      Disable accepting submission by unchecking the :guilabel:`Accept Submissions` checkbox if you want to prevent users from submitting more data for a particular form.


    - Click on :guilabel:`Publish` when you want to publish your data to:- 

        - Google Fusion table 
        - Google Spreadsheet
        - Z-ALPHA REDCap Server
        - Z-ALPHA JSON Server
        - Z-ALPHA Ohmage JSON Server

        .. tip:: 

         - You can choose whether you want to 

           - `Upload only`:- Take the current table and send it to the the service. No new data will be sent.
           - `Stream only`:- Only send new data after the service is created. No old data is sent.
           - `Both above options`:- Both new and old data is sent. 

        - Press :guilabel:`Grant Access` so that ODK Aggregate is allowed to make the file.  
        - When you click on :guilabel:`Publish` you will be asked to enter an email that will become the owner of the published tables.


    - Click on :guilabel:`Export` when you want to view your data in either Microsoft Excel or a Google Map. You can export your data to:-

       - CSV File
       - KML File
       - JSON File

    - Click on :guilabel:`Delete` when you want to remove a form.      


- Click on :guilabel:`Published Data` to get a view of the published data you have created for a particular form. 
   
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

.. image:: /img/aggregate-use/published-data.*
   :alt: Image showing Published Data tab.     

- The :guilabel:`Submission Admin` tab provides the following features:-

   - :guilabel:`Manually upload submission data` to manually upload submissions.

   .. note::

     Submissions are located under the /odk/instances directory on the phone's sdcard. This directory will contain subdirectories with names of the form: formID_yyyy-mm-dd_hh-MM-ss. Within each of these subdirectories are the submission data file (named: formID_yyyy-mm-dd_hh-MM-ss.xml),and zero or more associated data files for the images, audio clips, video clips, etc. linked with this submission.

   - Select form in the :guilabel:`Form` dropdown and click on :guilabel:`Purge Submission Data` if you want remove submission data for a particular form.

   - You can also see the :guilabel:`Incomplete Submissions` list.

   .. note::

      If you upload the submission, but fail to upload all media attachments, it places the submission in the incomplete submissions bucket. While it resides there, it won't be published to external servers or downloadable via ODK Briefcase.

.. image:: /img/aggregate-use/submission-admin.*
    :alt: Image showing Submission Admin tab.        



.. _submission-tab:

Submissions
--------------

This section describes various features in the :guilabel:`Submissions` tab. You can view the data submitted from ODK Collect here.

.. image:: /img/aggregate-use/filter-submission.*
   :alt: Image showing filter submission tab.

.. image:: /img/aggregate-use/apply-filter.*
   :alt: Image showing Filter creation.   

.. image:: /img/aggregate-use/visualize.*
   :alt: Image showing visulaize feature.         

- Click on the :guilabel:`Filter Submissions` tab to filter and visualize the submitted data.

   - Click on :guilabel:`Add Filter` to add filter to the data.

      - In the :guilabel:`Create filter to` dropdown, `Display/Hide` will specify whether you will be selecting data to show or hide and  `Rows/Columns` will specify whether you will be working with the rows or columns of the table. If you select `Rows` specify a condition you want to apply in the :guilabel:`where` box. If you selected `Columns` specify the columns you wish to display or hide in the :guilabel:`titled` box. Example :- `Display Rows where column Gender EQUAL male` specifies that you wanted to get the list of males over the age of 35. 
      
      - Click on :guilabel:`Save` to save the filter or filter group for future use. Unless the filter is saved, it is temporary. Clicking on :guilabel: `Save As` allows you to give a name to the filter or filter group.
      - Click on :guilabel:`Delete` to delete a filter or filter group.
      - You can check the :guilabel:`Display Metadata` checkbox to display or hide metadata.

      .. note::
       
       - Filters give you the ability to see a subset of your data. 
       - If you have multiple filters applied at once, then you have a filter group.
       - Metadata provides information about the submissions. There will be information such as date submitted, if the data is complete, version numbers, and id numbers.

   - Click on :guilabel:`Visualize` for basic data visualization. This Visualize functionality is meant to provide a quick means to view early data results in meaningful ways but is not meant to provide complex data analysis functionality. You can view your data in bar graph, pie chart or on a map by selecting either of them in the :guilabel:`Type` dropdown.

       - If you choose Pie Chart, choose whether you would like to count or sum data.

          - :guilabel:`Count` option is to count the number of times a unique answer occurs in the specified column. Select the column in which you want to apply this.
          - :guilabel:`Sum` option is to sum up the values in one column grouped together by a value in another column. Select the column of values that you want to add and another column that you want to use to group the numbers. Then click on :guilabel:`Pie It` to get the Pie Chart.

       - If you choose Bar Graph, you have the same options as that in case of Pie Chart. Choose the option you want to use and then click on :guilabel:`Bar It` to get the Bar Graph.

       - If you choose Map, select a column that you want to map in the :guilabel:`GeoPoint to Map` dropdown. Click on :guilabel:`Map It` to get the map. You can click on a point to view a balloon with the other information supplied in the table.
  
   - :guilabel:`Export` and :guilabel:`Publish` provide the same function as discussed in the :ref:`Form Management <form-manage-tab>` section.


- Click on :guilabel:`Exported Submissions` tab to view the list of exported files.

   - :guilabel:`File Type` specifies whether file is :file:`.csv` or :file:`.kml` or :file:`.json` file.
   - :guilabel:`Status` will state whether the file being made is in progress, or is now available for viewing.
   - :guilabel:`Time Completed` shows the time when the "Export" task is complete and the file is ready.
   - Click on the link in :guilabel:`Download File` to see your exported file.
   - Select delete box in the :guilabel:`Delete` column if you want to delete your exported file.

.. image:: /img/aggregate-use/exported-submission.*
   :alt: Image showing exported submission tab.



