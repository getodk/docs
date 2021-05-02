.. _central-intro:

ODK Central
===========

:dfn:`ODK Central` is the ODK server. It manages user accounts and permissions, stores form definitions, and allows data collection clients like :doc:`ODK Collect <collect-intro>` to connect to it for form download and submission upload.

Our goal with Central is to create a server that is straightforward to install, easy to use and extensible with new features and functionality both directly in the software and with the use of our REST, OpenRosa, and OData programmatic APIs.

.. _central-intro-features:

ODK Central Features
--------------------

Here are some of the major features we support today:

 - Projects to organize users, permissions, and forms
 - Form upload and management
 - User accounts with role-based permissioning

   - With support for form version updates
   - With drafts and testing on initial creation, and on version updates
   - With form multimedia or data attachments
   - Encrypted forms (self-supplied or project managed keys)

 - Submission upload and management

   - From filling from our mobile app or a web browser
   - From permissions-managed known users or anonymous public links
   - With submission multimedia or data attachments
   - With an interactive table preview of submission data
   - Support for reviewing, commenting on, and editing submissions after upload
   - Connectable to data analysis and dashboard applications like Excel, Power BI, or R over OData

 - Integrated checklist-based help system
 - Optional encrypted off-site data backups to Google Drive
 - Clean and modern REST API for integration and extensibility
 - High performance on low-cost hardware or cloud providers
 - ODK Briefcase-compatible data output
 - ODK Briefcase push/pull support

Central is in active development. We have a lot of exciting ideas for its future and we look forward to hearing yours as well. See `What is coming in Central <https://forum.getodk.org/t/whats-coming-in-central-over-the-next-few-years/19677>`_ for more on future direction.

.. _central-intro-who:

Who should use ODK Central?
---------------------------

We recommend that all new data collection projects use ODK Central because it is in active development by the core ODK team. ODK Central is a relatively new server. It replaces :doc:`aggregate-intro` which is no longer being updated. Central isn't as widely deployed as Aggregate, but its developers have put it through stress testing and it is used in production by many projects including several large ones.

Central solves some of the biggest problems with Aggregate. Some of our favorite features are:

- :doc:`projects <central-projects>` let you partition your server into different sandboxes to support multiple independent teams
- :ref:`direct upload of XLSForm files <central-forms-upload>` makes form management easier
- :ref:`the OData API <central-submissions-odata>` makes it easy to synchronize your live form data to desktop visualization and dashboard tools
- :doc:`managed encryption <central-encryption>` makes the process of handling encrypted form data significantly easier and in many cases more secure


Please give Central a try and provide your `feedback <https://forum.getodk.org/c/support>`_.

.. _central-performance:

Notes On Performance
--------------------

Central was designed from early on to be stable, predictable, and fast on limited hardware.

Perhaps most importantly, even under extreme traffic Central is guaranteed to either wholly succeed or wholly fail each submission. If, for instance, one submission attachment fails to upload or persist, the entire submission upload will fail and Collect will attempt the submission again. If Central reports that a submission was successfully uploaded, then all submitted data was successfully saved.

We have done some work to benchmark Central to verify these claims, and produce some guideline numbers. Every circumstance is different, and a lot will depend on your form design, your geographic location, and other factors. But in general, on the second-cheapest DigitalOcean configuration at time of writing ($10/month, 2GB memory), we found the following:

 - A 250 question form without attachments could support 500 devices simultaneously uploading many submissions without issues, at a rate of roughly 41.2 submissions per second.
 - A larger 5000 question form, without attachments, could also support 500 devices submitting data at once, but runs more slowly (~12 submissions/second) and fails about one submission in every 1000 (which can then be re-submitted without issues).
 - Including attachments slows the process down, since there is more data to shuffle around. Realistically, the number of concurrent users supported in this scenario will decrease simply because Internet bandwidth in and out of Central will limit the number of submissions it can see at a time. But we have tried situations featuring 5MB submissions with 50 devices at once without seeing issues (though for the mentioned reasons the response rate drops to between 1 and 2 submissions/second). Additionally, data exports with attachments take longer and are more memory-intensive.

 When you are planning for your installation and selecting a destination to deploy Central to, keep these numbers in mind. If 500 people submitting data *all at the same time* is a distant scenario, you can probably get by with a lower-performance option. If your deployment is larger than these numbers, consider bumping up to a more powerful machine. If you aren't sure, ask around in the forums.

.. _central-intro-learn-more:

Learn more about ODK Central
----------------------------

 - :doc:`central-setup`
 - :doc:`central-using`

