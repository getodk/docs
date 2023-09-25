.. auto generated file - DO NOT MODIFY 

Form Management
=======================================================================================================================

.. raw:: html
  
  <p><code>Form</code>s are the heart of ODK. They are created out of XML documents in the <a href="https://getodk.github.io/xforms-spec/">ODK XForms</a> specification format. The <a href="https://docs.getodk.org/form-design-intro/">Intro to Forms</a> on the ODK Documentation website is a good resource if you are unsure what this means. Once created, Forms can be retrieved in a variety of ways, their state can be managed, and they can be deleted.</p><p>These subsections cover only the modern RESTful API resources involving Forms. For documentation on the OpenRosa <code>formList</code> endpoint (which can be used to list Forms), see that section below.</p>


Forms
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>In this API, <code>Form</code>s are distinguished by their <a href="https://getodk.github.io/xforms-spec/#primary-instance"><code>formId</code></a>s, which are a part of the XForms XML that defines each Form. In fact, as you will see below, many of the properties of a Form are extracted automatically from the XML: <code>hash</code>, <code>name</code>, <code>version</code>, as well as the <code>formId</code> itself (which to reduce confusion internally is known as <code>xmlFormId</code> in ODK Central).</p><p>The only other property Forms currently have is <code>state</code>, which can be used to control whether Forms show up in mobile clients like ODK Collect for download, as well as whether they accept new <code>Submission</code>s or not.</p><p>It is not yet possible to modify a Form's XML definition once it is created.</p>

List all Forms
^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms**

.. raw:: html

  <p>Currently, there are no paging or filtering options, so listing <code>Form</code>s will get you every Form you are allowed to access, every time.</p><p>As of version 1.2, Forms that are unpublished (that only carry a draft and have never been published) will appear with full metadata detail. Previously, certain details like <code>name</code> were omitted. You can determine that a Form is unpublished by checking the <code>publishedAt</code> value: it will be <code>null</code> for unpublished forms.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>submissions</code> count of the number of Submissions that each Form has, the <code>reviewStates</code> object of counts of Submissions with specific review states, the <code>lastSubmission</code> most recent submission timestamp, as well as the Actor the Form was <code>createdBy</code>.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-03-21 12:45:02.312000+00:00``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - submissions


                  - number
                  
                    .. raw:: html

                      <p>The number of <code>Submission</code>s that have been submitted to this <code>Form</code>.</p>

                    Example: ``10``
                * - reviewStates


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - received


                            - number
                            
                              .. raw:: html

                                <p>The number of submissions receieved with no other review state.</p>

                              Example: ``3``
                          * - hasIssues


                            - number
                            
                              .. raw:: html

                                <p>The number of submissions marked as having issues.</p>

                              Example: ``2``
                          * - edited


                            - number
                            
                              .. raw:: html

                                <p>The number of edited submissions.</p>

                              Example: ``1``
                     
                * - lastSubmission


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The timestamp of the most recent submission, if any.</p>

                    Example: ``2018-04-18T03:04:51.695Z``
                * - createdBy


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
                     
                * - excelContentType


                  - string
                  
                    .. raw:: html

                      <p>If the Form was created by uploading an Excel file, this field contains the MIME type of that file.</p>

                * - entityRelated


                  - boolean
                  
                    .. raw:: html

                      <p>True only if this Form is related to a Dataset. In v2022.3, this means the Form's Submissions create Entities in a Dataset. In a future version, Submissions will also be able to update existing Entities.</p>

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

                    Example: ``403.1``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``The authenticated actor does not have rights to perform that action.``
              
      
Creating a new Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms**

