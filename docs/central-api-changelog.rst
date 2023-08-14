.. auto generated file - DO NOT MODIFY

Changelog
=======================================================================================================================



Here major and breaking changes to the API are listed by version.

ODK Central v2023.4
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Added**\ :

- `DELETE /sessions/current </central-api-authentication/#logging-out-current-session>`__ logs out the current session.

ODK Central v2023.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

- New endpoint `PATCH /projects/:id/datasets/:name </central-api-dataset-management/#update-dataset-metadata>`__ to change whether approval of Submission is required to create an Entity.
- New `Entities </central-api-entity-management>`__ endpoints for richer Entity-Based Data Collection workflows. These endpoints provide ways of accessing Entities, as well as the ability to *create*\ , *update*\  and *soft-delete*\  Entities via the API!
  
  * New endpoint `GET /projects/:id/datasets/:name/entities </central-api-entities/#entities-metadata>`__ for listing Entities within a Dataset.
  * New endpoint `GET /projects/:id/datasets/:name/entities/:uuid </central-api-entities/#getting-entity-details>`__ for getting the metadata, or details, about a specific Entity.
  * New endpoint `GET /projects/:id/datasets/:name/entities/:uuid/versions </central-api-entities/#listing-versions>`__ for listing the versions of an Entity.
  * New endpoint `GET /projects/:id/datasets/:name/entities/:uuid/diffs </central-api-entities/#getting-changes-between-versions>`__ for getting the changes between versions of an Entity.
  * New endpoint `GET /projects/:id/datasets/:name/entities/:uuid/audits </central-api-entities/#entity-audit-log>`__ for getting the server audit logs about a specific Entity.
  * New endpoint `POST /projects/:id/datasets/:name/entities </central-api-entities/#creating-an-entity>`__ for creating an Entity from JSON.
  * New endpoint `PATCH /projects/:id/datasets/:name/entities/:uuid </central-api-entities/#updating-an-entity>`__ for updating the data or label of an Entity.
  * New endpoint `DELETE /projects/:id/datasets/:name/entities/:uuid </central-api-entities/#deleting-an-entity>`__ for soft-deleting an Entity.

**Changed**\ :

- ETag support has been added for `Download Dataset </central-api-dataset-management/#download-dataset>`__ and `Download Form Attachment </central-api-form-management/#downloading-a-form-attachment>`__.
- The format of `Download Dataset </central-api-dataset-management/#download-dataset>`__ was changed to more closely match the OData Dataset format.
- In the `OData Dataset Service </central-api-odata-endpoints/#odata-dataset-service>`__, ``name``\  was removed because it is a duplication of an ``**\ id``\  representing an Entity's UUID.
- The ``properties``\  returned by the `Dataset Metadata endpoint </central-api-dataset-management/#dataset-metadata>`__ each now include a field ``odataName``\ , which represents the way the property name will be sanitized and outputted for OData.


ODK Central v2023.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

- New `OData Dataset Service </central-api-odata-endpoints/#odata-dataset-service>`__ for each ``Dataset``\  that provides a list of ``Entities``\ .

**Changed**\ :

- The response of ``GET``\ , ``POST``\ , ``PUT``\  and ``PATCH``\  methods of `Submissions </central-api-submission-management/#listing-all-submissions-on-a-form>`__ endpoint has been updated to include metadata of the ``currentVersion``\  of the Submission.

ODK Central v2023.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

- New endpoint `GET /projects/:id/datasets/:name </central-api-dataset-management/#dataset-metadata>`__ to get the metadata of a Dataset

**Changed**\ :

- `GET /projects/:id/datasets </central-api-dataset-management/#datasets>`__ now supports ``X-Extended-Metadata``\  header to retrieve number of Entities in the Dataset and timestamp of the last Entity

- ``$select``\  in OData now supports selecting complex type(groups)

- `Creating a form </central-api-form-management/#creating-a-new-form>`__ can now return workflow warnings

**Removed**\ :

- Scheduled backups to Google Drive are no longer supported. As a result, backups are no longer configurable. It is no longer possible to get or terminate a backups configuration or to use a backups configuration to GET a Direct Backup. For more information about these changes, please see `this topic <https://forum.getodk.org/t/backups-to-google-drive-from-central-will-stop-working-after-jan-31st/38895>`__ in the ODK Forum.

ODK Central v2022.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

