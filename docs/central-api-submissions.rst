.. auto generated file - DO NOT MODIFY

Submissions
=======================================================================================================================

``Submission``\ s are filled-out forms (also called ``Instance``\ s in some other ODK documentation). Each is associated with a particular Form (and in many cases with a particular *version*\  of a Form), and is also created out of a standard XML format based on the Form itself. Submissions can be sent with many accompanying multimedia attachments, such as photos taken in the course of the survey. Once created, the Submissions themselves as well as their attachments can be retrieved through this API.

These subsections cover only the modern RESTful API resources involving Submissions. For documentation on the OpenRosa submission endpoint (which can be used to submit Submissions), or the OData endpoint (which can be used to retrieve and query submission data), see those sections below.

> Like Forms, Submissions can have versions. Each Form has an overall ``xmlFormId``\  that represents the Form as a whole, and each version has a ``version``\  that identifies that particular version. Often, when fetching data by the ``xmlFormId``\  alone, information from the latest Form version is included in the response.

> Similarly with Submissions, the ``instanceId``\  each Submission is first submitted with will always represent that Submission as a whole. Each version of the Submission, though, has its own ``instanceId``\ . Sometimes, but not very often, when getting information about the Submission by only its overall ``instanceId``\ , information from the latest Submission version is included in the response.

Listing all Submissions on a Form
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions**

Currently, there are no paging or filtering options, so listing ``Submission``\ s will get you every Submission in the system, every time.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``submitter``\  data object alongside the ``submitterId``\  Actor ID reference.

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

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "reviewState": "approved",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "updatedAt": "2018-03-21T12:45:02.312Z",
              "currentVersion": {
                "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
                "instanceName": "village third house",
                "submitterId": 23,
                "deviceId": "imei:123456",
                "userAgent": "Enketo/3.0.4",
                "createdAt": "2018-01-19T23:58:03.395Z",
                "current": true
              },
              "submitter": {
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

              
      
  
Creating a Submission
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions**

To create a Submission by REST rather than over the `OpenRosa interface </reference/openrosa-endpoints/openrosa-form-submission-api>`__, you may ``POST``\  the Submission XML to this endpoint. The request must have an XML ``Content-Type``\  (``text/xml``\  or ``application/xml``\ ).

Unlike the OpenRosa Form Submission API, this interface does *not*\  accept Submission attachments upon Submission creation. Instead, the server will determine which attachments are expected based on the Submission XML, and you may use the endpoints found in the following section to add the appropriate attachments and check the attachment status and content.

If the XML is unparseable or there is some other input problem with your data, you will get a ``400``\  error in response. If a submission already exists with the given ``instanceId``\ , you will get a ``409``\  error in response.

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
      * - deviceID

          *(query)*

        - string
        
          Optionally record a particular `deviceID` associated with this submission. It is recorded along with the data, but Central does nothing more with it.

          Example: ``b1628661-65ed-4cab-8e30-19c17fef2de0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
              
      

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Getting Submission metadata
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

Like how ``Form``\ s are addressed by their XML ``formId``\ , individual ``Submission``\ s are addressed in the URL by their ``instanceId``\ .

As of version 1.4, a ``deviceId``\  and ``userAgent``\  will also be returned with each submission. The client device may transmit these extra metadata when the data is submitted. If it does, those fields will be recognized and returned here for reference. Here, only the initial ``deviceId``\  and ``userAgent``\  will be reported. If you wish to see these metadata for any submission edits, including the most recent edit, you will need to `list the versions </reference/submissions/submission-versions/listing-versions>`__.

As of version 2023.2, this API returns ``currentVersion``\  that contains metadata of the most recent version of the Submission.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``submitter``\  data object alongside the ``submitterId``\  Actor ID reference.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            },
            "submitter": {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
                * - submitter


                  - object
                  
                    The full details of the ``Actor``\  that submitted this ``Submission``\ .


                      
                    .. collapse:: expand

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
                            
                              None

                          * - type


                            - string
                            
                              the Type of this Actor; typically this will be ``user``\ .

                          * - updatedAt


                            - string
                            
                              ISO date format

                          * - deletedAt


                            - string
                            
                              ISO date format

                     
              
      

  **HTTP Status: 301**

  Content Type: text/html

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

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

              
      
  
Updating Submission Data
-----------------------------------------------------------------------------------------------------------------------

**PUT /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

*(introduced: version 1.2)*\ 

You can use this endpoint to submit *updates*\  to an existing submission.

The ``instanceId``\  that is submitted with the initial version of the submission is used permanently to reference that submission logically, which is to say the initial submission and all its subsequent versions. Each subsequent version will also provide its own ``instanceId``\ . This ``instanceId``\  becomes that particular version's identifier.

To perform an update, you need to provide in the submission XML an additional ```deprecatedID``\  metadata node <https://getodk.github.io/xforms-spec/#metadata>`__ with the ``instanceID``\  of the particular and current submission version you are replacing. If the ``deprecatedID``\  you give is anything other than the identifier of the current version of the submission at the time the server receives it, you will get a ``409 Conflict``\  back. You can get the current version ``instanceID``\  by getting the `current XML of the submission </reference/submissions/submissions/retrieving-submission-xml>`__.

The XML data you send will *replace*\  the existing data entirely. All of the data must be present in the updated XML.

When you create a new submission version, any uploaded media files attached to the current version that match expected attachment names in the new version will automatically be copied over to the new version. So if you don't make any changes to media files, there is no need to resubmit them. You can get information about all the submission versions `from the ``/versions``\  subresource <reference/submissions/submission-versions>`__.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being updated.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
              
      

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Updating Submission metadata
-----------------------------------------------------------------------------------------------------------------------

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

Currently, the only updatable *metadata*\  on a Submission is its ``reviewState``\ . To update the submission *data*\  itself, please see `Updating Submission data </reference/submissions/submissions/updating-submission-data>`__.

Starting with Version 2022.3, changing the ``reviewState``\  of a Submission to ``approved``\  can create an Entity in a Dataset if the corresponding Form maps Dataset Properties to Form Fields. If an Entity is created successfully then an ``entity.create``\  event is logged in Audit logs, else ``entity.create.error``\  is logged.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
              
      

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

              
      
  
Retrieving Submission XML
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}.xml**

