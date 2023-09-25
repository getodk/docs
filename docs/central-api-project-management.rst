.. auto generated file - DO NOT MODIFY 

Project Management
=======================================================================================================================

.. raw:: html
  
  <p>Apart from staff users (&quot;Web Users&quot; in the Central management interface) and some site-wide configuration details like Usage Reporting, all of ODK Central's objects (Forms, Submissions, App Users) are partitioned by Project, and available only as subresources below the main Projects resource.</p>


Projects
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.4)</em></p><p>You must create a containing Project before you can create any of its subobjects.</p>

Listing Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects**

.. raw:: html

  <p>The Projects listing endpoint is somewhat unique in that it is freely accessible to anybody, even unauthenticated clients. Rather than reject the user with a <code>403</code> or similar error, the Projects listing will only return Projects that the authenticated Actor is allowed to see. In most cases, this means that unauthenticated requests will receive <code>[]</code> in reply.</p><p>Currently, there are no paging or filtering options, so listing <code>Project</code>s will get you every Project you have access to.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>appUsers</code> count of App Users and <code>forms</code> count of Forms within the Project, as well as the <code>lastSubmission</code> timestamp of the latest submission to any for in the project, if any.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - forms

          *(query)*

        - boolean
        
          .. raw:: html

            _(introduced: Version 1.5)_ If set to true then endpoint also returns the Forms that the authenticated Actor is allowed to see, with those Forms nested within their corresponding Project under a new parameter `formList`. The returned Forms will match structure of Forms requested with extended metadata (including additional `lastSubmission` timestamp and `submissions` and `reviewStates` counts)

          Example: ``true``
      * - datasets

          *(query)*

        - boolean
        
          .. raw:: html

            _(introduced: Version 2023.4)_ If set to true then endpoint also returns the Datasets that the authenticated Actor is allowed to see, with those Datasets nested within their corresponding Project under a new parameter `datasetList`. The returned Datasets will match structure of Datasets requested with extended metadata (including additional `lastEntity` timestamp and `entities`)

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

      .. raw:: html

        <p>Standard Response</p>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                    Example: ``1``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                    Example: ``Default Project``
                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                    Example: ``Description of this Project to show on Central.``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                    Example: ``3``
                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

                    Example: ``none``

              
      .. raw:: html

        <p>Extended Response</p>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                    Example: ``1``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                    Example: ``Default Project``
                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                    Example: ``Description of this Project to show on Central.``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                    Example: ``3``
                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

                    Example: ``none``
                * - appUsers


                  - number
                  
                    .. raw:: html

                      <p>The number of App Users created within this Project.</p>

                    Example: ``4``
                * - forms


                  - number
                  
                    .. raw:: html

                      <p>The number of forms within this Project.</p>

                    Example: ``7``
                * - lastSubmission


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The timestamp of the most recent submission to any form in this project, if any.</p>

                    Example: ``2018-04-18T03:04:51.695Z``
                * - datasets


                  - number
                  
                    .. raw:: html

                      <p>The number of Datasets within this Project.</p>

                    Example: ``2``

              
      
Creating a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects**

.. raw:: html

  <p>To create a Project, the only information you must supply (via POST body) is the desired name of the Project.</p>

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "name": "Project Name"
          }

    .. tab-item:: Schema

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The desired name of the Project.</p>

              
  
  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Getting Project Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{id}**

.. raw:: html

  <p>To get just the details of a single Project, <code>GET</code> its single resource route by its numeric ID.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>appUsers</code> count of App Users and <code>forms</code> count of forms within the Project, as well as the <code>lastSubmission</code> timestamp of the latest submission to any for in the project, if any.</p><p>In addition, the extended metadata version of this endpoint (but not the overall Project listing) returns an array of the <code>verbs</code> the authenticated Actor is able to perform on/within the Project.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

                    Example: ``none``
                * - appUsers


                  - number
                  
                    .. raw:: html

                      <p>The number of App Users created within this Project.</p>

                * - forms


                  - number
                  
                    .. raw:: html

                      <p>The number of forms within this Project.</p>

                * - lastSubmission


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The timestamp of the most recent submission to any form in this project, if any.</p>

                * - datasets


                  - number
                  
                    .. raw:: html

                      <p>The number of Datasets within this Project.</p>

                * - verbs


                  - array
                  
                    .. raw:: html

                      <p>The array of string verbs the authenticated Actor may perform on and within this Project.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Deep Updating Project and Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PUT /v1/projects/{id}**

