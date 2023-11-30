Testing your forms
===================

.. article-info::
    :avatar: /img/authors/xing.jpg
    :avatar-link: https://www.researchpro.global/blog/categories/odk
    :avatar-outline: muted
    :author: Xing Brew, ResearchPro
    :date: Nov 30, 2023
    :read-time: 14 min read

:bdg-primary:`community guide`

ODK serves as a powerful tool for data collection, but the fidelity of the data collected is directly tied to the quality of the form definitions used in the process and the ability for data collectors to use them to capture accurate data. ODK Central offers a variety of different ways forms can be tested before being used in production, allowing researchers to ensure that the forms and data collectors are ready for real data collection.

In this guide, we will explore four different ways to test forms on Central and discuss the appropriate circumstances for using each approach.

Why test?
----------
Before we delve into the "how" of testing forms, it's essential to understand the "why". There are several benefits of thoroughly testing forms before they are used in production. Testing forms allows you to:

* Identify and fix bad or incomplete form logic, missing questions, and potential data submission errors
* Evaluate and fine-tune the user interface (UI), such as the layout of questions on the screen and ease of navigation, and make adjustments to enhance the overall user experience (UX).

In particular, a form's coherence and UI/UX can significantly influence data quality, as a well-designed and intuitive form can facilitate accurate data entry, while a poor design may lead to errors, omissions, and reduced data reliability.

Form testing also offers operational benefits that extend beyond ensuring the functionality of your data collection tools.

* Test forms serve as a valuable practice environment to train and familiarize data collectors with tools and procedures they will use in the field, including how to navigate and access forms using ODK Collect, and how to correctly input data.
* A testing environment enables you to set up and ensure the smooth operation of the backend components of a data collection system, such as the server, database, and API integrations. 

Four ways to test forms
------------------------

The four methods this guide will describe are:

#. :ref:`using Drafts <guide-testing-central-drafts>`
#. :ref:`creating a specific App User for testing purposes <guide-testing-app-user>`
#. :ref:`including a 'practice or real' question <guide-testing-select-one>`
#. :ref:`creating a Project to be used exclusively for testing purposes <guide-testing-project>`

Each of these methods offers unique benefits and caters to different stages of form development and deployment.

A fundamental tool for form developers, Drafts are unpublished forms ideal for iterating on form design, especially during the initial stages of development, or testing minor changes made to forms used in production.

While invaluable for form developers, Drafts are not suited for data collector training and testing. One more appropriate method for fieldworker training is creating a dedicated App User for testing purposes. This method is especially beneficial for data collection using Collect, as it enables data collectors to effectively get to know the app's interface and practice filling forms in a real-world context. 

Adding a question at the start of the form to label submissions as "practice" or "real" is another effective strategy for the final review stages of form development. This provides a practical submission experience while distinctly separating test data from actual data, making it an excellent tool for both testing and training purposes.

Finally, establishing a distinct test Project within Central can offer a comprehensive, isolated testing environment for forms at all stages of development. However, this approach demands careful attention from Central administrators and may have cost implications if using ODK Cloud.

Read on for an in-depth exploration of each testing method and insights to help you select the most suitable method(s) for your specific scenario. We'll consider various factors such as the stage of form development, the specific requirements of testing and training, as well as the resources at your disposal. By the end of this guide, you'll have a clearer understanding of how to effectively apply these methods to optimize your ODK form development process. You can also jump straight to :ref:`the summary table <guide-testing-summary>` for an overview.

.. _guide-testing-central-drafts:

1. Using Drafts
----------------

What is a Draft?
~~~~~~~~~~~~~~~~~
Drafts are unpublished versions of ODK forms that can be tested both as web forms and in Collect. If a form has already been published, uploading an updated form definition (XLS file) or media files will create a new Draft, which can be tested before being deployed to replace the current published version.

Each Draft makes it possible to submit test submissions that are deleted when the Draft is published. Once a Draft is published, it is available for use according to the access rules you have specified in the Form Access tab of the Project.

Why / When to use this method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
During the initial phases of form development, the creation and testing of Drafts provide form developers with a quick and easy way to iteratively assess and refine form layout and styling, question sequencing, and user experience both online and in Collect. Once ready, Draft forms can seamlessly be published directly to production. 

When minor adjustments to the form definition or updates to media files are required while a form is being used in production, testing the updated form using the Draft method is an excellent option, as it allows you to easily publish the updated version for immediate use. 

How to create and test a Draft
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Upload a new form definition on a Form's Status tab
  
   .. image:: /img/guides/testing-upload-draft.png

#. Navigate to the Testing tab (1 in screenshot below)
#. To test the form online, click the New button (2) and the form will open in a new tab in your browser
#. To test the form in Collect, click Add New Project on the app home screen and scan the QR code (3). 
#. You will see the Draft icon at the top right of the screen (📝) and be able to fill out and submit a form as you normally would in Collect
#. All Draft submissions will appear at the bottom of the screen on the Testing tab (4) 

   .. image:: /img/guides/testing-draft-testing.png

