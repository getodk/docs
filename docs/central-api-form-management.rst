.. auto generated file - DO NOT MODIFY 

Form Management
=======================================================================================================================

``Form``\ s are the heart of ODK. They are created out of XML documents in the `ODK XForms <https://getodk.github.io/xforms-spec/>`__ specification format. The `Intro to Forms <https://docs.getodk.org/form-design-intro/>`__ on the ODK Documentation website is a good resource if you are unsure what this means. Once created, Forms can be retrieved in a variety of ways, their state can be managed, and they can be deleted.

These subsections cover only the modern RESTful API resources involving Forms. For documentation on the OpenRosa ``formList``\  endpoint (which can be used to list Forms), see that section below.


Forms
-----------------------------------------------------------------------------------------------------------------------

In this API, ``Form``\ s are distinguished by their ```formId``\  <https://getodk.github.io/xforms-spec/#primary-instance>`__s, which are a part of the XForms XML that defines each Form. In fact, as you will see below, many of the properties of a Form are extracted automatically from the XML: ``hash``\ , ``name``\ , ``version``\ , as well as the ``formId``\  itself (which to reduce confusion internally is known as ``xmlFormId``\  in ODK Central).

The only other property Forms currently have is ``state``\ , which can be used to control whether Forms show up in mobile clients like ODK Collect for download, as well as whether they accept new ``Submission``\ s or not.

It is not yet possible to modify a Form's XML definition once it is created.

List all Forms
^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms**

Currently, there are no paging or filtering options, so listing ``Form``\ s will get you every Form you are allowed to access, every time.

As of version 1.2, Forms that are unpublished (that only carry a draft and have never been published) will appear with full metadata detail. Previously, certain details like ``name``\  were omitted. You can determine that a Form is unpublished by checking the ``publishedAt``\  value: it will be ``null``\  for unpublished forms.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``submissions``\  count of the number of Submissions that each Form has, the ``reviewStates``\  object of counts of Submissions with specific review states, the ``lastSubmission``\  most recent submission timestamp, as well as the Actor the Form was ``createdBy``\ .

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
              "projectId": 1,
              "xmlFormId": "simple",
              "name": "Simple",
              "version": "2.1",
              "enketoId": "abcdef",
              "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
              "keyId": 3,
              "state": "open",
              "publishedAt": "2018-01-21T00:04:11.153Z",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "updatedAt": "2018-03-21T12:45:02.312Z",
              "submissions": 10,
              "reviewStates": {
                "received": 3,
                "hasIssues": 2,
                "edited": 1
              },
              "lastSubmission": "2018-04-18T03:04:51.695Z",
              "createdBy": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "entityRelated": false
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - submissions


                  - number
                  
                    The number of ``Submission``\ s that have been submitted to this ``Form``\ .

                    Example: ``10``
                * - reviewStates


                  - object
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - received


                            - number
                            
                              The number of submissions receieved with no other review state.

                              Example: ``3``
                          * - hasIssues


                            - number
                            
                              The number of submissions marked as having issues.

                              Example: ``2``
                          * - edited


                            - number
                            
                              The number of edited submissions.

                              Example: ``1``
                     
                * - lastSubmission


                  - string
                  
                    ISO date format. The timestamp of the most recent submission, if any.

                    Example: ``2018-04-18T03:04:51.695Z``
                * - createdBy


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
                     
                * - excelContentType


                  - string
                  
                    If the Form was created by uploading an Excel file, this field contains the MIME type of that file.

                * - entityRelated


                  - boolean
                  
                    True only if this Form is related to a Dataset. In v2022.3, this means the Form's Submissions create Entities in a Dataset. In a future version, Submissions will also be able to update existing Entities.

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
                  
                    

                    Example: ``403.1``
                * - message


                  - string
                  
                    

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Creating a new Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms**

When creating a ``Form``\ , the only required data is the actual XForms XML or XLSForm itself. Use it as the ``POST``\  body with a ``Content-Type``\  header of ``application/xml``\  (``text/xml``\  works too), and the Form will be created.

As of Version 0.8, Forms will by default be created in Draft state, accessible under ``/projects/…/forms/…/draft``\ . The Form itself will not have a public XML definition, and will not appear for download onto mobile devices. You will need to `publish the form </central-api-form-management/#publishing-a-draft-form>`__ to finalize it for data collection. To disable this behaviour, and force the new Form to be immediately ready, you can pass the querystring option ``?publish=true``\ .

For XLSForm upload, either ``.xls``\  or ``.xlsx``\  are accepted. You must provide the ``Content-Type``\  request header corresponding to the file type: ``application/vnd.openxmlformats-officedocument.spreadsheetml.sheet``\  for ``.xlsx``\  files, and ``application/vnd.ms-excel``\  for ``.xls``\  files. You must also provide an ``X-XlsForm-FormId-Fallback``\  request header with the ``formId``\  you want the resulting form to have, if the spreadsheet does not already specify. This header field accepts percent-encoded values to support Unicode characters and other non-ASCII values.

By default, any XLSForm conversion Warnings will fail this request and return the warnings rather than use the converted XML to create a form. To override this behaviour, provide a querystring flag ``?ignoreWarnings=true``\ . Conversion Errors will always fail this request.