.. raw:: html

  <p><em>(introduced: version 0.7)</em></p><p>When managing a large deployment, it can be necessary to make sweeping changes to all Form States and Assignments within it at once—when rolling out a new Form, for example, or replacing a deprecated version with a new revision.</p><p>For this purpose, we offer this <code>PUT</code> resource, which allows a deep update of Project metadata, Form metadata, and Form Assignment metadata at once and transactionally using a nested data format.</p><p>One important mechanic to note immediately here is that we follow true <code>PUT</code> semantics, meaning that the data you provide is not merged with existing data to form an update. With our usual <code>PATCH</code> endpoints, we do this kind of merging and so data that you don't explicitly pass us is left alone. Because we allow the deletion of Form Assignments by way of omission with this API, we treat <em>all</em> omissions as an explicit specification to null the omitted field. This means that, for example, you must always re-specify the Project name, the Project description, and archival flag with every <code>PUT</code>.</p><p>This adherence to <code>PUT</code> semantics would normally imply that Forms could be created or deleted by way of this request, but such an operation could become incredibly complex. We currently return a <code>501 Not Implemented</code> error if you supply nested Form information but you do not give us exactly the entire set of extant Forms.</p><p>You can inspect the Request format for this endpoint to see the exact nested data structure this endpoint accepts. Each level of increased granularity is optional: you may <code>PUT</code> just Project metadata, with no <code>forms</code> array, and you may <code>PUT</code> Project and Form metadata but omit <code>assignments</code> from any Form, in which case the omitted detail will be left as-is.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The desired name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The desired description of the Project.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Archives the Project.</p>

                    Example: ``none``
                * - forms


                  - array
                  
                    .. raw:: html

                      <p>If given, the Form metadata to update.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Deleting a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{id}**

.. raw:: html

  <p>Deleting a Project will remove it from the management interface and make it permanently inaccessible. Do not do this unless you are certain you will never need any of its data again. For now, deleting a Project will not purge its Forms. (We will change that in a future release.)</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    .. raw:: html

                      <span></span>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Updating Project Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{id}**

.. raw:: html

  <p>The Project name may be updated, as well as the Project description and the <code>archived</code> flag.</p><p>By default, <code>archived</code> is not set, which is equivalent to <code>false</code>. If <code>archived</code> is set to <code>true</code>, the Project will be sorted to the bottom of the list, and in the web management application the Project will become effectively read-only. API write access will not be affected.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The desired name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Archives the Project.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Enabling Project Managed Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{id}/key**

.. raw:: html

  <p><em>(introduced: version 0.6)</em></p><p><a href="/central-api-encryption">Project Managed Encryption</a> can be enabled via the API. To do this, <code>POST</code> with the <code>passphrase</code> and optionally a reminder <code>hint</code> about the passphrase. If managed encryption is already enabled, a <code>409</code> error response will be returned.</p><p>Enabling managed encryption will modify all unencrypted forms in the project, and as a result the <code>version</code> of all forms within the project will also be modified. It is therefore best to enable managed encryption before devices are in the field. Any forms in the project that already have self-supplied encryption keys will be left alone.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - passphrase


                  - string
                  
                    .. raw:: html

                      <p>The encryption passphrase. If this passphrase is lost, the data will be irrecoverable.</p>

                * - hint


                  - string
                  
                    .. raw:: html

                      <p>A reminder about the passphrase. This is primarily useful when multiple encryption keys and passphrases are being used, to tell them apart.</p>

              
  
  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project.</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Project.</p>

                * - description


                  - string
                  
                    .. raw:: html

                      <p>The description of the Project, which is rendered as Markdown on Frontend.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If managed encryption is enabled on the project, the numeric ID of the encryption key as tracked by Central is given here.</p>

                * - archived


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the Project is archived or not. <code>null</code> is equivalent to <code>false</code>. All this does is sort the Project to the bottom of the list and disable management features in the web management application.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - details


                  - object
                  
                    .. raw:: html

                      <p>a subobject that contains programmatically readable details about this error</p>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      

