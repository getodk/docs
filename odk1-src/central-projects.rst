.. _central-projects:

Managing Projects in Central
============================

New as of `version 0.4 <https://github.com/opendatakit/central/releases/tag/v0.4.0-beta.1>`_, almost everything in ODK Central is organized by Project. Forms, Managers, and App Users are all partitioned by project. Both on the administration website as well as on a mobile device (within ODK Collect, for example), access to each project and its forms can be managed person-by-person. Only the Central administrative staff can create and grant initial access to projects.

.. _central-projects-overview:

Projects Overview and Roadmap
-----------------------------

Projects are a work in progress that we will add to and improve over the next few releases. If you are working on ODK Central **version 0.4**, projects work like this:

 - All **forms** must belong to a project. It is not possible to create a form that is not part of a project. It is not possible to assign one form to multiple projects (though the same form may be uploaded to as many projects as desired).
 - All **App Users** (who may access Project Forms through mobile device applications like Collect) must also belong to a particular project.

   - When a user connects to a project through Collect, they will only be able to see and submit new data to forms within that project.

If you have upgraded to **version 0.5**, the following changes have been made:

 - Only **Web Users** (who are allowed to administer ODK Central through the management website) marked **Administrator** have administrative access to the main site settings and all projects.

   - However, all Web Users created before version 0.5 were already marked Administrator. You will have to go change their :ref:`Site-wide Role <central-users-web-role>` to None if you wish to remove these privileges.

 - Normal Web Users who are not Administrators can be made Managers on select projects. These users have the ability to manage anything about the project. They can:

   - Appoint other project managers.
   - Create, manage, and archive forms on the project.
   - Access all submitted data within the project.
   - Create, manage, and retire App Users for the project.
   - Manage and archive the project itself.

Since the major changes that occurred in version 0.5, we have additionally made the following improvements:

 - Better, centralized form state and access management.
 - More granular project access, in the form a Project Viewer role which allows read-only access only to Forms and Submission data.

In future releases, we have a `loose roadmap <https://github.com/opendatakit/central/issues/35>`_ with at least the following goals:

 - Change the relationship between Collect and Central so that with one button you can synchronize the mobile device to some centrally managed desired state.

   - So for instance, you can decide which forms should be available on Collect within Central once, and within Collect just press "synchronize" to update to that state.
   - Eventually, Collect app settings may be synchronized this way as well.
   - And eventually, different App Users of different roles may be assigned different device states.

 - Download an entire project’s data at once.

If you have ideas on how projects might be made more useful for you, please do not hesitate to leave us feedback on the `ODK Forum <https://forum.opendatakit.org/c/features>`_.

.. _central-projects-migrate:

Migrating to Projects
---------------------

If you have an ODK Central server installed which is version 0.3 or earlier, your existing data will be migrated into a project when you update.

All of your existing forms and App Users will be placed into a project entitled "Forms you created before projects existed". There are no longer site-wide App Users, so that panel will no longer be present.

.. admonition:: Important: Upgrading to version 0.5

  Mobile clients like Collect which were configured to access version 0.3 will continue to work without intervention for version 0.4, but they must be reconfigured with a new QR Code access token from Central before migration to 0.5, because for version 0.5 this backwards compatibility will be removed.

  If you do not refresh the access tokens before upgrading to 0.5, you will have to reconfigure the device with a new QR Code from 0.5 in order to restore the connection.

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

.. _central-project-settings:

Editing Project Settings
~~~~~~~~~~~~~~~~~~~~~~~~

To edit Project Settings, first navigate to the Project, then click on the :guilabel:`Settings` tab underneath the Project name.

   .. image:: /img/central-projects/settings.png

From here, you will be able to edit the Project Name. You will also see a section for Archiving a Project, which is described in more detail :ref:`below <central-project-archive>`.

.. _central-project-roles:

Managing Project Roles
~~~~~~~~~~~~~~~~~~~~~~

Any Web User may be assigned as a Project Manager or Project Viewer on a Project.

