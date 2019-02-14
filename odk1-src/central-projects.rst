.. _central-projects:

Managing Projects in Central
============================

New as of `version 0.4 <https://github.com/opendatakit/central/releases/tag/v0.4.0-beta.0>`_, almost everything in ODK Central is organized by Project. Forms, Managers, and App Users are all partitioned by project. Both on the administration website as well as on a mobile device (within ODK Collect, for example), access to each project and its forms can be managed person-by-person. Only the Central administrative staff can create and grant initial access to projects.

.. _central-projects-overview:

Projects Overview and Roadmap
-----------------------------

Projects are a work in progress that we will add to and improve over the next few releases. As of **version 0.4**, projects work like this:

 - All **forms** must belong to a project. It is not possible to create a form that is not part of a project. It is not possible to assign one form to multiple projects (though the same form may be uploaded to as many projects as desired).
 - All **App Users** (who may access Central forms through mobile device applications like Collect) must also belong to a particular project.
    - When a user connects to a project through Collect, they will only be able to see and submit new data to forms within that project.

In the next release, **version 0.5**, we plan to add the following:

 - No longer will all **Web Users** (who are allowed to administer ODK Central through the management website) have administrative access to the main settings and all projects.
 - Rather, only users marked **administrator** will have this access.
 - Normal Web Users who are not Administrators can be made Managers on select projects. These users have the ability to manage anything about the project. They can:
    - Appoint other project managers.
    - Create, manage, and archive forms on the project.
    - Access all submitted data within the project.
    - Create, manage, and retire App Users for the project.
    - Manage and archive the project itself.

And in future releases beyond that, we have a `loose roadmap <https://github.com/opendatakit/central/issues/35>`_ with at least the following goals:

 - Change the relationship between Collect and Central so that with one button you can synchronize the mobile device to some centrally managed desired state.
    - So for instance, you can decide which forms should be available on Collect within Central once, and within Collect just press "synchronize" to update to that state.
    - Eventually, Collect app settings may be synchronized this way as well.
    - And eventually, different App Users of different roles may be assigned different device states.
 - Better, centralized form workflow/status management.
 - More granular project access: for example, a project Web User role type that grants read-only access to submitted data.
 - Download an entire project’s data at once.

If you have ideas on how projects might be made more useful for you, please do not hesitate to leave us feedback on the `ODK Forum <https://forum.opendatakit.org/c/features>`_.

.. _central-projects-migrate:

Migrating to Projects
---------------------

If you have an ODK Central server installed which is version 0.3 or earlier, your existing data will be migrated into a project when you update.

All of your existing forms and App Users will be placed into a project entitled "Forms you created before projects existed". There are no longer site-wide App Users, so that panel will no longer be present.

.. admonition:: Important: Preparing for version 0.5

  Mobile clients like Collect which were configured to access version 0.3 will continue to work without intervention for version 0.4, but they must be reconfigured with a new QR Code access token from Central when possible, because for version 0.5 this backwards compatibility will be removed.

.. _central-projects-create:

Creating a Project
------------------

Only ODK Central administrators may create projects. To create a project, navigate to the Projects section of the Central management homepage, and click on the :guilabel:`New` button.

   .. image:: /img/central-projects/new.png

You will be asked for a name for your new project. When you provide one and press :guilabel:`Create`, your project will be created and you will be taken to its management page.

.. _central-projects-manage:

Managing a Project
------------------

You can find all the projects you have access to in the Projects section of the ODK Central management website homepage.

   .. image:: /img/central-projects/list.png

When you click on its name, you will be taken to its management page.

   .. image:: /img/central-projects/overview.png

Here, you will find some basic details about the project, and a listing of all the forms in the project. You can click on any form name to :ref:`manage that form <central-forms-overview>` and view its submission data.

From the navigation tabs below the project name, you can also navigate to the App Users management page for that project, from which you can :ref:`create, manage, and retire app users <central-users-app-overview>`.

