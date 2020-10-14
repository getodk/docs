.. _central-submissions-overview:

Managing Form Submissions in Central
====================================

The most common way to use ODK Central is in conjunction with a data collection client, typically on a mobile device, such as ODK Collect. To do this, you will need to :ref:`connect to it from your mobile device <central-users-app-configure>`, after which you will be able to 
:ref:`uploaded submissions <uploading-forms>` back to Central.

ODK Central also bundles `Enketo <https://enketo.org>`_, which enables preview and submission of forms directly from a web browser. Please note that as with all ODK clients, Enketo does not always behave quite the same as Collect, or support the same features. Any authorized Web User may fill out a Form directly from the browser, as will be described in more detail below.

Finally, ODK Central offers Public Access Links. A Public Access Link grants anybody in possession of the link the ability to submit to a Form on your server. You can control whether each respondent can submit more than once, and revoke access from any Link at any time.

Submissions sent to Central are available to browse in a preview table, to connect directly to data analysis tools, and for download.

.. _central-submissions-direct:

Direct Web Browser Submissions
------------------------------

Web Users who are Administrators, Project Managers, or Data Collectors can directly fill Forms in the web browser from the Central administration website. This functionality is provided by Enketo, which does not always behave quite the same as Collect, or support the same features.

   .. image:: /img/central-submissions/new.png

Administrators and Project Managers can begin a survey by going to the :guilabel:`Submissions` tab of the Form, and clicking on the :guilabel:`New` button next to the Submissions header. This will open a new tab which will load the Form in Enketo.

   .. image:: /img/central-submissions/data-collector-form-listing.png

Data Collectors do not have access to the detailed Form management pages. Instead, they will find a :guilabel:`Fill Form` button next to the Form name in the list of Forms on the Project Overview page.

.. _central-submissions-public-link:

Public Access Links
-------------------

ODK Central allows the distribution of surveys to a broad or open respondent group using Public Access Links. These Links take recipients directly to the Form in their web browser, administered by Enketo.

To create a Public Access Link, go to the Form's :guilabel:`Public Access` tab. Click on :guilabel:`Create Public Access Link…` to begin.

   .. image:: /img/central-submissions/public-link-new.png

In the window that appears, you'll need to name the Link. This name is for your own identification purposes in the administration website, and is not displayed to respondents.

You'll also need to decide whether to allow multiple submissions per respondent. Normally, respondents filling a Form through a Public Link will be redirected to a thank you page after sending a Submission. Pressing the back button will not bring them back to the Form but they could send in another Submission by visiting the Link again. Checking the :guilabel:`Single Submission` checkbox enables basic protection against more than one Submission being made from the same browser.

.. admonition:: Single submission enforcement

  In Enketo, the enforcement limiting each respondent to a single response is done with in-browser tracking. This means that a user could submit multiple times using different devices or browsers, or distribute the link beyond the intended group.

  Also because of this tracking method, respondents will only be able to respond once *per Form*, not once per single-submission Link. Future versions of Central may change how this works. Please leave `feedback on the community forum <https://forum.getodk.org/c/features/9>`_ if this is something you'd like to see.

Once a Link is created, it will appear in the table, along with a web address you can copy and paste to distribute the Link to respondents.

   .. image:: /img/central-submissions/public-link-listing.png

You cannot yet edit any of the details of a Public Link. This will come in a future version of Central.

.. _central-submissions-link-revoke:

Revoking a Link
~~~~~~~~~~~~~~~

You can revoke a Link at any time to prevent any further Submissions through it. Once a Link is revoked, all Submissions will be immediately denied, and new attempts to load the Form using the Link will result in an error instead.

To revoke a Link, click on the :guilabel:`Revoke` button in the Link's row in the table. You will be asked to confirm the action. Once a Link is revoked, there is no way to restore it.

.. _central-submissions-accessing:

Accessing Submissions
---------------------

