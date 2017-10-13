***************************
OAuth2 Service Account
***************************

.. _oauth-service:

Overview
====================
Publishing your data into Google Spreadsheets or Google Fusion Tables requires a Google Oauth2 Service Account.

.. _api-request:

.. note::

   - Google now throttles requests for all of its APIs. This impacts ODK Aggregate's Map visualization (which requires an API key) and the publishing to Google Sheets and the publishing to Google Fusion Tables (both of which require a service account). 
   - If you have difficulties with any of these, go to the Google Cloud Platform project in which you created your service account, navigate to the API Manager tab, navigate to the appropriate API (either via the Dashboard list or via the links on the library sub-tab). 
   - If the API is enabled, you will have a graphical overview of your use of the API. Click on the Quota heading on the page to see the quotas for the API. By clicking on the pencil icons to the right of these quotas, you will get a pop-up from which you can request an increase in a quota. 
   - The quota that most critically needs to be increased is the Google Sheets quota for write requests per second per user. A better limit is 500 per second per user, or perhaps higher if your forms have many fields and/or repeat groups.

The Google API Key used by the Maps visualization is created and managed on the same screen as the Google Oauth2 Service Account.This page guides you through the creation and uploading of these two credentials into ODK Aggregate

.. _create-google-credentials:

Create the Google Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credentials are associated with a Google Cloud Platform project.

1. If you are using App Engine for your ODK Aggregate server, then you have already set up a Google Cloud Platform project -- you just need to navigate to it. Otherwise, you will need to create one. In either case, go to Google Cloud Platform and click on :guilabel:`Console`:

.. image:: /img/oauth2-service/my-console.*
   :alt: Image showing console.
   
2. If you have never configured a Google Cloud Platform project, please refer :ref:`this section <install-app-engine>` to configure a project using App Engine under which aggregate server would run.
   
3. If you have already configured you should be able to see the project screen, showing the project name in the upper-left side of the screen.In this case, I named my project "My Project 80299" and project id "regal-mediator-181503".

.. image:: /img/oauth2-service/myconsole-2.*
   :alt: Image showing project screen.
   
4. Click on the menu icon(three horizontal bars) in the upper-left side of the screen.

.. image:: /img/oauth2-service/menu-icon.*
   :alt: Image showing menu.
   
5. Now select :guilabel:`APIs & services` from the menu and then select :guilabel:`Library` option

.. image:: /img/oauth2-service/api-menu.*
   :alt: Image showing APIs option.
   
6. This will take you to the lists all the application APIs that Google offers. 

.. image:: /img/oauth2-service/api-library.*
   :alt: Image showing lists pf application of APIs.


To be able to publish to Google Sheets and Fusion Tables, and to be able to view maps, we need to enable this project to use 4 of these application APIs. The 4 application APIs we need to enable are:

- Google Maps Javascript API v3
- Drive API
- Sheets API
- Fusion Tables API

The Sheets API is under the same section heading as the Drive API.

7. For each of these APIs, click on the API. This takes you to an information page for that API. On that page, click on the :guilabel:`Enable` button. E.g., on the Google Maps Javascript API v3 page, it looks like this:

.. image:: /img/oauth2-service/enable-api.*
   :alt: Image showing information page for API.
   
8. After clicking on :guilabel:`Enable`, if you have more application APIs to enable, click on the back-arrow within the page to return to the list of application APIs (and repeat the previous step):

.. image:: /img/oauth2-service/after-enable.*
   :alt: Image showing after enable screen.
   
Otherwise, after enabling it, click on the :guilabel:`Create Credentials` button:

.. image:: /img/oauth2-service/after-enable-create.*
   :alt: Image showing Credentials option.
   
9. And on the credentials page, choose to create a ``service account``.

.. image:: /img/oauth2-service/Service-account.*
   :alt: Image showing service account option.
   
10. This takes you to the list of service accounts for your Google Cloud Platform project.Click on :guilabel:`Create service account`.

.. image:: /img/oauth2-service/create-service-account.*
   :alt: Image showing create service account option.
   
.. note::
  
  If you are using App Engine, there will already be a service account listed that was created and is used by Google's infrastructure. Please ignore that.
  
11. On the next screen, enter a name for the service account (e.g., "ODK Oauth2 Publishing"), choose to furnish a new private key, select a role, and request the P12 format. Then click :guilabel:`Create`:

.. image:: /img/oauth2-service/create-service-dialog.*
   :alt: Image showing service account dialog box.
   
