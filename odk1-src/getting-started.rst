Getting Started With ODK
=========================

This document walks you through the recommended workflow to get started with ODK.

You will:

.. contents::
 :local:

.. _getting-started-install-collect:

Install Collect
---------------------

The easiest way to install the Collect app is `to get it from the Google Play store <https://play.google.com/store/apps/details?id=org.odk.collect.android&hl=en>`_.

.. seealso:: :doc:`collect-install`

.. _getting-started-install-central:

Install Central
----------------

The easiest way to set up your own Central server is to :doc:`install it on DigitalOcean <central-install-digital-ocean>`, a cloud provider.

If you want to try Central out, you can :ref:`request access to the sandbox <central-install-sandbox>`.

.. warning::

  The Central sandbox server is for evaluation purposes only. All forms and data on this server are public and may be deleted without notice.
  
.. seealso:: :doc:`central-install`

.. _getting-started-create-form:

Create a form with XLSForm and upload it to Central
------------------------------------------------------
#. Create a document in your favorite spreadsheet tool (Excel, Google Sheets, etc)
#. Design your form using :doc:`XLSForm <xlsform>` or try `a sample XLSForm <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0>`_.
#. :ref:`Upload the form to Central <central-forms-upload>`.
    
.. _getting-started-load-form:

Load a form into Collect from Central
----------------------------------------------------------

#. :ref:`Find or create an App User <central-users-app-overview>` in Central
#. Open Collect on your Android device
#. Tap :guilabel:`Configure via QR code` from the menu at the top right
   (:menuselection:`⋮ --> Configure via QR code`)
#. Scan the QR code from Central
#. Go back to the app home screen and select :guilabel:`Get Blank Form`, then select your form.

.. _getting-started-fill-form:

Fill out a form and upload it to Central
-------------------------------------------

#. Select :guilabel:`Fill Blank Form` to complete a survey.
#. Select :guilabel:`Send Finalized Form` to upload your completed survey to Central.

Now log back into Central and see your completed survey results.
