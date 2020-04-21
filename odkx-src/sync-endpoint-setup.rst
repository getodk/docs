.. spelling::
  phpLDAPadmin
  readonly

ODK-X Sync Endpoint Setup
=========================

.. _sync-endpoint-intro:

:dfn:`ODK-X Sync Endpoint` is an implementation of :doc:`cloud-endpoints-intro`. It runs a server inside a :program:`Docker` container that implements the `ODK-X REST Protocol <https://github.com/odk-x/odk-x/wiki/ODK-2.0-Synchronization-API-(RESTful)>`_.

It communicates with your ODK-X Android applications to synchronize
your data and application files.

Depending on your needs, ODK-X Sync Endpoint can either be installed
in a cloud-based virtual machine, or on your own infrastructure.

- :ref:`Cloud-based Setup<sync-endpoint-cloud-setup>`
- :ref:`Manual Setup (on local infrastructure)<sync-endpoint-manual-setup>`

.. _sync-endpoint-auth:

Authentication
--------------

ODK-X Sync Endpoint does not store user information in its own database, instead it integrates with an *LDAP* directory or an *Active Directory*. That directory is then used to authenticate users and obtain user roles.

.. note::

  As a consequence of the integration, Basic Authentication is the only supported authentication method.


.. include:: sync-endpoint-cloud-setup.rst

.. include:: sync-endpoint-manual-setup.rst


.. _sync-endpoint-https:

HTTPS
-----

  The Sync Endpoint stack integrates support for automatic certificate
  provisioning via domain validation and letsencrypt. For most use
  cases this should be sufficient. Certificate provisioning parameters
  can be edited interactively during initialization or directly in
  :file:`config/https.env`.

  .. Tip:: For advanced users, if you would like to use an externally
           provisioned certificate one can be added by modifying the
           cert-bootstrap service in :file:`docker-compose-https.yml`
           to pull from the appropriate external files. Additionally
           docker's builtin secrets and config infrastructure can be
           used directly to expose the certificate and key only to the
           NGINX container.

.. _sync-endpoint-ldap:

LDAP
----

  - The default admin account is  *cn=admin,dc=example,dc=org*.
  - The default password is *admin* - it can be changed with the *LDAP_ADMIN_PASSWORD* environment variable in :file:`ldap.env`

  - The default readonly account is *cn=readonly,dc=example,dc=org*.
  - The default password is *readonly* - it can be changed with the *LDAP_READONLY_USER_PASSWORD* environment variable in :file:`ldap.env`. This account is used by the Sync Endpoint to retrieve user information.

The LDAP directory that you deployed with the instructions above is an :program:`OpenLDAP` server. In addition to the directory, a :program:`phpLDAPadmin` server is also deployed to help you configure the directory.

If you'd prefer to use the :program:`OpenLDAP` command line utilities, they're installed in the OpenLDAP container. These tools are accessible with this command:

  - Linux/macOS:

  .. code-block:: console

    $ docker exec $(docker ps -f "label=com.docker.swarm.service.name=syncldap_ldap-service" --format '{{.ID}}') LDAPTOOL ARGS

  - Windows:

  .. code-block:: console

    $ docker exec (docker ps -f "label=com.docker.swarm.service.name=syncldap_ldap-service" --format '{{.ID}}') LDAPTOOL ARGS

.. note::

  The phpLDAPadmin server listens on port 40000, it is important that you do not expose this port to the internet.

The following guides assume that you're using :program:`phpLDAPadmin`. In order to perform the following operation, please go to https://127.0.0.1:40000 in your browser.

.. _sync-endpoint-ldap-users:

Creating users
~~~~~~~~~~~~~~

  1. Click: :guilabel:`login` on the left and login as *admin*.
  2. Expand the tree view on the left until you see :guilabel:`ou=people`.
  3. Click on :guilabel:`ou=people` and choose :guilabel:`Create a child entry`.
  4. Choose the :guilabel:`Generic: User Account` template.
  5. Fill out the form and click :guilabel:`Create Object`.
  6. Assign users to groups with :ref:`these instructions <sync-endpoint-ldap-assign>`.

.. _sync-endpoint-ldap-groups:

Creating groups
~~~~~~~~~~~~~~~

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
"""""""""""""""""""""""""

  1. Click: :guilabel:`login` on the right and login as *admin*.
  2. Expand the tree view on the right until you see :guilabel:`ou=default_prefix`, then expand :guilabel:`ou=default_prefix`.
  3. This list is all the groups under *ou=default_prefix*.
  4. Click on the group that you want to assign users to.
  5. A few groups are created when the LDAP server is brought up, refer to :doc:`data-permission-filters` for descriptions of these groups.
  6. If the :guilabel:`memberUid` section is not present:

      a. Choose :guilabel:`Add new attribute`.
      b. Choose :guilabel:`memberUid` from the dropdown, then enter :guilabel:`uid` of the user you want to assign.
      c. Click :guilabel:`Update Object` at the bottom to update.

  7. If the :guilabel:`memberUid` section is present,

    a. Navigate to the :guilabel:`memberUid` section.
    b. Click modify group members to manage members.
