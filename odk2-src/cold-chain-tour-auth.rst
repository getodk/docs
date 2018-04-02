Authentication
==========================

.. image:: /img/cold-chain-tour/cold-chain-auth-needed.*
  :alt: Authentication Requested
  :class: device-screen-vertical side-by-side

.. image:: /img/cold-chain-tour/cold-chain-auth-enter.*
  :alt: Authentication Screen
  :class: device-screen-vertical side-by-side

.. _cold-chain-tour-auth-function:

Function
-----------------------

The Authentication screen is the gateway to the Cold Chain application. The application filters data and restricts access based on the authenticated user's group and assigned permissions. Therefore a user with a recognized set of permissions must be authenticated before the Cold Chain application can be used, and the application will lock itself until that condition is met.

The application checks the authenticated user's credentials at startup, so if a valid user is already logged in, this screen will be completely bypassed. If not, the screen shown to the left above is shown. When you press the :guilabel:`Log In` button, the *Change User* screen is directly launched. This allows you to authenticate as your desired user. After you have authenticated, you can press back until you return to the Cold Chain application. The same authentication check will occur, and either valid credentials will be found or the same Authentication screen will be shown.

If the authenticated user is an administrator, the :doc:`cold-chain-tour-admin` will be shown. If the authenticated user is a normal data synchronizer assigned to a valid group, the appropriate :doc:`cold-chain-tour-regions` screen will be shown.

.. _cold-chain-tour-auth-implementation:

Implementation
----------------------

This screen is the first view launched when the application is opened, which means it must start with :file:`assets/index.html`. This contains only few :code:`<div>` elements that will be filled in by :file:`assets/js/menu.js`. This file also makes use of the library: :file:`assets/js/util.js`.

The Cold Chain application supports both English and Spanish locales, and the first thing :file:`index.html` does is check the current locale, and use it to localize text throughout the page with the API :code:`odkCommon.getPreferredLocale()` and :code:`odkCommon.localizeText(...)`.

Next the JavaScript checks for a query parameter in the URL. Throughout this application arguments and query parameters will be passed across files as URL parameters. However, since this is the first launch, this argument will be null, which will trigger the check for the user's default group: :code:`odkData.getDefaultGroup(...)`.

Depending on the returned default group, the next action is:

  - *Valid Group*: the corresponding :doc:`cold-chain-tour-regions` page is shown.
  - *Table Administrator*, the :doc:`cold-chain-tour-admin` page is shown.
  - *Null*: the user is either anonymous or has not been set up with a default group. The user is prompted to authenticate with a different identity.
  - *Anything else*: The user does not have privileges within this application and is prompted to authenticate with a different identity.

In either of the bottom two options, the log in screen is shown. The :guilabel:`Log In` button launches an intent to the log in screen of ODK Services. The API :code:`odkCommon.doAction(...)` takes the intent as an argument, which should be pointed at the *SyncActivity*. To specifically get the log in screen the bundle should include the *showLogn* value set to *true*.

When the user returns from authentication this process will repeat until a *Valid Group* or a *Table Administrator* is found.

.. _cold-chain-tour-auth-implementation-files:

Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

  - :file:`assets/index.html`
  - :file:`assets/js/menu.js`
  - :file:`assets/js/util.js`

.. _cold-chain-tour-auth-implementation-forms:

Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~

None

.. _cold-chain-tour-auth-implementation-tables:

Database Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~

None