The API will currently check the XML's structure in order to extract the information we need about it, but ODK Central does *not*\  run comprehensive validation on the full contents of the XML to ensure compliance with the ODK specification. Future versions will likely do this, but in the meantime you will have to use a tool like `ODK Validate <https://getodk.org/use/validate/>`__ to be sure your Forms are correct.

You will get following workflow warnings while creating a new form or uploading a new version of an existing form:

- Structural Change: Returned when the uploaded definition of the form removes, renames or moves a field to a different group/repeat. `Learn more <https://docs.getodk.org/central-forms/#central-forms-updates>`__

- Deleted Form: Returned when there is a form with the same ID in the Trash. `Learn more <https://docs.getodk.org/central-forms/#deleting-a-form>`__

**Creating Datasets with Forms**\ 

Starting from Version 2022.3, a Form can also create a Dataset by defining a Dataset schema in the Form definition (XForms XML or XLSForm). When a Form with a Dataset schema is uploaded, a Dataset and its Properties are created. The state of the Dataset is dependent on the state of the Form; you will need to publish the Form to publish the Dataset. Datasets in the Draft state are not returned in `Dataset APIs </central-api-dataset-management>`__, however the `Related Datasets </central-api-form-management/#draft-form-dataset-diff>`__ API for the Form can be called to get the Dataset and its Properties.

It is possible to define the schema of a Dataset in multiple Forms. Such Forms can be created and published in any order. Publishing any of the Forms will also publish the Dataset and will generate a ``dataset.create``\  event; ``dataset.update``\  events are generated in Audit logs when a Form adds a new property in the Dataset. The state of a Property of a Dataset is also dependent on the state of the Form that FIRST defines that Property, which means if a Form is in the Draft state then the Properties defined by that Form will not appear in the `.csv file </central-api-dataset-management/#download-dataset>`__ of the Dataset.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - ignoreWarnings

          *(query)*

        - boolean
        
          Defaults to `false`. Set to `true` if you want the Form to be created even if the XLSForm conversion results in warnings.

          Example: ``false``
      * - publish

          *(query)*

        - boolean
        
          Defaults to `false`. Set to `true` if you want the Form to skip the Draft state to Published.

          Example: ``false``
      * - X-XlsForm-FormId-Fallback

          *(header)*

        - string
        
          e.g. filename.xlsx

          Example: ``filename.xlsx``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "projectId": 1,
            "xmlFormId": "simple",
            "name": "Simple",
            "version": "2.1",
            "enketoId": "abcdef",
            "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
            "keyId": 3,
            "state": "open",
            "publishedAt": "2018-01-21T00:04:11.153Z",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                * - state


                  - enum
                  
                    The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                * - createdAt


                  - string
                  
                    ISO date format

                * - updatedAt


                  - string
                  
                    ISO date format

              
      

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
                  
                    

              
      

Individual Form
-----------------------------------------------------------------------------------------------------------------------



Getting Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}**

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``submissions``\  count of the number of ``Submission``\ s that this Form has, as well as the ``lastSubmission``\  most recent submission timestamp.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - projectId


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
            "projectId": 1,
            "xmlFormId": "simple",
            "name": "Simple",
            "version": "2.1",
            "enketoId": "abcdef",
            "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
            "keyId": 3,
            "state": "open",
            "publishedAt": "2018-01-21T00:04:11.153Z",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "submissions": 10,
            "reviewStates": {
              "received": 3,
              "hasIssues": 2,
              "edited": 1
            },
            "lastSubmission": "2018-04-18T03:04:51.695Z",
            "createdBy": {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            },
            "entityRelated": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                * - state


                  - enum
                  
                    The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                * - createdAt


                  - string
                  
                    ISO date format

                * - updatedAt


                  - string
                  
                    ISO date format

                * - submissions


                  - number
                  
                    The number of ``Submission``\ s that have been submitted to this ``Form``\ .

                * - reviewStates


                  - object
                  
                    Additional counts of the number of submissions in various states of review.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - received


                            - number
                            
                              The number of submissions receieved with no other review state.

                          * - hasIssues


                            - number
                            
                              The number of submissions marked as having issues.

                          * - edited


                            - number
                            
                              The number of edited submissions.

                     
                * - lastSubmission


                  - string
                  
                    ISO date format. The timestamp of the most recent submission, if any.

                * - createdBy


                  - object
                  
                    The full information of the Actor who created this Form.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              ISO date format

                          * - displayName


                            - string
                            
                              All ``Actor``\ s, regardless of type, have a display name

                          * - id


                            - number
                            
                              

                          * - type


                            - enum
                            
                              the Type of this Actor; typically this will be ``user``\ .


                                
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

                          * - deletedAt


                            - string
                            
                              ISO date format

                     
                * - excelContentType


                  - string
                  
                    If the Form was created by uploading an Excel file, this field contains the MIME type of that file.

                * - entityRelated


                  - boolean
                  
                    True only if this Form is related to a Dataset. In v2022.3, this means the Form's Submissions create Entities in a Dataset. In a future version, Submissions will also be able to update existing Entities.

                    Example: ``none``
              
      

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
                  
                    

              
      
Deleting a Form
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}**

When a Form is deleted, it goes into the Trash section, but it can now be restored from the Trash. After 30 days in the Trash, the Form and all of its resources and submissions will be automatically purged. If your goal is to prevent it from showing up on survey clients like ODK Collect, consider setting its ``state``\  to ``closing``\  or ``closed``\  instead (see `Modifying a Form </central-api-form-management/#modifying-a-form>`__ just above for more details).

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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
                  
                    

              
      
