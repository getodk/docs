:orphan:

************************************
Visualizing Geographic Data
************************************

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

This guide helps the users to visualize the collected geodata uploaded on ODK Aggregate server using `Google Earth <https://www.google.com/intl/en_in/earth/>`_.

.. rubric:: Prerequisites

1. Make sure you have set up your :doc:`ODK Aggregate server <aggregate-install>`.
2. You should know how :doc:`ODK Collect  <collect-intro>` works.
3. You should be familiar with form designers like :doc:`ODK Build <build-intro>`,  :doc:`XLSForm <xlsform>` to create your location based forms and upload it to ODK Aggregate server.

.. _use-google-earth:

Google Earth
=================

:dfn:`Google Earth` is a virtual globe that accesses satellite and aerial imagery, and other geographic data over the internet to represent the Earth as a three-dimensional globe

Follow these steps to view your data using Google Earth:

1. Login to your ODK Aggregate server.
2. In the :guilabel:`Submissions` tab, under :guilabel:`Filter Submissions`, select the form you want to use and click on :guilabel:`Export`

.. image:: /img/visualize/export.*
  :alt: Image showing how to export form.

3. Choose the type as :file:`KML file` and click on :guilabel:`Export`.

.. image:: /img/visualize/kml-file.*
  :alt: Image showing how to export form.

4. You don't need to change the default options, but you can select the :menuselection:`title` according to your choice. Click on :guilabel:`Export`

5. You will be redirected to :guilabel:`Export Submissions` page where you can download your kml file.

.. image:: /img/visualize/export-submission.*
  :alt: Image showing how to download kml file.

6. After downloading go to `Google Earth website <https://earth.google.com/web/>`_ or you can download it from `here <https://www.google.com/earth/download/gep/agree.html>`_. Wait for a while as Google Earth takes time to load.

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

  - On Google Earth, you can choose your map style, add additional points, lines and polygons to add more information for the enhancement of map. You can also try out `this <https://www.google.com/earth/outreach/learn/annotating-google-earth/>`_ tutorial on how to annotate Google Earth.


