.. spelling::

  dbadmin
  Mumbai
  sysadmin

***********************************
Planning Your Aggregate Deployment
***********************************

ODK Aggregate can be deployed to :doc:`any local or cloud server that runs Tomcat, Java8, and PostgreSQL <aggregate-tomcat>` (MySQL is supported too).

You can also use these guides for some specific cloud providers:

- :doc:`DigitalOcean <aggregate-do>`
- :doc:`Amazon Web Services <aggregate-aws>`

There is also a fully set-up :doc:`virtual machine <aggregate-vm>` that can be run in nearly any environment.

If you have some development background, you can try using:

- A `Docker image <https://github.com/opendatakit/aggregate/blob/master/docs/build-and-run-a-docker-image.md>`_
- A `Docker Compose setup <https://github.com/opendatakit/aggregate/blob/master/docs/build-and-run-with-docker-compose.md>`_

Previous versions of Aggregate can be deployed in :doc:`Google AppEngine <aggregate-app-engine>`, but we strongly recommend deploying Aggregate v2 using any of the guides above.

You can also go without Aggregate altogether and use :doc:`ODK Briefcase  <briefcase-intro>`.

This document provides general advice for thinking through your deployment decisions.

.. _aggregate-deployment-considerations:

Things to Consider
-----------------------

.. _aggregate-deployment-internet-access:

Internet access
~~~~~~~~~~~~~~~~~

DigitalOcean and Amazon Web Services both require internet access. If you don't have consistent internet access, Briefcase may be more appropriate.

Tomcat deployments can operate without internet access. In such an environment, Collect would only be able to upload finalized forms after it connects to the network containing the Tomcat deployment.

.. _aggregate-deployment-computer-skills:

Computer skills
~~~~~~~~~~~~~~~~~~~

Tomcat deployments (including deployment to Amazon Web Services) have a steep learning curve and require technical aptitude. At a minimum you will be:

- changing network configuration
- selecting and using a website hosting service or specifying and configuring your own server and network router(s)
- installing software
- ensuring that your site has proper power-failure and data-backup systems in place

If this level of systems administration skill is not available, you will have more success using the :doc:`DigitalOcean <aggregate-do>` guide, which leverages a CloudConfig stack that will do most of the heavy lifting for you.

.. _aggregate-deployment-ongoing-support:

Ongoing support
~~~~~~~~~~~~~~~~

Tomcat deployments require periodic backups of your data. If data security is a concern, you should have a system administrator or database administrator periodically review logs and look for malicious activity.

.. _aggregate-deployment-dataset-size:

Dataset size
~~~~~~~~~~~~~~~

You have to take into account the size of the data set you need to store, which grows not only with the number of submissions but also with the structure of the forms. Forms with more media attachments will produce larger data sets.

When sizing your infrastructure, take into account:

- Greater storage capacity usually comes associated with higher costs.
- Storage is usually hard to scale. Try to start with enough capacity for your data set and some security slack.
- The computing power doesn't necessarily have to scale with the data set size.

.. note::

  Individual text database fields are capped at a length of 255 by default for performance reasons. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

.. _aggregate-deployment-data-locality:

Data locality
~~~~~~~~~~~~~~

Cloud providers have servers located anywhere in the world.

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions.

In some circumstances, you might be able to use :ref:`encrypted-forms` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine.

.. _aggregate-deployment-open-source:

Open source
~~~~~~~~~~~~~~~

The ODK software is `free <https://www.gnu.org/philosophy/free-sw.en.html>`_, `open source <https://opensource.com/resources/what-open-source>`_, and available for use without charge.

It is important to recognize that the open source software model does place additional responsibilities on the users of that software.

Unless you pay for assistance when technical support is needed, you will be required to take the initiative to research and find answers, and to perform technical support tasks yourself.

Finally, unless you and others contribute back to Open Data Kit through involvement in the community and contributions to the project, this software will become irrelevant and obsolete.

.. seealso:: `Learn more about participating in ODK <https://opendatakit.org/participate/>`_
