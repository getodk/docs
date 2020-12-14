.. _central-troubleshooting:

Troubleshooting Central 
=========================

.. _troubleshooting-emails:

Users aren't receiving emails
-----------------------------

Central uses email as a way to verify user identity when setting or changing passwords. This helps ensure that only the intended user has access to their Central account.

Email sounds like a simple technology but in practice there are many things that can cause message delivery issues. By default, Central is installed with a mail server which can be used without configuration. However, it will not work in every environment. For example:

* Many cloud providers restrict the usage of simple mail servers such as Central's as a spam-prevention strategy
* You can be assigned an IP address that was previously used for sending spam and is therefore blocked by many mail recipients
* Your domain may not be recognized by mail recipients and therefore messages from it may be discarded or marked as spam

To address delivery issues, consider using a dedicated email service such as `Mailgun <https://www.mailgun.com/smtp/>`_. Because Central doesn't send very many emails, using such a service will generally be a cost-effective way of ensuring email delivery. Once you have an account set up, you will need to :ref:`configure Central to use it <central-install-digital-ocean-custom-mail>`.

If you want to directly send emails from your Central installation, the `mail-tester <https://www.mail-tester.com/>`_ service can help you identify what barriers to email delivery you might have. Create a Central account with the email address that it provides, retrieve your results, and then delete the user. Typically, the first thing you will need to do is :ref:`configure DKIM <central-install-digital-ocean-dkim>` which will provide email recipients confidence that emails were actually sent by your Central server rather than by a spammer pretending to be your server.

.. _docker-compose-down:

Following a ``docker-compose down``, data does not appear
----------------------------------------------------------

Central is meant to be administrated without discarding its containers and  ``docker-compose down`` discards the containers it brings down. If you do a ``down`` and then an ``up``, the new containers will be connected to a new database instead of your existing one.

To recover from this state, you will need to identify where the new and real databases are located and move the contents of the real database to where the new one is:
#. Identify the data directory that currently is being used by your system:

  #. Run ``docker inspect --type container central_postgres_1 -f '{{(index .Mounts 0).Source}}'``
  #. Verify that you get a folder in ``/var/lib/docker/volumes/`` or equivalent with a long, random name.
  #. Make a note of the long name and label it ``target`` in your notes. Use it where the instructions say ``target`` below.

#. Find the volume that was previously mounted (before the ``down``) and holds your data:

  #. Run ``cd /var/lib/docker/volumes`` or otherwise go to the Docker volumes folder for your host.
  #. Run ``ls`` to list all of the volumes on your host. You should see several volumes with long random names. One of them is the one you identified above and another is the one you're looking for.
  #. Look for the folder with the long name that contains folders with the ``pg_`` prefix. For each volume on your host, see what is inside of its ``_data`` folder. For example, type ``ls`` followed by a space, then the first few characters of a folder name, then tab to autocomplete. Then tab again to autocomplete ``_data`` and then type ``Enter``. Once you find folders with the ``pg_`` prefix (e.g. ``pg_clog``), make note of its long name and label it ``source`` in your notes. Use it where the instructions say ``source`` below.

#. Now that you know the volume that holds your data (``source``) and the volume that's currently being mounted (``target``), put the contents of ``source`` at ``target``:

  .. code-block:: console

    $ cd
    $ cd central
    $ docker-compose stop
    $ pushd /var/lib/docker/volumes
    $ mv target target.bak
    $ mv source target
    $ popd
    $ docker-compose up -d

#. Go to your site in a browser and try to log in with an account that previously existed. If that doesn't immediately work, try doing another ``docker-compose stop`` followed by ``docker-compose up -d``.

#. Once things are working as expected, you can remove the backup folder you made: ``rm target.bak``