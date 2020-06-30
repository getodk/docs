.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. You do not have to upgrade to the latest version immediately, but we generally recommend that you do so to get access to the newest features, bug fixes, and security updates.

.. admonition:: Note

  You can check your current version by adding ``version.txt`` to the URL. For example `https://sandbox.central.getodk.org/version.txt <https://sandbox.central.getodk.org/version.txt>`_.

To perform an upgrade, you'll first need to get to the software. You'll need to log into your server's command line prompt again, like you did when you first set up the server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

Once you are logged into your server, navigate back to the project folder (``cd central``). Then, get the latest version of the infrastructure: ``git pull``.

(If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, just run ``git pull`` anyway and it will tell you.)

Now, get the latest client and server: ``git submodule update -i``. Then, build your server from the latest code you just fetched: ``docker-compose build``.

.. admonition:: Note

  If you run into problems with this step, try stopping the Central software (``systemctl stop docker-compose@central``) and retry ``docker-compose build`` after it has shut down the Central website.

Finally, restart the running server to pick up the changes: ``systemctl restart docker-compose@central``.

.. _central-upgrade-0.9:

Upgrading to Central 0.9
------------------------

Particularly if you are installed on Digital Ocean, you will need to modify the system firewall for Enketo features in Central to work correctly.

The quickest way to do this is to run ``ufw disable`` while logged into your server's command line prompt. You should see the message ``Firewall stopped and disabled on system startup``. If so, you have configured the firewall correctly.

.. admonition:: For advanced administrators

  If you don't want to disable the firewall entirely, you can instead configure Docker, ``iptables``, and ``ufw`` yourself. This can be really difficult to do correctly, so we don't recommend most people try.

  The goal here is to ensure that it is possible to access the host through its external IP from within each Docker container. In particular, if you can successfully ``curl`` your ODK Central website over HTTPS on its public domain name, all Enketo features should work correctly.

