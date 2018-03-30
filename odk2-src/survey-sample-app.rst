.. spelling::
  prepopulate
  prepopulated

ODK Survey: Sample Application
====================================

.. _survey-sample-app:

In this guide we will be demonstrating how to use ODK Survey via a guided tour of a sample application. This guide demonstrates both the general workflow of Survey and some of the features that differentiate it from ODK Collect.

.. warning::

  ODK Survey performs a similar role to ODK Collect in the ODK 2 Tool Suite. However, it is more complex and not every organization will need its features. The choice of whether to use ODK Collect or ODK Survey and the ODK 2 tools should be made carefully based on your organization's needs. A brief comparison can be found in the guide for :doc:`select-tool-suite`.

.. _survey-sample-app-prereqs:

Prerequisites
--------------------

Install ODK Survey and its prerequisites from the guide: :doc:`survey-install`.

.. _survey-sample-app-overview:

Sample Application Overview
-------------------------------

We have provided a sample application to help you acquaint yourself with the various features of ODK Survey. This sample app contains six sample forms within it:

  - **Example Form** -- a form with many examples of data entry widgets.
  - **Grid Screen Form** -- a form used to demonstrate a new screen layout that allows fully customized prompt placement.
  - **Household Survey** -- a form used to gather information about a household. To operate correctly, this requires the *Household Member Survey* sub-form and the *Education* sub-form (you should not open those sub-forms directly -- they are launched from within Household Survey).
  - **Select Examples** -- a form with several examples of select widgets, including widgets that access data on Yahoo servers, and others that access CSV files for their choice lists. It also demonstrates the use of custom CSS styles to change the look of the form.
  - **Household Member Survey** -- a form used to gather information about household members. This is a sub-form of the Household Survey form (you should not open it directly -- it is launched from within Household Survey). ODK Survey eliminates the repeat group concept and replaces it with sub-forms. From within the Household Survey you navigate into this sub-form by entering information about individuals in a household.
  - **Education** -- a form used to gather education information about household members. This is another sub-form of the Household Survey form (you should not open it directly -- it is launched from within Household Survey). This sub-form saves information to the same underlying data table (household_members) as the Household Member Survey form, but it asks different questions. This demonstrates the use of multiple forms to revise different sets of values within a data table. From within the Household Survey you navigate into this form when you enter education information about individuals in a household.

.. note::

  Since the *Education* and *Household Member Survey* operate on the same table, you will only see five tables in ODK Tables and in the Cloud Endpoint even though there are six forms.

.. _survey-sample-app-overview-learn-more:

Learn More
~~~~~~~~~~~~~~~

For instructions on creating your own Survey applications, view the :ref:`app-designer-common-tasks-designing-a-form` guide.


.. _survey-sample-app-install:

Installing the Sample Application
--------------------------------------

Unlike ODK Collect, the ODK 2 tools are application-focused. An application is identified by the name of the directory under the :file:`/sdcard/opendatakit/` folder. The sample application is named *default*, as is the sample applications provided for :doc:`tables-intro`. This means that you can only deploy one of these sample application at a time onto a device. We also provide :ref:`instructions <survey-launching-appname>` to rename one of these so that two or more applications can co-exist and not interfere with each other on this same device.

To access the sample application and its six sample forms:

  1. Launch ODK Survey. Press the :guilabel:`Settings` button that resembles a gear. This will launch the ODK Services tool to the settings page.

    .. image:: /img/survey-sample-app/survey-settings-button.*
      :alt: Survey Setting Button
      :class: device-screen-vertical

  2. Follow the :ref:`services-managing-server-config` instructions to set up your server.

    - Set your :guilabel:`Server URL` to :file:`https://opendatakit-2.appspot.com`.

      .. note::

        The server URL starts with :file:`https://` not :file:`http://`. Don't forget to include the *s*.

    - Leave your authentication as :guilabel:`None (anonymous access)`.

  3. Back out until you return to Survey.
  4. Follow the :ref:`services-using-sync` instructions (see :ref:`launching from Survey <services-using-sync-launch-other>`).

    - Again, leave your user as :menuselection:`None (anonymous access)`.
    - Leave the file attachment setting to :menuselection:`Fully Sync Attachments`

After synchronization is complete, your device's configuration will exactly match that of the server. This includes both collected data and application level files (such as form definitions and HTML files). If you had nothing on your device before, your device will be populated with this data and these application files. If you already had files on this device in this application namespace they will be updated to match the server version. Any local configuration files for data tables or forms that are not present on the server will be removed from your device. Everything under the :file:`/sdcard/opendatakit/default/config` directory will be revised to exactly match the content on the server.