.. raw:: html

  <p>When creating a <code>Form</code>, the only required data is the actual XForms XML or XLSForm itself. Use it as the <code>POST</code> body with a <code>Content-Type</code> header of <code>application/xml</code> (<code>text/xml</code> works too), and the Form will be created.</p><p>As of Version 0.8, Forms will by default be created in Draft state, accessible under <code>/projects/…/forms/…/draft</code>. The Form itself will not have a public XML definition, and will not appear for download onto mobile devices. You will need to <a href="/central-api-form-management/#publishing-a-draft-form">publish the form</a> to finalize it for data collection. To disable this behaviour, and force the new Form to be immediately ready, you can pass the querystring option <code>?publish=true</code>.</p><p>For XLSForm upload, either <code>.xls</code> or <code>.xlsx</code> are accepted. You must provide the <code>Content-Type</code> request header corresponding to the file type: <code>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</code> for <code>.xlsx</code> files, and <code>application/vnd.ms-excel</code> for <code>.xls</code> files. You must also provide an <code>X-XlsForm-FormId-Fallback</code> request header with the <code>formId</code> you want the resulting form to have, if the spreadsheet does not already specify. This header field accepts percent-encoded values to support Unicode characters and other non-ASCII values.</p><p>By default, any XLSForm conversion Warnings will fail this request and return the warnings rather than use the converted XML to create a form. To override this behaviour, provide a querystring flag <code>?ignoreWarnings=true</code>. Conversion Errors will always fail this request.</p><p>The API will currently check the XML's structure in order to extract the information we need about it, but ODK Central does <em>not</em> run comprehensive validation on the full contents of the XML to ensure compliance with the ODK specification. Future versions will likely do this, but in the meantime you will have to use a tool like <a href="https://getodk.org/use/validate/">ODK Validate</a> to be sure your Forms are correct.</p><p>You will get following workflow warnings while creating a new form or uploading a new version of an existing form:</p><ul><li><p>Structural Change: Returned when the uploaded definition of the form removes, renames or moves a field to a different group/repeat. <a href="https://docs.getodk.org/central-forms/#central-forms-updates">Learn more</a></p></li><li><p>Deleted Form: Returned when there is a form with the same ID in the Trash. <a href="https://docs.getodk.org/central-forms/#deleting-a-form">Learn more</a></p></li></ul><p><strong>Creating Datasets with Forms</strong></p><p>Starting from Version 2022.3, a Form can also create a Dataset by defining a Dataset schema in the Form definition (XForms XML or XLSForm). When a Form with a Dataset schema is uploaded, a Dataset and its Properties are created. The state of the Dataset is dependent on the state of the Form; you will need to publish the Form to publish the Dataset. Datasets in the Draft state are not returned in <a href="/central-api-dataset-management">Dataset APIs</a>, however the <a href="/central-api-form-management/#draft-form-dataset-diff">Related Datasets</a> API for the Form can be called to get the Dataset and its Properties.</p><p>It is possible to define the schema of a Dataset in multiple Forms. Such Forms can be created and published in any order. Publishing any of the Forms will also publish the Dataset and will generate a <code>dataset.create</code> event; <code>dataset.update</code> events are generated in Audit logs when a Form adds a new property in the Dataset. The state of a Property of a Dataset is also dependent on the state of the Form that FIRST defines that Property, which means if a Form is in the Draft state then the Properties defined by that Form will not appear in the <a href="/central-api-dataset-management/#download-dataset">.csv file</a> of the Dataset.</p>

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
      * - ignoreWarnings

          *(query)*

        - boolean
        
          .. raw:: html

            Defaults to `false`. Set to `true` if you want the Form to be created even if the XLSForm conversion results in warnings.

          Example: ``false``
      * - publish

          *(query)*

        - boolean
        
          .. raw:: html

            Defaults to `false`. Set to `true` if you want the Form to skip the Draft state to Published.

          Example: ``false``
      * - X-XlsForm-FormId-Fallback

          *(header)*

        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                * - state


                  - enum
                  
                    .. raw:: html

                      <p>The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.</p>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

              
      

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

              
      

Individual Form
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <span></span>

Getting Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}**

.. raw:: html

  <p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>submissions</code> count of the number of <code>Submission</code>s that this Form has, as well as the <code>lastSubmission</code> most recent submission timestamp.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - projectId


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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                * - state


                  - enum
                  
                    .. raw:: html

                      <p>The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.</p>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - submissions


                  - number
                  
                    .. raw:: html

                      <p>The number of <code>Submission</code>s that have been submitted to this <code>Form</code>.</p>

                * - reviewStates


                  - object
                  
                    .. raw:: html

                      <p>Additional counts of the number of submissions in various states of review.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - received


                            - number
                            
                              .. raw:: html

                                <p>The number of submissions receieved with no other review state.</p>

                          * - hasIssues


                            - number
                            
                              .. raw:: html

                                <p>The number of submissions marked as having issues.</p>

                          * - edited


                            - number
                            
                              .. raw:: html

                                <p>The number of edited submissions.</p>

                     
                * - lastSubmission


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The timestamp of the most recent submission, if any.</p>

                * - createdBy


                  - object
                  
                    .. raw:: html

                      <p>The full information of the Actor who created this Form.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                          * - displayName


                            - string
                            
                              .. raw:: html

                                <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                          * - id


                            - number
                            
                              .. raw:: html

                                <span></span>

                          * - type


                            - enum
                            
                              .. raw:: html

                                <p>the Type of this Actor; typically this will be <code>user</code>.</p>


                                
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

                          * - deletedAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format</p>

                     
                * - excelContentType


                  - string
                  
                    .. raw:: html

                      <p>If the Form was created by uploading an Excel file, this field contains the MIME type of that file.</p>

                * - entityRelated


                  - boolean
                  
                    .. raw:: html

                      <p>True only if this Form is related to a Dataset. In v2022.3, this means the Form's Submissions create Entities in a Dataset. In a future version, Submissions will also be able to update existing Entities.</p>

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

              
      