Modifying a Form
^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}**

It is currently possible to modify only one thing about a ``Form``\ : its ``state``\ , which governs whether it is available for download onto survey clients and whether it accepts new ``Submission``\ s. See the ``state``\  Attribute in the Request documentation to the right to see the possible values and their meanings.

We use ``PATCH``\  rather than ``PUT``\  to represent the update operation, so that you only have to supply the properties you wish to change. Anything you do not supply will remain untouched.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "state": "open"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - state


                  - enum
                  
                    If supplied, the Form lifecycle state will move to this value.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "projectId": 1,
            "xmlFormId": "simple",
            "name": "Simple",
            "version": "2.1",
            "enketoId": "abcdef",
            "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
            "keyId": 3,
            "state": "open",
            "publishedAt": "2018-01-21T00:04:11.153Z",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                * - state


                  - enum
                  
                    The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                * - createdAt


                  - string
                  
                    ISO date format

                * - updatedAt


                  - string
                  
                    ISO date format

              
      

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
                  
                    

              
      
Retrieving Form XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.xml**

To get the XML of the ``Form``\ , add ``.xml``\  to the end of the request URL.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <h:html xmlns="http://www.w3.org/2002/xforms" xmlns:h="http://www.w3.org/1999/xhtml" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:jr="http://openrosa.org/javarosa">
            <h:head>
              <h:title>Simple</h:title>
              <model>
                <instance>
                  <data id="simple" version="2.1">
                    <meta>
                      <instanceID/>
                    </meta>
                    <name/>
                    <age/>
                  </data>
                </instance>
          
                <bind nodeset="/data/meta/instanceID" type="string" readonly="true()" calculate="concat('uuid:', uuid())"/>
                <bind nodeset="/data/name" type="string"/>
                <bind nodeset="/data/age" type="int"/>
              </model>
          
            </h:head>
            </h:body>
              <input ref="/data/name">
                <label>What is your name?</label>
              </input>
              <input ref="/data/age">
                <label>What is your age?</label>
              </input>
            </h:body>
          </h:html>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Retrieving Form XLS(X)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.xlsx**

If a Form was created with an Excel file (``.xls``\  or ``.xlsx``\ ), you can get that file back by adding ``.xls``\  or ``.xlsx``\  as appropriate to the Form resource path.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)\n"

    .. tab-item:: Schema

      **If a Form was created with an Excel file (``.xls``\  or ``.xlsx``\ ), you can get that file back by adding ``.xls``\  or ``.xlsx``\  as appropriate to the Form resource path.**

      .. list-table::
        :class: schema-table-wrap

        * - 


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

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
                  
                    

              
      
Listing Form Attachments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/attachments**

This endpoint allows you to fetch the list of expected attachment files, and will tell you whether the server is in possession of each file or not. To modify an attachment, you'll need to create a Draft.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "myfile.mp3",
              "type": "image",
              "exists": true,
              "blobExists": true,
              "datasetExists": true,
              "updatedAt": "2018-03-21T12:45:02.312Z"
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
                  
                    The name of the file as specified in the XForm.

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - image


                            - string
                            
                              

                          * - audio


                            - string
                            
                              

                          * - video


                            - string
                            
                              

                          * - file


                            - string
                            
                              

                     
                * - exists


                  - boolean
                  
                    True if the server has the file or the Attachment is linked to a Dataset, otherwise false.

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    Whether the server has the file or not.

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    Whether attachment is linked to a Dataset.

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).

                    Example: ``2018-03-21T12:45:02.312Z``

              
      

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
              
      
Downloading a Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/attachments/{filename}**

To download a single file, use this endpoint. The appropriate ``Content-Disposition``\  (attachment with a filename) and ``Content-Type``\  (based on the type supplied at upload time) will be given.

This endpoint supports ``ETag``\ , which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, it returns a value in ``ETag``\  header, you can pass this value in the header ``If-None-Match``\  of subsequent requests. If the file has not been changed since the previous request, you will receive ``304 Not Modified``\  response otherwise you'll get the latest file.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          The name of the file to download.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)"

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

    
              
      

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
                  
                    

              
      
Getting Form Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/fields**

*(introduced: version 0.8)*\ 

For applications that do not rely on JavaRosa, it can be challenging to parse XForms XML into a simple schema structure. Because Central Backend already implements and performs such an operation for its own internal purposes, we also expose this utility for any downstream consumers which wish to make use of it.

While this may eventually overlap with the new OData JSON CSDL specification, we are likely to maintain this API as it more closely mirrors the original XForms data types and structure.

Central internally processes the XForms schema tree into a flat list of fields, and this is how the data is returned over this endpoint as well. It will always return fields in a *depth-first traversal order*\  of the original ``<instance>``\  XML block in the XForm.

