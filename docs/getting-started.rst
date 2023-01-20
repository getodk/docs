Getting Started With ODK
=========================

ODK lets you build powerful offline forms to collect the data you need wherever it is. You can:

1. Build powerful forms that include photos, GPS locations, skip logic, calculations, external datasets, multiple languages, and more.

2. Collect data offline with either the mobile app or the web app. Forms and submissions are synced when an Internet connection is found.

3. Analyze with ease by downloading your data as a CSV or linking ODK to Excel, Power BI, Python, or R to create live-updating dashboards.

From research scientists to M&E professionals, millions of people like you use ODK to collect their important data. Here's how to get started.

.. _getting-started-get-central:

Get a Central server
--------------------

The fastest and easiest way to get a Central server is by using `ODK Cloud <https://getodk.org/#odk-cloud>`_. Cloud is official managed hosting of Central on ODK's fast, reliable, and secure infrastructure. Pricing starts at $169 USD/month.

If you are technical, you can also install ODK on your own infrastructure for free. Get started with our :ref:`self-hosting Central <self-hosting>` guide.

You can find details on the many ways to install Central and the various tradeoffs in :doc:`Installing Central <central-install>`.

.. _getting-started-get-collect:

Get the Collect app
-------------------

The best way to get the Collect app is to download it from the `Google Play Store <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_.

You can also :ref:`install manually <install-collect-manually>` from an APK.

.. _getting-started-create-form:

Upload your XLSForm to Central
------------------------------
#. Create a form definition using :doc:`XLSForm <xlsform>` or try `this sample XLSForm <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0>`_.
#. :ref:`Upload your XLSForm to Central <central-forms-upload>` and publish it.

.. _getting-started-connect:

Connect Collect to Central
--------------------------

#. :ref:`Create an App User <central-users-app-overview>` in Central and :ref:`assign your form to that user <central-projects-form-access>`.
#. Open Collect, tap :guilabel:`Configure with QR code` and scan the code created for your App User.

.. _getting-started-fill-form:

Fill your form in Collect
-------------------------

#. Select :guilabel:`Fill Blank Form` to fill out your form.
#. Your form data will be automatically sent to Central when you finish.

.. _getting-started-use-data:

Use your data in Central
------------------------

#. Log into Central and see your data.
#. Download your data as a CSV or :ref:`visualize it in Power BI <central-submissions-odata>`.