To get only the XML of the ``Submission``\  rather than all of the details with the XML as one of many properties, just add ``.xml``\  to the end of the request URL.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <data id="simple">
            <orx:meta><orx:instanceID>uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44</orx:instanceID></orx:meta>
            <name>Alice</name>
            <age>32</age>
          </data>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
Getting an Enketo Edit URL
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/edit**

*(introduced: version 1.2)*\ 

This endpoint redirects the user to an Enketo-powered page that allows the user to interactively edit the submission. Once the user is satisfied, they can perform the submission update directly through the Enketo interface.

The Enketo instance is already hosted inside of ODK Central. There is no reason to create or use a separate Enketo installation.

This endpoint is intended for use by the Central administration frontend and will not work without it. In particular, the user must be logged into the Central administration site for Enketo editing to work. If there is no Central authentication cookie present when Enketo is loaded, the browser will then be redirected by Enketo to a Central login page.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being updated.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

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

              
      
  
Exporting Form Submissions to CSV
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv.zip**

To export all the ``Submission``\  data associated with a ``Form``\ , just add ``.csv.zip``\  to the end of the listing URL. The response will be a ZIP file containing one or more CSV files, as well as all multimedia attachments associated with the included Submissions.

You can exclude the media attachments from the ZIP file by specifying ``?attachments=false``\ .

If `Project Managed Encryption </reference/encryption>`__ is being used, additional querystring parameters may be provided in the format ``{keyId}={passphrase}``\  for any number of keys (eg ``1=secret&4=password``\ ). This will decrypt any records encrypted under those managed keys. Submissions encrypted under self-supplied keys will not be decrypted. **Note**\ : if you are building a browser-based application, please consider the alternative ``POST``\  endpoint, described in the following section.

If a passphrase is supplied but is incorrect, the entire request will fail. If a passphrase is not supplied but encrypted records exist, only the metadata for those records will be returned, and they will have a ``status``\  of ``not decrypted``\ .

If you are running an unsecured (``HTTP``\  rather than ``HTTPS``\ ) Central server, it is not a good idea to export data this way as your passphrase and the decrypted data will be sent plaintext over the network.