You may optionally add the querystring parameter ``?odata=true``\  to sanitize the field names and paths to match the way they will be outputted for OData. While the original field names as given in the XForms definition may be used as-is for CSV output, OData has some restrictions related to the domain-qualified identifier syntax it uses.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - odata

          *(query)*

        - boolean
        
          If set to `true`, will sanitize field names.

          Example: ``false``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "meta",
              "path": "/meta",
              "type": "structure"
            },
            {
              "name": "instanceID",
              "path": "/meta/instanceID",
              "type": "string"
            },
            {
              "name": "name",
              "path": "/name",
              "type": "string"
            },
            {
              "name": "age",
              "path": "/age",
              "type": "int"
            },
            {
              "name": "photo",
              "path": "/photo",
              "type": "binary",
              "binary": true
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
                  
                    

                * - path


                  - string
                  
                    

                * - type


                  - string
                  
                    

                * - binary


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
                  
                    

              
      
Restoring a Form
^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{id}/restore**

*(introduced: version 1.4)*\ 

Deleted forms can now be restored (as long as they have been in the Trash less than 30 days and have not been purged). However, a deleted Form with the same ``xmlFormId``\  as an active Form cannot be restored while that other Form is active. This ``/restore``\  URL uses the numeric ID of the Form (now returned by the ``/forms``\  endpoint) rather than the ``xmlFormId``\  to unambigously restore.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - id


        - string
        
          The ID (not xmlFormId) of the Form

          Example: ``simple``

  
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
                  
                    

              
      

Draft Form
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.8)*\ 

Draft Forms allow you to test and fix issues with Forms before they are finalized and presented to data collectors. They make this process easier, as Draft Forms can be created and discarded without consequence: your Drafts will not count against the overall Form schema, nor against the set of unique ``version``\  strings for the Form.

You can create or replace the current Draft Form at any time by ``POST``\ ing to the ``/draft``\  subresource on the Form, and you can publish the current Draft by ``POST``\ ing to ``/draft/publish``\ .

When a Draft Form is created, a Draft Token is also created for it, which can be found in Draft Form responses at ``draftToken``\ . This token allows you to `submit test Submissions to the Draft Form </central-api-submission-management/#creating-a-submission>`__ through clients like Collect. If the Draft is published or deleted, the token will be deactivated. But if you replace the Draft without first deleting it, the existing Draft Token will be carried forward, so that you do not have to reconfigure your device.

Getting Draft Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft**

The response here will include standard overall Form metadata, like ``xmlFormId``\ , in addition to the Draft-specific information.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "projectId": 1.0,
            "xmlFormId": "simple",
            "name": "Simple",
            "version": "2.1",
            "enketoId": "abcdef",
            "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
            "keyId": 3.0,
            "state": "",
            "publishedAt": "2018-01-21T00:04:11.153Z",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "draftToken": "lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - draftToken


                  - string
                  
                    The test token to use to submit to this draft form. See `Draft Testing Endpoints </central-api-submission-management/#draft-submissions>`__.

                    Example: ``lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this draft Form on Enketo at ``/-``\ . Authentication is not needed to access the draft form through Enketo.

                    Example: ``abcdef``
              
      

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
                  
                    

              
      
Creating a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft**

``POST``\ ing here will create a new Draft Form on the given Form. For the most part, it takes the same parameters as the `Create Form request </central-api-form-management/#creating-a-new-form>`__: you can submit XML or Excel files, you can provide ``ignoreWarnings``\  if you'd like.

Additionally, however, you may ``POST``\  with no ``Content-Type``\  and an empty body to create a Draft Form with a copy of the definition (XML, XLS, etc) that is already published, if there is one. This can be useful if you don't wish to update the Form definition itself, but rather one or more Form Attachments.

If your Draft form schema contains any field path which overlaps with a field path of a previous version of the Form, but with a different data type, your request will be rejected. You can rename the conflicting field, or correct it to have the same data type as it did previously.

When a Draft is created, the expected Form Attachments are computed and slots are created, as with a new Form. Any attachments that match existing ones on the published Form, if it exists, will be copied over to the new Draft.

Even if a Draft exists, you can always replace it by ``POST``\ ing here again. In that case, the attachments that exist on the Draft will similarly be copied over to the new Draft. If you wish to copy from the published version instead, you can do so by first ``DELETE``\ ing the extant Draft.

Draft ``version``\  conflicts are allowed with prior versions of a Form while in Draft state. If you attempt to `publish the Form </central-api-form-management/#draft-form/publishing-a-draft-form>`__ without correcting the conflict, the publish operation will fail. You can request that Central update the version string on your behalf as part of the publish operation to avoid this: see that endpoint for more information.

The ``xmlFormId``\ , however, must exactly match that of the Form overall, or the request will be rejected.

Starting from Version 2022.3, a Draft Form can also create or update a Dataset by defining a Dataset schema in the Form definition. The state of the Dataset and its Properties is dependent on the state of the Form, see `Creating a new form </central-api-form-management/#creating-a-new-form>`__ for more details.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - ignoreWarnings

          *(query)*

        - boolean
        
          Defaults to `false`. Set to `true` if you want the form to be created even if the XLSForm conversion results in warnings.

          Example: ``false``
      * - X-XlsForm-FormId-Fallback

          *(header)*

        - string
        
          e.g. filename.xlsx

          Example: ``filename.xlsx``

  
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
                  
                    

              
      
Deleting a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft**

Once a Draft Form is deleted, its definition and any Form Attachments associated with it will be removed.

You will not be able to delete the draft if there is no published version of the form.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
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
                  
                    

              
      
Retrieving Draft Form XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.xml**