Deleting a Form
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}**

.. raw:: html

  <p>When a Form is deleted, it goes into the Trash section, but it can now be restored from the Trash. After 30 days in the Trash, the Form and all of its resources and submissions will be automatically purged. If your goal is to prevent it from showing up on survey clients like ODK Collect, consider setting its <code>state</code> to <code>closing</code> or <code>closed</code> instead (see <a href="/central-api-form-management/#modifying-a-form">Modifying a Form</a> just above for more details).</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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

              
      
Modifying a Form
^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}**

.. raw:: html

  <p>It is currently possible to modify only one thing about a <code>Form</code>: its <code>state</code>, which governs whether it is available for download onto survey clients and whether it accepts new <code>Submission</code>s. See the <code>state</code> Attribute in the Request documentation to the right to see the possible values and their meanings.</p><p>We use <code>PATCH</code> rather than <code>PUT</code> to represent the update operation, so that you only have to supply the properties you wish to change. Anything you do not supply will remain untouched.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - state


                  - enum
                  
                    .. raw:: html

                      <p>If supplied, the Form lifecycle state will move to this value.</p>


                      
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                * - state


                  - enum
                  
                    .. raw:: html

                      <p>The present lifecycle status of this form. Controls whether it is available for download on survey clients or accepts new submissions.</p>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

              
      

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

              
      
Retrieving Form XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.xml**

.. raw:: html

  <p>To get the XML of the <code>Form</code>, add <code>.xml</code> to the end of the request URL.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

.. raw:: html

  <p>If a Form was created with an Excel file (<code>.xls</code> or <code>.xlsx</code>), you can get that file back by adding <code>.xls</code> or <code>.xlsx</code> as appropriate to the Form resource path.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <p>If a Form was created with an Excel file (<code>.xls</code> or <code>.xlsx</code>), you can get that file back by adding <code>.xls</code> or <code>.xlsx</code> as appropriate to the Form resource path.</p>

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

              
      
Listing Form Attachments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/attachments**

.. raw:: html

  <p>This endpoint allows you to fetch the list of expected attachment files, and will tell you whether the server is in possession of each file or not. To modify an attachment, you'll need to create a Draft.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the XForm.</p>

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>True if the server has the file or the Attachment is linked to a Dataset, otherwise false.</p>

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether attachment is linked to a Dataset.</p>

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).</p>

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
              
      
Downloading a Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/attachments/{filename}**

.. raw:: html

  <p>To download a single file, use this endpoint. The appropriate <code>Content-Disposition</code> (attachment with a filename) and <code>Content-Type</code> (based on the type supplied at upload time) will be given.</p><p>This endpoint supports <code>ETag</code>, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, it returns a value in <code>ETag</code> header, you can pass this value in the header <code>If-None-Match</code> of subsequent requests. If the file has not been changed since the previous request, you will receive <code>304 Not Modified</code> response otherwise you'll get the latest file.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

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

              
      
Getting Form Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/fields**

.. raw:: html

  <p><em>(introduced: version 0.8)</em></p><p>For applications that do not rely on JavaRosa, it can be challenging to parse XForms XML into a simple schema structure. Because Central Backend already implements and performs such an operation for its own internal purposes, we also expose this utility for any downstream consumers which wish to make use of it.</p><p>While this may eventually overlap with the new OData JSON CSDL specification, we are likely to maintain this API as it more closely mirrors the original XForms data types and structure.</p><p>Central internally processes the XForms schema tree into a flat list of fields, and this is how the data is returned over this endpoint as well. It will always return fields in a <em>depth-first traversal order</em> of the original <code>&lt;instance&gt;</code> XML block in the XForm.</p><p>You may optionally add the querystring parameter <code>?odata=true</code> to sanitize the field names and paths to match the way they will be outputted for OData. While the original field names as given in the XForms definition may be used as-is for CSV output, OData has some restrictions related to the domain-qualified identifier syntax it uses.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - odata

          *(query)*

        - boolean
        
          .. raw:: html

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

                      <span></span>

                * - path


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - type


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - binary


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

              
      
