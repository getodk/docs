Screen Client
=====================

.. image:: /img/hope-study-tour/hope-study-screen-client.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _hope-study-tour-screen-client-function:

Function
---------------------

The Screen Client form is used to conduct an interview with a potential new client. It provides a script for the interviewer and ask questions relating to the potential client's eligibility along with some basic demographic information. If the client is eligible, it asks for consent and instructs the interviewer in the process of randomizing the client into Hope or the control group.

.. _hope-study-tour-screen-client-implementation:

Implementation
---------------------

The form is defined in :file:`tables/femaleClients/forms/screenClient.xlsx`. This file is not directly consumed by the Android tools, but instead is input into the :doc:`xlsx-converter-intro` to create the files that the Android tools use (:file:`formDef.json`, :file:`definition.csv`, and so on). However we will only directly interact with the :file:`.xlsx` file.

The *survey* worksheet contains the main flow of the form. Interviewer scripts are provided with :tc:`note` prompt types, and data is collected mostly using :tc:`select_one`, :tc:`select_multiple`, and :tc:`integer` prompts. The flow of the form is controlled by :tc:`if`, :tc:`else:`, and :tc:`goto` elements in the :th:`clause` column, equations in the :th:`condition` column, and branches in the :th:`branch_label` column. Data is validated with the :th:`required` column and :tc:`select_multiple` prompts define their choices with links in the :th:`values_list` column.

The *choices* worksheet defines all the options for each :tc:`select_multiple` prompt.

The *settings* worksheet defines the :tc:`form_id` and the :tc:`table_id` to store form instances. Notice that the :tc:`table_id` is *femaleClients*, which will also be the :tc:`table_id` for other forms in the :ref:`follow up forms <hope-study-tour-follow-up-forms-implementation>`.

The *model* worksheet is used to specify the data model for the *femaleClients* table. See the :ref:`XLSX Converter Reference <xlsx-ref-model>` for more details

.. _hope-study-tour-screen-client-implementation-files:

Files
~~~~~~~~~~~~~~~~~~

  - :file:`tables/femaleClients/forms/screenClient.xlsx`

.. _hope-study-tour-screen-client-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~

 - *Add Client Form* with form ID *screenClient*

.. _hope-study-tour-screen-client-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~

  - *femaleClients*


