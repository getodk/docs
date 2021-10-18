.. spelling::

  geotagging

Geotagger Demo
==================

.. _tables-sample-app-geotagger:

For this portion of the tutorial, we will explore the *Geotagger* demo. Select the tab labeled :guilabel:`Geo` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-geo.*
    :alt: Launch Geotagger
    :class: device-screen-vertical

The *Geotagger* demo is a mapping of sites around the city of Seattle (and anywhere else anyone has recorded and uploaded to the server).

.. _tables-sample-app-navigate-view:

Navigate View
-----------------------

After launching the *Geotagger* demo app, you will see a *Map View* of the points in Seattle, or possibly a larger space. To switch to *Navigate View*, tap the lined paper icon in the upper right and choose :menuselection:`Navigate`.

  .. image:: /img/tables-sample-app/tables-sample-launch-navigate.*
    :alt: Launch Navigate
    :class: device-screen-vertical

You will see the same map on the bottom portion of the screen, but the top will be replaced by a compass and heading readouts.

  .. image:: /img/tables-sample-app/tables-sample-navigate-no-point.*
    :alt: Tables Sample Navigate View
    :class: device-screen-vertical

As you turn, the compass should update. If you select a point, the compass will add an arrow pointing towards the selected point from your current orientation. The :guilabel:`Distance` and :guilabel:`Heading` values should fill in as well and update as you move around.

  .. image:: /img/tables-sample-app/tables-sample-navigate-point.*
    :alt: Tables Sample Navigate View
    :class: device-screen-vertical

The *Navigate View* can be useful if you have loaded geopoints into your database (either preloaded or collected in the field) and you need to find your way to these points. It can be integrated into other workflows to navigate a worker to a point and then launch them into another data collection activity.

.. tip::

  The *Geotagger* demo also has a more complex *Map View* example. If you select *Map View* and tap on a map marker, that location will be highlighted in the *List View* on the top of the screen and it will expand to give you more information about it. This more sophisticated behavior is all performed in the JavaScript and HTML files.

Next, launch the *Plot* Demo.

.. _tables-sample-app-navigate-view-learn-more:

Learn More
~~~~~~~~~~~~~~~~~~~~

For more information about *Navigate View*, view the :ref:`tables-using-view-data-navigate` guide.


