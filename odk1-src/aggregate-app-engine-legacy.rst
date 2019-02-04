(Legacy) Installing Aggregate v1 on Google App Engine
=====================================================

.. warning::

  This document refers only to ODK Aggregate v1

In February 2019 ODK Aggregate v2 was released, removing official support for Google AppEngine, which many users relied upon to deploy Aggregate for their data collection campaigns.

This page gathers all the information from this docs that was previously available about Google AppEngine concerns and tips regarding Aggregate.

Remember that all the information in this page and others linked here refers only to Aggregate v1

Planning Your Aggregate Deployment
----------------------------------

We recommend using Google App Engine before attempting an EC2 or Tomcat deployment of Aggregate v1. Once you have tried Aggregate together with :doc:`ODK Collect <collect-intro>` and familiarized yourself with their use, you can consider alternative hosting platforms.

Internet access
~~~~~~~~~~~~~~~~~

Google App Engine and Amazon Web Services both require internet access. If you don't have consistent internet access, Briefcase may be more appropriate.

Dataset size
~~~~~~~~~~~~~~~

Google App Engine can store a virtually unlimited amount of data --- well in excess of a million submissions.

However, in deployments with data sets exceeding 7,000 submissions,
the :ref:`data export feature <export-data>` will stop working. To correct this, you will need a custom deployment with a larger virtual machine. This problem affects both Google App Engine and Tomcat deployments.

On Google App Engine, a larger server will incur higher billing costs. Additionally, for datasets of over 100,000 records, it is likely that performance will be better when using MySQL or PostgreSQL, rather than Google App Engine's data store. You also have more optimization opportunities when running your own database servers than are available through Google's cloud services.

.. note::

  Individual text database fields are capped at a length of 255 by default for performance reasons. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

Data locality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google App Engine servers may be located anywhere in the world.

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions.

In some circumstances, you might be able to use :ref:`encrypted-forms` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine.

.. seealso:: `Google Cloud Services Terms of Service <https://cloud.google.com/terms/>`_.

Billing
~~~~~~~~~

For identity verification purposes, Google requires a credit card or banking details to use the Google Cloud Platform that Google App Engine runs on. Accounts that meet this requirement receive a recurring $200 monthly credit per billing account.

Independent of Cloud Platform credits, App Engine allows a certain amount of free activity. These free quotas reset every 24 hours and are high enough to enable free use of ODK Aggregate during evaluation and small pilot studies.

You may be able to run a full deployment within these activity thresholds provided you:

- collect fewer than 2000 responses
- access the site a limited number of times a day
- can be flexible about when you upload and access data

Deployments with more activity that do not wish to wait 24 hours for quotas to reset can enable billing on their App Engine project.

Once billing is enabled, ODK Aggregate will start using the monthly credit that comes from the Cloud Platform. Once those credits are finished, the credit card or bank on file will then be used. Billing account owners can set spending limits to manage application costs.

Most ODK deployments will not surpass the $200/month credit and non-profits using more than that can apply for more credits through `Google for Nonprofits <https://www.google.com/nonprofits/>`_.

.. App Engine is usually sufficient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   For most users, Google App Engine will be the easiest and most cost-effective option.

   Two examples illustrate the cost-effectiveness of Google App Engine:

   - The fee to run the `ODK Aggregate Demo Server <http://opendatakit.appspot.com>`_ is near the minimum weekly charge, costing a few dollars a week.

   - A 6000 hour study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011).

   You can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (for example, between data gathering campaigns, while you are developing the forms for the next campaign). When disabled, access is restricted to the free daily usage limit.

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
