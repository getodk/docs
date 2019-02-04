.. spelling::

  Mumbai

Google App Engine Support (Legacy)
==================================

.. warning::

  In February 2019, ODK Aggregate v2.x was released with support for Google App Engine removed. This page gathers all the information previously available about Google App Engine for Aggregate v1.x. See `upcoming changes to Aggregate <https://forum.opendatakit.org/t/upcoming-changes-to-aggregate/17582>`_ for more information.

Planning Your Aggregate Deployment
----------------------------------

The recommended method to deploy Aggregate v1 is using Google App Engine or the ODK Aggregate VM before attempting an EC2 or Tomcat deployment.

Internet access
~~~~~~~~~~~~~~~~~

Google App Engine and Amazon Web Services both require internet access. If you don't have consistent internet access, Briefcase may be more appropriate.

Dataset size
~~~~~~~~~~~~~~~

Google App Engine can store a virtually unlimited amount of data --- well in excess of a million submissions.

However, in deployments with data sets exceeding 7,000 submissions,
the :ref:`data export feature <export-data>` will stop working. To correct this, you will need a custom deployment with a larger virtual machine.

On Google App Engine, a larger server will incur higher billing costs. Additionally, for datasets of over 100,000 records, it is likely that performance will be better when using MySQL or PostgreSQL, rather than Google App Engine's data store. You also have more optimization opportunities when running your own database servers than are available through Google's cloud services.

.. note::

  Individual text database fields are capped at a length of 255 by default for performance reasons. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

Data locality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google App Engine servers may be located anywhere in the world.

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions.

In some circumstances, you might be able to use :ref:`encrypted-forms` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine.

.. seealso:: `Google Cloud Services Terms of Service <https://cloud.google.com/terms/>`_.

Billing
~~~~~~~~~

For identity verification purposes, Google requires a credit card or banking details to use the Google Cloud Platform that Google App Engine runs on. Accounts that meet this requirement receive a recurring $200 monthly credit per billing account.

Independent of Cloud Platform credits, App Engine allows a certain amount of free activity. These free quotas reset every 24 hours and are high enough to enable free use of ODK Aggregate during evaluation and small pilot studies.

You may be able to run a full deployment within these activity thresholds provided you:

- collect fewer than 2000 responses
- access the site a limited number of times a day
- can be flexible about when you upload and access data

Deployments with more activity that do not wish to wait 24 hours for quotas to reset can enable billing on their App Engine project.

Once billing is enabled, ODK Aggregate will start using the monthly credit that comes from the Cloud Platform. Once those credits are finished, the credit card or bank on file will then be used. Billing account owners can set spending limits to manage application costs.

Most ODK deployments will not surpass the $200/month credit and non-profits using more than that can apply for more credits through `Google for Nonprofits <https://www.google.com/nonprofits/>`_.

App Engine is usually sufficient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For most users, Google App Engine will be the easiest and most cost-effective option.

Two examples illustrate the cost-effectiveness of Google App Engine:

- The fee to run the `ODK Aggregate Demo Server <http://opendatakit.appspot.com>`_ is near the minimum weekly charge, costing a few dollars a week.

- A 6000 hour study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011).

You can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (for example, between data gathering campaigns, while you are developing the forms for the next campaign). When disabled, access is restricted to the free daily usage limit.

Minimizing App Engine fees
------------------------------------

On App Engine, the major driver of cost is Datastore Reads. These add up quickly:

- Viewing a page of form submissions incurs *at least* one Read for each submission.
- Each multiple-choice question in a form incurs an additional Read on every displayed submission.
- An additional read is incurred for every 200 questions in your survey.
- Each image incurs at least 10 reads.
- The default view shows 100 submissions.
- The form submissions display refreshes every six seconds.

For example, if your survey has 500 questions (*q*), with a repeat group containing an additional 300 questions, the typical survey has 4 filled-in repeats (*rpt*), and 100 submissions (*s*) are shown on each page load (*pl*), then the cost to display the Submissions tab is a minimum of 1100 Reads (*R*) with each refresh of the Submissions tab.

.. math::

  100 s/pl \times (500 q/s  \times  \lfloor 1 R / 200 q \rfloor + 4 rpt/s \times 300 q/rpt \times \lfloor 1 R / 200 q \rfloor) = 1100 \ R/pl


At this rate, the free quota would be exceeded within 5 minutes!

And this hypothetical survey did not contain any select-one or select-multiple questions, or any audio, video or image captures, all of which would require more Reads.

Therefore, to reduce datastore reads:

 - :ref:`restrict access to the Aggregate website <aggregate-permissions>`
 - do not keep the browser window open on the submissions tab
 - :doc:`export or publish your data <aggregate-data-access>`, and do your analysis in a different tool
 - use :doc:`briefcase-intro` instead of Aggregate to generate CSV files

It is generally more efficient to use Briefcase to generate CSV files than to use Aggregate, as Briefcase will use the locally cached data to generate the CSV files.

With larger datasets, there are two modes of operation:

- Aggregate retains the full dataset.

  In this mode, it is slightly more efficient to Pull data to your local computer then immediately Push it back up. This sets some internal tracking logic within Briefcase so that the next Pull is somewhat more efficient, as the Push only verifies that what you have locally matches the content on Aggregate, rather than re-uploading all of it.

- Aggregate retains only a portion of the dataset.

  In this mode, you periodically purge older data collection records and never Push data up to Aggregate, as that would restore the purged data.

Installing Aggregate
--------------------

.. toctree::
  :maxdepth: 1

  aggregate-app-engine

Aggregate Preferences
---------------------

- You can *disable faster background actions* to reduce App Engine quota usage.

Backup and recovery on Google App Engine
----------------------------------------

.. warning::

  Although the following instructions are what was available in these docs before Aggregate v2, Google now recommends using the more up-to-date method of `extracting and importing entities <https://cloud.google.com/datastore/docs/export-import-entities>`_. This is explained in more depth at the `ODK Aggregate data wrangling compendium <https://forum.opendatakit.org/t/odk-aggregate-data-wrangling-compendium/14174>`_ forum post.

.. _create-backup:

Create backup
~~~~~~~~~~~~~~~

1. Open a browser to  `Google Cloud Platform <https://cloud.google.com/>`_ and click on :guilabel:`Console` in the top right corner.

.. image:: /img/aggregate-backup/cloud-console.png
   :alt: Image showing console option.

2. Sign in with a Gmail account which you used for Aggregate installation.

.. image:: /img/aggregate-backup/email-select.png
   :alt: Image showing sign in window.

3. Choose the project id for your ODK Aggregate server by clicking on the project dropdown in the top left corner.

.. image:: /img/aggregate-backup/dropdown.png
   :alt: Image showing project dropdown.

.. image:: /img/aggregate-backup/project-select.png
   :alt: Image showing project selection box.

4. Click on the menu icon (three horizontal bars) to the left of :guilabel:`Google Cloud Platform` in the upper left side of the screen and then select :guilabel:`Datastore` from the menu. Click on :menuselection:`Admin` in the dropdown.

.. image:: /img/aggregate-backup/admin.png
   :alt: Image showing Datastore and Admin option.

5. Enable Cloud Datastore Admin access by clicking on :guilabel:`Enable Datastore Admin`.

.. image:: /img/aggregate-backup/enable-admin.png
   :alt: Image showing Enable Datastore Admin option.

6. Then, click on :guilabel:`Open Datastore Admin`.

.. image:: /img/aggregate-backup/open-admin.png
   :alt: Image showing Open Datastore Admin option.

.. tip::

  It is recommended to disable writes during creation of backup. To disable writes, click on :guilabel:`Disable writes` on the Admin page.

  .. image:: /img/aggregate-backup/disable-writes.png
    :alt: Image showing Disable writes option.

.. warning::

  Your Aggregate server may become unstable when you disable writes. It will be fine when you enable writes again.

7. Select the entity kinds that you wish to back up and then click on :guilabel:`Backup Entities`.

.. image:: /img/aggregate-backup/backup-select.png
   :alt: Image showing backup entities selection.

8. A backup form will be displayed.

.. image:: /img/aggregate-backup/backup-form.png
   :alt: Image showing backup form.

.. note::

  - A backup name is supplied and it includes a datestamp. You must change this value if you make more than one backup per day because a backup is not made if a backup of the same name already exists.
  - The default queue is used for the backup job; you can use this in most cases. If you use a non-default queue for backup/restore, you can only specify the target **ah-builtin-python-bundle** in **queue.yaml**. You cannot use any other targets. To know more about queues, see `this <https://cloud.google.com/appengine/docs/standard/java/taskqueue/>`_.
  - Select Google Cloud Storage as the backup storage location.

