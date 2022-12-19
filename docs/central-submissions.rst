.. _central-submissions-overview:

Managing Submissions in Central
===============================

The most common way to use ODK Central is in conjunction with a data collection client, typically on a mobile device, such as ODK Collect. To do this, you will need to :ref:`connect to it from your mobile device <central-users-app-configure>`, after which you will be able to :ref:`upload submissions <uploading-forms>` back to Central.

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

The table preview you see here will at first show you the first ten fields of your survey and their results, with the latest submissions shown closest to the top. Any downloadable files will appear with a green download link you can use to directly download that media attachment. The submission's instance ID will always be shown at the right side of this preview table.

If your form has more than ten fields, you can show more columns by accessing the :guilabel:`Columns shown` dropdown and checking the columns you wish to see. While the Columns shown pane is open, you can use the search box along its top to search for a particular column name if you have many.

In the :guilabel:`State and actions` column, you will see the current review state of each submission and the number of edits that have been made, if any. If a submission is missing expected media uploads, you will see a warning here. When you hover over a row (or **tab** to it with your keyboard) you will see controls in this column to edit the submission, or see more details about it. You can read more about :ref:`review states <central-submissions-review-states>` and the :ref:`submission detail page <central-submissions-details>` below.

You can limit the rows that appear by the submitter, the date, and the review status. These filter controls are available just above the submission table.

Any filter you apply to the submission table also applies to the download button. To work with your data, you can download it from Central. Right now, you can do this in one of two ways:

1. The **CSV Download** option will get you a :file:`.zip` file containing one or more :file:`.csv` tables, along with any multimedia submitted to the form. This is a good option if you already have custom tools you wish to use, or you want to import it into an offline analysis tool like SPSS or Stata.
2. The **OData connector** allows you connect a live representation of the data to OData-capable tools like Microsoft Excel, Microsoft Power BI, Tableau, SAP, and others. This option has some advantages: the data is transferred more richly to maintain more data format information, and the feed is always live, meaning any analysis or reports you perform in your tool over an OData connection can be easily refreshed as more submissions come in.

When the rows of the table have been filtered in any way, that filter also applies to the downloads. This makes it possible to download partial sections of your data at once.

Learn more about these options below:

.. _central-submissions-download:

Downloading submissions as CSVs
-------------------------------

To download all submission data as :file:`.csv` tables, click on the :guilabel:`Download all # records` button on the right side of the listing page:

   .. image:: /img/central-submissions/download-button.png

If you have any row filters applied to the submission table, those filters will be applied to your download as well. You can use this to, for example, download only submissions from a particular month, or only approved submissions.

Once the download dialog opens, you'll be given some additional export options.

   .. image:: /img/central-submissions/download-modal.png

Some of the options may be disabled if they do not apply to your data, or if they are not available due to features that you have enabled (such as managed encryption).

 - The option to split :guilabel:`select multiple` choices will create a new column in the export :file:`csv` for each unique known value in each select multiple field. These columns then indicate whether each submission checked each option.
 - The remove group names option takes out the prefix usually added to groups in the header: so for example, :code:`meta-instanceID` would become just :code:`instanceID`.
 - Finally, the option to include previously deleted fields will include every known previously deleted field in any version of the Form in the export, along with any data found for those fields.

Click on one of the format options on the right to start the download.

Once the :file:`.csv` or :file:`.zip` completes downloading, you will find one or more files when you extract it:

 - A root table :file:`.csv` named after your Form title.
 - Join table :file:`.csv` files representing any repeats you may have in your form, with join columns on the left of each table relating each row to its counterpart in the parent table. Each join table is named to reflect its relationship with the others. If there is only one :file:`.csv` file, then your form has no repeats.
 - A folder named :file:`files` which contains subfolders, each named after an ``instanceId`` of a submission. Each subfolder then contains a set of file attachments relating to that submission. If no :file:`files` folder exists, then no multimedia attachments have been submitted to this form.
 - If you have enabled :doc:`Client Audit Logging <form-audit-log>` on your form, and log events have been submitted to the server, then you will find a file that ends with :file:`- audit.csv`. This file combines all the logging data from all submissions to the form into a single table.

.. tip::

  Excel will not import CSVs with Unicode characters like ã, ß, and 箸 correctly if you double-click the file or open it from the File menu. You must use the `Text Import Wizard <https://support.microsoft.com/en-us/office/text-import-wizard-c5b02af6-fda1-4440-899f-f78bafe41857>`_ and specify a file origin of Unicode (UTF-8, 65001) and the comma delimiter.

  Rather than downloading CSVs manually, you can also :ref:`connect Excel directly to Central via OData <central-submissions-odata>` and get a live-updating spreadsheet with auto-detected data types and Unicode support.

