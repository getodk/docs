ODK Collect
================

.. _collect-introduction:

:dfn:`ODK Collect` is an Android app for managing and filling out forms. It supports a wide range of question and answer types, and is designed to work well offline.

ODK Collect downloads blank forms from and submits filled forms to a server. It displays forms as input prompts that can include logic, constraints, and repeating sub-structures. Users work through the prompts and can save their data at any point.

Collect supports location, audio, images, video, barcodes, signatures, multiple-choice, free text, and numeric answers. It can even accept answers from other apps on your device. :doc:`See a complete list of supported question types here.  <form-question-types>`

.. image:: /img/collect-intro/register-household.*
  :alt: Household registration form
  :class: device-screen-vertical side-by-side
.. image:: /img/collect-intro/map-plot.*
  :alt: Capturing a polygon on a map.
  :class: device-screen-vertical side-by-side

.. _collect-supported-devices:

Supported devices
-------------------

You can use Collect with a wide range of Android devices and the only requirement is that they must run Android 5 or above. That said, we generally recommend using Android 10 or higher for the best :doc:`security <collect-security>` and performance.

The device specification that will make the biggest difference for Collect performance is RAM. For forms with a lot of complex :doc:`logic <form-logic>`, many :ref:`repeat instances <repeats>`, or 60k+ elements in a choice list, Entity List or attached data file, we recommend aiming for devices with at least 4 GB of RAM. Devices with less RAM will likely work even for complex forms but may feel slow and even occasionally crash.

.. _collect-intro-learn-more:

Learn more about ODK Collect
--------------------------------

- :doc:`getting-started`
- :doc:`collect-setup`
- :doc:`collect-using`
