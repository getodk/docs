.. spelling::

  dbadmin
  Mumbai
  sysadmin

***********************************
Planning Your Aggregate Deployment
***********************************

ODK Aggregate can be deployed to:

- :doc:`Google App Engine <aggregate-app-engine>`
- :doc:`Amazon's EC2 cloud services <aggregate-aws>`
- :doc:`any web server running Tomcat with MySQL or PostgreSQL <aggregate-tomcat>`. 

There is also a fully set-up :doc:`virtual machine <aggregate-vm>` that can be run in nearly any environment.

We recommend using Google App Engine or the ODK Aggregate VM before attempting an EC2 or Tomcat deployment. Once you have tried Aggregate together with :doc:`ODK Collect <collect-intro>` and familiarized yourself with their use, you can consider alternative hosting platforms. 

You can also go without Aggregate altogether and use :doc:`ODK Briefcase  <briefcase-intro>`.

This document provides general advice for thinking through your deployment decisions.

.. _aggregate-deployment-considerations:

Things to Consider
-----------------------

.. _aggregate-deployment-internet-access:

Internet access
~~~~~~~~~~~~~~~~~

Google App Engine and Amazon Web Services both require internet access. If you don't have consistent internet access, Briefcase may be more appropriate. 

Tomcat deployments can operate without internet access. In such an environment, Collect would only be able to upload finalized forms after it connects to the network containing the Tomcat deployment.

.. _aggregate-deployment-computer-skills:

Computer skills
~~~~~~~~~~~~~~~~~~~

Tomcat deployments (including deployment to Amazon Web Services) have a steep learning curve and require technical aptitude. At a minimum you will be:

- changing network configuration
- selecting and using a website hosting service or specifying and configuring your own server and network router(s)
- installing software
- ensuring that your site has proper power-failure and data-backup systems in place

If this level of systems administration skill is not available, you will have more success using Google App Engine.

.. _aggregate-deployment-ongoing-support:

Ongoing support
~~~~~~~~~~~~~~~~

Tomcat deployments require periodic backups of your data. If data security is a concern, you should have a system administrator or database administrator periodically review logs and look for malicious activity. 

.. _aggregate-deployment-availability:

Availability
~~~~~~~~~~~~~~~~

Google App Engine provides highly available servers and data storage. Tomcat deployments with similar availability will be expensive to operate unless your organization already has its own information technology department. The less downtime you can tolerate, the more expensive a Tomcat deployment will be.

On the other hand, high availability is not an issue for many deployments. Most users of Collect download blank forms once and rarely update those forms over the course of a study. Surveyors upload finalized forms to Aggregate infrequently and opportunistically. If that is your situation, you likely do not need a server that is as highly available as Google App Engine provides. 

.. _aggregate-deployment-dataset-size:

Dataset size
~~~~~~~~~~~~~~~

Google App Engine can store a virtually unlimited amount of data --- well in excess of a million submissions.

However, in deployments with data sets exceeding 7,000 submissions,
the :ref:`data export feature <export-data>` will stop working. To correct this, you will need a custom deployment with a larger virtual machine. This problem affects both Google App Engine and Tomcat deployments.

On Google App Engine, a larger server will incur higher billing costs. Additionally, for datasets of over 100,000 records, it is likely that performance will be better when using MySQL or PostgreSQL, rather than Google App Engine's data store. You also have more optimization opportunities when running your own database servers than are available through Google's cloud services.

.. note::

  Individual text database fields are capped at a length of 255 by default for performance reasons. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

.. _aggregate-deployment-data-locality:

Data locality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google App Engine servers may be located anywhere in the world. 

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions. 

In some circumstances, you might be able to use :ref:`encrypted-forms` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine. 

.. seealso:: `Google Cloud Services Terms of Service <https://cloud.google.com/terms/>`_. 

.. _aggregate-deployment-billing:

Billing
~~~~~~~~~

Google App Engine has 24-hour activity quotas that typically enable free use of ODK Aggregate during evaluation and small pilot studies. 

