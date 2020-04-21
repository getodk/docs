.. spelling::
  phpLDAPadmin
  readonly

.. _sync-endpoint-manual-setup:

Setup ODK-X Sync Endpoint Manually
==================================

Follow these setup instructions for manual or local setup of the sync
endpoint. If deploying to a cloud service, check out
:ref:`Cloud-based Setup <sync-endpoint-cloud-setup>`

Prerequisites
-------------

You must have :program:`Docker 18.09.2` or newer, and be running in *Swarm Mode*.
Follow these links for detailed instructions on installing :program:`Docker` and enabling Swarm Mode.

  - `Docker <https://docs.docker.com/install/>`_
  - `Swarm Mode <https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/>`_

If you wish to enable HTTPS, you also need to install `certbot <https://certbot.eff.org/>`_


ODK-X Sync Endpoint Setup
-------------------------

ODK-X Sync Endpoint requires a database and a *LDAP* directory, you could follow the instructions and deploy all three components together or supply your own database and/or *LDAP* directory.

.. note::

  All of the following commands should be run on your server.

  If you are using git on Windows, make sure git is configured with "core.autocrlf=false" - otherwise it will convert line endings with LF to CRLF, which will cause problems with the .sh-files when used in the Docker containers, thus preventing odk/sync-endpoint from starting and instead just returning with an ":invalid argument"-error. 

Setup instructions:

  1. Choose a directory to store you endpoint in. In that directory, run:

  .. code-block:: console

    $ git clone https://github.com/odk-x/sync-endpoint-default-setup
    
  2. Navigate into the the "sync-endpoint-default-setup" directory
  
  3. Checkout the sync-endpoint code by running:

  .. code-block:: console

    $ git clone https://github.com/odk-x/sync-endpoint
   
  3. Navigate into the sync-endpoint directory. Most likely

  .. code-block:: console

    $ cd sync-endpoint
	
  4. Build sync endpoint by running the following: (NOTE: you will need Apache Maven installed >= 3.3.3)
  
  .. code-block:: console

    $ mvn clean install
	
  5. Navigate back to the parent "sync-endpoint-default-setup" directory. 
  
  6. In the "sync-endpoint-default-setup" directory run:

  .. code-block:: console

    $ docker build --pull -t odk/sync-web-ui https://github.com/odk-x/sync-endpoint-web-ui.git

  7. In the "sync-endpoint-default-setup" cloned repository run:

  .. code-block:: console

    $ docker build --pull -t odk/db-bootstrap db-bootstrap

  8. In the "sync-endpoint-default-setup" cloned repository run:

  .. code-block:: console

    $ docker build --pull -t odk/openldap openldap

  9. In the "sync-endpoint-default-setup" cloned repository run:

  .. code-block:: console

    $ docker build --pull -t odk/phpldapadmin phpldapadmin

  10. Enter your hostname in the :code:`security.server.hostname` field in the :file:`security.properties` file (under the directory :file:`config/sync-endpoint`).

  11. If you're not using the standard ports (80 for *HTTP* and 443 for *HTTPS*) enter the ports you're using in the :code:`security.server.port` and :code:`security.server.securePort` fields in the :file:`security.properties`. Then edit the **ports** section under the **sync** section in :file:`docker-compose.yml` to be :code:`YOUR_PORT:8080`.

    .. note::

      It is important that the right side of the colon stays as 8080. This is the internal port that the web server is looking for.

  12. If you're using your own *LDAP* directory or database, continue with the instructions:

    - :ref:`Custom database instructions <sync-endpoint-setup-database>`
    - :ref:`Custom LDAP instructions <sync-endpoint-setup-ldap>`

  13. In the "sync-endpoint-default-setup" cloned repository run:

    - For HTTP:
    .. code-block:: console

      $ docker stack deploy -c docker-compose.yml syncldap

    - For HTTPS:
    .. code-block:: console

       $ docker stack deploy -c docker-compose.yml -c docker-compose-https.yml syncldap

  14. The server takes about 30s to start, then it will be running at http://127.0.0.1.
  15. See the :ref:`LDAP section <sync-endpoint-ldap>` for instructions on configuring users and groups.

.. _sync-endpoint-setup-database:

Custom database
~~~~~~~~~~~~~~~~~~~~~~

  1. If you haven't followed the :ref:`common instructions <sync-endpoint-setup>`, start with those.
  2. Remove the *db* and *db-bootstrap* sections in :file:`docker-compose.yml`.
  3. Modify :file:`jdbc.properties` to match your database. Supported database systems are :program:`PostgreSQL`, :program:`MySQL` and :program:`Microsoft SQL Server`. Sample config for each type of database can be found `on Github <https://github.com/odk-x/sync-endpoint-default-setup>`_.
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

    a. Make the public key of the CA available to ODK-X Sync Endpoint with this command.

    .. code-block:: console

      $ docker config create org.opendatakit.sync.ldapcert PATH_TO_CERT

    b. Uncomment the relevant lines in the *configs* section in :file:`docker-compose.yml` and the *configs* section under the *sync* section in :file:`docker-compose.yml`.

  3. Remove the *ldap-service* and *phpldapadmin* sections in :file:`docker-compose.yml`.
  4. Modify the relevant sections in :file:`security.properties` to match your LDAP directory. Further instructions are in the file.

  .. note::

    The default configuration does not use ldaps or StartTLS because the LDAP directory communicates with the ODK-X Sync Endpoint over a secure overlay network. You should use ldaps or StartTLS to communicate with your LDAP directory.

  5. In the cloned repository:

  .. code-block:: console

    $ docker stack deploy -c docker-compose.yml syncldap

  6. The server takes about 30s to start, then it will be running at http://127.0.0.1.

.. _sync-endpoint-stopping:

Stopping ODK-X Sync Endpoint
----------------------------

  1. Run:

  .. code-block:: console

    $ docker stack rm syncldap

  2. OPTIONAL: If you want to remove the volumes as well,

    .. Warning:: Removing volumes will remove any provisioned TLS keys
                 if https is enabled. These keys can only be
                 provisioned at a rate of 50 valid keys/domain/week.

    - Linux/macOS:

    .. code-block:: console

      $ docker volume rm $(docker volume ls -f "label=com.docker.stack.namespace=syncldap" -q)

    - Windows:

    .. code-block:: console

      $ docker volume rm (docker volume ls -f "label=com.docker.stack.namespace=syncldap" -q)

