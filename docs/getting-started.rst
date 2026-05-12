Getting Started With ODK
=========================

ODK lets you build powerful forms to collect the data you need wherever it is. You can:

1. Build powerful forms that include photos, GPS locations, skip logic, calculations, external datasets, multiple languages, and more.

2. Collect data offline with either the mobile app or web forms. Forms and submissions are synced when an internet connection is available.

3. Use your data by downloading it as a CSV or connecting ODK to Excel, Power BI, Python, or R to create live-updating dashboards.

Researchers, field teams, and other professionals just like you use ODK to collect their important data. Here's how to get started.

.. _getting-started-get-central:

1. Get a server
---------------

There are two ways to get a Central server. You can use official managed hosting on ODK Cloud, or, if you are comfortable running Linux servers, you can self-host Central.

.. tabs::

  .. tab:: ODK Cloud (recommended)

     ODK Cloud is the official managed hosting service for ODK Central. It's the fastest and easiest way to get a Central server. Organizations choose it because it provides:

     * Fully managed hosting so your team can focus on data collection instead of servers.
     * Reliable and secure infrastructure operated by the team that builds ODK.
     * Fast, responsive support from ODK experts when you need help.

     Learn more about `ODK Cloud <https://getodk.org/#pricing>`_.


  .. tab:: Self-hosting

     If you know how to run Linux servers, you can host Central on your own infrastructure for free.
     
     And while Central itself is free, note that self-hosting requires ongoing infrastructure, maintenance, and security work. You'll also be responsible for all user-facing support.
     
     If you are comfortable with these responsibilities, get started with our :ref:`self-hosting Central <self-hosting>` guide.

2. Build your form
------------------

#. Follow the :doc:`XLSForm tutorial <tutorial-first-form>` and use the :ref:`XLSForm template <xlsform-template>` to learn how to build great forms.

#. :ref:`Upload your XLSForm to Central <central-forms-upload>` to test and publish it.

3. Collect your data
--------------------

.. _getting-started-get-collect:
.. _getting-started-connect:
.. _getting-started-fill-form:

If you are working with data collectors or enumerators in the field, you'll want to use our mobile app. If you are doing a self-report project, use web forms.

.. tabs::
   
  .. tab:: Field data collection (mobile app)

     #. :ref:`Create an App User <central-users-app-overview>` in Central and :ref:`assign your form to that user <central-projects-form-access>`.

     #. Ask data collectors to download the ODK Collect app from the `Google Play Store <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_.

     #. Share the App User QR code with your data collectors (e.g., print it, send by text).

     #. In Collect, data collectors will tap :guilabel:`Configure with QR code` and scan the App User QR code.

     #. Data collectors can then tap :guilabel:`Fill Blank Form` to fill out the form.

     #. Completed forms will be sent to Central when data collectors finish.

  .. tab:: Self-report (web forms)

     #. Create a :ref:`public access link <central-submissions-public-link>` to the form in Central.

     #. Share the link with participants (e.g., by email, text message, or social media).

     #. Completed forms will be sent to Central when your participants finish.

.. _getting-started-use-data:

4. Use your data
----------------

#. Log into Central and see your data in a table or map.

#. Download your data as a CSV or :ref:`visualize it in Power BI <central-submissions-odata>`.

.. _getting-started-help:

5. Need help?
-------------

If you need help, we recommend trying the Ask AI feature on the upper left corner of this page. It's a chat assistant that explains features, helps with form design, troubleshoots issues, and more.

You can also ask for help on our `community forum <https://forum.getodk.org/>`_. The forum has over 19,000 members who are happy to help you get the most out of ODK.