You can use an `OData-style ``$filter``\  query </reference/odata-endpoints/odata-form-service/data-document>`__ to filter the submissions that will appear in the ZIP file. This is a bit awkward, since this endpoint has nothing to do with OData, but since we already must recognize the OData syntax, it is less strange overall for now not to invent a whole other one here. Only a subset of the ``$filter``\  features are available; please see the linked section for more information.

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
      * - attachments

          *(query)*

        - boolean
        
          Set to false to exclude media attachments from the export.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the given OData query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - groupPaths

          *(query)*

        - boolean
        
          Set to false to remove group path prefixes from field header names (eg `instanceID` instead of `meta-instanceID`). This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``true``
      * - deletedFields

          *(query)*

        - boolean
        
          Set to true to restore all fields previously deleted from this form for this export. All known fields and data for those fields will be merged and exported.

          Example: ``false``
      * - splitSelectMultiples

          *(query)*

        - boolean
        
          Set to true to create a boolean column for every known select multiple option in the export. The option name is in the field header, and a `0` or a `1` will be present in each cell indicating whether that option was checked for that row. This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``false``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Exporting Form Submissions to CSV via POST
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv.zip**

This non-REST-compliant endpoint is provided for use with `Project Managed Encryption </reference/encryption>`__. In every respect, it behaves identically to the ``GET``\  endpoint described in the previous section, except that it works over ``POST``\ . This is necessary because for browser-based applications, it is a dangerous idea to simply link the user to ``/submissions.csv.zip?2=supersecretpassphrase``\  because the browser will remember this route in its history and thus the passphrase will become exposed. This is especially dangerous as there are techniques for quickly learning browser-visited URLs of any arbitrary domain.

You can exclude the media attachments from the ZIP file by specifying ``?attachments=false``\ .

And so, for this ``POST``\  version of the Submission CSV export endpoint, the passphrases may be provided via ``POST``\  body rather than querystring. Two formats are supported: form URL encoding (``application/x-www-form-urlencoded``\ ) and JSON. In either case, the keys should be the ``keyId``\ s and the values should be the ``passphrase``\ s, as with the ``GET``\  version above.

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
      * - attachments

          *(query)*

        - boolean
        
          Set to false to exclude media attachments from the export.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the given OData query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - groupPaths

          *(query)*

        - boolean
        
          Set to false to remove group path prefixes from field header names (eg `instanceID` instead of `meta-instanceID`). This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``true``
      * - deletedFields

          *(query)*

        - boolean
        
          Set to true to restore all fields previously deleted from this form for this export. All known fields and data for those fields will be merged and exported.

          Example: ``false``
      * - splitSelectMultiples

          *(query)*

        - boolean
        
          Set to true to create a boolean column for every known select multiple option in the export. The option name is in the field header, and a `0` or a `1` will be present in each cell indicating whether that option was checked for that row. This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``false``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Exporting Root Data to Plain CSV
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv**

*(introduced: version 1.1)*\ 

The above submission endpoints will give you a ZIP file with the submission data in it. This is necessary to provide all the possible related repeat table files, as well as the media files associated with the submissions. But ZIP files can be difficult to work with, and many Forms have no repeats nor media attachments.

To export *just*\  the root table (no repeat data nor media files), you can call this endpoint instead, which will directly give you CSV data.

Please see the `above endpoint </reference/submissions/submissions/exporting-form-submissions-to-csv>`__ for notes on dealing with Managed Encryption.

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
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the given OData query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Exporting Root Data to Plain CSV via POST
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv**

*(introduced: version 1.1)*\ 

This endpoint is useful only for Forms under Project Managed Encryption.

As with ``GET``\  to ``.csv``\  just above, this endpoint will only return CSV text data, rather than a ZIP file containing ore or more files. Please see that endpoint for further explanation.

As with ```POST``\  to ``.csv.zip``\  </reference/submissions/submissions/exporting-form-submissions-to-csv-via-post>`__ it allows secure submission of decryption passkeys. Please see that endpoint for more information on how to do this.

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
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the given OData query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Retrieving Audit Logs
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/audits**

*(introduced: version 1.2)*\ 

