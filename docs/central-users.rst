.. _central-users-overview:

Managing Users in Central
=========================

There are two types of user accounts in ODK Central: **Web Users** and **App Users**.

 - **Web Users** have accounts on the Central management website. These accounts are global across all projects on the server. They can log into the web interface and perform administrative actions like user management, form upload and management, and submission data viewing and download. They can also fill and submit Forms directly in their web browser.
 - **App Users** can use mobile data collection apps like ODK Collect to :ref:`connect to Central <central-users-app-configure>`. App Users are limited to a single project at a time. Once connected through the app, they will be able to see the list of forms, download the ones they need, and upload completed submissions to those forms.

You will need both types of users in order to run a successful data collection project: a Web User must upload a valid form definition, an App User must upload submissions to it from their mobile device, and the Web User will then be able to see those submissions in the web interface and download them for analysis.

.. _central-users-web-roles:

Web User Roles
--------------

Central features Role-based User permissioning. Central currently defines four roles: Administrator, Project Manager, Project Viewer, and Data Collector.

Central roles allow the following:

+----------------------------------+---------------+-----------------+----------------+----------------+
| Action                           | Administrator | Project Manager | Project Viewer | Data Collector |
+==================================+===============+=================+================+================+
| **Projects**                                                                                         |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Edit details                     | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Archive                          | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Project Forms**                                                                                    |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| List all                         | x             | x               | x              | x              |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Edit attachments                 | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Edit details                     | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Set state                        | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Delete                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Project Form Submissions**                                                                         |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             | x               |                | x              |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Edit and review                  | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Comment                          | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| View and download                | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Access OData feed                | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Project Entity Lists**                                                                             |
|                                                                                                      |
| *Note: Data Collectors get read-only access to Entity Lists attached to Forms*                       |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| List all                         | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Add properties                   | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Update settings                  | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Project Entities**                                                                                 |
|                                                                                                      |
| *Note: Data Collectors create Entities when they fill Entity-creating Forms*                         |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| View and download                | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Access OData feed                | x             | x               | x              |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Update data                      | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Delete                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Project App Users**                                                                                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| List all                         | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Revoke access                    | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| See code                         | x             | x               |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| **Web Users**                                                                                        |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Create                           | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| List all                         | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Edit details                     | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| View email address               | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Revoke password                  | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+
| Delete                           | x             |                 |                |                |
+----------------------------------+---------------+-----------------+----------------+----------------+

.. _central-users-web-overview:

Managing Web Users
~~~~~~~~~~~~~~~~~~

You can make Users into Administrators from the :ref:`site-wide Users panel <central-users-web-role>`, and you can assign them as Project Managers or Viewers on the :ref:`Project Roles tab <central-project-roles>` within the Project.

To manage web users, navigate to :menuselection:`--> Users --> Web Users` at the top of the Central management website. You should see a listing of users that looks like this:

   .. image:: /img/central-users/web-users-listing.png

.. _central-users-web-create:

Creating a Web User
~~~~~~~~~~~~~~~~~~~

To create a new Web User, click on the :guilabel:`Create web user` button on the right side of the Web Users listing page. You will see a popup that looks like this:

   .. image:: /img/central-users/web-users-create.png

To create a new Web User, input the email address of the person who should receive access. Press :guilabel:`Create` once you are satisfied with the email address.

That email account will shortly receive an email with the subject line "ODK Central account created". If you do not see the email, check your spam folder. In the email, there will be a link which will allow the recipient to set a password for their new account, after which they will be able to log in.

The link is only valid for 24 hours. If 24 hours pass and it has not been used, you should use the :ref:`Reset Password <central-users-web-reset-password>` tool to send them a new link.

Newly created Web Users are only able to log in and edit their profile information. In order to give them access to do useful work on the server, please read the following section.

.. _central-users-web-role:

Assigning a site-wide Web User Role
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As mentioned under :ref:`central-users-web-roles` above, there are four Roles you may assign to Web Users in the current release of ODK Central: Administrator, Project Manager, Project Viewer, and Data Collector. Administrators may perform any action on the system, while Project Managers may perform any action on their assigned Project(s). Project Viewers may only see created forms and submissions within the Project they are assigned to, and cannot edit anything. Data Collectors may see the list of all Forms in the Project, and retrieve basic information about them, but may only create new Submissions. They cannot see any Submissions.

To learn how to assign a Project Manager or Viewer role, please see the :ref:`central-project-roles` section in the Projects guide.

To assign an Administrator role, navigate to the Web Users administration panel. There, you should see a table like this one:

   .. image:: /img/central-users/web-users-role.png

Under the :guilabel:`Sitewide Role` column in the table, you will see dropdown inputs with the options :guilabel:`Administrator` and :guilabel:`None`. To make a Web User an Administrator, change the dropdown next to their name to :guilabel:`Administrator`. You will see the page think for a moment, and then it will inform you that the action is done. To take away Administrator rights from a Web User, change the dropdown to :guilabel:`None`.

You will not be able to change your own Role in the system. To change your own Role, you will need to get somebody else to log in and change it for you.