#. Once the Draft has been tested and is ready to be published, return to the Status tab and click 'Publish Draft'.

   .. note:: The Draft submission data will disappear once the form is published.

   .. image:: /img/guides/testing-publish-draft.png

.. _guide-testing-app-user:

2. Creating an App User for Testing
----------------------------------------------

What is an App User for testing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
App Users are created at the Project level to submit data. Each App User can only download and access forms within a Project that they have been granted access to. A specific App User for testing is one which is created and given access to certain forms within a Project exclusively for the purpose of form testing.

.. image:: /img/guides/testing-app-user.png

Why / When to use this method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This approach is similar to :ref:`using a separate testing Project <guide-testing-project>` but is simpler to work with because there's only ever one published version of the same form. It's most appropriate to use before real data collection begins. Once verified, remove access from the testers and grant access to data collectors to seamlessly begin data collection.

Even once forms have been published to be used for real data collection, it can be helpful to create a specific App User to test and ensure the forms are functioning as intended.

In Projects containing multiple forms, a dedicated testing App User enables the simultaneous testing of certain forms within a Project, even as others are being used for real data collection.

If test submissions are inadvertently saved in a production Project, it is easy to identify which App User submitted the form and remove those submitted by the testing App User. One way to do so is to change the state of the forms submitted by the tester to Rejected (1), filter only the submissions that have the state 'Received' (2), then download the non-test submissions.

.. image:: /img/guides/testing-filter-rejected.png

How to create an App User for testing 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create a dedicated testing App User, click on 'Create App User' in the 'App Users' tab of a Project. We recommend assigning a clear name, such as 'Tester' or a similarly descriptive label, to signify the App User's intended use for testing purposes.

.. image:: /img/guides/testing-create-app-user.png

When first created, the App User won't have access to any forms. Access can be granted to the testing App User in the Form Access tab and, if needed, removed once real data collection begins.

.. image:: /img/guides/testing-assign-app-user.png

.. seealso:: 

    :ref:`Managing App Users <central-users-app-overview>`

.. _guide-testing-select-one:

3. Adding a practice/real question
-----------------------------------

After forms have undergone most of the testing process, one effective approach for conducting a final round of testing or training with data collectors using the published form is to incorporate a question at the beginning of the form to distinguish the submission as either a "practice" or a "real" submission. This method mitigates the risk of having the wrong App User configuration, as Collect will be configured with the App User that will be used for real data collection. 

Before real data collection begins or while the form is still undergoing final review, you can only include the option "Practice". Once the final version has been approved and/or data collection begins, the option "Real" can be added to the choice list. This method allows data collectors to continue practicing or for new data collectors to use the form for training purposes even as it is being used in production.

.. note::
    
    It is crucial that data collectors possess a strong understanding and exercise utmost care when responding to the "practice/real" question, to avoid selecting the incorrect option. But if the incorrect choice is made, data collectors should contact a data manager so a correction can be made.

How to add a practice/real question
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. In your XLSForm, add a select_one type question at the beginning of the form with the single choice "Practice" while the form is still being tested or before real data collection begins.

   .. image:: /img/guides/testing-select-one.png

#. Once the form is used in production, add the choice "real" to the choice list.

   .. image:: /img/guides/testing-select-one-choices.png
      :width: 400

#. If you would like to keep the practice option once real data collection begins, you may want to add a note to alert the data collector that they are entering practice data if that option is selected.

   .. image:: /img/guides/testing-select-one-note.png

   .. image:: /img/guides/testing-select-one-collect.png
      :class: device-screen-vertical

#. Once data has been collected, data managers can filter out all submissions in which the response to the practice/real question is "Practice" and keep only the real submissions for analysis.

.. _guide-testing-project:

4. Creating a test Project
---------------------------
What is a test Project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~
In Central, forms, submissions, and users are organized by Project. A test Project is a Project created to be used exclusively for the purpose of testing forms, data collection workflows, and associated processes. 

Why / When to use this method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advantages of creating a dedicated test Project include:

* **Isolated Environment**: A test Project provides a safe environment to experiment with form designs, logic, and features without the risk of disrupting ongoing data collection efforts.
* **Multiple Forms**: In scenarios where multiple forms within a Project are being used in production at different times, a test Project can serve as a centralized location for testing and refining forms before deployment to the real Project.
* **Entities**: Entity Lists and Entities can only be created from published forms and submissions, and it is not possible to test the usage of Entities in follow-up forms until real Entities have been created. A test Project in which all forms can be published and Entities created allows testing end-to-end workflows across multiple forms. 
* **Training Data Collectors**: In Projects that contain multiple forms, test Projects can be useful tools for familiarizing data collectors with navigating between different forms on Collect.
* **Backend Setup and Testing**: Test Projects are ideal for setting up and testing the backend components of data collection systems (e.g., server validation, database, and API integrations) while forms are undergoing development
* **Avoid Unintentional Data Loss and Breakages**: Making substantial modifications to a form being used in production can lead to unintentional data loss and potential breakages in the data collection pipeline. Testing changes in a dedicated test Project allows you to identify and resolve issues before they impact live data collection efforts.

