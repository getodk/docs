.. spelling::
  phpLDAPadmin
  readonly
  letsencrypt
  OpenLDAP
  ldif
  utils
  ldap
  env
  yml
  ldapUrl
  localhost
  UI
  authenticationMethod
  dhis

ODK-X Sync Endpoint
===================

.. _sync-endpoint-intro:

:dfn:`ODK-X Sync Endpoint` is an implementation of :doc:`cloud-endpoints-intro`. It runs a server inside a :program:`Docker` container that implements the `ODK-X REST Protocol <https://docs.odk-x.org/odk-2-sync-protocol/>`_.

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
           docker's built in secrets and config infrastructure can be
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
"""""""""""""""""""""""""

  1. Click: :guilabel:`login` on the left and login as *admin*.
  2. Expand the tree view on the left until you see :guilabel:`ou=people`.
  3. Click on :guilabel:`ou=people` and choose :guilabel:`Create a child entry`.
  4. Choose the :guilabel:`Generic: User Account` template.
  5. Fill out the form and click :guilabel:`Create Object`.
  6. Assign users to groups with :ref:`these instructions <sync-endpoint-ldap-assign>`.

.. _sync-endpoint-ldap-groups:

Creating groups
"""""""""""""""""""""""""

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

.. _sync-endpoint-advanced:

Advanced
--------

.. _sync-endpoint-ldap-defaults:

Editing the defaults of LDAP Directory
"""""""""""""""""""""""""""""""""""""""""""""
    Modify the :file:`ldap.env` file to configure the environment variables. The :file:`ldap.env` file is located in the sync-endpoint-default-setup directory.

    The default settings are as follows 

     .. code-block:: console

      # openldap
      LDAP_ORGANISATION=Open Data Kit            // name of your organisation
      LDAP_DOMAIN=example.org                    // domain of your organisation
      LDAP_READONLY_USER=true                    // enable the read only user
      LDAP_READONLY_USER_PASSWORD=readonly       // password for read only user
      LDAP_ADMIN_PASSWORD=admin                  // default password for admin account

      # phpldapadmin
      PHPLDAPADMIN_LDAP_HOSTS=ldap-service   // This is for the phpLDAPadmin. In Docker Swarm this is the hostname of the service running LDAP. This can be 
                                                eddited in the docker-compose.yml file


  .. note::

    For LDAP environment variables the corresponding options in the security.properties also need to be modified. The security.properties file is
    located at config/sync-endpoint in the sync-endpoint-default-setup directory.

.. _sync-endpoint-ldap-ui:

Using a Different LDAP UI
""""""""""""""""""""""""""""""""""""""""""""""

    If you want to use a UI outside the Docker Swarm in your local machine Modify the docker-compose.yml file in sync-endpoint-default-setup directory. Add ports 
    mapping to the ldap service to expose the port 389 of ldap service to a port in your local host. If you wish to access 
    the ldap protocol over TLS/SSL expose the port 636. Connect the UI application to this port on localhost.

    The ldap service of the the Docker compose should be like this after adding port mapping.

    .. code-block:: console

      ldap-service:
       image: odk/openldap
       deploy:
        replicas: 1
       networks:
        - ldap-network
       ports:
        - "YOUR_LOCAL_HOST_PORT:389"    // 389 is the default port of openLDAP 
       volumes:
        - ldap-vol:/var/lib/ldap
        - ldap-slapd.d-vol:/etc/ldap/slapd.d
       env_file:
        - ldap.env 

    .. Warning:: The LDAP service running at any port will not only be accessible from the localhost but will also be exposed over the Docker ingress overlay 
                 network (which is exposed to the Internet in most cases).

    For running the UI application in the Docker Swarm create a folder in the sync-endpoint-default-setup directory and create a Docker file inside it.
    Copy the templates folder from the phpLDAPadmin directory to the new directory. In the Docker file ,add the image of the UI application to be used and the 
    "COPY" command to copy the templates folder to the right path inside the container.

    To build the Docker image run the command in the sync-endpoint-default-setup-directory with tag odk/[YOUR_UI_APPLICATION_NAME]:

     .. code-block:: console

       $ docker build -t odk/[YOUR_UI_APPLICATION_NAME] [ Folder conatining the Docker file ]

    Edit the docker-compose.yml file. Replace the image of phpLDAPadmin service with odk/[YOUR_UI_APPLICATION_NAME]. 

.. _sync-endpoint-dhis2:    

Managing Identity through DHIS2
"""""""""""""""""""""""""""""""""
   In the sync-endpoint-default-setup directory navigate to config/sync-endpoint. Modify the :file:`security.properties` file to fill in the Settings for DHIS2 
   Authentication section. Set security.server.authenticationMethod in security.properties to dhis2. After this the following settings need to be configured for
   dhis2.

       - :guilabel:`security.server.dhis2ApiUrl`
       - :guilabel:`security.server.dhis2AdminUsername`
       - :guilabel:`security.server.dhis2AdminPassword`
       - :guilabel:`security.server.dhis2SiteAdmins`
       - :guilabel:`security.server.dhis2AdministerTables`
       - :guilabel:`security.server.dhis2SuperUserTables`
       - :guilabel:`security.server.dhis2SyncTables`
       - :guilabel:`security.server.dhis2FormManagers`
       - :guilabel:`security.server.dhis2DataViewers`
       - :guilabel:`security.server.dhis2DataCollectors`

   [OPTIONAL] Remove OpenLDAP and phpLDAPadmin from docker-compose.yml .

   After restarting your Sync Endpoint server, you will be able to login to Sync Endpoint using the same credentials you use
   for your DHIS2 server. DHIS2 organization units and groups, with membership preserved, will be converted to Sync Endpoint
   groups and accessible through the Sync Endpoint REST API.

.. _sync-endpoint-warnings:

Warnings
--------
 - The database and the LDAP Directory set up here are meant only for testing and evaluation. When running in production you should configure a production ready 
   database and a production ready LDAP Directory. Using the pre-configured database and directory in production can result in poor performance and degraded 
   availability.
 - You should refer to Docker Swarm documentation on running a production ready Swarm.
 - We recommend that you host Sync Endpoint on a commercial cloud provider (e.g. Google Cloud Platform, Amazon AWS, Microsoft Azure, etc.) If you want to host 
   Sync Endpoint on premise, you should consult your System Administrator for appropriate hardware.
 - Always make regular backups and test your backups to prevent potential data loss.
