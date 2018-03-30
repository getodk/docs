.. spelling::

  tableId
  rowPath
  rowpath
  elementType
  ETag
  dataETag
  changeSet
  changeSets
  Changesets
  Changeset
  sequenceValue
  rowId
  diff
  api
  API
  timestamp


ODK 2 Sync Protocol
========================

.. _sync-protocol:


.. _sync-protocol-intro:

Introduction
---------------

This documents the Synchronization API used in ODK 2.

The ODK 2 tools utilize a REST API to exchange configuration and data values with the server.

.. _sync-protocol-rest-url:

REST URL formats
---------------------

This document summarizes the API and the usage of the API. The URLs for the REST API have a common URL prefix. E.g.,

  - :file:`https://hostname:port/path/of/prefix/`

That is assumed to be supplied by a configuration setting.

When describing the REST URL, path elements surrounded by curly braces (`{}`) indicate the use of the value for that term in that location within the path. There are a handful of these substitution terms used within the REST URLs. The most common of these are:

  * `appId`-- identifies the 'application', which is a collection of configuration files and data tables that provide a self-contained user experience. e.g., a survey campaign, a specific set of workflows, etc. Applications live on the Android device under different subdirectories within the :file:`/sdcard/opendatakit` directory. The name of the subdirectory is the `appId` of the application contained in the directory. The default application, with an `appId` of *default* lives under the :file:`/sdcard/opendatakit/default/` directory.
  * `odkClientVersion` -- the "major version" of ODK 2 software on the device. This is the 100's digit of the Android manifest version code.  Also referred to as the "rev number" of the release. I.e., for rev 206, the `odkClientVersion` would be 2. Non-backward-compatible changes to the JS API would bump this up. It allows groups to maintain and move across incompatible API changes by supporting different versions of the :file:`formDef.json`, HTML and JS configuration files. Until we reach a release candidate, we are not strictly tracking non-backward-compatible client versions. The exception being the transition from jQuery-mobile-based JavaScript (version 1) and the current bootstrap-based JavaScript (version 2).
  * `tableId` -- identifies a particular data table.
  * `schemaETag` -- identifies a particular manifestation of a table. If you drop the table and recreate it, the re-creation will have a different `schemaETag` that the original table, even if it is otherwise identical.  In contrast, adding, updating or deleting individual rows in a table does not change the `schemaETag` for that table.
  * `rowId` -- the primary key for a particular row within a table.
  * `rowETag` -- identifies a particular revision of a row within a table.

When defining the REST API, we use modified version of the JAX-RS annotations to describe the interface. For example, the API to create a table on the server is described as:

.. code-block:: java

  @PUT
  @Path("{appId}/tables/{tableId}")
  @Consumes({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*TableResource*/ createTable(TableDefinition definition)
      throws ODKDatastoreException,
             TableAlreadyExistsException,
             PermissionDeniedException,
             ODKTaskLockException;

:code:`@PUT`, :code:`@POST`, :code:`@GET` and :code:`@DELETE` indicate the type of HTTP request.

:code:`@Path` indicates the URL path to invoke this method, with the curly brace substitutions of the indicated substitution terms.  This is appended to the common URL prefix provided by the configuration setting.

:code:`@Consumes` indicates the mime types of message bodies accepted by the server. In general, the server accepts JSON and XML in UTF-8 format; JSON is preferred.

:code:`@Produces` indicates the mime types of the message bodies returned to the client. In general, the server can return JSON or XML in UTF-8 format; JSON is preferred.

The method may have zero or more arguments qualified by :code:`@QueryParam(...)`. These identify query parameters for the request, with the `...` indicating the query parameter name.

Methods with entity bodies (PUT and POST methods) will generally have an additional unqualified argument that identifies the content of that entity body. In our documentation, this will generally be a Java class that uses Jackson2 parsers to marshal its content into or out of XML or JSON representations (in the above example, the body of the HTTP PUT request is a `TableDefinition` object).

The return type is indicated in a comment. The `Response` return type is a generic response type that encapsulates both the successful return type (`TableResource` in this example) and the error codes for the various exceptions.  As this API gets fleshed out, the error codes for each specific exception will be documented at the bottom of this page.

In general, the server supports GZIP compression of entity bodies in both directions.

Requests should specify 3 or 4 headers:

  - **X-OpenDataKit-Version** -- this should be set to `2.0`
  - **X-OpenDataKit-Installation-Id** -- this should be set to a UUID that identifies this client device. This UUID will generally be generated on first install of the ODK Services APK. Using "Clear Data" in the device settings will cause a new UUID to be generated. This is used to track the devices responsible for changes to the configuration (resetting the server) and for tracking the status of all devices as they synchronize with the server.
  - **User-Agent** -- this is required by Google AppEngine infrastructure before it will honor requests for GZIP content compression of response entities (i.e., it ignores "Accept-Encoding" directives on requests if this is not present). The value supplied must end with " (gzip)". Services uses a value of: `"Sync " + versionCode + " (gzip)"` where `versionCode` is is the revision code of the software release (e.g., 210). While optional, it is highly recommended that all requests supply this header.
  - **Accept-Encoding** -- this should be set to "gzip" when an entity body is returned.

.. _sync-protocol-rest-data-structures:

REST Data Structures
---------------------

We use Jackson 2.0 for transforming Java objects to and from XML and JSON representations. To understand the representations, it is best to use curl or any other REST client to send requests to the server and view the returned structures.

In the following presentation, we provide the Jackson 2.0 annotations used in our code.

.. _sync-protocol-rest-data-groupings:

Data Groupings
-----------------

Before discussing the API, it is useful to identify the data on the system. The ODK 2 tools assume all data fall into one of six groupings:

  1. (**Data Grouping #1**) HTML, JavaScript and tool configuration files that are not specific to any data table. These include custom home screens, CSS, logo icons, and settings for the tools (e.g., default font size, what settings options to show or hide).
  2. (**Data Grouping #2**) Data table definition, properties, HTML and JavaScript associated with a specific data table. These include all ODK Survey forms used to create or edit this data table, ODK Tables HTML and CSS files for list views, map displays and graphical displays of the data, and ODK Scan mark-sense form definitions.
  3. (**Data Grouping #3**) Data rows and the file attachments (e.g., images, audio, video or other files) associated with specific revision(s) of each data row.
  4. Other files and data that are not synchronized with the server and are for internal use only; e.g., the tools' internal configuration files and device-specific configuration.
  5. Other files that are not synchronized with the server but are generated for external use such as exported csv files and detailed log files for troubleshooting.
  6. content that is independently downloaded and managed by other means (e.g., cached map tiles). I.e., this is content that is not synchronized with the server via the Synchronization REST API.

.. _sync-protocol-rest-data-heirarchy:

Directory Hierarchy and Naming Convention
------------------------------------------

A directory hierarchy and naming convention partitions files into each of the above 6 groupings. This is described `here <https://github.com/opendatakit/opendatakit/wiki/Tool-Suite-Javascript-framework-and-formDef.json-(Survey)-format#configuration-file-structure>`_.

The mapping of these directories to the 3 data groupings that are synchronized with the server through the Synchronization REST API are as follows:

All table-level configuration files (**Data Grouping #2**) are either located under:

  - :file:`.../config/tables/{tableId}/`

Or, they are files or directories under the `csv` folder:

  - :file:`.../config/assets/csv/{tableId}.csv`
  - :file:`.../config/assets/csv/{tableId}/*`
  - :file:`.../config/assets/csv/{tableId}.{qualifier}.csv`
  - :file:`.../config/assets/csv/{tableId}.{qualifier}/*`

Note that the file:

  - :file:`.../config/tables/{tableId}/definition.csv`

Defines the schema for the table. This is stored on the server, but is not verified against the schema as created through the create-table REST API. This file is only processed when initializing a device database from content pushed from app-designer.

Note that the file:

  - :file:`.../config/tables/{tableId}/properties.csv`

Defines the key-value-store values for a data table. These define things such as the formId to use to edit the records in the table, the display names of the columns, etc. Prior to syncing a tableId, the contents of the key-value-store are written to this file, and this file is then compared against the file on the server. If there is any difference, the server file is downloaded. After the file is downloaded, the key-value-store entries for this table are entirely removed and replaced with the content from the server. Thus, with each sync, any changes you had made using the table properties-setting pages in Tables will, in general, be destroyed. These can only be preserved if you reset the app server, pushing your local properties.csv file up to the server. Future versions of the system may eliminate the table properties configuration screens from Tables and move them up to the app-designer (where they rightfully belong).

Everything else under :file:`.../config` is **Data Grouping #1**.

Everything under :file:`.../data` is **Data Grouping #3**.

All remaining files are not synchronized and are managed either as internal state of the application or are output produced by the application.


.. _sync-protocol-workflow:

Overall Sync Workflow
------------------------

The overall sync workflow is:

  1. verify that the server supports the device's `appId`  If the server does support the device's application name, then stop and report a server-configuration compatibility failure.
  2. authenticate the user
  3. request the list of capabilities (roles) the user has been assigned.
  4. request the list of users on the server.
  5. if the device is syncing (vs resetting the app server), verify that the server supports the device's `odkClientVersion`  If the server does not have any files for that client version, then stop and report a server-configuration compatibility failure.
  6. ensure that the device's set of files and the tools configuration not specific to any table (**Data Grouping #1**) exactly matches that on the server for the device's `odkClientVersion` -- removing any files on the device that are not on the server.
  7. for each table, ensure that the device's table definition and table-specific configuration  (**Data Grouping #2 part A**) exactly matches that on the server and that all the files and configuration specific to that table exactly matches those on the server for the device's `odkClientVersion` -- removing any extraneous files on the device.
  8. leave any tables that are on the device but not on the server untouched (do not delete them). By removing the configuration files for this table, it becomes invisible to users. for each table on the device that is not on the server, delete that table and its table-specific files ( (**Data Grouping #2 part B**). After this step, the table configuration on the device exactly matches that of the server.
  9. for each table, perform a bi-directional sync of the data and file attachments for the rows of that table  (**Data Grouping #3**). Log the device's table-level synchronization status for these tables after processing each table.
  10. report overall information about the device's synchronization status and information about the device model, etc. at the end of the synchronization interaction.

.. _sync-protocol-workflow-verify-appId:

Verify `appId` support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

  @GET
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*AppNameList*/ getAppNames()
      throws AppNameMismatchException,
             PermissionDeniedException,
			 ODKDatastoreException;

Where the response is a list of supported `appId` values.

The current server endpoints only support a single `appId`.

.. code-block:: java

  @JacksonXmlRootElement(localName="appNames")
  public class AppNameList extends ArrayList<String> {
  }

.. _sync-protocol-workflow-authenticate-user:

Authenticate user
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

  @GET
  @Path("{appId}/privilegesInfo")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*PrivilegesInfo*/ getPrivilegesInfo()
      throws AppNameMismatchException,
	         PermissionDeniedException,
			 ODKDatastoreException,
			 ODKTaskLockException;

The system current expects a BasicAuth authentication header.

Some server implementations can also accept an "Authorization: Bearer ..." header as an, e.g., Oauth2 token.

The authentication header information is verified against the user list.

If successful, a `PrivilegesInfo` object is returned. This object contains the internal user_id that identifies this user and the friendly name (full_name) of the user. It also provides the user's default group, if configured, and the list of privileges that the user has.

That list will consist of `ROLE_...` and `GROUP_...` values. The `ROLE_...` values are predefined permissions within the ODK tools. The `GROUP_...` values are user-defined and generally correspond to organizational groups to which users belong. This allows application designers to create workflows on the device that are appropriate for the organizational privileges of the user on that device.

The returned object is defined as:

.. code-block:: java

  @JacksonXmlRootElement(localName="privilegesInfo")
  public class PrivilegesInfo {

    /**
      * User id -- this may be more fully-qualified than the user identity information
      * that the client used for login (the server may have provided auto-completion
      * of a qualifying domain, etc.). The client should update their user
      * identity property to this value.
      */
    @JsonProperty(required = true)
    private String user_id;

    /**
      * Friendly full name for this user. Could be used for display.
      */
    @JsonProperty(required = false)
    private String full_name;

    /**
      * Default group
      */
    @JsonProperty(required = false)
    private String defaultGroup;


    /**
      * The roles and groups this user belongs to.
      * This is sorted alphabetically.
      */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="roles")
    private ArrayList<String> roles
  }

.. _sync-protocol-workflow-obtain-users:

Obtain Users List
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

  @GET
  @Path("{appId}/usersInfo")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*UserInfoList*/ getUsersInfo()
     throws AppNameMismatchException,
	        PermissionDeniedException,
			ODKDatastoreException,
			ODKTaskLockException;

This list may or may not be pruned based upon the privileges of the requesting user. i.e., unprivileged users might only see themselves in this list.

This list is useful if the requesting user has the privileges needed to alter the permissions columns of a table's row. They can use this list to select the user to assign ownership to based upon the user's friendly name (full_name) instead of the user_id (the internal string identifying that user), etc.

The `UserInfoList` and `UserInfo` objects are defined as:

.. code-block:: java

  @JacksonXmlRootElement(localName="userInfoList")
  public class UserInfoList extends ArrayList<UserInfo> {
  }

and

.. code-block:: java

  @JacksonXmlRootElement(localName="userInfo")
  public class UserInfo {

    /**
    * user id (unique)
    */
    @JsonProperty(required = true)
    private String user_id;

    /**
    * display name of user (may not be unique)
    */
    @JsonProperty(required = true)
    private String full_name;

    /**
    * The privileges this user has.
    * Sorted.
    */
    @JsonProperty(required = true)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="roles")
    private ArrayList<String> roles;
  }

.. _sync-protocol-rest-sync-api-1:

Data Grouping #1 REST Synchronization API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sync workflow for this step is:

  1. obtain a manifest of the application-level files suitable for this client device.
  2. compare the application-level files on the device against the manifest entry. If different, download the file, if not present on the server, delete it.

.. _sync-protocol-rest-sync-api-1-sub-clientversion:

Substitution Term `odkClientVersion`
""""""""""""""""""""""""""""""""""""""""

The `odkClientVersion` substitution term enables different sets of files to be delivered to different clients. The primary need for this is for configuration settings files that must be linked to a specific version of an installed tool (APK), or for HTML files that invoke a JavaScript API exposed by a specific version of a tool (APK), so that the appropriate implementation of that interface is used for the specific version of the tool (APK) present on the device.

This term is the 100's digit of the build revision. E.g., for rev 210, this is '2'.

This term is limited to 10 characters in length.

.. _sync-protocol-rest-sync-api-1-obtain-clientversion:

Obtain Supported `odkClientVersion`
""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/clientVersions")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*ClientVersionList*/ getOdkClientVersions()
      throws AppNameMismatchException,
	         PermissionDeniedException,
			 ODKDatastoreException,
			 ODKTaskLockException;

This returns a list of the `odkClientVersion` values supported by this server. This is used to fast-fail a synchronization attempt against a server when that server does not have any configuration suitable for the indicated `odkClientVersion`. This commonly happens when an application designer intends to reset the app server with their configuration files, but instead syncs.

.. note::

  Resetting the application server for a '3' client version will not damage or alter the '2' client version files. As long as the data table structures are not altered, the two client versions can coexist on the server.

This provides an upgrade path across incompatible client versions.

The returned list is just a list of strings:

.. code-block:: java

  @JacksonXmlRootElement(localName="clientVersions")
  public class ClientVersionList extends ArrayList<String> {
  }

.. _sync-protocol-rest-sync-api-1-manifest:

Manifest REST API
""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/manifest/{odkClientVersion}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*OdkTablesFileManifest*/ getAppLevelFileManifest();

Requests the manifest of all app-level files for an `appId` and `odkClientVersion`.

The data structure returned is:

.. code-block:: java

  @JacksonXmlRootElement(localName="manifest")
  public class OdkTablesFileManifest {

    /**
      * The entries in the manifest.
      * Ordered by filename and md5hash.
      */
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="file")
    private ArrayList<OdkTablesFileManifestEntry> files;
  }

and here:

.. code-block:: java

  public class OdkTablesFileManifestEntry {

    /**
      * This is the name of the file relative to
      * the either the 'config' directory (for
      * app-level and table-level files) or the
      * row's attachments directory (for row-level
      * attachments).
      *
      * I.e., for the new directory structure,
      * if the manifest holds configpath files, it is under:
      *   /sdcard/opendatakit/{appId}/config
      * if the manifest holds rowpath files, it is under:
      *   /sdcard/opendatakit/{appId}/data/attachments/{tableId}/{rowId}
      */
    public String filename;

    @JsonProperty(required = false)
    public Long contentLength;

    @JsonProperty(required = false)
    public String contentType;

    /**
      * This is the md5hash of the file, which will be used
      * for checking whether or not the version of the file
      * on the phone is current.
      */
    @JsonProperty(required = false)
    public String md5hash;

    /**
      * This is the url from which the current version of the file can be
      * downloaded.
      */
    @JsonProperty(required = false)
    public String downloadUrl;
  }

e.g., for JSON:

.. code-block:: javascript

  {
    "files": [
      {
        "filename": "assets\/app.properties",
        "contentLength": 730,
        "contentType": "application\/octet-stream",
        "md5hash": "md5:aa47d6c0c2b63a5b99c54e5b2630be42",
        "downloadUrl": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/files\/2\/assets\/app.properties"
      },
      {
        "filename": "assets\/changeAccessFilters.html",
        "contentLength": 3202,
        "contentType": "text\/html",
        "md5hash": "md5:78d7402bdab8709b7c35d59ac7048689",
        "downloadUrl": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/files\/2\/assets\/changeAccessFilters.html"
      },
      ...
    ]
  }

e.g., for XML:

.. code-block:: xml

  <?xml version="1.0"?>
  <manifest>
      <file>
          <filename>assets/app.properties</filename>
          <contentLength>730</contentLength>
          <contentType>application/octet-stream</contentType>
          <md5hash>md5:aa47d6c0c2b63a5b99c54e5b2630be42</md5hash>
          <downloadUrl>https://msundt-test.appspot.com:443/odktables/default/files/2/assets/app.properties</downloadUrl>
      </file>
      <file>
          <filename>assets/changeAccessFilters.html</filename>
          <contentLength>3202</contentLength>
          <contentType>text/html</contentType>
          <md5hash>md5:78d7402bdab8709b7c35d59ac7048689</md5hash>
          <downloadUrl>https://msundt-test.appspot.com:443/odktables/default/files/2/assets/changeAccessFilters.html</downloadUrl>
      </file>
  </manifest>

.. _sync-protocol-rest-sync-api-1-download-app-file:

Download App-Level File REST API
"""""""""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/files/{odkClientVersion}/{filePath:.*}")
  @Produces({"*"})
  public Response getFile(@QueryParam("as_attachment") String asAttachment)
         throws IOException, ODKTaskLockException;


If a query parameter (`?as_attachment=true`) is supplied, then a
`Content-Disposition` header is supplied to trigger a browser to
download the file rather than attempt to display it.

.. _sync-protocol-rest-sync-api-1-upload-app-file:

Upload App-Level File REST API
""""""""""""""""""""""""""""""""""

.. code-block:: java

  @POST
  @Path("{appId}/files/{odkClientVersion}/{filePath:.*}")
  @Consumes({"*"})
  public Response putFile(byte[] content)
        throws IOException, ODKTaskLockException;


This API is only used for updating the server configuration. During the normal client synchronization workflow, this API is not invoked.

.. _sync-protocol-rest-sync-api-1-delete-app-file:

Delete App-Level File REST API
"""""""""""""""""""""""""""""""""""

.. code-block:: java

  @DELETE
  @Path("{appId}/files/{odkClientVersion}/{filePath:.*}")
  public Response deleteFile()
        throws IOException, ODKTaskLockException;

This API is only used for updating the server configuration. During the normal client synchronization workflow, this API is not invoked.

.. _sync-protocol-rest-sync-api-2:

Data Grouping #2 REST Synchronization API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Synchronizing table-level configuration and data involves:
  1. Getting the list of available tables from the server
  2. Verifying that the table definition on the server and client match
  3. Getting the table-level configuration and files to the client.

The first two steps involve the table API and the table definition API. The data structures used by these APIs will be discussed after the APIs are presented.

.. _sync-protocol-rest-sync-api-2-table-api:

Data Grouping #2 REST Synchronization -- Table API and Table Definition API
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The table APIs manipulate `TableResource` objects and lists. A `TableResource` identifies the table, information about the earliest and latest update to the data rows in the table, and the `schemaETag` for the table.

The server generates a new, unique, `schemaETag` every time it creates or modifies the table schema. If you create a table, destroy it, then re-create it, the new table will be given a new `schemaETag`.

Creating a table registers a `TableDefinition` for that dataset with the server and creates the necessary database tables for it. Using the `schemaETag`, clients can request the `TableDefinitionResource` for any dataset on the server; that resource consists of the `TableDefinition` and additional information.

Deleting a table on the server involves deleting the specific `TableDefinition` for that tableId's current `schemaETag`.

To prevent data loss, clients that encounter an unexpected `schemaETag` should sync their data as if for the first time.

.. _sync-protocol-rest-sync-api-2-table-api-list-resources:

List All Table Resources API
""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*TableResourceList*/ getTables(@QueryParam("cursor") String cursor, @QueryParam("fetchLimit") String fetchLimit)
      throws ODKDatastoreException,
             AppNameMismatchException,
             PermissionDeniedException,
			 ODKTaskLockException;

If the server does not return the entire set of tables, it will provide a `resumeParameter` in the `TableResourceList` that can be passed in as a query parameter for subsequent requests.
.. _sync-protocol-rest-sync-api-2-table-api-get-resources:

Get Table Resource API
"""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*TableResource*/ getTable()
    throws ODKDatastoreException,
           AppNameMismatchException,
		   PermissionDeniedException,
		   ODKTaskLockException,
		   TableNotFoundException;

.. _sync-protocol-rest-sync-api-2-table-api-create-resources:

Create Table Resource API
""""""""""""""""""""""""""""""

.. code-block:: java

  @PUT
  @Path("{appId}/tables/{tableId}")
  @Consumes({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*TableResource*/ createTable(TableDefinition definition)
      throws ODKDatastoreException,
             AppNameMismatchException,
		     TableAlreadyExistsException,
             PermissionDeniedException,
             ODKTaskLockException,
			 IOException;
.. _sync-protocol-rest-sync-api-2-table-api-get-definition:

Get Table Definition API
"""""""""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*TableDefinitionResource*/ getDefinition()
    throws ODKDatastoreException,
           AppNameMismatchException,
	       PermissionDeniedException,
		   ODKTaskLockException,
		   TableNotFoundException;

.. _sync-protocol-rest-sync-api-2-table-api-delete-definition:

Delete Table Definition API
""""""""""""""""""""""""""""""""""

.. code-block:: java

  @DELETE
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}")
  public Response /*void*/ deleteTable()
    throws ODKDatastoreException,
           AppNameMismatchException,
           ODKTaskLockException,
		   PermissionDeniedException;

.. _sync-protocol-rest-sync-api-2-table-api-table-resource-objects:

`TableResourceList`, `TableResource` and `TableEntry` objects
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @JacksonXmlRootElement(localName="tableResourceList")
  public class TableResourceList {

    /**
    * pass this in to return this same result set.
    */
    @JsonProperty(required = false)
    private String webSafeRefetchCursor;

    /**
    * Alternatively, the user can obtain the elements preceding the contents of the
    * result set by constructing a 'backward query' with the same filter criteria
    * but all sort directions inverted and pass the webSafeBackwardCursor
    * to obtain the preceding elements.
    */
    @JsonProperty(required = false)
    private String webSafeBackwardCursor;

    /**
    * together with the initial query, pass this in to
    * return the next set of results
    */
    @JsonProperty(required = false)
    private String webSafeResumeCursor;

    @JsonProperty(required = false)
    private boolean hasMoreResults;

    @JsonProperty(required = false)
    private boolean hasPriorResults;

    /**
    * The entries in the manifest.
    * This is and ordered list by tableId.
    */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="tableResource")
    private ArrayList<TableResource> tables;

    /**
    * If known, the ETag of the app-level files
    * manifest is also returned.
    */
    @JsonProperty(required = false)
    private String appLevelManifestETag;
  }

.. code-block:: java

  @JacksonXmlRootElement(localName="tableResource")
  public class TableResource extends TableEntry {

    /**
    * URLs for various other parts of the API
    */

    /**
    * Get this same TableResource.
    */
    private String selfUri;

    /**
    * Get the TableDefinition for this tableId
    */
    private String definitionUri;

    /**
    * Path prefix for data row interactions
    */
    private String dataUri;

    /**
    * Path prefix for data row attachment interactions
    */
    private String instanceFilesUri;

    /**
    * Path prefix for differencing (changes-since) service.
    */
    private String diffUri;

    /**
    * Path prefix for permissions / access-control service.
    */
    private String aclUri;

    /**
    * table-level file manifest ETag (optional)
    */
    @JsonProperty(required = false)
    private String tableLevelManifestETag;
  }

and

.. code-block:: java

  public class TableEntry implements Comparable<TableEntry> {

    /**
    * The tableId this entry describes.
    */
    private String tableId;

    /**
    * The ETag of the most recently modified data row
    */
    @JsonProperty(required = false)
    private String dataETag;

    /**
    * The ETag of the TableDefinition
    */
    @JsonProperty(required = false)
    private String schemaETag;
  }

e.g., for JSON:

.. code-block:: javascript

  {
    "webSafeRefetchCursor": null,
    "webSafeBackwardCursor": "H4sIAAAAAAAAAG2P3QqCQBSEXyW6jVw1SpBtQawgiAKRbuWUJ5XMjbNn2R6_yKAfmsuZb2BGHi0ZTYPbpe3MfFgzX2MhnHOevmJXAsO5YU9TJXpwqCQwU3OwjFu4oCrSbJnk6922WCT5Uorv9A3vobWoQj-Ixn40Dv08DOJwFk8ibzaZjvyHPro9LC01GzCcIVvqsOzdCrVD4BpJir-AbMxKkwMq0-dkdYLWoBS_tnxdUne9OG7_BAEAAA",
    "webSafeResumeCursor": "H4sIAAAAAAAAAG2PzQrCMBCEX0W8Spu2osUSA1IVBKkgxWuJ7VKDNZHNhvj4ihX8wTnOfAMzvHZoDQ5ul07b-fBEdM0Y896H5gq6kSTPikKDLevBoeCSCNXRERTyAqLK96tFudkV1XJRrjj7Tt_wQXYORBLFaRClQRKVSZwl02wyDuN4Nooe-uj2MHeottLSHsihhqZ3WzAeJJ0Aq9roRpEy2nL2l-XKrg16iU3-XC8IHXD26_LXOXEHZEOUAg4BAAA",
    "hasMoreResults": false,
    "hasPriorResults": false,
    "tables": [
      {
        "tableId": "geoweather",
        "dataETag": "uuid:d74fb991-850a-4a4c-add5-858690b97c81",
        "schemaETag": "uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8",
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather",
        "definitionUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather\/ref\/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8",
        "dataUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather\/ref\/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8\/rows",
        "instanceFilesUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather\/ref\/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8\/attachments",
        "diffUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather\/ref\/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8\/diff",
        "aclUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather\/acl",
        "tableLevelManifestETag": "19260e15"
      },
      {
        "tableId": "geoweather_conditions",
        "dataETag": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "schemaETag": "uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1",
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions",
        "definitionUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1",
        "dataUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows",
        "instanceFilesUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/attachments",
        "diffUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/diff",
        "aclUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/acl",
        "tableLevelManifestETag": "75a915a5"
      }
    ],
    "appLevelManifestETag": "eded21dd"
  }

e.g., for XML:

.. code-block:: xml

  <tableResourceList>
      <webSafeRefetchCursor/>
      <webSafeBackwardCursor>H4sIAAAAAAAAAG2P3QqCQBSEXyW6jVw1SpBtQawgiAKRbuWUJ5XMjbNn2R6_yKAfmsuZb2BGHi0ZTYPbpe3MfFgzX2MhnHOevmJXAsO5YU9TJXpwqCQwU3OwjFu4oCrSbJnk6922WCT5Uorv9A3vobWoQj-Ixn40Dv08DOJwFk8ibzaZjvyHPro9LC01GzCcIVvqsOzdCrVD4BpJir-AbMxKkwMq0-dkdYLWoBS_tnxdUne9OG7_BAEAAA</webSafeBackwardCursor>
      <webSafeResumeCursor>H4sIAAAAAAAAAG2PzQrCMBCEX0W8Spu2osUSA1IVBKkgxWuJ7VKDNZHNhvj4ihX8wTnOfAMzvHZoDQ5ul07b-fBEdM0Y896H5gq6kSTPikKDLevBoeCSCNXRERTyAqLK96tFudkV1XJRrjj7Tt_wQXYORBLFaRClQRKVSZwl02wyDuN4Nooe-uj2MHeottLSHsihhqZ3WzAeJJ0Aq9roRpEy2nL2l-XKrg16iU3-XC8IHXD26_LXOXEHZEOUAg4BAAA</webSafeResumeCursor>
      <hasMoreResults>false</hasMoreResults>
      <hasPriorResults>false</hasPriorResults>
      <appLevelManifestETag>eded21dd</appLevelManifestETag>
      <tableResource>
          <tableId>geoweather</tableId>
          <dataETag>uuid:d74fb991-850a-4a4c-add5-858690b97c81</dataETag>
          <schemaETag>uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8</schemaETag>
          <selfUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather</selfUri>
          <definitionUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather/ref/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8</definitionUri>
          <dataUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather/ref/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8/rows</dataUri>
          <instanceFilesUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather/ref/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8/attachments</instanceFilesUri>
          <diffUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather/ref/uuid:eb4e7240-af0c-4ccb-abc5-4e537a4609f8/diff</diffUri>
          <aclUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather/acl</aclUri>
          <tableLevelManifestETag>19260e15</tableLevelManifestETag>
      </tableResource>
      <tableResource>
          <tableId>geoweather_conditions</tableId>
          <dataETag>uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96</dataETag>
          <schemaETag>uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1</schemaETag>
          <selfUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions</selfUri>
          <definitionUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions/ref/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1</definitionUri>
          <dataUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions/ref/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1/rows</dataUri>
          <instanceFilesUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions/ref/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1/attachments</instanceFilesUri>
          <diffUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions/ref/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1/diff</diffUri>
          <aclUri>https://msundt-test.appspot.com:443/odktables/default/tables/geoweather_conditions/acl</aclUri>
          <tableLevelManifestETag>75a915a5</tableLevelManifestETag>
      </tableResource>
  </tableResourceList>

.. _sync-protocol-rest-sync-api-2-table-api-table-definition-objects:

`TableDefinition`, `Column` and `TableDefinitionResource` objects
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @JacksonXmlRootElement(localName="tableDefinition")
  public class TableDefinition {

    /**
     * Schema version ETag for the tableId's database schema.
     */
    @JsonProperty(required = false)
    private String schemaETag;

    /**
     * Unique tableId
     */
    private String tableId;

    /**
     * The columns in the table.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(localName="orderedColumns")
    @JacksonXmlProperty(localName="column")
    private ArrayList<Column> orderedColumns;
  }


.. code-block:: java

  @JacksonXmlRootElement(localName="tableDefinitionResource")
  public class TableDefinitionResource extends TableDefinition {

    /**
     * Get this same TableDefinitionResource.
     */
    private String selfUri;

    /**
     * Get the TableResource for this tableId.
     */
    private String tableUri;
  }


The `configpath` type's value is relative to the `config` directory. The 'rowpath' type's value is relative to the directory in which a `rowId` attachments are stored.

with columns defined by:

.. code-block:: java

  public class Column {
    /**
     * The tableId containing this elementKey
     */
    /**
     * The fully qualified key for this element. This is the element's database
     * column name. For composite types whose elements are individually retained
     * (e.g., geopoint), this would be the elementName of the geopoint (e.g.,
     * 'myLocation' concatenated with '_' and this elementName (e.g.,
     * 'myLocation_latitude').
     *
     * Never longer than 58 characters.
     * Never a SQL or SQLite reserved word
     * Satisfies this regex: '^\\p{L}\\p{M}*(\\p{L}\\p{M}*|\\p{Nd}|_)*$'
     */
    private String elementKey;

    /**
     * The name by which this element is referred. For composite types whose
     * elements are individually retained (e.g., geopoint), this would be simply
     * 'latitude'
     *
     * Never longer than 58 characters.
     * Never a SQL or SQLite reserved word
     * Satisfies this regex: '^\\p{L}\\p{M}*(\\p{L}\\p{M}*|\\p{Nd}|_)*$'
     */
    @JsonProperty(required = false)
    private String elementName;

    /**
     * This is the ColumnType of the field. It is either:
     *    boolean
     *    integer
     *    number
     *    configpath
     *    rowpath
     *    array
     *    array(len)
     *    string
     *    string(len)
     *    typename
     *    typename(len)
     *
     *    or
     *
     *    typename:datatype
     *    typename:datatype(len)
     *
     *    where datatype can be one of boolean, integer, number, array, object
     *
     *    Where:
     *
     *    'typename' is any other alpha-numeric name (user-definable data type).
     *
     *    The (len) attribute, if present, identifies the VARCHAR storage
     *    requirements for the field when the field is a unit of retention.
     *    Ignored if not a unit of retention.
     *
     *    The server stores:
     *
     *      integer as a 32-bit integer.
     *
     *      number as a double-precision floating point value.
     *
     *      configpath indicates that it is a relative path to a file under the 'config'
     *             directory in the 'new' directory structure. i.e., the relative path is
     *             rooted from:
     *                 /sdcard/opendatakit/{appId}/config/
     *
     *      rowpath indicates that it is a relative path to a file under the row's attachment
     *             directory in the 'new' directory structure. i.e., the relative path is
     *             rooted from:
     *                 /sdcard/opendatakit/{appId}/data/attachments/{tableId}/{rowId}/
     *
     *      array is a JSON serialization expecting one child element key
     *            that defines the data type in the array.  Array fields
     *            MUST be a unit of retention (or be nested within one).
     *
     *      string is a string value
     *
     *      anything else, if it has no child element key, it is a string
     *            (simple user-defined data type). Unless a datatype is specified.
     *
     *      anything else, if it has one or more child element keys, is a
     *            JSON serialization of an object containing those keys
     *            (complex user-defined data type).
     *
     */
    private String elementType;

    /**
     * JSON serialization of an array of strings. Each value in the
     * array identifies an elementKey of a nested field within this
     * elementKey. If there are one or more nested fields, then the
     * value stored in this elementKey is a JSON serialization of
     * either an array or an object. Otherwise, it is either an
     * integer, number or string field.
     *
     * If the elementType is 'array', the serialization is an
     * array and the nested field is retrieved via a subscript.
     *
     * Otherwise, the serialization is an object and the nested
     * field is retrieved via the elementName of that field.
     */
    @JsonProperty(required = false)
    private String listChildElementKeys;
  }

e.g., for JSON

.. code-block:: javascript

  {
    "schemaETag": "uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1",
    "tableId": "geoweather_conditions",
    "orderedColumns": [
      {
        "elementKey": "Code",
        "elementName": "Code",
        "elementType": "string",
        "listChildElementKeys": "[]"
      },
      {
        "elementKey": "Description",
        "elementName": "Description",
        "elementType": "string",
        "listChildElementKeys": "[]"
      },
      {
        "elementKey": "Language",
        "elementName": "Language",
        "elementType": "string",
        "listChildElementKeys": "[]"
      }
    ],
    "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1",
    "tableUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions"
  }


.. _sync-protocol-rest-sync-api-2-table-api-table-level:

Data Grouping #2 REST Synchronization -- Table-level Files API
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To support table-specific files, a new manifest API is provided

.. code-block:: java

  @GET
  @Path("{appId}/manifest/{odkClientVersion}/{tableId}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*OdkTablesFileManifest*/ getTableIdFileManifest()
       throws ODKEntityNotFoundException,
	          ODKOverQuotaException,
			  PermissionDeniedException,
			  ODKDatastoreException,
			  ODKTaskLockException;


The table-level files API is identical to the app-level files API. It relies upon the file naming convention to distinguish between app-level files and table-level files.


.. _sync-protocol-rest-sync-api-3:

Data Grouping #3 REST Synchronization - Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _sync-protocol-rest-sync-api-3-attachments:

Attachments: BLOBs and Documents
"""""""""""""""""""""""""""""""""""""

BLOBs, long strings (e.g., MySQL TEXT fields) and arbitrary files can be associated with any data row. These are stored as files and viewed as 'attachments' of the row. If a row has an attachment, the row is expected to have one or more columns in its data table that contain the path to that attachment.

For example, the ODK Tools use a `rowpath` elementType (see the Column object, presented earlier), the attachment field definition in Survey (either an `imageUri`, `audioUri` or `videoUri` object) consists of two parts, a `uriFragment` that is a `rowpath` elementType and a `contentType` that is a string containing the mime type of the attachment. The `rowpath` is a path relative to the storage location for files associated with this `rowId`. e.g.,

.. code-block:: javascript

  { uriFragment: "filename.jpg",
    contentType: "image/jpg" }

Attachments are immutable. If an attachment is modified, it must be given a new, unique, `filepath`. The server will not accept revisions to an attachment.

.. _sync-protocol-rest-sync-api-3-revision-states:

Revision States
"""""""""""""""""""""""

It is assumed that the client maintains a set of revision states for an individual row. These states are:
  1. `synced` - no changes to an existing record obtained from the server and all attachment changes have been handled.
  2. `new_row` - a new record on the client.
  3. `changed` - the client modified an existing record obtained from the server.
  4. `deleted` - the client deleted an existing record obtained from the server.
  5. `synced_pending_files` - the client considers the row data to be in the 'rest' state, but the attachments for this row may or may not be up-to-date.
  6. `in_conflict` - the client has determined that there was both a local change to the row and another client has pushed a change to the server, so that the local change cannot be directly submitted to the server, but must instead be resolved with the server's version before being uploaded.

For a given tableId, whenever the `schemaETag` for that tableId has changed, if the client wishes to ensure that its current dataset is preserved, the client should:
  * reset all rows in the `in_conflict` state to their original local change status (i.e., one of `new_row`, `changed` or `deleted`),
  * mark all `synced` and `synced_pending_files` rows as `new_row`.
  * reset the table's last-change-processed value so that the next sync of the table's data will attempt to sync every row in the table.

This may cause all the client's rows to become in conflict with the server; it is unclear what should be the default treatment for this condition.

The server maintains a full history of all changes to a given row. Each row is identified by a `rowId`. Each row revision is identified by its (`rowId`, `rowETag`) tuple.

When a client row is synced with the server, the `rowETag` of the prior version of that `rowId` is sent up to the server (sending **null** if this is an `new_row` row) along with all the values in the row.

When a client row is in the `new_row` state, the client may optionally send **null** for the value of the `rowId`, in which case the server will assign an id.

An insert-or-update row request is successful if:
  * the `rowId` does not yet exist, or
  * the `rowETag` matches the value for the most recent revision to `rowId`, or
  * the `rowETag` doesn't match, but the values of the most recent version of the `rowId` on the server exactly match the values sent from the client.

A delete row request is successful if:
  * the `rowId` does not yet exist, or
  * the `rowETag` matches the value for the most recent revision to `rowId`

If successful, any changes are applied on the server, and the client is returned the updated row (and updated `rowETag`). The client should then either delete the local copy if it was in the `deleted` state, or update its corresponding row to `synced_pending_files` if there are rowpath columns in the dataset or `synced` if not, and set `rowETag` to the value returned for `rowETag` in the updated record.

If unsuccessful, an `ETagMismatchException` error is reported back to the client, and the client should mark the row as `in_conflict`.  `in_conflict` rows are not eligible to be synced until the client resolves the conflict state, usually through processing convention or user intervention.

If the row is in the `synced_pending_files` state, then the client must determine what actions it needs to perform to bring this row's attachment(s) state into concordance with the server.

Because data records can be sent up to the server before their associated attachments are sent, clients may obtain data records from the server that lack the attachment files that they reference. I.e., `ClientOne` may sync a row with an updated attachment to the server, but fail to send the attachment itself. `ClientTwo` may then sync with the server, obtain the row updates that `ClientOne` just posted, and therefore have a valid, current, row without the attachments that it references.

This is a normal condition and should be anticipated and gracefully handled by the client.

.. _sync-protocol-rest-sync-api-3-pending-files:

`synced_pending_files` treatment
""""""""""""""""""""""""""""""""""""

There is a potential for loss of an earlier attachment if the data row is partially synced (transitioning into `synced_pending_files`) and the data row is then updated, changing the attachment, before the earlier version of the attachment is saved on the server.

Because the client is strictly forbidden from modifying the contents of the attachment file, we always know if a new attachment is created because the data row will always be modified to update the attachment path.

Similarly, because the `config` directory is static and dictated by the server, any `configpath` field in a data row does not require syncing of that referenced file with the server. It is assumed that the server already has that file. Only the `rowpath` fields in a data row need to have their attachments synced.

The server maintains a manifest of all `rowpath` attachments uploaded for all versions of the row.

The current implementation only considers attachments specified in 'rowpath' elements. If the attachment has not yet been uploaded, a NOT\_FOUND is returned should that attachment be requested.

The sync mechanism first requests all rowpath files, either specifying an ETag if the file exists locally, or omitting it, to pull the file. If a request with an ETag returns NOT\_MODIFIED, then the server has that file. If it returns NOT\_FOUND, then the client should push the file to the server. If it returns the file, then there is an exceptional condition and the client should log an error (but it is fine to download the file -- the server is still the authority for what these files should contain).

.. _sync-protocol-rest-sync-api-3-workflow:

Data Grouping #3 REST Synchronization - Workflow
"""""""""""""""""""""""""""""""""""""""""""""""""""""

The normal data synchronization workflow is:
  1. Request the `TableResource` for a tableId (using the Table API, defined earlier).
  2. If the `dataETag` in this resource matches the last-change-processed value maintained by the client, then there are no row-value changes. Proceed to upload our changes.
  3. Otherwise, use the `diffUri` to request the list of rows with recent changes.  If you have no last-changed-processed value, use the `dataUri` to request all rows in the table.
  4. Update client state to reflect changes on server.
  5. Update the dataETag of our table to that given in the first result set (RowResourceList) of server rows or changes pulled from the server.
  6. Push `new_row`, `changed` and `deleted` records up to server. Specify the table's dataETag in this request (RowList). If a 409 (CONFLICT) is returned, then go to step (3) above. Otherwise, update our table dataETag with that returned on the RowOutcomeList. Update our local state with the outcomes specified in the RowOutcomeList.
  7. If the above two stages complete without errors, resolve rows in the `synced_pending_files` state by pushing / pulling attachments to / from the server. If successful, transition that row into the `synced` state.
  8. Report status metrics for this table to the server.

And, at some later time:
* Resolve any `in_conflict` rows (user-directed)
This conflict resolution will transition rows either into a state matching that on the server, or into an updated `changed` state such that on the next synchronization those changes will be able to be successfully pushed to the server (unless those rows were changed, yet again, by another client).

.. _sync-protocol-rest-sync-api-3-get-changes-since:

Get All Data Changes Since... API
"""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/diff")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*RowResourceList*/ getRowsSince(@QueryParam("data_etag") String dataETag, @QueryParam("cursor") String cursor, @QueryParam("fetchLimit") String fetchLimit)
      throws ODKDatastoreException,
             PermissionDeniedException,
             InconsistentStateException,
             ODKTaskLockException, BadColumnNameException;

Unlike the other REST interfaces, this takes a query parameter specifying the `dataETag` from which to report the set of changed rows.

If the server cannot return the entire set of rows, it will provide a `resumeParameter` in the `RowResourceList` that can be passed in as a query parameter to generate the next grouping of rows.

.. _sync-protocol-rest-sync-api-3-get-changesets:

Get Changesets API
"""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/diff/changeSets")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*ChangeSetList*/ getChangeSetsSince(@QueryParam("data_etag") String dataETag, @QueryParam("sequence_value") String sequenceValue)
      throws ODKDatastoreException, PermissionDeniedException, InconsistentStateException, ODKTaskLockException, BadColumnNameException;

This API is not actively used in the device's Sync implementation.

As with the previous API, this takes a query parameter specifying the `dataETag` from which to report the set of changeSets (subsequent `dataETag` values).

If the server cannot return the entire set of `dataETag` values processed since the specified `dataETag`, it will provide a `sequenceValue` in the `ChangeSetList` that can be passed in as a query parameter to generate the next grouping of set of `dataETag` values.

Get the changeSets that have been applied since the dataETag changeSet (must be a valid dataETag) or since the given sequenceValue.

These are returned in no meaningful order. For consistency, the values are sorted alphabetically. The returned object includes a sequenceValue that can be used on a subsequent call to get all changes to this table since this point in time.

The `ChangeSetList` contains a list of `dataETag` strings and a `sequenceValue` that allows the client to request changeSets that have been processed since this set of changeSets were returned.

.. code-block:: java

  @JacksonXmlRootElement(localName="changeSetList")
  public class ChangeSetList {

    /**
     * The dataETag values.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="changeSet")
    private ArrayList<String> changeSets;

    /**
     * The dataETag value of the table at the START of this request.
     */
    @JsonProperty(required = false)
    private String dataETag;

    /**
     * The sequenceValue of the server at the START of this request.
     * A monotonically increasing string.
     */
    @JsonProperty(required = false)
    private String sequenceValue;
  }

.. _sync-protocol-rest-sync-api-3-get-changesets-rows:

Get Changeset Rows API
"""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/diff/changeSets/{dataETag}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*RowResourceList*/ getChangeSetRows(@QueryParam("active_only") String isActive,
                             @QueryParam("cursor") String cursor, @QueryParam("fetchLimit") String fetchLimit)
      throws ODKDatastoreException, PermissionDeniedException,
	         InconsistentStateException, ODKTaskLockException,
			 BadColumnNameException;

This API is not actively used in the device's Sync implementation.

This fetches the set of row changes corresponding to this changeSet `dataETag`.

If the "active_only" query parameter is provided, only the changes that are in this change set that are currently active (have not been superseded) will be returned.

.. _sync-protocol-rest-sync-api-3-get-data-rows:

Get All Data Rows API
""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/rows")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*RowResourceList*/ getRows(@QueryParam("cursor") String cursor, @QueryParam("fetchLimit") String fetchLimit)
          throws ODKDatastoreException, PermissionDeniedException,
                 InconsistentStateException, ODKTaskLockException,
                 BadColumnNameException;

If the server cannot return the entire set of rows, it will provide a `resumeParameter` in the `RowResourceList` that can be passed in as a query parameter to generate the next grouping of rows.

The `RowResourceList` returned contains the dataETag of the last change processed on the server.

.. note::

  Later requests with resume cursors may return different values for this dataETag..

The value in the first result should be compared with the value returned at the end of the chain of requests. If this value does change, the client should update its table dataETag to the first value and issue a new request using the first dataETag. This will pull the changes that were occurring as the first result set was being pulled and processed by the client. Only once the dataETag does not change can the client be assured that it does not have any partial changeSets.

.. _sync-protocol-rest-sync-api-3-get-data-row:

Get a Data Row API
""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/rows/{rowId}")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*RowResource*/ getRow()
         throws ODKDatastoreException,
                PermissionDeniedException, InconsistentStateException,
                ODKTaskLockException, BadColumnNameException;

Gets the current values for a specific rowId.

.. _sync-protocol-rest-sync-api-3-alter-data-row:

Alter Data Rows (Insert, Update or Delete)API
"""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @PUT
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/rows")
  @Consumes({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /*RowOutcomeList*/ alterRows(RowList rows)
         throws ODKTaskLockException, ODKDatastoreException,
                PermissionDeniedException, BadColumnNameException,
				InconsistentStateException, TableDataETagMismatchException;

This REST interface takes a `RowList` that must contain the dataETag of the table that matches the one on the server. If the value does not match, the server returns 409 (CONFLICT) and the client should use the diff API to fetch changes from the server before re-attempting to alter data on the server. If the dataETag does match, a `RowOutcomeList` is returned with the actions taken by the server.

.. warning::

  Some row changes may fail, and some may succeed (e.g., due to permissions violations).

The client should process the `RowOutcome` information to update its local database to match that on the server. For bandwidth efficiency, large portions of the `RowOutcome` object will be null upon success.

The `RowOutcomeList` contains the dataETag of the resulting change set on the server. The client should update its table dataETag to match this value.

.. _sync-protocol-rest-sync-api-3-row-objects:

`Row` and `RowList`, `RowResource` and `RowResourceList`, `RowOutcome` and `RowOutcomeList` Objects
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

`RowList` is a list of rows:

.. code-block:: java

  @JacksonXmlRootElement(localName="rowList")
  public class RowList {

    /**
     * The entries in the manifest.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="row")
    private ArrayList<Row> rows;

    /**
     * The dataETag of the table at the START of this request.
     */
    @JsonProperty(required = false)
    private String dataETag;
  }

`RowOutcomeList` is a list of row outcomes:

.. code-block:: java

  @JacksonXmlRootElement(localName="rowList")
  public class RowOutcomeList {

    /**
     * The URL that returns the TableResource for this table.
     */
    @JsonProperty(required = false)
    private String tableUri;

    /**
     * The entries in the manifest.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="row")
    private ArrayList<RowOutcome> rows;

    /**
     * The dataETag for the changes made by this request.
     */
    @JsonProperty(required = false)
    private String dataETag;
  }

`RowResourceList` is a list of row resources:

.. code-block:: java

  @JacksonXmlRootElement(localName="rowResourceList")
  public class RowResourceList {

    /**
     * The entries in the manifest.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(useWrapping=false)
    @JacksonXmlProperty(localName="rowResource")
    private ArrayList<RowResource> rows;

    /**
     * The dataETag of the table at the START of this request.
     */
    @JsonProperty(required = false)
    private String dataETag;

    /**
     * The URL that returns the TableResource for this table.
     */
    private String tableUri;

    /**
     * together with the initial query, pass this in to
     * return this same result set.
     */
    @JsonProperty(required = false)
    private String webSafeRefetchCursor;

    /**
     * Alternatively, the user can obtain the elements preceding the contents of the
     * result set by constructing a 'backward query' with the same filter criteria
     * but all sort directions inverted and pass the webSafeBackwardCursor
     * to obtain the preceding elements.
     */
    @JsonProperty(required = false)
    private String webSafeBackwardCursor;

    /**
     * together with the initial query, pass this in to
     * return the next set of results
     */
    @JsonProperty(required = false)
    private String webSafeResumeCursor;

    @JsonProperty(required = false)
    private boolean hasMoreResults;

    @JsonProperty(required = false)
    private boolean hasPriorResults;

`RowResource` extends a `Row` and supplies a self-reference URL.

.. code-block:: java

  @JacksonXmlRootElement(localName="rowResource")
  public class RowResource extends Row {

    /**
     * The URL that returns this RowResource.
     */
    private String selfUri;
  }

`RowOutcome` also extends `Row` with a self-reference URL and an `OutcomeType`:

.. code-block:: java

  @JacksonXmlRootElement(localName = "rowResource")
  public class RowOutcome extends Row {

    /**
     * Possible values:
     * <ul>
     * <li>UNKNOWN -- initial default value</li>
     * <li>SUCCESS -- rowETag, dataETagAtModification, filterScope updated</li>
     * <li>DENIED -- permission denied -- just the rowId is returned</li>
     * <li>IN_CONFLICT -- server record is returned (in full)</li>
     * <li>FAILED -- anonymous insert conflict (impossible?) or
     *               delete of non-existent row -- just rowId is returned</li>
     * </ul>
     */
    public enum OutcomeType {
      UNKNOWN, SUCCESS, DENIED, IN_CONFLICT, FAILED
    }

    /**
     * The URL that returns this RowResource.
     */
    @JsonProperty(required = false)
    private String selfUri;

    @JsonProperty(required = false)
    private OutcomeType outcome = OutcomeType.UNKNOWN;
  }

`Row` contains the data for a row.

.. code-block:: java

  public class Row {

    /**
     * PK identifying this row of data.
     */
    @JacksonXmlProperty(localName = "id")
    @JsonProperty(value = "id", required = false)
    private String rowId;

    /**
     * identifies this revision of this row of data.
     * (needed to support updates to data rows)
     * (creation is a revision from 'undefined').
     */
    @JsonProperty(required = false)
    private String rowETag;

    /**
     * identifies the service-level
     * interaction during which this
     * revision was made. Useful for
     * finding coincident changes
     * and prior/next changes.
     */
    @JsonProperty(required = false)
    private String dataETagAtModification;

    /**
     * deletion is itself a revision.
     */
    @JsonProperty(required = false)
    private boolean deleted;

    /**
     * audit field returned for
     * archive/recovery tools.
     */
    @JsonProperty(required = false)
    private String createUser;

    /**
     * audit field returned for
     * archive/recovery tools
     */
    @JsonProperty(required = false)
    private String lastUpdateUser;

    /**
     * OdkTables metadata column.
     *
     * The ODK Survey form that
     * was used when revising this
     * row.
     *
     * This can be useful for
     * implementing workflows.
     * I.e., if savepointTyp is
     * COMPLETE with this formId,
     * then enable editing with
     * this other formId.
     */
    @JsonProperty(required = false)
    private String formId;

    /**
     * OdkTables metadata column.
     *
     * The locale of the device
     * that last revised this row.
     */
    @JsonProperty(required = false)
    private String locale;

    /**
     * OdkTables metadata column.
     *
     * One of either COMPLETE
     * or INCOMPLETE. COMPLETE
     * indicates that the formId
     * used to fill out the row
     * has validated the entered
     * values.
     */
    @JsonProperty(required = false)
    private String savepointType;

    /**
     * OdkTables metadata column.
     *
     * For Mezuri, the timestamp
     * of this data value.
     *
     * For ODK Survey, the last
     * save time of the survey.
     *
     * For sensor data,
     * the timestamp for the
     * reading in this row.
     */
    @JsonProperty(required = false)
    private String savepointTimestamp;

    /**
     * OdkTables metadata column.
     *
     * For ODK Survey, the user
     * that filled out the survey.
     *
     * Unclear what this would be
     * for sensors.
     *
     * For Mezuri, this would be
     * the task execution ID that
     * created the row.
     */
   @JsonProperty(required = false)
    private String savepointCreator;

    /**
     * RowFilterScope is passed down to device.
     *
     * Implements DEFAULT, MODIFY, READ_ONLY, HIDDEN
     * with rowOwner being the "owner" of the row.
     *
     * It is passed down to the
     * device so that the
     * device can do best-effort
     * enforcement of access control
     * (trusted executor)
     */
    @JacksonXmlProperty(localName = "filterScope")
    @JsonProperty(value = "filterScope", required = false)
    private RowFilterScope rowFilterScope;

    /**
     * Array of user-defined column name to
     * the string representation of its value.
     * Sorted by ascending column name.
     */
    @JsonProperty(required = false)
    @JacksonXmlElementWrapper(localName="orderedColumns")
    @JacksonXmlProperty(localName="value")
    private ArrayList<DataKeyValue> orderedColumns;
  }

where `RowFilterScope` is:

.. code-block:: java

  public class RowFilterScope {

    /**
     * Type of Filter.
     *
     * Limited to 10 characters
     */
    public enum Access {
      FULL, MODIFY, READ_ONLY, HIDDEN,
    }

    @JsonProperty(required = false)
    private Access defaultAccess;

    @JsonProperty(required = false)
    private String rowOwner;

    @JsonProperty(required = false)
    private String groupReadOnly;

    @JsonProperty(required = false)
    private String groupModify;

    @JsonProperty(required = false)
    private String groupPrivileged;
  }

and `DataKeyValue` is:

.. code-block:: java

  public class DataKeyValue {
    @JacksonXmlProperty(isAttribute=true)
    public String column;

    @JacksonXmlText
    public String value;
  }

e.g., for JSON

.. code-block:: javascript

  {
    "rows": [
      {
        "rowETag": "uuid:e818c096-c3c6-4ec6-ac40-015ddfbef303",
        "dataETagAtModification": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "deleted": false,
        "createUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "lastUpdateUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "formId": "geoweather_conditions",
        "locale": "en_US",
        "savepointType": "COMPLETE",
        "savepointTimestamp": "2017-07-21T19:13:52.594000000",
        "savepointCreator": "username:msundt",
        "orderedColumns": [
          {
            "column": "Code",
            "value": "clear"
          },
          {
            "column": "Description",
            "value": "Clear skies on 5.0"
          },
          {
            "column": "Language",
            "value": "en"
          }
        ],
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows\/uuid:50caa4ef-4f7f-4229-80b6-8e2d44026b90",
        "id": "uuid:50caa4ef-4f7f-4229-80b6-8e2d44026b90",
        "filterScope": {
          "defaultAccess": "FULL",
          "rowOwner": null,
          "groupReadOnly": null,
          "groupModify": null,
          "groupPrivileged": null
        }
      },
      {
        "rowETag": "uuid:a3a8e4b8-295c-410e-a9ec-7577e386799f",
        "dataETagAtModification": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "deleted": false,
        "createUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "lastUpdateUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "formId": "geoweather_conditions",
        "locale": "en_US",
        "savepointType": "COMPLETE",
        "savepointTimestamp": "2017-07-21T19:13:02.633000000",
        "savepointCreator": "username:msundt",
        "orderedColumns": [
          {
            "column": "Code",
            "value": "rain"
          },
          {
            "column": "Description",
            "value": "Raining on 5.0"
          },
          {
            "column": "Language",
            "value": "en"
          }
        ],
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows\/uuid:7fba9aa0-df29-4e3b-a390-e07b4ee48fe8",
        "id": "uuid:7fba9aa0-df29-4e3b-a390-e07b4ee48fe8",
        "filterScope": {
          "defaultAccess": "READ_ONLY",
          "rowOwner": null,
          "groupReadOnly": null,
          "groupModify": null,
          "groupPrivileged": null
        }
      },
      {
        "rowETag": "uuid:34847487-3f5d-4f66-814c-602e2dc4d6d2",
        "dataETagAtModification": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "deleted": false,
        "createUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "lastUpdateUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "formId": "geoweather_conditions",
        "locale": "en_US",
        "savepointType": "COMPLETE",
        "savepointTimestamp": "2017-07-21T19:14:32.127000000",
        "savepointCreator": "username:msundt",
        "orderedColumns": [
          {
            "column": "Code",
            "value": "thunderstorm"
          },
          {
            "column": "Description",
            "value": "Thunderstorm on 5.0"
          },
          {
            "column": "Language",
            "value": "en"
          }
        ],
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows\/uuid:7fba9aa0-df29-4e3b-a390-e08b4ee48fe8",
        "id": "uuid:7fba9aa0-df29-4e3b-a390-e08b4ee48fe8",
        "filterScope": {
          "defaultAccess": "READ_ONLY",
          "rowOwner": null,
          "groupReadOnly": null,
          "groupModify": null,
          "groupPrivileged": null
        }
      },
      {
        "rowETag": "uuid:9c13fa4c-62c0-4a53-9038-34514c9b17f0",
        "dataETagAtModification": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "deleted": false,
        "createUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "lastUpdateUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "formId": "geoweather_conditions",
        "locale": "en_US",
        "savepointType": "COMPLETE",
        "savepointTimestamp": "2017-07-21T19:12:36.747000000",
        "savepointCreator": "username:msundt",
        "orderedColumns": [
          {
            "column": "Code",
            "value": "drizzle"
          },
          {
            "column": "Description",
            "value": "Light rain (drizzle) on 5.0"
          },
          {
            "column": "Language",
            "value": "en"
          }
        ],
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows\/uuid:88b2edbc-092a-44c2-9736-8d50f6e44704",
        "id": "uuid:88b2edbc-092a-44c2-9736-8d50f6e44704",
        "filterScope": {
          "defaultAccess": "HIDDEN",
          "rowOwner": null,
          "groupReadOnly": null,
          "groupModify": null,
          "groupPrivileged": null
        }
      },
      {
        "rowETag": "uuid:82d61608-a870-4976-baa8-2c7af974f74e",
        "dataETagAtModification": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
        "deleted": false,
        "createUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "lastUpdateUser": "uid:msundt|2014-10-03T16:48:04.320+0000",
        "formId": "geoweather_conditions",
        "locale": "en_US",
        "savepointType": "COMPLETE",
        "savepointTimestamp": "2017-07-21T19:15:04.655000000",
        "savepointCreator": "username:msundt",
        "orderedColumns": [
          {
            "column": "Code",
            "value": "partly_cloudy"
          },
          {
            "column": "Description",
            "value": "Partly cloudy on 5.0"
          },
          {
            "column": "Language",
            "value": "en"
          }
        ],
        "selfUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions\/ref\/uuid:b48be1ae-d861-4453-97a2-ac6cd8bf98b1\/rows\/uuid:999f57ec-d866-45bc-ad54-52c57489d54b",
        "id": "uuid:999f57ec-d866-45bc-ad54-52c57489d54b",
        "filterScope": {
          "defaultAccess": "MODIFY",
          "rowOwner": null,
          "groupReadOnly": null,
          "groupModify": null,
          "groupPrivileged": null
        }
      }
    ],
    "dataETag": "uuid:e93ead34-8ee1-4c5c-9d25-7732a5ec9c96",
    "tableUri": "https:\/\/msundt-test.appspot.com:443\/odktables\/default\/tables\/geoweather_conditions",
    "webSafeRefetchCursor": null,
    "webSafeBackwardCursor": "H4sIAAAAAAAAAG2PW4vCMBCF_4r4KmnSUO2FGBB1YUFckLKvMjXT3WBtJZlQf_6W7YIX9jzMw5nvHDjqFJzv3OR2aVq_nH4TXQvO-76Puiu2BgjOlqLOffERnGoFRM5WgXAPF9TH9WG7Kt8_9sfNqtwq_vy9w5_QBNRSxCkTKZOilHEh00JkUT6PZ2LQQ3aEVXB2B54OSMG1aEY3BGuKuTgBJFizpE6HI2XOMlEtWIbSJImQiyof-v7NK-vfOteDM-vfRbqGxqPir7b6W6x_ACeKKe0jAQAA",
    "webSafeResumeCursor": "H4sIAAAAAAAAAG2Py2rDMBREf6VkW2QpimVFRhWYPCBQUgimWyNbaiOS2OH6Cvfza-pC0pJZDTNnFqObCH0HT1-Xc9u_zI6I15zSYRiS7upbZ9GeAiYdfNIJnBltESHUEf3eXrypVodNUe7e9tW6KDea_m1v8Ls9R284m0vCJOGs5POcy5yphPHFMxt1t51gHSG82h4PHiO03k1pjMHlSqkPIX1D3DLLSCrqhlgnUiJ4I2S6VKOvNX2416HfdjBYcKufRwYhek3_p_r3sPkG0rFWryIBAAA",
    "hasMoreResults": false,
    "hasPriorResults": false
  }

The `dataETagAtModification` field tracks the change entry that can be used with the **Get All Data Changes Since... API** to return the changes in the data table from this row's last data change (as indicated by the `rowETag`).

The `createUser` and `lastUpdateUser` fields may be set and returned by the server.  These are intended for data-dump and data-restore functionality and are not normally provided by a client.

The `formId` field identifies the ODK Survey form that last modified this record.  This is useful for implementing multi-stage client workflows.

The `locale` field tracks the last ODK Survey locale in which the form was opened and perhaps modified.

The `savepointType` is one of `INCOMPLETE` or `COMPLETE`; it indicates whether the data is considered to be in a possibly-incomplete state or if it is complete (i.e., in ODK Survey, if it has been validated and marked as finalized). Together with the `formId`, this can indicate whether the client processing can advance from one workflow stage (`formId`) to another (i.e., when the record is 'COMPLETE' in the current stage) or whether to stall within the current workflow stage (`formId`). For autonomous data publishing (e.g., ODK Sensors Framework), this should be set to `COMPLETE`.

The `savepointTimestamp` is the timestamp of the last save of this data record, as reported on the client (whose time clock may be inaccurate).

The `savepointCreator` is the entity modifying/writing this data row. For ODK Survey, this is the user as identified by the Android device.

The `filterScope` should default to `{type: 'Default', value: null}`. It is used to control access to the data record. Future updates to this protocol will likely make this unmodifiable on the server unless the requesting user has appropriate permissions. The contents, interpretation and use of this field is evolving at this time.

The `values` map holds the data values that the user has defined.

.. _sync-protocol-rest-sync-api-3-get-manifest-attachments:

Get Manifest of Attachments API
"""""""""""""""""""""""""""""""""""""""""

.. code-block: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/attachments/{rowId}/manifest")
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response /* OdkTablesFileManifest */ getManifest(@QueryParam("as_attachment") String asAttachment)
     throws IOException;

This returns all attachments (both current and historical) for the given `rowId` on the server.

This uses the same return structure as the Table-level and App-level manifest, but the path is relative to the directory in which the `rowId` attachments are stored on the client.

There is both a multipart file download/upload API and an individual-file download/upload API. The Android client uses the multipart file API.

.. _sync-protocol-rest-sync-api-3-get-manifest-attachments-multipart:

Multipart Get Attachment API
""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @POST
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/attachments/{rowId}/download")
  @Consumes({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  @Produces({"multipart/form-data"})
  public Response getFiles(OdkTablesFileManifest manifest) throws IOException, ODKTaskLockException, PermissionDeniedException;


Returns a multipart form containing the files.

**To Do**: Verify that a part's name is the filename relative to the folder holding attachments for the `rowId`.

.. _sync-protocol-rest-sync-api-3-put-manifest-attachments-multipart:

Multipart Put Attachment API
"""""""""""""""""""""""""""""""""""

.. code-block: java

  @POST
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/attachments/{rowId}/upload")
  @Consumes({"multipart/form-data"})
  @Produces({"application/json",
             "text/xml;charset=UTF-8",
             "application/xml;charset=UTF-8"})
  public Response postFiles(InMultiPart inMP)
	throws IOException, ODKTaskLockException, ODKTablesException, ODKDatastoreException;


**To Do**: verify that a part's name is the filename relative to the folder holding attachments for the `rowId`.

Returns a string describing error on failure, otherwise empty and Status.CREATED.

.. _sync-protocol-rest-sync-api-3-get-attachment:

Get Attachment API
""""""""""""""""""""""""""

.. code-block:: java

  @GET
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/attachments/{rowId}/file/{filePath:.*}")
  @Produces({"*"})
  public Response getFile(@QueryParam("as_attachment") String asAttachment)
        throws IOException, ODKTaskLockException, PermissionDeniedException;

The `filePath` is relative to the folder holding attachments for the `rowId`.

.. _sync-protocol-rest-sync-api-3-put-attachment:

Put Attachment API
""""""""""""""""""""""""""

.. code-block:: java

  @POST
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/attachments/{rowId}/file/{filePath:.*}")
  @Consumes({"*"})
  public Response putFile(byte[] content)
        throws IOException, ODKTaskLockException, PermissionDeniedException, ODKDatastoreException;

.. _sync-protocol-rest-sync-api-3-report-status-metrics:

Report table status metrics
"""""""""""""""""""""""""""""

.. code-block:: java

  @POST
  @Path("{appId}/tables/{tableId}/ref/{schemaETag}/installationStatus")
  @Consumes({"application/json"})
  public Response /*OK*/ postInstallationStatus(Object body)
      throws AppNameMismatchException,
	         PermissionDeniedException,
			 ODKDatastoreException,
			 ODKTaskLockException;

This takes a generic JSON object and stores it on the server.

The JSON object (serialization) should be less than 4000 characters in length.

This API is used to report the outcome of the synchronization of this
table on the client. In particular, it can be used to determine which
devices are up-to-date with respect to the server's table contents
(i.e., have no conflicts). That information is useful for determining when
rows on the server can be permanently removed after having been marked
as deleted.

.. _sync-protocol-rest-sync-api-3-report-overall-stats:

Report device info and overall sync state
""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java

  @POST
  @Path("{appId}/installationInfo")
  @Consumes({"application/json"})
  public Response /*OK*/ postInstallationInfo(Object body)
      throws AppNameMismatchException,
	         PermissionDeniedException,
			 ODKDatastoreException,
			 ODKTaskLockException;

This API is invoked after the sync has completed on the client.

This takes a generic JSON object and stores it on the server.

The JSON object (serialization) should be less than 4000 characters in length.

It can be used to determine whether a client successfully synced and provides information mapping the client's `X-OpenDataKit-Installation-Id` back to a physical device (info on the type of device and the reported Android ID for the device are in the Android implementation's object).

