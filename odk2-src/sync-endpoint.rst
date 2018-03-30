.. spelling::
  phpLDAPadmin
  readonly

ODK Sync Endpoint
=====================

.. _sync-endpoint-intro:

:dfn:`ODK Sync Endpoint` is an implementation of :doc:`cloud-endpoints-intro`. It runs a server inside a :program:`Docker` container that implements the `ODK 2 REST Protocol <https://github.com/opendatakit/opendatakit/wiki/ODK-2.0-Synchronization-API-(RESTful)>`_.

It communicates with your ODK 2 Android applications to synchronize your data and application files.

.. _sync-endpoint-auth:

Authentication
----------------------

ODK Sync Endpoint does not store user information in its own database, instead it integrates with an *LDAP* directory or an *Active Directory*. That directory is then used to authenticate users and obtain user roles.

.. note::

  As a consequence of the integration, Basic Authentication is the only supported authentication method.

.. _sync-endpoint-prereqs:

ODK Sync Endpoint prerequisites
-----------------------------------

You must have :program:`Docker 17.06.1` or newer, and be running in *Swarm Mode*.
Follow these links for detailed instructions on installing :program:`Docker` and enabling Swarm Mode.

  - `Docker <https://docs.docker.com/install/>`_
  - `Swarm Mode <https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/>`_

.. _sync-endpoint-setup:

ODK Sync Endpoint Setup
----------------------------

ODK Sync Endpoint requires a database and a *LDAP* directory, you could follow the instructions and deploy all three components together or supply your own database and/or *LDAP* directory.

.. note::

  All of the following command should be run on your server

Setup instructions:

  1. Choose a directory to store you endpoint in. In that directory, run:

  .. code-block:: console

    $ git clone https://github.com/opendatakit/sync-endpoint-default-setup

  2. Then run:

  .. code-block:: console

    $ docker build --pull -t odk/sync_endpoint https://github.com/opendatakit/sync-endpoint-containers.git

  3. Then run:

  .. code-block:: console

    $ docker build --pull -t odk/sync-web-ui https://github.com/opendatakit/sync-endpoint-web-ui.git

  4. In the cloned repository,

  .. code-block:: console

    $ docker build --pull -t odk/db-bootstrap db-bootstrap

  5. In the cloned repository,

  .. code-block:: console

    $ docker build --pull -t odk/openldap openldap

  6. In the cloned repository,

  .. code-block:: console

    $ docker build --pull -t odk/phpldapadmin phpldapadmin

  7. Enter your hostname in the :code:`security.server.hostname` field in the :file:`security.properties` file.

  8. If you're not using the standard ports (80 for *HTTP* and 443 for *HTTPS*) enter the ports you're using in the :code:`security.server.port` and :code:`security.server.securePort` fields in the :file:`security.properties`. Then edit the **ports** section under the **sync** section in :file:`docker-compose.yml` to be :code:`YOUR_PORT:8080`.

    .. note::

      It is important that the right side of the colon stays as 8080. This is the internal port that the web server is looking for.

  9. If you're using your own *LDAP* directory or database, continue with the instructions:

    - :ref:`Custom database instructions <sync-endpoint-setup-database>`
    - :ref:`Custom LDAP instructions <sync-endpoint-setup-ldap>`

  10. In the cloned repository:

  .. code-block:: console

    $ docker stack deploy -c docker-compose.yml syncldap

  11. The server takes about 30s to start, then it will be running at http://127.0.0.1.
  12. See the :ref:`LDAP section <sync-endpoint-ldap>` for instructions on configuring users and groups.

.. _sync-endpoint-setup-database:

Custom database
~~~~~~~~~~~~~~~~~~~~~~

  1. If you haven't followed the :ref:`common instructions <sync-endpoint-setup>`, start with those.
  2. Remove the *db* and *db-bootstrap* sections in :file:`docker-compose.yml`.
  3. Modify :file:`jdbc.properties` to match your database. Supported database systems are :program:`PostgreSQL`, :program:`MySQL` and :program:`Microsoft SQL Server`. Sample config for each type of database can be found `on Github <https://github.com/opendatakit/sync-endpoint-default-setup>`_.
  4. Modify :file:`sync.env` to match your database
  5. In the cloned repository,

  .. code-block:: console

    $ docker stack deploy -c docker-compose.yml syncldap

  6. The server takes about 30s to start, then it will be running at http://127.0.0.1.

