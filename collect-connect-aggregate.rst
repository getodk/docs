Connecting to your own ODK Aggregate Server
=================================================

.. admonition:: Before you get started...

  You need to :doc:`install ODK Aggregate <aggregate-install>` before you can connect to it.
  
  When connecting to an ODK Aggregate server from Collect, you will need a username and password from your Aggregate server. This can be the superuser created when you install Aggregate, or another user account created by you.   

  - See :doc:`aggregate-install` to setup your ODK Aggregate server.
  - See :ref:`Aggregate Site Admin <site-admin>` for details on setting up new users.
  
    
1. From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`


   .. image:: /img/collect-connect/main-menu-highlight-kebab.* 
     :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red. 

   .. image:: /img/collect-connect/kebab-menu-general-settings.* 
     :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.
  
2. Select :guilabel:`Server`

   .. image:: /img/collect-connect/general-settings-server.* 
     :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

3. Select :guilabel:`Type`, and set it to :menuselection:`ODK Aggregate`

   .. image:: /img/collect-connect/server-settings-type-aggregate.* 
     :alt: The Server Settings screen in the Collect app. The first item in the menu is labeled *Type*, and this item is circled in red.

   .. image:: /img/collect-connect/server-settings-type-modal.* 
     :alt: The Server Settings screen in the Collect App, as displayed in the previous image. There is now a modal menu labeled *Platform*, with single-select radio buttons for: *ODK Aggregate*, *Google Drive, Google Sheets*, and *Other*. *ODK Aggregate* is selected and circled in red.
  

4. Edit :guilabel:`ODK Aggregate settings`

   .. image:: /img/collect-connect/server-settings-aggregate-settings.* 
     :alt: The Server Settings screen in the Collect app. Below the *Type* option is a section titled *ODK Aggregate Settings*, with the items labeled *URL*, *Username*, and *Password*. These three items are numbered in red.

   .. image:: /img/collect-connect/server-settings-server-url.* 
     :alt: The Server Settings screen in the Collect app, with a modal overlay titled *Server URL*. There is a single text-entry field with a URL, and buttons labeled OK and CANCEL.

   .. image:: /img/collect-connect/server-settings-odk-username.* 
     :alt: The Server Settings screen in the Collect app, with a modal overlay titled *ODK Username.* There is a single text-entry field, and buttons labeled OK and CANCEL.

   .. image:: /img/collect-connect/server-settings-odk-password.* 
     :alt: The Server Settings screen in the Collect app, with a modal overlay titled *ODK Password*. There is a single obscured-text field, and buttons for OK and CANCEL.
  
------

.. admonition:: Connecting to another OpenRosa server app

  Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`_ can be connected to, using :doc:`the instructions laid out above <collect-connect-aggregate>`. You would still choose :menuselection:`ODK Aggregate` as the server type.

  In :menuselection:`Server Settings`, there is currently a :guilabel:`Type` option of :menuselection:`Other`. It is unlikely you will need this option, since any server application will need to implement the same API as ODK Aggregate. 

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.opendatakit.org/c/support>`_.

  The :menuselection:`Other` option will likely be deprecated in the future, and its use is not recommended.  
