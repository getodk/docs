Connecting to a Server
================================

ODK Collect is used to complete surveys with participants. But if you want to review and analyse your collected data, you'll need to upload your collected data to another application.

.. note::

  When you first install Collect, it connects to the `ODK Aggregate Demo server <https://opendatakit.appspot.com/Aggregate.html>`_. This allows you to try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, :doc:`filling them out   <collect-filling-forms>`, and :ref:`uploading completed forms <uploading-forms>` back to the demo server.
  
  Once you are done "trying out" Collect, and you start actually using it, you will need to decide on a plan for managing forms and data submissions.

The two most common options for form and data management are:

.. toctree::
  :maxdepth: 2

  collect-connect-aggregate
  collect-connect-google
 
:doc:`aggregate-guide` provides a robust data repository with tools for data visualization, querying, and export. For complex data collection and aggregation tasks, it is usually the right choice. However, setting up and maintaining an Aggregate server is not a trivial matter. 

Using Google Drive to manage form submissions is simpler and, in most cases, cheaper. With this simplicity you sacrifice a richer feature set. Additionally, using Google Drive may not meet your privacy requirements.

.. _other-collect-server-options:

Other options
~~~~~~~~~~~~~~~

Managing forms from an ODK Aggregate server or Google Drive is typical. However, there are other ways to use Collect.

 - :ref:`Upload blank forms directly to your device <loading-forms-directly>`
 - :doc:`Download completed forms directly with adb <collect-adb>`
 - :doc:`Use ODK Briefcase <briefcase-forms>`
