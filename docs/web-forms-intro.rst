Trying ODK Web Forms
====================

ODK Central provides a web-based interface to your forms for data edits, to preview form definitions, and to enable data collection from devices other than Android phones. You can learn more about :ref:`how Central uses web-based forms <central-web-submissions>`.

By default, web forms in Central are powered by `Enketo <https://enketo.org/>`_, a powerful library that was initially developed outside the ODK project and that the ODK team has contributed to.

The ODK team is now developing `ODK Web Forms <https://github.com/getodk/web-forms?tab=readme-ov-file#odk-web-forms>`_ which will eventually replace Enketo in ODK Central. ODK Web Forms is designed to align with ODK Collect and provide a modern user experience. This page describes how to opt into trying ODK Web Forms and documents its functionality.

To quickly try your forms in ODK Web Forms, see `the preview website <https://getodk.org/web-forms-preview/>`_. This page describes how to :ref:`opt a Central Form into using ODK Web Forms <web-forms-opt-in>` for all web-based functions and documents :ref:`more complex question types <web-forms-question-types>`.

.. _web-forms-opt-in:

Opting into ODK Web Forms in Central
----------------------------------------

.. warning::
    ODK Web Forms is experimental and does not support all form functionality! Please test your form carefully.

Starting in Central v2025.1.0, you can opt individual forms into using `ODK Web Forms <https://github.com/getodk/web-forms?tab=readme-ov-file#odk-web-forms>`_, an experimental replacement for Enketo designed from the ground up to align with ODK Collect. ODK Web Forms is still early in its development. We recommend trying ODK Web Forms if:

* You are curious about how web forms will evolve in Central.
* You want to provide feedback and ideas `on the forum <https://forum.getodk.org/tag/odk-webforms>`_.
* You have a form that doesn't work well with Enketo. For example, this could be because of the presentation of certain question types such as ``geopoint``, performance issues, or bugs in repeats.

To opt into ODK Web Forms, go to the :guilabel:`Settings` tab for a specific form. In the :guilabel:`Web Forms` section, select the :guilabel:`ODK Web Forms` option, read the description, and confirm that you want to opt in.

You can see what functionality is currently supported `on Github <https://github.com/getodk/web-forms?tab=readme-ov-file#feature-matrix>`_. In particular, please note that the following sometimes subtle features are not yet supported:

* :ref:`Dynamic defaults <dynamic-defaults>` and the XLSForm ``trigger`` column
* :ref:`Metadata questions <metadata>`
* Entity creation or update
* References to form fields in translated labels and hints (this works for single-language forms)

You can change a form's setting between Enketo and Web Forms at any time. Any form links that users already have will continue to work and will reflect the setting on the server at the time that the user loads the form link. Existing submissions are not affected by switching between web forms libraries.

.. _web-forms-question-types:

Question types
--------------

To know which question types are currently supported in Web Forms, see `the Github feature matrix <https://github.com/getodk/we
b-forms?tab=readme-ov-file#feature-matrix>`_. While most supported functionality is very similar to Collect's, this section describes question types with more complex functionality or that differ from Collect.

Geopoint
~~~~~~~~

The :ref:`geopoint question type <geopoint-widget>` without appearance captures the current location of the device. Currently, this is the only location experience provided by Web Forms, including for edits. In the future, there will be a map-based interface accessible by setting different ``appearance`` values. Additionally, it will be possible to use a map to view and edit a location captured by the default geopoint question type.

When a form includes a geopoint question, users of the form will see a :guilabel:`Get location` button. When a user taps that button, a dialog will appear, showing the accuracy of the currently-available location or no value if location permissions are not granted yet. If location permissions are not granted yet, the user will also be asked to grant location permissions by their browser.

.. image:: /img/web-forms/geopoint-permission.*
  :alt: Web Forms location permissions request

.. warning::
  
  Different browsers manage location permissions differently. Some may not prompt for the permission and may require users to go to their settings to grant location access.

  If a user denies location permissions to a form, that permission will apply for all forms on that server and a user may need to go to browser settings to grant the permission.

Once location permissions are granted to Web Forms, it will start reading location data from available sensors on the device. The current location accuracy will be displayed along with qualitative information about that accuracy to help guide the person filling out the form to get the highest accuracy point possible. Location will continue to update until the user taps the :guilabel:`Save location` button or the accuracy reaches the target accuracy defined by the form, whichever comes first. The target accuracy is the value in the "Location will be saved at N m" message.

.. image:: /img/web-forms/geopoint-refining-accuracy.*
  :alt: Web forms location-finding dialog
  :class: central-partial-screen

Image
~~~~~~~~

The :ref:`image question type <default-image-widget>` without appearance allows the user to capture an image. In Web Forms, if the user is on a mobile device, they can take a picture with their mobile camera. Devices like laptops that use a desktop browser will not show the capture button, even if they have a built-in camera.

Date
~~~~~

The :ref:`date question type <default-date-widget>` without appearance allows the user to enter a date. The user can manually type a date in the text field in the mm/dd/yyyy format or click in the field to select a date from a calendar. To change the year, they can press on the current year at the top of the calendar. To change the month, they can use the navigation arrows or press on the current month at the top of the calendar. There are also buttons to clear the date or jump to today.
