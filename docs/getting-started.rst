Getting Started With ODK
=========================

This document walks you through the recommended workflow to get started with ODK.

.. note::
  Once you can do these steps, deepen your skills by :doc:`learning how to use ODK for different data collector workflows <data-collector-workflows>`.

.. _getting-started-install-central:

Get a Central server
--------------------

The easiest way to get a Central server is by using `ODK Cloud <https://getodk.org/#odk-cloud>`_.

ODK Cloud provides fast Central servers with regular feature updates, automatic security patches, daily backups, uptime management, enterprise security, and guaranteed support on any issues.

If you are technical and prefer to self-host, we recommend you :doc:`install Central on DigitalOcean <central-install-digital-ocean>`.

.. _getting-started-install-collect:

Get the Collect app
-------------------

The easiest way to get the Collect app is to download it from the `Google Play Store <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_.

You can also :ref:`install manually <install-collect-manually>` from an APK.


.. _getting-started-create-form:

Create a form with XLSForm and upload it to Central
------------------------------------------------------
#. Create a document in your favorite spreadsheet tool (Excel, Google Sheets, etc).
#. Design your form using :doc:`XLSForm <xlsform>` or try `a sample XLSForm <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0>`_.
#. :ref:`Upload the form to Central <central-forms-upload>`.

.. _getting-started-load-form:

Load a form into Collect from Central
----------------------------------------------------------

#. :ref:`Create an App User <central-users-app-overview>` in Central.
#. Open Collect on your Android device, tap :guilabel:`Configure with QR code` and scan the Client Configuration Code created for your App User.

.. _getting-started-fill-form:

Fill out a form and upload it to Central
-------------------------------------------

#. Select :guilabel:`Fill Blank Form` to complete a survey.
#. Select :guilabel:`Send Finalized Form` to upload your completed survey to Central.

Now log back into Central and see your completed survey results.
