.. spelling::

  clickjacking
  dateTime
  datetime
  init
  itemset
  JBoss
  jr
  memcache
  Memcache
  myformid
  NaN
  Nan
  pgAdmin
  Resteasy
  ui
  yyyymmddnn

Upgrading Aggregate
=====================

.. _upgrade-aggregate:

Need for Upgrading
--------------------

It is important to upgrade to newer ODK Aggregate versions as they come out. You don't need to do this immediately, but this should be something you do at least once a year.

There are several reasons for this.

Security vulnerabilities
~~~~~~~~~~~~~~~~~~~~~~~~~

The ODK developers are constantly upgrading the libraries we use with newer, safer, versions. The older your software, the greater the number of vulnerabilities in it.

Hosting revisions
~~~~~~~~~~~~~~~~~~~~

If you are using Google App Engine as we recommend, your hosting environment is being continuously updated.

Google AppEngine is a managed environment, unlike AWS or other "bare-box" hosting services. Google is continuously updating features and removing support for older features in this environment. 

The Aggregate development team is committed to supporting Google App Engine, so we update our application as the platform changes. If you do not upgrade gradually as new versions come out, your installation may stop working or cease to have a viable upgrade path.

Performance improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~

As we find performance issues and address them, the Aggregate gets faster and cheaper to run.

Enhanced capabilities
~~~~~~~~~~~~~~~~~~~~~~

:doc:`javarosa`, the underlying form rendering library is updated about annually. Those updates add new functions, features, and occasionally data types. New features are slowly added to ODK Aggregate, too.

To use these newer features, keep your Aggregate installation up to date.

.. _determine-version:

Determining your Aggregate version
-----------------------------------

If you are able to log onto the server as a Site Administrator, the ODK Aggregate version is displayed at the top of the :guilabel:`Preferences` sub-tab under the :guilabel:`Site Admin` tab.

If you are unable to log onto your server, you will need to search for the version in the application logs. To do that:

1. Open a browser to https://appengine.google.com.
2. Choose the project id for your ODK Aggregate server by clicking on the project dropdown in the top left corner.

.. image:: /img/aggregate-upgrade/dropdown.*
   :alt: Image showing dropdown option.

.. image:: /img/aggregate-upgrade/select-project.*
   :alt: Image showing project selection window.   
 
3. Search `logs` in the search box and select `logging`.

.. image:: /img/aggregate-upgrade/search-logs.*
   :alt: Image showing searching log.

4. In the filter text box paste this text : `afterPropertiesSet` and hit enter.
5. Expand the list of logs and find the log which shows the version of Aggregate. It will of the following format:

.. code-block:: none

   13:24:54.806 org.opendatakit.common.security.Realm afterPropertiesSet: Version: v1.4.15 Production (Realm.java:51)

.. image:: /img/aggregate-upgrade/find-version.*
   :alt: Image showing search result for version.  

.. note::

    In the 1.0 Production release, the Version appears on the :guilabel:`Site Admin` Tab, under the :guilabel:`Preferences` sub-tab. If no version information is displayed even after you log in, then you are running an extremely old version of ODK Aggregate; in that case follow this cheat sheet:

    - `Beta 1 and earlier`: :guilabel:`Permissions` tab looks nothing like the tab in the Production release.
    - `Beta 2`: :guilabel:`Permissions` tab looks like the Production release; Forms tab does not show the number of media files associated with a form.
    - `Beta 3`: The number of media files associated with a form is displayed; publishing to Google is broken.
    - `Beta 4`: There are :guilabel:`Form Management` and :guilabel:`Site Admin` tabs; publishing to Google is broken.
    - `RC1`: csv exports apply the active Filter to the exported columns; publishing to Google is broken.
    - `RC2`: :guilabel:`Submissions` tab is paginated (shows 500 records per page by default); publishing to Google works.
    - `RC3`: kml exports apply the active Filter to the exported data. All data is exported. It no longer truncates to the first 500 records.
    - `RC4`: Submissions for forms with non-repeating groups are now properly reconstructed into Briefcase. Date fields are broken.
    
    
    Publishing to Google is broken prior to RC2 (due to a change in Google infrastructure).
    
.. _general-steps-for-upgrading-aggregate:

General steps for upgrading
------------------------------------

#. Disable all submissions to ODK Aggregate, in the :guilabel:`Form Management` tab.
#. Use :doc:`ODK Briefcase  <briefcase-using>` to pull a copy of all data to your computer. 
#. Log onto your server to confirm that it is still functioning.
#. Download the next ODK Aggregate version and upgrade to that version.
#. Log onto your server to confirm that it is still functioning.
#. Repeat the steps 3-6 until you have upgraded to the current version.
#. Enable submissions to ODK Aggregate via the :guilabel:`Form Management` tab.

.. tip::

  You need to know the exact *instance name* that was used in prior installs for your username and password to continue to work. If you add a space or change capitalization or spelling, the passwords will be invalid (you just need to re-run the installer with the correct string to correct the problem).

  
.. _downgrade-steps:

Downgrade steps
-----------------

On April 12, 2016, Google disabled the login mechanism used by the older update scripts that were packaged with these installers.

To use these older installers:

1. Download and run an ODK Aggregate 1.4.8 (or newer) installer. On the final screen, uncheck the :guilabel:`Launch upload tool (3-10 minutes)` checkbox and click :guilabel:`Finish`.
2. Go into the directory where the installer placed the files, go into the :file:`ODK Aggregate` directory, and rename the :file:`ODKAggregate` directory inside it to *NewRemoval*.
3. Download and run the pre-1.4.8 ODK Aggregate installer. On the final screen, uncheck the :guilabel:`Launch upload tool (3-10 minutes)` checkbox and click :guilabel:`Finish`.
4. Go into the directory where the pre-1.4.8 installer placed its files, go into the :file:`ODK Aggregate` directory, and copy the :file:`ODKAggregate` directory from there to the installer directory created by the newer installer (effectively replacing the configuration produced by the newer installer with the configuration produced by the older one).
5. In the directory created by the newer installer, if on:
   
   - *Windows*: double-click the :file:`ODKAggregateAppEngineUpdater.jar` and use that to update your App Engine instance.
   - *Mac OSX*: double-click the :file:`uploadAggregateToAppEngine.app` file in that directory.
   - *Linux*: open a bash shell, navigate to this directory, and run the :file:`uploadAggregateToAppEngine.sh` file.

.. note::

   If you are reverting from a 1.4.8 or later release to a 1.4.7 or earlier release, you must manually delete the background module of your App Engine using the Google Cloud Platform administration web pages.
