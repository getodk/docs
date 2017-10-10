.. _deployment-planning:

*******************************
Aggregate Deployment Planning
*******************************

ODK Aggregate can be deployed to Google's App Engine, Amazon's EC2 cloud services, and to webservers running Tomcat with MySQL or PostgreSQL databases.

In general, you should gain familiarity with ODK Aggregate using Google's App Engine cloud services or the ODK Aggregate VM before attempting an EC2 or Tomcat deployment. See :ref:`Aggregate installation <install-app-engine>`.

Once you can download forms from ODK Aggregate to :ref:`ODK Collect <collect-introduction>`, fill them out, upload finalized forms to ODK Aggregate, view, export and publish data from within ODK Aggregate, and download data from ODK Aggregate using :doc:`briefcase-guide`, you might then consider whether a Google App Engine cloud services deployment or VM is appropriate for your needs.

Considerations
---------------

Here are some issues to consider when determining whether Google's App Engine cloud services are appropriate for your deployment:

1) **internet access** — Google App Engine requires internet access. If you don't have internet access, consider using only ODK Briefcase; it may be more appropriate. Tomcat deployments can operate without internet access; in such an environment, ODK Collect would only be able to upload finalized forms after it connects to the network containing the Tomcat deployment.
2) **computer skills** — Tomcat deployments have a steep learning curve and require technical aptitude. At a minimum you will be (1) changing network configuration, (2) either selecting and using a website hosting service or specifying and configuring your own server and network router(s), (3) installing software, and (4) ensuring that your site has proper power-failure and data-backup systems in place.
3) **ongoing support** — Tomcat deployments require periodic backups of your data; if data security is a concern, you should have a part-time system- and/or database- administrator to periodically review logs and look for malicious activity.
4) **availability** — Most users provision ODK Collect with blank forms and rarely update those forms over the course of a study; surveyors upload finalized forms to ODK Aggregate infrequently and opportunistically. If that is your situation, you likely do not need as high-availability a server as Google App Engine provides. Google App Engine cloud services provides highly available servers and data storage. Tomcat deployments with similar availability will be expensive to operate unless your organization already has its own information technology department. The less downtime you can tolerate, the more expensive a Tomcat deployment will be.
5) **dataset size** — Google App Engine can store an unlimited amount of data (well in excess of 1 million submissions). However, for both Google App Engine and Apache Tomcat deployments with large datasets (over 7,000 submissions), the "Export to CSV file", "Export to KML file", and "Export to JSON file" functions will cease to operate unless you perform a custom deployment to increase the size of the server on which the background processes run (i.e., use a larger virtual machine). On Google App Engine, this larger server will incur higher billing costs. Additionally, for very large datasets (over 100,000 records), it is highly likely that performance will be better when using MySQL or PostgreSQL, and it is certainly true that you have more optimization opportunities when running your own database servers than are available through Google's cloud services.
6) **data locality and security** — Google App Engine servers may be located anywhere in the world. Depending on the sensitivity of the data and specific storage rules/restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions. In some circumstances, you might be able to use Encrypted Forms(:ref:`read here <encrypted-forms>`) to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine. See the Google App Engine `Terms of Service <https://cloud.google.com/terms/>`_. 
7) **billing** — Google App Engine has 24-hour activity quotas that typically enable free use of ODK Aggregate during evaluation and small pilot studies. You may be able to run a full study within these activity thresholds provided you are collecting fewer than 2000 responses, access the site only during the work day (not 24hr/day), and can be flexible as to when you upload data from ODK Collect or access that data (should the quota have been exceeded).  Otherwise, you will need to set up a billing account with Google.

Finally, while the software is open-source and available for use without charge, it is important to recognize that the open-source software model does place additional responsibilities on the users of that software. Unless you pay for assistance, when technical support is needed, you will be required to take the initiative to research and find answers, and to perform technical support tasks yourself. And, unless you contribute back to the open-source community through your involvement in the user groups and through contributions to the project, this software will become irrelevant and obsolete.

For most users, Google App Engine will be more cost-effective. The http://opendatakit.appspot.com site, which is lightly used, typically costs just over the minimum charge of $2.10/week unless there are a lot of users that have set up publishing actions (we purge these periodically). A 6000 hh study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011). Keep in mind that you can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (e.g., between data gathering campaigns, while you are developing the forms for the next campaign); when disabled, access is restricted to the free daily usage limit.

App Engine Usage Fees
-----------------------

On App Engine, the primary consumption is Datastore Reads.

To minimize App Engine usage fees, users should restrict access to the ODK Aggregate website and **NOT** keep browser windows open on the submissions tab. That tab is refreshed every 6 seconds if the user is actively doing work, or slightly less frequently if they are not. At the default display of 100 submissions (a minimum of 100 Reads), that can quickly add up. Keep in mind that every select-one or select-multiple question incurs an additional Read (one for each value stored). And images incur a minimum of 10 Reads. Every 200 questions in your survey costs an additional Read, and each repeat group also costs a Read for each filled-in repeat in that group.

For example, if your survey has 500 questions, with a repeat group containing an additional 300 questions, and the typical survey has 4 filled-in repeats, then the cost to display the Submissions tab is a minimum of 100*( (500 questions in chunks of 200 per Read = 3) + 4*(300 questions in chunks of 200 per Read = 2) ) = 100 * (3 + 4*2) ) = 100 * 11 = 1100 Reads with each refresh of the Submissions tab. At this rate, the free quota would be exceeded within 5 minutes! And this survey did not contain any select-one or select-multiple questions, or any audio, video or image captures, all of which would require more Reads.

Also, it is generally more efficient to use ODK Briefcase to generate CSV files than to use ODK Aggregate, as ODK Briefcase will use the locally-cached data to generate the CSV files.

With larger datasets, there are two modes of operation:

    1) ODK Aggregate retains the full dataset. In this mode, it is slightly more efficient to Pull data to your local computer then immediately Push it back up. This sets some internal tracking logic within ODK Briefcase so that the next Pull is somewhat more efficient (the Push just verifies that what you have locally matches the content on ODK Aggregate).
    2) ODK Aggregate retains only a portion of the dataset. In this mode, the user periodically uses the Purge button on the Forms Management / Submissions Admin tab to remove older data collection records. In this mode, you would never Push data up to ODK Aggregate, as that would restore the purged data.

Finally, when minimizing usage, setting up a single publisher to, e.g., Fusion Tables, and doing your data analysis and review on that platform will be most cost effective. You can export CSVs from that platform, should you wish to avoid using ODK Briefcase.