How to create a test Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To create a Project in Central, you can follow the steps in :ref:`this guide <central-projects-create>`. 

You will want to make it very apparent that this is a test Project to avoid real data being accidentally submitted to this Project once data collection begins, such as by naming the Project with a prefix like 💥 or `***TESTING***`. 

.. image:: /img/guides/testing-project.png

Once the test Project has been created, you can publish forms, create App Users, and grant them access to the forms, as you would do in a production Project. If testing the forms on Collect, click 'Add Project' and submit forms to the test Project.

If modifications are needed to the forms, upload and publish the new form definitions to the test Project. After the forms have been thoroughly tested and approved in the test Project, deploy them to the real Project folder. 

.. warning::
    When testing forms using a test Project, it's important to ensure data collectors do not accidentally submit real data. Some suggestions to avoid this include:

    * Adding a prefix like `***TESTING***` or 💥 to the Project name to clearly indicate it as being a test Project
    * Deleting the test Project in Collect before configuring the real one
    * Changing a form to the ``closed`` state when migrating it to the real Project
    * Removing access for the App User(s) once real data collection begins

.. _guide-testing-summary:

Summary
---------
This table outlines suitable scenarios for each of the testing methods described above, specific form elements and features to test in each approach, and key considerations to be mindful of during their application.

+--------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
|                                                  | ODK Drafts                                                   | App User                                                                                                                                   | Practice vs Real Question                                                                                                        | Test Project                                                                                                          |
+==================================================+==============================================================+============================================================================================================================================+==================================================================================================================================+=======================================================================================================================+
| Used for                                         | Form developers to iterate quickly                           | * Testing user interface and flow                                                                                                          | * Data collector training                                                                                                        | * Backend set up (e.g., server validation, database, and API integrations) for multi-form projects                    |
|                                                  |                                                              | * Data collector feedback                                                                                                                  | * Allowing data collectors to continue training while form used in production                                                    | * Testing Entities                                                                                                    |
+--------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| When                                             | Initial stages of form development                           | Once forms have undergone initial testing and structural and content-related issues have been addressed)                                   | Final stages of form development, prior to and after deployment to production                                                    | All stages of form development and testing                                                                            |
+--------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| What                                             | * Relevance and conditionals work as needed                  | * Overall flow and grouping of questions on each screen                                                                                    | * Final verification that forms are error-free                                                                                   | * Backend components of data pipeline working correctly                                                               |
|                                                  | * Choice lists are accurate and complete                     | * Form navigation is intuitive and optimized                                                                                               | * There are no issues with saving and submitting forms to the server                                                             | * Data collectors are comfortable navigating between various forms in a Project                                       |
|                                                  | * Metadata/external files are correctly formatted            | * Forms can be saved and submitted without issue                                                                                           | * ODK Collect is being correctly synced to the server                                                                            | * Testing significant changes made to a form already being used in production to ensure no breakages in data pipeline |
|                                                  | * Questions are ordered correctly and free of typos          | * Data collectors are comfortable using the form and inputting data correctly                                                              | * Data collectors are comfortable using the form and inputting data correctly                                                    |                                                                                                                       |
|                                                  | * Text style and formatting (e.g., font size, color)         | * Data collectors are comfortable navigating between various forms in a Project                                                            | * Data collectors are comfortable using the form in a real life setting                                                          |                                                                                                                       |
|                                                  | * If using media, audio and visual elements are working well | * Backend structure of the dataset looks good                                                                                              | * Backend structure of dataset looks good                                                                                        |                                                                                                                       |
|                                                  | * Repeat groups are behaving properly                        |                                                                                                                                            |                                                                                                                                  |                                                                                                                       |
|                                                  | * Calculate fields and constraints are working as needed     |                                                                                                                                            |                                                                                                                                  |                                                                                                                       |
|                                                  | * Required fields are correctly marked                       |                                                                                                                                            |                                                                                                                                  |                                                                                                                       |
+--------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Notes                                            |                                                              | Removing access for testing App Users once real data collection begins can prevent test data from being unintentionally submitted          | Data collectors must be very careful when selecting 'Real' vs. 'Practice', as all form submissions will be stored in one dataset | Ensure devices and ODK Collect are configured correctly and data collectors do not submit real data to test project   |
+--------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Each of the methods described above plays an important and complementary role in form testing. Whether it's refining form design through Drafts, simulating realistic training scenarios with a dedicated testing App User, adding a 'practice or real' question, or creating a distinct test Project — each approach significantly bolsters the integrity of your data collection Project. Effectively leveraging these methods not only enhances the reliability and accuracy of your forms but also cultivates a sense of confidence among form developers, data managers, and fieldworkers. By integrating these testing strategies, you can lay the foundation for success in your data collection Projects, ensuring they are resilient and reliable.
