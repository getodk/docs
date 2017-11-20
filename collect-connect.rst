Connecting to a Server
================================

When you first install Collect, it connects to the `ODK Aggregate Demo server <https://opendatakit.appspot.com/Aggregate.html>`_. You can try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :ref:`filling them out <fill-blank-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.

.. tip::
  Managing forms from an ODK Aggregate server or Google Drive is typical. However, there are other ways to use ODK Collect. You can also :ref:`upload blank forms directly to your device <loading-forms-directly>`, :doc:`download completed forms directly with adb <collect-adb>`, or :doc:`use ODK Briefcase <briefcase-forms>`.


.. _connecting-to-aggregate:

Connecting to your own ODK Aggregate Server
------------------------------------------------

See :doc:`aggregate-install` to setup your ODK Aggregate server.

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`ODK Aggregate`.
- Edit :guilabel:`ODK Aggregate settings` to connect to your ODK Aggregate instance.

.. _connecting-to-google:

Connecting to a Googe Drive Account
--------------------------------------

- Open the app's main menu (:guilabel:`⋮`)  and then select :menuselection:`General Settings`.
- Select :guilabel:`Server`.
- :guilabel:`Type` should be set to :menuselection:`Google Drive, Google Sheets`.
- Select your Google account. (The available Google Accounts are pulled from the Google Play Store app.)

.. _connecting-to-other:

Connecting to another server app
-----------------------------------

Any server application that implements the `OpenRosa API <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`_ can be connected to, using the :ref:`connecting-to-aggregate` instructions. Choose :menuselection:`ODK Aggregate` as the server type.

.. warning::

  In :menuselection:`Server Settings`, there is currently a :guilabel:`Type` option of :menuselection:`Other`. It is unlikely you will need this option, since any server application will need to implement the same API as ODK Aggregate. 

  If you think you might need to connect to a non-Aggregate server application, and are having trouble, we encourage you to visit our `Support Forum <https://forum.opendatakit.org/c/support>`_.

  The :menuselection:`Other` option will likely be deprecated in the future, and its use is not recommended.  
