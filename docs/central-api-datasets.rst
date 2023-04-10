.. auto generated file - DO NOT MODIFY

Datasets
=======================================================================================================================

*(introduced: version 2022.3)*\ 

Version 2022.3 introduces server-managed Datasets as the first step on our `Entity-based data collection <https://forum.getodk.org/t/entity-based-data-collection/38115>`__ journey.

An Entity is a specific person, place, or thing. A Dataset is a collection of Entities. A Dataset is defined within a Form, and then a Submission to that Form creates an Entity when that Submission is **approved**\ . The Dataset definition includes the Dataset name and which Form fields map to which Dataset/Entity Properties, e.g. how to construct an Entity from a Submission.

See the `ODK XForms specification <https://getodk.github.io/xforms-spec>`__ for guidance on defining Datasets in Forms.

Once a Dataset exists, it can be linked to another Form as an Attachment and served as an automatically-updating CSV.

Related APIs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `Implicit creation of Datasets via Forms <#reference/forms/forms/creating-a-new-form>`__

- `Link a Dataset to a Form Attachment <#reference/forms/draft-form/linking-a-dataset-to-a-draft-form-attachment>`__

- `Get a Form's Related Datasets <#reference/forms/related-datasets>`__

Datasets
-----------------------------------------------------------------------------------------------------------------------

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

          [
            {
              "name": "people",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "projectId": 1.0
            }
          ]

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

                    Example: ``1.0``

              

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

                    Example: ``1.0``
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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Dataset Metadata
-----------------------------------------------------------------------------------------------------------------------

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

          {
            "name": "people",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "projectId": 1,
            "linkedForms": [
              {
                "xmlFormId": "simple",
                "name": "Simple"
              }
            ],
            "properties": [
              {
                "name": "first_name",
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - name


                  - string
                  
                    The name of the Dataset

                * - createdAt


                  - string
                  
                    ISO date format.

                * - projectId


                  - number
                  
                    The numerical ID of the Project that the Dataset belongs to.

                * - linkedForms


                  - array
                  
                    Forms that consume data from the Dataset

                    
    

                     
                * - properties


                  - array
                  
                    All properties of the Dataset

                    
    

                     
              
      

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Download Dataset
-----------------------------------------------------------------------------------------------------------------------

**GET /projects/{projectId}/datasets/{name}/entities.csv**

Datasets (collections of Entities) can be used as Attachments in other Forms, but they can also be downloaded directly as a CSV file. The CSV format matches what is expected for a `select question <https://docs.getodk.org/form-datasets/#building-selects-from-csv-files>`__ with columns for ``name``\ , ``label,``\  and properties. In the case of Datasets, the ``name``\  column is the Entity's UUID, the ``label``\  column is the human-readable Entity label populated in the Submission, and the properties are the full set of Dataset Properties for that Dataset. If any Property for an given Entity is blank (e.g. it was not captured by that Form or was left blank), that field of the CSV is blank.

Note that as of Version 2022.3 we do not guarantee the order of the Dataset Property columns.

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


              

    
              
      
  
