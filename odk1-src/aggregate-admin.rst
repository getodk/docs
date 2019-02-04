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

Please visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to change this user's password.

You can specify additional usernames with browser access to the server under the :guilabel:`Permissions` sub-tab. Privileges are as follows:

- **Data Collector**: able to download forms to ODK Collect and submit data from ODK Collect to ODK Aggregate.

.. note::

   - Only ODK accounts and the anonymousUser can be granted Data Collector rights.
   - The anonymousUser must be granted Data Collector rights to accept submissions from unidentified sources (e.g., from ODK Collect 1.1.5 and earlier, or from ODK Collect 1.1.7 and later if not authenticating).

- **Data Viewer**: able to log onto the ODK Aggregate website, filter and view submissions, and generate csv or kml files for download.
- **Form Manager**: all the capabilities of a Data Viewer plus the abilities to upload a form definition, delete a form and its data, and upload submissions manually through the ODK Aggregate website.
- **Site Administrator**: all the capabilities of a Form Manager plus the ability to add users, set passwords, and grant these capabilities to other users.

Remember to click :guilabel:`Save Changes` to make these changes take effect. You can also edit the privileges for current users.

You can upload a :file:`.csv` file of users and their capabilities as well as download the current file.

.. _preference-tab:

Preferences
~~~~~~~~~~~~

In the :guilabel:`Preferences` sub-tab under :guilabel:`Site Admin` tab, you can manage:

- Google API credentials: These credentials are used when publishing into Google services. For details on this, see :doc:`Aggregate OAuth2 info <oauth2-service>`.

- **Enketo credentials**: These credentials are used for Enketo webforms integration. To link Enketo with Aggregate, see `this <https://accounts.enketo.org/support/aggregate/>`_.
- **ODK 2.0 App name**

   - *ODK Tables Synchronization Functionality* - check this to enable ODK Tables functionality to download, upload and alter data records within ODK Tables as restricted by table-access privileges granted to the user.

- **Aggregate features**: These settings affect the operations of the server.

   - *Skip malformed submissions* - check this to ignore corrupted submissions.
