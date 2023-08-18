.. auto generated file - DO NOT MODIFY 

Entity Management
=======================================================================================================================

.. raw:: html
  
  <p><em>(introduced: version 2023.3)</em></p><p>Version 2023.3 brings further core enhancements to Datasets and Entities, including several new endpoints for accessing information about Entities, as well as the ability to <em>create</em>,  <em>update</em>, and <em>soft-delete</em> Entities via the API.</p><p>An Entity is a specific person, place, or thing. Datasets represent collections of Entities. More information about how to set up and use Datasets can be found in the <a href="/central-api-dataset-management">Datasets</a> section of this documentation.</p>

Entities Metadata
---------------------------

**GET /projects/{projectId}/datasets/{name}/entities**

.. raw:: html

  <p>This endpoint returns a list of the Entities of a Dataset. Please note that this endpoint only returns metadata of the entities not the data. If you want to get the data of all entities then please refer to <a href="/central-api-odata-endpoints/#odata-form-service">OData Dataset Service</a>You can provide <code>?deleted=true</code> to get only deleted entities.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "uuid": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "updatedAt": "2018-03-21T12:45:02.312Z",
              "deletedAt": "2018-03-21T12:45:02.312Z",
              "creatorId": 1,
              "creator": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "currentVersion": {
                "label": "John (88)",
                "current": true,
                "createdAt": "2018-03-21T12:45:02.312Z",
                "creatorId": 1,
                "userAgent": "Enketo/3.0.4",
                "creator": {
                  "createdAt": "2018-04-18T23:19:14.802Z",
                  "displayName": "My Display Name",
                  "id": 115,
                  "type": "user",
                  "updatedAt": "2018-04-18T23:42:11.406Z",
                  "deletedAt": "2018-04-18T23:42:11.406Z"
                }
              }
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
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                     

              
      .. raw:: html

        <p>Extended Response</p>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                     
                * - creator


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
              
      
Creating an Entity
----------------------------

**POST /projects/{projectId}/datasets/{name}/entities**

.. raw:: html

  <p>Creates an Entity in the Dataset. Request body takes the JSON representation of the Entity. It should have <code>uuid</code> and <code>label</code> property in addition to the user-defined properties of the Dataset in <code>data</code> property.</p><p>Value type of all properties is <code>string</code>.</p><p>You can provide header <code>X-Action-Notes</code> to store the metadata about the request. The metadata can retrieved using <a href="/central-api-entities/#entity-audit-log">Entity Audit Log</a></p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "uuid": "54a405a0-53ce-4748-9788-d23a30cc3afa",
            "label": "John Doe (88)",
            "data": {
              "firstName": "John",
              "age": "88"
            }
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
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                * - label


                  - string
                  
                    .. raw:: html

                      <p>Label of the Entity</p>

                * - data


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``John``
                          * - age


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``88``
                     
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "uuid": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "deletedAt": "2018-03-21T12:45:02.312Z",
            "creatorId": 1,
            "currentVersion": {
              "label": "John (88)",
              "current": true,
              "createdAt": "2018-03-21T12:45:02.312Z",
              "creatorId": 1,
              "userAgent": "Enketo/3.0.4",
              "data": {
                "firstName": "John",
                "age": "88"
              }
            }
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
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``88``
                               
                     
              
      

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
              
      
Getting Entity Details
--------------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}**

.. raw:: html

  <p>This returns the metadata and current data of an Entity</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "uuid": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "deletedAt": "2018-03-21T12:45:02.312Z",
            "creatorId": 1,
            "creator": {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            },
            "currentVersion": {
              "label": "John (88)",
              "current": true,
              "createdAt": "2018-03-21T12:45:02.312Z",
              "creatorId": 1,
              "userAgent": "Enketo/3.0.4",
              "data": {
                "firstName": "John",
                "age": "88"
              },
              "creator": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              }
            }
          }

    .. tab-item:: Schema

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``88``
                               
                     

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - creator


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
                     
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``88``
                               
                     

              
      

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

              
      
Deleting an Entity
----------------------------

**DELETE /projects/{projectId}/datasets/{name}/entities/{uuid}**

.. raw:: html

  <p>Use this API to delete an Entity. With this API, Entity is soft-deleted, which means it is still in the database and you can retreive it by passing <code>?deleted=true</code> to <a href="/central-api-entities/#entities-metadata">GET /projects/:id/datasets/:name/entities</a>. In the future, we will provide a way to restore deleted entities and purge deleted entities.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "message": "Success"
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
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Success``
              
      

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

              
      
Updating an Entity
----------------------------

**PATCH /projects/{projectId}/datasets/{name}/entities/{uuid}**