* Introducing `Datasets </central-api-dataset-management>`__ as the first step of Entity-Based Data Collection! Future versions of Central will build on these new concepts. We consider this functionality experimental and subject to change in the next release.

  * Forms can now create Datasets in the project, see `Creating a New Form </central-api-form-management/#creating-a-new-form>`__ and the `ODK XForms specification <https://getodk.github.io/xforms-spec>`__ for details.
  * New endpoint `GET /projects/:id/datasets </central-api-dataset-management/#datasets>`__ for listing Datasets of a project.
  * New endpoint `GET /projects/:id/datasets/:name/entities.csv </central-api-dataset-management/#download-dataset>`__ to download the Dataset as a CSV file.
  * New endpoints for `Related Datasets </central-api-form-management/#related-datasets>`__ to see the Datasets affected by published and unpublished Forms.
  * New endpoint `PATCH .../attachments/:name </central-api-form-management/#linking-a-dataset-to-a-draft-form-attachment>`__ to link/unlink a Dataset to a Form Attachment.

* OData Data Document requests now allow limited use of ``$select``\ .

**Changed**\ :

* The following endpoints have changed with the addition of Datasets:

  * The `Extended Project </central-api-project-management/#listing-projects>`__ endpoint now returns the ``datasets``\  count for the Project.
  * The `Extended Form </central-api-form-management/#list-all-forms>`__ endpoint now returns the ``entityRelated``\  flag if the form defines a Dataset schema.
  * `DELETE .../draft/attachments/:name </central-api-form-management/#clearing-a-draft-form-attachment>`__ will unlink the Dataset if there's a Dataset link to the attachment.
  * `GET .../draft/attachments/:filename <central-api-form-management/#downloading-a-form-attachment>`__ will return the Dataset as a CSV file if the attachment is linked to a Dataset.
  * `GET .../draft/attachments </central-api-form-management/#listing-expected-draft-form-attachments>`__ returns two additional flags ``blobExists``\  and ``datasetExists``\ .
  * In the `OpenRosa Form Manifest <central-api-form-management/#openrosa-form-manifest-api>`__, if a Form Attachment is linked to a Dataset then the value of ``hash``\  is the MD5 of the last updated timestamp or the MD5 of ``1970-01-01 00:00:00``\  if the Dataset is empty.

ODK Central v1.5.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Removed**\ :

* It is no longer possible to initiate a new backups configuration (``POST /v1/config/backups/initiate``\ ) or to verify one (``POST /v1/config/backups/verify``\ ). However, for now, if there is an existing configuration, it is still possible to get it or terminate it. If the existing configuration is terminated, it will not be possible to set up a new configuration. Note that it is still possible to download a `Direct Backup </central-api-system-endpoints/#direct-backup>`__. For more information about this change, please see `this topic <https://forum.getodk.org/t/backups-to-google-drive-from-central-will-stop-working-after-jan-31st/38895>`__ in the ODK Forum.

ODK Central v1.5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.5 adds editable Project descriptions as well as more detailed information about Forms and Submissions when listing Projects.

**Added**\ :

* New ``description``\  field returned for each `Project </central-api-project-management/#projects>`__ that can be set or updated through ``POST``\ /``PATCH``\ /``PUT``\  on ``/projects/…``\ 
    * Note that for the ``PUT``\  request, the Project's description must be included in the request. `Read more </central-api-project-management/#deep-updating-project-and-form-details>`__.

* `Form extended metadata </central-api-form-management/#getting-form-details>`__ now includes a ``reviewStates``\  object of counts of Submissions with specific review states.
    * e.g. ``{"received":12, "hasIssues":2, "edited":3}``\ 

* New ``?forms=true``\  option on `Project Listing </central-api-project-management/#listing-projects-with-nested-forms>`__ that includes a ``formList``\  field containing a list of extended Forms (and the review state counts described above) associated with that Project.

ODK Central v1.4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.4 enables additional CSV export options and creates an API-manageable 30 day permanent purge system for deleted Forms. Previously, deleted Forms were made inaccessible but the data was not purged from the database.

**Added**\ :

* New ``?groupPaths``\  and ``?splitSelectMultiples``\  options on `CSV export paths </central-api-submission-management/#exporting-form-submissions-to-csv>`__ which aim to replicate ODK Briefcase export behavior. One simplifies nested path names and the other breaks select multiple options out into multiple columns.

* New ``?deletedFields``\  option on `CSV export </central-api-submission-management/#exporting-form-submissions-to-csv>`__ which exports all previously known and deleted fields and data on the form.

* Deleted Forms (either by API ``DELETE``\  or through the web interface) are now placed in a 30 day hold, after which an automated process will permanently delete all data related to the Form.

  * You can see Forms in the 30 day wait by `listing Forms with ``?deleted=true``\  </central-api-form-management/#list-all-forms>`__. You can also see them in the Trash section on the web interface.
  * ``POST /projects/…/forms/…/restore``\  to restore a Form that hasn't yet been permanently purged.

