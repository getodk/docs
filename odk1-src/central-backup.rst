.. _central-backup:

Backing Up Central
==================

Having a data backup strategy is a critical part of running a web service like ODK Central. Backups should go to a system in a different physical location from where Central is installed in order to prevent data loss across a broad range of scenarios. Many cloud providers offer backup strategies that run automatically. If you are an experienced system administrator, you may want to set up your own backups of the PostgreSQL database. If you don't already have a server-wide backup system in place and don't want to set up your own database backup, Central provides a managed backup system to Google Drive.

.. _central-managed-backups:

Managed backups
---------------

ODK Central features an off-site backup system to keep your data safe. For each backup, we extract all your data (including user accounts, forms, and submissions), we encrypt it so that only you can access it, and we send the encrypted result to your Google Drive account for safekeeping.

.. admonition:: About Google Drive account access

  When ODK Central requests to connect to your Google Drive account, it only requests permissions from Google to:

  - Create new files and folders in your Drive
  - Read and modify files and folders *that it created*

  This means that ODK Central *cannot* read or modify any other files or folders in your Drive, no matter what.

To see your current managed backups status, navigate to :menuselection:`--> System` at the top of the Central management website. You should see a status page for backups that looks something like this:

   .. image:: /img/central-backup/panel-initial.png

.. _central-backup-setup:

Setting up backups
------------------

1. To set up a new automated backup, click on the :guilabel:`Set up now` button on the right.

   .. tip::

     If you see a `Terminate` button instead of a `Set up now` button, you already have an automated backup configured. Right now, you can only have one automated backup scheduled at a time. If you wish to change where the backup is saved, you will need to terminate the old one before creating a new one.

#. You'll be asked to enter an optional passphrase. This passphrase is what the server will use to encrypt your backups. You will be unable to restore the backup without the passphrase, exactly as you type it in here. If you leave this field blank, we will still encrypt your backup data but anybody will be able to decrypt it by doing nothing more than leaving the passphrase blank.

#. The next step talks about connecting to your Google Drive account to store your backups. When you press :guilabel:`Next` again, a Google permissions page will appear in a popup. You will need to press :guilabel:`Allow` to proceed. If you are feeling unsure about granting access, please see the "About Google Drive account access" note at the top of this page.

   .. image:: /img/central-backup/google-auth.png

#. Once you press **Allow**, you will see a screen in the popup which contains a lengthy code, and instructions to copy and paste it back into "your application." Copy the code, switch back to the ODK Central website, and paste it into the :guilabel:`Confirmation text` box. Press :guilabel:`Next` to confirm it.

   .. image:: /img/central-backup/code-google.png

   .. image:: /img/central-backup/code-central.png

#. The setup box should close and you should see a message telling you :guilabel:`Success! Automated backups are now configured.`

#. Backups are scheduled to run once a day, at 02:00 server local time. If more than 24 hours pass without a backup completing successfully, you'll want to double check that everything has been correctly set up.

.. _central-backup-restore:

Restoring a backup
------------------

Restoring a backup to an ODK Central instance will entirely replace all of its data with the backup. Please be very sure you are restoring to the right place with the right backup snapshot before proceeding. 

.. note::

  A backup can only be restored to the Central version it was created from. For example, if you create a backup from Central v0.5, upgrade to Central v1.0, and then decide to restore the backup, you will first need to install Central v0.5. After your restore, you can upgrade again.

1. The first thing you'll have to do is download your backup from Google Drive, which you can do from the `Google Drive website <https://drive.google.com/>`_. You will find the backups in a folder called ``ODK Backups``. Each file is a single backup snapshot, and each snapshot should be titled ``backup-{date}T{time}Z.zip``.

#. Once you have the file on your local computer, you will have to transfer that backup snapshot file to your ODK Central server. If you don't know how to do this, and you used our DigitalOcean installation guide, please see `their instructions <https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server>`_ on how to transfer a file to a Droplet.

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

   You'll have to replace the filename following :file:`/data/transfer` with your own snapshot filename, and the text ``SECRET_PASSPHRASE`` with the passphrase you typed when backups were first set up. If you did not set up a passphrase, immediately press Enter after you have finished putting the :file`.zip` filename in:

   .. code-block:: console

     docker-compose exec service node /usr/odk/lib/bin/restore.js /data/transfer/backup-2018-01-01T00:00:00Z.zip

#. The server will think for a while, and then print some more instructions. You will have to refresh any browser windows you have open to ODK Central to proceed. If you run into error messages at this step, please read them carefully and then seek help on the `ODK Forum <https://forum.getodk.org/>`_ if you are not sure what to do.