12. The private key for this service account will begin downloading (it will have a .p12 file extension). After it has downloaded, click :guilabel:`Close`.

.. image:: /img/oauth2-service/created-account.*
   :alt: Image showing service account and key created dialog box.

13. This returns you to the list of service accounts. Click on the the menu icon to the left of **Google Cloud Platform** and select :guilabel:`APIs & services` from the menu and then select :guilabel:`Credentials` option.

.. image:: /img/oauth2-service/credentials.*
   :alt: Image showing Credentials option.
   
14. Choose :guilabel:`Create credentials` and select ``API Key``.

.. image:: /img/oauth2-service/create-credentials.*
   :alt: Image showing create credentials option.
   
15. After selecting ``API key`` an API key will be generated, copy it as it will be used further and click on :guilabel:`Restrict Key`.

.. image:: /img/oauth2-service/Api-key.*
   :alt: Image showing API key .
   
16. Enter a name (e.g., "ODK Aggregate"), enter the hostname (and port, if nonstandard) of your ODK Aggregate server, followed by a slash and star and choose the key restriction(**HTTP referrers**). Then click :guilabel:`Save`: 

.. image:: /img/oauth2-service/restrict-api.*
   :alt: Image showing how to restrict api .
   
17. You will be redirected to credentials page, now click on :guilabel:`OAuth consent screen` tab.

.. image:: /img/oauth2-service/oauth.*
   :alt: Image showing OAuth consent screen tab.

18. Enter a product name and email address on this screen and fill in any additional fields that you might want to provide.Click :guilabel:`Save`.

.. image:: /img/oauth2-service/credentials-info.*
   :alt: Image showing credentials information.
   
19. Once again, click on the :guilabel:`Credentials` tab if not redirected, select the ``ODK Oauth2 Publishing`` key that you created above, and choose ``Manage service accounts``:

.. image:: /img/oauth2-service/manage-service-account.*
   :alt: Image showing manage service account option.
   
20. This takes you to details about that **ODK Oauth2 Publishing** service account. Keep this browser screen open; you will need to cut and paste values from this screen into ODK Aggregate. This is what those details look like:

.. image:: /img/oauth2-service/service-account-id.*
   :alt: Image showing details about that ODK Oauth2 Publishing service account.
   
.. note::

  - The **Service Account** information and the downloaded private key file must be uploaded to ODK Aggregate to enable publishing to Google Spreadsheets and Google Fusion Tables.
  - The **API Key** is for use by Google Maps.
  
.. _entering-credential-odk-aggregate:

Entering Credentials into ODK Aggregate 1.3 and higher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you have created the credentials , you need to upload these credentials to ODK Aggregate.

The same credentials can be used across multiple ODK Aggregate servers.

To upload the credentials:

1. Log onto ODK Aggregate as a Site Administrator. Click on the :guilabel:`Site Admin` then click on :guilabel:`Preferences` tab.Now, click on :guilabel:`Change Google API Credentials`.

.. image:: /img/oauth2-service/change-google-api.*
   :alt: Image showing Change Google API Credentials option.
   
2. This will bring up the **Google API Credentials Upload** dialog.From the Google website, copy and paste the **API key** into ODK Aggregate's ``Simple API Key`` field.
3. Click on :guilabel:`Choose File` and select the previously-downloaded (from Step 1, above) P12 private key file.
4. From the Google website, copy and paste the **Service account** section's "Key ID" into ODK Aggregate's ``ID (Key ID) or perhaps Client ID`` field.
5. From the Google website, copy and paste the **Service account ID** (it looks like an Email address) into ODK Aggregate's ``Service Account ID (looks like an Email address)`` field:

.. image:: /img/oauth2-service/upload-api.*
   :alt: Image showing Google API Credentials Upload dialog box.
   
6. Click on :guilabel:`Upload Google Credentials`. This should present a successful-upload pop-up:

.. image:: /img/oauth2-service/success.*
   :alt: Image showing successful upload pop-up box.
   
7. Click on the :guilabel:`X` to close that pop-up. The ``Simple API Access Key`` and ``Google OAuth2 Credentials`` should be updated:

.. image:: /img/oauth2-service/site-admin.*
   :alt: Image showing updated information.
   
Your ODK Aggregate server is now configured to support publishing of data to Google Spreadsheets and Google Fusion Tables.

.. tip::

  If your publishers seems to be stalled in an Active Paused or Paused state, this is most likely caused by exceeding Google's quota limits. See :ref:`this section <api-request>` for how to navigate to a pop-up from which you can request a quota limit increase.
