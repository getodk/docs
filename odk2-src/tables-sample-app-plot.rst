Plot Demo
================

.. _tables-sample-app-plot:

For this portion of the tutorial we will explore the *Plot* demo. Select the tab labeled :guilabel:`Plot` and press :guilabel:`Launch Demo`.

  .. image:: /img/tables-sample-app/tables-sample-launch-plot.*
    :alt: Launch Plot Demo
    :class: device-screen-vertical

The *Plot* demo is a fictional collection of crop data and graphs of that data.

.. _tables-sample-app-graph-view:

Graph View
-------------------

After launching the *Plot* demo app, you will see a custom view that lets you select which crop data you want to see. Choose :guilabel:`View Plots`.

  .. image:: /img/tables-sample-app/tables-sample-plot-chooser.*
    :alt: Tables Sample Plot Selection
    :class: device-screen-vertical

The next screen is a *Map View* of the different sites in the records.

  .. image:: /img/tables-sample-app/tables-sample-plot-map.*
    :alt: Tables Sample Plot Map View
    :class: device-screen-vertical

Each site is meant to represent an area where crop growth and health is being tracked. This provides a convenient view of the locations of the sample sites, and would be a good use for the *Navigation View* if a user had trouble finding one of the sites. Choose the :menuselection:`Ungoni` site.

  .. image:: /img/tables-sample-app/tables-sample-plot-graph-original.*
    :alt: Tables Sample Plot Graph View
    :class: device-screen-vertical

The screen shows a *Graph View* of the crop height data collected for the *Ungoni* site. The bar graph shows corn crop heights across three different visits to this farm.

.. tip::

  The graph was rendered using the :program:`D3` JavaScript library. That library can render scatter plots, line graphs, graphs with error bars, and many other visualizations.

.. _tables-sample-app-graph-update:

Updated Graph View
~~~~~~~~~~~~~~~~~~~~~~

The graph was rendered on the device based on collected data. If new data is collected this graph will be updated. To demonstrate that, let's perform a new visit. Scroll down the page and press the :guilabel:`New Visit` button.

  .. image:: /img/tables-sample-app/tables-sample-plot-graph-new-visit.*
    :alt: Tables Sample Plot New Visit
    :class: device-screen-vertical

This will launch Survey to a form that the *Plot* application specified. Advance through the form. Notice that some of the fields are prepopulated, such as the plot being observed. Be sure to leave that set to :menuselection:`Ungoni`.

When you reach the prompt asking for crop height, enter: `130`.

  .. image:: /img/tables-sample-app/tables-sample-plot-survey.*
    :alt: Tables Sample Plot Survey
    :class: device-screen-vertical

Advance through the rest of the form, entering any data you like. Finalize the changes. When you return to the *Graph View* notice that a new visit has been added to the graph.

  .. image:: /img/tables-sample-app/tables-sample-plot-updated.*
    :alt: Tables Sample Plot Updated
    :class: device-screen-vertical

Tour the rest of the *Plot* demo to see a variety of other *Graph Views*. These are all rendered in custom JavaScript, and could be customized to your organization's unique needs.

Next launch the *JGI* Demo to see a demo of data collection directly through Tables.

.. _tables-sample-app-graph-view-learn-more:

Learn More
"""""""""""""""""""""

For more information about *Graph View*, view the :ref:`tables-using-view-data-graph` guide.
