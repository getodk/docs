.. spelling::
  rw
  rwd
  rwdp
  defaultAccessOnCreation
  unverifiedUserCanCreate

Data Permission Filters
========================

.. _data-permission-filters:

.. _data-permission-filters-limitations:

Limitations
----------------------------

Traditional access control frameworks provide strong protections for data and the management of which users can modify that data. The permission filtering introduced in ODK 2.0 is weaker. When syncing devices with the server, all data rows for all data tables are currently synced and shared across all devices. Every device gets a full copy of all data. Permission filtering enables a supervisor to restrict the visibility of that data and to manage who can modify or delete the data through the programmatic means provided by the ODK 2.0 tools.

This is weaker than traditional access control frameworks in that application designers can:

  - Circumvent via software. There are specific ways in which application designers can write their applications to defeat these filters. When those mechanisms are not employed, permission filtering provides equivalent policy enforcement to that of a traditional access control framework.
  - Circumvent via external access. The data and attachments are stored as plaintext on the device. Anyone can copy this data off of the device and access it, or write their own apps and directly modify it.

It is important to understand these limitations when designing your applications.

.. _data-permission-filters-overview:

Overview
-------------

By default, all tables can be altered by all users.

The ODK 2.0 data access filtering mechanism relies on five interacting features:

  - Verified user identities
  - Verified user capabilities
  - Table-level security configuration (whether data in the table can be modified by unprivileged users).
  - Row-level access filters (to specify whether a row is visible to a given user, whether the user can modify the row's data value, and whether the user can change this row's access filters).
  - Sync status of the individual row.

.. _data-permission-filters-verified-user-identities:

Verified User Identities
-----------------------------

Enforcing restrictions on who can see or modify data requires that the identity of the user has been verified.

When configuring the :guilabel:`Server Settings`, any changes to any of the settings (such as the server URL, type of credential (or anonymous access), username, password or Gmail account) will clear any prior user identity and capability information and flag the user identity as unverified.

When leaving the :guilabel:`Server Settings` screen, a user-verification screen will then be presented (unless no server sign-on credential is specified, in which case anonymous access to the server will be attempted):

.. image:: /img/data-permission-filters/verify-user.*
  :alt: Verify User Screen
  :class: device-screen-vertical

Clicking the :guilabel:`Verify User Permissions` button on this screen will initiate a series of requests to the configured server. These requests verify that the server URL is correct, that the server works with this application name, and then verify the server sign-on credential that has been configured on the :guilabel:`Server Settings` page.

.. warning::

  If the server sign-on credential is rejected, the user identity will be flagged as unverified and any further interactions on the device will be performed as if by an anonymous user.

.. _data-permission-filters-verified-user-capabilities:

Verified User Capabilities
--------------------------------

As part of the user-verification process, once the user's identity has been verified, the list of groups to which this user belongs and the capabilities (roles) assigned to that user are downloaded from the server. These are cached on the device for use during data access filtering until the user logs out of the ODK 2.0 tools on the device or a different server sign-on credential is specified.

For the purposes of the data access filtering mechanism, there are 4 user capabilities of interest:

  - **ROLE_USER** -- a user who is able to verify their identity.
  - **ROLE_SYNCHRONIZE_TABLES** -- a user who is able to execute the sync protocol.
  - **ROLE_SUPER_USER_TABLES** -- a privileged user who can edit all rows, change how rows are visible, and change who has special permission to edit a given row.
  - **ROLE_ADMINISTER_TABLES** -- a privileged user who can :guilabel:`Reset App Server` and who can edit all rows, change how rows are visible, and change who has special permission to edit a given row.

The first two of these identify users that are unprivileged. These users may be granted privileges to individual rows by being designated the owner of that row or through their membership in one or more user groups identified in the row's access filter columns.

The second two of these identify privileged users that have full control of the device. Additionally, the last of these capabilities (**ROLE_ADMINISTER_TABLES**) identifies a user that can alter the configuration of the Cloud Endpoint.

Application designers that wish to restrict access by unverified users or manage anonymous access to the server can further restrict table and row access in these scenarios.

.. _data-permission-filters-row-access-filter-cols:

Row Access Filter Columns
--------------------------------

Management of which unprivileged users can see, modify or manage access to a given row is controlled through five access filter columns. The first of these columns specifies the access to the row that is granted to all unprivileged users. The second identifies the owner of this row. Row owners have modify privileges on a row. The other three are either null or specify a user group that is granted that specific access right:

  - **_DEFAULT_ACCESS** -- one of :tc:`HIDDEN`, :tc:`READ_ONLY`, :tc:`MODIFY` or :tc:`FULL`.
  - **_ROW_OWNER** -- this user has :tc:`FULL` privileges on this row.
  - **_GROUP_READ_ONLY** -- a user who is a member of this group will be able to read this row of data
  - **_GROUP_MODIFY** -- a user who is a member of this group will be able to read and modify this row of data but not delete it.
  - **_GROUP_PRIVILEGED** -- a user who is a member of this group will be able to read, modify, delete and change privileges on this row of data.

