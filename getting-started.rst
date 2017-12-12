Getting Started Guide
=========================

.. _using-odk:

Using ODK
-----------

In most cases, users of ODK:

- Create survey forms using `Build <https://build.opendatakit.org/>`_ or `XLSForm <http://xlsform.org/>`_
- Upload forms to an Aggregate server
- Load forms into Collect on an Android device
- Use Collect to fill out forms with :term:`participants <participant>`
- Upload survey data from Collect to Aggregate
- Analyse or export data in Aggregate

This requires:

- :doc:`Installing Collect on a phone or other mobile device <collect-install>`
- :ref:`Installing Aggregate on a server <installing-aggregate>`

.. tip::

  While this is the *typical* use pattern, it is not the only way to do things. For example:

  - Forms can be created using tools other than Build or XLSForm
  - Forms can be transfered directly to Collect, without using Aggregate

  ODK is a very flexible set of tools, and organizations will find their own best practices for adopting it.

.. _install-collect:

Install Collect
---------------------

The easiest way to install the ODK Collect App is `to get it from the Google Play store <https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_.

For other installation options, see :doc:`collect-install`.

.. _installing-aggregate:

Install Aggregate
---------------------

The easiest, recommended way to setup an ODK Aggregate instance is to use `Google App Engine <https://cloud.google.com/appengine/>`_ and the `ODK Aggregate Installer <https://opendatakit.org/downloads/download-category/aggregate/>`_.

You'll set up a new Google Cloud project, and then run the install utility locally. This will connect to your Google Cloud account and install Aggregate there.

For full details, and other installation methods, see the :doc:`ODK Aggregate Installation and Setup Guide <aggregate-install>`.

You can also watch `this video <https://www.youtube.com/watch?v=uZYInkghbCo/>`_ which explains the installation procedure of ODK Aggregate on Google App Engine and also this `Aggregate tutorial video <https://www.youtube.com/watch?v=ceEC9RZiIiA&list=PLRRSiEabNvxtzLqIKlMOQaTByxH-REEuM&index=5/>`_ which describes few of its functionalities. 

.. change to
    :ref:`ODK Aggregate Installation and Setup Guide <aggregate-install-guide>`.
    once that section is completed

.. _intro-odk-build:

Create and Upload Survey Forms with ODK Build
-----------------------------------------------

The quickest and easiest way to start using your own survey forms is to create them online with `ODK Build <https://build.opendatakit.org/>`_. To create a form, you can follow the steps below or watch this `tutorial <https://www.youtube.com/watch?v=LPdG3rKDzpo/>`_ which explains the creation process.

- Go to `build.opendatakit.org <https://build.opendatakit.org/>`_, create a new account, and log in.
- Once logged in, a blank survey is created. Give it a name (:guilabel:`rename` in the upper left-hand corner) and add a few questions (click on question types in the :guilabel:`+Add New` bar along the bottom).
- Once your new form is complete, go to :menuselection:`File --> Upload form to Aggregate...` to upload your form.

.. tip::

  - ODK Build is a great tool for simple forms. For more complex forms, try `XLSForm <http://xlsform.org/>`_.
  - ODK Build can also be run locally. `Desktop versions are available for download here <https://opendatakit.org/downloads/download-category/build/>`_.

.. link to list of more form design options

.. _using-collect-intro:

Load, Complete, and Upload a Form with ODK Collect
----------------------------------------------------------

- :doc:`Install <collect-install>` and open ODK Collect on your Android device.
- Open the :guilabel:`⋮` menu and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- Edit the server settings to connect to your ODK Aggregate instance.
- Go back to the app home screen and select :guilabel:`Get Blank Form`, then select your form.
- Select :guilabel:`Fill Blank Form` to complete a survey.
- Select :guilabel:`Send Finalized Form` to upload your completed survey to ODK Aggregate.


Now, you should be able to log back into your ODK Aggregate instance and see your completed survey results.
