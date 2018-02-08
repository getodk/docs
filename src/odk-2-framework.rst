ODK 2.0 Framework
======================

.. _odk-2-framework:

The ODK 2.0 Tool Suite is a platform and exposes a variety of interfaces for you to build your data management applications on top of. For a description of these interfaces, as well as the inner working of how ODK processes this information and implements your application, read the `full description on our wiki <https://github.com/opendatakit/opendatakit/wiki/Tool-Suite-Javascript-framework-and-formDef.json-(Survey)-format>`_. The main points addressed in this document include:

  - Javascript Structure describes the form that ODK expects your data management applications to take and how ODK exposes functionality to them.

    - **Injected Interfaces** details the injected JavaScript interfaces that expose the APIs into the Android tools.
    - **Configuration File Structure** shows the full file structure and organization that ODK expects from your application.
    - **Internationalization** explains how the translation and internationalization system within ODK works and how to add locales to your application.
    - **ODK Tables** web pages describes how to format your HTML files and include the injected interfaces in your application.

  - **ODK Survey** form processing details how ODK Survey functions to create the form navigation experience

    - **ODK Survey Calling Contexts (ctxt)** explains how callbacks work in the Survey's control flow
    - **ODK Survey javascript modules** lists the javascript libraries and modules used by Survey and what they do
    - **ODK Survey control flow** overview gives an end to end description of control flow in ODK Survey
    - **ODK Survey controller actions (details)** lists the 10 actions available in a form defintion and what each does.
    - **ODK Survey formDef.json structure** is the dormDef.json specification

Full description is available on the `Github wiki <https://github.com/opendatakit/opendatakit/wiki/Tool-Suite-Javascript-framework-and-formDef.json-(Survey)-format>`_.