You can retrieve all `Server Audit Logs </reference/system-endpoints/server-audit-logs>`__ relating to a submission. They will be returned most recent first.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally expand the ``actorId``\  into full ``actor``\  details, and ``acteeId``\  into full ``actee``\  details. The ``actor``\  will always be an Actor, and the ``actee``\  will be the Form this Submission is a part of.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "actorId": 42,
              "action": "form.create",
              "acteeId": "85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "loggedAt": "2018-04-18T23:19:14.802Z",
              "actor": {
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

              
      
  
Listing Encryption Keys
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/keys**

This endpoint provides a listing of all known encryption keys needed to decrypt all Submissions for a given Form. It will return at least the ``base64RsaPublicKey``\  property (as ``public``\ ) of all known versions of the form that have submissions against them. If managed keys are being used and a ``hint``\  was provided, that will be returned as well.

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
            {}
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Listing Submitters
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/submitters**

This endpoint provides a listing of all known submitting actors to a given Form. Each Actor that has submitted to the given Form will be returned once.

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
            {}
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Listing Comments
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/comments**

Comments have only a ``body``\  comment text and an ``actor``\  that made the comment.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``actor``\  data object alongside the ``actorId``\  Actor ID reference.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "body": "this is my comment",
              "actorId": 42,
              "actor": {
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

              
      
  
Posting Comments
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/comments**

Currently, the only accepted data is ``body``\ , which contains the body of the comment to be made.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "body": "this is the text of my comment"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    The text of the comment.

              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "body": "this is my comment",
            "actorId": 42
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    The text of the comment.

                * - actorId


                  - number
                  
                    The ID of the Actor that made the comment.

              
      

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

              
      
  
Listing expected Submission Attachments
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments**

You can retrieve the list of expected Submission attachments at this route, along with a boolean flag indicating whether the server actually has a copy of the expected file or not. If the server has a file, you can then append its filename to the request URL to download only that file (see below).

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "file1.jpg",
              "exists": true
            },
            {
              "name": "file2.jpg",
              "exists": false
            },
            {
              "name": "file3.jpg",
              "exists": true
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Downloading an Attachment
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

The ``Content-Type``\  and ``Content-Disposition``\  will be set appropriately based on the file itself when requesting an attachment file download.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)\n"

    .. tab-item:: Schema

      **The ``Content-Type``\  and ``Content-Disposition``\  will be set appropriately based on the file itself when requesting an attachment file download.**

      .. list-table::
        :class: schema-table-wrap

        * - 


              

    
              
      

  **HTTP Status: 403**

  Content Type: {the MIME type of the attachment file itself}

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

              
      
  
Uploading an Attachment
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

*(introduced: version 0.4)*\ 

To upload a binary to an expected file slot, ``POST``\  the binary to its endpoint. Supply a ``Content-Type``\  MIME-type header if you have one.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
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
                  
                    None

              
      

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

              
      
  
Clearing a Submission Attachment
-----------------------------------------------------------------------------------------------------------------------

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

*(introduced: version 0.4)*\ 

Because Submission Attachments are completely determined by the XML data of the submission itself, there is no direct way to entirely remove a Submission Attachment entry from the list, only to clear its uploaded content. Thus, when you issue a ``DELETE``\  to the attachment's endpoint, that is what happens.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
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
                  
                    None

              
      

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

              
      
  
Listing Versions
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions**

This will return all submission metadata for every version of this submission, in descending creation order.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``submitter``\  data object alongside the ``submitterId``\  Actor ID reference.

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
      * - instanceId


        - string
        
          The `instanceId` of the initially submitted version. Please see the notes at the top of this documentation section for more information.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true,
              "submitter": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "formVersion": "1.0"
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Getting Version Details
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}**

Returns metadata about a particular version of the submission. As with the normal submission endpoint, you'll only get metadata in JSON out of this route. If you want to retrieve the XML, `add ``.xml``\  </reference/submissions/submission-versions/getting-version-xml>`__.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to return a ``submitter``\  data object alongside the ``submitterId``\  Actor ID reference.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          The `instanceId` of the particular version of this submission in question.

          Example: ``uuid:b1628661-65ed-4cab-8e30-19c17fef2de0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "instanceName": "village third house",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "current": true,
            "submitter": {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            },
            "formVersion": "1.0"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                * - instanceName


                  - string
                  
                    The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the ``Submission``\  version.

                * - current


                  - boolean
                  
                    Whether the version is current or not.

                * - submitter


                  - object
                  
                    The full details of the ``Actor``\  that submitted this version of the ``Submission``\ .


                      
                    .. collapse:: expand

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
                            
                              None

                          * - type


                            - string
                            
                              the Type of this Actor; typically this will be ``user``\ .

                          * - updatedAt


                            - string
                            
                              ISO date format

                          * - deletedAt


                            - string
                            
                              ISO date format

                     
                * - formVersion


                  - string
                  
                    The version of the form the submission version was created against. Only returned with specific Submission Version requests.

              
      

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

              
      
  
Getting Version XML
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}.xml**

