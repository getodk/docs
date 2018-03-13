.. spelling:: 
  basemap
  geospatial
  heatmaps
  Mapbox
  pbf

Using Offline Maps
====================

Collect's :ref:`geoshape`, :ref:`geotrace` and :ref:`geopoint` question types can be configured to display different maps. To use online maps, :ref:`set the mapping engine and basemap <mapping-settings>` in :ref:`interface-settings`. Users will need to be online to load questions with maps.

Offline maps are useful for low-connectivity environments or to present custom geospatial data. Use them to display high-resolution imagery, annotated maps, heatmaps, and more. ODK Collect can display any map layer saved as a set of tiles in the `MBTiles format <https://github.com/mapbox/mbtiles-spec)>`_. Tiles are images that represent a subset of a map. The only limitation is that tile data in Mapbox's pbf format are not supported.

.. _offline-maps-quick-start:

Offline maps quick start
-------------------------
#. From :ref:`Collect's settings <mapping-settings>`, change the Mapping SDK to Google Maps SDK
#. :ref:`Get or create your MBTiles file <getting-map-tiles>` with `TileMill <https://tilemill-project.github.io/tilemill/>`_ or other software.
#. :ref:`Transfer tiles to devices <transferring-offline-tiles>`. The MBTiles file must be placed in a sub-folder on your device in the :file:`/sdcard/odk/layers` folder.
#. Open a question that displays a map (types :ref:`geoshape`, :ref:`geotrace`, :ref:`geopoint` with certain appearances)
#. Tap the layers icon and select your map

.. _getting-map-tiles:

Getting map tiles
-------------------------
`Open Map Tiles <https://openmaptiles.org/>`_ hosts many free map tile files that can be used in ODK Collect.

To create MBTiles files, use one of the `compatible applications <https://github.com/mapbox/mbtiles-spec/wiki/Implementations#applications>`_ that can write tiles. Commonly used free software packages are `TileMill <https://tilemill-project.github.io/tilemill/>`_ and `QGIS <https://qgis.org/en/site/>`_ with the `QTiles plugin <https://github.com/nextgis/QTiles#qtiles>`_.


.. _transferring-offline-tiles:

Transferring offline tiles to devices
-------------------------------------
To make MBTiles files available for use in ODK Collect they must be manually transferred to Android devices. The tile files need to be inside a folder in the :file:`/sdcard/odk/layers` folder. The folder name will be used to identify your offline map in the user interface so choose a user-friendly name for it. For example, if your MBTiles file is `my_tiles.mbtiles` and it includes information about settlements in the mapped area, you may want to call your folder :file:`/sdcard/odk/layers/All settlements/`.

.. note::

  MBTiles files placed directly in the :file:`/sdcard/odk/layers` folder will not be detected! Placing it in a subdirectory with a friendly name is required.

To transfer files, you can upload them to an online service such as Google Drive, connect your device to a computer and transfer them via USB or use :doc:`adb <collect-adb>`.
