.. auto generated file - DO NOT MODIFY 

Dataset Management
=======================================================================================================================

.. raw:: html
  
  <p><em>(introduced: version 2022.3)</em></p><blockquote><p>⚠️  In this API and in the related <a href="https://getodk.github.io/xforms-spec/entities">ODK XForms specification</a>, collections of <code>Entities</code> are referred to as <code>Datasets</code>. The term &quot;Entity List&quot; is used for this concept in the Central frontend UI, user documentation, and all other text intended for end users who are not developers.</p></blockquote><p>A Dataset is a named collection of <a href="/central-api-entity-management/">Entities</a> that have the same properties.</p><p>A Dataset can be linked to Forms as Attachments. This will make it available to clients as an automatically-updating CSV.</p><p><strong>Related APIs:</strong></p><ul><li><p><a href="/central-api-form-management/#forms/creating-a-new-form">Implicit creation of Datasets via Forms</a></p></li><li><p><a href="/central-api-form-management/#linking-a-dataset-to-a-draft-form-attachment">Link a Dataset to a Form Attachment</a></p></li><li><p><a href="/central-api-form-management/#related-datasets">Get a Form's Related Datasets</a></p></li></ul>

Datasets
------------------

**GET /projects/{projectId}/datasets**

.. raw:: html

  <p>The Dataset listing endpoint returns all published Datasets in a Project. If a Draft Form defines a new Dataset, that Dataset will not be included in this list until the Form is published.</p>

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
              "name": "people",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "projectId": 1,
              "approvalRequired": true,
              "lastEntity": "2018-04-18T03:04:51.695Z",
              "entities": 10
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
                
                
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Dataset</p>

                    Example: ``people``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format.</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project that the Dataset belongs to.</p>

                    Example: ``1``
                * - approvalRequired


                  - boolean
                  
                    .. raw:: html

                      <p>Control whether a Submission should be approved before an Entity is created from it.</p>

                    Example: ``true``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The name of the Dataset</p>

                    Example: ``people``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format.</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Project that the Dataset belongs to.</p>

                    Example: ``1``
                * - approvalRequired


                  - boolean
                  
                    .. raw:: html

                      <p>Control whether a Submission should be approved before an Entity is created from it.</p>

                    Example: ``true``
                * - lastEntity


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The timestamp of the most recent entity, if any.</p>

                    Example: ``2018-04-18 03:04:51.695000+00:00``
                * - entities


                  - number
                  
                    .. raw:: html

                      <p>The number of Entities in the Dataset.</p>

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

              
      
Dataset Metadata
--------------------------

**GET /projects/{projectId}/datasets/{name}**

