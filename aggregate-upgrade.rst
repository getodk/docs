*******************
Aggregate Upgrade
*******************

.. _upgrade-aggregate:

Need for Upgrading
--------------------

It is important to upgrade to newer ODK Aggregate versions as they come out (not necessarily immediately, but this should be something you do at least once a year).

There are several reasons for this:-

- **Security vulnerabilities** - we (and Google) are constantly upgrading the libraries we use with newer, safer, versions. The older your software, the greater the number of vulnerabilities in it.
- **Hosting revisions** - Google AppEngine is a managed environment, unlike, say, AWS or other "bare-box" hosting services. Google is continuously updating features and removing support for older features in this environment. If you don't upgrade, there may not be an upgrade path that works due to these changes -- unlike "bare-box" hosting, you, and the ODK team, only have partial control over the software and hardware environment.
- **Performance revisions** - as we find performance issues and address them, the tools get better and faster.
- **Enhanced capabilities** - the form-processing library (javarosa) has roughly-annual updates to add new functions (e.g., sin(), cos()) and occasionally data types. And new features are slowly added to ODK Aggregate, too.

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
    
.. _general-steps:

General steps
---------------

1. Disable all submissions to ODK Aggregate via the :guilabel:`Form Management` tab.
2. Use :doc:`ODK Briefcase <briefcase-forms>` to pull a copy of all data to your computer.
3. Search upward in the :ref:`release notes <release-notes>` below, starting from your current ODK Aggregate version to locate the most recent ODK Aggregate version that does not require any manual upgrade steps. 
4. Log onto your server to confirm that it is still functioning.
5. Download the next ODK Aggregate version, perform the manual upgrade steps if any and upgrade to that version (and perform any post-install upgrade steps, if any).
6. Log onto your server to confirm that it is still functioning.
7. Repeat the steps 3-6 until you have upgraded to the current version.
8. Enable submissions to ODK Aggregate via the :guilabel:`Form Management` tab.

.. tip::

  You need to know the exact *instance name* that was used in prior installs for your username and password to continue to work. If you add a space or change capitalization or spelling, the passwords will be invalid (you just need to re-run the installer with the correct string to correct the problem).

.. _release-notes:

Release notes
---------------

.. _v1.4.15:

Aggregate v1.4.15
~~~~~~~~~~~~~~~~~~~

1. Update javarosa to the new opendatakit-javarosa-2.3.0.jar.
2. Fix: rev 210 sync protocol. User permissions were incorrectly being computed and filtered. This prevented resetting the server with new content from the device (but syncing with existing content worked fine). 

.. note::

   The rev 210 sync protocol is incompatible with anything prior to rev 210.

.. admonition:: Upgrade notes
   :class: upgrade

   - Do not upgrade if you are using ODK 2.0 rev 208 or earlier.
   - See :ref:`v1.4.13 <v1.4.13>` upgrade notes.

.. _v1.4.14:

Aggregate v1.4.14
~~~~~~~~~~~~~~~~~~~

1. Update javarosa to the new opendatakit-javarosa-2.2.0.jar
2. Fix for JSON publisher correctly handling UTF-8
3. Added SHA-1 library to browser so that Basic Auth can now be configured and will now work (this capability is not exposed in the wizard-based installer/configurer; existing passwords need to be changed before they can be used in a Basic Auth configuration)
4. Revised sync protocol and database schema for ODK 2.0. This is incompatible with anything prior to rev 210 (not yet available).
5. Microsoft SQLServer configurations can now run on Linux and MacOSX boxes.
6. Updated to the latest AppEngine SDK.
7. Updated build environment to a mixed Java 7 and Java 8 environment.

.. admonition:: Upgrade notes
   :class: upgrade

   - Do not upgrade if you are using ODK 2.0 rev 208 or earlier.
   - See :ref:`v1.4.13 <v1.4.13>` upgrade notes.

.. _v1.4.13:

Aggregate v1.4.13
~~~~~~~~~~~~~~~~~~~~

1. Add support for Microsoft SQL Server database and Azure SQL Server
2. Updated to expect Tomcat 8 and JDBC 4 libraries. This extensively impacted the datastore layer.
3. Rewrote the Google Sheets publisher to use a newer API.
4. Changed the PAUSED publisher state to expose a restart button. Fixed bug that prevented ABANDONED button from working. When a publisher enters the Paused state, this button triggers ODK Aggregate to resume from that state. This happens automatically every 8 minutes or so, but having a resume button simplifies integration testing. i.e., when a publisher is in the Paused state, you do NOT need to click this button -- but if you are testing a publisher to your own server, it can be useful to have.
5. Fixes for ODK 2.0 datatype form.
6. NaN +Infinity and -Infinity are now handled within Google AppEngine. These cannot be supported on systems using MySQL and SQL Server (a fundamental limitation of those databases). On PostgreSQL systems, if you alter your tables to use REAL instead of DECIMAL(38,0) columns, it will be able to store and process these special values.
7. Updated a multitude of jars (libraries).
8. If this is a first-time install using PostgreSQL, please see the upgrade steps below for the additional commands you need to execute to complete the PostgreSQL configuration. These commands are missing from the :file:`create_db_and_user.sql` but are required for PostgreSQL operations.

