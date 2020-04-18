.. _central-intro:

ODK Central
===========

:dfn:`ODK Central` is an ODK server alternative that is early in its development. Like ODK Aggregate, it manages user accounts and permissions, stores form definitions, and allows data collection clients like ODK Collect to connect to it for form download and submission upload.

Our goal with Central is to create a modern sibling to Aggregate that is easier to install, easier to use, and more extensible with new features and functionality both directly in the software and with the use of our REST, OpenRosa, and OData programmatic APIs.

.. _central-intro-features:

ODK Central Features
--------------------

We have a lot of exciting ideas for the future of Central, and we look forward to hearing yours as well. Here are the features we already support today:

 - User accounts and management
 - Role-based user permissioning
 - Projects to organize users, permissions, and forms
 - Form and submission upload and management

   - With form and submission multimedia or data attachments
   - With a table preview of submission data
   - Encrypted forms (self-supplied or project managed keys)
   - OData live data feed for analysis with tools like Excel and Power BI

 - Integrated checklist-based help system
 - Automatic, encrypted off-site data backups to Google Drive
 - Clean and modern REST API for integration and extensibility
 - High performance on low-cost hardware or cloud providers
 - ODK Briefcase-compatible data output
 - ODK Briefcase push/pull support

Here are some (but not all) key features we **do not yet** support:

 - Customizable user roles

See `What is coming in Central <https://forum.getodk.org/t/whats-coming-in-central-over-the-next-few-years/19677>`_ for more on future features.

.. _central-intro-who:

Who should use ODK Central?
---------------------------

Central is much younger than Aggregate. Because of this, it isn't as heavily battle-tested, and you might come across quirks and problems while using it. Among other things, it can be a little tricky to install. But the issues people have run into have been minor so far.

Additionally, Central does not support every feature that Aggregate does. There are some Aggregate features that we do not intend to ever support in Central, especially around data preview and visualization. You can find a list of these differences and some of the planned improvements to Central `here <https://forum.getodk.org/t/whats-coming-in-central-over-the-next-few-years/19677>`_.

On the other hand, Central supports some things that Aggregate does not. Projects let you partition your server into different sandboxes to support multiple independent teams. Managed encryption makes the process of handling encrypted form data significantly easier and in many cases more securely. Central allows direct upload of XLSForm files. It also offers an OData API to easily synchronize your live form data to desktop visualization and dashboard tools.

If you are an adventurous user who is comfortable with (new) technology, you are happy with the supported features, and you are okay with the risks with using early release software, please consider giving Central a try and giving us your `feedback <https://forum.getodk.org/c/features>`_.

If you finished reading all the above and you're not feeling too sure about it, we suggest sitting it out for a little while longer. Keep watching the `release announcements board <https://forum.getodk.org/c/releases>`_ for future updates, and we'll be sure to sound the bells when we're sure things are ready for a broader audience.

.. _central-performance:

Notes On Performance
--------------------

Central was designed from early on to be stable, predictable, and fast on limited hardware.

Perhaps most importantly, even under extreme traffic Central is guaranteed to either wholly succeed or wholly fail each submission. If, for instance, one submission attachment fails to upload or persist, the entire submission upload will fail and Collect will attempt the submission again. If Central reports that a submission was successfully uploaded, then all submitted data was successfully saved.

We have done some work to benchmark Central to verify these claims, and produce some guideline numbers. Every circumstance is different, and a lot will depend on your form design, your geographic location, and other factors. But in general, on the second-cheapest DigitalOcean configuration at time of writing ($10/month, 2GB memory), we found the following:

 - A 250 question form without attachments could support 500 devices simultaneously uploading many submissions without issues, at a rate of roughly 41.2 submissions per second.
 - A larger 5000 question form, without attachments, could also support 500 devices submitting data at once, but runs more slowly (~12 submissions/second) and fails about one submission in every 1000 (which can then be re-submitted without issues).
 - Including attachments slows the process down, since there is more data to shuffle around. Realistically, the number of concurrent users supported in this scenario will decrease simply because Internet bandwidth in and out of Central will limit the number of submissions it can see at a time. But we have tried situations featuring 5MB submissions with 50 devices at once without seeing issues (though for the mentioned reasons the response rate drops to between 1 and 2 submissions/second).

 When you are planning for your installation and selecting a destination to deploy Central to, keep these numbers in mind. If 500 people submitting data *all at the same time* is a laughably distant scenario, you can probably get by with an even cheaper option. If your deployment is larger than these numbers, consider bumping up to a more powerful machine. If you aren't sure, ask around in the forums.

.. _central-intro-learn-more:

Learn more about ODK Central
----------------------------

 - :doc:`central-setup`
 - :doc:`central-using`