To get the XML of the Draft Form, add ``.xml``\  to the end of the request URL.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <h:html xmlns="http://www.w3.org/2002/xforms" xmlns:h="http://www.w3.org/1999/xhtml" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:jr="http://openrosa.org/javarosa">
            <h:head>
              <h:title>Simple</h:title>
              <model>
                <instance>
                  <data id="simple" version="2.1">
                    <meta>
                      <instanceID/>
                    </meta>
                    <name/>
                    <age/>
                  </data>
                </instance>
          
                <bind nodeset="/data/meta/instanceID" type="string" readonly="true()" calculate="concat('uuid:', uuid())"/>
                <bind nodeset="/data/name" type="string"/>
                <bind nodeset="/data/age" type="int"/>
              </model>
          
            </h:head>
            <h:body>
              <input ref="/data/name">
                <label>What is your name?</label>
              </input>
              <input ref="/data/age">
                <label>What is your age?</label>
              </input>
            </h:body>
          </h:html>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Retrieving Draft Form XLS(X)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.xlsx**

If a Draft Form was created with an Excel file (``.xls``\  or ``.xlsx``\ ), you can get that file back by adding ``.xls``\  or ``.xlsx``\  as appropriate to the Draft Form resource path.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          (binary data)
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Listing expected Draft Form Attachments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments**

Form Attachments for each form are automatically determined when the form is first created, by scanning the XForms definition for references to media or data files. Because of this, it is not possible to directly modify the list of form attachments; that list is fully determined by the given XForm. Instead, the focus of this API subresource is around communicating that expected list of files, and uploading binaries into those file slots.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "myfile.mp3",
              "type": "image",
              "exists": true,
              "blobExists": true,
              "datasetExists": true,
              "updatedAt": "2018-03-21T12:45:02.312Z"
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
                  
                    The name of the file as specified in the XForm.

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - image


                            - string
                            
                              

                          * - audio


                            - string
                            
                              

                          * - video


                            - string
                            
                              

                          * - file


                            - string
                            
                              

                     
                * - exists


                  - boolean
                  
                    True if the server has the file or the Attachment is linked to a Dataset, otherwise false.

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    Whether the server has the file or not.

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    Whether attachment is linked to a Dataset.

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).

                    Example: ``2018-03-21T12:45:02.312Z``

              
      

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
              
      
Downloading a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

To download a single file, use this endpoint. The appropriate ``Content-Disposition``\  (attachment with a filename or Dataset name) and ``Content-Type``\  (based on the type supplied at upload time or ``text/csv``\  in the case of a linked Dataset) will be given.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          The name of tha attachment.

          Example: ``people.csv``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself or text/csv for a Dataset}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)\n"

    .. tab-item:: Schema

      **To download a single file, use this endpoint. The appropriate ``Content-Disposition``\  (attachment with a filename or Dataset name) and ``Content-Type``\  (based on the type supplied at upload time or ``text/csv``\  in the case of a linked Dataset) will be given.**

      .. list-table::
        :class: schema-table-wrap

        * - 


              

    
              
      

  **HTTP Status: 403**

  Content Type: {the MIME type of the attachment file itself or text/csv for a Dataset}

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
                  
                    

              
      
Uploading a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

To upload a binary to an expected file slot, ``POST``\  the binary to its endpoint. Supply a ``Content-Type``\  MIME-type header if you have one.

As of version 2022.3, if there is already a Dataset linked to this attachment, it will be unlinked and replaced with the uploaded file.

This endpoint supports ``ETag``\  header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in ``ETag``\  header. If you pass that value in the ``If-None-Match``\  header of a subsequent request, then if the file has not been changed since the previous request, you will receive ``304 Not Modified``\  response; otherwise you'll get the latest file.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          The name of that attachment.

          Example: ``people.csv``

  
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
                  
                    

              
      
Clearing a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

Because Form Attachments are completely determined by the XForms definition of the form itself, there is no direct way to entirely remove a Form Attachment entry from the list, only to clear its uploaded content or to unlink the Dataset. Thus, when you issue a ``DELETE``\  to the attachment's endpoint, that is what happens.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          The name of tha attachment.

          Example: ``people.csv``

  
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
                  
                    

              
      
Linking a Dataset to a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

*(introduced: version 2022.3)*\ 

This endpoint can update a Form Attachment's link to a Dataset. You can use this to link or unlink a Dataset to a Form Attachment. Linking of a Dataset to the Attachment only happens if the Attachment type is ``file``\  and there is a Dataset with the exact name of the Attachment (excluding extension ``.csv``\ ) in the Project. For example, if the Form definition includes an Attachment named ``people.csv``\ , then it can be linked to a Dataset named ``people``\ . Pay special attention to letter case and spaces.

When linking a Dataset, if there is any existing file attached then it will be removed.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          The name of the attachment.

          Example: ``people.csv``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "dataset": "true"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - dataset


                  - boolean
                  
                    true for linking Dataset and false for unlinking Dataset.

                    Example: ``true``
              
  
  
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
                  
                    

              
      

  **HTTP Status: 404**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "404.1",
            "message": "Could not find the resource you were looking for."
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
                  
                    

              
      
Getting Draft Form Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/fields**