.. admonition:: Upgrade notes
   :class: upgrade

   - If publishing to Google Sheets, you must go to the API Manager tab and enable the Google Sheets API.
   - Tomcat installs now require Tomcat 8 or higher. The war file produced by the installer will work as-is on those systems -- no need for any manual modifications to get things to work (though MySQL still requires downloading and copying the MySQL Connector/J, and SQL Server also has a manual configuration step).
   - If using an older MySQL database, please upgrade to MySQL 5.7 or higher; note that some MySQL releases expire all database passwords after 360 days. Please verify the behavior of your version of MySQL and either change the password expiration policy or create a calendar reminder to change the password before it expires. For ODK Aggregate, you will need to re-run the installer to specify any new password. For more information, see the MySQL documentation. e.g., `MySQL password expiration policy <https://dev.mysql.com/doc/refman/5.7/en/password-management.html>`_
   - The ODK 2.0 sync protocol in this release is compatible with the ODK 2.0 Rev 200, 202, 204, 206 and 208 tools. Note that you cannot just upgrade from a server earlier than 1.4.10; you have to delete everything and start over.
   - See :ref:`v1.4.12 <v1.4.12>` upgrade steps if upgrading from an earlier ODK Aggregate version.
   - If using an older PostgreSQL database, please upgrade to at least 9.4. For all PostgreSQL servers, you must execute an additional command to grant permissions to the schema on the server. This is a change from the earlier 9.1 install and the additional command is missing from the :file:`create_db_and_user.sql` script. The commands to be executed in the pgAdmin query window are as follows, with your_database, your_schema and database_username replaced with the values you specified when you ran the installer:

   .. code-block:: none

     \c "your_database";
     alter schema "your_schema" owner to "database_username";

.. _v1.4.12:

Aggregate v1.4.12
~~~~~~~~~~~~~~~~~~

1. Update to installer with new language and links to documentation.
2. Revise upload tool for Google AppEngine deployments to more-consistently display the token-entry dialog.
3. Add .csv-based downloading and bulk updating of configured users and their capabilities.
4. Change MySQL ODK 1.x and ODK 2.0 data table constructions to use MEDIUMBLOB columns for media attachments. Fix several issues around accessing attachments. See Upgrade notes below and MySQL configuration instructions in :ref:`installing Aggregate on Tomcat <install-tomcat>` for configuration that is required for MySQL.
5. Tweak Google AppEngine configuration to reduce frontend usage hours and thereby reduce costs.
6. Performance improvements to Google AppEngine task locks (primarily for ODK 2.0 support).
7. Add ``/users/list`` URL that returns the list of all configured users and the roles they have been granted. Access to this URL requires authentication and is restricted to ODK Aggregate usernames and Google accounts (anonymousUser access is forbidden). If the authenticated user does not have Tables Super-user, Administer Tables, or Site Administrator permissions, a singleton list is returned that contains only information about their own identity and its capabilities.
8. Changes to support row-level filtering in ODK 2.0.
9. Implement a paginated view of ODK 2.0 data rows; 100 records per page.
10. Upgrade to Google AppEngine 1.9.42 SDK.
11. The ODK 2.0 "datatypes" example form and table (in the app-designer repository) fail to upload to ODK Aggregate. This will be addressed in a future release.

.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration (if this is a new database install, you can reduce *max_allowed_packet* to *16842752*):

   .. code-block:: none

     character_set_server=utf8
     collation_server=utf8_unicode_ci
     max_allowed_packet=1073741824

   - For ODK 1.x uses, no special upgrade steps are required.
   - If you are using ODK 2.0 features, you must visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab and click :guilabel:`Save Changes` to complete the upgrade to this release. You do not need to modify anything on that page, just click the button.
   - The ODK 2.0 sync protocol in this release is compatible with the ODK 2.0 Rev 200, 202, 204, 206 and 208 tools. Note that you cannot just upgrade from a server earlier than 1.4.10; you have to delete everything and start over.
   - See :ref:`v1.4.11 <v1.4.11>` upgrade steps if upgrading from an earlier ODK Aggregate version.

.. _v1.4.11:

Aggregate v1.4.11
~~~~~~~~~~~~~~~~~~~~

1. Add a mutex around ODK 1.x form submission creation and updating. This should eliminate submission data corruption.
2. If only ODK 2.0 privileges are assigned, hide the Submissions tab.
3. Fix: advisory memcache interaction to delete the entry when rolling back the datastore update.
4. Add **Tables Super-user** as a configurable user capability. Users with this capability will be able to modify the table-level and row-level privileges on ODK 2.0 rev 206 data tables. These privileges are advisory and do not provide strong access or revision control.
5. Add ``/roles/granted`` URL that returns the roles granted to an authenticated username or google account. This will be used by ODK 2.0 rev 206 tools to determine and save the capabilities of the configured user on a device. Those capabilities are then used to apply advisory access controls on the tables and rows.


.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration:

   .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824

   - For ODK 1.x uses, no special upgrade steps are required.
   - If you are using ODK 2.0 features, you must visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab and click :guilabel:`Save Changes` to complete the upgrade to this release. You do not need to modify anything on that page, just click the button.
   - The ODK 2.0 sync protocol in this release is compatible with the ODK 2.0 Rev 200, 202 and 204 tools. You cannot just upgrade from a server earlier than 1.4.10; you have to delete everything and start over.
   - See :ref:`v1.4.10 <v1.4.10>` upgrade steps if upgrading from an earlier ODK Aggregate version.

.. _v1.4.10:

Aggregate v1.4.10
~~~~~~~~~~~~~~~~~~~~

1. On AppEngine, add advisory memcache interactions inside database mutex implementation (TaskLockImpl) to detect and thereby reduce race conditions that could lead to database corruption. These changes do not alter the fundamental mutex mechanism. They may reduce the likelihood of a mutex failure.
2. Fix ODK 2.0 sync: table-specific pre-loaded instance attachments under :file:`config/assets/csv/tableid/instances/...` were not being identified as table-specific.
3. Fix ODK 2.0 sync: add mutex around app-level file, table-level file and row-level attachment REST interactions. Eliminates the possibility of joint-updating that could corrupt the app-, table- or row-level manifests.
4. Fix ODK 2.0 sync: change row-level file attachment bulk-update to not refetch the manifest after adding each file attachment. This had caused 1% failure rate on row-level attachment syncing when there were large numbers of file attachments (30-60) for each row.
5. Fix ODK 2.0 sync: when authorization fails (permission denied), return UNAUTHORIZED response rather than DENIED. This reports an authorization failure on the client vs. a protocol error.

