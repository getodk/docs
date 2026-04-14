.. _central-backup:

Backing Up Central
==================

Having a data backup strategy is a critical part of running a web service like ODK Central. Backups should go to a system in a different physical location from where Central is installed in order to prevent data loss across a broad range of scenarios. Many cloud providers offer backup strategies that run automatically.

If you are an experienced system administrator, you may want to set up your own backups of the PostgreSQL database that contains all of Central's data. One strategy for doing this is to :ref:`configure a separate database server <central-install-digital-ocean-custom-db>` and back up that database server.

You will additionally need to have a backup of Enketo data to be able to restore existing Web Form links. At a minimum, you must back up Enketo's Redis store and the keys generated in the Enketo configuration. **In general, we recommend making a full system backup.**

If you :ref:`store file data in S3-compatible storage <central-install-digital-ocean-s3>`, you will need to have a backup and restore strategy for that data as well.

If you don't already have a full system backup in place and don't want to set up your own database backup, Central provides an API endpoint to download a backup of the database.

.. _central-direct-backups:

Direct Backups via API
----------------------

.. warning::

  `Direct Backups via API </central-api-system-endpoints/#direct-backup>`_ include all of your collected data, unless you have set up S3-compatible storage for attachments; in that case, the backup will not include those attachments. Furthermore, the backups do **NOT** include sufficient information to re-establish the same Web Form links. If you use :ref:`Public Links <central-submissions-public-link>` for broad surveying or share :ref:`links to Web Forms <central-submissions-direct>` through another system, we strongly recommend also making a full system backup.

  If you only use Web Forms for previews or for making Submissions directly from Central, and you are not using external storage for attachments, Direct Backups are sufficient. You can regenerate previews by uploading the same Form with a new :ref:`Form version <central-forms-updates>`.

The Central API offers an `HTTP endpoint </central-api-system-endpoints/#direct-backup>`_ to perform an immediate backup of the database and download the result to your computer. We call this type of backup a Direct Backup. For each Direct Backup, we extract all your data (including user accounts, Forms, and Submissions), and optionally encrypt it with a passphrase. The encrypted backup will be returned in the HTTP response. As detailed above, the backup will not include Web Form configurations, nor will it include files offloaded to S3-compatible storage.

Performing a Direct Backup can take some time. Take care in using this feature particularly if you have a lot of data and traffic, as performing a backup while a lot of data is being saved to the database can slow the process down significantly. Additionally, please note that a backup may fail or the downloading of it may break halfway for various reasons. Thus especially in unattended automated scheduled backup scenarios, care has to be taken to set up error handling and alerting so that you don't end up finding out you have no recent backups just when you need them. You might consider `ODK Cloud <https://getodk.org/#pricing>`_ and not worry about these aspects.


* .. collapse:: Advanced: Example backup API usage

    This is a recommendation on how to use the direct backup API, to be used as-is or as a building block in a periodic automated backup strategy.

    Below is an example configuration file to be used with the ``curl`` command-line client. This has been tested with version ``8.19.0``, but may work with versions from ``7.83.0`` (released April 27, 2022) onwards.
    
    Copy the below contents into some private file (as it will contain a passphrase used for backup encryption).
    Adjust the variables, then invoke ``curl`` to use the configuration file:
    
    ``curl --config /path/to/that/configfile``
    
    You will be asked for the password of the admin account configured in the configuration file.
        
    If anything goes wrong, there will not be any backup file saved, a warning will be output, and the process exit code will be nonzero.

    .. code-block::

        # Configuration file for downloading ODK database backups, see https://docs.getodk.org/central-backup/#direct-backups-via-api
        # Keep this file private.
        
        # Set to the URL of your Central server installation
        url = "http://127.0.0.1:8686/v1/backup"
        
        # Set the username of an admin account. Curl will ask for
        # the password when you run it.
        user = someone@somewhere.somedomain
        
        # Set your backup encryption passphrase.
        json = {"passphrase":"MakeThisHardToGuess"}
        
        # Set the backup storage directory 
        output-dir = /where/the/backups/go
        
        # NO USER-SERVICEABLE PARTS BELOW
        http1.1
        show-error
        fail
        remote-name
        remote-header-name
        remove-on-error
        no-clobber
        create-dirs
        write-out = "%{onerror}%{stderr}\n\n\n\tAN ERROR OCCURRED AND YOUR BACKUP WAS NOT SAVED\n\n\n"
        # End of configuration file