* Additional metadata field 'formVersion' on `CSV export </central-api-submission-management/#exporting-form-submissions-to-csv>`__, `OData feed </central-api-odata-endpoints/#data-document>`__, and `extended Submission Version request </central-api-submission-management/#listing-versions>`__ which reports the version of the Form the Submission was *originally*\  created with.

* Additional metadata fields ``userAgent``\  and ``deviceId``\  tracked and returned for each `Submission Version </central-api-submission-management/#listing-versions>`__.

  * These are collected automatically upon submission through transmitted client metadata information, similar to the existing ``deviceId``\  field returned with each Submission.

ODK Central v1.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.3 adds granular Submission edit history, as well as opt-in usage reporting to the Central team.

**Added**\ :

* ``GET /projects/…/forms/…/submissions/…/diffs``\  will return the `changes between each version </central-api-submission-management/#getting-changes-between-versions>`__ of a Submission.

* You can set the `Usage Reporting configuration </central-api-system-endpoints/#usage-reporting-configuration>`__ to choose whether the server will share anonymous usage data with the Central team. By default, no usage information will be sent at all.

* You can also `preview the Usage Report </central-api-system-endpoints/#usage-report-preview>`__ to see exactly what information would be sent in a Usage Report.

**Changed**\ :

* Additional actions are now logged in the `Server Audit Log </central-api-system-endpoints/#server-audit-logs>`__:

  * A ``user.session.create``\  action will be logged when a User `logs in using Session Authentication </central-api-authentication/#logging-in>`__.
  * A ``form.submissions.export``\  action will be logged when a User exports Form Submissions to CSV.

* The Submission update timestamp is now included in OData (as ``**\ system/updatedAt``\ ). Resources that accept the ``$filter``\  query parameter can be filered on ``**\ \ system/updatedAt``\ .

* All groups are now included in OData, even if they are not relevant. For more information, see `this post <https://forum.getodk.org/t/include-non-relevant-groups-and-fields-in-odk-central-api-responses/33536>`__ in the ODK Forum.

* The ``Content-Disposition``\  header now specifies the ``filename*``\  parameter, allowing filenames to contain Unicode.

ODK Central v1.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.2 adds submission editing, review states, and commenting.

**Added**\ :

* ``POST /projects/…/submission``\  now accepts ecosystem-compatible submission updates over OpenRosa, using the ``deprecatedID``\ .

* REST-friendly submission updates by ``PUT``\ ing XML directly to the submission resource path.

* ``GET /projects/…/forms/…/submissions/…/edit``\  will now redirect the authenticated user (after some thought) to an Enketo-powered webform for editing the submission.

* There is now a subresource ``/projects/…/forms/…/submissions/…/versions``\  to get all versions of a submission, and details about each one, including submitted media files.

* There is now a subresource ``/projects/…/forms/…/submissions/…/comments``\  which allows very simple comment creation (``POST``\ ) and listing (``GET``\ ) on a submission.

* Submissions now have a ``reviewState``\  property which can be updated via ``PATCH /projects/…/forms/…/submissions``\ .

* You can now provide ``X-Action-Notes``\  on any API request that might generate audit logs, to leave a note on those log entries.

* ``GET /projects/…/forms/…/submissions/…/audits``\  will return just audit logs pertaining to that submission.

* OData queries may now request ``?expand=*``\  to request all nested data structures inline. Only ``*``\  is accepted.

* OData ``$filter``\  queries may now reference the new ``**\ system/reviewState``\  metadata field.

* There is now a `data download path </central-api-odata-endpoints/#data-download-path>`__ you can direct users to which eases media file access.

* Submissions now have an ``instanceName``\  field which reflects the ``<instanceName/>``\  tag on the submitted XML.

* The REST submission endpoint now accepts optional ``?deviceID=``\  just like the OpenRosa submission endpoint.

**Changed**\ :

* Unpublished Forms (Forms that only have a Draft and have never been published) will now appear with full details in ``GET /projects/…/forms``\ . Previously, values like ``name``\  would be ``null``\  for these Forms. You can still identify unpublished Forms as they will have a ``publishedAt``\  value of ``null``\ .

* Date and Boolean OData types are now given as date and boolean rather than text.

* Broke Forms and Submissions section apart into two below. This may break some links.

ODK Central v1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.1 adds minor new features to the API.

**Added**\ :

* ``POST``\ /``GET /backup``\ , will immediately perform a backup of the database and return the encrypted backup.