Restoring a Form
^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{id}/restore**

.. raw:: html

  <p><em>(introduced: version 1.4)</em></p><p>Deleted forms can now be restored (as long as they have been in the Trash less than 30 days and have not been purged). However, a deleted Form with the same <code>xmlFormId</code> as an active Form cannot be restored while that other Form is active. This <code>/restore</code> URL uses the numeric ID of the Form (now returned by the <code>/forms</code> endpoint) rather than the <code>xmlFormId</code> to unambigously restore.</p>

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
      * - id


        - string
        
          .. raw:: html

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

              
      

Draft Form
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.8)</em></p><p>Draft Forms allow you to test and fix issues with Forms before they are finalized and presented to data collectors. They make this process easier, as Draft Forms can be created and discarded without consequence: your Drafts will not count against the overall Form schema, nor against the set of unique <code>version</code> strings for the Form.</p><p>You can create or replace the current Draft Form at any time by <code>POST</code>ing to the <code>/draft</code> subresource on the Form, and you can publish the current Draft by <code>POST</code>ing to <code>/draft/publish</code>.</p><p>When a Draft Form is created, a Draft Token is also created for it, which can be found in Draft Form responses at <code>draftToken</code>. This token allows you to <a href="/central-api-submission-management/#creating-a-submission">submit test Submissions to the Draft Form</a> through clients like Collect. If the Draft is published or deleted, the token will be deactivated. But if you replace the Draft without first deleting it, the existing Draft Token will be carried forward, so that you do not have to reconfigure your device.</p>

Getting Draft Form Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft**

.. raw:: html

  <p>The response here will include standard overall Form metadata, like <code>xmlFormId</code>, in addition to the Draft-specific information.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - draftToken


                  - string
                  
                    .. raw:: html

                      <p>The test token to use to submit to this draft form. See <a href="/central-api-submission-management/#draft-submissions">Draft Testing Endpoints</a>.</p>

                    Example: ``lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this draft Form on Enketo at <code>/-</code>. Authentication is not needed to access the draft form through Enketo.</p>

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

              
      
Creating a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft**

.. raw:: html

  <p><code>POST</code>ing here will create a new Draft Form on the given Form. For the most part, it takes the same parameters as the <a href="/central-api-form-management/#creating-a-new-form">Create Form request</a>: you can submit XML or Excel files, you can provide <code>ignoreWarnings</code> if you'd like.</p><p>Additionally, however, you may <code>POST</code> with no <code>Content-Type</code> and an empty body to create a Draft Form with a copy of the definition (XML, XLS, etc) that is already published, if there is one. This can be useful if you don't wish to update the Form definition itself, but rather one or more Form Attachments.</p><p>If your Draft form schema contains any field path which overlaps with a field path of a previous version of the Form, but with a different data type, your request will be rejected. You can rename the conflicting field, or correct it to have the same data type as it did previously.</p><p>When a Draft is created, the expected Form Attachments are computed and slots are created, as with a new Form. Any attachments that match existing ones on the published Form, if it exists, will be copied over to the new Draft.</p><p>Even if a Draft exists, you can always replace it by <code>POST</code>ing here again. In that case, the attachments that exist on the Draft will similarly be copied over to the new Draft. If you wish to copy from the published version instead, you can do so by first <code>DELETE</code>ing the extant Draft.</p><p>Draft <code>version</code> conflicts are allowed with prior versions of a Form while in Draft state. If you attempt to <a href="/central-api-form-management/#draft-form/publishing-a-draft-form">publish the Form</a> without correcting the conflict, the publish operation will fail. You can request that Central update the version string on your behalf as part of the publish operation to avoid this: see that endpoint for more information.</p><p>The <code>xmlFormId</code>, however, must exactly match that of the Form overall, or the request will be rejected.</p><p>Starting from Version 2022.3, a Draft Form can also create or update a Dataset by defining a Dataset schema in the Form definition. The state of the Dataset and its Properties is dependent on the state of the Form, see <a href="/central-api-form-management/#creating-a-new-form">Creating a new form</a> for more details.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - ignoreWarnings

          *(query)*

        - boolean
        
          .. raw:: html

            Defaults to `false`. Set to `true` if you want the form to be created even if the XLSForm conversion results in warnings.

          Example: ``false``
      * - X-XlsForm-FormId-Fallback

          *(header)*

        - string
        
          .. raw:: html

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

              
      
Deleting a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft**

.. raw:: html

  <p>Once a Draft Form is deleted, its definition and any Form Attachments associated with it will be removed.</p><p>You will not be able to delete the draft if there is no published version of the form.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

              
      