Returns the XML of a particular version of the submission.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          The `instanceId` of the particular version of this submission in question.

          Example: ``uuid:b1628661-65ed-4cab-8e30-19c17fef2de0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <data id="simple">
            <orx:meta><orx:instanceID>uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44</orx:instanceID></orx:meta>
            <name>Alice</name>
            <age>32</age>
          </data>
          

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


              

    
              
      
  
Listing Version expected Attachments
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}/attachments**

You can retrieve the list of expected Submission attachments for the given version at this route, along with a boolean flag indicating whether the server actually has a copy of the expected file or not. If the server has a file, you can then append its filename to the request URL to download only that file (see below).

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          The `instanceId` of the particular version of this submission in question.

          Example: ``uuid:b1628661-65ed-4cab-8e30-19c17fef2de0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "file1.jpg",
              "exists": true
            },
            {
              "name": "file2.jpg",
              "exists": false
            },
            {
              "name": "file3.jpg",
              "exists": true
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Downloading a Version&#x27;s Attachment
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}/attachments/{filename}**

It is important to note that this endpoint returns whatever is *currently*\  uploaded against the *particular version*\  of the *Submission*\ . It will not track overwritten attachments.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          The `instanceId` of the particular version of this submission in question.

          Example: ``uuid:b1628661-65ed-4cab-8e30-19c17fef2de0``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)\n"

    .. tab-item:: Schema

      **It is important to note that this endpoint returns whatever is *currently*\  uploaded against the *particular version*\  of the *Submission*\ . It will not track overwritten attachments.**

      .. list-table::
        :class: schema-table-wrap

        * - 


              

    
              
      

  **HTTP Status: 403**

  Content Type: {the MIME type of the attachment file itself}

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

              
      
  
Getting changes between Versions
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/diffs**

This returns the changes, or edits, between different versions of a Submission. These changes are returned in an object that is indexed by the ``instanceId``\  that uniquely identifies that version. Between two submissions, there is an array of objects representing how each field changed. This change object contains the old and new values, as well as the path of that changed node in the Submission XML. These changes reflect the updated ``instanceID``\  and ``deprecatedID``\  fields as well as the edited value.

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
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {}
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Listing all Submissions on a Draft Form
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions**

Identical to `the non-Draft version </reference/submissions/submissions/listing-all-submissions-on-a-form>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `id` of this form as given in its XForms XML definition

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "reviewState": "approved",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "updatedAt": "2018-03-21T12:45:02.312Z",
              "currentVersion": {
                "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
                "instanceName": "village third house",
                "submitterId": 23,
                "deviceId": "imei:123456",
                "userAgent": "Enketo/3.0.4",
                "createdAt": "2018-01-19T23:58:03.395Z",
                "current": true
              },
              "submitter": {
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

              
      
  
Creating a Submission
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions**

Identical to `the non-Draft version </reference/submissions/submissions/creating-a-submission>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
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
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
              
      

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Exporting Form Submissions to CSV
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions.csv.zip**

Identical to `the non-Draft version </reference/submissions/submissions/exporting-form-submissions-to-csv>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Exporting Form Submissions to CSV via POST
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions.csv.zip**

Identical to `the non-Draft version </reference/submissions/submissions/exporting-form-submissions-to-csv-via-post>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``

  
.. dropdown:: Response

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
                  
                    None

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Listing Encryption Keys
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/keys**

