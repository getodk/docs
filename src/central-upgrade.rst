.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. You do not have to upgrade to the latest version immediately, but we generally recommend that you do so to get access to the newest features, bug fixes, and security updates.

.. admonition:: Note

  To see your version number, click on the question mark icon in the upper right section of your Central menu bar, then click :guilabel:`Version`. If you don't see the question mark, you can also see the version number by adding ``version.txt`` to the root URL (e.g., `demo.getodk.cloud/version.txt <https://demo.getodk.cloud/version.txt>`_).

To perform an upgrade, you'll first need to get to the software. You'll need to log into your server's command line prompt again, like you did when you first set up the server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

Once you are logged into your server, navigate back to the project folder (``cd central``). Then, get the latest version of the infrastructure: ``git pull``.

.. admonition:: Note

  If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, just run ``git pull`` anyway and it will tell you.

.. warning::

  If you are upgrading to Central v1.4, see :ref:`Upgrading to Central v1.4 <central-upgrade-1.4>` if you have tens of thousands of submissions.

  If you are upgrading to Central v1.3, see :ref:`Upgrading to Central v1.3 <central-upgrade-1.3>` to ensure you have the correct version of docker-compose.

  If you are upgrading to Central v1.2, see :ref:`Upgrading to Central v1.2 <central-upgrade-1.2>` to learn how to resolve any error messages using ``git pull``.


Now, get the latest client and server: ``git submodule update -i``. Then, build your server from the latest code you just fetched: ``docker-compose build``.

.. admonition:: Note

  If you run into problems with this step, try stopping the Central software (``docker-compose stop``) and retry ``docker-compose build`` after it has shut down the Central website.

Next, you need to do a little bit of maintenance. Run ``docker prune``. If it thinks ``prune`` is not a docker command, run ``docker image prune`` instead. You'll be asked to confirm the removal of all dangling images. Agree by typing the letter ``y`` and pressing ``Enter``.

Finally, restart the running server to pick up the changes: ``docker-compose stop`` and ``docker-compose up -d``.

.. _central-upgrade-1.4:

Upgrading to Central v1.4
-------------------------

There are several time-consuming migrations in v1.4. If you have tens of thousands of submissions, consider temporarily increasing server performance and :ref:`memory allocation <central-install-custom-memory>` before upgrading.

 .. _central-upgrade-1.3:

Upgrading to Central v1.3
-------------------------

Before upgrading, run ``docker-compose --version`` to confirm you have docker-compose v1.28.3 or later. If you don't, upgrade with these commands from the `Docker's documentation <https://docs.docker.com/compose/install/#install-compose-on-linux-systems>`_.

.. code-block:: console

 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

.. _central-upgrade-1.2:

Upgrading to Central v1.2
-------------------------

In v1.2, we added some advanced features to Central's server configuration. These features will not be meaningful to most users. However, because we would like to make this change and further improvements in the future, we have modified the template ``.env`` configuration file you set up during installation.

Since you have made your own changes to the ``.env`` file to set Central up for your environment, you will see an error message when you run the ``git pull`` command:

.. code-block:: console

 error: Your local changes to the following files would be overwritten by merge:
         .env
 Please commit your changes or stash them before you merge.

Don't worry, nothing bad happens if you see this. To get around this error, run this set of commands instead of ``git pull``:

.. code-block:: console

 mv .env env-tmp
 git pull
 mv env-tmp .env

Afterwards, ``git status`` should not say anything about the ``.env`` file at all and you can continue with the upgrade instructions above. 

If ``git status`` still shows errors, copy and paste your entire console session into a `forum thread <https://forum.getodk.org/c/support/6>`_ and someone will help you out.

.. _central-upgrade-0.9:

Upgrading to Central v0.9
-------------------------

Particularly if you are installed on DigitalOcean, you will need to modify the system firewall for Enketo features in Central to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  While it sounds dangerous, disabling your system firewall does not put your server at greater risk. In fact, most Linux operating systems come with the system firewall disabled.

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be really difficult to do correctly, so we don't recommend most people try. Another option is to use an upstream network firewall.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your Central website over HTTPS on its public domain name from within the Enketo container, all Enketo features should work correctly.