Retrieving Draft Form XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.xml**

.. raw:: html

  <p>To get the XML of the Draft Form, add <code>.xml</code> to the end of the request URL.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

.. raw:: html

  <p>If a Draft Form was created with an Excel file (<code>.xls</code> or <code>.xlsx</code>), you can get that file back by adding <code>.xls</code> or <code>.xlsx</code> as appropriate to the Draft Form resource path.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

.. raw:: html

  <p>Form Attachments for each form are automatically determined when the form is first created, by scanning the XForms definition for references to media or data files. Because of this, it is not possible to directly modify the list of form attachments; that list is fully determined by the given XForm. Instead, the focus of this API subresource is around communicating that expected list of files, and uploading binaries into those file slots.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the XForm.</p>

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>True if the server has the file or the Attachment is linked to a Dataset, otherwise false.</p>

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether attachment is linked to a Dataset.</p>

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).</p>

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
              
      
Downloading a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

.. raw:: html

  <p>To download a single file, use this endpoint. The appropriate <code>Content-Disposition</code> (attachment with a filename or Dataset name) and <code>Content-Type</code> (based on the type supplied at upload time or <code>text/csv</code> in the case of a linked Dataset) will be given.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <p>To download a single file, use this endpoint. The appropriate <code>Content-Disposition</code> (attachment with a filename or Dataset name) and <code>Content-Type</code> (based on the type supplied at upload time or <code>text/csv</code> in the case of a linked Dataset) will be given.</p>

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

              
      
Uploading a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

.. raw:: html

  <p>To upload a binary to an expected file slot, <code>POST</code> the binary to its endpoint. Supply a <code>Content-Type</code> MIME-type header if you have one.</p><p>As of version 2022.3, if there is already a Dataset linked to this attachment, it will be unlinked and replaced with the uploaded file.</p><p>This endpoint supports <code>ETag</code> header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in <code>ETag</code> header. If you pass that value in the <code>If-None-Match</code> header of a subsequent request, then if the file has not been changed since the previous request, you will receive <code>304 Not Modified</code> response; otherwise you'll get the latest file.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          .. raw:: html

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

              
      
Clearing a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

.. raw:: html

  <p>Because Form Attachments are completely determined by the XForms definition of the form itself, there is no direct way to entirely remove a Form Attachment entry from the list, only to clear its uploaded content or to unlink the Dataset. Thus, when you issue a <code>DELETE</code> to the attachment's endpoint, that is what happens.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          .. raw:: html

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

              
      
Linking a Dataset to a Draft Form Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}/draft/attachments/{filename}**

.. raw:: html

  <p><em>(introduced: version 2022.3)</em></p><p>This endpoint can update a Form Attachment's link to a Dataset. You can use this to link or unlink a Dataset to a Form Attachment. Linking of a Dataset to the Attachment only happens if the Attachment type is <code>file</code> and there is a Dataset with the exact name of the Attachment (excluding extension <code>.csv</code>) in the Project. For example, if the Form definition includes an Attachment named <code>people.csv</code>, then it can be linked to a Dataset named <code>people</code>. Pay special attention to letter case and spaces.</p><p>When linking a Dataset, if there is any existing file attached then it will be removed.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - dataset


                  - boolean
                  
                    .. raw:: html

                      <p>true for linking Dataset and false for unlinking Dataset.</p>

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

              
      
Getting Draft Form Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/fields**

.. raw:: html

  <p>Identical to the <a href="/central-api-form-management/#getting-form-schema-fields">same request</a> for the published Form, but will return the fields related to the current Draft version.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - odata

          *(query)*

        - boolean
        
          .. raw:: html

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

                      <span></span>

                * - path


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - type


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - binary


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

              
      
Publishing a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/publish**

.. raw:: html

  <p>This will publish your current Draft Form and make it the active Form definition (and attachments).</p><p>If your Draft <code>version</code> conflicts with an older version of the Form, you will get an error.</p><p>If you wish for the <code>version</code> to be set on your behalf as part of the publish operation, you can provide the new version string as a querystring parameter <code>?version</code>.</p><p>Once the Draft is published, there will no longer be a Draft version of the form.</p><p>Starting with Version 2022.3, publishing a Draft Form that defines a Dataset schema will also publish the Dataset. It will generate <code>dataset.create</code> event in Audit logs and make the Dataset available in <a href="/central-api-dataset-management">Datasets APIs</a>. If the Dataset is already published and the Form adds new properties then <code>dataset.update</code> event will be generated.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version

          *(query)*

        - string
        
          .. raw:: html

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

              
      