.. note::

  Privileged users are not governed by these settings -- they have unlimited access to all tables on the device.

Individual users can belong to any number of groups, enabling arbitrarily complex row-level access management. Users may also be assigned a default group. Management of group memberships is dictated by the server being used. Refer to the :doc:`cloud-endpoints-intro` for the capabilities of the different servers. More detail will be given regarding these filter columns in the :ref:`Row-level Access Filters <data-permission-filters-row-access-filters>` section.

.. _data-permission-filters-obtaining-roles:

Obtaining a User's Groups and Roles
----------------------------------------

Inside ODK Survey and ODK Tables web pages, the groups and roles of the current verified user are available in JavaScript via the API:

.. code-block:: javascript

  odkData.getRoles(function(result) {
    var roles = result.getRoles();
    // roles is an array of capabilities granted to the verified user.
    // It will be null for anonymous and unverified users.
  }, function(errorMsg) {
    // error handler
  });

.. _data-permission-filters-obtaining-default-group:

Obtaining a User's Default Group
---------------------------------------

Inside ODK Survey and ODK Tables web pages, the default group of the current verified user is available in JavaScript via the API:

.. code-block:: javascript

  odkData.getDefaultGroup(function(result) {
    var defaultGroup = result.getDefaultGroup();
    // defaultGroup is null or a string
  }, function(errorMsg) {
    // error handler
  });


.. note::

  Default groups are not directly used within the ODK 2.0 framework. These are provided for use by an application designer when crafting their application.

.. _data-permission-filters-obtaining-other-info:

Obtaining Information About Other Users
------------------------------------------------

Whenever the server is contacted to verify a user's identity, if the user is determined to be a privileged user, the server will, additionally, provide a list of all users configured on the server and all of the groups and roles assigned to those users. This list can be useful when performing task assignments via assigning row ownership.

This list will contain entries of the form:

.. code-block:: javascript

  {
    user_id: "verified_identity_token",
    full_name: "content of the Full Name field on the server",
    default_group: "default group of the user"
    roles: [...]
  }

The *Full Name* field on the server (on the :menuselection:`Site Admin -->  Permissions` sub-tab) is provided here to allow super-users and administrators to select people by *name*. *user_id* should be stored in the :th:`_ROW_OWNER` column to assign ownership to this user. The list of roles (and groups) is provided to allow super-users and administrators to choose users based upon their capabilities.

If the user has been assigned to a default group it will be provided.  Default groups are not directly used within the ODK 2.0 framework. These are provided for use by an application designer when crafting their application.

Inside ODK Survey and ODK Tables web pages, the list of all configured users is available in JavaScript via the API:

.. code-block:: javascript

  odkData.getUsers(function(result) {
    var users= result.getUsers();
    // users is an array of the above objects.
    // It will be null for anonymous and unverified users.
    // It will be a singleton list if the user lacks permissions.
  }, function(errorMsg) {
    // error handler
  });

.. _data-permission-filters-table-security-config:

Table-level Security Configuration
-------------------------------------------

As mentioned earlier, by default, all tables can be altered by all users.

Data permission filtering introduces the notion of a *locked* table. Only super-users and administrators can create and delete rows in locked tables. Anonymous, unverified, or ordinary users are unable to do so.

A table property is used to specify that a table is *locked.*

Two other table properties control the creation of a row. The first property specifies whether an anonymous or unverified user can create a row in the table (this only applies if a table is not *locked;* it has no effect if the table is *locked*, since row creation is prohibited for all but super-users and administrators). The second property specifies the type of row-level access filter to assign to this newly-created row. Row-level access settings are covered more completely in the :ref:`following section <data-permission-filters-row-access-filters>`.

These three table properties can be specified in the properties sheet of the XLSX file. If they are not specified, the default values for these three properties are:

.. list-table::
  :header-rows: 1

  * - partition
    - aspect
    - key
    - type
    - value
  * - Table
    - security
    - locked
    - boolean
    - false
  * - Table
    - security
    - unverifiedUserCanCreate
    - boolean
    - true
  * - Table
    - security
    - defaultAccessOnCreation
    - string
    - FULL

.. _data-permission-filters-row-access-filters:

Row-level Access Filters
-----------------------------------

Control of who can see, modify, or delete an individual row is governed by the row-level access filter columns of that row and that row's sync status. As described earlier in this page, these filters are stored in the row itself under the :th:`_default_access`, :th:`_row_owner`, :th:`_group_read_only`, :th:`_group_modify`, and :th:`_group_privileged` metadata columns. The sync status of the row is also stored in the row itself under the :th:`_sync_state` metadata column.