You may be able to run a full study within these activity thresholds provided you:

- collect fewer than 2000 responses
- access the site only during the work day
- can be flexible about when you upload and access data

Otherwise, you will need to set up a billing account with Google.

.. note::

  These usage limits are well within what is needed to try out ODK,
  to determine if it would be a good fit for your data collection needs.
  
  Because of this, and its ease of setup,
  we recommend using Google App Engine 
  in test deployments and pilot studies,
  even if you will likely need a custom deployment later on.
  
.. _aggregate-deployment-open-source:

Open source
~~~~~~~~~~~~~~~

The ODK software is `free <https://www.gnu.org/philosophy/free-sw.en.html>`_, `open source <https://opensource.com/resources/what-open-source>`_, and available for use without charge. 

It is important to recognize that the open source software model does place additional responsibilities on the users of that software.

Unless you pay for assistance when technical support is needed, you will be required to take the initiative to research and find answers, and to perform technical support tasks yourself. 

Finally, unless you and others contribute back to Open Data Kit through involvement in the community and contributions to the project, this software will become irrelevant and obsolete.

.. seealso:: `Learn more about participating in ODK <https://opendatakit.org/participate/>`_

.. _aggregate-deployment-app-engine-sufficient:

.. App Engine is usually sufficient
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   For most users, Google App Engine will be the easiest and most cost-effective option. 

   Two examples illustrate the cost-effectiveness of Google App Engine:

   - The fee to run the `ODK Aggregate Demo Server <http://opendatakit.appspot.com>`_ is near the minimum weekly charge, costing a few dollars a week.

   - A 6000 hour study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011). 

   You can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (for example, between data gathering campaigns, while you are developing the forms for the next campaign). When disabled, access is restricted to the free daily usage limit.

.. _minimizing-app-engine-fees:

Minimizing App Engine fees
------------------------------------

On App Engine, the major driver of cost is Datastore Reads. These add up quickly:

- Viewing a page of form submissions incurs *at least* one Read for each submission.
- Each multiple-choice question in a form incurs an additional Read on every displayed submission.
- An additional read is incurred for every 200 questions in your survey.
- Each image incurs at least 10 reads.
- The default view shows 100 submissions.
- The form submissions display refreshes every six seconds.

For example, if your survey has 500 questions (*q*), with a repeat group containing an additional 300 questions, the typical survey has 4 filled-in repeats (*rpt*), and 100 submissions (*s*) are shown on each page load (*pl*), then the cost to display the Submissions tab is a minimum of 1100 Reads (*R*) with each refresh of the Submissions tab. 

.. math::

  100 s/pl \times (500 q/s  \times  \lfloor 1 R / 200 q \rfloor + 4 rpt/s \times 300 q/rpt \times \lfloor 1 R / 200 q \rfloor) = 1100 \ R/pl
 

At this rate, the free quota would be exceeded within 5 minutes! 

And this hypothetical survey did not contain any select-one or select-multiple questions, or any audio, video or image captures, all of which would require more Reads.

Therefore, to reduce datastore reads:

 - :ref:`restrict access to the Aggregate website <aggregate-permissions>`
 - do not keep the browser window open on the submissions tab
 - :doc:`export or publish your data <aggregate-data-access>`, and do your analysis in a different tool
 - use :doc:`briefcase-intro` instead of Aggregate to generate CSV files
 
It is generally more efficient to use Briefcase to generate CSV files than to use Aggregate, as Briefcase will use the locally cached data to generate the CSV files.

With larger datasets, there are two modes of operation:

    - Aggregate retains the full dataset. 
    
      In this mode, it is slightly more efficient to Pull data to your local computer then immediately Push it back up. This sets some internal tracking logic within Briefcase so that the next Pull is somewhat more efficient, as the Push only verifies that what you have locally matches the content on Aggregate, rather than re-uploading all of it.
    
    - Aggregate retains only a portion of the dataset. 
    
      In this mode, you periodically purge older data collection records and never Push data up to Aggregate, as that would restore the purged data.