Published Form Versions
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>All published versions of a Form are available read-only at the <code>/versions</code> subresource for reference, including the currently published version. You may read that version and its details, retrieve the Form definition, and any attachments associated with each version.</p>

Listing Published Form Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions**

.. raw:: html

  <p>Each entry of the version listing will contain some of the same duplicate keys with basic information about the Form: <code>xmlFormId</code> and <code>createdAt</code>, for example. This is done to match the data you'd receive if you'd requested each version separately.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>Actor</code> that each version was <code>publishedBy</code>.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-03-21 12:45:02.312000+00:00``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-03-21 12:45:02.312000+00:00``
                * - publishedBy


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
                     
                * - excelContentType


                  - string
                  
                    .. raw:: html

                      <p>If the Form was created by uploading an Excel file, this field contains the MIME type of that file.</p>


              
      

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
              
      
Getting Form Version Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}**

.. raw:: html

  <p>Since the XForms specification allows blank strings as <code>version</code>s (and Central treats the lack of a <code>version</code> as a blank string), you may run into trouble using this resource if you have such a Form. In this case, pass the special value <code>___</code> (three underscores) as the <code>version</code> to retrieve the blank <code>version</code> version.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The <code>id</code> of the project this form belongs to.</p>

                    Example: ``1.0``
                * - xmlFormId


                  - string
                  
                    .. raw:: html

                      <p>The <code>id</code> of this form as given in its XForms XML definition</p>

                    Example: ``simple``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The friendly name of this form. It is given by the <code>&lt;title&gt;</code> in the XForms XML definition.</p>

                    Example: ``Simple``
                * - version


                  - string
                  
                    .. raw:: html

                      <p>The <code>version</code> of this form as given in its XForms XML definition. If no <code>version</code> was specified in the Form, a blank string will be given.</p>

                    Example: ``2.1``
                * - enketoId


                  - string
                  
                    .. raw:: html

                      <p>If it exists, this is the survey ID of this Form on Enketo at <code>/-</code>. This will be the ID of the published version if it exists, otherwise it will be the draft ID. Only a cookie-authenticated user may access the preview through Enketo.</p>

                    Example: ``abcdef``
                * - hash


                  - string
                  
                    .. raw:: html

                      <p>An MD5 sum automatically computed based on the XForms XML definition. This is required for OpenRosa compliance.</p>

                    Example: ``51a93eab3a1974dbffc4c7913fa5a16a``
                * - keyId


                  - number
                  
                    .. raw:: html

                      <p>If a public encryption key is present on the form, its numeric ID as tracked by Central is given here.</p>

                    Example: ``3.0``
                * - state


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>Indicates when a draft has most recently been published for this Form. If this value is <code>null</code>, this Form has never been published yet, and contains only a draft.</p>

                    Example: ``2018-01-21 00:04:11.153000+00:00``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-01-19 23:58:03.395000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

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

              
      
Retrieving Form Version XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}.xml**

.. raw:: html

  <p>To get the XML of the Form Version, add <code>.xml</code> to the end of the request URL.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

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

.. raw:: html

  <p>If a Form Version was created with an Excel file (<code>.xls</code> or <code>.xlsx</code>), you can get that file back by adding <code>.xls</code> or <code>.xlsx</code> as appropriate to the Form Version resource path.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

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

.. raw:: html

  <p>Attachments are specific to each version of a Form. You can retrieve the attachments associated with a given version here.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the XForm.</p>

                    Example: ``myfile.mp3``
                * - type


                  - enum
                  
                    .. raw:: html

                      <span></span>


                      
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
                  
                    .. raw:: html

                      <p>True if the server has the file or the Attachment is linked to a Dataset, otherwise false.</p>

                    Example: ``true``
                * - blobExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``
                * - datasetExists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether attachment is linked to a Dataset.</p>

                    Example: ``true``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this file's binary content was set (POST) or cleared (DELETE).</p>

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

              
      
Downloading a Form Version Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}/attachments/{filename}**

.. raw:: html

  <p>To download a single file, use this endpoint. The appropriate <code>Content-Disposition</code> (attachment with a filename) and <code>Content-Type</code> (based on the type supplied at upload time) will be given.</p><p>This endpoint supports <code>ETag</code> header, which can be used to avoid downloading the same content more than once. When an API consumer calls this endpoint, the endpoint returns a value in <code>ETag</code> header. If you pass that value in the <code>If-None-Match</code> header of a subsequent request, then if the file has not been changed since the previous request, you will receive <code>304 Not Modified</code> response; otherwise you'll get the latest file.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

            The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

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

              
      
