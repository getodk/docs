Hope Demo
==================

.. _tables-sample-app-hope:

For this portion of the tutorial, we will explore the *Hope* demo. Select the tab labeled :guilabel:`Hope` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-hope.*
    :alt: Launch Hope Demo
    :class: device-screen-vertical

The *Hope* demo is a complex, longitudinal medical survey involving mothers with HIV.

.. _tables-sample-app-integrate-with-survey:

Integrate With Survey
-------------------------

After launching the *Hope* demo app, you will see a custom view that lets you choose whether you are visiting with a new client or following up with an existing client. This study involves multiple visits from the same patient that occur over a period of months during and after the mother's pregnancy. Let's imagine that a client with ID number *44176* has come in for a 6 week follow up visit.

Select :guilabel:`Follow Up with Existing Client`.

  .. image:: /img/tables-sample-app/tables-sample-hope-nav.*
    :alt: Tables Sample Hope Naviation Screen
    :class: device-screen-vertical

This will open a *List View* that shows all the registered clients in the system (registered using the :guilabel:`Screen Female Client` option from the previous screen).

  .. image:: /img/tables-sample-app/tables-sample-hope-list.*
    :alt: Tables Sample Hope Client List
    :class: device-screen-vertical

On the top of the screen is a search field that is custom written in HTML, CSS, and JavaScript. Use this to enter the client ID of the patient we imagine to be interviewing: *44176*. After pressing :guilabel:`Search` the desired client should be visible.

  .. image:: /img/tables-sample-app/tables-sample-hope-search.*
    :alt: Tables Sample Hope Search Results
    :class: device-screen-vertical

Select client *44716* to see a *Detail View* of that patient.

  .. image:: /img/tables-sample-app/tables-sample-hope-detail.*
    :alt: Tables Sample Hope Client Detail
    :class: device-screen-vertical

This page is a *Detail View*, but most of the collected data about this patient is not shown. Instead, links to the follow up Survey forms are provided to make follow up visits run smoothly. If you needed to update the patient's information, you could tap the pencil icon in the top right to launch the Survey form containing all of that patient's data.

Tap :guilabel:`Client Forms` and choose :guilabel:`Six Week Follow-Up`. This will launch the Survey to the specific form containing the six week follow-up questionnaire.

  .. image:: /img/tables-sample-app/tables-sample-hope-six-weeks.*
    :alt: Tables Sample Hope Six Week Follow Up Survey
    :class: device-screen-vertical

This demo imitates a single visit. Next, you can try to emulate the full length of the study for a single patient from the initial screening through all the follow-up visits. Notice that the *Graph Views* will update with this new information as well.

.. _tables-sample-app-hope-edit-survey-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~

For more information about integrating Survey and Tables, view the :ref:`tables-using-edit-data` guide.