.. _central-users-web-reset-password:

Resetting a Web User password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any user may request a reset of their own password by using the link at the bottom of the login screen:

   .. image:: /img/central-users/web-users-self-reset.png

After submitting the reset form, the user should receive an email with the subject line "ODK Central account password reset". If they cannot find it, they should check their spam folder. When resetting a password this way, the user's current password continues to function until they actually use the link in the email to set a new one.

We also provide a separate way for administrators to directly reset any Web User's password in the administration panel for two reasons:

1. In case the user's password has been stolen and needs to be disabled immediately.
#. In case the user does not know how to do this themselves.

With the administrative reset, the user's password **stops working immediately** and they will be completely unable to log in until a new one is set. They will receive an email with instructions and a link on how to do this exactly :ref:`as shown above <central-users-web-create>`. To perform the administrative reset, navigate to the Web Users listing page, and use the Actions menu at the right side of the table:

   .. image:: /img/central-users/web-users-admin-reset.png

.. _central-users-web-retire:

Retiring a Web User
~~~~~~~~~~~~~~~~~~~

When you retire a Web User, their login access will be revoked and they will be immediately signed out everywhere. They will disappear from the Web Users management list, but any records that trace their actions (submission uploader or form creator name, or audit log action initiator, for example) will still show their information.

If a retired Web User attempts to reset their password, they will receive a special email explaining that their account has been retired.

To retire a Web User, find them on the Web User administration panel, and open the Actions menu:

   .. image:: /img/central-users/web-users-retire.png

From here, select :guilabel:`Retire User` and follow the on-screen instructions.

.. _central-users-app-overview:

Managing App Users
------------------

App Users never gain any access to the management website: they do not have email addresses or passwords associated with their account, only a nickname so you can tell which is which. Once a Web User creates an App User within some project, a :doc:`configuration QR Code <collect-import-export>` will be generated which will grant a mobile device access to that project as that App User. Access can be revoked at any time, and Web Users can see which App Users uploaded which submissions.

A newly created App User does not have access to any Forms. To give them access once they are created, use the :ref:`Form Access <central-projects-form-access>` tab on the Project. You will be able to allow access to particular Forms within the Project for each App User.

.. tip::
  In version 0.6 and earlier of ODK Central, all App Users were granted download and submission rights on all Forms within their Project. These users retain their access when you first upgrade to version 0.7. Once you have version 0.7 installed, you can adjust these Users' access per form.

To manage App Users, navigate to the project whose App Users you wish to manage, and then click on the :guilabel:`App Users` tab just below the project name. You should see a listing of users that looks like this:

   .. image:: /img/central-users/app-users-listing.png

.. _central-users-app-create:

Creating an App User
~~~~~~~~~~~~~~~~~~~~

To create a new App User, click on the :guilabel:`Create app user` button on the right side of the App Users listing page. You will see a popup that looks like this:

   .. image:: /img/central-users/app-users-create.png

Once you provide a nickname for the user (usually the name of the data enumerator who will carry the mobile device works well), click :guilabel:`Create`. The user will be created, and you will see a screen that looks like this:

   .. image:: /img/central-users/app-users-created.png

That App User has now been created and granted access to use their mobile device to list, download, and submit to all :ref:`available forms <central-forms-lifecycle>` within their project. To do so, however, their mobile device will have to get set up with this new account. That is what the QR Code you see on this screen is for. Read on to the next section to find out how to use it.

.. _central-users-app-configure:

Configuring an App User mobile device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A mobile device will need to be configured to access your ODK Central server as a particular App User in order to gain access to the forms and upload submissions within their project. This is done by way of the Collect Settings QR Code.

The QR Code contains information about how to find your ODK Central server, and how to prove to the server that the mobile device belongs to a valid App User. In future versions of ODK Central, it will be possible to specify other settings to be imported to the device as well.

There are two ways to access the QR Code for an App User. The first is in the second step of the :ref:`App User creation wizard <central-users-app-create>`. Please find the second screenshot in the previous section to see what this looks like. If you close out of this wizard, you can still access the QR Code by clicking on the :guilabel:`See code` link in the listings table:

   .. image:: /img/central-users/app-users-code.png

If instead of a :guilabel:`See code` link you see text that says :guilabel:`Access revoked`, that App User no longer has access to the server. Create a new App User if you need a new QR Code.

Once you have found the QR Code, distribute it to data collectors so they can configure ODK Collect. See :doc:`settings QR codes <collect-import-export>` to learn more.

.. _central-users-app-revoke:

Revoking an App User
~~~~~~~~~~~~~~~~~~~~

You may wish to revoke an App User's access, for instance if their QR Code has been stolen or if they have left the organization. To do so, navigate to the App Users listing page, and use the Actions menu at the right side of the table:

   .. image:: /img/central-users/app-users-revoke.png

App Users whose access has been revoked will still appear in the App Users listing table, and will still be visible as the submitter of any submissions they uploaded. However, they no longer have a valid QR Code with which they can configure an ODK Collect installation, and any mobile devices already configured with their code will no longer have access to the project.

