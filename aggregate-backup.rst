Backup Strategies for Aggregate
================================

.. _briefcase-backup:

Recovering from Briefcase
---------------------------

Use :doc:`ODK Briefcase <briefcase-guide>` to back up all forms and submissions on Aggregate. You can :ref:`pull forms from your Aggregate server <pull-from-aggregate>` into your local machine using Briefcase. In particular, Briefcase's :ref:`command line interface <cli-use>` makes this easier.

.. _mysql-backup:

Recovering database from MySQL dump 
--------------------------------------

1. Stop running Tomcat.
2. :doc:`Upgrade to the latest version of Aggregate <aggregate-upgrade>`.
3. Finally, restore it from MySQL dump. An SQL dump of a database is a common method to safely store away a snapshot of the database for archival purposes or to migrate data between database instances, e.g. between two major system releases. The content of a SQL dump is a large collection of SQL commands in ASCII. Running the script will recreate the database in the same state as it was when the dump was created. The primary tool to consider for making an ASCII dump is `mysqldump <https://dev.mysql.com/doc/mysql-backup-excerpt/5.7/en/using-mysqldump.html>`_, which includes a wide variety of options.

.. code-block:: console

  $ mysqldump [ options ] [ dbname ]

Some of the useful options are:

- :option:`-h hostname` or :option:`--host=hostname` specifies host to connect to.
- :option:`-p portnr` or :option:`--port=portnr` specifies port to connect to.
- :option:`-u user` or :option:`--user=user` specifies user id.
- :option:`-d database` or :option:`--database=database` specifies database to connect to.

To take a backup of database:

.. code-block:: console

  $ mysqldump database > backup-file.sql; 

To restore a database:

.. code-block:: console

  $ mysql database < backup-file.sql;

To copy a database from one server to another

.. code-block:: console

  $ mysqldump --opt database | mysql --host=remote_host -C database

**remote_host** indicates a remote server where you want to take backup.      

.. note::

  Creation of the dump respects your credentials, which means you only can dump the tables you have access to. 

.. _gae-backup:

Backup and recovery on Google App Engine
-------------------------------------------

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

.. _restore-backup:

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