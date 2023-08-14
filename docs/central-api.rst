.. auto generated file - DO NOT MODIFY

ODK Central API
=======================================================================================================================

`ODK Central Backend <https://github.com/getodk/central-backend>`__ is a RESTful API server that provides key functionality for creating and managing ODK data collection campaigns. It couples with `Central Frontend <https://github.com/getodk/central-frontend>`__, an independent frontend interface, to form `ODK Central <https://github.com/getodk/central>`__, a complete user-installable ODK server solution. While Central Frontend is the primary consumer of the ODK Central API, the API this server provides is fully public and generic: anything that can be done in the user interface can be done directly via the API.

You can read on for a brief overview of the main concepts and how they fit together, or jump to one of the sections for a more in-depth description.

API Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the API to manage your data collection campaigns, you will need to **authenticate**\  with it, so it knows who you are and what you are allowed to do. We provide multiple methods to authenticate with the API, as well as different models for managing the identities and permissions in your system. Human staff users that manage data collection campaigns are ``User``\ s, and mobile devices are granted access via ``App User``\ s, and each of these account types have their own way of authenticating. But, these concepts both boil down to ``Actor``\ s, which are how the API actually thinks about authentication and permissioning.

The ``/users``\  resource can be used to create, manage, and delete **Users**\ . These are the staff members who have administrative rights on your server, some projects, or both. Additional tasks like resetting a user's password are also available. You could use this API to, for example, synchronize accounts with another system or mass-provision Users.

Actors (and thus Users) may be granted rights via Assignments. In short, a Roles API is available which describes the defined Roles within the system, each of which allows some set of verbs. The Assignments APIs, in turn, assign Roles to certain Actors upon certain system objects. More information on these may be found below, under `Accounts and Users </central-api-accounts-and-users>`__.

The rest of system is made up mostly of standard REST resources and subresources, nested under and partitioned by the ``/projects``\  Projects resource. Forms, submissions to those forms, attachments on forms or submissions, and App Users ("App Users" in the management interface), are all subresources within ``/projects``\ . This way, each project is essentially its own sandbox which can be managed and manipulated at will.

The ``/projects/:id/app-users``\  subresource can be used to create, manage, and delete **App Users**\ .

The ``/projects/:id/forms``\  resource and its subresource ``/projects/:id/forms/…/submissions``\  provide full access to create, manage, and delete **``Form``\ s and ``Submission``\ s to those Forms**\ . Each Form is a single ODK XForms survey, and many Submissions (filled-out forms, also sometimes called ``Instance``\ s) may be attached to each Form. These resources are somewhat unique in that they are created by sending XML in the ODK XForms format instead of JSON. One can also retrieve all the multimedia attachments associated with any submission through the ``/projects/:id/forms/…/submissions/…/attachments``\  subresource.

Forms and their submissions are also accessible through two **open standards specifications**\  that we follow:

* The `OpenRosa <https://docs.getodk.org/openrosa/>`__ standard allows standard integration with tools like the `ODK Collect <https://docs.getodk.org/collect-intro/>`__ mobile data collection app, or various other compatible tools like `Enketo <https://enketo.org/>`__. It allows them to see the forms available on the server, and to send new submissions to them.

* The `OData <http://odata.org/>`__ standard allows data to be shared between platforms for analysis and reporting. Tools like `Microsoft Power BI <https://powerbi.microsoft.com/en-us/>`__ and `Tableau <https://public.tableau.com/en-us/s/>`__ are examples of clients that consume the standard OData format and provide advanced features beyond what we offer. If you are looking for a straightforward JSON output of your data, or you are considering building a visualization or reporting tool, this is your best option.

Finally, **system information and configuration**\  is available via a set of specialized resources. Currently, you may set the Usage Reporting configuration and retrieve Server Audit Logs.



.. toctree::
  :maxdepth: 1

  central-api-changelog
  central-api-authentication
  central-api-accounts-and-users
  central-api-project-management
  central-api-form-management
  central-api-submission-management
  central-api-dataset-management
  central-api-entity-management
  central-api-openrosa-endpoints
  central-api-odata-endpoints
  central-api-system-endpoints
  central-api-encryption
