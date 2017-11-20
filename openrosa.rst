OpenRosa
==========

OpenRosa is a set of communication standards for moving blank forms and completed form instances between server applications (like ODK Aggregate) and clients (like :doc:`ODK Collect  <collect-intro>`).

They were originally worked on by the OpenRosa WorkGroup, and they were an outgrowth of the JavaRosa project. The working group is no longer active. However, many apps within the ODK ecosystem (including Collect and Aggregate) continue to implement the API.

This set of docs is intended to provide information about the OpenRosa standards, for use by developers working on applications that communicate with other applications within the ODK ecosystem.

.. _openrosa-1-0-apis:

OpenRosa 1.0 APIs
-------------------

OpenRosa 1.0 APIs were formally approved by the OpenRosa Working Group in December of 2011. To be considered "OpenRosa 1.0 Compliant," a system must implement all 5 of the OpenRosa 1.0 APIs.


.. toctree::
  :maxdepth: 2
 
  openrosa-metadata
  openrosa-http
  openrosa-authentication
  openrosa-form-submission
  openrosa-form-list