.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration:

   .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824
      
   - For ODK 1.x uses, no special upgrade steps are required.
   - The ODK 2.0 sync protocol is compatible with the ODK 2.0 Rev 200, 202 and 204 tools.
   - For ODK 2.0 uses, if you have pre-loaded datasets (via tables.init) that have row-level attachments (e.g., geotagger example dataset), you should:

     1. Remove these incorrectly-categorized files from the server (anything under :file:`assets/csv/table_id/instances/...` on the :guilabel:`Manage App Level Files` sub-tab)
     2. Deploy your device configuration to a clean device
     3. Reset App Server to correctly upload these files so that they appear under the :guilabel:`Manage Table Level Files` sub-tab.

.. _v1.4.9:

Aggregate v1.4.9
~~~~~~~~~~~~~~~~~~

1. Add XPath 3.1 math functions (e.g., exp, log, sin, cos, etc.)
2. Fix AppEngine adaptation layer for Apache HttpClient so that Oauth2 authentications work change version string in :file:`ODKAggregateAppEngineUpdater.jar` to be a date stamp.
3. Fix ODK 2.0 interfaces to support ODK Aggregate username / password for authentication.
4. Fix ODK 2.0 Sync so that a delete-table request can be repeated until successful or Not Found (404) when it times out.

.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration:

   .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824
      
   - For all other installations, there are no special upgrade steps required.
   - The ODK 2.0 sync protocol is compatible with the ODK 2.0 Rev 200, 202 and 204 tools.

.. _v1.4.8:

Aggregate v1.4.8
~~~~~~~~~~~~~~~~~

1. Submission Filters are once again working.
2. Update javarosa library with fixes for:
  
  - fix date, time, dateTime handling of time zones (in collaboration with SurveyCTO)
  - fix itemset choice lists -- various issues.
  - fix jr:choice-name() context resolution so that it can work with relative paths and repeat groups (SurveyCTO contribution).
  - add CONTROL_FILE_CAPTURE for future arbitrary-file-attachment handling
  - use consistent UTF-8 treatment when writing and reading files
  - better detection and handling of binary-file-format changes across versions
  - build with Java 7

3. Add support for geotrace and geoshape to Export-to-KML (for ODK 1.x).
4. Update Apache HTTP Client libraries to 4.5.2; this should support SNI protocol interactions of external publishers (ODK 1.x - untested).
5. Change Google App Engine update mechanism to use new wizard update tool.
6. Change Google App Engine code to use EAR / module format.
7. Widespread jar update.
8. Correct bug in csv-export library shared with ODK 2.0 tools for exporting datasets in those tools (does not impact Export as CSV in the 1.x toolchain).
9. Add new bulk attachment-POST APIs for ODK 2.0 sync protocol.
10. Rework ui tests to use Chrome for the Selenium web testing.
11. Rework all of the eclipse projects and add documentation for setting up a tomcat eclipse debug environment.
12. Rework the Google App Engine maven projects to use the EAR / module format.
13. Update maven plugins and tools to newer versions.

.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration:

   .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824
      
   - For all other installations, there are no special upgrade steps required.
   - The ODK 2.0 sync protocol is compatible with the ODK 2.0 Rev 200 and higher tools.

.. _v1.4.7:

Aggregate v1.4.7
~~~~~~~~~~~~~~~~~~

1. Submission Filters are broken in this release. When submissions rows are corrupted, consistently report the information necessary for end-users to delete or repair the corrupted submission. 
2. Correct ODK 2.0 delete-table functionality so that it does not generate errors when it is not running on AppEngine. The code had been performing an unguarded explicit cast to an AppEngine-only implementation class.

.. admonition:: Upgrade notes
   :class: upgrade

   - For MySQL installations, please make sure you have this server configuration:

   .. code-block:: none

      character_set_server=utf8
      collation_server=utf8_unicode_ci
      max_allowed_packet=1073741824
      
   - For all other installations, there are no special upgrade steps required.

.. warning::
   
   Google disabled functionality used by this installer and earlier versions to upload ODK Aggregate to Google App Engine. See :ref:`here <downgrade-steps>` for the work-around.

.. _v1.4.6:

Aggregate v1.4.6
~~~~~~~~~~~~~~~~~~

1. Submission Filters are broken in this release.
2. Fix for Google Sheets publisher-creation problem caused by April 20th deprecation of the Google Docs API. We were making a single call to that obsolete API to create a blank Google Sheets document.
3. Update to javarosa-2015-04-17 jar. That jar adds OpenStreetMap support to javarosa. Removal of the *Sign in with Google* mechanisms that used OpenID.
4. Widespread update to jars, custom repository configuration, and the elimination of several custom-built jars because of the elimination of OpenID and the maturity of Maven as a version repository.

.. admonition:: Upgrade notes
   :class: upgrade

   No special upgrade steps required.

Aggregate v1.4.5
~~~~~~~~~~~~~~~~~~~~