Project Managers may perform any action upon and within that Project, including changing its name, adding more Project Managers, and uploading and managing Forms and Submissions. Any Web Users that are site-wide Administrators will already be able to perform these actions on any Project without being explicitly named a Manager.

Project Viewers can view basic information about all Forms in the Project, and download Submission data or access it over OData for analysis. They cannot make any modifications to any data or settings.

You will find a detailed breakdown of user roles :ref:`here <central-users-web-roles>`.

To assign or remove Managers or Viewers for a Project, first go to the Project overview page, then click on the :guilabel:`Project Managers` tab under the Project name. You should see the following page:

   .. image:: /img/central-projects/roles.png

If roles have not already been assigned to the Project, the table will be empty. This is normal: the table only shows Users with assigned roles on the Project at first. To find a Web User to assign them a role, search for them in the :guilabel:`Search for a user` field above the table. You can find users by their Display Name or their Email. Type part or all of either into the box, and press :kbd:`Enter`. The search results will appear in the table.

   .. image:: /img/central-projects/role.png

To make a Web User into a Project Manager or Viewer, change the dropdown next to their name in the :guilabel:`Project Role` column from :guilabel:`None` to :guilabel:`Manager`. You should see the page think for a moment, and then a confirmation of success. If you clear the search in the text box, the newly assigned user should remain.

To demote a Web User from any role, change the dropdown back to :guilabel:`None`.

.. _central-project-app-users:

Managing Project App Users
~~~~~~~~~~~~~~~~~~~~~~~~~~

To manage App Users for a Project, you can navigate to the Project overview page, then click on the :guilabel:`App Users` tab under the Project name. For more information about creating, managing, and retiring Project App Users, please see :ref:`this section <central-users-app-overview>`.

.. _central-projects-form-access:

Managing Form Access
~~~~~~~~~~~~~~~~~~~~

Right now, Central offers two ways to control around Form Access within each Project:

 - Each Form's :ref:`Lifecycle State <central-forms-lifecycle>` controls whether any App User can download and/or submit to that Form. Near the end of a Form's life, for example, it makes sense to disallow downloading the Form as a blank, but still receive any submissions that have already been created.
 - Access to download and submit each Form can be customized per App User associated with the Project. When first creating a Form, for example, it makes sense to only allow a testing user access to the Form so that one can be sure that it works before rolling it out to all users.

We place these access controls for all Forms in a single place, on the Form Access tab at the Project level. To access it, navigate to the Project and select the tab at the top of the page labeled :guilabel:`Form Access`.

   .. image:: /img/central-projects/access.png

On the left side of the Form Access page, you will find a list of all the Forms in the Project, along with a dropdown selection to set the lifecycle state for each one. Along the top, you will see all active App Users in the Project. At each row/column intersection, there is a checkbox that governs whether each App User is allowed access to each Form.

If you are having trouble recalling what each Form State means, the :guilabel:`?` icon in the header will give you a quick recap:

   .. image:: /img/central-projects/access-states.png

As you make changes to Form States and App User access, they will be highlighted in yellow. You can make all the changes you'd like to apply at once (marking an old version of a Form as Closing while granting Open access to the new one, for example), and once you are satisfied with what you see you can click the Save button at the top-right of the screen to apply them all at once.

.. tip::
  When you first create an App User, it will not have access to any Forms. When you first create a Form, no App Users will be allowed to access it.

.. _central-project-archive:

Archiving a Project
~~~~~~~~~~~~~~~~~~~

When you Archive a Project, it will appear at the bottom of the Project List on the homepage, with :guilabel:`(archived)` added onto the end of its name.

In version 0.6 of Central, archiving a Project would disable certain features on it. We have eliminated this behavior, so all your archived Projects can still be used and manipulated freely.

To Archive a Project, first navigate to the Project, then click on the :guilabel:`Settings` tab underneath the Project name.

   .. image:: /img/central-projects/settings.png

Click on the red :guilabel:`Archive this Project` button on the right, and follow the on-screen instructions to proceed.

