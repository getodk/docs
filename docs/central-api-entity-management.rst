.. auto generated file - DO NOT MODIFY 

Entity Management
=======================================================================================================================

*(introduced: version 2023.3)*\ 

Version 2023.3 brings further core enhancements to Datasets and Entities, including several new endpoints for accessing information about Entities, as well as the ability to *create*\ ,  *update*\ , and *soft-delete*\  Entities via the API.

An Entity is a specific person, place, or thing. Datasets represent collections of Entities. More information about how to set up and use Datasets can be found in the `Datasets </central-api-dataset-management>`__ section of this documentation.

Entities Metadata
---------------------------

**GET /projects/{projectId}/datasets/{name}/entities**

This endpoint returns a list of the Entities of a Dataset. Please note that this endpoint only returns metadata of the entities not the data. If you want to get the data of all entities then please refer to `OData Dataset Service </central-api-odata-endpoints/#odata-form-service>`__
You can provide ``?deleted=true``\  to get only deleted entities.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
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

      **Standard Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                     

              
      **Extended Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                     
                * - creator


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
              
      
Creating an Entity
----------------------------

**POST /projects/{projectId}/datasets/{name}/entities**

Creates an Entity in the Dataset. Request body takes the JSON representation of the Entity. It should have ``uuid``\  and ``label``\  property in addition to the user-defined properties of the Dataset in ``data``\  property.

Value type of all properties is ``string``\ .

You can provide header ``X-Action-Notes``\  to store the metadata about the request. The metadata can retrieved using `Entity Audit Log </central-api-entities/#entity-audit-log>`__

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                * - label


                  - string
                  
                    Label of the Entity

                * - data


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              

                              Example: ``John``
                          * - age


                            - string
                            
                              

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        

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
              
      
Getting Entity Details
--------------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}**

This returns the metadata and current data of an Entity

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
          UUID of the Entity

          Example: ``54a405a0-53ce-4748-9788-d23a30cc3afa``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "null"

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        

                                        Example: ``88``
                               
                     

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - creator


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
                     
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        

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
                  
                    

              
      
Deleting an Entity
----------------------------

**DELETE /projects/{projectId}/datasets/{name}/entities/{uuid}**

Use this API to delete an Entity. With this API, Entity is soft-deleted, which means it is still in the database and you can retreive it by passing ``?deleted=true``\  to `GET /projects/:id/datasets/:name/entities </central-api-entities/#entities-metadata>`__. In the future, we will provide a way to restore deleted entities and purge deleted entities.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    

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
                  
                    

              
      
Updating an Entity
----------------------------

**PATCH /projects/{projectId}/datasets/{name}/entities/{uuid}**

Use this API to update one or all properties of an Entity. It will throw ``400 - Bad Request``\  if any of the updating properties doesn't exist in the dataset.

To unset value of any property, you can set it to empty string (""). Setting it to ``null``\  will throw an error.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - label


                  - string
                  
                    Label of the Entity

                * - data


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              

                              Example: ``John``
                          * - age


                            - string
                            
                              

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - uuid


                  - string
                  
                    The ``uuid``\  of the Entity that uniquely identifies the Entity.

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    Timestamp of the last update in ISO date format. ``null``\  when there is only one version of the Entity.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - deletedAt


                  - string
                  
                    Timestamp of the deletion in ISO date format. ``null``\  if the Entity is not deleted.

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - currentVersion


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - label


                            - string
                            
                              Label of the Entity

                              Example: ``John (88)``
                          * - current


                            - boolean
                            
                              if the version is the latest one

                              Example: ``true``
                          * - creatorId


                            - number
                            
                              The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                              Example: ``1``
                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                              Example: ``Enketo/3.0.4``
                          * - data


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - firstName


                                      - string
                                      
                                        

                                        Example: ``John``
                                    * - age


                                      - string
                                      
                                        

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
                  
                    

              
      
Listing Versions
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/versions**

This returns the Entity metadata and data for every version of this Entity, in ascending creation order.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``creator``\  data object alongside the ``creatorId``\  Actor ID reference.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
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

      **Standard Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - label


                  - string
                  
                    Label of the Entity

                    Example: ``John (88)``
                * - current


                  - boolean
                  
                    if the version is the latest one

                    Example: ``true``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                    Example: ``Enketo/3.0.4``
                * - data


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              

                              Example: ``John``
                          * - age


                            - string
                            
                              

                              Example: ``88``
                     

              
      **Extended Response**

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - label


                  - string
                  
                    Label of the Entity

                    Example: ``John (88)``
                * - current


                  - boolean
                  
                    if the version is the latest one

                    Example: ``true``
                * - creatorId


                  - number
                  
                    The ID of the Actor (App User, User, or Public Link) that originally created the Entity.

                    Example: ``1``
                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that created the ``Entity``\  version.

                    Example: ``Enketo/3.0.4``
                * - data


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - firstName


                            - string
                            
                              

                              Example: ``John``
                          * - age


                            - string
                            
                              

                              Example: ``88``
                     
                * - reator


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
                  
                    

              
      
Getting changes between Versions
------------------------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/diffs**

This returns the changes, or edits, between different versions of an Entity. These changes are returned as an array of arrays. Between two Entities, there is an array of objects representing how each property changed. This change object contains the old and new values, as well as the property name.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - None


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - new


                            - string
                            
                              The new value of this property.

                              Example: ``John``
                          * - old


                            - string
                            
                              The old value of this property.

                              Example: ``Jane``
                          * - propertyName


                            - string
                            
                              The name of the property that is changed.

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
                  
                    

              
      
Entity Audit Log
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities/{uuid}/audits**

Returns `Server Audit Logs </central-api-system-endpoints/#server-audit-logs>`__ relating to an Entity. They will be returned most recent first.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - uuid


        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The ID of the actor, if any, that initiated the action.

                    Example: ``42``
                * - action


                  - string
                  
                    The action that was taken.

                    Example: ``form.create``
                * - acteeId


                  - string
                  
                    The ID of the permissioning object against which the action was taken.

                    Example: ``85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - details


                  - object
                  
                    Additional details about the action that vary according to the type of action.

                * - loggedAt


                  - string
                  
                    ISO date format

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
                  
                    

              
      

