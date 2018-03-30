ODK Services
==============

.. _services-intro:

:dfn:`ODK Services` is a program that handles database access, file access, and data synchronization services between all the ODK 2 applications. Mostly this happens behind the scenes, but you will need to install ODK Services as a prerequisite to using the other ODK 2 tools.

It also allows you to sync data collected by the ODK 2 tools with an ODK Cloud Endpoint. The Services application can be used to reset the Cloud Endpoint with the data that is on a tablet or to sync the data on the tablet with what is currently on the Cloud Endpoint.

.. _services-intro-user-guide:

User Guide
-----------------------------

.. toctree::
  :maxdepth: 2

  services-install
  services-using

.. _services-intro-architect-guide:

Deployment Architect Guide
----------------------------------

.. toctree::
  :maxdepth: 2

  services-managing
  services-internals