.. raw:: html

  <p>Use this API to update one or all properties of an Entity. It will throw <code>400 - Bad Request</code> if any of the updating properties doesn't exist in the dataset.</p><p>To unset value of any property, you can set it to empty string (&quot;&quot;). Setting it to <code>null</code> will throw an error.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "label": "John Doe (88)",
            "data": {
              "firstName": "John",
              "age": "88"
            }
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
                
                
                * - label


                  - string
                  
                    .. raw:: html

                      <p>Label of the Entity</p>

                * - data


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``John``
                          * - age


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``88``
                     
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "uuid": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "deletedAt": "2018-03-21T12:45:02.312Z",
            "creatorId": 1,
            "currentVersion": {
              "label": "John (88)",
              "current": true,
              "createdAt": "2018-03-21T12:45:02.312Z",
              "creatorId": 1,
              "userAgent": "Enketo/3.0.4",
              "data": {
                "firstName": "John",
                "age": "88"
              }
            }
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
                
                
                * - uuid


                  - string
                  
                    .. raw:: html

                      <p>The <code>uuid</code> of the Entity that uniquely identifies the Entity.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the last update in ISO date format. <code>null</code> when there is only one version of the Entity.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>Timestamp of the deletion in ISO date format. <code>null</code> if the Entity is not deleted.</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              .. raw:: html

                                <p>Label of the Entity</p>

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>if the version is the latest one</p>

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                        Example: ``88``
                               
                     
              
      

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

              
      
Listing Versions
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/versions**

.. raw:: html

  <p>This returns the Entity metadata and data for every version of this Entity, in ascending creation order.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>creator</code> data object alongside the <code>creatorId</code> Actor ID reference.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "label": "John (88)",
              "current": true,
              "createdAt": "2018-03-21T12:45:02.312Z",
              "creatorId": 1,
              "userAgent": "Enketo/3.0.4",
              "data": {
                "firstName": "John",
                "age": "88"
              },
              "creator": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              }
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
                
                
                * - label


                  - string
                  
                    .. raw:: html

                      <p>Label of the Entity</p>

                    Example: ``John (88)``
                * - current


                  - boolean
                  
                    .. raw:: html

                      <p>if the version is the latest one</p>

                    Example: ``true``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                    Example: ``Enketo/3.0.4``
                * - data


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``John``
                          * - age


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``88``
                     

              
      .. raw:: html

        <p>Extended Response</p>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - label


                  - string
                  
                    .. raw:: html

                      <p>Label of the Entity</p>

                    Example: ``John (88)``
                * - current


                  - boolean
                  
                    .. raw:: html

                      <p>if the version is the latest one</p>

                    Example: ``true``
                * - creatorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor (App User, User, or Public Link) that originally created the Entity.</p>

                    Example: ``1``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that created the <code>Entity</code> version.</p>

                    Example: ``Enketo/3.0.4``
                * - data


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``John``
                          * - age


                            - string
                            
                              .. raw:: html

                                <span></span>

                              Example: ``88``
                     
                * - reator


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

              
      
Getting changes between Versions
------------------------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/diffs**

.. raw:: html

  <p>This returns the changes, or edits, between different versions of an Entity. These changes are returned as an array of arrays. Between two Entities, there is an array of objects representing how each property changed. This change object contains the old and new values, as well as the property name.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            [
              {
                "new": "John",
                "old": "Dana",
                "propertyName": "firstName"
              },
              {
                "new": "Doe",
                "old": "Roe",
                "propertyName": "lastName"
              },
              {
                "new": "John Doe",
                "old": "Jane Roe",
                "propertyName": "label"
              }
            ],
            [
              {
                "new": "Robert",
                "old": "Doe",
                "propertyName": "firstName"
              },
              {
                "new": "Robert Doe",
                "old": "Doe Doe",
                "propertyName": "label"
              }
            ]
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
                
                
                * - None


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - new


                            - string
                            
                              .. raw:: html

                                <p>The new value of this property.</p>

                              Example: ``John``
                          * - old


                            - string
                            
                              .. raw:: html

                                <p>The old value of this property.</p>

                              Example: ``Jane``
                          * - propertyName


                            - string
                            
                              .. raw:: html

                                <p>The name of the property that is changed.</p>

                              Example: ``name``
                     

              
      

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

              
      
Entity Audit Log
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/audits**

.. raw:: html

  <p>Returns <a href="/central-api-system-endpoints/#server-audit-logs">Server Audit Logs</a> relating to an Entity. They will be returned most recent first.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          .. raw:: html

            UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "actorId": 42,
              "action": "entity.create",
              "acteeId": "85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "loggedAt": "2018-04-18T23:19:14.802Z"
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

                      <p>The ID of the actor, if any, that initiated the action.</p>

                    Example: ``42``
                * - action


                  - string
                  
                    .. raw:: html

                      <p>The action that was taken.</p>

                    Example: ``form.create``
                * - acteeId


                  - string
                  
                    .. raw:: html

                      <p>The ID of the permissioning object against which the action was taken.</p>

                    Example: ``85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - details


                  - object
                  
                    .. raw:: html

                      <p>Additional details about the action that vary according to the type of action.</p>

                * - loggedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-04-18T23:19:14.802Z``

              
      

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

              
      

