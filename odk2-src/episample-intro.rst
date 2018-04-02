Geographic Health Survey App
==============================

.. _episample-intro:

EpiSample is a geographic health survey application originally developed by `Belendia Serda at MACEPA <http://www.makingmalariahistory.org/about/about-macepa-malaria-control-and-evaluation-partnership-in-africa/about-our-team/>`_. It is a prototype application for health surveys regarding malaria prevention behavior, and has been used Ethiopia and Zambia. This article, written about an earlier version of EpiSample, provides some context for its development: `The scrum master, the coder, and the phone <http://www.makingmalariahistory.org/the-scrum-master-the-coder-and-the-phone/>`_.

  .. image:: /img/episample-intro/episample-collect-screen.*
    :alt: Config Startup
    :class: device-screen-vertical side-by-side


.. _episample-odk2-features:

Key Features
----------------------------

The EpiSample application provides a good example of the following ODK 2 platform features:

  - **Data Synchronization and Reuse**: Collected data is reused to generate tasks across devices. Shared configuration is set by a supervisor and synchronized across devices.
  - **Custom Web Views**: Location data is displayed and updated in real time. Custom data visualizations are used on data entry screens to help guide collection.
  - **Complex Workflows**: Custom logic is implemented in JavaScript to generate tasks using collected data and to dynamically launch Survey forms.
  - **Mapping and Navigation**: A map of of homes is generated using collected geo-data. *Navigate View* is integrated into the workflow to guide data collectors to homes and launch follow up surveys.
  - **Adaptability**: The application is designed to be flexible to differing usage scenarios. Different Survey forms can be loaded into the same workflow to adapt to different data collection needs. Data quantity and location accuracy requirements can be configured in the app and updated as needed.

  .. _episample-installing:

Installing EpiSample
--------------------------

Source code for this Data Management Application can be found in the `malaria-demo branch of the App Designer repository <https://github.com/opendatakit/app-designer/tree/malaria-demo>`_. As with all of the ODK 2 reference applications (and the ODK 2 platform itself), the code is free and open source. Feel free to reuse, modify, or extend this application and its component parts to suit your organization's needs.

.. note::
  The EpiSample application (and all other Data Management Applications provided in these docs) come with a full copy of the Application Designer they were developed in.

After you have have downloaded the application, you can set it up according to the :doc:`Application Designer setup <app-designer-setup>` instructions. Similarly You can push the application to your device using the :ref:`build-app-pushing` instructions.


.. _episample-intro-tour:

Guided Tour
------------------------

A walk-through of the features and the application and an overview of how they are implemented is provided in the guide below.

.. toctree::
  :maxdepth: 2

  episample-tour