In the bucket name box, enter *your-project-id.appspot.com*. You can alternatively preface the bucket name with **/gs/**, for example, /gs/[BUCKET_NAME].

.. note::

  Buckets are containers where your backup will be stored. You can also `create buckets <https://cloud.google.com/storage/docs/creating-buckets>`_ for your project.

Now click on :guilabel:`Backup Entities` to start the backup jobs.

9. A job status page is displayed. Click on :guilabel:`Back to Datastore Admin` to see the backup status.

.. image:: /img/aggregate-backup/backup-job.png
   :alt: Image showing backup job status page.

You can abort a backup by selecting a backup from the list of pending backups and clicking on :guilabel:`Abort`.

.. image:: /img/aggregate-backup/pending-backup.png
   :alt: Image showing Abort and Info option.

.. warning::

  When you abort a backup job, App Engine attempts to delete backup data that has been saved up to that point. However, in some cases, some files can remain after the abort. You can locate these files in the location you chose for your backups in Google Cloud Storage and safely delete them after the abort completes. The names of such files start with the following pattern: **datastore_backup_[BUCKET_NAME]**.

Click on :guilabel:`Info` to get more information about the backup. On the info page, click :guilabel:`Back to Datastore Admin` to return to the main Cloud Datastore Admin screen.

.. image:: /img/aggregate-backup/backup-info.png
   :alt: Image showing backup info.

.. tip::

  After the backup is complete, if you disabled Cloud Datastore writes, re-enable them by going to Admin page and clicking on :guilabel:`Enable writes`.

  .. image:: /img/aggregate-backup/enable-writes.png
    :alt: Image showing Enable writes option.

Restoring data from Backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to the Admin page as described in the :ref:`creation of backup <create-backup>`.

.. image:: /img/aggregate-backup/admin.png
   :alt: Image showing Datastore and Admin option.

.. tip::

  Disable Cloud Datastore writes for your application. It's normally a good idea to do this to avoid conflicts between the restore and any new data written to Cloud Datastore. To disable writes, click on :guilabel:`Disable writes` on the Admin page.

  .. image:: /img/aggregate-backup/disable-writes.png
    :alt: Image showing Disable writes option.

2. Click on :guilabel:`Open Datastore Admin`.

.. image:: /img/aggregate-backup/open-admin.png
   :alt: Image showing Open Datastore Admin option.

3. In the list of available backups, select the backup that you want to restore from and click on :guilabel:`Restore`. You can click on :guilabel:`Info` to get more information about the backup. To delete a backup, select the backup and click on :guilabel:`Delete`.

.. image:: /img/aggregate-backup/backup-list.png
   :alt: Image showing Restore, Info and Delete options.

4. In the advisory page that is displayed, notice the list of entities with checkboxes. By default, all of the entities will be restored. Uncheck the checkbox next to each entity that you don't want to restore. Click on :guilabel:`Restore` at the bottom of the page to start the restoration.

.. image:: /img/aggregate-backup/restore-backup.png
   :alt: Image showing restore option.

.. note::

  In the advisory page, notice that the default queue, with its pre-configured performance settings, is used for the restore job. Change this to another queue that you have configured differently if you need different queue performance characteristics, making sure the queue chosen does not have any target specified in **queue.yaml** other than **ah-builtin-python-bundle**. To know more about queues, see `this <https://cloud.google.com/appengine/docs/standard/java/taskqueue/>`_.

5. A job status page is displayed. Click on :guilabel:`Back to Datastore Admin` to see the status of the restore.

.. image:: /img/aggregate-backup/restore-job.png
   :alt: Image showing job status page.

.. image:: /img/aggregate-backup/restore-status.png
   :alt: Image showing restore status.

.. tip::

  After the restore is complete, if you disabled Cloud Datastore writes, re-enable them by going to Admin page and clicking on :guilabel:`Enable writes`.

  .. image:: /img/aggregate-backup/enable-writes.png
    :alt: Image showing Enable writes option.

.. note::

  - If you back up your data using Google Cloud Storage, you can restore backups to applications other than the application used to create the backup. To restore backup data from a source application to a target application, see this `guide <https://cloud.google.com/appengine/docs/standard/python/console/datastore-backing-up-restoring>`_.
  - Google has new beta service for `exporting and importing <https://cloud.google.com/datastore/docs/export-import-entities>`_. Only Cloud Platform projects with `billable accounts <https://cloud.google.com/support/billing/>`_ can use the export and import functionality.

Tips and best practices
-----------------------

.. toctree::
  :maxdepth: 2

  aggregate-boost-performance

Pushing Data to Aggregate on Google App Engine
-------------------------------------------------

If Aggregate is :doc:`installed on Google App Engine <aggregate-app-engine>`, using the default datastore as described in our documentation, a combination of request time limits and datastore implementation create the following issues.

Simultaneous push requests will block each other and may time out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within ODK Aggregate, there is a global mutex (*TaskLock* across all server instances, mediated by the datastore layer) in the server when inserting submissions. Having multiple push requests occurring simultaneously will cause them to block on the mutex, chewing up their 60-second request limit, as they get processed in single file no matter how many server instances are spun up.

The solution to this is: **Serialize your push requests.**

Time limit may be exceeded on low-bandwidth connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 60-second request limit can be very commonly exceeded over low-bandwidth connections, and even text-only submissions can be impacted on satellite connections. That is why ODK Collect splits submissions into multiple 10MB submission requests. The timer starts upon receipt of the first byte, so a slow connection can account for a sizeable portion of those 60 seconds. The same applies for sending a response. The processing on the server is generally negligible in relation to the transmission times.

.. note::

   - The above two limitations, the global mutex and the in-memory copies/full-packet-assembly, are a result of implementing on top of App Engine and its Datastore.
   - A server that used database transactions and that used streaming servlet 3.0 functionality would have less trouble with concurrent requests.

Media held in memory
----------------------

When a form submission is uploaded, and when blank forms are downloaded, all the associated media files are held in memory at the same time, twice. For forms with a lot of media files, this can consume a lot of memory.

The previous section already suggested serializing form submission uploads. This is not absolutely critical for form downloads, but you should probably manage how many form download requests are being handled concurrently, in order to avoid memory problems.

..  Spinning up of copies of the frontend will incur faster quota usage on App Engine. For that reason, the Aggregate configuration here specifies a 14-second queuing time threshold before a new instance is spun up. Only if at least one request is queued for longer than 14 seconds will a new instance be spun up, and then that new instance will take about 30 seconds to become live. Leaving a 15-second processing interval. This is why ODK Collect tried twice before failing a submit.
