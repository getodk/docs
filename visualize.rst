**********************************************************
Visualize Data with Google Fusion Tables and Google Earth
**********************************************************

The importance of location data is continuously increasing, so do the ways through which we can visualize this information. This guide helps the users to visualize the collected data uploaded on ODK Aggregate server using Google Fusion Tables and Google Earth.

.. _visual-prerequisites:  

Prerequisites
~~~~~~~~~~~~~~~~

1. Make sure you have set up your :doc:`ODK Aggregate server <aggregate-install>`.
2. You should know how :doc:`ODK Collect <collect-guide>` works.
3. You should be familiar with form designers like :doc:`ODK Build <odk-build>`, :doc:`XLSForm <xlsform>` to create your location based forms and upload it to ODK Aggregate server.

.. _use-google-fusion: 
 
Using Google Fusion Tables
----------------------------

:dfn:`Google Fusion Tables` is a web service provided by Google for data management. Fusion tables can be used for visualizing dataset on a map.

Follow these steps to view your data using fusion tables:

1. Login to your ODK Aggregate server.
2. In the :guilabel:`Submissions` tab, under :guilabel:`Filter Submissions`, select the form you want to use.

.. image:: /img/visualize/aggregate-form.*
  :alt: Image showing location-based form

.. warning:: 


  1. If you are using Google Cloud Platform make sure you have enabled relevant APIs like **Google Drive API**, **Fusion Tables API**, **and Google Maps Javascript API** otherwise you may get *RequestFailureException error*.

  .. image:: /img/visualize/error.*
    :alt: Image showing an error message.

  |
  
  2. To enable the APIs go to `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner. Click on the three horizontal bars in the top left corner, now select :guilabel:`APIs & services` from the menu and then select :guilabel:`Library` option. 

  .. image:: /img/visualize/google-cloud.*
    :alt: Image showing API and services option.
  
  |
    
    
  3. You will be able to see the API Library page.
  
  .. image:: /img/visualize/api-library.*
    :alt: Image showing API Library.
    
  |    
    
  4. Search the APIs in the search bar.
  
  .. image:: /img/visualize/search-api.*
    :alt: Search box
  
  |
  
  5. Click on :guilabel:`Enable`.
  
  .. image:: /img/visualize/fusion-api.*
    :alt: Image showing how to enable API.
  
  
6. Click on the :guilabel:`Publish` button.

.. image:: /img/visualize/publish-form.*
  :alt: Image showing Publish button.

7. In :guilabel:`Publish to` field, choose the platform from the drop-down menu to which you want to publish your data, choose Google Fusion Tables. In the :guilabel:`Data to Publish` field, Select the option from the drop-down menu to define what you want to upload:

- :guilabel:`Upload Existing Submission Data Only` will only upload the existing data you already have submitted to your  ODK Aggregate server.
- :guilabel:`Stream New Submission Data Only` can be used if you want new submissions to be automatically entered into Google Fusion Tables.
- :guilabel:`BOTH Upload Existing and Stream New Submission Data` will upload your existing submissions into Fusion Tables and continue automatically adding new submissions to your table.

Choose :guilabel:`BOTH Upload Existing and Stream New Submission Data` and click on :guilabel:`Publish`.

.. tip::
  
  If you choose :guilabel:`BOTH Upload Existing and Stream New Submission Data` option, you would be able to create a link between your data in Google Earth and 
  Google Fusion Tables, for more information, refer this `link <https://support.google.com/fusiontables/answer/171215?hl=en>`_.

.. image:: /img/visualize/publish-form2.*
  :alt: Image showing options for publishing data.

8. You will need to enter an email address and that email address will be granted access to the documents.

.. image:: /img/visualize/email-prompt.*
  :alt: Image showing prompt for email.

9. Check the inbox of the email address that you entered and there would be an email from **odk-oauth2-publishing**, click on :guilabel:`Open`.

.. image:: /img/visualize/email.*
  :alt: Image showing email from odk-oauth2.

10. After clicking on :guilabel:`Open` you would be redirected to Google Fusion tables `website <https://fusiontables.google.com/>`_. Here you would be able to see your submissions.

.. image:: /img/visualize/data.*
  :alt: Image showing submissions.

11. Select :guilabel:`Map of location` and you should see your data points displayed on a Google Map.

.. image:: /img/visualize/map.*
  :alt: Image showing data point.

.. tip::

  If the points aren't displaying where you expect them to display, visit `Help <https://support.google.com/fusiontables/?hl=en#topic=27020&rd=1>`_ . You can also customize pop-up balloons in Google Fusion Tables using :guilabel:`Change info window` button under the :menuselection:`Feature map` option.
  
  .. image:: /img/visualize/feature-info.*
    :alt: Image showing Change Info button.
  
 .. _use-google-earth:  
 
Using Google Earth
---------------------

:dfn:`Google Earth` is a virtual globe that accesses satellite and aerial imagery, and other geographic data over the internet to represent the Earth as a three-dimensional globe

Follow these steps to view your data using Google Earth:

1. Login to your ODK Aggregate server.
2. In the :guilabel:`Submissions` tab, under :guilabel:`Filter Submissions`, select the form you want to use and click on :guilabel:`Export`

.. image:: /img/visualize/export.*
  :alt: Image showing how to export form.

3. Choose the type as :file:`KML file` and click on :guilabel:`Export`.

.. image:: /img/visualize/kml-file.*
  :alt: Image showing how to export form.

4. You don't need to change the default options, but you can select the :menuselection:`title` according to your choice.Click on :guilabel:`Export` 

5. You will be redirected to :guilabel:`Export Submissions` page where you can download your kml file.

.. image:: /img/visualize/export-submission.*
  :alt: Image showing how to download kml file.

6. After downloading go to `Google Earth website <https://earth.google.com/web/>`_ or you can download it from `here <https://www.google.com/earth/download/gep/agree.html>`_.Please wait for some time. 

.. image:: /img/visualize/google-earth.*
  :alt: Image showing Google Earth.

7. Click on |places| and to enable KML import click on :guilabel:`Settings`.

.. |places| image:: /img/visualize/my-places.*
  :alt: Image showing my places icon.

.. image:: /img/visualize/import-settings.*
  :alt: Image showing settings option.


8. In the Settings window, enable KML file import and click on :guilabel:`SAVE`.

.. image:: /img/visualize/enable-import.*
  :alt: Image showing how to enable KML file import.


9. Click on :guilabel:`IMPORT KML FILE` and import the downloaded kml file.

.. image:: /img/visualize/import-file.*
  :alt: Image showing import kml file option.


10. Now you will be able to see your data in an organized manner on Google Earth.

.. image:: /img/visualize/earth-data.*
  :alt: Image showing the data on Google Earth.


.. tip::

  - On Google Earth, you can choose your map style ,add additional points, lines and polygons to add more information for the enhancement of map. You can also try out `this <https://www.google.com/earth/outreach/learn/annotating-google-earth/>`_ tutorial on how to annotate Google Earth.
  - If you're looking to do some quick visualizations of a small dataset and aren't too worried about the inherent risks of experimental tools, then you should use Fusion Tables.
  - If you're serious about the long-term use of geo data and have large dataset use Google Earth.








