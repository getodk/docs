Reducing Data Corruption and Boosting Performance
=================================================

.. warning::

  This document only applies ODK Aggregate v1.x. See `why we are removing App Engine support <https://forum.opendatakit.org/t/upcoming-changes-to-aggregate/17582>`_ for more information.

If you have many form definitions on your server, you may get better performance and reduce the likelihood of data corruption if you increase the size of your server.

.. _what-is-causing-data-corruption:

What is causing data corruption?
-------------------------------------

Data corruption is generally caused by the premature termination of an action (for example, saving of a submission) because it took longer than the allotted time.

The likelihood of data corruption is correlated with the following factors:

- quantity of form definitions on the server
- the size of the individual submissions
- the number of devices simultaneously submitting data
- the speed of the network.


Increasing the web server size enables it to handle larger workloads faster, which can reduce the likelihood of hitting this time limit, thereby avoiding data corruption.

.. _increase-server-size:

Increasing web server size
------------------------------

To change Google App Engine configuration, you must edit the configuration files produced by the installer and re-run the uploader script to push the changes to Google's servers.

There are two server settings that can be changed:

.. _increase-web-server-size:

Web Server Size
~~~~~~~~~~~~~~~~~~~

The web server handles all browser interactions and all data-submission and form-download requests from ODK Collect and ODK Briefcase. Increasing the size of the web server should reduce the likelihood of data corruption if it is not caused by slow network speeds.

To change the Google App Engine web server size:

1. Go to the folder you specified when you ran  the installer.
2. Within that folder, navigate to :file:`ODKAggregate/default/WEB-INF/appengine-web.xml` and open that file.
3. The file looks like this:

   .. code-block:: xml

     <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
       <application>opendatakit-simpledemo</application>
       <module>default</module>
       <version>1</version>

  	   <instance-class>F2</instance-class>
     ...

   To change the size of the web server, replace **F2** with a different instance class size.

   There are several different instance classes available. Select from among the instance classes beginning with the letter **F**. See `instance classes <https://cloud.google.com/appengine/docs/about-the-standard-environment#instance_classes>`_  for their descriptions or search for `Google App Engine instance classes standard environment` on the web.

4. Re-run the upload tool within the ODKAggregate folder.

   - Windows: double-click :file:`ODKAggregateAppEngineUpdater.jar`
   - Mac: double-click :file:`uploadAggregateToAppEngine.app`
   - Linux: double-click :file:`uploadAggregateToAppEngine.sh`

5. Once you have uploaded these changes to App Engine, your server will be running on the instance size that you have specified.

.. _increase-background-server-size:

Background Server Size
~~~~~~~~~~~~~~~~~~~~~~~~~

App Engine deployments use a "background" copy of the website to process long-running actions like generating CSV and KML files for export and for publishing all accumulated data to an external server.

If you experience difficulty exporting to CSV or KML, the size of that server will also need to be updated.


1. Go to the folder you specified when you ran  the installer.
2. Within that folder, navigate to :file:`ODKAggregate/background/WEB-INF` and open that file.
3. The file looks like this:

   .. code-block:: xml

       <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
	  <application>opendatakit-simpledemo</application>
	  <module>background</module>
	  <version>1</version>

	      <instance-class>B2</instance-class>
       ...

   To change the size of the server, replace **B2** with a different instance class size.

   There are several different instance classes available. Select from among the instance classes beginning with the letter **B**. See instance classes for their descriptions or search for `Google AppEngine instance classes standard environment` on the web as described in Web Server Size.

   4. Re-run the upload tool within the ODKAggregate folder.

   - Windows: double-click :file:`ODKAggregateAppEngineUpdater.jar`
   - Mac: double-click :file:`uploadAggregateToAppEngine.app`
   - Linux: double-click :file:`uploadAggregateToAppEngine.sh`

5. Once you have uploaded these changes to App Engine, your server will be running on the instance size that you have specified.

----

.. note::

  For data corruption caused by slow network speeds, you might also be able to change more aspects of the App Engine configuration (specified in these files) to make your web server always-available and to replace it with a Bx instance that does not have an automatic request time limit (the documentation provided by Google is currently unclear on whether this is still possible with the new services constructions).
