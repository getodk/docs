Connecting to a Server
================================

ODK Collect is used to complete surveys with participants. But if you want to review and analyse your collected data, you'll need to upload your collected data to another application.

.. note::

  When you first install Collect, it connects to the `ODK Aggregate Demo server <https://opendatakit.appspot.com/Aggregate.html>`_. This allows you to try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :ref:`filling them out <fill-blank-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.
  
  Once you are done "trying out" ODK Collect, and you start actually using it, you will need to decide on a plan for managing forms and data submissions.






.. _choosing-collect-server-options:

Choosing a server option for Collect
--------------------------------------

The two most common options for form and data management are:

 - :ref:`connecting-to-aggregate`
 - :ref:`connecting-to-google`
 
:doc:`aggregate-guide` provides a robust data repository with tools for data visualization, querying, and export. For complex data collection and aggregation tasks, it is usually the right choice. However, setting up and maintaing an Aggregate server is not a trivial matter. 

Using Google Drive to manage form submissions is simpler and, in most cases, cheaper. With this simplicity you sacrifice a richer feature set. Additionally, using Google Drive may not meet your privacy requirements.

.. _other-collect-server-options:

Other options
~~~~~~~~~~~~~~~

Managing forms from an ODK Aggregate server or Google Drive is typical. However, there are other ways to use ODK Collect. You can also :ref:`upload blank forms directly to your device <loading-forms-directly>`, :doc:`download completed forms directly with adb <collect-adb>`, or :doc:`use ODK Briefcase <briefcase-forms>`.







.. _connecting-to-aggregate:

Connecting to your own ODK Aggregate Server
------------------------------------------------

.. admonition:: Before you get started...

  You need to :doc:`install ODK Aggregate <aggregate-install>` before you can connect to it.
  
  When connecting to an ODK Aggregate server from Collect, you will need a username and password from your Aggregate server. This can be the superuser created when you install Aggregate, or another user account created by you.   

  - See :doc:`aggregate-install` to setup your ODK Aggregate server.
  - See :ref:`Aggregate Site Admin <site-admin>` for details on setting up new users.
  
    
From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/main-menu-highlight-kebab.* 
  :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red. 

.. image:: /img/collect-connect/kebab-menu-general-settings.* 
  :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.
  
Select :guilabel:`Server`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/general-settings-server.* 
  :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

Select :guilabel:`Type`, and set it to :menuselection:`ODK Aggregate`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/server-settings-type-aggregate.* 
  :alt: The Server Settings screen in the Collect app. The first item in the menu is labelled *Type*, and this item is circled in red.
  
.. image:: /img/collect-connect/server-settings-type-modal.* 
  :alt: The Server Settings screen in the Collect App, as displayed in the previous image. There is now a modal menu labelled *Platform*, with single-select radio buttons for: *ODK Aggregate*, *Google Drive, Google Sheets*, and *Other*. *ODK Aggregate* is selected and circled in red.
  

Edit :guilabel:`ODK Aggregate settings`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. image:: /img/collect-connect/server-settings-aggregate-settings.* 
  :alt: The Server Settings screen in the Collect app. Below the *Type* option is a section titled *ODK Aggregate Settings*, with the itmes labelled *URL*, *Username*, and *Password*. These three items are numbered in red.

.. image:: /img/collect-connect/server-settings-server-url.* 
  :alt: The Server Settings screen in the Collect app, with a modal overlay titled *Server URL*. There is a single text-entry field with a URL, and buttons labelled OK and CANCEL.
  
.. image:: /img/collect-connect/server-settings-odk-username.* 
  :alt: The Server Settings screen in the Collect app, with a modal overal titled *ODK Username.* There is a single text-entry field, and buttons labelled OK and CANCEL.
  
.. image:: /img/collect-connect/server-settings-odk-password.* 
  :alt: The Server Settings screen in the Collect app, with a modal overlay titled *ODK Password*. There is a single obscured-text field, and buttons for OK and CANCEL.
  

.. _connecting-to-google:

Connecting to a Google Drive Account
--------------------------------------

.. admonition:: Before you get started...

  ODK Collect connects to your Google Account using the Google Play Store credentials stored on your Android device. This means that before you can connect Collect to your Google account, you need to `add your account to your device <https://support.google.com/googleplay/answer/2521798?hl=en>`_.

    
From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/main-menu-highlight-kebab.* 
  :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red. 

.. image:: /img/collect-connect/kebab-menu-general-settings.* 
  :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.
  
Select :guilabel:`Server`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/general-settings-server.* 
  :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

Select :guilabel:`Type`, and set it to :menuselection:`Google Drive, Google Sheets`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/server-settings-type-google.* 
  :alt: The Server Settings screen in the Collect app. The first item in the menu is labelled *Type*, and this item is circled in red.
  
.. image:: /img/collect-connect/server-settings-type-model-google.* 
  :alt: The Server Settings screen in the Collect App, as displayed in the previous image. There is now a modal menu labelled *Platform*, with single-select radio buttons for: *ODK Aggregate*, *Google Drive, Google Sheets*, and *Other*. *Google Drive, Google Sheets* is selected and circled in red.

Select your :guilabel:`Google Account`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-connect/server-settings-google-account.* 
  :alt: The Server Settings screen in the Collect app. Below the *Type* setting is a section titled *Google Sheets settings*, eith items for *Google Account* and *Fallback submission URL*. *Google Account* is circled in red.

.. image:: /img/collect-connect/server-settings-google-account-modal.* 
  :alt: The Server Settings screen as displayed in the previous image. There is now a modal labelled *Google account,* with a set of radio button (single select) options. The options are Google Accounts associated with the device, and a final option labelled 'No account'. Below that is a button labelled CANCEL.

  
Optional: Set a :guilabel:`Fallback submission URL`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Collect with a Google account, form submissions will be posted to a Google Sheet specified in the form. 

You have the option to specify a :guilabel:`Fallback submisison URL`. This is the URL of a Google sheet to which form submissions will be posted if the submitted form does not specify it own URL.

If your forms will specify a submission URL, you can leave this setting empty. Otherwise, enter the URL of a Google sheet you would like to use.  
    
.. _connecting-to-other:

Connecting to another server app
-----------------------------------

Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`_ can be connected to, using the :ref:`connecting-to-aggregate` instructions. Choose :menuselection:`ODK Aggregate` as the server type.

.. warning::

  In :menuselection:`Server Settings`, there is currently a :guilabel:`Type` option of :menuselection:`Other`. It is unlikely you will need this option, since any server application will need to implement the same API as ODK Aggregate. 

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.opendatakit.org/c/support>`_.

  The :menuselection:`Other` option will likely be deprecated in the future, and its use is not recommended.  