Row-level access will always be one of:

  - Not visible
  - **r** -- Read-only access to the row
  - **rw** -- Read and modify access to the row. Deletion is not allowed. Modification of the row-level access filter columns is not allowed.
  - **rwd** -- Read, modify and delete access to the row. Modification of the row-level access filter columns is not allowed.
  - **rwdp** -- Read, modify and delete access, plus the ability to modify the row-level access filter columns.

The rules for the row-level access filter are as follows (stop at the first rule that applies):

  1. Super-users and administrators have full read/write/delete(rwd) capabilities on all rows, regardless of their row-level access filters and independent of the table's *locked* status. These privileged users also have the ability to change the row-level access filter column values (ordinary users cannot).

    .. list-table::
      :header-rows: 1

      * - User Capability
        - unlocked table
        - *locked* table
      * - ROLE_SUPER_USER_TABLE
        - rwdp
        - rwdp
      * - ROLE_ADMINISTER_TABLE
        - rwdp
        - rwdp

  2. If a row has not yet been synced to the server, the current user has full read/write/delete (rwd) capabilities on that row. This includes the anonymous and unverified users and is independent of the table's *locked* status.

    .. list-table::
      :header-rows: 1

      * - _sync_state
        - unlocked table
        - *locked* table
      * - new_row
        - rwd
        - rwd

  3. If the :th:`_row_owner` column contain the user_id of the current user, then this user has full read/write/delete (rwd) capability on this row or, for *locked* tables, can modify the row (but cannot delete it).

    .. list-table::
      :header-rows: 1

      * - _row_owner
        - unlocked table
        - *locked* table
      * - user_id of current verified user
        - rwd
        - rw

  4. If the user is a member of one the following groups, their corresponding privileges are shown below.

    .. list-table::
      :header-rows: 1

      * - group columns
        - unlocked table
        - *locked* table
      * - _group_privileged
        - rwdp
        - rwdp
      * - _group_modify
        - rw
        - r
      * - _group_read_only
        - r
        - r

  5. Otherwise, row-level access is governed by the _default_access column and whether or not the table is locked, as follows:

    .. list-table::
      :header-rows: 1

      * - _default_access
        - unlocked table
        - *locked* table
      * - FULL
        - rwd
        - r
      * - MODIFY
        - rw
        - r
      * - READ_ONLY
        - r
        - r
      * - HIDDEN
        - not visible
        - not visible

.. note::

  :th:`_row_owner` can be null or any arbitrary placeholder string. If you use placeholder strings, it is recommended that they not begin with *username:* or *mailto:* or be *anonymous* to prevent any possible collisions with existing usernames. Placeholder strings might be useful in workflows to designate queues of unassigned-work.

Super-users and administrators can update the row-level access filters via the JavaScript API:

.. code-block:: javascript

  odkData.changeAccessFilterOfRow(tableId, defaultAccess, rowOwner, groupReadOnly,
    groupModify, groupPrivileged, rowId,
    function(result) {
      // success outcome
      // result holds the result set: SELECT * FROM tableId WHERE _id = "rowId"
    },
    function(error) {
      // error handler
    });

Alternatively, super-users and administrators can also use the :code:`updateRow` API.

Ordinary users will receive a not-authorized error if they attempt to set any of these metadata fields (even if the values they set are unchanged from the current values of those fields).

.. _data-permission-filters-hidden-filter:

Implementation of the HIDDEN filter on queries
-----------------------------------------------------

When a SQL query is processed inside the ODK Services layer, it is first examined to see if the result set contains the columns :th:`_sync_state`, :th:`_default_access`, :th:`_row_owner`, :th:`_group_read_only`, :th:`_group_modify`, and :th:`_group_privileged`. If it contains all six columns, then the query is wrapped with a :code:`where` clause to exclude hidden rows and that, in turn, is wrapped by whatever :code:`limit` and :code:`offset` you have specified for the query.

.. warning::

  If you issue a query that omits one or more of these six columns from the result set, then no :tc:`HIDDEN` filtering will be applied. This is one way to circumvent data permission filtering in software -- by crafting queries that omit one or more of these fields.

  For example, queries that return the maximum value in a field:

  .. code-block:: sql

    SELECT MAX(crop_height) as max_height FROM crop_plantings

  Would return the maximum crop height across all crop planting -- even if the current user only had access to the crop height data for their own plantings (and the crop information from other farms was hidden from them).

  If you want to restrict such calculations to just the data visible to the current user, you must manually construct the query to do so. This would be the revised query:

  .. code-block:: sql

    SELECT MAX(crop_height) as max_height FROM crop_plantings WHERE _default_access != ? or _row_owner = ? bind parameters = [ "HIDDEN", odkCommon.getActiveUser() ]

