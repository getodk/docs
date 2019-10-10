Cold Chain Guided Tour
========================

.. _cold-chain-tour:

This document guides you through the :doc:`cold-chain-intro`, named Cold Chain. This application is stateful and does not have a single workflow to follow. Therefore it is organized by area of interest, with each classification broken down into different workflows and modules contained within it. Each individual module contains both a brief description of the purpose and function of the module, as well as an overview of how that functionality is implemented.

.. note::

  All file paths in this document are inside of the Application Designer directory. Additionally, all user defined files in a Data Management Application are inside the :file:`app/config/` directory. For convenience this document omits these portions of the file paths.

  For example, let us assume I have stored the Application Designer directory on my computer in :file:`/home/bobsmith/workspace/app-designer`. If this guide were to reference a file as :`assets/index.html` that indicates the file located on my computer at :file:`/home/bobsmith/workspace/app-designer/app/config/assets/index.html`.

.. toctree::
  :maxdepth: 2

  cold-chain-tour-initial-data
  cold-chain-tour-auth
  cold-chain-tour-regions
  cold-chain-tour-health-facilities
  cold-chain-tour-refrigerators
  cold-chain-tour-maintenance-records
  cold-chain-tour-refrigerator-types
  cold-chain-tour-admin