Getting Form Version Schema Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/versions/{version}/fields**

.. raw:: html

  <p>Identical to the <a href="/central-api-form-management/#getting-form-schema-fields">same request</a> for the published Form, but will return the fields related to the specified version.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - version


        - string
        
          .. raw:: html

            The `version` of the Form version being referenced. Pass `___` to indicate a blank `version`.

          Example: ``one``
      * - odata

          *(query)*

        - boolean
        
          .. raw:: html

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

                      <span></span>

                * - path


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - type


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - binary


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

              
      

Form Assignments
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.7)</em></p><p>There are multiple Assignments resources. This one, specific to the Form it is nested within, only governs Role assignments to that Form. Assigning an Actor a Role that grants, for example, a verb <code>submission.create</code>, allows that Actor to create a submission to this Form alone. It is also possible to assign umbrella rights to a whole Project and therefore all Forms within it: see the <a href="/central-api-project-management/#project-assignments">Project Assignments resource</a> for information about this.</p><p>The <a href="/central-api-accounts-and-users/#assignments">sitewide Assignments resource</a>, at the API root, manages Role assignments for all objects across the server. Apart from this difference in scope, the introduction to that section contains information useful for understanding the following endpoints.</p><p>There are only one set of Roles, applicable to either scenario. There are not a separate set of Roles used only upon Projects or Forms.</p>

Listing all Form Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/assignments**

.. raw:: html

  <p>This will list every assignment upon this Form, in the form of <code>actorId</code>/<code>roleId</code> pairs.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to expand the <code>actorId</code> into a full <code>actor</code> objects. The Role reference remains a numeric ID.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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
              
      
Listing all Actors assigned some Form Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, this endpoint lists all <code>Actors</code> that have been assigned that Role upon this particular Form.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - roleId


        - string
        
          .. raw:: html

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
              
      
Assigning an Actor to a Form Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, assigns that Role to that Actor for this particular Form.</p><p>No <code>POST</code> body data is required, and if provided it will be ignored.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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
              
      
Revoking a Form Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, unassigns that Role from that Actor for this particular Form.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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

              
      

Public Access Links
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.0)</em></p><p>Anybody in possession of a Public Access Link for a Form can use that link to submit data to that Form. Public Links are useful for collecting direct responses from a broad set of respondents, and can be revoked using the administration website or the API at any time.</p><p>The API for Public Links is particularly useful, as it can be used to, for example, programmatically create and send individually customized and controlled links for direct distribution. The user-facing link for a Public Link has the following structure: <code>/-/{enketoId}?st={token}</code> where <code>-</code> is the Enketo root, <code>enketoId</code> is the survey ID of this published Form on Enketo and <code>token</code> is a session token to identify this Public Link.</p><p>To revoke the access of any Link, terminate its session <code>token</code> by issuing <a href="/central-api-authentication/#logging-out"><code>DELETE /sessions/:token</code></a>.</p>

Listing all Links
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/public-links**

.. raw:: html

  <p>This will list every Public Access Link upon this Form.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to retrieve the Actor the Link was <code>createdBy</code>.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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
                * - token


                  - string
                  
                    .. raw:: html

                      <p>If present, this is the Token to include as the <code>st</code> query parameter for this <code>Public Link</code>. If not present, this <code>Public Link</code> has been revoked.</p>

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - once


                  - boolean
                  
                    .. raw:: html

                      <p>If set to <code>true</code>, an Enketo <a href="https://blog.enketo.org/single-submission-surveys/">single submission survey</a> will be created instead of a standard one, limiting respondents to a single submission each.</p>

                    Example: ``none``

              
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
                * - token


                  - string
                  
                    .. raw:: html

                      <p>If present, this is the Token to include as the <code>st</code> query parameter for this <code>Public Link</code>. If not present, this <code>Public Link</code> has been revoked.</p>

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - once


                  - boolean
                  
                    .. raw:: html

                      <p>If set to <code>true</code>, an Enketo <a href="https://blog.enketo.org/single-submission-surveys/">single submission survey</a> will be created instead of a standard one, limiting respondents to a single submission each.</p>

                    Example: ``none``
                * - createdBy


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
                     

              
      
Creating a Link
^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/public-links**