* .. collapse:: Advanced: Decrypting and verifying a backup

    As of Central v2026.2, the backup format is such that you can decrypt and verify it using standard utilities.
    
    For instance, you may have an existing backup file and you want to verify whether the encryption passphrase you have on hand is valid for that file. Or, you want to decrypt the file in order to hand over a standard ``pgdump``-format file to a database system administrator for restoring. Or, you may have special requirements for the restore procedure, not accommodated for by the Central ``restore.js`` utility, and thus you want to run `pg_restore <https://www.postgresql.org/docs/14/app-pgrestore.html>`_ yourself.
    
    What follows is not a complete guide, but a few pointers that would help someone technical on their way for such tasks.
    
    On a Linux/Unix system, you can use the ``openssl`` and ``pg_restore`` utilities to check a backup file's integrity in the following way. OpenSSL decrypts the file and, if supplied with the correct passphrase, produces a unencrypted stream in the ``pg_dump`` binary archival format (conversely, if given an incorrect passphrase, it will produce a stream of gibberish). If we hand that stream to ``pg_restore``, we can simulate a restore and by that, verify the archive. Example incantation:
    
    ``openssl enc -d -chacha20 -pbkdf2 < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin | pg_restore --file /dev/null``
    
    It will ask for the backup passphrase. Just press the ``enter`` key if you didn't use any passphrase.
    
    * If you see an error "``bad magic number``", then that is OpenSSL stating that its input doesn't match what it expects. Potentially the input file is not a post-v2026.2-Central produced backup file.
    
    * If you see an error along the lines of "``pg_restore: error: unsupported version (1.16) in file header``", then the version of ``pg_restore`` on your system is too old.
    
    * If you see an error along the lines of "``pg_restore: error: could not read from input file: end of file``", then the archive was cut short — presumably, the download was aborted; see "Advanced usage: Example backup API usage" on how to avoid saving such truncated backups.
    
    * If you see an error along the lines of "``pg_restore: error: input file does not appear to be a valid archive``", then either the passphrase you entered was incorrect, or the backup file is corrupted (or both). If you want to exclude that the problem is with the passphrase, you can look at the first 5 bytes of ``openssl`` output (example):
    
      ``openssl enc -d -chacha20 -pbkdf2 < /path/to/central-backup-2026-04-01T11:22:33.456Z.pgdump.enc.bin 2>/dev/null | head -c 5``
    
      If you see ``PGDMP`` in the output of this command, then the passphrase was correct.


.. _central-backup-restore:

Restoring a backup
------------------

.. warning::
    As of Central v2026.2, a backup is restored to the database configured for the Central instance where the restoration process is invoked. This was not necessarily the case with earlier versions, which restored to the database name as it was at the time and place where the backup was created.
    
    Restoring a Direct Backup file to a Central instance will entirely replace all of its data with the backup. Please be very sure you are restoring to the right place with the right backup snapshot before proceeding.

.. note::

  You cannot restore a backup to an older version of Central. For example, if you create a backup from Central v2024.1, you cannot restore it to Central v2022.3`.

.. note::

  Prior to version v2023.1, Central supported scheduled backups to Google Drive. That functionality has been `sunsetted <https://forum.getodk.org/t/backups-to-google-drive-from-central-will-stop-working-after-jan-31st/38895>`_, but you can follow the same steps here to restore a backup file from Google Drive. The first thing you'll have to do is download your backup from Google Drive, which you can do from the `Google Drive website <https://drive.google.com/>`_. You will find the backups in a folder called ``ODK Backups``. Each file is a single backup snapshot, and each snapshot should be titled ``backup-{date}T{time}Z.zip``.

1. Find the backup file on your local computer. You will have to transfer that backup snapshot to your ODK Central server. If you don't know how to do this, and you used our DigitalOcean installation guide, please see `their instructions <https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server>`_ on how to transfer a file to a Droplet.

#. Once the file is on the server itself, you'll need to log back into it, like you did when you first set up the server.

   .. tip::

     If you used our :ref:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the :ref:`login steps <central-install-digital-ocean-build>`.

#.  Locate the file you transferred. In the below examples, we pretend that it's ``/root/backupfile``. We also pretend you set a passphrase "SECRET_PASSHPRASE". If you did not set a passphrase when backing up, then you can leave off the whole ``'SECRET_PASSPHRASE'`` bit.

    * For a backup ending with ``.pgdump.enc.bin`` (the post-v2026.2 format), you can run the restore process like so:
    .. code-block:: bash

        cd
        cd central
        cat /root/backupfile | docker compose exec -T service node /usr/odk/lib/bin/restore.js - 'SECRET_PASSPHRASE'

    * For a backup ending with .zip (the format produced by Central versions prior to v2026.2), we cannot simply stream the file, and we have to transfer the file "into" the container first. This will create an extra copy of the backup file. The restore process then unpacks the .zip file, creating yet *another* copy of the data. Thus you may want to make sure that there is enough disk space available. You can run the restore process like so:
    .. code-block:: bash

        cd
        cd central
        cat /root/backupfile | docker compose exec -T service sh -c "cat > /tmp/odk_backup.zip"
        docker compose exec service node /usr/odk/lib/bin/restore.js /tmp/odk_backup.zip 'SECRET_PASSPHRASE'
        docker compose exec service rm /tmp/odk_backup.zip

#. Once the restore process finishes, you will have to refresh any browser windows or tabs you have opened ODK Central in to proceed. If you run into error messages at this step, please read them carefully and then seek help on the `ODK Forum <https://forum.getodk.org/>`_ if you are not sure what to do.
