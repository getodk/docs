.. _central-forms-overview:

Managing Forms in Central
=========================

Forms are at the heart of Open Data Kit. Once fetched onto a mobile device from ODK Central, they define the questions, validation, and logic to be presented during data collection. They also serve to organize the data coming back from mobile devices.

In ODK Central, there are four important steps to understand when managing a data collection project:

1. **Form design** is where you define the form itself, laying out many details like the questions and acceptable responses. ODK Central itself does not help with form design. Instead, please take a look at the many :doc:`available tools <form-tools>` and the :doc:`introduction to form design <form-design-intro>` for help creating your form.
2. **Form upload** is done after you have a working form design. Here you log into ODK Central and upload your new form so that Central knows that it exists. Once you do this, it will become available to any mobile device connected to the server for download and submission upload.
3. **Data extraction and analysis** can occur either at the end of the project, or continually as the project runs. Either way, ODK Central provides several different methods for extracting and analyzing your submission data. This is covered in the :doc:`Form Submissions <central-submissions>` article.
4. **Form lifecycle** tools let you manage the lifecycle of your data collection project: ongoing projects can be left alone to stay open, but many projects need a way to wrap things up. ODK Central provides tools to help control, for example, when workers using ODK Collect are allowed to download each form's definition, or separately to upload submissions to each form.

For more information about how to accomplish each of these tasks, please read on.

.. _central-forms-upload:

Uploading a form to ODK Central
-------------------------------

As mentioned, ODK Central does not feature a built-in form design utility. Please take a look at the many :doc:`available tools <form-tools>` and the :doc:`introduction to form design <form-design-intro>` for help creating your form.

Once you have an XForms :file:`.xml` file in hand, we strongly recommend that you first double check that it is valid using :doc:`ODK Validate <validate>`. Once you have confirmation that your form will work, the next step will be to upload it into ODK Central. To do this, log into the management website, and navigate to the Forms listing page by clicking on :menuselection:`--> Forms` at the top of the screen.

   .. image:: /img/central-forms/listing.png

From there, click on the :guilabel:`Create a new form` button on the right side of the screen, and you should see a popup appear:

   .. image:: /img/central-forms/new.png

You can either click on the :guilabel:`choose one` button to browse for your XForms :file:`.xml` file, or if you already have it handy somewhere, you can drag it over the gray box and drop it to select it. Either way, once you have chosen your file (you will see the name of your file at the bottom of the gray box when you do), you can click on the :guilabel:`Create` button immediately below to upload the form.

.. admonition:: Some errors you may see:

   - You may see a message that reads **A resource already exists with xmlFormId value(s) of xyz.** If you do, there already exists a form on this server with the same unique designation. If you are using XLSForm, try changing the name of the file. If you designed the form by hand, please check the ``id="…"`` attribute immediately inside the ``<instance>`` tag.
   - You may see a message that says **A form previously existed which had the same formId and version as the one you are attempting to create now. To prevent confusion, please change one or both and try creating the form again.** This means there once was a form on the server that has since been deleted that has exactly the same formId (see the previous bullet point) *and* version designation as the one you are now trying to upload. Central won't accept the new form, because this conflict could cause confusion with mobile devices that still have the old form sitting around. To upload this form, change either the formId (again, see the previous bullet point) or `update the version <https://opendatakit.github.io/xforms-spec/#primary-instance>`_ and try again.

Once the form is successfully uploaded, you will be taken to the Form Overview page.

.. _central-forms-checklist:

The Form Overview page
----------------------

Here, you can get a brief summary of the status of your form, and recommended next steps. You are automatically taken here when you upload a new form or click on the form name in the Form listing page. You can also get back here from other form-related pages by clicking the :menuselection:`--> Overview` tab below the name of the form.

   .. image:: /img/central-forms/checklist.png

The documentation on this page is a more detailed introductory explanation of form management in ODK Central, but the checklist you find on the Overview page is tailored to the current status of your form and your server and is a great place to look when you aren't sure what to do next.

In the future, look forward to seeing even more useful information at-a-glance on this page.

.. _central-forms-submissions:

Seeing Form Submissions
-----------------------

To see the current submissions uploaded to Central for a form, you can click on the :menuselection:`--> Submissions` tab below the name of the form. Here, you will see a summary table of all known submissions, and you will find multiple options for downloading and analyzing your submission data. This page and these options are covered in more detail in the :doc:`central-submissions` article.

.. _central-forms-lifecycle:

Managing Form Lifecycle
-----------------------

Forms can be in one of three lifecycle stages: **Open**, **Closing**, and **Closed**. All forms start in **Open** state when they are first created. You can see what each of these means below:

========= ================================ ===================================
  State    Available for download to apps   Accepts new submissions from apps
--------- -------------------------------- -----------------------------------
Open      **yes**                          **yes**
Closing   no                               **yes**
Closed    no                               no
========= ================================ ===================================

As you can see, you can use the **Closing** state to prevent further distribution of a form while still allowing the final few submissions to come in, while the **Closed** state effectively turns the form off completely. You can always set the form lifecycle stage to whatever you want: you can always, for example, re-open a closed form.

To set the form lifecycle stage, go to the Form Settings page by clicking on the :menuselection:`--> Settings` tab under the name of the form at the top of the page. Here, you will find the three possible stages on the left side. Clicking on one will immediately set the new stage: it is not necessary to click on any Save button.

   .. image:: /img/central-forms/settings.png

.. _central-forms-delete:

Deleting a Form
---------------

Do not delete a form until you are completely sure you never need a form or its submissions again. If you only want to turn the form off so that it doesn't appear to users of mobile data collection apps, we suggest using the :ref:`form lifecycle controls <central-forms-lifecycle>` explained above.

If you are certain you wish to delete a form, you can find the option on the Form Settings page: click on the :menuselection:`--> Settings` tab under the name of the form at the top of the page. On the right side of this page, you will find the :guilabel:`Delete this form` button.

