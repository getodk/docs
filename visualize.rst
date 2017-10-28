**********************************************************
Visualize Data with Google Fusion Tables and Google Earth
**********************************************************

The importance of location data is continuously increasing, so do the ways through which we can visualize this information. This guide helps the users to visualize the collected data uploaded on ODK Aggregate server using Google Fusion Tables and Google Earth.

Prerequisites
~~~~~~~~~~~~~~~~

1. Make sure you have set up your :doc:`ODK Aggregate server <aggregate-install>`.
2. You should know how :doc:`ODK Collect <collect-guide>` works.
3. You should be familiar with form designers like :doc:`ODK Build <odk-build>`,:doc:`XLSForm <xlsform>` to create your location based forms and upload it to ODK Aggregate server.


Using Google Fusion Tables
----------------------------

:dfn:`Google Fusion Tables` is a web service provided by Google for data management. Fusion tables can be used for visualising dataset on a map.

Follow these steps to view your data using fusion tables:

1. Login to your ODK Aggregate server.
2. In the :guilabel:`Submissions` tab, under :guilabel:`Filter Submissions`, select the form you want to use.

image

.. warning:: 


  1. If you are using Google Cloud Platform make sure you have enabled relevant APIs like **Google Drive API**,**Fusion Tables API**, and Google Maps Javascript API otherwise you may get RequestFailureException error.

  image

  2. To enable the APIs go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner. Click on the three horizontal bars in the top left corner and click on now select :guilabel:`APIs & services` from the menu and then select :guilabel:`Library` option. 

  image

  3. You will be able to see the API Library page, search the APIs in the search bar and click on :guilabel:`Enable`.

  image

6. Click on the :guilabel:`Publish` button.

image

7. In :guilabel:`Publish to` field, choose the platform from drop-down menu to which you want to publish your data, choose Google Fusion Tables. In the :guilabel:`Data to Publish` field, Select the option from the drop-down menu to define what you want to upload:

- :guilabel:`Upload Existing Submission Data Only` will only upload the existing data you already have submitted to your  ODK Aggregate server.
- :guilabel:`Stream New Submission Data Only` can be used if you want new submissions to be automatically entered into Google Fusion Tables.
- :guilabel:`BOTH Upload Existing and Stream New Submission Data` will upload your existing submissions into Fusion Tables and continue automatically adding new submissions to your table.

Choose :guilabel:`BOTH Upload Existing and Stream New Submission Data` and click on :guilabel:`Publish`.

image

8. You will need to enter an email address that will grant access to the documents.
image

9. Check the inbox of the email address that you entered and there would be an email from **odk-oauth2-publishing**, click on :guilabel:`Open`.

image

10. After clicking on :guilabel:`Open` you would be redirected to Google Fusion tables `website <https://fusiontables.google.com/>`_. Here you would be able to see your submissions.

image

11. Select :guilabel:`Map of location` and you should see your data points displayed on a Google Map.
image

.. tip::

  If the points aren't displaying where you expect them to display, visit `Help <https://support.google.com/fusiontables/?hl=en#topic=27020&rd=1>`_ . You can  also customize pop-up balloons in Google Fusion Tables using :guilabel:`Change Info` button under the :menuselection:`Feature map` option.
  
  image
 
 
Using Google Earth
---------------------

:dfn:`Google Earth` is a virtual globe that accesses satellite and aerial imagery, and other geographic data over the internet to represent the Earth as a three-dimensional globe

Follow these steps to view your data using Google Earth:

1. Login to your ODK Aggregate server.
2. In the :guilabel:`Submissions` tab, under :guilabel:`Filter Submissions`, select the form you want to use and click on :guilabel:`Export`

image

3. Choose the type as :file:`KML file` and click on :guilabel:`Export`.

image

4. You don't need to change the default options, but you can select the :menuselection:`title` according to your choice.Click on :guilabel:`Export` 

image

5. You will be redirected to :guilabel:`Export Submissions` page where you can download your kml file.

image

6. After downloading go to `Google Earth website <https://earth.google.com/web/>`_ or you can download it from `here <https://www.google.com/earth/download/gep/agree.html>`_.

img

7. Click on my places icon and to enable KML import click on :guilabel:`Settings`.

img

img

8. In the Settings window, enable KML file import and click on :guilabel:`SAVE`.

img

9. Click on :guilabel:`IMPORT KML FILE` and import the downloaded kml file.

img

10. Now you will be able to see your data in organized manner on Google Earth.

image

.. tip::

  - On Google Earth, you can choose your map style ,add additional points, lines and polygons to add more information for the enhancement of map.
  - If you're looking to do some quick visualisations of a small dataset and aren't too worried about the inherent risks of experimental tools, then you should use Fusion Tables.
  - If you're serious about long-term use of geo data and have large dataset use Google Earth.








