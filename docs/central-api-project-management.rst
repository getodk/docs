.. auto generated file - DO NOT MODIFY 

Project Management
=======================================================================================================================

Apart from staff users ("Web Users" in the Central management interface) and some site-wide configuration details like Usage Reporting, all of ODK Central's objects (Forms, Submissions, App Users) are partitioned by Project, and available only as subresources below the main Projects resource.


Projects
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.4)*\ 

You must create a containing Project before you can create any of its subobjects.

Listing Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects**

The Projects listing endpoint is somewhat unique in that it is freely accessible to anybody, even unauthenticated clients. Rather than reject the user with a ``403``\  or similar error, the Projects listing will only return Projects that the authenticated Actor is allowed to see. In most cases, this means that unauthenticated requests will receive ``[]``\  in reply.

Currently, there are no paging or filtering options, so listing ``Project``\ s will get you every Project you have access to.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``appUsers``\  count of App Users and ``forms``\  count of Forms within the Project, as well as the ``lastSubmission``\  timestamp of the latest submission to any for in the project, if any.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - forms

          *(query)*

        - boolean
        
          _(introduced: Version 1.5)_ If set to true then endpoint also returns the Forms that the authenticated Actor is allowed to see, with those Forms nested within their corresponding Project under a new parameter `formList`. The returned Forms will match structure of Forms requested with extended metadata (including additional `lastSubmission` timestamp and `submissions` and `reviewStates` counts)

          Example: ``true``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "id": 1,
              "name": "Default Project",
              "description": "Description of this Project to show on Central.",
              "keyId": 3,
              "archived": false,
              "appUsers": 4,
              "forms": 7,
              "lastSubmission": "2018-04-18T03:04:51.695Z",
              "datasets": 2
            }
          ]

    .. tab-item:: Schema

      **Standard Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                    Example: ``1``
                * - name


                  - string
                  
                    The name of the Project.

                    Example: ``Default Project``
                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                    Example: ``Description of this Project to show on Central.``
                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                    Example: ``3``
                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``

              
      **Extended Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                    Example: ``1``
                * - name


                  - string
                  
                    The name of the Project.

                    Example: ``Default Project``
                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                    Example: ``Description of this Project to show on Central.``
                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                    Example: ``3``
                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
                * - appUsers


                  - number
                  
                    The number of App Users created within this Project.

                    Example: ``4``
                * - forms


                  - number
                  
                    The number of forms within this Project.

                    Example: ``7``
                * - lastSubmission


                  - string
                  
                    ISO date format. The timestamp of the most recent submission to any form in this project, if any.

                    Example: ``2018-04-18T03:04:51.695Z``
                * - datasets


                  - number
                  
                    The number of Datasets within this Project.

                    Example: ``2``

              
      
Creating a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects**

To create a Project, the only information you must supply (via POST body) is the desired name of the Project.

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "name": "Project Name"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The desired name of the Project.

              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 1,
            "name": "Default Project",
            "description": "Description of this Project to show on Central.",
            "keyId": 3,
            "archived": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                * - name


                  - string
                  
                    The name of the Project.

                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Getting Project Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{id}**

To get just the details of a single Project, ``GET``\  its single resource route by its numeric ID.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``appUsers``\  count of App Users and ``forms``\  count of forms within the Project, as well as the ``lastSubmission``\  timestamp of the latest submission to any for in the project, if any.

