.. _central-users-overview:

Managing Users in Central
=========================

There are two types of user accounts in ODK Central: **web users** and **app users**.

 - **Web users** have accounts on the Central management website. These accounts are global across all projects on the server. They can log into the web interface and perform administrative actions like user management, form upload and management, and submission data viewing and download.
 - **App users** can use mobile data collection apps like ODK Collect to :ref:`connect to Central <central-users-app-configure>`. App Users are limited to a single project at a time. Once connected through the app, they will be able to see the list of forms, download the ones they need, and upload completed submissions to those forms.

You will need both types of users in order to run a successful data collection project: a web user must upload a valid form definition, an app user must upload submissions to it from their mobile device, and the web user will then be able to see those submissions in the web interface and download or sync them for analysis.

.. _central-users-web-overview:

Managing Web Users
------------------

In the current alpha release of Central, all web users are administrators. This means that all web users will be able to see and do everything any other web user can:

 - Manage web users
    - Create new web users
    - See all current web users and their email addresses
    - Revoke web user passwords
 - Manage projects
    - Create new projects
 - Manage app users
    - Create new app users
    - See all current app users
    - Revoke app user access
    - See app user provisioning code
 - Manage forms
    - Create new forms
    - See all current forms
    - Manage form attachments
    - Set form lifecycle state
    - Delete any form
    - See all submissions for any form
       - Download all submissions for any form
       - Access submission data via OData
 - Configure the server
    - Set up automated backups
    - Terminate a scheduled automated backup

Also in the current alpha release, all users are known only by their email addresses, which cannot currently be altered once set. Nicknames, profile edit, and user delete are all coming soon.

To manage web users, navigate to :menuselection:`--> Users --> Web Users` at the top of the Central management website. You should see a listing of users that looks like this:

   .. image:: /img/central-users/web-users-listing.png

.. _central-users-web-create:

Creating a Web User
~~~~~~~~~~~~~~~~~~~

To create a new Web User, click on the :guilabel:`Create web user` button on the right side of the Web Users listing page. You will see a popup that looks like this:

   .. image:: /img/central-users/web-users-create.png

To create a new Web User, input the email address of the person who should receive access. As :ref:`noted above <central-users-web-overview>`, in the current alpha release the person will get full administrative access to the site. Press :guilabel:`Create` once you are satisfied with the email address.

That email account will shortly receive an email with the subject line "ODK Central account created". If you do not see the email, check your spam folder. In the email, there will be a link which will allow the recipient to set a password for their new account, after which they will be able to log in.

The link is only valid for 24 hours. If 24 hours pass and it has not been used, you should use the :ref:`Reset Password <central-users-web-reset-password>` tool to send them a new link.

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

.. _central-users-web-delete:

Deleting a Web User
~~~~~~~~~~~~~~~~~~~

This is not yet possible in the current alpha release of ODK Central.

.. _central-users-app-overview:

Managing App Users
------------------

App Users never gain any access to the management website: they do not have email addresses or passwords associated with their account, only a nickname so you can tell which is which. Once a Web User creates an App User within some project, a :doc:`configuration QR Code <collect-import-export>` will be generated which will grant a mobile device access to that project as that App User. Access can be revoked at any time, and Web Users can see which App Users uploaded which submissions.

In the current alpha release of ODK Central, all App Users can download any :ref:`Open form  <central-forms-lifecycle>` and upload submissions to any :ref:`non-Closed form <central-forms-lifecycle>` within their project. Future versions will feature more options to restrict certain App Users to certain forms.

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

Once you have found the QR Code, you will be able to use it to configure ODK Collect. Please see the section on :doc:`importing settings into Collect <collect-import-export>` to learn how to do this.

.. _central-users-app-revoke:

Revoking an App User
~~~~~~~~~~~~~~~~~~~~

You may wish to revoke an App User's access, for instance if their QR Code has been stolen or if they have left the organization. To do so, navigate to the App Users listing page, and use the Actions menu at the right side of the table:

   .. image:: /img/central-users/app-users-revoke.png

App Users whose access has been revoked will still appear in the App Users listing table, and will still be visible as the submitter of any submissions they uploaded. However, they no longer have a valid QR Code with which they can configure an ODK Collect installation, and any mobile devices already configured with their code will no longer have access to the project.

