.. _central-projects:

Managing Projects in Central
============================

Almost everything in ODK Central is organized by Project: Forms, Managers, and App Users are all partitioned by project. Both on the administration website as well as on a mobile device (within ODK Collect, for example), access to each project and its forms can be managed person-by-person. Only the Central administrative staff can create and grant initial access to projects.

.. _central-projects-overview:

Projects Overview
-----------------

With Projects, you can organize your Forms and Users into separate efforts. Many things in Central, like Forms, cannot be created except inside a particular Project.

   .. image:: /img/central-projects/structure.svg

In general, Projects consist of Forms and their submissions, and the people assigned to facilitate the process.

Administrators may manage any Project. Web Users that have been created on the Central server can be assigned a specific role for each Project: they can be a Project Manager able to see and change anything about the Project, a Data Collector who uses the Central website in a web browser to collect data, or another of our supported :ref:`Project Roles <central-users-web-role>`.

App Users are created specifically inside and for each Project, and can use a mobile device to collect Submission data. You can assign individual App User accounts access to specific Forms.

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

You can also see in this list the Forms in each Project. You can click on a Form to navigate directly to it, or click on any of the numbers to see only Submissions in that state. Otherwise, click on a Project name to see its details.

   .. image:: /img/central-projects/overview.png

Here, you will find some basic details about the project, and a listing of all the forms in the project. The text at the top of the Projects page is customizable per Project by Administrators and Project Managers, and can include tables, formatted text, links, images, and anything else supported by Markdown.

You can click on any form name to :ref:`manage that form <central-forms-overview>` and view its submission data.

.. _central-project-settings:

Editing Project Settings
~~~~~~~~~~~~~~~~~~~~~~~~

To edit Project Settings, first navigate to the Project, then click on the :guilabel:`Settings` tab underneath the Project name.

   .. image:: /img/central-projects/settings.png

From here, you will be able to edit the Project name and description. Markdown is supported in the description field, so you can insert formatted text, headings, tables, images, and links. All members of a Project see the same description on the overview page, so it's a great place to put instructions, notices, and links to useful resources related to the Project.

You will also see a section for Archiving a Project, which is described in more detail :ref:`below <central-project-archive>`. You can also enable :ref:`Project Managed Encryption <central-encryption-managed>`.

.. _central-project-roles:

Managing Project Roles
~~~~~~~~~~~~~~~~~~~~~~

Any Web User may be assigned as a Project Manager or Project Viewer on a Project.

Project Managers may perform any action upon and within that Project, including changing its name, adding more Project Managers, and uploading and managing Forms and Submissions. Any Web Users that are site-wide Administrators will already be able to perform these actions on any Project without being explicitly named a Manager.

Project Viewers can view basic information about all Forms in the Project, and download Submission data or access it over OData for analysis. They cannot make any modifications to any data or settings.

Data Collectors may view the list of Forms, retrieve basic information about them, and submit new records to any Form in the Project.

You will find a detailed breakdown of user roles :ref:`here <central-users-web-roles>`.

To assign or remove Managers, Viewers, or Collectors for a Project, first go to the Project overview page, then click on the :guilabel:`Project Managers` tab under the Project name. You should see the following page:

   .. image:: /img/central-projects/roles.png

If roles have not already been assigned to the Project, the table will be empty. This is normal: the table only shows Users with assigned roles on the Project at first. To find a Web User to assign them a role, search for them in the :guilabel:`Search for a user` field above the table. You can find users by their Display Name or their Email. Type part or all of either into the box, and press :kbd:`Enter`. The search results will appear in the table.

   .. image:: /img/central-projects/role.png

To make a Web User into a Project Manager, Viewer, or a Data Collector, change the dropdown next to their name in the :guilabel:`Project Role` column from :guilabel:`None` to the desired role. You should see the page think for a moment, and then a confirmation of success. If you clear the search in the text box, the newly assigned user should remain.

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

On the left side of the Form Access page, you will find a list of all the Forms in the Project, along with a dropdown selection to set the Form Lifecycle state for each one. Along the top, you will see all active App Users in the Project. At each row/column intersection, there is a checkbox that governs whether each App User is allowed access to each Form.

.. tip::
  You may see a pencil icon next to the Lifecycle state dropdown on some Forms. This means that those Forms are currently Drafts, with no published version. They will not be visible to data collection clients no matter the Lifecycle state setting, or the checkboxes on this page. Once a Draft Form is published, then the settings on this page will immediately take effect.

If you are having trouble recalling what each Form State means, the :guilabel:`?` icon in the header will give you a quick recap:

   .. image:: /img/central-projects/access-states.png

As you make changes to Form States and App User access, they will be highlighted in yellow. You can make all the changes you'd like to apply at once (for example, marking an old version of a Form as Closing while granting Open access to the new one), and once you are satisfied with what you see you can click the Save button at the top-right of the screen to apply them all at once.

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

