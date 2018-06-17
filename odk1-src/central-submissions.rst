.. _central-submissions-overview:

Managing Form Submissions in Central
====================================

Once you have :ref:`uploaded a form <central-forms-upload>` to ODK Central, :ref:`connected to it from your mobile device <central-users-app-configure>`, and :ref:`uploaded submissions <uploading-forms>` back to Central, you will see them appear in the Form submissions page in Central.

To find the Form submissions page, first find the form in the Form listings page (:menuselection:`--> Forms`) and click on it. You will be taken to the :ref:`Form Overview <central-forms-checklist>` page for that form. Click on the :menuselection:`--> Submissions` tab below the form name to find the submissions.

   .. image:: /img/central-submissions/listing.png

It is not yet possible to screen or delete submissions for quality, edit form data, or to see the form data itself. These features are planned for future releases. For now, you will need to pull your data out of Central before you can work with it. Right now, you can do this in one of two ways:

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

.. tip::

   This :file:`.zip` is similar to but not exactly the same as the ODK Briefcase output format. We will correct this in a release soon, so that your Briefcase-based tools will work with Central data.

.. _central-submissions-odata:

Connecting to submission data over OData
----------------------------------------

To connect a third-party tool to Central over OData, you will need a link to paste into the tool. You can find this link by clicking on the :guilabel:`Analyze via OData` button on the right side of the listing page:

   .. image:: /img/central-submissions/odata-button.png

Once you click on it, you should see this popup appear:

   .. image:: /img/central-submissions/odata.png

Because OData is a industry standard, only one link is necessary to make most tools work. However, because it is a relatively new technology, some tools need a little bit of customization to work correctly. If you are using such a tool, like Tableau, click on its tab to get the special link we provide for it. Otherwise, just copy the link and paste it into your tool.

For information on how to create an OData connection in Microsoft Excel, `click here <https://support.office.com/en-us/article/connect-to-an-odata-feed-power-query-4441a94d-9392-488a-a6a9-739b6d2ad500>`_. For instructions in Microsoft Power BI, `see this page <https://docs.microsoft.com/en-us/power-bi/desktop-connect-odata>`_. And for help with Tableau, make sure you have the appropriate tab selected before you copy the link, and click `here <https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_odata.html>`_ for more information.

When asked for login information, provide the email address and password you use to log into ODK Central. Make sure you trust the tool you are using before you do this.