1. Update to javarosa-2015-01-10 jar.
2. Update to jQuery 1.11.1
3. Update the ODK 2.0 Data model and Sync protocol (incompatible with device releases: rev 122 and earlier).
4. Fix: support performing mark-as-complete on encrypted submissions (requires ODK Briefcase v1.4.5 or higher).
5. Fix: add server preference to ignore partially inserted/deleted submissions. Logs them but ignores them so that you can access all other rows in your dataset. Disabled by default. By default, all actions fail upon encountering any malformed submission. You should not ignore these failures but should correct them as soon as is practical.
6. Attempted fix: for *Log In* issue -- insert sleep to give Google a chance to propagate clearing of session cookie. Tweak the webpage resize/layout calculations to be more efficient.
7. Fix: make incomplete deletions and insertions more recoverable.
8. Performance: change MySQL table creation to not declare primary keys and just use ordinary indices for the primary key.
9. Security: Support Enketo-express (allow non-https communications with Enketo server). When the communications are not secure, this change discloses the Enketo access token to eavesdroppers.
10. Security: Filter out forbidden characters in redirect string to prevent XSS attacks.
11. Security: Add clickjacking prevention header as detailed here: https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet.

.. admonition:: Upgrade notes
   :class: upgrade

   If you were testing out ODK Tables, you should delete all ODK Tables files and data tables before upgrading, as the database schema has changed. The server no longer works with ODK Sync 2.0 rev 122 (or earlier releases).

.. _v1.4.4:

Aggregate v1.4.4
~~~~~~~~~~~~~~~~~~

1. Installer now asks for an ODK Aggregate username for the super-user (not a Google e-mail account). Default password is aggregate.
2. Banner displayed if super-user's password has not been changed from aggregate.
3. Fix: column name generator bug (upload of form definition failed)
4. Fix: add more detailed error messages when a submission is corrupted
5. IE6 and IE7 are no longer supported. Upgrade your browser.
6. Allow user to specify the ODK 2.0 App Name.
7. Allow anonymous access to ODK 2.0 Sync APIs.
8. Enforce *Administer Tables* access for ODK 2.0 Sync APIs that alter server configuration.
9. For ODK 2.0 Sync APIs, remove JBoss Resteasy; use Apache Wink instead.
10. Extensive version updates to supporting software libraries.
11. Update :file:`CONFIGURE.txt` instructions for maven builds. Define ANT scripts for external dependencies.

.. admonition:: Upgrade notes
   :class: upgrade
   
   Upgrades require several manual interventions:

   - You must have Java 7 installed - the GAE 1.9.7 SDK used within the installer now requires that version of Java. If you are upgrading from ODK Aggregate 1.4.3, you have already done this.
   - If you were testing out ODK Tables, you should delete all ODK Tables data tables before upgrading, as the database schema has changed.
   - You must flush the session cookies on the server. Session cookies are used to identify the logged-in users of the system. The security software versions were updated in this release, causing the older cookies to become invalid. See below for the upgrade steps.
   
   After performing the above steps, the upgrade steps after those are as follows:

   1. Open a browser and go to your `Google AppEngine dashboard <https://appengine.google.com/>`_.
   2. Click through to your application id. Then click on :guilabel:`Memcache Viewer` under the :guilabel:`Data` heading in the left sidebar. Keep this window open.
   3. Now, run the installer and deploy ODK Aggregate 1.4.4 to this application id.
   4. After it has deployed, click on :guilabel:`Flush Cache` in the dashboard window's Memcache Viewer screen.
   5. Follow the instructions :ref:`here <permission-tab>` for changing the password of the super-user username.
   
   Other than the need to flush this cache, and the need to delete any ODK Tables data before upgrading, this should be a seamless upgrade from ODK Aggregate 1.4.x.

.. _v1.4.3:

Aggregate v1.4.3
~~~~~~~~~~~~~~~~~~

1. Updated javarosa jar.
2. Add stub Tomcat/MySQL Eclipse project with readme.
3. Update selenium test environment and various 3rd party jars.
4. Update the GAE SDK inside the installer to 1.9.0.
5. New ODK Tables sync protocol and UI. Breaks ODK Tables Alpha 2 sync.
6. New sync protocol exchanges SAVEPOINT_TYPE, FILTER_TYPE, FILTER_VALUE.

.. admonition:: Upgrade notes
   :class: upgrade

   Upgrades require a manual intervention:

   1. You must have Java 7 installed - the GAE 1.9.0 SDK used within the installer now requires that version of Java.
   2. If you were testing out ODK Tables, you should delete all ODK Tables data tables before upgrading, as the database schema has changed.

   Otherwise, this should be a seamless upgrade from ODK Aggregate 1.4.

.. _v1.4.2:   

Aggregate v1.4.2
~~~~~~~~~~~~~~~~~

1. Fixes to ODK Tables sync protocol for the combined release. Due to interactions with Google AppEngine, the ODK Tables Synchronization protocol does not currently work on Google AppEngine servers. You must :ref:`install a local server or a VM image <install-vm>` in order to use that mechanism.

.. admonition:: Upgrade notes
   :class: upgrade

   If you were testing out ODK Tables, you should delete all tables before upgrading, as the database schema has changed.

   Otherwise, this should be a seamless upgrade from ODK Aggregate 1.4.

.. _v1.4.1:

Aggregate v1.4.1
~~~~~~~~~~~~~~~~~