In addition, the extended metadata version of this endpoint (but not the overall Project listing) returns an array of the ``verbs``\  the authenticated Actor is able to perform on/within the Project.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the Project

          Example: ``16``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 1,
            "name": "Default Project",
            "description": "Description of this Project to show on Central.",
            "keyId": 3,
            "archived": false,
            "appUsers": 4,
            "forms": 7,
            "lastSubmission": "2018-04-18T03:04:51.695Z",
            "datasets": 2,
            "verbs": [
              "form.create",
              "form.delete"
            ]
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                * - name


                  - string
                  
                    The name of the Project.

                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
                * - appUsers


                  - number
                  
                    The number of App Users created within this Project.

                * - forms


                  - number
                  
                    The number of forms within this Project.

                * - lastSubmission


                  - string
                  
                    ISO date format. The timestamp of the most recent submission to any form in this project, if any.

                * - datasets


                  - number
                  
                    The number of Datasets within this Project.

                * - verbs


                  - array
                  
                    The array of string verbs the authenticated Actor may perform on and within this Project.

                    Example: ``null``
                    
    

                     
              
      

  **HTTP Status: 403**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "pencil",
            "message": "pencil"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Deep Updating Project and Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PUT /v1/projects/{id}**

*(introduced: version 0.7)*\ 

When managing a large deployment, it can be necessary to make sweeping changes to all Form States and Assignments within it at once&mdash;when rolling out a new Form, for example, or replacing a deprecated version with a new revision.

For this purpose, we offer this ``PUT``\  resource, which allows a deep update of Project metadata, Form metadata, and Form Assignment metadata at once and transactionally using a nested data format.

One important mechanic to note immediately here is that we follow true ``PUT``\  semantics, meaning that the data you provide is not merged with existing data to form an update. With our usual ``PATCH``\  endpoints, we do this kind of merging and so data that you don't explicitly pass us is left alone. Because we allow the deletion of Form Assignments by way of omission with this API, we treat *all*\  omissions as an explicit specification to null the omitted field. This means that, for example, you must always re-specify the Project name, the Project description, and archival flag with every ``PUT``\ .

This adherence to ``PUT``\  semantics would normally imply that Forms could be created or deleted by way of this request, but such an operation could become incredibly complex. We currently return a ``501 Not Implemented``\  error if you supply nested Form information but you do not give us exactly the entire set of extant Forms.

You can inspect the Request format for this endpoint to see the exact nested data structure this endpoint accepts. Each level of increased granularity is optional: you may ``PUT``\  just Project metadata, with no ``forms``\  array, and you may ``PUT``\  Project and Form metadata but omit ``assignments``\  from any Form, in which case the omitted detail will be left as-is.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the Project

          Example: ``16``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "name": "New Project Name",
            "description": "New Project Description",
            "archived": false,
            "forms": [
              {
                "xmlFormId": "simple",
                "state": "open",
                "assignments": [
                  {
                    "roleId": 2,
                    "actorId": 14
                  },
                  {
                    "roleId": 2,
                    "actorId": 21
                  }
                ]
              },
              {
                "xmlFormId": "test",
                "state": "closed"
              }
            ]
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The desired name of the Project.

                * - description


                  - string
                  
                    The desired description of the Project.

                * - archived


                  - boolean
                  
                    Archives the Project.

                    Example: ``none``
                * - forms


                  - array
                  
                    If given, the Form metadata to update.

                    Example: ``null``
                    
    

                     
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 1,
            "name": "Default Project",
            "description": "Description of this Project to show on Central.",
            "keyId": 3,
            "archived": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                * - name


                  - string
                  
                    The name of the Project.

                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      

  **HTTP Status: 501**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "501.1",
            "message": "The requested feature $unsupported is not supported by this server."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Deleting a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{id}**

Deleting a Project will remove it from the management interface and make it permanently inaccessible. Do not do this unless you are certain you will never need any of its data again. For now, deleting a Project will not purge its Forms. (We will change that in a future release.)

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the Project

          Example: ``16``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "success": true
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Updating Project Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{id}**

The Project name may be updated, as well as the Project description and the ``archived``\  flag.