Once the configuration and data on the device is an exact match to that of the server, the file attachments associated with those data are synchronized. If you have a slow connection, it may take two or three tries before the sync is successful. This will not overwrite or hurt anything to do multiple synchronizations in a row.

When complete, click :guilabel:`OK` on the :guilabel:`Sync Outcome` dialog and back out of the Services, returning to Survey.

If the sync was successful, ODK Survey will scan through the downloaded configuration, updating its list of available forms.

  .. image:: /img/survey-sample-app/survey-scanning.*
    :alt: Survey Scanning Form Definitions
    :class: device-screen-vertical

When that is completed you should now be presented with the list of those six sample forms.

.. _survey-sample-app-installing-learn-more:

Learn More
~~~~~~~~~~~~~~~

For instructions on installing your own Survey application to a device, view the :ref:`app-designer-common-tasks-move-to-device` guide.

.. _survey-sample-app-open-form:

Opening a Form
-------------------------

Open Survey. If you have successfully installed the sample application, you should be presented with a list of the six sample forms.

  .. image:: /img/survey-sample-app/survey-sample-form-list.*
    :alt: Survey Displaying the List of Sample Forms
    :class: device-screen-vertical

.. note::

  The *Household Members* and *Education* forms are not intended to be called directly, but are launched from within the *Household* form.

To open a form, tap on it in this list. For this tutorial, open the :menuselection:`Example Form`.

  .. image:: /img/survey-sample-app/survey-example-home.*
    :alt: Survey Example Form
    :class: device-screen-vertical

This screen shows the name and version of the form you are viewing. If you scroll down you will see a list of previously created instances of this form.

.. tip::

  Form instances can always be edited, even after they have been finalized.

To fill in a new instance, tap the :guilabel:`Create new instance` button.

.. _survey-sample-app-opening-learn-more:

Learn More
~~~~~~~~~~~~~~~

For more detailed instructions on opening and modifying Survey form instances, view the :ref:`survey-opening-form` guide.

.. _survey-sample-app-navigating-form:

Navigating a Form
--------------------

Forms in Survey are defined in HTML, CSS, and JavaScript. A default look-and-feel, along with an extensive selection of prompt widgets, is provided by the ODK 2 framework, but this can be customized by your organization.

To navigate forms using the default look-and-feel:

  - Tap on the name of the survey in the top left to access a pop-up menu of options.
  - Tap the :guilabel:`Back` or :guilabel:`Next` buttons in the top right of the form to navigate through the form.

Let's fill out the instance of the :menuselection:`Example Form` that we opened in the previous section. After tapping the :guilabel:`Create new instance` button you should see the following screen:

  .. image:: /img/survey-sample-app/survey-example-start.*
    :alt: Survey Example Form Start Screen
    :class: device-screen-vertical

Use the :guilabel:`Next` button in the top right to progress to the first question.

.. _survey-sample-app-initial-value:

Initial Value
~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-initial-rating.*
    :alt: Survey Example Form Initial Rating
    :class: device-screen-vertical

This prompt asks you to give the form an initial rating. Its purpose in this example is to show how Survey can use previously collected data to populate and calculate later fields. Enter any number you like and it will be used later.

Press the :guilabel:`Next` button in the top right to progress to the next question.

.. _survey-sample-app-prompt-selection:

Prompt Selection
~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-prompt-selection.*
    :alt: Survey Example Form Prompt Selection
    :class: device-screen-vertical

This prompt allows you to choose which sections of the form to complete. Survey form navigation can be completely customized, even at runtime, to include or exclude sections, repeat portions, jump directly to different prompts based on entered values, and more. For this example we will complete the :menuselection:`label features`, :menuselection:`computed assignment of initial values`, and :menuselection:`custom template` sections. However, feel free to enter any combination you like and explore.

Press the :guilabel:`Next` button in the top right to progress to the next question. Note that we skip the :menuselection:`intent launching` section and progress directly to :menuselection:`label features`.

.. _survey-sample-app-label-features:

Label Features
~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-label-html.*
    :alt: Survey Example Form Label Customization
    :class: device-screen-vertical

This prompt shows that the label and hint fields of the prompt can be customized by editing the HTML and CSS. This allows your organization to modify the look-and-feel of the prompts to suit their needs.

Press :guilabel:`Next` to see a more complex example:

  .. image:: /img/survey-sample-app/survey-example-label-media.*
    :alt: Survey Example Form Label Customization
    :class: device-screen-vertical

This prompt shows a label that has been edited to include media files including an image and an audio clip. Press play on the audio clip to hear a bird call. However, media can also be added via spreadsheet columns, which is generally easier.

Press :guilabel:`Next` to advance to the next section.

.. _survey-sample-app-reuse-values:

Reading Previous Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-name-prompt.*
    :alt: Survey Example Form Name Prompt
    :class: device-screen-vertical

This prompt is requesting a value that will be used to render the next question. Enter any name you like and press :guilabel:`Next`.

  .. image:: /img/survey-sample-app/survey-example-name-use.*
    :alt: Survey Example Form Name Used
    :class: device-screen-vertical

This prompt shows that a prompt can use a previously collected value in the rendering of a prompt. For example, a subject's name and gender could be used to properly address them throughout a survey.

Press :guilabel:`Next` to see another example of data reuse.

  .. image:: /img/survey-sample-app/survey-example-coffee-prompt.*
    :alt: Survey Example Form Coffee Prompt
    :class: device-screen-vertical

This prompt is requesting a value that will be used to render the next question. Enter any value you like and press :guilabel:`Next`.

  .. image:: /img/survey-sample-app/survey-example-coffee-autofill.*
    :alt: Survey Example Form Coffee Autofill
    :class: device-screen-vertical

This prompt will prepopulate the entered data with the value from the previous prompt. In general, you can prepopulate the a prompt with any previously collected value. In another example you might record a subject's address and then prepopulate that address on their household members address prompts.

Press :guilabel:`Next` to advance to the next section.

.. _survey-sample-app-custom-template:

Custom Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-graph-prompt.*
    :alt: Survey Example Form Graph Prompt
    :class: device-screen-vertical

This prompt is requesting data that will be used in the next prompt to render a custom template. We will also use this to demonstrate constraints. Enter an age that is greater than 20 and press :guilabel:`Next`.

  .. image:: /img/survey-sample-app/survey-example-graph-validate.*
    :alt: Survey Example Form Graph Validate
    :class: device-screen-vertical

Survey will not allow you to progress until you've entered a valid value. This validation can be done dynamically as well. For example, you could have a running average of crop heights you have measured, and disallow crop heights that differ by more than three standard deviations.

Enter a valid age, weight, and height, and press :guilabel:`Next`.

  .. image:: /img/survey-sample-app/survey-example-graph-render.*
    :alt: Survey Example Form Graph Render
    :class: device-screen-vertical

This prompt will show the data point you entered in the previous prompt, rendered on a plot of average weights. This is a custom prompt defined in JavaScript for this example, it is not a default display option provided by the ODK 2 framework. It demonstrates that Survey can be customized to whatever level your organization requires without the effort of rewriting and recompiling the Android tools.

Press :guilabel:`Next` to advance to the next section.

.. _survey-sample-app-update-value:

Update Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-update-value.*
    :alt: Survey Example Form Update Value
    :class: device-screen-vertical

This prompt is prepopulated from the initial value we entered in the first prompt. Whatever you entered for that field will be filled in here. Updating this field will update the value in the database.

This was the final prompt for this example. Press :guilabel:`Next` to advance to the final screen of the form.

.. _survey-sample-app-complete:

Complete Form Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. image:: /img/survey-sample-app/survey-example-finish.*
    :alt: Survey Example Form Complete
    :class: device-screen-vertical

This screen tells you that you have reached the end of the form. This **does not** mean that you have entered data for every field. In this example we skipped the majority of the questions. From here you can navigate backwards and update any of your previous answers. You can also use the button in the upper left to navigate to previous questions or leave the form instance.

.. warning::

  Updating answers may cause later prompts to render differently or be invalidated.

To save the form instance, either press :guilabel:`Finalize` or :guilabel:`Incomplete`.

  - :guilabel:`Finalize` will mark the form as *Finalized* and indicate that this instance is completed.
  - :guilabel:`Incomplete` will mark the form as *Incomplete* and indicate that this form should be revisited and completed in the future. Use this option to save your progress if you have to pause while filling out a form.

After pressing one of the above options you will be returned to the Survey home-screen. If you select :menuselection:`Example Form` again you will see this form instance at the top of the list of previously saved instances, with the date you saved it and the state you chose.

.. _survey-sample-app-navigating-learn-more:

Learn More
~~~~~~~~~~~~~~~

For more detailed instructions on navigating Survey forms, view the :ref:`survey-navigating` guide.


.. _suvey-sample-app-explore:

Explore the Sample Application
---------------------------------

This concludes the guided tour of the sample application for Survey. However, this is far from a complete reference. Please continue to explore the different forms and prompts to learn more about the tool's capabilities.

You can find a more detailed user guide for Survey here: :doc:`survey-using`. And you can find a more detailed guide to managing Survey for Deployment Architects here: :doc:`survey-managing`. You can also find the sample forms shown in this tutorial in the Github repository for `App Designer <https://github.com/opendatakit/app-designer/>`_.
