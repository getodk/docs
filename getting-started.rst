Getting Started Guide
=========================

.. _what-is-odk:

What is ODK?
--------------

Open Data Kit (ODK) is a suite of open source applications that help organizations engaged in enumerator-mediated data collection. ODK tools assist with the collection and management of survey data using mobile forms. These include the primary ODK applications:

- **ODK Collect**, an Android mobile app that replaces paper-based forms.
- **ODK Aggregate**, a server-side data storage and analysis tool.

Also part of the ODK suite are several tools that support form creation and data management:

- **ODK Build** lets you design forms with a drag-and-drop form interface.
- **ODK XLSForm** lets you design forms in Excel.
- **ODK Validate** validates forms against the ODK XForms specification.
- **ODK Form Uploader** uploads blank forms and their media files to ODK Aggregate.
- **ODK Briefcase** packages and transfers data between instances of Collect and Aggregate.

ODK also maintains libraries and specifications that support these applications.

- **ODK XForm** is a subset of the W3 XForm specification, for use in the ODK ecosystem.
- **ODK JavaRosa** is a Java library that renders forms complying with the ODK XForm specification.

For a complete list of our projects, check out `Open Data Kit on Github <https://github.com/opendatakit>`_.

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

- :ref:`Installing Collect on a device or other mobile device <installing-collect>`
- :ref:`Installing Aggregate on a server <installing-aggregate>`

.. tip::

  While this is the *typical* use pattern, it is not the only way to do things. For example:

  - Forms can be created using tools other than Build or XLSForm
  - Forms can be uploaded directly to Collect, without using Aggregate

  ODK is a very flexible set of tools, and orgnizations will find their own best practices for adopting it.

.. _installing-collect:

Installing Collect
---------------------

- **Recommended:** `The ODK Collect App is available in the Google Play store <https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_.
- You can also download from the web and install manually:

  - From your device's application drawer, choose :guilabel:`Settings`, then :guilabel:`Applications`. Make sure Unknown sources is checked.
  - Return to the application drawer and choose :guilabel:`Browser`. Navigate to `https://opendatakit.org/downloads/download-category/collect/ <https://opendatakit.org/downloads/download-category/collect/>`_ and download the ODK Collect APK.
  - In the download window, you will see ODK_Collect_vN.N.N.apk. - Select it to download the file.

    - On older devices, the APK will automatically install after you approve the security settings.
    - On newer devices, you must go to the download list, rename the file to restore the .apk extension (the extension will have been renamed to .man during the download process), then click on it to install it.

.. note::

  On older Android devices (4.0 and earlier) ODK Collect required an external SD Card. This is no longer an issue because Android devices have internal storage. Virtually all current Android devices will run ODK Collect.

.. tip::

  You can also `install ODK Collect on an Android emulator <https://github.com/opendatakit/opendatakit/wiki/DevEnv-Setup>`_. However, this can be slow and buggy, and is not recommended.

.. _installing-aggregate:

Installing Aggregate
---------------------

The easiest, recommended way to setup an ODK Aggregate instance is to use `Google App Engine <https://cloud.google.com/appengine/>`_ and the `ODK Aggregate Installer <https://opendatakit.org/downloads/download-category/aggregate/>`_.

You'll set up a new Google Cloud project, and then run the install utility locally. This will connect to your Google Cloud account and install Aggregate there.

For full details, and other installation methods, see the `ODK Aggregate Installation and Setup Guide <https://opendatakit.org/use/aggregate/>`_.

.. change to
    :ref:`ODK Aggregate Installation and Setup Guide <aggregate-install-guide>`.
    once that section is completed

.. _intro-odk-build:

Create and Upload Survey Forms with ODK Build
-----------------------------------------------

The quickest and easiest way to start using your own survey forms is to create them in online with `ODK Build <https://build.opendatakit.org/>`_.

- Go to `build.opendatakit.org <https://build.opendatakit.org/>`_, create a new account, and log in.
- Once logged in, a blank survey is created. Give it a name (:guilabel:`rename` in the upper left-hand corner) and add a few questions (click on question types in the :guilabel:`+Add New` bar along the bottom).
- Once your new form is complete, go to :menuselection:`File --> Upload form to Aggregate...` to upload your form.

.. tip::

  - ODK Build is a great tool for simple forms. For more complex forms, try `ODK XLSForm <http://xlsform.org/>`_.
  - ODK Build can also be run locally. `Desktop versions are available for download here <https://opendatakit.org/downloads/download-category/build/>`_.

.. link to list of more form design options

.. _using-collect-intro:

Load, Complete, and Upload a Form with ODK Collect
----------------------------------------------------------

- :ref:`Install <installing-collect>` and open ODK Collect on your Android device.
- Open the :guilabel:`⋮` menu and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- Edit the server settings to connect to your ODK Aggregate instance.
- Go back to the app home screen and select :guilabel:`Get Blank Form`, then select your form.
- Select :guilabel:`Fill Blank Form` to complete a survey.
- Select :guilabel:`Send Finalized Form` to upload your completed survey to ODK Aggregate.


Now, you should be able to log back in to your ODK Aggregate instance and see your completed survey results.
