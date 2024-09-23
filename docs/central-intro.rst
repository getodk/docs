.. _central-intro:

ODK Central
===========

.. tip::
  `ODK Cloud <https://getodk.org/#pricing>`_ is the best way to use ODK. With ODK Cloud, you can be collecting the data you need a few minutes after you subscribe. No technical skills required. `Get started today <https://getodk.org/#pricing>`_.

:dfn:`ODK Central` is the ODK server. It manages user accounts and permissions, forms and submissions, longitudinal data records, and allows data collection clients like :doc:`ODK Collect <collect-intro>` to connect to it for form download and submission upload.

Our goal with Central is to create a server that is straightforward to install, easy to use, and extensible with new features and functionality both directly in the software and with the use of our REST, OpenRosa, and OData programmatic APIs.

.. _central-intro-features:

ODK Central Features
--------------------

Here are some of the major features we support today:

 - Projects to organize users, permissions, and forms
 - User accounts with role-based permissioning
 - Form upload and management

   - With support for form version updates
   - With drafts and testing on initial creation, and on version updates
   - With form multimedia or data attachments
   - Encrypted forms (self-supplied or project managed keys)
   - Upload XLSForms directly
   - True deletion of forms
 - Submission upload and management

   - Form filling from our mobile app or a web browser
   - From permissions-managed known users or anonymous public links
   - With submission multimedia or data attachments
   - With an interactive table preview of submission data
   - Support for reviewing, commenting on, and editing submissions after upload
   - Connectable to analysis and dashboard applications like Excel, Power BI, or R over OData
   - Entities for registration/follow-up workflows
 - Entity system for longitudinal data management

   - Persist and share data across Form instances
   - Update long-lived records with new information
   - Reference information from these records from Forms during data collection
   - Conflict management system when parallel updates run into each other
   - Bulk upload of existing data
 - Clean and modern REST API for integration and extensibility
 - High performance on low-cost hardware or cloud providers
 - ODK Briefcase-compatible data output
 - ODK Briefcase push/pull support

Central is in active development. We have a lot of exciting ideas for its future and we look forward to hearing yours as well. See `our roadmap <https://roadmap.getodk.org>`_ for more on future direction.

.. _central-intro-overview:

ODK Central Overview
--------------------

Once you have :ref:`installed Central <central-install>`, you may be wondering where to start.

In Central, everything begins with the :ref:`Project <central-projects>`. Projects organize a Central server into individual little worlds, allowing many separate data collection projects and teams to live on the same server.

Within a Project can live many :doc:`Forms <central-forms>`. Once you :doc:`author a Form <form-design-intro>` you can upload it to Central, where you can test and preview the Form before publishing it. When it comes time to make changes to a published Form, there is a :ref:`Form Draft <central-forms-updates>` process that helps you update and test the Form safely while important data is still being collected.

When a Form is filled out either :ref:`directly on the web in Central <central-submissions-direct>` (using Enketo) or from a mobile client such as :doc:`Collect <collect-intro>`, the finalized data will become a :doc:`Submission <central-submissions>` in Central. Central has features to allow :ref:`review and approval/rejection <central-submissions-review-states>`, :ref:`comments <central-submissions-details>`, and :ref:`edits <central-submissions-editing>` on Submissions. You can also :ref:`bulk download <central-submissions-download>` your data as a file, :ref:`connect to a live feed <central-submissions-odata>` of your data through analysis apps like Power BI or Excel, or use the :ref:`OData API <central-submissions-other-api>` directly to access data.

Additionally, Submissions can also create or update :doc:`Entities <central-entities>`. An Entity is a lasting data record: a patient, this tree, that school, and so on. Forms in Central can be configured to :ref:`create <central-entities-registration-forms>` or :ref:`update <central-entities-update>` an Entity with new information when a Submission is uploaded. This updated Entity data is then sent back out to any data collection clients and can then be :ref:`referenced in future Forms <central-entities-follow-up-forms>`. This allows you to definitively relate repeated encounters with the same Entity together without any homework or guesswork, and it allows you to contextualize and customize the Form filling process using the latest information about a known Entity. In case multiple people try to update an Entity at the same time, there is a :ref:`conflict management system <central-entities-update-conflicts>`. Just like Forms and Submissions, Entities live inside of Projects.

Of course, you will need to set up people in the system to do all this work. Right now in Central, :doc:`Users <central-users>` are divided into two main categories:

- :ref:`Web Users <central-users-web-overview>` who log directly into the Central website, and can be granted permission to:

  - Administrate the entire Central server
  - Manage a particular Project
  - Fill out Forms within a particular Project
  - View collected data within a particular Project
- :ref:`App Users <central-users-app-overview>` who connect to Central from a mobile device running Collect, and can submit data to a controlled set of available Forms. Unlike Web Users which exist across the whole server, App Users are limited to the Project they are created within.

And before you get too far, you might want to think about :ref:`setting up backups <central-backup>` of your data. However, if you're on ODK Cloud you never have to worry about this!

.. _central-intro-learn-more:

Learn more about ODK Central
----------------------------

 - :doc:`central-install`
 - :doc:`central-using`
 - :doc:`central-manage`

