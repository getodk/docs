Setting Up ODK Aggregate
===============================

.. toctree::
  :maxdepth: 2
   
  aggregate-install
  aggregate-deployment-planning
  aggregate-upgrade
  aggregate-backup

.. _aggregate-setup-tips:
  
Setup Tips and Best Practices
-------------------------------

- Try the ODK Aggregate `demo server <https://opendatakit.appspot.com>`_ to explore the core functionality.

- Decide whether to install a cloud instance or a local instance. It is strongly recommended to try an App Engine cloud instance first. If you wish to host locally, see :ref:`Aggregate Deployment Planning <deployment-planning>`

- Local hosting implies that you are taking ownership of the off-site back up and restoration of your data and are documenting the steps necessary to return your systems to operation in circumstances that might include a full hardware failure or the destruction of your facility.    

- You must also plan for the security of your data and systems. And finally, it requires that you `configure your network routers <https://opendatakit.org/use/aggregate/tomcat-install/#Configure_for_Network_Access>`_. It is recommended to seek assistance from your local computer-technical-support community before proceeding. The set-up of the ODK Aggregate web server and database are very easy in comparison.