.. raw:: html

  <p>Returns the metadata of a published Dataset including properties and forms that create and consume the Dataset.</p>

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

          {
            "name": "people",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "projectId": 1,
            "approvalRequired": true,
            "sourceForms": [
              {
                "xmlFormId": "treeRegistration",
                "name": "Tree Registration"
              }
            ],
            "linkedForms": [
              {
                "xmlFormId": "simple",
                "name": "Simple"
              }
            ],
            "properties": [
              {
                "name": "the.age",
                "odataName": "the_age",
                "publishedAt": "2018-01-21T00:04:11.153Z",
                "forms": [
                  {
                    "xmlFormId": "simple",
                    "name": "Simple"
                  }
                ]
              }
            ]
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
                
                
                * - linkedForms


                  - array
                  
                    .. raw:: html

                      <p>Forms that consume data from the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - xmlFormId


                            - string
                            
                              .. raw:: html

                                <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                              Example: ``simple``
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

                              Example: ``Simple``

                     
                * - sourceForms


                  - array
                  
                    .. raw:: html

                      <p>Forms that create Entities in the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - xmlFormId


                            - string
                            
                              .. raw:: html

                                <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                              Example: ``simple``
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

                              Example: ``Simple``

                     
                * - properties


                  - array
                  
                    .. raw:: html

                      <p>All properties of the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The name of the Property.</p>

                              Example: ``the.age``
                          * - odataName


                            - string
                            
                              .. raw:: html

                                <p>The name of the property as it will appear in OData. OData property names can only contain alphanumeric characters and underscores.</p>

                              Example: ``the_age``
                          * - publishedAt


                            - string
                            
                              .. raw:: html

                                <p>Publishing timestamp of the form that defined this property for the first time.</p>

                              Example: ``2018-01-21T00:04:11.153Z``
                          * - forms


                            - array
                            
                              .. raw:: html

                                <p>List of forms that create the property</p>

                              Example: ``null``
                              
                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - xmlFormId


                                      - string
                                      
                                        .. raw:: html

                                          <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                                        Example: ``simple``
                                    * - name


                                      - string
                                      
                                        .. raw:: html

                                          <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

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

              
      
Update Dataset Metadata
---------------------------------

**PATCH /projects/{projectId}/datasets/{name}**

.. raw:: html

  <p>You can only update <code>approvalRequired</code> using this endpoint. <code>approvalRequired</code> flag controls the Entity creation flow; if it is <code>true</code> then the Submission must be approved before an Entity can be created from it and if it is <code>false</code> then an Entity is created as soon as the Submission is received by the ODK Central.</p><p>By default <code>approvalRequired</code> is <code>false</code> for the Datasets created after v2023.3. Datasets created prior to that will have <code>approvalRequired</code> set to <code>true</code>.</p>

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
            "approvalRequired": true
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
                
                
                * - approvalRequired


                  - boolean
                  
                    .. raw:: html

                      <p>Control whether a Submission should be approved before an Entity is created from it.</p>

                    Example: ``true``
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "name": "people",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "projectId": 1,
            "approvalRequired": true,
            "sourceForms": [
              {
                "xmlFormId": "treeRegistration",
                "name": "Tree Registration"
              }
            ],
            "linkedForms": [
              {
                "xmlFormId": "simple",
                "name": "Simple"
              }
            ],
            "properties": [
              {
                "name": "the.age",
                "odataName": "the_age",
                "publishedAt": "2018-01-21T00:04:11.153Z",
                "forms": [
                  {
                    "xmlFormId": "simple",
                    "name": "Simple"
                  }
                ]
              }
            ]
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
                
                
                * - linkedForms


                  - array
                  
                    .. raw:: html

                      <p>Forms that consume data from the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - xmlFormId


                            - string
                            
                              .. raw:: html

                                <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                              Example: ``simple``
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

                              Example: ``Simple``

                     
                * - sourceForms


                  - array
                  
                    .. raw:: html

                      <p>Forms that create Entities in the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - xmlFormId


                            - string
                            
                              .. raw:: html

                                <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                              Example: ``simple``
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

                              Example: ``Simple``

                     
                * - properties


                  - array
                  
                    .. raw:: html

                      <p>All properties of the Dataset</p>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - name


                            - string
                            
                              .. raw:: html

                                <p>The name of the Property.</p>

                              Example: ``the.age``
                          * - odataName


                            - string
                            
                              .. raw:: html

                                <p>The name of the property as it will appear in OData. OData property names can only contain alphanumeric characters and underscores.</p>

                              Example: ``the_age``
                          * - publishedAt


                            - string
                            
                              .. raw:: html

                                <p>Publishing timestamp of the form that defined this property for the first time.</p>

                              Example: ``2018-01-21T00:04:11.153Z``
                          * - forms


                            - array
                            
                              .. raw:: html

                                <p>List of forms that create the property</p>

                              Example: ``null``
                              
                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - xmlFormId


                                      - string
                                      
                                        .. raw:: html

                                          <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                                        Example: ``simple``
                                    * - name


                                      - string
                                      
                                        .. raw:: html

                                          <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition. Returns <code>xmlFormId</code> if there is no title in the form definition.</p>

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

              
      
Download Dataset
--------------------------

**GET /projects/{projectId}/datasets/{name}/entities.csv**

.. raw:: html

  <p>Datasets (collections of Entities) can be used as Attachments in other Forms, but they can also be downloaded directly as a CSV file.</p><p>The CSV format closely matches the <a href="/central-api-odata-endpoints/#odata-dataset-service">OData Dataset Service</a> format, with columns for system properties such as <code>__id</code> (the Entity UUID), <code>__createdAt</code>, <code>__creatorName</code>, etc., the Entity Label <code>label</code>, and the Dataset/Entity Properties themselves. If any Property for an given Entity is blank (e.g. it was not captured by that Form or was left blank), that field of the CSV is blank.</p><p>This endpoint supports <code>ETag</code> header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in the ETag header. If you pass that value in the If-None-Match header of a subsequent request, then if the Dataset has not been changed since the previous request, you will receive <code>304 Not Modified</code> response; otherwise you'll get the new data.</p>

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

  Content Type: text/csv

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          __id,label,geometry,species,circumference_cm,__createdAt,__creatorId,__creatorName,__updates,__updatedAt,__version
          2c1ee90b-dde8-434b-9985-2eefd8465339,666cm purpleheart,-29.281608 -67.624883 0 0,purpleheart,667,2023-05-31T19:49:28.902Z,22,Alice,1,2023-05-31T19:52:34.467Z,1
          84ac3a03-9980-4098-93a5-b81fdc6ea749,555cm wallaba,18.921876 77.309451 0 0,wallaba,555,2023-05-31T19:49:20.152Z,22,Alice,0,,1
          

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


              

    
              
      

