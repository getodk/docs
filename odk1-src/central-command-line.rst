.. _central-command-line:

ODK Central Command Line Tools
==============================

ODK Central allows some administrative actions to be performed by anybody with direct console access to the server itself. Usually, this means only the person who set up the server and installed Central onto it. These tools can be used to:

 - create new user accounts,
 - reset passwords,
 - and manage user permissions.

All of these actions can be done through the website, and if everything is working normally we strongly recommend that you use the web interface to perform these actions. But things happen, and if something gets broken (like everybody forgets their password, or someone deletes all the users), you can use the command line tools to get things working again.

.. _central-command-line-basics:

Getting to the tools
--------------------

First, you'll need to get to the tools. You'll need to log into your server's command line prompt again, like you did when you first set up the server. If you used our :doc:`DigitalOcean installation steps <central-install-digital-ocean>` but can't quite remember how to do this, we suggest reviewing the section :ref:`central-install-digital-ocean-build` as a reminder, or if you can't remember your password to start at the top of that section to reset your password.

Once you have a command line in front of you (it should say something like ``root@server-name:~#``), you'll want to enter the following commands:

.. code-block:: console

  cd central
  docker-compose exec service odk-cmd

If you see instructions appear with the section headings *Usage*, *Options*, and *Commands*, you'll know you're in the right place. If you are familiar with command line tools in general, those instructions are probably all you need to get going. Otherwise, please see the sections below for a short guide and example on how to use each one.

.. _central-command-line-user-create:

Creating a Web User by command line
-----------------------------------

If you followed our :doc:`DigitalOcean installation steps <central-install-digital-ocean>`, then you've already done this once down in :ref:`this section <central-install-digital-ocean-account>`. You shouldn't have to do this again unless you deleted all your users. But if you do, please start by performing the steps above in the :ref:`central-command-line-basics` section. Then, this is what you would type, assuming your email address is ``example@getodk.org``:

.. code-block:: console

  docker-compose exec service odk-cmd --email example@getodk.org user-create

You will be asked for a password for the account, and if everything worked correctly you should see some data printed out that among other things lists the email you entered a moment ago. The next thing you'll need to do is to :ref:`make the new account an administrator <central-command-line-user-promote>`, which is normally automatically done by the web interface. If you don't, the new user will not be able to do anything.

.. _central-command-line-user-set-password:

Setting a Web User password by command line
-------------------------------------------

You can always reset any user's password from the website login page, which will send them an email with a link to set their new password. However, if for instance that email address no longer works, or the email is getting lost somehow, you can directly set any user's password with the command line tools.

Please start by performing the steps above in the :ref:`central-command-line-basics` section. Once you do, here is what you would type, assuming the email address of the account you wish to set a password for is ``example@getodk.org``:

.. code-block:: console

  docker-compose exec service odk-cmd --email example@getodk.org user-set-password

You will be prompted for a new password. Type it in and press Enter, and if you see text that says ``true``, the action succeeded. You can then use the website to log into that user account.

.. _central-command-line-user-promote:

Promoting a Web User to administrator by command line
-----------------------------------------------------

In the current release of ODK Central, all users created by the website interface are automatically administrators. If you create a user using the ``user-create`` tool shown above, however, you'll have to perform that step manually. If you do not, the user will be unable to do much of anything at all once they log in.

Please start by performing the steps above in the :ref:`central-command-line-basics` section. Once you do, here is what you would type, assuming the email address of the account you wish to make an administrator is ``example@getodk.org``:

.. code-block:: console

  docker-compose exec service odk-cmd --email example@getodk.org user-promote

If the action succeeded, you will see text that reads ``{"success":"true"}``.