Project Assignments
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.5)</em></p><p>There are multiple Assignments resources. This one, specific to the Project it is nested within, only governs Role assignments to that Project. Assigning an Actor a Role that grants, for example, a verb <code>submission.create</code>, allows that Actor to create a submission anywhere within this Project. It is also possible to assign rights only to specific forms for actions related only to that form and its submissions: see the <a href="/central-api-form-management/#form-assignments">Form Assignments resource</a> for information about this.</p><p>The <a href="/central-api-accounts-and-users/#assignments">sitewide Assignments resource</a>, at the API root, manages Role assignments for all objects across the server. Apart from this difference in scope, the introduction to that section contains information useful for understanding the following endpoints.</p><p>There are only one set of Roles, applicable to either scenario. There are not a separate set of Roles used only upon Projects or Forms.</p>

Listing all Project Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments**

.. raw:: html

  <p>This will list every assignment upon this Project, in the form of <code>actorId</code>/<code>roleId</code> pairs.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to expand the <code>actorId</code> into a full <code>actor</code> objects. The Role reference remains a numeric ID.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Actor ID being assigned.</p>

                    Example: ``42``
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

                    Example: ``4``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    .. raw:: html

                      <p>The full Actor data for this assignment.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              .. raw:: html

                                <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              .. raw:: html

                                <span></span>

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              .. raw:: html

                                <p>The type of actor</p>


                                
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
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``403.1``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Listing all Actors assigned some Project Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/{roleId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, this endpoint lists all <code>Actors</code> that have been assigned that Role upon this particular Project.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          .. raw:: html

            Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - projectId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-04-18 23:19:14.802000+00:00``
                * - displayName


                  - string
                  
                    .. raw:: html

                      <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                    Example: ``My Display Name``
                * - id


                  - number
                  
                    .. raw:: html

                      <span></span>

                    Example: ``115.0``
                * - type


                  - enum
                  
                    .. raw:: html

                      <p>The type of actor</p>


                      
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
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``403.1``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Assigning an Actor to a Project Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, assigns that Role to that Actor for this particular Project.</p><p>No <code>POST</code> body data is required, and if provided it will be ignored.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``16``
      * - roleId


        - string
        
          .. raw:: html

            Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - actorId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    .. raw:: html

                      <span></span>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Revoking a Project Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, unassigns that Role from that Actor for this particular Project.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``16``
      * - roleId


        - string
        
          .. raw:: html

            Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``
      * - actorId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - success


                  - boolean
                  
                    .. raw:: html

                      <span></span>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Seeing all Form Assignments within a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/forms**

.. raw:: html

  <p>Returns a summary of all <em>Form-specific</em> Assignments within this Project. This endpoint is meant to simplify the task of summarizing all Form permissions within a Project at a glance and in one transactional request. Because it is necessary to specify which Form each Assignment is attached to, returned results form this endpoint include an <code>xmlFormId</code> field.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to expand the <code>actorId</code> into a full <code>actor</code> objects. The Role reference remains a numeric ID and the Form reference remains a string ID.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Actor ID being assigned.</p>

                    Example: ``42``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of the assigned form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

                    Example: ``4``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              .. raw:: html

                                <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              .. raw:: html

                                <span></span>

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              .. raw:: html

                                <p>The type of actor</p>


                                
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
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of the assigned form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``403.1``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Seeing Role-specific Form Assignments within a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/assignments/forms/{roleId}**

.. raw:: html

  <p>Like the <a href="/central-api-form-management/#listing-all-form-assignments">Form Assignments summary API</a>, but filtered by some <code>roleId</code>.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to expand the <code>actorId</code> into a full <code>actor</code> objects. The Role reference remains a numeric ID and the Form reference remains a string ID.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``16``
      * - roleId


        - number
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Actor ID being assigned.</p>

                    Example: ``42``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of the assigned form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

                    Example: ``4``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actor


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:19:14.802000+00:00``
                          * - displayName


                            - string
                            
                              .. raw:: html

                                <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                              Example: ``My Display Name``
                          * - id


                            - number
                            
                              .. raw:: html

                                <span></span>

                              Example: ``115.0``
                          * - type


                            - enum
                            
                              .. raw:: html

                                <p>The type of actor</p>


                                
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
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                          * - deletedAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                              Example: ``2018-04-18 23:42:11.406000+00:00``
                     
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of the assigned form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - roleId


                  - number
                  
                    .. raw:: html

                      <p>The numeric Role ID being assigned.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - code


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``403.1``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      

