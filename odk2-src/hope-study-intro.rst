.. spelling::

  Prepopulated
  prepopulated

Longitudinal Clinic Study App
=================================

.. _hope-study-intro:

The Hope Study is a longitudinal clinical trial originally developed at the University of Washington as a collaboration between the Computer Science and Global Health departments. It was a randomized control trial studying pregnant, HIV discordant couples and their health outcomes, and was used for eight months by health workers in western Kenya. More info about the study can be found in `this article <https://clinicaltrials.gov/ct2/show/NCT01784783>`_. The study was conducted using ODK Collect, and then ported to the ODK 2 tools to demonstrate the features that could be added on this platform.

  .. image:: /img/hope-study-intro/hope-study-home.*
    :alt: Hope Study Home Screen
    :class: device-screen-vertical side-by-side

.. _hope-study-odk2-features:

Key Features
----------------------------

The Hope Study application provides a good example of the following ODK 2 platform features:

  - **Data Synchronization and Reuse**: The study takes place over a number of months, revisiting the same clients and reusing previously collected data. Launching the synchronization interface is built into the application's workflow. Known data is prepopulated into form prompts.
  - **Custom Web Views**: Navigation to the current client and appropriate form is made simple and easy. Custom data visualizations provide statistics on the full data set.
  - **Custom Form Linkage**: Multiple Survey forms update the same records in a single database table.
  - **Complex Form Navigation**: Forms will jump between screens based on client eligibility and response validation.


.. _hope-study-installing:

Installing Hope Study
--------------------------

Source code for this Data Management Application can be found in the `master branch of the App Designer repository <https://github.com/opendatakit/app-designer/tree/master>`_. It is one of the five demo applications for ODK Tables. As with all of the ODK 2 reference applications (and the ODK 2 platform itself), the code is free and open source. Feel free to reuse, modify, or extend this application and its component parts to suit your organization's needs.

.. note::
  The Hope Study application (and all other Data Management Applications provided in these docs) come with a full copy of the Application Designer they were developed in.

After you have have downloaded the application, you can set it up according to the :doc:`Application Designer setup <app-designer-setup>` instructions. Similarly You can push the application to your device using the :ref:`build-app-pushing` instructions.


.. _hope-study-intro-tour:

Guided Tour
------------------------

A walk-through of the features and the application and an overview of how they are implemented is provided in the guide below.

.. toctree::
  :maxdepth: 2

  hope-study-tour