Identical to the `same request </central-api-form-management/#getting-form-schema-fields>`__ for the published Form, but will return the fields related to the current Draft version.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - odata

          *(query)*

        - boolean
        
          If set to `true`, will sanitize field names.

          Example: ``false``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "meta",
              "path": "/meta",
              "type": "structure"
            },
            {
              "name": "instanceID",
              "path": "/meta/instanceID",
              "type": "string"
            },
            {
              "name": "name",
              "path": "/name",
              "type": "string"
            },
            {
              "name": "age",
              "path": "/age",
              "type": "int"
            },
            {
              "name": "photo",
              "path": "/photo",
              "type": "binary",
              "binary": true
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
                  
                    

                * - path


                  - string
                  
                    

                * - type


                  - string
                  
                    

                * - binary


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
                  
                    

              
      
Publishing a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/publish**

This will publish your current Draft Form and make it the active Form definition (and attachments).

If your Draft ``version``\  conflicts with an older version of the Form, you will get an error.

If you wish for the ``version``\  to be set on your behalf as part of the publish operation, you can provide the new version string as a querystring parameter ``?version``\ .

Once the Draft is published, there will no longer be a Draft version of the form.

Starting with Version 2022.3, publishing a Draft Form that defines a Dataset schema will also publish the Dataset. It will generate ``dataset.create``\  event in Audit logs and make the Dataset available in `Datasets APIs </central-api-dataset-management>`__. If the Dataset is already published and the Form adds new properties then ``dataset.update``\  event will be generated.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version

          *(query)*

        - string
        
          The `version` to be associated with the Draft once it's published.

          Example: ``newVersion``

  
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
                  
                    

              
      

Published Form Versions
-----------------------------------------------------------------------------------------------------------------------

All published versions of a Form are available read-only at the ``/versions``\  subresource for reference, including the currently published version. You may read that version and its details, retrieve the Form definition, and any attachments associated with each version.

Listing Published Form Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions**

Each entry of the version listing will contain some of the same duplicate keys with basic information about the Form: ``xmlFormId``\  and ``createdAt``\ , for example. This is done to match the data you'd receive if you'd requested each version separately.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``Actor``\  that each version was ``publishedBy``\ .

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "projectId": 1,
              "xmlFormId": "simple",
              "name": "Simple",
              "version": "2.1",
              "enketoId": "abcdef",
              "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
              "keyId": 3,
              "state": "open",
              "publishedAt": "2018-01-21T00:04:11.153Z",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "updatedAt": "2018-03-21T12:45:02.312Z",
              "publishedBy": {
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


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - publishedBy


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
                     
                * - excelContentType


                  - string
                  
                    If the Form was created by uploading an Excel file, this field contains the MIME type of that file.


              
      

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
              
      
Getting Form Version Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}**

Since the XForms specification allows blank strings as ``version``\ s (and Central treats the lack of a ``version``\  as a blank string), you may run into trouble using this resource if you have such a Form. In this case, pass the special value ``**\ _``\  (three underscores) as the ``version``\  to retrieve the blank ``version``\  version.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "projectId": 1.0,
            "xmlFormId": "simple",
            "name": "Simple",
            "version": "2.1",
            "enketoId": "abcdef",
            "hash": "51a93eab3a1974dbffc4c7913fa5a16a",
            "keyId": 3.0,
            "state": "",
            "publishedAt": "2018-01-21T00:04:11.153Z",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    The ``id``\  of the project this form belongs to.

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    The ``id``\  of this form as given in its XForms XML definition

                    Example: ``simple``
                * - name


                  - string
                  
                    The friendly name of this form. It is given by the ``<title>``\  in the XForms XML definition.

                    Example: ``Simple``
                * - version


                  - string
                  
                    The ``version``\  of this form as given in its XForms XML definition. If no ``version``\  was specified in the Form, a blank string will be given.

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    If it exists, this is the survey ID of this Form on Enketo at ``/-``\ . This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.

                    Example: ``3.0``
                * - state


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - open


                            - string
                            
                              

                          * - closing


                            - string
                            
                              

                          * - closed


                            - string
                            
                              

                     
                * - publishedAt


                  - string
                  
                    Indicates when a draft has most recently been published for this Form. If this value is ``null``\ , this Form has never been published yet, and contains only a draft.

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-03-21 12:45:02.312000+00:00``
              
      

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
                  
                    

              
      
Retrieving Form Version XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}.xml**

To get the XML of the Form Version, add ``.xml``\  to the end of the request URL.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <h:html xmlns="http://www.w3.org/2002/xforms" xmlns:h="http://www.w3.org/1999/xhtml" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:jr="http://openrosa.org/javarosa">
            <h:head>
              <h:title>Simple</h:title>
              <model>
                <instance>
                  <data id="simple" version="2.1">
                    <meta>
                      <instanceID/>
                    </meta>
                    <name/>
                    <age/>
                  </data>
                </instance>
          
                <bind nodeset="/data/meta/instanceID" type="string" readonly="true()" calculate="concat('uuid:', uuid())"/>
                <bind nodeset="/data/name" type="string"/>
                <bind nodeset="/data/age" type="int"/>
              </model>
          
            </h:head>
          
              <input ref="/data/name">
                <label>What is your name?</label>
              </input>
              <input ref="/data/age">
                <label>What is your age?</label>
              </input>
            </h:body>
          </h:html>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Retrieving Form Version XLS(X)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}.xlsx**

