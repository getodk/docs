.. spelling:word-list::
    yyyy

Trying ODK Web Forms
====================

ODK Central provides a web-based interface to your forms for data edits, to preview form definitions, and to enable data collection from devices other than Android phones. You can learn about how Central uses web-based forms in :ref:`the section on managing Submissions <central-web-submissions>`.

By default, web forms in Central are powered by `Enketo <https://enketo.org/>`_, a powerful library that was initially developed outside the ODK project and that the ODK team has contributed to.

The ODK team is now developing `ODK Web Forms <https://github.com/getodk/web-forms?tab=readme-ov-file#odk-web-forms>`_ which will eventually replace Enketo in ODK Central. ODK Web Forms is designed to align with ODK Collect and provide a modern user experience. This page describes how to opt into trying ODK Web Forms and documents its functionality.

To quickly try your forms in ODK Web Forms, see `the preview website <https://getodk.org/web-forms-preview/>`_. This page describes how to :ref:`opt a Central Form into using ODK Web Forms <web-forms-opt-in>` for all web-based functions and documents :ref:`more complex question types <web-forms-question-types>`.

.. _web-forms-opt-in:

Opting into ODK Web Forms in Central
----------------------------------------

.. warning::
    ODK Web Forms is experimental and does not support all form functionality! Please test your forms carefully. If you opt into using ODK Web Forms for real data collection, we encourage you to go to `the forum's release category <https://forum.getodk.org/c/releases/16>`_ and click on the bell so you are notified when there is a new release. Be sure to verify your forms after each Central release.

Starting in Central v2025.1, you can opt individual forms into using `ODK Web Forms <https://github.com/getodk/web-forms?tab=readme-ov-file#odk-web-forms>`_, an alternative to Enketo designed from the ground up to align with ODK Collect. ODK Web Forms is still early in its development. We recommend trying ODK Web Forms if:

* You are curious about how web forms will evolve in Central.
* You like ODK Web Form's look and feel.
* You want to provide feedback and ideas `on the forum <https://forum.getodk.org/tag/odk-webforms>`_.
* You have a form that doesn't work well with Enketo. For example, this could be because of the presentation of certain question types such as ``geopoint``, performance issues, or bugs in repeats.

To opt into ODK Web Forms, go to the :guilabel:`Settings` tab for a specific form. In the :guilabel:`Web Forms` section, select the :guilabel:`ODK Web Forms` option, read the description, and confirm that you want to opt in.

If you make some test submission using Web Forms and find that all of the functionality that you need is supported well, Web Forms can be used to collect real data.

You can see what functionality is currently supported `on Github <https://github.com/getodk/web-forms?tab=readme-ov-file#feature-matrix>`_. In particular, please note that the following sometimes subtle features are not yet supported:

* :ref:`Dynamic defaults <dynamic-defaults>` and the XLSForm ``trigger`` column
* :ref:`Metadata questions <metadata>`

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

Image
~~~~~~~~

.. image:: /img/web-forms/image-desktop.*
  :class: central-partial-screen

The :ref:`image question type <default-image-widget>` without appearance allows the user to capture an image. In Web Forms, if the user is on a mobile device, they can take a picture with their mobile camera. Devices like laptops that use a desktop browser will not show the capture button, even if they have a built-in camera.

Date
~~~~~

.. image:: /img/web-forms/calendar-yyyy-mm-dd.*
  :class: central-partial-screen

The :ref:`date question type <default-date-widget>` without appearance allows the user to enter a date. The user can manually type a date in the text field in the mm/dd/yyyy format or click in the field to select a date from a calendar. To change the year, they can press on the current year at the top of the calendar. To change the month, they can use the navigation arrows or press on the current month at the top of the calendar. There are also buttons to clear the date or jump to today.

.. _web-forms-selects-images:

Selects with images
~~~~~~~~~~~~~~~~~~~

.. seealso:: :ref:`Best practices for images <label-images-best-practices>`

When you specify :ref:`images for select options <image-options>`, Web Forms displays the options in containers to support visual processing and make selection easier.

.. image:: /img/web-forms/select-with-images.*
  :alt: Select with images in Web Forms

By default, choices with images are displayed in a grid. Each choice container is given the same width and height and the number of columns is determined by the screen width (this is the same as the :ref:`columns appearance <select-columns-widget>`). Images are never distorted or scaled up but they may be scaled down. The maximum image height used is 300 pixels. We recommend using a consistent size for all images and trying your form on the devices you plan to use for data collection.

If you would like to display one choice with image per row, as is the default for Collect, you can use the :ref:`columns-1 appearance <select-columns-n-widget>`.

Form styling
~~~~~~~~~~~~~

.. seealso:: :ref:`Markdown in forms <markdown-in-forms>`

You can style text such as notes, labels, hints, options, and validation messages using Markdown format.

.. image:: /img/web-forms/form-styling.*
  :alt: Styling in Web Forms

.. _web-forms-select-from-map:

Select one from map
~~~~~~~~~~~~~~~~~~~

.. versionadded:: Central v2025.3

The :ref:`select one from map question type <select-from-map>` allows users to select an option from choices displayed on a map. Each choice must include a ``geometry`` column in the ``choices`` sheet. The map uses OpenStreetMap as the base layer and supports zooming, panning, and tapping features to view details and make a selection.

.. image:: /img/web-forms/select-one-from-map.*
  :alt: Select one from map in Web Forms

When defining properties, keep the list concise and easy to read, as it appears in a compact popup on selection.

The following features are not supported yet:

- The ``quick`` appearance
- Offline tiles
- Map layer customization (e.g., switching to Google Maps or Mapbox, terrain or satellite views)
- Custom styling for points (``marker-color`` and ``marker-symbol``), lines (``stroke`` and ``stroke-width``) and shapes (``stroke``, ``stroke-width``, and ``fill``)
