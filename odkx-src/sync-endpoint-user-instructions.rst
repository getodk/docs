.. spelling::
  ldap
  phpLDAPadmin
  readonly
  dns
  letsencrypt
  subdomain


Users and Groups
=================

A user needs to be assigned to a group within ODK-X sync-endpoint to set their permissions and roles for ODK-X apps. More information about groups and the roles is available in :ref:`Data Permission Filters<data-permission-filters>` section.


.. _sync-endpoint-ldap-users: .. _sync-endpoint-setup-create-user:

Creating users
--------------------

  1. Click: :guilabel:`login` on the left and login as *admin*.
      | Start by logging into the ldap-service. Copy the login below.
      |  - login DN: :guilabel:`cn=admin,dc=example,dc=org`
      |  - password: :guilabel:`admin`

    .. image:: /img/setup-create-user/setup-user1.png
      :width: 600

  2. Expand the tree view on the left until you see :guilabel:`ou=people`.
     Click the :guilabel:`+` sign next to **dc=example, dc=org** to expand it. Within the unfolded menu, in the **ou=people** section, click on :guilabel:`Create a child entry` (new person).

    .. image:: /img/setup-create-user/setup-user2.png
      :width: 600

  3. Then, select the :guilabel:`Generic: User Account` template.

    .. image:: /img/setup-create-user/setup-user3.png
      :width: 600

  4. Fill out information for the new user and “create object.” Assign it to the *default_prefix_synchronize_tables* group. Will need to commit (confirm) that you want to create this entry on the next screen.

    .. image:: /img/setup-create-user/setup-user4.png
      :width: 600

    We have now created the user! We just need to add the user to the respective group from the group settings.


.. _sync-endpoint-ldap-groups:

Creating groups
-------------------

  1. Click: :guilabel:`login` on the left and login as *admin*.
  2. Expand the tree view on the left until you see :guilabel:`ou=groups`.
  3. Click on :guilabel:`ou=default_prefix` and choose :guilabel:`Create a child entry`.
  4. Choose the :guilabel:`Generic: Posix Group` template.
  5. Fill out the form and click :guilabel:`Create Object`.

  .. note::

    The group name must start with the group prefix, in this case the group prefix is *default_prefix* so for example: *default_prefix my-new-group*

  6. Assign users to groups with :ref:`these instructions <sync-endpoint-ldap-assign>`.



.. _sync-endpoint-ldap-assign:

Assigning users to groups
-------------------------

  1. Click: :guilabel:`login` on the right and login as *admin*.
  2. Expand the tree view on the right until you see :guilabel:`ou=default_prefix`, then expand :guilabel:`ou=default_prefix`.
  3. This list is all the groups under *ou=default_prefix*.
  4. Click on the group that you want to assign users to. In this section, click on :guilabel:`gidNumber=503`, which is the group ID that corresponds to *default_prefix_synchronize_tables*. Groups correspond to the access permissions available to a certain user.

    .. image:: /img/setup-create-user/setup-user5.png
      :width: 600

  5. A few groups are created when the LDAP server is brought up, refer to :doc:`data-permission-filters` for descriptions of these groups.

   .. note::

     A user needs to be assigned one of the roles in addition to any other group of your choosing. These roles are available as groups 500 (Row owner), 501 (Group read only), 502 (Group modify), 503 (Group privileged).


  6. Assign users to groups with :ref:`these instructions <sync-endpoint-ldap-assign>`.
  7. If the :guilabel:`memberUid` section is not present:

      a. Choose :guilabel:`Add new attribute`.
      b. Choose :guilabel:`memberUid` from the dropdown, then enter :guilabel:`uid` of the user you want to assign.
      c. Click :guilabel:`Update Object` at the bottom to update.

  8. If the :guilabel:`memberUid` section is present,

    a. Navigate to the :guilabel:`memberUid` section.
    b. Click modify group members to manage members.

    .. image:: /img/setup-create-user/setup-user6.png
      :width: 600

    .. image:: /img/setup-create-user/setup-user7.png
      :width: 600

  9. Navigate to http://[IP_ADDRESS]/web-ui/login in order to access the login screen.

    .. image:: /img/setup-create-user/setup-user8.png
      :width: 600