1. You can now use `Enketo <https://enketo.org/>`_ browser-based Webforms to fill-in and publish submissions directly into ODK Aggregate. This feature was developed and donated by `SDRC India <http://sdrc.co.in/>`_. To enable Enketo integration, go to the :guilabel:`Preferences` sub-tab under :guilabel:`Site Admin` tab and click on :guilabel:`Enketo API Configuration`.
2. Fix the Z-ALPHA JSON publisher and the JSON File export to emit an array of zero or more objects, one object per submission, with proper treatment of embedded quotes, etc and confirmed that the output passes JSLint.
3. Fix the CVS File export functionality to double-up all occurrences of double-quotes in a field before surrounding that field with double quotes (per RFC 4180).
4. Clean up date and time handling in REDCap publisher and enforce GMT time zone interpretation when rendering date and time strings.
5. Various GWT interfaces have been changed to use concrete ArrayList types (reduces code size).
6. New permissions have been added in support of ODK Tables -- Synchronize Tables and Administer Tables and for most ODK Tables interactions, the user is required to have Synchronize Tables permissions.
7. Extensive changes to ODK Tables sync protocol and database structures. There will be further changes in the next update.
8. Fix sizing calculations and CSS so that the ODK logo does not get clipped or overwritten.

.. admonition:: Upgrade notes
   :class: upgrade

   If you were testing out ODK Tables, you should delete all tables before upgrading, as the database schema has changed.

   Otherwise, this should be a seamless upgrade from ODK Aggregate 1.4.

.. _v1.4:

Aggregate v1.4
~~~~~~~~~~~~~~~~

1. Changed behavior: simple JSON publisher now POSTs an application/json entity body; added option for how to treat binary content. Incompatible change; see Upgrading section if you were using the Z-ALPHA JSON Server
2. Changed representation: ODK Tabled storage schema has been revised. Incompatible change; see Upgrading section if you used your server to upload or download data to ODK Tables. Syncing with ODK Tables is broken in this release. Only v1.3.4 on Google AppEngine works with the ODK Tables alpha (we are in the middle of changing table schemas). 
3. Fix: file exports were not properly writing UTF-8 character sets.
4. Fix: PostgreSQL failures on some forms (column names must be less than 63 characters)
5. Upgrade Aggregate’s Google publishers to use the updated Oauth2 libraries (e.g., Google Fusion Tables, Google Spreadsheet). Publishing from Google Apps domains does not work (it never has). 
6. Add support for publishing data to Google Maps Engine.
7. Rework Spreadsheet and Fusion Table publishers to use Google libraries (consistent with the new Google Maps Engine publisher)
8. Additional active-paused state in publisher to extend the delay in publishing attempts (and reduce quota usage) if the destination publisher is reporting an error.
9. Improved how failures during form definition uploads are rolled back to increase the likelihood that the database is restored to a clean state.

.. admonition:: Upgrade notes
   :class: upgrade

   - You may need to clear your browser cache to complete the upgrade. If the browser screen flickers after upgrading, first clear your browser cache and reload the page.
   - If you were using the Z-ALPHA JSON Server, you must delete all instances of that publisher before upgrading. After upgrading, the updated publisher will send a single application/json entity body to the external server instead of a multi-part form containing that entity.
   - If you were using ODK Tables with ODK Aggregate, you need to delete all the ODK Tables data on ODK Aggregate before upgrading.

.. _v1.3.4:

Aggregate v1.3.4
~~~~~~~~~~~~~~~~~~ 

1. Fix for the v1.3.3 fix for Google AppEngine -- The original fix caused the creation of new publishers to Google Spreadsheets to fail, export to files to fail, form deletions to fail, and purge-sent-submissions actions to fail. This fix should rectify those issues.  

.. _v1.3.3:

Aggregate v1.3.3
~~~~~~~~~~~~~~~~~

1. Fix for Google AppEngine -- entity keys (unique identifiers assigned by Google AppEngine and used internally by ODK Aggregate) may now contain slashes. Submissions that have been assigned an entity key containing a slash were breaking the 'SubmissionKey' parsing used when publishing, retrieving images, accessing repeat groups, or retrieving submissions using ODK Briefcase.

.. _v1.3.2:

Aggregate v1.3.2
~~~~~~~~~~~~~~~~~~~

1. Expose the ODK Tables data and management tabs.
2. When installing for first time, ODK Aggregate will not require you to log in. Access restrictions are not altered when upgrading. This only affects new deployments. issue 710 (on Google Code) - upon an initial install, configure anonymousUser with Data Collector and Form Manager (and Data Viewer) permissions.
3. Watchdog sweep interval shortened to 30 seconds in fast-publishing mode (from 60 seconds). Ensure watchdog is scheduled to be fired when there are records remaining to be published.
4. Fix publisher failure to Google Spreadsheets and Fusion Tables by prepending 'n' to element names beginning with digits.
5. Fix publishing failure with Fusion Tables when a form with repeat groups has submissions without any repeats.
6. Fix publisher-creation failure that can cause cycling UI refresh.
7. Update javarosa library, adding format-date-time().
8. Update to selemium 2.33.0 to resolve Firefox ESR 17.0.7 failures.

.. _v1.3.1:

Aggregate v1.3.1
~~~~~~~~~~~~~~~~~~

1. Change watchdog to run more frequently if there is an active publisher. Provide a :guilabel:`disable` button on the Site Admin / Preferences page to restore older behavior (to conserve GAE quota).

.. warning::

   Following issues arise while using this version:

   - Form upload fails for some forms on MySQL with stack exhaustion.
   - Fix to simple JSON publisher had caused instability when used.
   - Popups don't show centered in screen when displayed on top of scrolling regions.
   - Forms with repeat groups cannot be versioned.
   - Rows-per-page value keeps getting reset on refresh.

.. _v1.3:

Aggregate v1.3
~~~~~~~~~~~~~~~~

