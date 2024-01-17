.. ODK documentation master file, created by
   sphinx-quickstart on Wed May 24 09:46:59 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ODK's Docs!
======================

:dfn:`ODK` is a data collection platform that helps researchers, field teams, and other professionals collect the data they need wherever it is. For a quick start, read :doc:`getting-started`.

In most cases, users of ODK:

- Create forms using the :doc:`XLSForm <xlsform>` standard in Excel or Google Sheets.
- :ref:`Upload forms <central-forms-upload>` to an :doc:`ODK Central server <central-intro>`.
- :ref:`Download forms <loading-forms-into-collect>` into the :doc:`ODK Collect app <collect-intro>` on an Android device.
- :doc:`Use Collect to fill out forms <collect-filling-forms>`.
- :ref:`Upload survey data <uploading-forms>` from Collect to Central.
- :doc:`Analyze or export data from Central <central-submissions>`.

While this is the most popular workflow, it is not the only way to do things because ODK is a very flexible platform. For example, instead of using the Collect app, you can use a browser to fill out :ref:`web forms <central-submissions-public-link>`. With ODK, you have complete control over your data collection.

ODK is open-source software that's made by a welcoming community of people just like you. To get involved, join the `community forum <https://forum.getodk.org/>`_ and, if you are a developer, contribute to our code on `GitHub <https://github.com/getodk>`_.

.. toctree::
  :maxdepth: 1
  :hidden:

  getting-started

.. toctree::
  :hidden:
  :maxdepth: 1
  :caption: Collect

  collect-intro
  collect-setup
  collect-using
  collect-best-practices

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Central

  central-intro
  central-install
  central-using
  central-manage

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Form Design

  form-design-intro
  XLSForm Tutorial <xlsform-first-form>
  Entities Tutorial <tutorial-community-reporting>
  form-reference
  form-best-practices

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Developers

  collect-api
  central-api
  pyODK <https://getodk.github.io/pyodk/>
  ODK XForms Spec <https://getodk.github.io/xforms-spec/>
  openrosa

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Reference

  security-privacy
  additional-resources