By default, ``archived``\  is not set, which is equivalent to ``false``\ . If ``archived``\  is set to ``true``\ , the Project will be sorted to the bottom of the list, and in the web management application the Project will become effectively read-only. API write access will not be affected.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the Project

          Example: ``16``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "name": "New Project Name",
            "description": "Description of this Project to show on Central.",
            "archived": true
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The desired name of the Project.

                * - description


                  - string
                  
                    The description of the Project.

                * - archived


                  - boolean
                  
                    Archives the Project.

                    Example: ``none``
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 1,
            "name": "Default Project",
            "description": "Description of this Project to show on Central.",
            "keyId": 3,
            "archived": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                * - name


                  - string
                  
                    The name of the Project.

                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Enabling Project Managed Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{id}/key**

*(introduced: version 0.6)*\ 

`Project Managed Encryption </central-api-encryption>`__ can be enabled via the API. To do this, ``POST``\  with the ``passphrase``\  and optionally a reminder ``hint``\  about the passphrase. If managed encryption is already enabled, a ``409``\  error response will be returned.

Enabling managed encryption will modify all unencrypted forms in the project, and as a result the ``version``\  of all forms within the project will also be modified. It is therefore best to enable managed encryption before devices are in the field. Any forms in the project that already have self-supplied encryption keys will be left alone.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the Project

          Example: ``16``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "passphrase": "super duper secret",
            "hint": "it was a secret"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - passphrase


                  - string
                  
                    The encryption passphrase. If this passphrase is lost, the data will be irrecoverable.

                * - hint


                  - string
                  
                    A reminder about the passphrase. This is primarily useful when multiple encryption keys and passphrases are being used, to tell them apart.

              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 1,
            "name": "Default Project",
            "description": "Description of this Project to show on Central.",
            "keyId": 3,
            "archived": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    The numerical ID of the Project.

                * - name


                  - string
                  
                    The name of the Project.

                * - description


                  - string
                  
                    The description of the Project, which is rendered as Markdown on Frontend.

                * - keyId


                  - number
                  
                    If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.

                * - archived


                  - boolean
                  
                    Whether the Project is archived or not. ``null``\  is equivalent to ``false``\ . All this does is sort the Project to the bottom of the list and disable management features in the web management application.

                    Example: ``none``
              
      

  **HTTP Status: 400**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "400",
            "message": "Could not parse the given data (2 chars) as json."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    

              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      

  **HTTP Status: 409**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "409.1",
            "message": "A resource already exists with id value(s) of 1."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      

Project Assignments
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.5)*\ 

There are multiple Assignments resources. This one, specific to the Project it is nested within, only governs Role assignments to that Project. Assigning an Actor a Role that grants, for example, a verb ``submission.create``\ , allows that Actor to create a submission anywhere within this Project. It is also possible to assign rights only to specific forms for actions related only to that form and its submissions: see the `Form Assignments resource </central-api-form-management/#form-assignments>`__ for information about this.

The `sitewide Assignments resource </central-api-accounts-and-users/#assignments>`__, at the API root, manages Role assignments for all objects across the server. Apart from this difference in scope, the introduction to that section contains information useful for understanding the following endpoints.

There are only one set of Roles, applicable to either scenario. There are not a separate set of Roles used only upon Projects or Forms.

Listing all Project Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments**

