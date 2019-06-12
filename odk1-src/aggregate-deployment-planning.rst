***********************************
Planning Your Aggregate Deployment
***********************************

ODK Aggregate can be deployed to :doc:`any local or cloud server that runs Tomcat, Java8, and PostgreSQL <aggregate-tomcat>` (MySQL is supported too).

You can also use these guides for some specific cloud providers:

- :doc:`DigitalOcean <aggregate-digital-ocean>`
- :doc:`Amazon Web Services <aggregate-aws>`

There is also a fully set-up :doc:`virtual machine <aggregate-vm>` that can be run in nearly any environment.

If you have highly-technical user, you can also try using:

- A `Docker image <https://github.com/opendatakit/aggregate/blob/master/docs/build-and-run-a-docker-image.md>`_
- A `Docker Compose setup <https://github.com/opendatakit/aggregate/blob/master/docs/build-and-run-with-docker-compose.md>`_

Previous versions of Aggregate (v1.x) can be deployed in :doc:`Google App Engine <aggregate-app-engine>`, but we strongly recommend deploying Aggregate v2.x using any of the guides above.

You can also go without Aggregate altogether and use :doc:`ODK Briefcase <briefcase-intro>`.

This document provides general advice for thinking through your deployment decisions.

.. _aggregate-deployment-considerations:
.. _aggregate-deployment-internet-access:

Internet access
---------------

DigitalOcean and Amazon Web Services both require internet access. If you don't have consistent internet access, :doc:`ODK Briefcase <briefcase-intro>` may be more appropriate.

Tomcat deployments can operate without internet access. In such an environment, Collect would only be able to upload finalized forms after it connects to the network containing the Tomcat deployment.

.. _aggregate-deployment-computer-skills:

Computer skills
---------------

Custom `Tomcat deployments in local or cloud servers <aggregate-tomcat>`_, including the one described in the :doc:`Amazon Web Services <aggregate-aws>` guide, have a steep learning curve and require technical aptitude. At a minimum you will be:

- changing network configuration
- selecting and using a website hosting service or specifying and configuring your own server and network router(s)
- installing software
- ensuring that your site has proper power-failure and data-backup systems in place

If this level of systems administration skill is not available, you will have more success using the :doc:`DigitalOcean <aggregate-digital-ocean>` guide, which leverages a Cloud-Config stack that will do most of the heavy lifting for you.

.. _aggregate-deployment-component-versions:

Component versions
------------------

ODK Aggregate should work with these minimum component versions. In most cases, newer versions should also work.

.. csv-table::
  :header: , ≥ v1.4.13

  Java, 8
  Tomcat, 8.0
  PostgreSQL, 9.4
  MySQL (not MariaDB), 5.7

.. _aggregate-deployment-ongoing-support:

Ongoing support
---------------

- You should consider doing periodic backups of your data.

- If data security is a concern, you should have a system administrator or database administrator periodically review logs and look for malicious activity.

.. _aggregate-deployment-dataset-size:

Infrastructure architecture
---------------------------

In these docs we explain how to deploy a monolithic server with everything Aggregate needs to run (Tomcat, PostgreSQL, SSL support), but there is a multitude of scenarios that you might want to consider:

- You could deploy Aggregate on one machine and the database in a separate machine, or even use a cloud database.
- You could have high-availability or an horizontal scalability option by using a load balancer.
- You could provide SSL security with a load balancer or proxy.

If you are considering alternative architectures for your specific needs, we recommend you ask for help in the `support forum <https://forum.opendatakit.org/c/support>`_.

Dataset size
------------

You have to take into account the size of the data set you need to store, which grows not only with the number of submissions but also with the structure of the forms. Forms with more media attachments will produce larger data sets.

When sizing your infrastructure, take into account:

- Greater storage capacity usually comes associated with higher costs.
- Storage is usually hard to scale. Try to start with enough capacity for your data set and add a little bit extra.
- The computing power doesn't necessarily have to scale with the data set size.

.. note::

  For historical reasons, individual text database fields are capped at a length of 255 by default. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

.. _aggregate-deployment-data-locality:

Data locality
-------------

Cloud providers have servers located all over the world. Most of these providers will let you choose where your server should be located.

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions.

.. _aggregate-deployment-security-and-protected-data:

Secure and protected data
-------------------------

If you need to prevent eavesdroppers from seeing your data as it is transmitted to your ODK Aggregate instance, you need to do one of the following:

- only connect to ODK Aggregate from within your organization's network (when the submitting devices are on your premises)
- obtain an SSL certificate and install it on your server (a certificate is required to secure transmissions over `https`)
- use :doc:`encrypted-forms`

Encrypted forms can be used in conjunction with either of the first two suggestions.

If you are not using encrypted forms and are handling sensitive data, a computer security specialist should review your system and your security procedures.

.. note::

  Use of an SSL and `https` is recommended for any deployment accessed from the internet.


.. _aggregate-deployment-availability:

Availability
------------

Decide the availability of your server depending on how frequently you want to update and upload forms. If you do need a high-availability server, you need to talk to your Internet Service Provider (ISP) as to their availability guarantees.

.. _aggregate-deployment-data-loss:

Data loss
---------

Your tolerance to data loss will impact your backup schedule and your server hardware. Invest in a system based on your tolerance to data loss. Seek technical assistance for these requirements.