1. Wholesale transition from OAuth 1.0 to OAuth 2.0, breaking all publishers.    
2. Installer now supports migrated AppEngine instances (for the Master-Slave -to- High-Replication Datastore migration).
3. Google Fusion Tables publisher now provides the links to the tables of all the repeat groups, the top-level record, and a left-outer-join view of the first repeat group and top-level record. This gives a 'flat' view of the data.
4. Google Spreadsheets and Google Fusion Tables publishers are now using OAuth 2.0 for authentication. This breaks all existing publishers (you need to republish). For more details on this, see :doc:`OAuth2-service <oauth2-service>`.
5. Google Maps v3 API is now used for the visualization features.
6. Added a *Published Through* and an *Owner* column to the *Published Data* table to communicate the progress of the publisher and who is receiving the data.
7. JSON file export now exports multiple-choice values as a JSON array of string values, rather than a space-separated string.
8. MySQL media attachments are stored as BLOB types, allowing the default MySQL configuration to work.
9. forms are now listed alphabetically
10. New additions:

        - Alpha release REDCap (XML) publisher
        - Alpha release Simple JSON publisher
        - Alpha release Ohmage JSON publisher

.. warning::

   Following issues arise while using this version:

   - Google Spreadsheet publisher failed badly if name was blank.
   - Extra comma in JSON file export (in repeat groups).
   - Arbitrary intermingling of http and https requests are problematic
   - Filters are not saved unless display metadata is checked.  
   - Title of existing form cannot be changed.

.. admonition:: Upgrade notes
   :class: upgrade

   After the upgrade, ODK Aggregate needs to be :doc:`configured with OAuth 2.0 credentials <oauth2-service>` on the Site Admin / Permissions page. Once configured, you will then be able to create new publishers for your data (it is not possible to resume or restore publishing to the original publishers).

   To avoid having to create new publishers that re-publish already-published data, follow these steps before upgrading:

   1. Go to the :guilabel:`Form Management` tab.
   2. Uncheck :guilabel:`Accept Submissions`.
   3. Verify that all submissions appearing on the :guilabel:`Submissions` tab have been successfully published to Fusion Tables and Google Spreadsheets.
   4. At this point, because ODK Aggregate is not accepting any new submissions, your surveyors are unable to send filled-in forms and we can be assured that no data is in transit during the upgrade process.
   5. Deploy ODK Aggregate 1.3.0.
   6. Go to the Publishers page, and create replacement publishers using :guilabel:`Stream New Submissions ONLY`.
   7. Now go to Fusion Tables or Spreadsheets and copy the data from the v1.2 tables into the newly-created publisher tables.
   8. Check :guilabel:`Accept Submissions` under the :guilabel:`Form Management` tab.
   9. At this point, new submissions will stream into the new publishers and you have manually copied the old data into the new publisher, so these new publishers will now have all of your data.

.. tip::

   The database tables for the new publishers and older publishers do not overlap, so if you roll back to the ODK Aggregate 1.2 release, you will not see the new publishers, but the earlier 1.2 publishers will 'reappear.' If you want to, after the upgrade, in MySQL or PostgreSQL, you can drop the unused old tables:

   - ``_server_preferences`` (has been replaced by ``_server_preference_properties``)
   - ``_form_service_cursor`` (has been replaced by ``_form_service_cursor_2``)
   - ``_fusion_table`` (has been replaced by ``_fusion_table_2``)
   - ``_fusion_table_repeat`` (has been replaced by ``_fusion_table_repeat_2``)
   - ``_google_spreadsheet`` (has been replaced by ``_google_spreadsheet_2``)
   - ``_google_spreadsheet_repeat`` (has been replaced by ``_google_spreadsheet_repeat_2``)

.. _v1.2:

Aggregate v1.2
~~~~~~~~~~~~~~~

1. Updated javarosa library with cascading select support (as with KoBo Collect).
2. Add a :guilabel:`Delete` button to the Exports list to enable deleting the generated files.
3. Exported files using filters now export the metadata if displayed by the filter.
4. Improved Map visualization display and pop-ups (showing images)
5. Improved filter, export and publishing pop-ups.
6. Update to use LONGBLOB and LONGSTRING on MySQL (new tables only).

.. note::

   The use of LONGBLOB and LONGSTRING requires a configuration change in the MySQL server. The server requires the transmisison packet size to be configured large enough to hold the largest LONGBLOB or LONGSTRING you will ever send to the server. See `this <https://dev.mysql.com/doc/connector-net/en/connector-net-programming-blob-serverprep.html>`_ for details.

   Alternatively, after creating your tables, you can use the MySQL ``ALTER TABLE`` command to change the LONGBLOB field to a BLOB field. This was the pre-1.2 setting, and will be the 1.2.1 setting for image fields, returning the system to use 65kB image chunks and avoiding the need to change the server configuration. If you do this, you will need to stop and restart your ODK Aggregate server for the change to be detected and take effect.


7. Cache thumbnail images for 1 hr for improved performance and lower AppEngine datastore usage.
8. Form definition files and media attachments can now be altered and those changes uploaded to the ODK Aggregate server. The server still maintains only one version of the form, and all alterations must not affect the number of questions in the form or change the data type of any field (e.g., from int to decimal or string, etc.).
9. Whenever a form or any of its media files are modified, the version attribute in the top-level element (where the form id is defined) must be changed. 

.. tip::

  Version attributes are recommended to be of the form "yyyymmddnn", e.g., 2012060400 -- the last two digits are the form iteration within the given day. They must be integer values and the new value must compare lexically greater than the prior value (this means, for example, since "9" compares lexically greater than "10", you cannot update a version from 9 to 10 -- but you could upgrade from "09" to "10").

10. There is a 15-minute grace period for uploading revisions after which the version must be incremented (e.g., incremented to 2012060401).
11. Fix odd start-up failures on Google AppEngine.

