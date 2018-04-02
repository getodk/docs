.. spelling::
  prepopulated

Follow Up Forms
=======================

.. image:: /img/hope-study-tour/hope-study-follow-up-forms.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _hope-study-tour-follow-up-forms-function:

Function
---------------------

The follow up forms are the bulk of the longitudinal study. After clients are screened and entered into the study, six week and six month follow ups will take place. Furthermore, their partner may be screened to enter the study with them, and also receive a six month follow up.

Each of these are launched from the :doc:`hope-study-tour-client-details` module. They are survey forms that provide the interviewer with a script and ask detailed medical questions. Some previously collected data will be prepopulated in the forms prompts.

.. _hope-study-tour-follow-up-forms-implementation:

Implementation
-----------------------

The two :guilabel:`Client Forms` both read and write from the *femaleClients* table (as can be seen on the *settings* worksheet of both forms). This is true for both :guilabel:`Partner Forms` and the *maleClients* table as well.

These surveys are similar in structure to the initial :doc:`hope-study-tour-screen-client` form. There is basic navigation logic via :tc:`if` and :th:`condition` clauses. Simple data collection occurs with :tc:`select_one`, :tc:`select_multiple`, :tc:`integer`, :tc:`decimal`, :tc:`text:`, and :tc:`date` prompts. Interviewer scripts are provided with :tc:`note` prompts. The client ID is marked as necessary with the :th:`required:` column, however, this field should always be prepopulated in follow up forms. This is because the form is modifying an existing record in the database, and the field already has a value. In general this could be changed, though in this workflow this would be rare. The *model* worksheet provides the linkage with the database table.

There are also files to define *List Views* and *Detail View* for the male partners, even though they are not reachable through the normal workflows. These can be launched by opening the table directly via the *Tables Manager* screen.

.. _hope-study-tour-follow-up-forms-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

  - :file:`tables/femaleClients/forms/client6Week.xlsx`
  - :file:`tables/femaleClients/forms/client6Month.xlsx`
  - :file:`tables/maleClients/forms/screenPartner.xlsx`
  - :file:`tables/maleClients/forms/partner6Month.xlsx`

.. _hope-study-tour-follow-up-forms-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - *Client 6 Week* with form ID *client6Week*
  - *Client 6 Month* with form ID *client6Month*
  - *Screen Partner* with form ID *screenPartner*
  - *Partner 6 Month* with form ID *partner6Month*

.. _hope-study-tour-follow-up-forms-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - *femaleClients*
  - *maleClients*
