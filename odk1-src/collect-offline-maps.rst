.. spelling:: 
  basemap
  Basemap
  basemaps
  Basemaps
  geospatial
  heatmaps
  Mapbox
  pbf
  tileset
  tilesets

Using Offline Maps
====================

Collect's :ref:`geopoint <geopoint-maps>`, :ref:`geotrace <geotrace-widget>`, and :ref:`geoshape <geoshape-widget>` questions can be configured to display different map data. To use online basemaps, :ref:`set the basemap source and style <basemap-settings>` in :guilabel:`mapping-settings`. Users will need to be online to load questions with maps.

Offline layers are useful to present custom geospatial data layered over standard basemaps or as basemaps for low-connectivity environments. Use them to display high-resolution imagery, annotated maps, heatmaps, and more. ODK Collect can display any map layer saved as a set of tiles in the `MBTiles format <https://github.com/mapbox/mbtiles-spec>`_.

.. warning::

  - Vector MBTiles (with data in `Mapbox Vector Tile format (pbf) <https://github.com/mapbox/vector-tile-spec>`_) are only supported if :guilabel:`Mapbox` is selected as the :ref:`basemap source <basemap-settings>`.

  - Vector MBTiles are currently displayed without styling. Each layer's lines are displayed in a different color picked by ODK Collect. This color will be the same across all devices using the same MBTiles file. Fills are not displayed.

.. _offline-maps-quick-start:

Offline maps quick start
-------------------------
#. :ref:`Get or create your MBTiles file <getting-map-tiles>` with `TileMill <https://tilemill-project.github.io/tilemill/>`_ or other software.
#. :ref:`Transfer tiles to devices <transferring-offline-tiles>`. The MBTiles file must be placed on your device in the :file:`/sdcard/odk/layers` folder.
#. Select your offline layer in the :ref:`reference layer settings <reference-layer-settings>`.
#. Open a :ref:`geopoint <geopoint-maps>`, :ref:`geotrace <geotrace-widget>`, or :ref:`geoshape <geoshape-widget>` questions.

Your offline layer should be displayed. If it has transparency (PNG or PBF tiles only), the selected basemap will show through. If it does not have transparency or you are offline, only your offline layer will be displayed.

.. _getting-map-tiles:

Getting map tilesets
-------------------------
`OpenMapTiles <https://openmaptiles.org/>`_ hosts many free map tile files that can be used in Collect.

To create MBTiles files, use one of the `compatible applications <https://github.com/mapbox/mbtiles-spec/wiki/Implementations#applications>`_ . Commonly used free software packages are `TileMill <https://tilemill-project.github.io/tilemill/>`_ and `QGIS <https://qgis.org/en/site/>`_ with the `QTiles plugin <https://github.com/nextgis/QTiles#qtiles>`_.

If you have existing geospatial data that is not in an MBTiles file, you may be able to convert it for use in Collect. For example, `Tippecanoe <https://github.com/mapbox/tippecanoe>`_ is a tool to build vector MBTiles files from GeoJSON features (see warning above: vector MBTiles files are only supported with Mapbox basemaps and are displayed without styling).

The name of the tileset provided in the MBTiles file will be displayed in the Collect layer selection menu. The filename will also be displayed.

.. _transferring-offline-tiles:

Transferring offline tilesets to devices
-----------------------------------------
MBTiles files must be manually transferred to Android devices to be available to Collect. Place the MBTiles files in the :file:`/sdcard/odk/layers` folder.

To transfer files, you can upload them to an online service such as Google Drive, connect your device to a computer and transfer them via USB, or use :doc:`adb <collect-adb>`.

.. _selecting-offline-tilesets:

Selecting offline tilesets
---------------------------
Once an MBTiles file has been transfered to the :file:`/sdcard/odk/layers` folder, it will be available for selection as a reference layer. A reference layer provides useful reference information for a data collector. A reference layer with no transparency acts like a basemap.

There are two ways to set the reference layer:

- from :ref:`mapping-settings`
- by tapping on the layers button in a :ref:`geopoint <geopoint-maps>`, :ref:`geotrace <geotrace-widget>`, or :ref:`geoshape <geoshape-widget>` question

Both options set the reference layer for all :ref:`geopoint <geopoint-maps>`, :ref:`geotrace <geotrace-widget>`, and :ref:`geoshape <geoshape-widget>` questions. The tileset name shown in the menu is read from the metadata in the MBTiles file.