Identical to `the non-Draft version </reference/submissions/submissions/listing-encryption-keys>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
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
            {}
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Getting Submission details
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}**

Identical to `the non-Draft version </reference/submissions/submissions/getting-submission-metadata>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
            "submitterId": 23,
            "deviceId": "imei:123456",
            "userAgent": "Enketo/3.0.4",
            "reviewState": "approved",
            "createdAt": "2018-01-19T23:58:03.395Z",
            "updatedAt": "2018-03-21T12:45:02.312Z",
            "currentVersion": {
              "instanceId": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
              "instanceName": "village third house",
              "submitterId": 23,
              "deviceId": "imei:123456",
              "userAgent": "Enketo/3.0.4",
              "createdAt": "2018-01-19T23:58:03.395Z",
              "current": true
            },
            "submitter": {
              "createdAt": "2018-04-18T23:19:14.802Z",
              "displayName": "My Display Name",
              "id": 115,
              "type": "user",
              "updatedAt": "2018-04-18T23:42:11.406Z",
              "deletedAt": "2018-04-18T23:42:11.406Z"
            }
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    The ``instanceId``\  of the ``Submission``\ , given by the Submission XML.

                * - submitterId


                  - number
                  
                    The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that originally submitted this ``Submission``\ .

                * - deviceId


                  - string
                  
                    The self-identified ``deviceId``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``deviceId``\  will be returned here.

                * - userAgent


                  - string
                  
                    The self-identified ``userAgent``\  of the device that collected the data, sent by it upon submission to the server. The initial submission ``userAgent``\  will be returned here.

                * - reviewState


                  - string
                  
                    The current review state of the submission.

                * - createdAt


                  - string
                  
                    ISO date format. The time that the server received the Submission.

                * - updatedAt


                  - string
                  
                    ISO date format. ``null``\  when the Submission is first created, then updated when the Submission's XML data or metadata is updated.

                * - currentVersion


                  - object
                  
                    The current version of the ``Submission``\ .


                      
                    .. collapse:: expand

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              The ``instanceId``\  of the ``Submission``\  version, given by the Submission XML.

                          * - instanceName


                            - string
                            
                              The ``instanceName``\ , if any, given by the Submission XML in the metadata section.

                          * - submitterId


                            - number
                            
                              The ID of the ``Actor``\  (``App User``\ , ``User``\ , or ``Public Link``\ ) that submitted this ``Submission``\  version.

                          * - deviceId


                            - string
                            
                              The self-identified ``deviceId``\  of the device that submitted the ``Submission``\  version.

                          * - userAgent


                            - string
                            
                              The self-identified ``userAgent``\  of the device that submitted the ``Submission``\  version.

                          * - createdAt


                            - string
                            
                              ISO date format. The time that the server received the ``Submission``\  version.

                          * - current


                            - boolean
                            
                              Whether the version is current or not.

                     
                * - submitter


                  - object
                  
                    The full details of the ``Actor``\  that submitted this ``Submission``\ .


                      
                    .. collapse:: expand

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
                            
                              None

                          * - type


                            - string
                            
                              the Type of this Actor; typically this will be ``user``\ .

                          * - updatedAt


                            - string
                            
                              ISO date format

                          * - deletedAt


                            - string
                            
                              ISO date format

                     
              
      

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

              
      
  
Retrieving Submission XML
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}.xml**

Identical to `the non-Draft version </reference/submissions/submissions/retrieving-submission-xml>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <data id="simple">
            <orx:meta><orx:instanceID>uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44</orx:instanceID></orx:meta>
            <name>Alice</name>
            <age>32</age>
          </data>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
Listing expected Submission Attachments
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments**

Identical to `the non-Draft version </reference/submissions/attachments/listing-expected-submission-attachments>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "name": "file1.jpg",
              "exists": true
            },
            {
              "name": "file2.jpg",
              "exists": false
            },
            {
              "name": "file3.jpg",
              "exists": true
            }
          ]

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - array


    

              
      

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

              
      
  
Downloading an Attachment
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

Identical to `the non-Draft version </reference/submissions/attachments/downloading-an-attachment>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: {the MIME type of the attachment file itself}

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          "(binary data)\n"

    .. tab-item:: Schema

      **Identical to `the non-Draft version &lt;/reference/submissions/attachments/downloading-an-attachment&gt;`__ of this endpoint.**

      .. list-table::
        :class: schema-table-wrap

        * - 


              

    
              
      

  **HTTP Status: 403**

  Content Type: {the MIME type of the attachment file itself}

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

              
      
  
Uploading an Attachment
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

Identical to `the non-Draft version </reference/submissions/attachments/uploading-an-attachment>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
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
                  
                    None

              
      

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

              
      
  
Clearing a Submission Attachment
-----------------------------------------------------------------------------------------------------------------------

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

Identical to `the non-Draft version </reference/submissions/attachments/clearing-a-submission-attachment>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          The name of the file as given by the Attachments listing resource.

          Example: ``file1.jpg``

  
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
                  
                    None

              
      

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

              
      
  