If a Form Version was created with an Excel file (``.xls``\  or ``.xlsx``\ ), you can get that file back by adding ``.xls``\  or ``.xlsx``\  as appropriate to the Form Version resource path.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          (binary data)
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Listing Form Version Attachments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}/attachments**

Attachments are specific to each version of a Form. You can retrieve the attachments associated with a given version here.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "myfile.mp3",
              "type": "image",
              "exists": true,
              "blobExists": true,
              "datasetExists": true,
              "updatedAt": "2018-03-21T12:45:02.312Z"
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
                  
                    The name of the file as specified in the XForm.

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - image


                            - string
                            
                              

                          * - audio


                            - string
                            
                              

                          * - video


                            - string
                            
                              

                          * - file


                            - string
                            
                              

                     
                * - exists


                  - boolean
                  
                    True if the server has the file or the Attachment is linked to a Dataset, otherwise false.

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    Whether the server has the file or not.

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    Whether attachment is linked to a Dataset.

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).

                    Example: ``2018-03-21T12:45:02.312Z``

              
      

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
                  
                    

              
      
Downloading a Form Version Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}/attachments/{filename}**

To download a single file, use this endpoint. The appropriate ``Content-Disposition``\  (attachment with a filename) and ``Content-Type``\  (based on the type supplied at upload time) will be given.

This endpoint supports ``ETag``\  header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in ``ETag``\  header. If you pass that value in the ``If-None-Match``\  header of a subsequent request, then if the file has not been changed since the previous request, you will receive ``304 Not Modified``\  response; otherwise you'll get the latest file.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``
      * - filename


        - string
        
          The name of tha attachment.

          Example: ``people.csv``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)"

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

    
              
      

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
                  
                    

              
      
Getting Form Version Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}/fields**

Identical to the `same request </central-api-form-management/#getting-form-schema-fields>`__ for the published Form, but will return the fields related to the specified version.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``
      * - odata

          *(query)*

        - boolean
        
          If set to `true`, will sanitize field names.

          Example: ``false``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "meta",
              "path": "/meta",
              "type": "structure"
            },
            {
              "name": "instanceID",
              "path": "/meta/instanceID",
              "type": "string"
            },
            {
              "name": "name",
              "path": "/name",
              "type": "string"
            },
            {
              "name": "age",
              "path": "/age",
              "type": "int"
            },
            {
              "name": "photo",
              "path": "/photo",
              "type": "binary",
              "binary": true
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
                  
                    

                * - path


                  - string
                  
                    

                * - type


                  - string
                  
                    

                * - binary


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
                  
                    

              
      

Form Assignments
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.7)*\ 

There are multiple Assignments resources. This one, specific to the Form it is nested within, only governs Role assignments to that Form. Assigning an Actor a Role that grants, for example, a verb ``submission.create``\ , allows that Actor to create a submission to this Form alone. It is also possible to assign umbrella rights to a whole Project and therefore all Forms within it: see the `Project Assignments resource </central-api-project-management/#project-assignments>`__ for information about this.

The `sitewide Assignments resource </central-api-accounts-and-users/#assignments>`__, at the API root, manages Role assignments for all objects across the server. Apart from this difference in scope, the introduction to that section contains information useful for understanding the following endpoints.

There are only one set of Roles, applicable to either scenario. There are not a separate set of Roles used only upon Projects or Forms.

Listing all Form Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/assignments**

This will list every assignment upon this Form, in the form of ``actorId``\ /``roleId``\  pairs.

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
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

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
              
      
Listing all Actors assigned some Form Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, this endpoint lists all ``Actors``\  that have been assigned that Role upon this particular Form.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``manager``

  
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
              
      
Assigning an Actor to a Form Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , assigns that Role to that Actor for this particular Form.

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
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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
              
      
Revoking a Form Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , unassigns that Role from that Actor for this particular Form.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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
                  
                    

              
      

Public Access Links
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 1.0)*\ 

Anybody in possession of a Public Access Link for a Form can use that link to submit data to that Form. Public Links are useful for collecting direct responses from a broad set of respondents, and can be revoked using the administration website or the API at any time.

The API for Public Links is particularly useful, as it can be used to, for example, programmatically create and send individually customized and controlled links for direct distribution. The user-facing link for a Public Link has the following structure: ``/-/{enketoId}?st={token}``\  where ``-``\  is the Enketo root, ``enketoId``\  is the survey ID of this published Form on Enketo and ``token``\  is a session token to identify this Public Link.

To revoke the access of any Link, terminate its session ``token``\  by issuing ```DELETE /sessions/:token``\  </central-api-authentication/#logging-out>`__.

Listing all Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/public-links**

