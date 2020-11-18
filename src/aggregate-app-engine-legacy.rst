.. spelling::

  Mumbai

Google App Engine Support (Legacy)
==================================

.. warning::
  Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

.. warning::

  In February 2019, ODK Aggregate v2.x was released with support for Google App Engine removed. This page gathers all the information previously available about Google App Engine for Aggregate v1.x. See `why we are removing App Engine support <https://forum.getodk.org/t/upcoming-changes-to-aggregate/17582>`_ for more information.

Planning Your Aggregate Deployment
----------------------------------

The recommended method to deploy Aggregate v1.x is using Google App Engine or the :doc:`ODK Aggregate VM <aggregate-vm>`. Try those first before attempting other methods.

Internet access
~~~~~~~~~~~~~~~

Google App Engine requires internet access. If you don't have consistent internet access, :doc:`ODK Briefcase <briefcase-intro>` may be more appropriate.

Availability
~~~~~~~~~~~~

Google App Engine provides highly available servers and data storage.

Dataset size
~~~~~~~~~~~~

Google App Engine can store a virtually unlimited amount of data --- well in excess of a million submissions.

However, in deployments with data sets exceeding 7,000 submissions, the :ref:`data export feature <export-data>` will stop working. To correct this, you will need to :doc:`increase server size <aggregate-boost-performance>`.

On Google App Engine, a larger instance will incur higher billing costs. Additionally, for datasets of over 100,000 records, it is likely that performance will be better when using MySQL or PostgreSQL, rather than Google App Engine's data store. You also have more optimization opportunities when running your own database servers than are available through Google's cloud services.

.. note::

  Individual text database fields are capped at a length of 255 by default for performance reasons. If you intend to collect text data longer than 255 characters (including using types :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`), your forms should :doc:`specify database field lengths greater than 255 <aggregate-field-length>`.

Data locality and security
~~~~~~~~~~~~~~~~~~~~~~~~~~

Google App Engine servers may be located anywhere in the world.

Depending on the sensitivity of the data and specific storage rule, regulations, or restrictions of your country or organization, the server infrastructure may not have all necessary locality guarantees or security precautions.

In some circumstances, you might be able to use :ref:`encrypted forms <encrypted-forms>` to achieve compliance. You should research and comply with applicable laws and regulations before storing data on Google App Engine.

.. seealso:: `Google Cloud Services Terms of Service <https://cloud.google.com/terms/>`_.

Billing
~~~~~~~

For identity verification purposes, Google requires a credit card or banking details to use the Google Cloud Platform that Google App Engine runs on. Accounts that meet this requirement receive a recurring $200 monthly credit per billing account.

Independent of Cloud Platform credits, App Engine allows a certain amount of free activity. These free quotas reset every 24 hours and are high enough to enable free use of ODK Aggregate during evaluation and small pilot studies.

You may be able to run a full deployment within these activity thresholds provided you:

- collect fewer than 2000 responses
- access the site a limited number of times a day
- can be flexible about when you upload and access data

Deployments with more activity that do not wish to wait 24 hours for quotas to reset can enable billing on their App Engine project.

Once billing is enabled, ODK Aggregate will start using the monthly credit that comes from the Cloud Platform. Once those credits are finished, the credit card or bank on file will then be used. Billing account owners can set spending limits to manage application costs.

Most ODK deployments will not surpass the $200/month credit and non-profits using more than that can apply for more credits through `Google for Nonprofits <https://www.google.com/nonprofits/>`_.

Cost effectiveness
~~~~~~~~~~~~~~~~~~

For most users, Google App Engine will be the easiest and most cost-effective option.

Two examples illustrate the cost-effectiveness of Google App Engine:

- A 6000 hour study in Mumbai that ran from 01 September 2011 through 29 February 2012 also incurred the minimum charge of $2.10/week for mid-November onward (Google did not begin billing until mid November 2011).

You can enable billing on an as-needed weekly basis. You will incur no charges at all if you disable billing (for example, between data gathering campaigns, while you are developing the forms for the next campaign). When disabled, access is restricted to the free daily usage limit.

Minimizing fees
~~~~~~~~~~~~~~~~

.. hint::

  In the :guilabel:`Preferences` sub-tab under :guilabel:`Site Admin` tab, you can *Disable faster background actions* to reduce App Engine quota usage.

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

Installing Aggregate
--------------------

See :doc:`Installing Aggregate on Google App Engine <aggregate-app-engine>`.

Backing up Aggregate
--------------------

You can export and import Datastore entities using the `managed export and import service <https://cloud.google.com/datastore/docs/export-import-entities>`_. See `ODK Aggregate data wrangling for App Engine <https://forum.getodk.org/t/odk-aggregate-data-wrangling-compendium/14174>`_ for more detail.

Tips and Best Practices
-----------------------

Aggregate Limitations
~~~~~~~~~~~~~~~~~~~~~

Pushing Data to Aggregate
"""""""""""""""""""""""""

If Aggregate is :doc:`installed on Google App Engine <aggregate-app-engine>`, using the default datastore as described in our documentation, a combination of request time limits and datastore implementation create the following issues.

**Simultaneous push requests will block each other and may time out**

Within ODK Aggregate, there is a global mutex (*TaskLock* across all server instances, mediated by the datastore layer) in the server when inserting submissions. Having multiple push requests occurring simultaneously will cause them to block on the mutex, chewing up their 60-second request limit, as they get processed in single file no matter how many server instances are spun up.

The solution to this is: Serialize your push requests.

**Time limit may be exceeded on low-bandwidth connections**

The 60-second request limit can be very commonly exceeded over low-bandwidth connections, and even text-only submissions can be impacted on satellite connections. That is why ODK Collect splits submissions into multiple 10MB submission requests. The timer starts upon receipt of the first byte, so a slow connection can account for a sizeable portion of those 60 seconds. The same applies for sending a response. The processing on the server is generally negligible in relation to the transmission times.

.. note::

   - The above two limitations, the global mutex and the in-memory copies/full-packet-assembly, are a result of implementing on top of App Engine and its Datastore.
   - A server that used database transactions and that used streaming servlet 3.0 functionality would have less trouble with concurrent requests.

Media held in memory
""""""""""""""""""""

When a form submission is uploaded, and when blank forms are downloaded, all the associated media files are held in memory at the same time, twice. For forms with a lot of media files, this can consume a lot of memory.

The previous section already suggested serializing form submission uploads. This is not absolutely critical for form downloads, but you should probably manage how many form download requests are being handled concurrently, in order to avoid memory problems.

..  Spinning up of copies of the frontend will incur faster quota usage on App Engine. For that reason, the Aggregate configuration here specifies a 14-second queuing time threshold before a new instance is spun up. Only if at least one request is queued for longer than 14 seconds will a new instance be spun up, and then that new instance will take about 30 seconds to become live. Leaving a 15-second processing interval. This is why ODK Collect tried twice before failing a submit.

Reducing Data Corruption and Boosting Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`Reducing Data Corruption and Boosting Performance on Google App Engine <aggregate-boost-performance>`.
