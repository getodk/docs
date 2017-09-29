***********************************
Aggregate Usage
***********************************

- Beginning with ODK Aggregate 1.3.2, upon the initial installation of the server, it is configured to allow unauthenticated (anonymousUser) submissions from ODK Collect and unauthenticated browser access to the submissions and forms management functionality of ODK Aggregate. When the URL to the ODK Aggregate server is first opened, you will be presented with the application page showing the Submissions and Form Management tabs.
- In April 2015, the use of Google e-mail accounts for accessing the site (via Sign in with Google) stopped working (Google turned off that functionality).  If you have an existing site running an old version of ODK Aggregate that does not have ODK Aggregate usernames configured for website access (and offers a Sign in with Google sign-in choice), you will need to upgrade to regain access to it.
- Submitted data, once in ODK Aggregate, can be viewed, exported, mapped and deleted.

.. image:: /img/aggregate-use/features.*
   :alt: Image showing various features in ODK Aggregate.

- Use the :guilabel:`Add New Form` button on the :guilabel:`Form Management` tab to upload a new form definition to ODK Aggregate.

.. image:: /img/aggregate-use/form-manage.*
   :alt: Image showing form management tab.

- View data submitted from ODK Collect on the :guilabel:`Submissions` tab.

.. image:: /img/aggregate-use/submission.*
   :alt: Image showing submissions tab.

- If the :guilabel:`Site Admin` tab is not visible, click the :guilabel:`Log In` link in the upper right corner of the screen to be presented with the Log onto Aggregate screen. Choose the :guilabel:`Sign in with Aggregate password` button and enter the super-user username you specified within the installer. The initial password for this account is ``aggregate``. When signing in with this method, if you do not enter the password correctly, you may need to close all your browser windows and quit your browser before you can try again.

.. image:: /img/aggregate-use/log-in.*
   :alt: Image showing log in option

- If you have not yet changed your super-user password to something other than aggregate, the server will display `This server and its data are not secure! Please change the super-user's password!` at the top of the web page. Please visit the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to change this user's password.
- If the instance name of the server changes (the installer asks for this name), then the passwords for all ODK Aggregate usernames will be cleared (preventing their use) and the super-user username's password will be reset to aggregate and the above message will also be displayed. In this case, you should log in, change the super-user's password, and change the passwords for all of your ODK Aggregate usernames.
- Use the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to restrict who can download forms or submit data from ODK Collect. Do this by creating an ODK username and password and granting it **Data Collector** privileges. This username and password can then be entered into ODK Collect's settings page. When restricting access you must also remove the Data Collector privilege from the anonymousUser. Remember to click on **Save Changes** to make these changes take effect. Conversely, granting the Data Collector privilege to the anonymousUser enables anyone to submit data to your ODK Aggregate server.

.. image:: /img/aggregate-use/site-admin.*
   :alt: Image showing site admin and permissions tab.
   
- Use the :guilabel:`Permissions` sub-tab under the :guilabel:`Site Admin` tab to specify additional usernames with browser access to the server. For each user you add, select whether they have access to the submitted data (Data Viewer privileges), the ability to upload forms and export or publish data (Form Management), or the ability to manage site access and users (Site Admin) privileges. Remember to click :guilabel:`Save Changes` to make these changes take effect. And, for each username you define, remember to Change Password to assign a password; by default, usernames are created with unusable passwords. Granting any of these privileges to the anonymousUser enables browser access to these functions without first logging in.