.. admonition:: Upgrade notes
   :class: upgrade

   Existing 1.0 installations can upgrade to the 1.2 release, but, once upgraded, if you use the new form-versioning feature, these installations cannot downgrade from 1.2 to the earlier 1.0 releases.

   MySQL and PostgreSQL require special upgrade instructions. The ``_filter_group`` table has a new column. If you are running ODK Aggregate 1.0 or 1.1, you will need to issue an ``alter table`` command on this table to add this column.

   For MySQL:

   .. code-block:: none

      ALTER TABLE `_filter_group` ADD COLUMN `INCLUDE_METADATA` char(1) NULL;

   For PostgreSQL:

   .. code-block:: none

      ALTER TABLE "_filter_group" ADD COLUMN "INCLUDE_METADATA" boolean NULL;

   Depending upon your database management tool, you may need to qualify the table name with the schema.

.. _v1.1tov1.0.4:

General steps for v1.1 to v1.0.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For any Aggregate version from v1.1 to v1.0.4, no additional upgrade steps are required if none of your forms use **odk:length** to alter the maximum string length.

Otherwise, for ONLY those forms that use **odk:length**:

1. Download the forms that use odk:length using the ODK Briefcase application.
2. Delete the forms on Google AppEngine (this may take several minutes or hours if you have many submissions).
3. Upload the forms from ODK Briefcase back onto your Google AppEngine instance.

**odk:length** has always been respected on MySQL and PostgreSQL; there are no additional steps to be performed on those systems.

.. _v1.0.3tov1.0:

General steps for version v1.0.3 to v1.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For any Aggregate version from v1.0.3 to v1.0, if you are running RC4, RC3, RC2, or RC1 (on Google's AppEngine or with MySQL or PostgreSQL), there are no special upgrade steps. It should just work.

If you are using Beta 4, follow these upgrade instructions:

**On GAE**: No additional steps required. It should just work.

**On MySQL or PostgreSQL**: The persistent results tables that hold the exported csv and kml files have changed (adding support for emitting csv files filtered by the active filter).

1. Stop Tomcat.
2. In your database's administration tool, connect to the database and:

    - ``drop table _persistent_results;``
    - ``drop table _persistent_result_file_bin;``
    - ``drop table _persistent_result_file_ref;``
    - ``drop table _persistent_result_file_blb;``

3. Copy the new WAR to the :file:`/webapps` directory.
4. Start Tomcat.

For all other Alpha or Beta releases, you must either use a new appspot instance or delete all data in your appspot instance. If you are using MySQL or PostgreSQL with an Alpha or Beta release, you should start with an empty database. 

.. _alpha-beta:

General steps to upgrade from Alpha and Beta releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On GAE
""""""""

1. If running builds prior to Beta 2 on Google AppEngine cloud services, any forms with Decimal data will need to be deleted and reloaded. Decimal data had been represented as strings and is now represented properly as double-precision numbers in Google AppEngine. 
2. Disable writes to the datastore (via Application Settings / Disable Datastore Writes )
3. Deploy to GAE.
4. Delete all the records in these kinds (using Datastore Viewer):
   
    - opendatakit._granted_authority_hierarchy
    - opendatakit._registered_users
    - opendatakit._user_granted_authority

5. Disable your application via Application Settings / Disable Application.
6. Enable writes.
7. Enable your application.

On MySQL or PostgreSQL
""""""""""""""""""""""""

1. Stop Tomcat.
2. In your database's administration tool, connect to the database and:
    
    - ``drop table _granted_authority_hierarchy;``
    - ``drop table _registered_users;``
    - ``drop table _user_granted_authority;``

3. copy the new WAR to the :file:`/webapps` directory.
4. Start Tomcat.

.. warning::

   The primary upgrade impact is the loss of all registered users and their privileges (what the manual steps above do). Beta 3 changes the user configuration. Registered users are now either Gmail accounts or ODK Aggregate usernames. ODK Aggregate now supports only anonymous access and/or registered users.

.. _v0.9xtov1.x:

Migration from ODK Aggregate 0.9x to 1.x
------------------------------------------

.. note::

  - Aggregate 0.9.x has a 1000-record limit to the number of records it can display (this is by design); it does, however, still retain all records i.e. it will hold as many records as you've uploaded and does not loose or ignore the 1001st record, etc; in general, any webserver will have a limit to what it can display interactively (at some point it will run out of memory or time out). 
  - On Aggregate 0.9.x, we provide the Briefcase applet (one of the links on the top row) to allow you to extract your data from the server into a local CSV file for local processing. That should retrieve all data within the server, and should work regardless of the number of submissions you have uploaded.
  - Aggregate 1.0 has far fewer display restrictions and has implemented display paging on the submissions display page so you can page through all the submissions on the server, rather than just the first 1000 (and you get to set the page size, as well).
  - Aggregate 1.x has stricter requirements on the form definition than 0.9.x, so you will likely need to edit your form definitions before they can be successfully uploaded into Aggregate 1.x.
  - Migration will necessitate creating a new AppEngine application id and migrating your ODK Collect devices to use that new AppEngine URL. This allows you to keep the old Aggregate 0.9.x instance should you need to return to it (e.g., if there is an error discovered after data migration), and it gives you time to validate the accuracy of the data that was migrated. It is simply safer to do the migration this way rather than overwrite your older instance.

Since Google is now charging for AppEngine usage, the lowest-cost sequence for the AppEngine migration is as follows:

1. Upgrade ODK Aggregate 0.9.x to the latest 0.9.x release. If you have any 0.9.x release, you can upgrade to the latest 0.9.x release without any changes (the newer updates are backward compatible). Get the latest Aggregate release from the ODK Downloads page `here <https://opendatakit.org/downloads/download-info/odk-aggregate-v0-9-8-1/>`_.
2. Create a new application id for the 1.x instance.
3. Download the latest installer for ODK Aggregate 1.x, run it, and deploy to the new application id. For installation process, see the :ref:`Aggregate Installation Guide <install-app-engine>`.
4. Manually download the form definitions (as XML) from Aggregate 0.9.x. Browse to your Aggregate 0.9.x instance and choose the :guilabel:`View XML` button on the main forms page. Then, from the resulting page, choose the :guilabel:`Download XML` button. Repeat for every form you have on the system.

.. tip::

   You may wish to specify a new folder for the downloads of your forms so that you can easily locate and edit them.

5. Manually upload the form definitions to Aggregate 1.x, editing and fixing the form definitions as needed. First sign into your Aggregate server. Go to the :guilabel:`Forms List` sub-tab under :guilabel:`Form Management` tab. Click the :guilabel:`Add New Form` button. Select the form to upload, and click on :guilabel:`Upload Form`. Repeat with the remaining forms.

.. warning::

   Following issues may arise in form upload process:

   - Your form definition may be using *xmlns="myformid"* to define the Identifier (Aggregate 0.9.x) now referred to as the Form Id (Aggregate 1.x) of the form. In Aggregate 1.x, we enforce that all xmlns assignments conform to URL syntax. This is a w3c standard and a requirement of some Xml parsers and editing systems. Since most users have just a simple short alphanumeric id for their forms, the fix is to change from using xmlns to using id to define your "form id". E.g., use *id="myformid"* instead. This variant allows "myformid" to be any alphanumeric string with additional non-space characters (e.g., dashes and underscores).
   - Aggregate 1.0.1 warns you if you have fields in the form that do not have defined data types. I.e., they lack any <bind> expressions or their <bind> expression does not specify a type="datatype" expression, with datatype being one of the known data types. This is a concern because Aggregate can filter results based on the values of individual columns. The ranking order for the string "111" would place it before (less than) "13", but that would be incorrect if this field were actually an integer value. The warnings are to catch omissions like this so that filters can work properly and so that data can be properly published to Fusion Tables.


6. Configure the Aggregate 1.x instance to accept submissions from ODK Collect. If you are running ODK Collect 1.1.5, you will need to configure Aggregate 1.x to grant the anonymousUser the Data Collector privilege. This allows unauthenticated users to submit data to Aggregate 1.x. If you are running ODK Collect 1.1.7 or higher, you can choose to define one or more local usernames and passwords, and configure ODK Collect 1.1.7 to identify itself with one of those usernames and passwords when accessing the server. Steps to do either of this are as follows:

   a. Go to the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab.
   b. If you are creating new local user(s), type the username(s) in the text box in the Add Users section of the page and click :guilabel:`Add`. You can add multiple users by separating the usernames with spaces or commas. The table above will update with the added users. Ensure that the Account Type is *ODK* for each of these users.
   c. Check the :guilabel:`Data Collector` check box beside each username that will be used by ODK Collect. If you have ODK Collect 1.1.5, check the check box beside the anonymousUser.
   d. Click :guilabel:`Save Changes` to apply your changes.
   e. Then, for each username you created, you must click :guilabel:`Change Password` and set the password for that username.

7. Configure all your ODK Collect clients to use the new Aggregate 1.x instance. On both ODK Collect 1.1.5 and 1.1.7, ensure that the Server URL points to the new instance and begins with *https* (for AppEngine instances). For MySQL or PostgreSQL systems, specify *https* only if the server has an SSL certificate. For ODK Collect 1.1.7, if you are requiring authentication, enter one of the configured usernames and passwords into the phone. 

8. :doc:`Install <briefcase-install>` the latest ODK Briefcase application.
9. Run ODK Briefcase, choosing to :ref:`pull all forms <pull-from-aggregate>` from your 0.9.x instance to the local server. You will need enough space to store these files.
10. For any form definitions you have changed, manually overwrite the downloaded form definition within the Briefcase directory with the one updated for Aggregate 1.x. The ODK Briefcase Storage Area has a :file:`/forms` directory under it, and, in that, it has directories for each form downloaded from Aggregate 0.9.x. The form definition is within that directory and must have the same name (with a file extension of .xml) as the directory containing it.
11. Run ODK Briefcase, choosing to :ref:`push all forms <push-to-aggregate>` from your local server to the new Aggregate 1.x instance.
12. Validate that your Aggregate 1.x instance has all the data you expect, and the values are complete and correct (by, e.g., publishing to Fusion Tables and comparing this dataset to the corresponding dataset produced by 0.9.x).
13. Once you are comfortable with the operations of the Aggregate 1.x instance, you should go to the Aggregate 0.9.x dashboard and delete that application id.
 
   a. Click on the :guilabel:`Application Settings` link on the left sidebar under the Administration heading.
   b. Click on the :guilabel:`Disable Application..` button on this page.
   c. Choose to disable it, and then, when prompted, choose to delete the application.

This is more cost-effective than deleting the forms (and data) from the old instance and trying to reuse it as that would incur usage charges. Deleting the entire instance accomplishes that without running up any charges.


.. tip::

   If you have to do this migration mid-survey and need to be able to incrementally pull data from ODK Aggregate v0.9.x, you should follow these steps:

   1. Pull data from ODK Aggregate v0.9.x
   2. Push data to ODK Aggregate v1.x
   3. Pull data from ODK Aggregate v1.x
   4. Repeat periodically.

   The extra pull of data down from ODK Aggregate v1.x sets a flag within ODK Briefcase that identifies the record as being "complete" (having all of its attachments). This does not prevent ODK Briefcase from downloading all the data each time from ODK Aggregate v0.9.x, but it does enable it to avoid repeatedly uploading this data to ODK Aggregate v1.x.

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
   







 