.. _central-submissions-odata:
.. _connecting-to-submission-data-over-odata:

Downloading submissions with Power BI or Excel
----------------------------------------------

Central provides an OData feed that Power BI or Excel can use to pull data into ODK at (pretty much) the click of a button.

..  youtube:: CDycTI-8TOc
   :width: 100%

As shown in the tutorial video above from `Humanitarian Data Solutions <https://www.humanitariandatasolutions.com>`_, you will first need a link to paste into the tool. You can find this link by clicking on the :guilabel:`Analyze via OData` button on the right side of the listing page:

   .. image:: /img/central-submissions/odata-button.png

Once you click on it, you should see this popup appear:

   .. image:: /img/central-submissions/odata.png

To connect with Excel or Power BI, follow these steps.

1. Start the Get OData feed action.

  * In Excel, select the :guilabel:`Data` menu, then :guilabel:`Get Data`, :guilabel:`From Other Sources`, then :guilabel:`From OData Feed`.

  * In Power BI, select the :guilabel:`Home` menu, then :guilabel:`Get Data`, then :guilabel:`OData feed`.

2. Leave the feed type as :guilabel:`Basic` (not Advanced), then copy and paste in the link from Central and then select :guilabel:`OK`.

   .. image:: /img/central-submissions/powerbi-url.png

3. Change the authentication type to :guilabel:`Basic` (not Anonymous), enter your Central email address and password, and then :guilabel:`Connect`.

   .. image:: /img/central-submissions/powerbi-auth.png

4. The :guilabel:`Navigator` window now appear. Select :guilabel:`Submissions`, then :guilabel:`Load`.

.. tip::
  See `Import external data into Excel <https://support.office.com/en-us/article/connect-to-an-odata-feed-power-query-4441a94d-9392-488a-a6a9-739b6d2ad500>`_ and `OData feeds in Power BI <https://docs.microsoft.com/en-us/power-bi/desktop-connect-odata>`_ for more information about using Power BI or Excel for OData feeds.

  If you are having trouble getting Power BI or Excel to connect, and especially if you see error messages about permissions or authentication, `clear your cached permissions <https://docs.microsoft.com/en-us/power-query/connectorauthentication#change-the-authentication-method>`_ and try again.

  If you are using Excel 2016, install `Microsoft Power Query for Excel 6 <https://www.microsoft.com/en-us/download/details.aspx?id=39379>`_ and go to the :guilabel:`Data` menu, then :guilabel:`New Query`, and then :guilabel:`From Other Sources` to find the :guilabel:`From OData Feed` item.

Downloading submissions with Python, R, and more
------------------------------------------------
If you use `Python <https://www.python.org/>`_, we recommend `pyODK <https://github.com/getodk/pyodk>`_ for downloading submissions via an OData feed into Python. pyODK is the official Python client for Central and it makes common data analysis and workflow automation tasks simple. Get started with `pyODK's docs <https://github.com/getodk/pyodk>`_.

If you use `R <https://www.r-project.org/>`_, we recommend `ruODK <https://docs.ropensci.org/ruODK/>`_ for downloading submissions via an OData feed into R. ruODK is open-source software developed by ODK community members. Get started with `ruODK's docs <https://docs.ropensci.org/ruODK/articles/odata-api.html>`_.

You can also access the OData feed yourself. The OData feed is an easily consumable JSON data format and offers a metadata schema, some filtering and paging options, and more. To learn more about the OData feed, click the :guilabel:`API Access` button or see the `API documentation <https://odkcentral.docs.apiary.io/#reference/odata-endpoints>`_ directly.

.. _central-submissions-media-downloads:
.. _setting-up-media-downloads:

Accessing submission media from external tools
----------------------------------------------

It can be tricky to access submission media files while using external tools like Power BI or Python for data analysis or visualization. Using an external tool to fetch submissions from Central does not mean it can or knows how to get associated images, video, and other media.

In the OData feed, you will see media files given by their filename. If you want, you can construct a link within your analysis tool that will download any media file with your web browser. You can do this by gluing together pieces of text into a URL. Often this gluing operation is called ``concat`` or ``concatenate``. You'll need to make it look like this:

  .. code-block:: console

    https://DOMAIN/#/dl/projects/PROJECTID/forms/FORMID/submissions/INSTANCEID/attachments/FILENAME

