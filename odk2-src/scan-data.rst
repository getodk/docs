Managing ODK Scan's Data
=========================

.. _scan-data:

ODK Scan shares a database with the rest of the ODK tools, and the data can be accessed using the normal means through the :doc:`cloud-endpoints-intro` and :doc:`suitcase-intro`. However, Scan adds extra columns to store snippets of each data field's original image, the image file type, and the data value predicted by Scan.

.. _scan-using-suitcase:

Suitcase Formatting
------------------------------------------

:doc:`suitcase-intro` is the mechanism for downloading and exporting data from the ODK 2 data tables into local :file:`.csv` files. Suitcase has a specific option to format Scan's :file:`.csv` files more to be more readable. The image below shows this option underlined in red.

.. image:: /img/scan-data/suitcase-scan.*
  :alt: Scan formatting option in Suitcase
  :class: device-screen-vertical

