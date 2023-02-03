.. _central-backup:

Backing Up Central
==================

Having a data backup strategy is a critical part of running a web service like ODK Central. Backups should go to a system in a different physical location from where Central is installed in order to prevent data loss across a broad range of scenarios. Many cloud providers offer backup strategies that run automatically.

If you are an experienced system administrator, you may want to set up your own backups of the PostgreSQL database that contains all of Central's data. One strategy for doing this is to :ref:`configure a separate database server <central-install-digital-ocean-custom-db>` and back up that database server.

You will additionally need to have a backup of Enketo data to be able to restore existing Web Form links. At a minimum, you must back up Enketo's Redis store and the keys generated in the Enketo configuration. **In general, we recommend making a full system backup.**

If you don't already have a full system backup in place and don't want to set up your own database backup, Central provides an API endpoint to download a backup of the database.

.. _central-direct-backups:

Direct Backups via API
----------------------

.. warning::

  `Direct Backups via API <https://odkcentral.docs.apiary.io/#reference/system-endpoints/direct-backup>`_ include all of your collected data but do **NOT** include sufficient information to re-establish the same Web Form links. If you use :ref:`Public Links <central-submissions-public-link>` for broad surveying or share :ref:`links to Web Forms <central-submissions-direct>` through another system, we strongly recommend also making a full system backup.

  If you only use Web Forms for previews or for making Submissions directly from Central, Direct Backups are sufficient. You can regenerate previews by uploading the same Form with a new :ref:`Form version <central-forms-updates>`.

The Central API offers an HTTP endpoint to perform an immediate backup of the database and download the result to your computer. We call this type of backup a Direct Backup. For each Direct Backup, we extract all your data (including user accounts, Forms, and Submissions), then encrypt it with an optional passphrase. The encrypted backup will be returned in the HTTP response. As detailed above, the backup will not include Web Form configurations.

Performing a Direct Backup can take some time, and it is normal for data to download quite slowly for many minutes before it gets faster. Take care in using this feature particularly if you have a lot of data and traffic, as performing a backup while a lot of data is being saved to the database can slow the process down significantly.

For more information, please see the `API documentation <https://odkcentral.docs.apiary.io/#reference/system-endpoints/direct-backup>`_.

.. _central-backup-restore:

Restoring a backup
------------------

Restoring a Direct Backup file to a Central instance will entirely replace all of its data with the backup. Please be very sure you are restoring to the right place with the right backup snapshot before proceeding.

.. note::

  You cannot restore a backup to an older version of Central. For example, if you create a backup from Central v1.0, you cannot restore it to Central v0.9.

.. note::

  Before v2023.1, Central supported scheduled backups to Google Drive. That functionality has been `sunsetted <https://forum.getodk.org/t/backups-to-google-drive-from-central-will-stop-working-after-jan-31st/38895>`_, but you can follow the same steps here to restore a backup file from Google Drive. The first thing you'll have to do is download your backup from Google Drive, which you can do from the `Google Drive website <https://drive.google.com/>`_. You will find the backups in a folder called ``ODK Backups``. Each file is a single backup snapshot, and each snapshot should be titled ``backup-{date}T{time}Z.zip``.

1. Find the backup file on your local computer. You will have to transfer that backup snapshot to your ODK Central server. If you don't know how to do this, and you used our DigitalOcean installation guide, please see `their instructions <https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server>`_ on how to transfer a file to a Droplet.

#. Once the file is on the server itself, you'll need to log back into it, like you did when you first set up the server.

   .. tip::

     If you used our :ref:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the :ref:`login steps <central-install-digital-ocean-build>`.

#. Now you'll want to put it in a special place where it can be used by the restore tool: :file:`/data/transfer`. If, for example, you uploaded the file to :file:`/root/backup-2018-01-01T00:00:00Z.zip`, you'll want to run this command in order to move it:

   .. code-block:: console

     mv /root/backup-2018-01-01T00:00:00Z.zip /data/transfer/

#. Now you need to run the restore script. **Please note again** that **all data** on this server is about to be replaced by the backup snapshot data! Anybody currently using the server will be kicked off and all changes made since the last backup will be lost. When you are sure you wish to proceed, run the following commands:

   .. code-block:: console

     cd
     cd central
     docker-compose exec service node /usr/odk/lib/bin/restore.js /data/transfer/backup-2018-01-01T00:00:00Z.zip 'SECRET_PASSPHRASE'

   You'll have to replace the filename following :file:`/data/transfer` with your own snapshot filename, and the text ``SECRET_PASSPHRASE`` with the passphrase you typed when backups were first set up. If you did not set up a passphrase, immediately press Enter after you have finished putting the :file:`.zip` filename in:

   .. code-block:: console

     docker-compose exec service node /usr/odk/lib/bin/restore.js /data/transfer/backup-2018-01-01T00:00:00Z.zip

#. The server will think for a while, and then print some more instructions. You will have to refresh any browser windows you have open to ODK Central to proceed. If you run into error messages at this step, please read them carefully and then seek help on the `ODK Forum <https://forum.getodk.org/>`_ if you are not sure what to do.

