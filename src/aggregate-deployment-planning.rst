.. spelling::

  dbadmin
  Mumbai
  sysadmin

***********************************
Planning Your Aggregate Deployment
***********************************

ODK Aggregate can be deployed to :doc:`Google App Engine <aggregate-app-engine>`, :doc:`Amazon's EC2 cloud services <aggregate-aws>`, or to :doc:`webservers running Tomcat with MySQL or PostgreSQL <aggregate-tomcat>`. There is also a fully set-up :doc:`virtual machine <aggregate-vm>` that can be run in nearly any environment.

We recommend using Google App Engine or the ODK Aggregate VM before attempting an EC2 or Tomcat deployment.

Once you have tried ODK Aggregate together with :doc:`ODK Collect <collect-intro>` and familiarized yourself with their use, you can consider alternative hosting platforms. You can also think about foregoing Aggregate altogether and just using :doc:`ODK Briefcase <briefcase-guide>`.

This document provides general advise for thinking through your deployment decisions.


Considerations
---------------

Here are some issues to consider when determining whether Google's App Engine cloud services are appropriate for your deployment:

Internet access
~~~~~~~~~~~~~~~~~

Google App Engine and Amazon Web Services both require internet access. If you don't have consistent internet access, ODK Briefcase may be more appropriate.

Tomcat deployments can operate without internet access. In such an environment, ODK Collect would only be able to upload finalized forms after it connects to the network containing the Tomcat deployment.

Computer skills
~~~~~~~~~~~~~~~~~~~

Tomcat deployments have a steep learning curve and require technical aptitude. At a minimum you will be:

- changing network configuration
- selecting and using a website hosting service or specifying and configuring your own server and network router(s)
- installing software
- ensuring that your site has proper power-failure and data-backup systems in place

If this level of systems administration skill is not available, you will probably have more success using Google App Engine.

Ongoing support
~~~~~~~~~~~~~~~~

Tomcat deployments require periodic backups of your data. If data security is a concern, you should have a sysadmin or dbadmin periodically review logs and look for malicious activity. 

Availability
~~~~~~~~~~~~~~~~

Most users provision ODK Collect with blank forms and rarely update those forms over the course of a study. Surveyors upload finalized forms to ODK Aggregate infrequently and opportunistically. 

If that is your situation, you likely do not need as high-availability a server as Google App Engine provides. Google App Engine cloud services provides highly available servers and data storage. Tomcat deployments with similar availability will be expensive to operate unless your organization already has its own information technology department. The less downtime you can tolerate, the more expensive a Tomcat deployment will be.

Dataset size
~~~~~~~~~~~~~~~

Google App Engine can store a virtually unlimited amount of data (well in excess of 1 million submissions). 

However, for both Google App Engine and Apache Tomcat deployments with large datasets (over 7,000 submissions), the "Export to CSV file", "Export to KML file", and "Export to JSON file" functions will cease to operate unless you perform a custom deployment to increase the size of the server on which the background processes run. (That is, you will need to use a larger virtual machine). 

On Google App Engine, this larger server will incur higher billing costs. Additionally, for very large datasets (over 100,000 records), it is highly likely that performance will be better when using MySQL or PostgreSQL, and it is certainly true that you have more optimization opportunities when running your own database servers than are available through Google's cloud services.

Data locality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google App Engine servers may be located anywhere in the world. 

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions. 

In some circumstances, you might be able to use :ref:`encrypted-forms` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine. 

.. note:: 

  See the Google App Engine `Terms of Service <https://cloud.google.com/terms/>`_. 

Billing
~~~~~~~~~

Google App Engine has 24-hour activity quotas that typically enable free use of ODK Aggregate during evaluation and small pilot studies. 

You may be able to run a full study within these activity thresholds provided you:

- collect fewer than 2000 responses
- access the site only during the work day
- can be flexible about when you upload and access data

Otherwise, you will need to set up a billing account with Google.

Open source
~~~~~~~~~~~~~~~

The ODK software is open source and available for use without charge. It is important to recognize that the open source software model does place additional responsibilities on the users of that software.

Unless you pay for assistance when technical support is needed, you will be required to take the initiative to research and find answers, and to perform technical support tasks yourself. 

And, unless you contribute back to the open source community through your involvement in the user groups and through contributions to the project, this software will become irrelevant and obsolete.

App Engine is usually sufficient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For most users, Google App Engine will be the easiest and most cost-effective option. The http://opendatakit.appspot.com site, which is lightly used, typically costs just over the minimum charge of $2.10/week unless there are a lot of users that have set up publishing actions (we purge these periodically). 

A 6000 hour study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011). Keep in mind that you can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (for example, between data gathering campaigns, while you are developing the forms for the next campaign). When disabled, access is restricted to the free daily usage limit.

Minimizing App Engine fees
------------------------------------

On App Engine, the primary consumption is Datastore Reads.

To minimize App Engine usage fees, users should restrict access to the ODK Aggregate website and **not keep browser windows open on the submissions tab**. That tab is refreshed every 6 seconds if the user is actively doing work, or slightly less frequently if they are not. At the default display of 100 submissions (a minimum of 100 Reads), that can quickly add up. 

Keep in mind that every select-one or select-multiple question incurs an additional Read (one for each value stored). And images incur a minimum of 10 Reads. Every 200 questions in your survey costs an additional Read, and each repeat group also costs a Read for each filled-in repeat in that group.

For example, if your survey has 500 questions, with a repeat group containing an additional 300 questions, and the typical survey has 4 filled-in repeats, then the cost to display the Submissions tab is a minimum of 100*( (500 questions in chunks of 200 per Read = 3) + 4*(300 questions in chunks of 200 per Read = 2) ) = 100 * (3 + 4*2) ) = 100 * 11 = 1100 Reads with each refresh of the Submissions tab. At this rate, the free quota would be exceeded within 5 minutes! And this hypothetical survey did not contain any select-one or select-multiple questions, or any audio, video or image captures, all of which would require more Reads.

Also, it is generally more efficient to use ODK Briefcase to generate CSV files than to use ODK Aggregate, as ODK Briefcase will use the locally-cached data to generate the CSV files.

With larger datasets, there are two modes of operation:

    - ODK Aggregate retains the full dataset. 
    
      In this mode, it is slightly more efficient to Pull data to your local computer then immediately Push it back up. This sets some internal tracking logic within ODK Briefcase so that the next Pull is somewhat more efficient (the Push just verifies that what you have locally matches the content on ODK Aggregate).
    
    - ODK Aggregate retains only a portion of the dataset. 
    
      In this mode, the user periodically uses the Purge button on the Forms Management / Submissions Admin tab to remove older data collection records. In this mode, you would never Push data up to ODK Aggregate, as that would restore the purged data.

Finally, to minimizing usage, set up a data publishing to another application (for example, Fusion Tables) and do your data analysis and review there. You can export CSVs from that platform, should you wish to avoid using ODK Briefcase.