.. _data-permission-filters-effective-access:

Effective Access
-----------------------

As mentioned above, when a SQL query is processed inside the ODK Services layer, it is first examined to see if the result set contains the columns :th:`_sync_state`, :th:`_default_access`, :th:`_row_owner`, :th:`_group_read_only`, :th:`_group_modify`, and :th:`_group_privileged`. If it contains all six columns, then a synthesized column, :th:`_effective_access` is added to the result set. That column returns one of *r*, *rw*, *rwd*, or *rwdp* (with the *p* indicating that a user can change permissions for the row as well) to indicate the level of access the current user has on the rows in the result set.

Additionally, once a result set is returned for a given table, you can determine whether the current user can create new rows on the table by calling :code:`getCanCreateRow`

.. code-block:: javascript

  odkData.query(tableId, whereClause, sqlBindParams, groupBy, having,
                orderByElementKey, orderByDirection, limit, offset, includeKVS,
  function(result) {
    // success outcome
    // result holds the result set. Assume this has at least one row.
    // obtain the effective access for the first row in the result set
    // this will be one of "r", "rw", "rwd", or "rwdp"
    var effectiveAccess = result.getData(0, "_effective_access");
    // obtain the boolean indicating whether the current user can
    // create new rows in this tableId.
    var ableToCreate = result.getCanCreateRow();
  },
  function(error) {
    // error handler
  });

.. _data-permission-filters-usage:

Usages Within Applications
--------------------------------

Consider a workflow application where a first group of field agents create work requests, those requests are then sent to a supervisor who assigns them to a different set of field agents for processing.

In this case, you might configure a work_requests table to create rows with a :tc:`HIDDEN` default access (via :code:`defaultAccessOnCreation`). Then create a form for opening work requests.

The first group of agents (ordinary users) uses that form to create new work requests. Each agent would only see the work requests they themselves create because all other rows in that table would be hidden due to the :th:`_default_access` being :tc:`HIDDEN` and due to their being ordinary users.

After the field worker in the first group syncs to the server, and the supervisors sync to the server, the set of work requests the field worker created will have become available on the supervisors' devices. The supervisor (a super-user or administrator) can then see and change the :th:`_row_owner` on each work request to one of the field agents in the second group.

When the supervisor syncs to the server, and then the field agent in the second group (another ordinary user) syncs to the server, that field agent will see the work items that have been assigned to them (and they will not see any other work items because they are ordinary users of the system).

When the agent in the first group next syncs, their created work item will disappear from their view because it is :tc:`HIDDEN` and the :th:`_row_owner` no longer matches this field agent's verified user id (it was assigned to the second agent).

Upon completion of the task and after syncing to the server, after the supervisor next syncs, the supervisor could then change the :th:`_row_owner` to null or to a special placeholder value to remove it from the second agent's list of work items (and that removal would occur when that second agent next syncs with the server after the supervisor syncs his :th:`_row_owner` change).

.. _data-permission-filters-usage-example:

Example Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app designer has a row-level access demo using the *geoweather* and *geoweather_conditions* tables and forms.

.. note::

  This demo only works on the device.

To install the demo on the device:

  #. Force close all the apps.
  #. Delete the :file:`/sdcard/opendatakit/default/` directory on the device.
  #. From the app designer, execute

    .. code-block:: console

      $ grunt adbpush-tables-rowlevelaccessdemo

  #. Start ODK Survey and exit it.
  #. Start ODK Tables.

You will be presented with a demo launch screen.

At this point, all the rows in all the tables have a :th:`_sync_state` of :tc:`new_row` and are fully editable and deletable. The demo will not become interesting until you set up and sync with a server.

Set up an ODK Cloud Endpoint or ODK Aggregate 1.4.15 server with 2 ordinary users, 1 super-user and 1 tables administrator. :guilabel:`Reset App Server` to push the configuration and data up to the server.

You are now an administrator (you needed to be in order to reset the server). You can choose :guilabel:`Change Row-Level Access Filters` to view and perhaps modify the default access and row owner of one or more rows. All rows in all tables are fully editable and deletable.

Now, change your :guilabel:`Server Settings` to one of the ordinary users (a username other than *olive* or *sue*). Notice that the list of conditions from the *geoweather_conditions* table no longer contains the *Light Rain* option. That was hidden and will only be visible to a username of "olive" or a super-user or administrator.

Use the table display on the :guilabel:`Change Row-Level Access Filters` page to examine what the :th:`_effective_access` for each row is in the various tables and verify that those settings are enforced.

Change your :guilabel:`Server Settings` to different users to see how their effective accesses change.
