.. _central-upgrade:

Upgrading Central
=================

We release new versions of Central regularly. You do not have to upgrade to the latest version immediately, but we generally recommend that you do so to get access to the newest features, bug fixes, and security updates.

To perform an upgrade, you'll first need to get to the software. You'll need to log into your server's command line prompt again, like you did when you first set up the server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

Once you are logged into your server, navigate back to the project folder (``cd central``). Then, get the latest version of the infrastructure: ``git pull``.

(If you have made local changes to the files, you may have to start with ``git stash``, then run ``git stash pop`` after you perform the ``pull``. If you aren't sure, just run ``git pull`` anyway and it will tell you.)

Now, get the latest client and server: ``git submodule update -i``. Then, build your server from the latest code you just fetched: ``docker-compose build``.

.. admonition:: Note

  If you run into problems with this step, try stopping the Central software (``systemctl stop docker-compose@central``) and retry ``docker-compose build`` after it has shut down the Central website.

Finally, restart the running server to pick up the changes: ``systemctl restart docker-compose@central``.