.. _sync-endpoint-setup-ldap:

Custom LDAP directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1. If you haven't followed the :ref:`common instructions <sync-endpoint-setup>`, start with those.
  2. OPTIONAL: If your LDAP directory uses a certificate that was signed by a self-signed CA,

    a. Make the public key of the CA available to ODK Sync Endpoint with this command.

    .. code-block:: console

      $ docker config create org.opendatakit.sync.ldapcert PATH_TO_CERT

    b. Uncomment the relevant lines in the *configs* section in :file:`docker-compose.yml` and the *configs* section under the *sync* section in :file:`docker-compose.yml`.

  3. Remove the *ldap-service* and *phpldapadmin* sections in :file:`docker-compose.yml`.
  4. Modify the relevant sections in :file:`security.properties` to match your LDAP directory. Further instructions are in the file.

  .. note::

    The default configuration does not use ldaps or StartTLS because the LDAP directory communicates with the ODK Sync Endpoint over a secure overlay network. You should use ldaps or StartTLS to communicate with your LDAP directory.

  5. In the cloned repository:

  .. code-block:: console

    $ docker stack deploy -c docker-compose.yml syncldap

  6. The server takes about 30s to start, then it will be running at http://127.0.0.1.

.. _sync-endpoint-stopping:

Stopping ODK Sync Endpoint
-------------------------------

  1. Run:

  .. code-block:: console

    $ docker stack rm syncldap

  2. OPTIONAL: If you want to remove the volumes as well,

    - Linux/macOS:

    .. code-block:: console

      $ docker volume rm $(docker volume ls -f "label=com.docker.stack.namespace=syncldap" -q)

    - Windows:

    .. code-block:: console

      $ docker volume rm (docker volume ls -f "label=com.docker.stack.namespace=syncldap" -q)

.. _sync-endpoint-ldap:

LDAP
-----------

  - The default admin account is *cn=admin,dc=example,dc=org*.
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

The following guides assume that you're using :program:`phpLDAPadmin`.

.. _sync-endpoint-ldap-users:

Creating users
~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Click: :guilabel:`login` on the right and login as *admin*.
  2. Expand the tree view on the right until you see :guilabel:`ou=people`.
  3. Click on :guilabel:`ou=people` and choose :guilabel:`Create a child entry`.
  4. Choose the :guilabel:`Generic: User Account` template.
  5. Fill out the form and click :guilabel:`Create Object`.
  6. Assign users to groups with `these instructions <sync-endpoint-ldap-assign>`.

.. _sync-endpoint-ldap-groups:

Creating groups
~~~~~~~~~~~~~~~~~~~~~~~~~

  1. Click: :guilabel:`login` on the right and login as *admin*.
  2. Expand the tree view on the right until you see :guilabel:`ou=groups`.
  3. Click on :guilabel:`ou=default_prefix` and choose :guilabel:`Create a child entry`.
  4. Choose the :guilabel:`Generic: Posix Group` template.
  5. Fill out the form and click :guilabel:`Create Object`.

  .. note::

    The group name must start with the group prefix, in this case the group prefix is *default_prefix* so for example: *default_prefix my-new-group*

  6. Assign users to groups with `these instructions <sync-endpoint-ldap-assign>`.

.. _sync-endpoint-ldap-assign:

Assigning users to groups
"""""""""""""""""""""""""""""

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

.. _sync-endpoint-https:

HTTPS
-----------------

  1. Store your certificate public key in a :program:`Docker` config with this command:

  .. code-block:: console

    $ docker config create example.com.fullchain.pem PATH_TO_PUBLIC_KEY

  2. Store your certificate private key in a :program:`Docker` secret with this command:

  .. code-block:: console

    $ docker secret create examepl.com.privkey.pem PATH_TO_PRIVATE_KEY

  3. Modify the *configs* section and *secrets* section in :guilabel:`docker-compose.yml` to include name of the :program:`Docker` config and :program:`Docker` secret created above.
  4. Uncomment the relevant lines in the *nginx* section in :guilabel:`docker-compose.yml`.