This will list every Public Access Link upon this Form.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to retrieve the Actor the Link was ``createdBy``\ .

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``2``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
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
              "deletedAt": "2018-04-18T23:42:11.406Z",
              "token": "d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT",
              "once": false,
              "createdBy": {
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
                * - token


                  - string
                  
                    If present, this is the Token to include as the ``st``\  query parameter for this ``Public Link``\ . If not present, this ``Public Link``\  has been revoked.

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - once


                  - boolean
                  
                    If set to ``true``\ , an Enketo `single submission survey <https://blog.enketo.org/single-submission-surveys/>`__ will be created instead of a standard one, limiting respondents to a single submission each.

                    Example: ``none``

              

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
                * - token


                  - string
                  
                    If present, this is the Token to include as the ``st``\  query parameter for this ``Public Link``\ . If not present, this ``Public Link``\  has been revoked.

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - once


                  - boolean
                  
                    If set to ``true``\ , an Enketo `single submission survey <https://blog.enketo.org/single-submission-surveys/>`__ will be created instead of a standard one, limiting respondents to a single submission each.

                    Example: ``none``
                * - createdBy


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
                     

              
      
Creating a Link
^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/public-links**

To create a new Public Access Link to this Form, you must send at least a ``displayName``\  for the resulting Actor. You may also provide ``once: true``\  if you want to create a link that `can only be filled by each respondent once <https://blog.enketo.org/single-submission-surveys/>`__. This setting is enforced by Enketo using local device tracking; the link is still distributable to multiple recipients, and the enforcement can be defeated by using multiple browsers or devices.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``2``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "displayName": "my public link",
            "once": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - displayName


                  - string
                  
                    The name of the Link, for keeping track of. This name is displayed on the Central administration website but not to survey respondents.

                * - once


                  - boolean
                  
                    If set to ``true``\ , an Enketo `single submission survey <https://blog.enketo.org/single-submission-surveys/>`__ will be created instead of a standard one, limiting respondents to a single submission each.

                    Example: ``none``
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "createdAt": "2018-04-18T23:19:14.802Z",
            "displayName": "My Display Name",
            "id": 115,
            "type": "user",
            "updatedAt": "2018-04-18T23:42:11.406Z",
            "deletedAt": "2018-04-18T23:42:11.406Z",
            "token": "d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT",
            "once": false
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - createdAt


                  - string
                  
                    ISO date format

                * - displayName


                  - string
                  
                    All ``Actor``\ s, regardless of type, have a display name

                * - id


                  - number
                  
                    

                * - type


                  - enum
                  
                    the Type of this Actor; typically this will be ``user``\ .


                      
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

                * - deletedAt


                  - string
                  
                    ISO date format

                * - token


                  - string
                  
                    If present, this is the Token to include as the ``st``\  query parameter for this ``Public Link``\ . If not present, this ``Public Link``\  has been revoked.

                * - once


                  - boolean
                  
                    If set to ``true``\ , an Enketo `single submission survey <https://blog.enketo.org/single-submission-surveys/>`__ will be created instead of a standard one, limiting respondents to a single submission each.

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
                  
                    

              
      
Deleting a Link
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/public-links/{linkId}**

You can fully delete a link by issuing ``DELETE``\  to its resource. This will remove the Link from the system entirely. If instead you wish to revoke the Link's access to prevent future submission without removing its record entirely, you can issue ```DELETE /sessions/:token``\  </central-api-authentication/#session-authentication/logging-out>`__.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - linkId


        - integer
        
          The numeric ID of the Link

          Example: ``42``

  
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
                  
                    

              
      

Related Datasets
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 2022.3)*\ 

Datasets are created and updated through Forms. Dataset-related Forms follow `the entities sub-spec <https://getodk.github.io/xforms-spec/entities>`__ of the ODK XForms specification that allow them to define a Dataset and a mapping of Form Fields to Dataset Properties. Submissions from such a Form can create Entities within the Dataset defined in the Form.

Currently, Datasets and Dataset Properties are purely additive. Multiple Forms can add Properties to the same Dataset and multiple Forms can create Entities in the same Dataset. Not all Properties of a Dataset have to be included in a Form for that Dataset. For example, one Form publishing to a Dataset called ``trees``\  could add ``location``\  and ``species``\ , while another could add ``species``\  and ``circumference``\ . The Properties of the Dataset would be the union of Properties from all Forms for that Dataset (``location``\ , ``species``\ , ``circumference``\ ). Note that it is not necessary that a Form will save to all Properties of a Dataset, so the endpoint also returns a ``inForm``\  flag for each property which is true only if the Form affects that Property.

The following endpoints return the Dataset(s) that Submissions of that Form will populate. They also return all of the Entity Properties for each Dataset and indicate which ones are mapped to Fields in the specified Form.

Published Form Related Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/dataset-diff**

This endpoint lists the name and Properties of a Dataset that are affected by a Form. The list of Properties includes all published Properties on that Dataset, but each property has the ``inForm``\  flag to note whether or not it will be filled in by that form.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "people",
              "properties": [
                {
                  "name": "first_name",
                  "inForm": true
                }
              ]
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
                  
                    The name of the Dataset.

                    Example: ``people``
                * - properties


                  - array
                  
                    All properties of the Dataset.

                    Example: ``null``
                    
    

                     

              
      
Draft Form Dataset Diff
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/dataset-diff**

This endpoint reflects the change to a Dataset that will go into effect once the form is Published. Like the endpoint above, it lists the Dataset name and Properties, but it also includes the ``isNew``\  flag on both the Dataset, and on each individual property. This flag is true only if the Dataset/Property is new and is going to be created by publishing the Draft Form.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "people",
              "isNew": true,
              "properties": [
                {
                  "name": "first_name",
                  "inForm": true,
                  "isNew": true
                }
              ]
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
                  
                    The name of the Dataset.

                    Example: ``people``
                * - isNew


                  - boolean
                  
                    Whether or not this Dataset is new (will be created by publishing the Draft Form).

                    Example: ``true``
                * - properties


                  - array
                  
                    All properties of the Dataset.

                    Example: ``null``
                    
    

                     

              
      