To find the Form submissions page, first find the form in the Form listings page (:menuselection:`--> Forms`) and click on it. You will be taken to the :ref:`Form Overview <central-forms-checklist>` page for that form. Click on the :menuselection:`--> Submissions` tab below the form name to find the submissions.

   .. image:: /img/central-submissions/listing.png

The table preview you see here will show you the first ten fields of your survey and their results, with the latest submissions shown closest to the top. Any downloadable files will appear with a green download link you can use to directly download that media attachment. The submission's instance ID will always be shown at the right side of this preview table.

It is not yet possible to screen or delete submissions for quality or edit submission data. These features are planned for future releases. For now, you will need to pull your data out of Central before you can work with it. Right now, you can do this in one of two ways:

1. The **CSV Download** option will get you a :file:`.zip` file containing one or more :file:`.csv` tables, along with any multimedia submitted to the form. This is a good option if you already have custom tools you wish to use, or you want to import it into an offline analysis tool like SPSS or Stata.
2. The **OData connector** allows you connect a live representation of the data to OData-capable tools like Microsoft Excel, Microsoft Power BI, Tableau, SAP, and others. This option has some advantages: the data is transferred more richly to maintain more data format information, and the feed is always live, meaning any analysis or reports you perform in your tool over an OData connection can be easily refreshed as more submissions come in.

Learn more about these options below:

.. _central-submissions-download:

Downloading submissions as CSVs
-------------------------------

To download all submission data as a :file:`.zip` of :file:`.csv` tables, click on the :guilabel:`Download all # records` button on the right side of the listing page:

   .. image:: /img/central-submissions/download-button.png

Once it completes downloading, you will find one or more files when you extract it:

 - A root table :file:`.csv` named after your Form title.
 - Join table :file:`.csv` files representing any repeats you may have in your form, with join columns on the left of each table relating each row to its counterpart in the parent table. Each join table is named to reflect its relationship with the others. If there is only one :file:`.csv` file, then your form has no repeats.
 - A folder named :file:`files` which contains subfolders, each named after an ``instanceId`` of a submission. Each subfolder then contains a set of file attachments relating to that submission. If no :file:`files` folder exists, then no multimedia attachments have been submitted to this form.
 - If you have enabled :doc:`Client Audit Logging <form-audit-log>` on your form, and log events have been submitted to the server, then you will find a file that ends with :file:`- audit.csv`. This file combines all the logging data from all submissions to the form into a single table.

.. _central-submissions-odata:

Connecting to submission data over OData
----------------------------------------

To connect a third-party tool to Central over OData, you will need a link to paste into the tool. You can find this link by clicking on the :guilabel:`Analyze via OData` button on the right side of the listing page:

   .. image:: /img/central-submissions/odata-button.png

Once you click on it, you should see this popup appear:

   .. image:: /img/central-submissions/odata.png

Because OData is a industry standard, only one link is necessary to make most tools work. However, because it is a relatively new technology, some tools need a little bit of customization to work correctly. If you are using such a tool, like Power BI, click on its tab to get the special link we provide for it. Otherwise, copy the link as-is and paste it into your tool.

For information on how to create an OData connection in Microsoft Excel, `click here <https://support.office.com/en-us/article/connect-to-an-odata-feed-power-query-4441a94d-9392-488a-a6a9-739b6d2ad500>`_. For instructions in Microsoft Power BI, `see this page <https://docs.microsoft.com/en-us/power-bi/desktop-connect-odata>`_.

If you want to use the free and popular `R statistics and analysis tool <https://www.r-project.org/>`_, we recommend you use `ruODK <https://docs.ropensci.org/ruODK/>`_. A guide for getting started with it can be found `here <https://docs.ropensci.org/ruODK/articles/odata-api.html>`_. Just like ODK itself, ruODK is developed and supported by community members. If you wish to help improve it, you can find information `on GitHub <https://docs.ropensci.org/ruODK/CONTRIBUTING.html>`_.

When asked for login information, provide the email address and password you use to log into ODK Central. Make sure you trust the tool you are using before you do this.