* ``POST``\ /``GET /projects/…/forms/…/submissions.csv``\ , which allows download of the root table (excluding repeat data) as CSV, without a zipfile.

* ``POST``\ /``GET /projects/…/forms/…/submissions.csv.zip``\  now allows ``?attachments=false``\  to exclude attachments.

* OData Data Document requests now allow limited use of ``$filter``\ .

* The various ``submissions.csv.*``\  endpoints also allow ``$filter``\ , using the same limited OData syntax.

* ``GET /projects/…/forms/…/submissions/submitters``\  which returns submitter Actors for a given Form.

**Fixed**\ :

* Documented the ``deviceId``\  property of submission, which was added in version 0.4.

ODK Central v1.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v1.0 adds Public Links to the API, and makes one minor breaking change.

**Added**\ :

* The new `Public Link </central-api-form-management/#public-access-links>`__ resource lets you create Public Access Links, granting anonymous browser-based access to submit to your Forms using Enketo.

**Changed**\ :

* The non-extended App User response no longer includes a ``createdBy``\  numeric ID. To retrieve the creator of an App User, request the extended response.

* We no longer reject the request if multiple authentication schemes are presented, and instead document the priority order of the different schemes `here </central-api-authentication>`__.

ODK Central v0.9
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v0.9 does not change the API except for one minor breaking change.

**Changed**\ :

* The `OpenRosa Form Listing API </central-api-openrosa-endpoints/#openrosa-form-listing-api>`__ has been modified to always require authentication. If a valid Actor is authenticated at all, a form list will always be returned, filtered by what that Actor is allowed to access.

ODK Central v0.8
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ODK Central v0.8 introduces Draft Forms, publishing, and archived Form versions, which has a significant breaking impact on the existing API. The changes should be straightforward to adapt to, however. If you are currently creating Forms with ``POST /projects/…/forms``\ , you may wish to add ``?publish=true``\  to skip the Draft state and mimic the old behaviour. If you are using the API to push Form Attachments onto Forms, you'll only be able to do so now in draft state, at ``/projects/…/forms/…/draft/attachments``\ .

**Added**\ :

* Draft Forms and publishing, and archived Form versions.

  * This includes `a subresource </central-api-form-management/#draft-form>`__ at ``/projects/…/forms/…/draft``\ ,
  * and `another </central-api-form-management/#published-form-versions>`__ at ``/projects/…/forms/…/versions``\ ,
  * and a `new collection of OpenRosa endpoints </central-api-openrosa-endpoints/#draft-testing-endpoints>`__, under ``/test/…/projects/…/forms/…/draft``\ , for submitting test submissions to the draft version of the form.

* ``GET /projects/…/forms/…/fields``\ , which replaces ``GET /projects/…/forms/….schema.json``\ .

* App User responses now include the ``projectId``\  they are bound to.

**Changed**\ :

* As part of the Draft Forms change, the read/write endpoints for Form Attachments have been moved to the Draft Form state and subresource, at ``/projects/…/forms/…/draft/attachments``\ .

**Removed**\ :

* ``GET /projects/…/forms/….schema.json``\  has been removed in favor of ``GET /projects/…/forms/…/fields``\ .

**Fixed**\ :

* Documented ``GET /projects/…/forms/….xls(x)``\ , which was added in 0.7.

ODK Central v0.7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

* Form-specific `Assignments resource </central-api-form-management/#form-assignments>`__ at ``projects/…/forms/…/assignments``\ , allowing granular role assignments on a per-Form basis.

  * Relatedly, the `OpenRosa Form Listing API </central-api-openrosa-endpoints/#openrosa-form-listing-api>`__ no longer rejects requests outright based on authentication. Rather, it will only return Forms that the authenticated user is allowed to view.
  * A `new summary API </central-api-project-management/#seeing-all-form-assignments-within-a-project>`__ ``GET /projects/…/assignments/forms``\  which returns all assignments on all Forms within a Project, so you don't have to request this information separately for each Form.

* ``PUT /projects/:id``\ , which while complex allows you to update many Forms' states and assignments with a single transactional request.

* ``POST /projects/…/forms``\  now allows upload of ``.xls``\  and ``.xlsx``\  XLSForm files. The correct MIME type must be given.

* ``GET /users/?q``\  will now always return user details given an exact match for an email, even for users who cannot ``user.list``\ . The request must still be authenticate as a valid Actor. This allows non-Administrators to choose a user for an action (eg grant rights) without allowing full search.

**Changed**\ :

* Newly created App Users are no longer automatically granted download and submission access to all Forms within their Project. You will want to use the `Form Assignments resource </central-api-form-management/#form-assignments>`__ to explicitly grant ``app-user``\  role access to the Forms they should be allowed to see.