Where the uppercase words need to be replaced with the appropriate values. The easiest way to get the ``DOMAIN``, ``PROJECTID``, and ``FORMID`` is to open the Form in your web browser in the Central administration website and just copy the values you see there. The two web addresses are quite similar. Then you have to add the ``INSTANCEID`` and the ``FILENAME``, both of which you can find in the OData data itself.

Here is an example of a completed address:

  .. code-block:: console

    https://my.odk.server/#/dl/projects/1/forms/forest_survey/submissions/uuid:20bcee82-4a22-4381-a6aa-f926fc85fb22/attachments/my.file.mp3

This location is a web page that causes a web browser to download a file. It cannot be used directly to embed images or video on any website or application.

.. _central-submissions-review-states:

Submission Review States
------------------------

As of version 1.2, Central allows Project Managers and Administrators to review submissions and assign them certain states. This feature lets you perform verification and follow-up data editing within Central itself, if you need this kind of a workflow. The available states are:

+------------+-------------+-----------------------------------------------------------------------------------+
| State      | Assigned by | Description                                                                       |
+============+=============+===================================================================================+
| Received   | System      | The default state for all incoming submissions, assigned automatically by Central |
+------------+-------------+-----------------------------------------------------------------------------------+
| Edited     | System      | Automatically assigned by Central whenever a submission is edited by any user     |
+------------+-------------+-----------------------------------------------------------------------------------+
| Has Issues | User        | Can be assigned by project staff if a submission has problems                     |
+------------+-------------+-----------------------------------------------------------------------------------+
| Approved   | User        | Can be assigned by project staff to approve a submission                          |
+------------+-------------+-----------------------------------------------------------------------------------+
| Rejected   | User        | Can be assigned by project staff to reject a submission                           |
+------------+-------------+-----------------------------------------------------------------------------------+

The ``Received`` and ``Edited`` states are automatically set by Central any time a submission is uploaded or edited. The other states are assigned by project staff. We suggest some meanings for these states above, but they don't cause anything to happen automatically. For example, rejected submissions will still be included in your data exports unless you filter them out yourself. So, you are free to use these states however you'd like.

Once submissions have been reviewed, the submission table download and the OData connection both allow submissions to be filtered by review state. This lets you, for example, download only all the approved submissions.

.. _central-submissions-details:

Submission Details
------------------

As of version 1.2, each submission has its own detail page which provides basic information about the submission, an activity history of action and discussion on that submission, and tools for updating the submission review state and data itself.

   .. image:: /img/central-submissions/details.png

The title at the top is pulled from the ``instance_name`` if there is one, otherwise it will be the automatically assigned ``instanceID``. We recommend you :ref:`define an instance_name <instance-name>` based on the data in each submission. This is especially important if you plan on using this page a lot, because it makes navigation much easier to have friendly names at the top of the page and in the web browser title and tab.


Basic detail can be found along the left. If there are expected media attachments for this submission, that status information will be provided.

The main activity feed on the right shows you the discussion and action history of the submission. Any review state changes, comments, and edits will appear here. At the top of the activity feed, you can :guilabel:`Review` a submission to assign a new review state, :guilabel:`Edit` the submission directly in your web browser, or type in the box to begin leaving a comment.

You can leave a note when you update the review state, to indicate why the decision is being made, or any other information you'd like saved.

.. _central-submissions-editing:

Submission Editing
------------------

From the :ref:`submission detail page <central-submissions-details>` you can press the :guilabel:`Edit` button to edit the submission in your web browser. When an edited submission is resubmitted, a new version of it is created, just like a form version. You will be able to see previous submission versions in a future version of Central.

Any time a user edits a submission, they will see a note when they are returned to the detail page suggesting that they leave a comment describing the edits they have made. This is optional but highly encouraged. In a future version of Central, greater detail will be automatically provided about the data values that were changed.

Finally, when edits are submitted, the submission :ref:`review state <central-submissions-review-states>` will automatically be set to :guilabel:`Edited`, and (as of version 1.3) you will see the changes between versions in the Submission Detail activity feed. Please note that Central will show you the differences between versions, but it doesn't know the exact actions you took to cause those changes. Sometimes the differences shown are not the same as the actions taken, but the resulting data will appear exactly as edited.

   .. image:: /img/central-submissions/diff.png