This will list every assignment upon this Project, in the form of ``actorId``\ /``roleId``\  pairs.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to expand the ``actorId``\  into a full ``actor``\  objects. The Role reference remains a numeric ID.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``2``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "actor": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "roleId": 4
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The numeric Actor ID being assigned.

                    Example: ``42``
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    The full Actor data for this assignment.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              All ``Actor``\ s, regardless of type, have a display name

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              The type of actor


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - user


                                      - string
                                      
                                        

                                    * - field_key


                                      - string
                                      
                                        

                                    * - public_link


                                      - string
                                      
                                        

                                    * - singleUse


                                      - string
                                      
                                        

                               
                          * - updatedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                    Example: ``403.1``
                * - message


                  - string
                  
                    

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Listing all Actors assigned some Project Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/{roleId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, this endpoint lists all ``Actors``\  that have been assigned that Role upon this particular Project.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18 23:19:14.802000+00:00``
                * - displayName


                  - string
                  
                    All ``Actor``\ s, regardless of type, have a display name

                    Example: ``My Display Name``
                * - id


                  - number
                  
                    

                    Example: ``115.0``
                * - type


                  - enum
                  
                    The type of actor


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - user


                            - string
                            
                              

                          * - field_key


                            - string
                            
                              

                          * - public_link


                            - string
                            
                              

                          * - singleUse


                            - string
                            
                              

                     
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18 23:42:11.406000+00:00``

              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                    Example: ``403.1``
                * - message


                  - string
                  
                    

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Assigning an Actor to a Project Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , assigns that Role to that Actor for this particular Project.

No ``POST``\  body data is required, and if provided it will be ignored.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - actorId


        - number
        
          The integer ID of the `Actor`.

          Example: ``14``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "success": true
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Revoking a Project Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , unassigns that Role from that Actor for this particular Project.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - actorId


        - number
        
          The integer ID of the `Actor`.

          Example: ``14``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "success": true
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    

                    Example: ``none``
              
      

  **HTTP Status: 403**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                * - message


                  - string
                  
                    

              
      
Seeing all Form Assignments within a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/forms**

Returns a summary of all *Form-specific*\  Assignments within this Project. This endpoint is meant to simplify the task of summarizing all Form permissions within a Project at a glance and in one transactional request. Because it is necessary to specify which Form each Assignment is attached to, returned results form this endpoint include an ``xmlFormId``\  field.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to expand the ``actorId``\  into a full ``actor``\  objects. The Role reference remains a numeric ID and the Form reference remains a string ID.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "actor": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "xmlFormId": "simple",
              "roleId": 4
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The numeric Actor ID being assigned.

                    Example: ``42``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of the assigned form as given in its XForms XML definition

                    Example: ``simple``
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              All ``Actor``\ s, regardless of type, have a display name

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              The type of actor


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - user


                                      - string
                                      
                                        

                                    * - field_key


                                      - string
                                      
                                        

                                    * - public_link


                                      - string
                                      
                                        

                                    * - singleUse


                                      - string
                                      
                                        

                               
                          * - updatedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - xmlFormId


                  - string
                  
                    The ``id``\  of the assigned form as given in its XForms XML definition

                    Example: ``simple``
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              
      

  **HTTP Status: 403**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                    Example: ``403.1``
                * - message


                  - string
                  
                    

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Seeing Role-specific Form Assignments within a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/forms/{roleId}**

Like the `Form Assignments summary API </central-api-form-management/#listing-all-form-assignments>`__, but filtered by some ``roleId``\ .

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to expand the ``actorId``\  into a full ``actor``\  objects. The Role reference remains a numeric ID and the Form reference remains a string ID.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - roleId


        - number
        
          The numeric ID of the Role

          Example: ``16``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "actor": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "xmlFormId": "simple",
              "roleId": 4
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The numeric Actor ID being assigned.

                    Example: ``42``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of the assigned form as given in its XForms XML definition

                    Example: ``simple``
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              All ``Actor``\ s, regardless of type, have a display name

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              The type of actor


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - user


                                      - string
                                      
                                        

                                    * - field_key


                                      - string
                                      
                                        

                                    * - public_link


                                      - string
                                      
                                        

                                    * - singleUse


                                      - string
                                      
                                        

                               
                          * - updatedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              ISO date format

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - xmlFormId


                  - string
                  
                    The ``id``\  of the assigned form as given in its XForms XML definition

                    Example: ``simple``
                * - roleId


                  - number
                  
                    The numeric Role ID being assigned.

                    Example: ``4``

              
      

  **HTTP Status: 403**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "403.1",
            "message": "The authenticated actor does not have rights to perform that action."
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    

                    Example: ``403.1``
                * - message


                  - string
                  
                    

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      