**Fixed**\ :

* Correctly documented ``keyId``\  property on Projects.

ODK Central v0.6
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

* ``GET /audits``\  Server Audit Log retrieval resource.

* Project Managed Encryption:

  * ``POST /projects/…/key``\  to enable project managed encryption.
  * Both submission intake methods (OpenRosa and REST) now support encrypted submissions.
  * ``GET /projects/…/forms/…/submissions/keys``\  to get a list of encryption keys needed to decrypt all submitted data.
  * ``?{keyId}={passphrase}``\  option on ``GET /projects/…/forms/…/submissions.csv.zip``\  to get a decrypted archive given the ``passphrase``\ .
  * ``POST /projects/…/forms/…/submissions.csv.zip``\  to provide a browser-secure (no querystring) method of accessing the above ``GET .csv.zip``\  resource.
  * OData and ``.csv.zip``\  data responses now contain an additional ``status``\  system column.

* Form resource data now includes ``projectId``\  and 'keyId'.

* ``?odata=true``\  option on ``GET /projects/…/forms/….schema.json``\  to sanitize the field names to match the way they will be outputted for OData.

**Changed**\ :

* ``GET /projects/…/forms/…/attachments``\  now always returns ``updatedAt``\ . There is no longer a separate Extended Metadata response for this resource.

* The Submission response format now provides the submitter ID at ``submitterId``\  rather than ``submitter``\ . This is so that the Extended responses for Submissions can use ``submitter``\  to provide the full Actor subobject rather than replacing it. This brings the response format to be more similar to the other Extended formats.

* OData resources now namespace the ``**\ system``\  schema information under ``org.opendatakit.submission``\  rather than alongside user metadata (``org.opendatakit.user.*``\ ). The actual returned data has not changed; this is purely a metadata document change.

**Removed**\ :

* The Extended responses for Forms and Submissions no longer include an ``xml``\  property. To retrieve Form or Submission XML, use the dedicated endpoints for `Form XML </central-api-form-management/#retrieving-form-xml>`__ and `Submission XML </central-api-submission-management/#retrieving-submission-xml>`__.

ODK Central v0.5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

* Roles and Assignments resources at ``/roles``\ , ``/assignments``\ , and ``/projects/…/assignments``\ .

* Optional ``?q=``\  querystring parameter on Users ``GET``\  listing, for searching users.

* Extended ``GET /users/current``\ : added ``verbs``\  list of verbs the authenticated Actor may perform server-wide.

* Extended Project ``GET``\ : added ``appUsers``\  count of App Users and ``verbs``\  list of verbs the authenticated Actor may perform upon/within the Project.

* User ``DELETE``\ .

* Projects now have an ``archived``\  flag which may be set to clear a Project out of the way without deleting it.

**Changed**\ :

* **Removed**\  autopromotion of Users to Administrator upon creation (``POST``\ ). Roles must be assigned separately and explicitly.

* **Changed**\  Project Listing (``GET /projects``\ ) to never reject based on authentication; instead it filters the response based on the access of the authenticated Actor.

* **Changed**\  ``xmlFormId``\ /``version``\  conflict errors on ``POST``\ ing a new Form from a ``400``\  code to a ``409``\  code.

* **Changed**\  all remaining textual references to "Field Keys" to "App Users" in the documentation.

**Fixed**\ :

* Corrected Actor documentation to match reality: **removed**\  ``meta``\  field and added ``type``\  field.

* Corrected Extended Form documentation: **added**\  ``createdBy``\  field.

* Corrected Backup Config documentation. It was almost entirely wrong.

* Added Submission POST REST documentation.

ODK Central v0.4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Added**\ :

* Projects resource at ``/projects``\ .

* Submission XML resource fetch at ``GET /projects/…/forms/…/submissions/….xml``\ .

* Submission attachment management over REST, at the ``/attachments``\  subresource within Submissions.

**Changed**\ :

* **Renamed**\  all ``/field-keys``\  routes to ``/app-users``\ .

* **Moved**\  all Forms, Submissions, and App User resources under Projects (e.g. ``/forms/simple``\  would now be something like ``/projects/1/forms/simple``\ ).

* **Changed**\  ``GET``\  Form to not return Form XML. The Extended Metadata version of those requests will give the XML.

* **Changed**\  both OpenRosa and REST Submission creation processes to create and accept only the attachment filenames that are indicated to exist by the Submission XML.

* **Changed**\  ``GET``\  Submission Attachemnts listing to return an array of objects containing attachment details rather than an array of filename strings.


