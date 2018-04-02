Client Details
=======================

.. image:: /img/hope-study-tour/hope-study-client-details.*
  :alt: Main Menu
  :class: device-screen-vertical

.. _hope-study-tour-client-details-function:

Function
-----------------------

The Client Details module is a hub to perform follow up and additional data collection for the selected client. The three main data points about the client are displayed at the top: client ID, age, and randomization status. The follow up forms are organized into :guilabel:`Client Forms` (forms pertaining to the female client) and :guilabel:`Partner Forms` (forms pertaining to the female clients partner). Tapping the desired section will expand it to display the collection options.

The :guilabel:`Home Locater` button launches the :doc:`hope-study-tour-home-locator` module. The rest of the forms are discussed in the :doc:`hope-study-tour-follow-up-forms` section.

.. _hope-study-tour-client-details-implementation:

Implementation
--------------------------

The HTML file file:`tables/femaleClients/html/femaleClients_detail.html` is, minimal, like its sister *List View* HTML file, and provides only a basic skeleton of the user interface which will be filled in by :file:`tables/femaleClients/js/femaleClients_detail.js`

The JavaScript file :file:`femaleClients_detail.js` implements the basic *Detail View* workflow. The call that launched the view provided a query as a parameter that selects which record will be displayed in the *Detail View*. This record is retrieved with the :code:`odkData.getViewData(...)` call. The returned record is used to fill in the basic info at the top of the screen, and then the :guilabel:`Client Forms` and :guilabel:`Partner Forms` are created. These buttons link to the :doc:`hope-study-tour-follow-up-forms` using :code:`odkTables.editRowWithSurvey(...)` and :code:`odkTables.addRowWithSurvey(...)` API calls. All the buttons in the :guilabel:`Client Forms` section use the table ID *femaleClients* and the client ID of the selected record, while all the buttons in the :guilabel:`Partner Forms` section use the table ID *maleClients* and the male client ID (read from the selected record).

Additionally, the :doc:`hope-study-tour-home-locator` module is launched with the :guilabel:`Home Locater` button using an :file:`openTableToListView(...)` call.

.. _hope-study-tour-client-details-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~~

  - :file:`tables/femaleClients/html/femaleClients_detail.html`
  - :file:`tables/femaleClients/js/femaleClients_detail.js`

.. _hope-study-tour-client-details-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~~

None

.. _hope-study-tour-client-details-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~

  - *femaleClients*