.. raw:: html

  <p>To create a new Public Access Link to this Form, you must send at least a <code>displayName</code> for the resulting Actor. You may also provide <code>once: true</code> if you want to create a link that <a href="https://blog.enketo.org/single-submission-surveys/">can only be filled by each respondent once</a>. This setting is enforced by Enketo using local device tracking; the link is still distributable to multiple recipients, and the enforcement can be defeated by using multiple browsers or devices.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - displayName


                  - string
                  
                    .. raw:: html

                      <p>The name of the Link, for keeping track of. This name is displayed on the Central administration website but not to survey respondents.</p>

                * - once


                  - boolean
                  
                    .. raw:: html

                      <p>If set to <code>true</code>, an Enketo <a href="https://blog.enketo.org/single-submission-surveys/">single submission survey</a> will be created instead of a standard one, limiting respondents to a single submission each.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - displayName


                  - string
                  
                    .. raw:: html

                      <p>All <code>Actor</code>s, regardless of type, have a display name</p>

                * - id


                  - number
                  
                    .. raw:: html

                      <span></span>

                * - type


                  - enum
                  
                    .. raw:: html

                      <p>the Type of this Actor; typically this will be <code>user</code>.</p>


                      
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

                * - deletedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - token


                  - string
                  
                    .. raw:: html

                      <p>If present, this is the Token to include as the <code>st</code> query parameter for this <code>Public Link</code>. If not present, this <code>Public Link</code> has been revoked.</p>

                * - once


                  - boolean
                  
                    .. raw:: html

                      <p>If set to <code>true</code>, an Enketo <a href="https://blog.enketo.org/single-submission-surveys/">single submission survey</a> will be created instead of a standard one, limiting respondents to a single submission each.</p>

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

              
      
Deleting a Link
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/public-links/{linkId}**

.. raw:: html

  <p>You can fully delete a link by issuing <code>DELETE</code> to its resource. This will remove the Link from the system entirely. If instead you wish to revoke the Link's access to prevent future submission without removing its record entirely, you can issue <a href="/central-api-authentication/#session-authentication/logging-out"><code>DELETE /sessions/:token</code></a>.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - linkId


        - integer
        
          .. raw:: html

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

              
      

Related Datasets
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 2022.3)</em></p><p>Datasets are created and updated through Forms. Dataset-related Forms follow <a href="https://getodk.github.io/xforms-spec/entities">the entities sub-spec</a> of the ODK XForms specification that allow them to define a Dataset and a mapping of Form Fields to Dataset Properties. Submissions from such a Form can create Entities within the Dataset defined in the Form.</p><p>Currently, Datasets and Dataset Properties are purely additive. Multiple Forms can add Properties to the same Dataset and multiple Forms can create Entities in the same Dataset. Not all Properties of a Dataset have to be included in a Form for that Dataset. For example, one Form publishing to a Dataset called <code>trees</code> could add <code>location</code> and <code>species</code>, while another could add <code>species</code> and <code>circumference</code>. The Properties of the Dataset would be the union of Properties from all Forms for that Dataset (<code>location</code>, <code>species</code>, <code>circumference</code>). Note that it is not necessary that a Form will save to all Properties of a Dataset, so the endpoint also returns a <code>inForm</code> flag for each property which is true only if the Form affects that Property.</p><p>The following endpoints return the Dataset(s) that Submissions of that Form will populate. They also return all of the Entity Properties for each Dataset and indicate which ones are mapped to Fields in the specified Form.</p>

Published Form Related Datasets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/dataset-diff**

.. raw:: html

  <p>This endpoint lists the name and Properties of a Dataset that are affected by a Form. The list of Properties includes all published Properties on that Dataset, but each property has the <code>inForm</code> flag to note whether or not it will be filled in by that form.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

                      <p>The name of the Dataset.</p>

                    Example: ``people``
                * - properties


                  - array
                  
                    .. raw:: html

                      <p>All properties of the Dataset.</p>

                    Example: ``null``
                    
    

                     

              
      
Draft Form Dataset Diff
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/dataset-diff**

.. raw:: html

  <p>This endpoint reflects the change to a Dataset that will go into effect once the form is Published. Like the endpoint above, it lists the Dataset name and Properties, but it also includes the <code>isNew</code> flag on both the Dataset, and on each individual property. This flag is true only if the Dataset/Property is new and is going to be created by publishing the Draft Form.</p>

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
      * - xmlFormId


        - string
        
          .. raw:: html

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

                      <p>The name of the Dataset.</p>

                    Example: ``people``
                * - isNew


                  - boolean
                  
                    .. raw:: html

                      <p>Whether or not this Dataset is new (will be created by publishing the Draft Form).</p>

                    Example: ``true``
                * - properties


                  - array
                  
                    .. raw:: html

                      <p>All properties of the Dataset.</p>

                    Example: ``null``
                    
    

                     

              
      

