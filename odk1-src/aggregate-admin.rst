Administering Aggregate
===========================

Click the :guilabel:`Log In` link in the upper right corner of the screen to be presented with the Log onto Aggregate screen. Choose the :guilabel:`Sign in with Aggregate password` button and enter the super-user username you specified within the installer. The initial password for this account is `aggregate`. When you log in, :guilabel:`Site Admin` will be visible to you.

.. tip::

  When signing in with this method, if you do not enter the password correctly, you may need to close all your browser windows and quit your browser before you can try again.

.. warning::

  If the instance name of the server changes (the installer asks for this name), then the passwords for all ODK Aggregate usernames will be cleared (preventing their use) and the super-user username's password will be reset to aggregate and the above message will also be displayed. In this case, you should log in, change the super-user's password, and change the passwords for all of your ODK Aggregate usernames.

.. _aggregate-permissions:

Permissions
~~~~~~~~~~~~~

.. warning::
   Remember to change the default password of your super-user account. Otherwise, anyone can take complete control of your server!

You can manage the credentials to access Aggregate in the :guilabel:`Site Admin` > :guilabel:`Permissions` sub-tab.

Privileges are as follows:

- **Data Collector**: able to download forms to ODK Collect and submit data from ODK Collect to ODK Aggregate.
- **Data Viewer**: able to log onto the ODK Aggregate website, filter, view, and export submissions.
- **Form Manager**: all the capabilities of a Data Viewer plus the abilities to upload a form definition, delete a form and its data, and upload submissions manually through the ODK Aggregate website.
- **Site Administrator**: all the capabilities of a Form Manager plus the ability to add users, set passwords, and grant these capabilities to other users.

You can also download a :file:`.csv` template file with all the credentials and upload it to make changes in bulk.

Remember to click :guilabel:`Save Changes` to make these changes take effect. You can also edit the privileges for current users.

.. _preference-tab:

Preferences
~~~~~~~~~~~~

In the :guilabel:`Preferences` sub-tab under :guilabel:`Site Admin` tab, you can manage:

- **Google API credentials**: These credentials are used when publishing into Google services. For details on this, see :doc:`Aggregate OAuth2 info <oauth2-service>`.
- **Enketo credentials**: These credentials are used for Enketo webforms integration. To link Enketo with Aggregate, see `this <https://accounts.enketo.org/support/aggregate/>`_.
- **Aggregate features**: These settings affect the operations of the server.

   - *Skip malformed submissions* - check this to ignore corrupted submissions.
