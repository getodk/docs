Connecting to your own ODK Aggregate Server
=================================================

.. admonition:: Before you get started...

  You need to :doc:`install ODK Aggregate <aggregate-install>` before you can connect to it.

  When connecting to an ODK Aggregate server from Collect, you will need a username and password from your Aggregate server. This can be the superuser created when you install Aggregate, or another user account created by you.

  - See :doc:`aggregate-install` to setup your ODK Aggregate server.
  - See :doc:`Aggregate Site Admin <aggregate-admin>` for details on setting up new users.


1. From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`


   .. image:: /img/collect-connect/main-menu-highlight-kebab.*
     :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red.

   .. image:: /img/collect-connect/kebab-menu-general-settings.*
     :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.

2. Select :guilabel:`Server`

   .. image:: /img/collect-connect/general-settings-server.*
     :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

4. Make sure :guilabel:`ODK` is selected under :guilabel:`Type` and then fill in the :guilabel:`URL`, :guilabel:`Username` and :guilabel:`Password` for your server:

   .. image:: /img/collect-connect/server-settings-odk.*
     :alt: The Server Settings screen in the Collect app. Below the *Type* option there are three items labeled *URL*, *Username*, and *Password*.

------

.. admonition:: Connecting to another OpenRosa server app

  Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`_ can be connected to, using :doc:`the instructions laid out above <collect-connect-aggregate>`. You would still choose :menuselection:`ODK` as the :menuselection:`Type`.

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.getodk.org/c/support>`_.
