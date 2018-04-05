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

.. _survey-sample-app-contents:

Sample Application Contents
-----------------------------

A tour of the sample application is provided in the documents below. It is intended to be run from top to bottom, but you can also skip to a section that interests you.

.. toctree::
  :maxdepth: 2

  survey-sample-app-install
  survey-sample-app-open-form
  survey-sample-app-navigate-form
  survey-sample-app-end

