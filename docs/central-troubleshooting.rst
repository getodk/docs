.. _central-troubleshooting:

Troubleshooting Central 
=========================

.. _reading-container-logs:

Reading container logs
----------------------

If Central is behaving in an unexpected way, it is often helpful to read the Docker container logs with the `docker logs <https://docs.docker.com/engine/reference/commandline/logs/>`_ command for hints as to what has gone wrong.

The containers that are most likely to be helpful for troubleshooting are the `service` container and the `nginx` container. Use the `--tail` and `--since` options to help filter the logs. For example:

* ``docker logs --tail 100 central-service-1`` to see the last 100 lines of the service logs.
* ``docker logs --since 5m central-nginx-1`` to see the last 5 minutes of the nginx logs.

Other commands that are helpful are:

* ``docker ps`` to see the status of all containers.
* ``docker stats`` to see the CPU and RAM usage of all containers.

.. _troubleshooting-emails:

Users aren't receiving emails
-----------------------------

Central uses email as a way to verify user identity when setting or changing passwords. This helps ensure that only the intended user has access to their Central account.

Email sounds like a simple technology but in practice there are many things that can cause message delivery issues. By default, Central is installed with a mail server which can be used without configuration. However, it will not work in every environment. For example:

* Many cloud providers restrict the usage of simple mail servers such as Central's as a spam-prevention strategy
* You can be assigned an IP address that was previously used for sending spam and is therefore blocked by many mail recipients
* Your domain may not be recognized by mail recipients and therefore messages from it may be discarded or marked as spam

To solve delivery issues, we strongly recommend using a dedicated email service such as `Mailjet <https://www.mailjet.com>`_. Central doesn't send many emails, so such a service will generally be a cost-effective way of ensuring email delivery. Once you have an account set up, you will need to :ref:`configure Central to use it <central-install-digital-ocean-custom-mail>`.

If you do not want to use a dedicated email service, you can try directly sending emails from your Central installation. :ref:`Configure DKIM <central-install-digital-ocean-dkim>` to increase the likelihood of your emails being delivered.

The `mail-tester <https://www.mail-tester.com/>`_ service can help you identify what barriers to email delivery you might have. Create a Central account with the email address that it provides, retrieve your results, and then retire the user. 

.. _troubleshooting-form-preview-:

Preview could not connect with server
-------------------------------------

You may run into a "Could not connect with Server" error message when previewing forms. This error message is typically because your host machine has not made its DNS servers available to Central.

To resolve this problem, first identify your upstream DNS servers. Run ``cat /run/systemd/resolve/resolv.conf`` to see your current list of nameservers with their IP addresses. They will look like this:

.. code-block:: bash

  nameserver 1.2.3.4
  nameserver 9.8.7.6


Now, run ``nano /etc/docker/daemon.json`` to make those nameservers and, optionally, the Google DNS (8.8.8.8) as a fallback available to Docker. Your ``daemon.json`` file will look like the snippet below, but you will need to replace ``1.2.3.4`` and ``9.8.7.6`` with your nameservers' IP addresses.

.. code-block:: bash

  {
      "dns": ["1.2.3.4", "9.8.7.6", "8.8.8.8"]
  }

Finally, stop the containers, restart Docker, and bring the containers back up with ``docker compose stop``, ``systemctl restart docker`` and ``docker compose up -d``.

.. _migration-fails-due-to-out-of-memory-error:

Migration fails due to out-of-memory error
------------------------------------------

During upgrades, some versions of Central may perform complex database migrations that need more memory than the 2 GB typically allocated to Central.

If you get an error suggesting that the JavaScript heap is out of memory, try :ref:`increasing allocated memory <central-install-custom-memory>`.

.. _export-produces-corrupt-zip:

Export produces corrupt zip
---------------------------

If you have installed Central on a 1 GB server, you may encounter problems exporting submission .zip files. Usually, the .zip file will end up being empty, or much smaller than expected and possibly corrupt.

We recommend having at least 2 GB of memory. If you still run into problems, try :ref:`increasing allocated memory <central-install-custom-memory>`.

.. _file-upload-fails-with-413:

File upload fails with 413
---------------------------

If you get an error `413` when trying to upload a submission or when trying to upload a form attachment, the file you are trying to upload is too large. By default, files up to 100 MB are accepted. We typically recommend reducing the size of the files to upload if possible. For example, :ref:`images can be scaled down in form design <scaling-down-images>`.

If you absolutely must upload files over 100 MB, you can change the `client_max_body_size` `nginx` directive:

.. code-block:: bash

  $ cd central
  $ docker compose stop
  $ nano files/nginx/odk.conf.template
  <modify the nginx conf value for client_max_body_size>
  $ docker compose up -d

.. _troubleshooting-docker-compose-down:

Database reset after running Docker command
-------------------------------------------

.. warning::
  If you are experiencing data loss, the most important thing to do first is to stop and think through your next steps (ideally with a colleague, who can review those steps). Rushing to act without a plan will most certainly make the situation worse.

  If you do not have a backup, do not reboot or restart the machine. Instead, take a live, full disk backup of the machine so you have a fallback. If you are using DigitalOcean, see `how to create snapshots <https://docs.digitalocean.com/products/images/snapshots/how-to/snapshot-droplets/>`_.


In Central v2023.1 or earlier, it is possible to accidentally reset the database by running the ``down`` command with ``docker-compose``. This no longer happens in Central v2023.2 or later because the default database is stored on a named volume. If you are running an older Central version, you have run this command and your database has reset, follow these steps to restore your data.

The instructions below assume you installed Central on an Ubuntu LTS server. If you did not, or do not feel confident following the steps below, email support@getodk.org for assistance.

1. Capture the location of the new (and empty) database.

   .. code-block:: bash
 
     $ CENTRAL_NEW_DB=$(docker inspect --type container central_postgres_1 \
       -f '{{(index .Mounts 0).Source}}' | cut -d / -f 6)


2. Next, find any additional databases you have. You should get the number one (``1``) back. If you get anything else, stop and email support@getodk.org for assistance.

   .. code-block:: bash

     $ find /var/lib/docker/volumes/ -name pg_hba.conf \
       | grep -v "$CENTRAL_NEW_DB" | wc -l

3. Now that you've confirmed you have only one additional database, capture the location of the old database you wish to restore.

   .. code-block:: bash

     $ CENTRAL_OLD_DB=$(find /var/lib/docker/volumes/ -name pg_hba.conf \
       | grep -v "$CENTRAL_NEW_DB" | cut -d / -f 6)

4. Stop the Docker containers to prepare for restoration.

   .. code-block:: bash

     $ cd central
     $ docker-compose stop

5. Backup the new database and restore the old database.

   .. code-block:: bash

     $ cd /var/lib/docker/volumes/
     $ mv "$CENTRAL_NEW_DB" "$CENTRAL_NEW_DB"-backup
     $ mv "$CENTRAL_OLD_DB" "$CENTRAL_NEW_DB"

6. Now rebuild and restart the containers.

   .. code-block:: bash

     $ cd central
     $ docker-compose build
     $ docker-compose up -d

7. Go to your site in a browser and try to log in with an account that previously existed. If everything works as expected, consider deleting the backup of the new database. You can find it with the following command.

   .. code-block:: bash

     $ find /var/lib/docker/volumes/ -name *-backup
