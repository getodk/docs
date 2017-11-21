***********************************
Aggregate Installation and Setup
***********************************

Before going through this section, make sure you have used :doc:`ODK Collect  <collect-intro>` and are familiar with how it works.

.. tip::

  - Try the ODK Aggregate `demo server <https://opendatakit.appspot.com>`_ to explore the core functionality.
  - Decide whether to install a cloud instance or a local instance. It is strongly recommended to try an App Engine cloud instance first. If you wish to host locally, see :ref:`Aggregate Deployment Planning <deployment-planning>`
  - Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility.    
  - You must also plan for the security of your data and systems. And finally, it requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer-technical-support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.

  
Install options
==================

.. toctree::
  aggregate-app-engine
  aggregate-tomcat
  aggregate-aws
  
.. _install-vm:

Installing VM (Local or Cloud)
-------------------------------

- The `ODK Aggregate VM <https://gumroad.com/l/odk-aggregate-vm>`_ is a fully-configured install of Aggregate that you can run on any computer. It requires very little setup, works well without Internet connectivity, and gives you complete control over your data collection campaign.
