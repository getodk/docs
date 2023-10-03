Upgrading Aggregate
=====================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

.. _upgrade-aggregate:

Need for Upgrading
--------------------

It is important to upgrade to newer ODK Aggregate versions as they come out. You don't need to do this immediately, but this should be something you do at least once a year.

Security vulnerabilities
~~~~~~~~~~~~~~~~~~~~~~~~~

The ODK developers are constantly upgrading the libraries we use with newer, safer versions. The older your software, the greater the number of vulnerabilities in it.

Performance improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~

As we find performance issues and address them, the Aggregate gets faster and cheaper to run.

Enhanced capabilities
~~~~~~~~~~~~~~~~~~~~~~

JavaRosa, the underlying form rendering library is updated about annually. Those updates add new functions, features, and occasionally data types. New features are slowly added to ODK Aggregate, too.

To use these newer features, keep your Aggregate installation up to date.

.. _determine-aggregate-version:

Determining your Aggregate version
-----------------------------------

Aggregate shows a notice about the deployed version at the bottom left corner of all the pages. The version notice will be clickable if there's an update available.

Instructions for older versions:

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
5. Expand the list of logs and find the log which shows the version of Aggregate. It will be of the following format:

.. code-block:: none

   13:24:54.806 org.opendatakit.common.security.Realm afterPropertiesSet: Version: v1.4.15 Production (Realm.java:51)

.. image:: /img/aggregate-upgrade/find-version.*
   :alt: Image showing search result for version.


.. _general-steps-for-upgrading-aggregate:

General steps for upgrading
------------------------------------

1. Disable all submissions to ODK Aggregate, in the :guilabel:`Form Management` tab.
2. Use :doc:`ODK Briefcase <briefcase-using>` to pull a copy of all data to your computer.
3. Log onto your server to confirm that it is still functioning.
4. :ref:`Determine your current version number <determine-aggregate-version>`.
5. Download the **next ODK Aggregate version** and upgrade to that version. `Find previous versions here <https://github.com/getodk/aggregate/releases>`_.

   Do not simply upgrade from an old version of Aggregate
   to the latest version.
   It is important to upgrade sequentially through versions,
   instead of trying to upgrade directly to the latest version
   from an older one.

   Some versions will require manual changes upon upgrade.
   Complete notes about upgrading can be found in each version's `release notes <https://github.com/getodk/aggregate/releases>`_.

6. Log onto your server to confirm that it is still functioning.
7. Repeat the steps 4-7 until you have upgraded to the current version.
8. Enable submissions to ODK Aggregate via the :guilabel:`Form Management` tab.

.. tip::

  You need to know the exact *instance name* that was used in prior installations for your username and password to continue to work. If you add a space or change capitalization or spelling, the passwords will be invalid (you just need to re-run the installer with the correct string to correct the problem).

.. _upgrading-digital-ocean:

Upgrading DigitalOcean deployments
----------------------------------

Please, refer to the `Aggregate Cloud-Config updates <https://github.com/getodk/aggregate/tree/master/cloud-config#updates>`_ guide
