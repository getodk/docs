.. auto generated file - DO NOT MODIFY 

Dataset Management
=======================================================================================================================

*(introduced: version 2022.3)*\ 

Version 2022.3 introduces server-managed Datasets as the first step on our `Entity-based data collection <https://forum.getodk.org/t/entity-based-data-collection/38115>`__ journey.

An Entity is a specific person, place, or thing. A Dataset is a collection of Entities. A Dataset is defined within a Form, and then a Submission to that Form creates an Entity when that Submission is **approved**\ . The Dataset definition includes the Dataset name and which Form fields map to which Dataset/Entity Properties, e.g. how to construct an Entity from a Submission.

See the `ODK XForms specification <https://getodk.github.io/xforms-spec>`__ for guidance on defining Datasets in Forms.

Once a Dataset exists, it can be linked to another Form as an Attachment and served as an automatically-updating CSV.

**Related APIs:**\ 

- `Implicit creation of Datasets via Forms </central-api-form-management/#forms/creating-a-new-form>`__

- `Link a Dataset to a Form Attachment </central-api-form-management/#linking-a-dataset-to-a-draft-form-attachment>`__

- `Get a Form's Related Datasets </central-api-form-management/#related-datasets>`__

Datasets
------------------

**GET /projects/{projectId}/datasets**

The Dataset listing endpoint returns all published Datasets in a Project. If a Draft Form defines a new Dataset, that Dataset will not be included in this list until the Form is published.

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

          "null"

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The name of the Dataset

                    Example: ``people``
                * - createdAt


                  - string
                  
                    ISO date format.

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - projectId


                  - number
                  
                    The numerical ID of the Project that the Dataset belongs to.

                    Example: ``1``
                * - approvalRequired


                  - boolean
                  
                    Control whether a Submission should be approved before an Entity is created from it.

                    Example: ``true``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The name of the Dataset

                    Example: ``people``
                * - createdAt


                  - string
                  
                    ISO date format.

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - projectId


                  - number
                  
                    The numerical ID of the Project that the Dataset belongs to.

                    Example: ``1``
                * - approvalRequired


                  - boolean
                  
                    Control whether a Submission should be approved before an Entity is created from it.

                    Example: ``true``
                * - lastEntity


                  - string
                  
                    ISO date format. The timestamp of the most recent entity, if any.

                    Example: ``2018-04-18 03:04:51.695000+00:00``
                * - entities


                  - number
                  
                    The number of Entities in the Dataset.

                    Example: ``10.0``

              
      

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
                  
                    

              
      
Dataset Metadata
--------------------------

**GET /projects/{projectId}/datasets/{name}**

Returns the metadata of a Dataset including properties and forms that create and consume the Dataset.

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

          "null"

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - linkedForms


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

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
                     
                * - properties


                  - array
                  
                    All properties of the Dataset

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - name


                            - string
                            
                              The name of the Property.

                              Example: ``the.age``
                          * - odataName


                            - string
                            
                              The name of the property as it will appear in OData. OData property names can only contain alphanumeric characters and underscores.

                              Example: ``the_age``
                          * - publishedAt


                            - string
                            
                              Publishing timestamp of the form that defined this property for the first time.

                              Example: ``2018-01-21T00:04:11.153Z``
                          * - forms


                            - array
                            
                              List of forms that create the property

                              Example: ``null``
                              
                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - xmlFormId


                                      - string
                                      
                                        The ``id``\  of this form as given in its XForms XML definition

                                        Example: ``simple``
                                    * - name


                                      - string
                                      
                                        The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition. Returns ``xmlFormId``\  if there is no title in the form definition.

                                        Example: ``Simple``

                               

                     

              
      

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
                  
                    

              
      
Update Dataset Metadata
---------------------------------

**PATCH /projects/{projectId}/datasets/{name}**

You can only update ``approvalRequired``\  using this endpoint. ``approvalRequired``\  flag controls the Entity creation flow; if it is ``true``\  then the Submission must be approved before an Entity can be created from it and if it is ``false``\  then an Entity is created as soon as the Submission is received by the ODK Central.

By default ``approvalRequired``\  is ``false``\  for the Datasets created after v2023.3. Datasets created prior to that will have ``approvalRequired``\  set to ``true``\ .

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
            "approvalRequired": true
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - approvalRequired


                  - boolean
                  
                    Control whether a Submission should be approved before an Entity is created from it.

                    Example: ``true``
              
  
  
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
                
                
                * - linkedForms


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

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
                     
                * - properties


                  - array
                  
                    All properties of the Dataset

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - name


                            - string
                            
                              The name of the Property.

                              Example: ``the.age``
                          * - odataName


                            - string
                            
                              The name of the property as it will appear in OData. OData property names can only contain alphanumeric characters and underscores.

                              Example: ``the_age``
                          * - publishedAt


                            - string
                            
                              Publishing timestamp of the form that defined this property for the first time.

                              Example: ``2018-01-21T00:04:11.153Z``
                          * - forms


                            - array
                            
                              List of forms that create the property

                              Example: ``null``
                              
                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - xmlFormId


                                      - string
                                      
                                        The ``id``\  of this form as given in its XForms XML definition

                                        Example: ``simple``
                                    * - name


                                      - string
                                      
                                        The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition. Returns ``xmlFormId``\  if there is no title in the form definition.

                                        Example: ``Simple``

                               

                     

              
      

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
                  
                    

              
      
Download Dataset
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities.csv**

Datasets (collections of Entities) can be used as Attachments in other Forms, but they can also be downloaded directly as a CSV file.

The CSV format closely matches the `OData Dataset Service </central-api-odata-endpoints/#odata-dataset-service>`__ format, with columns for system properties such as ``**\ id``\  (the Entity UUID), ``**\ \ createdAt``\ , ``**\ creatorName``\ , etc., the Entity Label ``label``\ , and the Dataset/Entity Properties themselves. If any Property for an given Entity is blank (e.g. it was not captured by that Form or was left blank), that field of the CSV is blank.

This endpoint supports ``ETag``\  header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in the ETag header. If you pass that value in the If-None-Match header of a subsequent request, then if the Dataset has not been changed since the previous request, you will receive ``304 Not Modified``\  response; otherwise you'll get the new data.

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

  Content Type: text/csv

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          name,label,first_name,last_name,age,favorite_color
          54a405a0-53ce-4748-9788-d23a30cc3afa,Amy Aardvark,Amy,Aardvark,45,
          0ee79b8b-9711-4aa0-9b7b-ece0a109b1b2,Beth Baboon,Beth,Baboon,19,yellow
          3fc9c54c-7d41-4258-b014-bfacedb95711,Cory Cat,Cory,Cat,,cyan
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: text/csv

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

