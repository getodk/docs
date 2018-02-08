Connecting to a Google Drive Account
=======================================
    
1. From the Action Button (:guilabel:`⋮`), select :menuselection:`General Settings`

   .. image:: /img/collect-connect/main-menu-highlight-kebab.* 
     :alt: The Main Menu screen of the Collect app. The three-dot 'kebab' menu in the upper-right corner is circled in red. 

   .. image:: /img/collect-connect/kebab-menu-general-settings.* 
     :alt: The Main Menu screen of the Collect App. A modal menu has unrolled in the top-right corner, with the option *About*, *General Settings*, and *Admin Settings*. *General Settings* is circled in red.

2. Select :guilabel:`Server`

   .. image:: /img/collect-connect/general-settings-server.* 
     :alt: The General Settings menu in the Collect app. The options are *Server*, *User Interface*, *Form management*, and *User and device identity*. *Server* is circled in red.

3. Select :guilabel:`Type`, and set it to :menuselection:`Google Drive, Google Sheets`

   .. image:: /img/collect-connect/server-settings-type-google.* 
     :alt: The Server Settings screen in the Collect app. The first item in the menu is labeled *Type*, and this item is circled in red.

   .. image:: /img/collect-connect/server-settings-type-model-google.* 
     :alt: The Server Settings screen in the Collect App, as displayed in the previous image. There is now a modal menu labeled *Platform*, with single-select radio buttons for: *ODK Aggregate*, *Google Drive, Google Sheets*, and *Other*. *Google Drive, Google Sheets* is selected and circled in red.

4. Select your :guilabel:`Google Account`. You can select any account which is already linked with your device or add a new account as well.

   .. image:: /img/collect-connect/server-settings-google-account.* 
     :alt: The Server Settings screen in the Collect app. Below the *Type* setting is a section titled *Google Sheets settings*, with items for *Google Account* and *Fallback submission URL*. *Google Account* is circled in red.

   .. image:: /img/collect-connect/server-settings-google-account-modal.* 
     :alt: The Server Settings screen as displayed in the previous image. There is now a modal labeled *Google account,* with a set of radio button (single select) options. The options are Google Accounts associated with the device, and a final option labeled 'Add account'. Below that are buttons labeled CANCEL and OK.

  
5. **Optional:** Set a :guilabel:`Fallback submission URL`

   When using Collect with a Google account, form submissions will be posted to a Google Sheet specified in the form. 

   You have the option to specify a :guilabel:`Fallback submisison URL`. This is the URL of a Google sheet to which form submissions will be posted if the submitted form does not specify its own URL.

   If your forms will specify a submission URL, you can leave this setting empty. Otherwise, enter the URL of a Google sheet you would like to use.    
