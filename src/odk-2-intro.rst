ODK 2.0 Tool Suite
=======================

.. _odk-2-introduction:

The :dfn:`ODK 2.0 Tool Suite` is a new set of ODK tools that will co-exist with the existing ODK 1.0 Tool Suite. It addresses several limitations of the existing ODK 1.0 data collection workflows such as:

- **Fully customizable layout of prompts on the Android device**. The 2.0 tools use HTML, JavaScript, and CSS to specify the layout of nearly all the screens viewed by the data collectors. This enables individuals and organizations with basic web development skills to modify and customize the appearance of their surveys and workflow. At the same time, we retain the easy-to-use spreadsheet-based definition of the survey questions (however, this XLSX Converter mechanism is not cross-compatible with XLSForm).
- **More flexible, user-directed, navigation of a survey**. The 2.0 tools do not impose a strict sequential advancement through a form like ODK Collect; form designers can allow users to traverse a form in any order, yet impose validation of collected data prior to traversing into subsequent steps in a workflow.
- **Improved treatment of repeat-groups**. In the 2.0 tools, we have eliminated the concept of a repeat-group. In its place, we provide prompts that enable you to open and edit other surveys with links back to the originating survey (if desired). These prompts can describe a sub-form (nested) relationship among the surveys (e.g., household and household-member) or they can represent arbitrary relational linkages across your data (e.g., tea-houses and tea-types).
- **Bi-directional synchronization of data across devices**. The ODK 2.0 tools support the collaborative sharing of survey data across devices, as well as the updating and submission of changes to previously-collected data (i.e., follow-up surveys) via a bi-directional synchronization protocol; this contrasts with the unidirectional device-to-server submission pathway of ODK Collect / ODK Aggregate / ODK Briefcase.
- **Data curation and visualization on the device**. ODK Tables gives organizations the ability to investigate and visualize entire datasets directly on the Android devices through graphical and non-graphical displays and through filtered views.
- **Row-level access filters**. The visibility of the data and the ability to edit and/or delete data can be restricted for different users and groups.

.. _odk-2-intro-learn-more:

Learn More
--------------
View a full feature comparison in the guide for :doc:`select-tool-suite`.

.. _odk-2-intro-list-of-tools:

List of Tools
---------------
The ODK 2.0 Tool Suite consists of:
  - :doc:`app-designer-intro` - a design environment for creating, customizing, and previewing your forms, data curation, and visualization applications.
  - :doc:`survey-intro` - a data collection application based upon HTML, CSS, JavaScript.
  - :doc:`tables-intro` - a data curation and visualization application running on your mobile device.
  - :doc:`services-intro` - an application for handling database access, file access, and data synchronization services between all the ODK 2.0 applications. It allows you to synchronize data collected by the ODK 2.0 Android tools with a cloud endpoint.
  - :doc:`cloud-endpoints-intro` - a cloud server to host data and application files, and to support bi-directional data synchronization across disconnected mobile devices.
  - :doc:`suitcase-intro` - a desktop tool for synchronizing data with a cloud endpoint.

.. _odk-2-intro-trying-it-out:

Trying It Out
----------------
First see the sections for :doc:`survey-intro`, :doc:`tables-intro`, and :doc:`services-intro`. They cover the overview of each tool, setup instructions, and demonstration forms and applications built with these tools. These demonstration applications will give you a good sense of the flexibility and breadth of capabilities of the two tools.

Next, see the :doc:`getting-started-2` to understand the process for revising and developing your own forms. That guide will walk you through modifying the Geotagger demo app to add an additional field to it.

Finally, see the :doc:`data-permission-filters` page for how to manage table and row-level access filters.

