:og:image: https://docs.getodk.org/_static/img/tutorial-mapping-households.png

Power BI tutorial: Mapping households
=====================================

When surveying households, you may want to map each submission to visualize progress. In this tutorial, you'll learn to connect `Power BI <https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop>`_ to ODK Central to build a map of households that can be refreshed as new submissions arrive.

.. tip::

  * See `easily connect ODK to Power BI <https://www.youtube.com/watch?v=CDycTI-8TOc>`_ for a video using Power BI with ODK.

  * See `connecting Excel to ODK <https://forum.getodk.org/t/step-by-step-instructions-for-odata-use-with-excel-professional-2016/45118>`_ for instructions on using Excel with ODK.

  Power BI and Excel uses the same underlying technology (Power Query) to connect to Central's OData feed. Try both of the above resources to maximize your learning.

Goals
-----

* Connect ODK to Power BI
* Prepare location data for mapping
* Build a map that displays households

.. _tutorial-power-bi-connect:


Collect data with locations
---------------------------

.. warning::
   
   If you've never created an XLSForm before, complete the :doc:`XLSForm Tutorial <tutorial-first-form>` first.

#. Download this `Household Survey <https://docs.google.com/spreadsheets/d/1I3dpRRgdMWG83IjBsymwrN8nYouKyrEmww1KTI-TGiI/edit?usp=sharing>`_ as an .xlsx.
#. Upload the form into Central, publish it, connect your app user, and send in some sample data.


Connect ODK to Power BI
------------------------

#. In Central, find your form's OData link by clicking on the :guilabel:`Analyze via OData` button on the right side of the Submissions page.

   .. image:: /img/tutorial-mapping-households/analyze-odata.png

#. Once you click the button, you will see a popup. Copy the link starting with `https`.

   .. image:: /img/tutorial-mapping-households/odata-url.png
     :width: 450px

#. In Power BI, create a :guilabel:`Blank report`.

#. Select the :guilabel:`Home` menu, :guilabel:`Get data`, then :guilabel:`OData feed`.

   .. image:: /img/tutorial-mapping-households/get-data.png
     :width: 450px

#. Leave the feed type as :guilabel:`Basic` (not Advanced), copy and paste in the link from Central, then select :guilabel:`OK`.

   .. image:: /img/tutorial-mapping-households/odata-feed.png
     :width: 450px

#. Change the authentication type to :guilabel:`Basic` (not Anonymous), enter your Central email address and password, then :guilabel:`Connect`.

   .. image:: /img/tutorial-mapping-households/basic-auth.png
     :width: 450px


#. The :guilabel:`Navigator` window will now appear. Select :guilabel:`Submissions`, then :guilabel:`Transform Data`.

.. tip::

  If you are having trouble getting Power BI to connect, and especially if you see error messages about permissions or authentication, `clear your cached permissions <https://docs.microsoft.com/en-us/power-query/connectorauthentication#change-the-authentication-method>`_ and try again.


Prepare data for mapping
------------------------

Power BI doesn't understand OData locations, so we have to prepare the data before mapping.

#. Select your `primary_entrance` column.

#. In the :guilabel:`Transform` menu, select :guilabel:`Extract`, then :guilabel:`Text Between Delimiters`.

   .. image:: /img/tutorial-mapping-households/text-between-delimiters-menu.png

#. Use `(` as the start delimiter and `)` as the end delimiter then select :guilabel:`OK`.

   .. image:: /img/tutorial-mapping-households/text-between-delimiters.png
     :width: 450px

#. In the :guilabel:`Transform` menu, select :guilabel:`Split Column`, then :guilabel:`By Delimiter`.

   .. image:: /img/tutorial-mapping-households/split-column-delimiter-menu.png

#. Use `Space` as the delimiter then select :guilabel:`OK`.

   .. image:: /img/tutorial-mapping-households/split-column-delimiter.png
     :width: 300px

#. You will now have three columns" `primary_entrance.1`, `primary_entrance.2`, `primary_entrance.3`. Right-click each column and rename them accordingly:

   * `primary_entrance.1` -> `primary_entrance.longitude`
   * `primary_entrance.2` -> `primary_entrance.latitude`
   * `primary_entrance.3` -> `primary_entrance.altitude`

   .. image:: /img/tutorial-mapping-households/rename-columns.png

#. In the :guilabel:`File` menu, select :guilabel:`Close and Apply`.

   .. image:: /img/tutorial-mapping-households/close-apply.png
     :width: 450px

#. Switch to :guilabel:`Table View`, select :guilabel:`Column tools`, then set the :guilabel:`Data category` accordingly:

   * `primary_entrance.longitude` to :guilabel:`Longitude`
   * `primary_entrance.latitude` to :guilabel:`Latitude`

   .. image:: /img/tutorial-mapping-households/data-category.png


Display households on the map
-----------------------------

#. Switch to :guilabel:`Report view` and make sure you can see your :guilabel:`Visualizations` and :guilabel:`Data` panes.

   .. image:: /img/tutorial-mapping-households/expand-panes.png

#. Select :guilabel:`Map`, and drag the visualization's bottom-left corner to fill the screen.

   .. image:: /img/tutorial-mapping-households/map.png

#. Drag `primary_entrance.latitude` from the :guilabel:`Data` pane to the :guilabel:`Latitude` section of the :guilabel:`Visualization` pane. Do the same for `primary_entrance.longitude`.

   .. image:: /img/tutorial-mapping-households/map-locations.png

#. Drag `household_name` from the :guilabel:`Data` pane to the :guilabel:`Tooltips` section of the :guilabel:`Visualization` pane. It will show up as `First household_name`. Rename to just `household_name`.

#. Now, as new submissions arrive, you can select :guilabel:`Home`, then :guilabel:`Refresh` to get the latest data.

   .. image:: /img/tutorial-mapping-households/refresh.png

#. You can now mouseover each submission to see `household_name` and `primary_location`. Enjoy your map!

   .. image:: /img/tutorial-mapping-households/map-final.png

Your turn
----------
#. Can you change the color of the point based on `electricity_access`?
#. Can you filter to only show approved submissions in the last 10 days?
#. Can you add another page with `household_name` on the X-axis and `children_under_five` on the Y?