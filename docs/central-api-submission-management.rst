.. auto generated file - DO NOT MODIFY 

Submission Management
=======================================================================================================================

.. raw:: html
  
  <p><code>Submission</code>s are filled-out forms (also called <code>Instance</code>s in some other ODK documentation). Each is associated with a particular Form (and in many cases with a particular <em>version</em> of a Form), and is also created out of a standard XML format based on the Form itself. Submissions can be sent with many accompanying multimedia attachments, such as photos taken in the course of the survey. Once created, the Submissions themselves as well as their attachments can be retrieved through this API.</p><p>These subsections cover only the modern RESTful API resources involving Submissions. For documentation on the OpenRosa submission endpoint (which can be used to submit Submissions), or the OData endpoint (which can be used to retrieve and query submission data), see those sections below.</p><blockquote><p>Like Forms, Submissions can have versions. Each Form has an overall <code>xmlFormId</code> that represents the Form as a whole, and each version has a <code>version</code> that identifies that particular version. Often, when fetching data by the <code>xmlFormId</code> alone, information from the latest Form version is included in the response.</p></blockquote><blockquote><p>Similarly with Submissions, the <code>instanceId</code> each Submission is first submitted with will always represent that Submission as a whole. Each version of the Submission, though, has its own <code>instanceId</code>. Sometimes, but not very often, when getting information about the Submission by only its overall <code>instanceId</code>, information from the latest Submission version is included in the response.</p></blockquote>


Submissions
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><code>Submission</code>s are available as a subresource under <code>Form</code>s. So, for instance, <code>/v1/projects/1/forms/myForm/submissions</code> refers only to the Submissions that have been submitted to the Form <code>myForm</code>.</p><p>Once created (which, like with Forms, is done by way of their XML data rather than a JSON description), it is possible to retrieve and export Submissions in a number of ways, as well as to access the multimedia <code>Attachment</code>s associated with each Submission.</p>

Listing all Submissions on a Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions**

.. raw:: html

  <p>Currently, there are no paging or filtering options, so listing <code>Submission</code>s will get you every Submission in the system, every time.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>submitter</code> data object alongside the <code>submitterId</code> Actor ID reference.</p>

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                    Example: ``Enketo/3.0.4``
                * - reviewState


                  - object
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - null


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                    Example: ``2018-03-21T12:45:02.312Z``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                              Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                              Example: ``village third house``
                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                              Example: ``23``
                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``imei:123456``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                              Example: ``2018-01-19T23:58:03.395Z``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``true``
                     

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                    Example: ``Enketo/3.0.4``
                * - reviewState


                  - object
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - null


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                    Example: ``2018-03-21T12:45:02.312Z``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                              Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                              Example: ``village third house``
                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                              Example: ``23``
                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``imei:123456``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                              Example: ``2018-01-19T23:58:03.395Z``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``true``
                     
                * - submitter


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
              
      
Creating a Submission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions**

.. raw:: html

  <p>To create a Submission by REST rather than over the <a href="/central-api-openrosa-endpoints/#openrosa-form-submission-api">OpenRosa interface</a>, you may <code>POST</code> the Submission XML to this endpoint. The request must have an XML <code>Content-Type</code> (<code>text/xml</code> or <code>application/xml</code>).</p><p>Unlike the OpenRosa Form Submission API, this interface does <em>not</em> accept Submission attachments upon Submission creation. Instead, the server will determine which attachments are expected based on the Submission XML, and you may use the endpoints found in the following section to add the appropriate attachments and check the attachment status and content.</p><p>If the XML is unparseable or there is some other input problem with your data, you will get a <code>400</code> error in response. If a submission already exists with the given <code>instanceId</code>, you will get a <code>409</code> error in response.</p>

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
      * - deviceID

          *(query)*

        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

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

              
      
Getting Submission metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

.. raw:: html

  <p>Like how <code>Form</code>s are addressed by their XML <code>formId</code>, individual <code>Submission</code>s are addressed in the URL by their <code>instanceId</code>.</p><p>As of version 1.4, a <code>deviceId</code> and <code>userAgent</code> will also be returned with each submission. The client device may transmit these extra metadata when the data is submitted. If it does, those fields will be recognized and returned here for reference. Here, only the initial <code>deviceId</code> and <code>userAgent</code> will be reported. If you wish to see these metadata for any submission edits, including the most recent edit, you will need to <a href="/central-api-submission-management/#listing-versions">list the versions</a>.</p><p>As of version 2023.2, this API returns <code>currentVersion</code> that contains metadata of the most recent version of the Submission.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>submitter</code> data object alongside the <code>submitterId</code> Actor ID reference.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``none``
                     
                * - submitter


                  - object
                  
                    .. raw:: html

                      <p>The full details of the <code>Actor</code> that submitted this <code>Submission</code>.</p>


                      
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

              
      
Updating Submission Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PUT /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

.. raw:: html

  <p><em>(introduced: version 1.2)</em></p><p>You can use this endpoint to submit <em>updates</em> to an existing submission.</p><p>The <code>instanceId</code> that is submitted with the initial version of the submission is used permanently to reference that submission logically, which is to say the initial submission and all its subsequent versions. Each subsequent version will also provide its own <code>instanceId</code>. This <code>instanceId</code> becomes that particular version's identifier.</p><p>To perform an update, you need to provide in the submission XML an additional <a href="https://getodk.github.io/xforms-spec/#metadata"><code>deprecatedID</code> metadata node</a> with the <code>instanceID</code> of the particular and current submission version you are replacing. If the <code>deprecatedID</code> you give is anything other than the identifier of the current version of the submission at the time the server receives it, you will get a <code>409 Conflict</code> back. You can get the current version <code>instanceID</code> by getting the <a href="/central-api-submission-management/#retrieving-submission-xml">current XML of the submission</a>.</p><p>The XML data you send will <em>replace</em> the existing data entirely. All of the data must be present in the updated XML.</p><p>When you create a new submission version, any uploaded media files attached to the current version that match expected attachment names in the new version will automatically be copied over to the new version. So if you don't make any changes to media files, there is no need to resubmit them. You can get information about all the submission versions <a href="central-api-submission-management/#submission-versions">from the <code>/versions</code> subresource</a>.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

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

              
      
Updating Submission metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}**

.. raw:: html

  <p>Currently, the only updatable <em>metadata</em> on a Submission is its <code>reviewState</code>. To update the submission <em>data</em> itself, please see <a href="/central-api-submission-management/#updating-submission-data">Updating Submission data</a>.</p><p>Starting with Version 2022.3, changing the <code>reviewState</code> of a Submission to <code>approved</code> can create an Entity in a Dataset if the corresponding Form maps Dataset Properties to Form Fields. If an Entity is created successfully then an <code>entity.create</code> event is logged in Audit logs, else <code>entity.create.error</code> is logged.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

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

              
      
Retrieving Submission XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}.xml**

.. raw:: html

  <p>To get only the XML of the <code>Submission</code> rather than all of the details with the XML as one of many properties, just add <code>.xml</code> to the end of the request URL.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/edit**

.. raw:: html

  <p><em>(introduced: version 1.2)</em></p><p>This endpoint redirects the user to an Enketo-powered page that allows the user to interactively edit the submission. Once the user is satisfied, they can perform the submission update directly through the Enketo interface.</p><p>The Enketo instance is already hosted inside of ODK Central. There is no reason to create or use a separate Enketo installation.</p><p>This endpoint is intended for use by the Central administration frontend and will not work without it. In particular, the user must be logged into the Central administration site for Enketo editing to work. If there is no Central authentication cookie present when Enketo is loaded, the browser will then be redirected by Enketo to a Central login page.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

              
      
Exporting Form Submissions to CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv.zip**

.. raw:: html

  <p>To export all the <code>Submission</code> data associated with a <code>Form</code>, just add <code>.csv.zip</code> to the end of the listing URL. The response will be a ZIP file containing one or more CSV files, as well as all multimedia attachments associated with the included Submissions.</p><p>You can exclude the media attachments from the ZIP file by specifying <code>?attachments=false</code>.</p><p>If <a href="/central-api-encryption">Project Managed Encryption</a> is being used, additional querystring parameters may be provided in the format <code>{keyId}={passphrase}</code> for any number of keys (eg <code>1=secret&amp;4=password</code>). This will decrypt any records encrypted under those managed keys. Submissions encrypted under self-supplied keys will not be decrypted. <strong>Note</strong>: if you are building a browser-based application, please consider the alternative <code>POST</code> endpoint, described in the following section.</p><p>If a passphrase is supplied but is incorrect, the entire request will fail. If a passphrase is not supplied but encrypted records exist, only the metadata for those records will be returned, and they will have a <code>status</code> of <code>not decrypted</code>.</p><p>If you are running an unsecured (<code>HTTP</code> rather than <code>HTTPS</code>) Central server, it is not a good idea to export data this way as your passphrase and the decrypted data will be sent plaintext over the network.</p><p>You can use an <a href="/central-api-odata-endpoints/#data-document">OData-style <code>$filter</code> query</a> to filter the submissions that will appear in the ZIP file. This is a bit awkward, since this endpoint has nothing to do with OData, but since we already must recognize the OData syntax, it is less strange overall for now not to invent a whole other one here. Only a subset of the <code>$filter</code> features are available; please see the linked section for more information.</p>

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
      * - attachments

          *(query)*

        - boolean
        
          .. raw:: html

            Set to false to exclude media attachments from the export.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the given OData query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - groupPaths

          *(query)*

        - boolean
        
          .. raw:: html

            Set to false to remove group path prefixes from field header names (eg `instanceID` instead of `meta-instanceID`). This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``true``
      * - deletedFields

          *(query)*

        - boolean
        
          .. raw:: html

            Set to true to restore all fields previously deleted from this form for this export. All known fields and data for those fields will be merged and exported.

          Example: ``false``
      * - splitSelectMultiples

          *(query)*

        - boolean
        
          .. raw:: html

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

              
      
Exporting Form Submissions to CSV via POST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv.zip**

.. raw:: html

  <p>This non-REST-compliant endpoint is provided for use with <a href="/central-api-encryption">Project Managed Encryption</a>. In every respect, it behaves identically to the <code>GET</code> endpoint described in the previous section, except that it works over <code>POST</code>. This is necessary because for browser-based applications, it is a dangerous idea to simply link the user to <code>/submissions.csv.zip?2=supersecretpassphrase</code> because the browser will remember this route in its history and thus the passphrase will become exposed. This is especially dangerous as there are techniques for quickly learning browser-visited URLs of any arbitrary domain.</p><p>You can exclude the media attachments from the ZIP file by specifying <code>?attachments=false</code>.</p><p>And so, for this <code>POST</code> version of the Submission CSV export endpoint, the passphrases may be provided via <code>POST</code> body rather than querystring. Two formats are supported: form URL encoding (<code>application/x-www-form-urlencoded</code>) and JSON. In either case, the keys should be the <code>keyId</code>s and the values should be the <code>passphrase</code>s, as with the <code>GET</code> version above.</p>

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
      * - attachments

          *(query)*

        - boolean
        
          .. raw:: html

            Set to false to exclude media attachments from the export.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the given OData query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - groupPaths

          *(query)*

        - boolean
        
          .. raw:: html

            Set to false to remove group path prefixes from field header names (eg `instanceID` instead of `meta-instanceID`). This behavior mimics a similar behavior in ODK Briefcase.

          Example: ``true``
      * - deletedFields

          *(query)*

        - boolean
        
          .. raw:: html

            Set to true to restore all fields previously deleted from this form for this export. All known fields and data for those fields will be merged and exported.

          Example: ``false``
      * - splitSelectMultiples

          *(query)*

        - boolean
        
          .. raw:: html

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

              
      
Exporting Root Data to Plain CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv**

.. raw:: html

  <p><em>(introduced: version 1.1)</em></p><p>The above submission endpoints will give you a ZIP file with the submission data in it. This is necessary to provide all the possible related repeat table files, as well as the media files associated with the submissions. But ZIP files can be difficult to work with, and many Forms have no repeats nor media attachments.</p><p>To export <em>just</em> the root table (no repeat data nor media files), you can call this endpoint instead, which will directly give you CSV data.</p><p>Please see the <a href="/central-api-submission-management/#exporting-form-submissions-to-csv">above endpoint</a> for notes on dealing with Managed Encryption.</p>

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
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the given OData query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

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

              
      
Exporting Root Data to Plain CSV via POST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions.csv**

.. raw:: html

  <p><em>(introduced: version 1.1)</em></p><p>This endpoint is useful only for Forms under Project Managed Encryption.</p><p>As with <code>GET</code> to <code>.csv</code> just above, this endpoint will only return CSV text data, rather than a ZIP file containing ore or more files. Please see that endpoint for further explanation.</p><p>As with <a href="/central-api-submission-management/#exporting-form-submissions-to-csv-via-post"><code>POST</code> to <code>.csv.zip</code></a> it allows secure submission of decryption passkeys. Please see that endpoint for more information on how to do this.</p>

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
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the given OData query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

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

              
      
Retrieving Audit Logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/audits**

.. raw:: html

  <p><em>(introduced: version 1.2)</em></p><p>You can retrieve all <a href="/central-api-system-endpoints/#server-audit-logs">Server Audit Logs</a> relating to a submission. They will be returned most recent first.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally expand the <code>actorId</code> into full <code>actor</code> details, and <code>acteeId</code> into full <code>actee</code> details. The <code>actor</code> will always be an Actor, and the <code>actee</code> will be the Form this Submission is a part of.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

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
                     
                * - actee


                  - object
                  
                    .. raw:: html

                      <p>The details of the actee given by <code>acteeId</code>. Depending on the action type, this could be a number of object types, including an <code>Actor</code>, a <code>Project</code>, or a <code>Form</code>.</p>


              
      

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
              
      
Listing Encryption Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/keys**

.. raw:: html

  <p>This endpoint provides a listing of all known encryption keys needed to decrypt all Submissions for a given Form. It will return at least the <code>base64RsaPublicKey</code> property (as <code>public</code>) of all known versions of the form that have submissions against them. If managed keys are being used and a <code>hint</code> was provided, that will be returned as well.</p>

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
              "id": 1,
              "public": "bcFeKDF3Sg8W91Uf5uxaIlsuhzmjbgUnIyiLzIjrx4CAaf9Y9LG7TAu6wKPqfbH6ZAkJTFSfjLNovbKhpOQcmO5VZGGay6yvXrX1TFW6C6RLITy74erxfUAStdtpP4nraCYqQYqn5zD4/1OmgweJt5vzGXW2ch7lrROEQhXB9lK+bjEeWx8TFW/+6ha/oRLnl6a2RBRL6mhwy3PoByNTKndB2MP4TygCJ/Ini4ivk74iSqVnoeuNJR/xUcU+kaIpZEIjxpAS2VECJU9fZvS5Gt84e5wl/t7bUKu+dlh/cUgHfk6+6bwzqGQYOe5A==",
              "managed": true,
              "hint": "it was a secret"
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
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Key.</p>

                    Example: ``1``
                * - public


                  - string
                  
                    .. raw:: html

                      <p>The base64-encoded public key, with PEM envelope removed.</p>

                    Example: ``bcFeKDF3Sg8W91Uf5uxaIlM2uK0cUN9tBSGoASbC4LeIPqx65+6zmjbgUnIyiLzIjrx4CAaf9Y9LG7TAu6wKPqfbH6ZAkJTFSfjLNovbKhpOQcmO5VZGGay6yvXrX1TFW6C6RLITy74erxfUAStdtpP4nraCYqQYqn5zD4/1OmgweJt5vzGXW2ch7lrROEQhXB9lK+bjEeWx8TFW/+6ha/oRLnl6a2RBRL6mhwy3PoByNTKndB2MP4TygCJ/Ini4ivk74iSqVnoeuNJR/xUcU+kaIpZEIjxpAS2VECJU9fZvS5Gt84e5wl/t7bUKu+dlh/cUgHfk6+6bwzqGQYOe5A==``
                * - managed


                  - boolean
                  
                    .. raw:: html

                      <p>If true, this is a key generated by Project managed encryption. If not, this key is self-supplied.</p>

                    Example: ``true``
                * - hint


                  - string
                  
                    .. raw:: html

                      <p>The hint, if given, related to a managed encryption key.</p>

                    Example: ``it was a secret``

              
      

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
              
      
Listing Submitters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/submitters**

.. raw:: html

  <p>This endpoint provides a listing of all known submitting actors to a given Form. Each Actor that has submitted to the given Form will be returned once.</p>

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
              
      

Comments
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.2)</em></p><p>This API is likely to change in the future. In version 1.2 we have added comments to submissions, so changes and problems with the data can be discussed. It's very likely we will want comments in more places in the future, and at that time a more complete comments API will be introduced, and this current one may be changed or deprecated entirely.</p><p>Currently, it is not possible to get a specific comment's details, or to edit or delete a comment once it has been made.</p>

Listing Comments
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/comments**

.. raw:: html

  <p>Comments have only a <code>body</code> comment text and an <code>actor</code> that made the comment.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>actor</code> data object alongside the <code>actorId</code> Actor ID reference.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    .. raw:: html

                      <p>The text of the comment.</p>

                    Example: ``this is my comment``
                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor that made the comment.</p>

                    Example: ``42``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    .. raw:: html

                      <p>The text of the comment.</p>

                    Example: ``this is my comment``
                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor that made the comment.</p>

                    Example: ``42``
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
              
      
Posting Comments
^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/comments**

.. raw:: html

  <p>Currently, the only accepted data is <code>body</code>, which contains the body of the comment to be made.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    .. raw:: html

                      <p>The text of the comment.</p>

              
  
  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - body


                  - string
                  
                    .. raw:: html

                      <p>The text of the comment.</p>

                * - actorId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the Actor that made the comment.</p>

              
      

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

              
      

Attachments
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>When a <code>Submission</code> is created, either over the OpenRosa or the REST interface, its XML data is analyzed to determine which file attachments it references: these may be photos or video taken as part of the survey, or an audit/timing log, among other things. Each reference is an expected attachment, and these expectations are recorded permanently alongside the Submission.</p><p>With this subresource, you can list the expected attachments, see whether the server actually has a copy or not, and download, upload, re-upload, or clear binary data for any particular attachment.</p>

Listing expected Submission Attachments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments**

.. raw:: html

  <p>You can retrieve the list of expected Submission attachments at this route, along with a boolean flag indicating whether the server actually has a copy of the expected file or not. If the server has a file, you can then append its filename to the request URL to download only that file (see below).</p>

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
      * - instanceId


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the Submission XML.</p>

                    Example: ``myfile.mp3``
                * - exists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``

              
      

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
              
      
Downloading an Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p>The <code>Content-Type</code> and <code>Content-Disposition</code> will be set appropriately based on the file itself when requesting an attachment file download.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <p>The <code>Content-Type</code> and <code>Content-Disposition</code> will be set appropriately based on the file itself when requesting an attachment file download.</p>

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

              
      
Uploading an Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p><em>(introduced: version 0.4)</em></p><p>To upload a binary to an expected file slot, <code>POST</code> the binary to its endpoint. Supply a <code>Content-Type</code> MIME-type header if you have one.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

              
      
Clearing a Submission Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p><em>(introduced: version 0.4)</em></p><p>Because Submission Attachments are completely determined by the XML data of the submission itself, there is no direct way to entirely remove a Submission Attachment entry from the list, only to clear its uploaded content. Thus, when you issue a <code>DELETE</code> to the attachment's endpoint, that is what happens.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

              
      

Submission Versions
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.2)</em></p><p>The <code>instanceId</code> that is submitted with the initial version of the submission is used permanently to reference that submission logically, which is to say the initial submission and all its subsequent versions. Each subsequent version will also provide its own <code>instanceId</code>. This <code>instanceId</code> becomes that particular version's identifier.</p><p>So if you submit a submission with <code>&lt;orx:instanceID&gt;one&lt;/orx:instanceID&gt;</code> and then update it, deprecating <code>one</code> for version <code>two</code>, then the full route for version <code>one</code> is <code>/v1/projects/…/forms/…/submissions/one/versions/one</code>, and for <code>two</code> it is <code>/v1/projects/…/forms/…/submissions/one/versions/two</code>.</p><p>As of version 1.4, a <code>deviceId</code> and <code>userAgent</code> will also be returned with each submission. For each submission of a version, the submitting client device may transmit these extra metadata. If it does, those fields will be recognized and returned here for reference.</p>

Listing Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions**

.. raw:: html

  <p>This will return all submission metadata for every version of this submission, in descending creation order.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>submitter</code> data object alongside the <code>submitterId</code> Actor ID reference.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the initially submitted version. Please see the notes at the top of this documentation section for more information.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - instanceName


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                    Example: ``village third house``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                    Example: ``Enketo/3.0.4``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - current


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the version is current or not.</p>

                    Example: ``true``

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - instanceName


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                    Example: ``village third house``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                    Example: ``Enketo/3.0.4``
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - current


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the version is current or not.</p>

                    Example: ``true``
                * - submitter


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
                     
                * - formVersion


                  - string
                  
                    .. raw:: html

                      <p>The version of the form the submission version was created against. Only returned with specific Submission Version requests.</p>

                    Example: ``1.0``

              
      

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
              
      
Getting Version Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}**

.. raw:: html

  <p>Returns metadata about a particular version of the submission. As with the normal submission endpoint, you'll only get metadata in JSON out of this route. If you want to retrieve the XML, <a href="/central-api-submission-management/#getting-version-xml">add <code>.xml</code></a>.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to return a <code>submitter</code> data object alongside the <code>submitterId</code> Actor ID reference.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                * - instanceName


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                * - current


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the version is current or not.</p>

                    Example: ``none``
                * - submitter


                  - object
                  
                    .. raw:: html

                      <p>The full details of the <code>Actor</code> that submitted this version of the <code>Submission</code>.</p>


                      
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

                     
                * - formVersion


                  - string
                  
                    .. raw:: html

                      <p>The version of the form the submission version was created against. Only returned with specific Submission Version requests.</p>

              
      

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

              
      
Getting Version XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}.xml**

.. raw:: html

  <p>Returns the XML of a particular version of the submission.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}/attachments**

.. raw:: html

  <p>You can retrieve the list of expected Submission attachments for the given version at this route, along with a boolean flag indicating whether the server actually has a copy of the expected file or not. If the server has a file, you can then append its filename to the request URL to download only that file (see below).</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the Submission XML.</p>

                    Example: ``myfile.mp3``
                * - exists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``

              
      

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

              
      
Downloading a Version&#x27;s Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/versions/{versionId}/attachments/{filename}**

.. raw:: html

  <p>It is important to note that this endpoint returns whatever is <em>currently</em> uploaded against the <em>particular version</em> of the <em>Submission</em>. It will not track overwritten attachments.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - versionId


        - string
        
          .. raw:: html

            The `instanceId` of the particular version of this submission in question.

          Example: ``uuid:b1628661-65ed-4cab-8e30-19c17fef2de0``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <p>It is important to note that this endpoint returns whatever is <em>currently</em> uploaded against the <em>particular version</em> of the <em>Submission</em>. It will not track overwritten attachments.</p>

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/submissions/{instanceId}/diffs**

.. raw:: html

  <p>This returns the changes, or edits, between different versions of a Submission. These changes are returned in an object that is indexed by the <code>instanceId</code> that uniquely identifies that version. Between two submissions, there is an array of objects representing how each field changed. This change object contains the old and new values, as well as the path of that changed node in the Submission XML. These changes reflect the updated <code>instanceID</code> and <code>deprecatedID</code> fields as well as the edited value.</p>

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
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "two": [
              {
                "new": "Donna",
                "old": "Dana",
                "path": [
                  "name"
                ]
              },
              {
                "new": "55",
                "old": "44",
                "path": [
                  "age"
                ]
              },
              {
                "new": "two",
                "old": "one",
                "path": [
                  "meta",
                  "instanceID"
                ]
              },
              {
                "new": "one",
                "old": null,
                "path": [
                  "meta",
                  "deprecatedID"
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

                                <p>The new value of this node, which can either be a simple string, or JSON string representing a larger structural change to the Submission XML. It can also be null if this field no longer exists in the Submission.</p>

                          * - old


                            - string
                            
                              .. raw:: html

                                <p>The old value of this node, with similar properties to <code>new</code>. It can be null if this field did not exist previously.</p>

                          * - path


                            - array
                            
                              .. raw:: html

                                <p>An array representing the path (XPath) in the Submission tree for this node. It does not include the outermost path <code>data</code>. For elements that are part of repeat groups, the path element is the node name and the index (starting at 0), e.g. ['child', 2] is the third child.</p>

                              Example: ``null``
                              
    

                               
                     

              
      

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
              
      

Draft Submissions
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>All <a href="/central-api-form-management/#draft-form">Draft Forms</a> feature a <code>/submissions</code> subresource (<code>/draft/submissions</code>), which is identical to the same subresource on the form itself. These submissions exist only as long as the Draft Form does: they are removed if the Draft Form is published, and they are abandoned if the Draft Form is deleted or overwritten.</p><p>Here we list all those resources again just for completeness.</p>

Listing all Submissions on a Draft Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#listing-all-submissions-on-a-form">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `id` of this form as given in its XForms XML definition

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                    Example: ``Enketo/3.0.4``
                * - reviewState


                  - object
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - null


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                    Example: ``2018-03-21T12:45:02.312Z``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                              Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                              Example: ``village third house``
                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                              Example: ``23``
                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``imei:123456``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                              Example: ``2018-01-19T23:58:03.395Z``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``true``
                     

              
      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                    Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                    Example: ``23``
                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                    Example: ``imei:123456``
                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                    Example: ``Enketo/3.0.4``
                * - reviewState


                  - object
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - null


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                    Example: ``2018-01-19T23:58:03.395Z``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                    Example: ``2018-03-21T12:45:02.312Z``
                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <span></span>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                              Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                              Example: ``village third house``
                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                              Example: ``23``
                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``imei:123456``
                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                              Example: ``Enketo/3.0.4``
                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                              Example: ``2018-01-19T23:58:03.395Z``
                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``true``
                     
                * - submitter


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
              
      
Creating a Submission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#creating-a-submission">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

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

              
      
Exporting Form Submissions to CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions.csv.zip**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#exporting-form-submissions-to-csv">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

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

              
      
Exporting Form Submissions to CSV via POST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions.csv.zip**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#exporting-form-submissions-to-csv-via-post">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

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

              
      
Listing Encryption Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/keys**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#listing-encryption-keys">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
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
              "id": 1,
              "public": "bcFeKDF3Sg8W91Uf5uxaIlsuhzmjbgUnIyiLzIjrx4CAaf9Y9LG7TAu6wKPqfbH6ZAkJTFSfjLNovbKhpOQcmO5VZGGay6yvXrX1TFW6C6RLITy74erxfUAStdtpP4nraCYqQYqn5zD4/1OmgweJt5vzGXW2ch7lrROEQhXB9lK+bjEeWx8TFW/+6ha/oRLnl6a2RBRL6mhwy3PoByNTKndB2MP4TygCJ/Ini4ivk74iSqVnoeuNJR/xUcU+kaIpZEIjxpAS2VECJU9fZvS5Gt84e5wl/t7bUKu+dlh/cUgHfk6+6bwzqGQYOe5A==",
              "managed": true,
              "hint": "it was a secret"
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
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Key.</p>

                    Example: ``1``
                * - public


                  - string
                  
                    .. raw:: html

                      <p>The base64-encoded public key, with PEM envelope removed.</p>

                    Example: ``bcFeKDF3Sg8W91Uf5uxaIlM2uK0cUN9tBSGoASbC4LeIPqx65+6zmjbgUnIyiLzIjrx4CAaf9Y9LG7TAu6wKPqfbH6ZAkJTFSfjLNovbKhpOQcmO5VZGGay6yvXrX1TFW6C6RLITy74erxfUAStdtpP4nraCYqQYqn5zD4/1OmgweJt5vzGXW2ch7lrROEQhXB9lK+bjEeWx8TFW/+6ha/oRLnl6a2RBRL6mhwy3PoByNTKndB2MP4TygCJ/Ini4ivk74iSqVnoeuNJR/xUcU+kaIpZEIjxpAS2VECJU9fZvS5Gt84e5wl/t7bUKu+dlh/cUgHfk6+6bwzqGQYOe5A==``
                * - managed


                  - boolean
                  
                    .. raw:: html

                      <p>If true, this is a key generated by Project managed encryption. If not, this key is self-supplied.</p>

                    Example: ``true``
                * - hint


                  - string
                  
                    .. raw:: html

                      <p>The hint, if given, related to a managed encryption key.</p>

                    Example: ``it was a secret``

              
      

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
              
      
Getting Submission details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#getting-submission-metadata">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - instanceId


                  - string
                  
                    .. raw:: html

                      <p>The <code>instanceId</code> of the <code>Submission</code>, given by the Submission XML.</p>

                * - submitterId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that originally submitted this <code>Submission</code>.</p>

                * - deviceId


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>deviceId</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>deviceId</code> will be returned here.</p>

                * - userAgent


                  - string
                  
                    .. raw:: html

                      <p>The self-identified <code>userAgent</code> of the device that collected the data, sent by it upon submission to the server. The initial submission <code>userAgent</code> will be returned here.</p>

                * - reviewState


                  - enum
                  
                    .. raw:: html

                      <p>The current review state of the submission.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - None


                            - string
                            

                          * - edited


                            - string
                            

                          * - hasIssues


                            - string
                            

                          * - rejected


                            - string
                            

                          * - approved


                            - string
                            

                          * - approved


                            - string
                            

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The time that the server received the Submission.</p>

                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. <code>null</code> when the Submission is first created, then updated when the Submission's XML data or metadata is updated.</p>

                * - currentVersion


                  - object
                  
                    .. raw:: html

                      <p>The current version of the <code>Submission</code>.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - instanceId


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceId</code> of the <code>Submission</code> version, given by the Submission XML.</p>

                          * - instanceName


                            - string
                            
                              .. raw:: html

                                <p>The <code>instanceName</code>, if any, given by the Submission XML in the metadata section.</p>

                          * - submitterId


                            - number
                            
                              .. raw:: html

                                <p>The ID of the <code>Actor</code> (<code>App User</code>, <code>User</code>, or <code>Public Link</code>) that submitted this <code>Submission</code> version.</p>

                          * - deviceId


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>deviceId</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - userAgent


                            - string
                            
                              .. raw:: html

                                <p>The self-identified <code>userAgent</code> of the device that submitted the <code>Submission</code> version.</p>

                          * - createdAt


                            - string
                            
                              .. raw:: html

                                <p>ISO date format. The time that the server received the <code>Submission</code> version.</p>

                          * - current


                            - boolean
                            
                              .. raw:: html

                                <p>Whether the version is current or not.</p>

                              Example: ``none``
                     
                * - submitter


                  - object
                  
                    .. raw:: html

                      <p>The full details of the <code>Actor</code> that submitted this <code>Submission</code>.</p>


                      
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

              
      
Retrieving Submission XML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}.xml**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#retrieving-submission-xml">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#listing-expected-submission-attachments">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

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

                      <p>The name of the file as specified in the Submission XML.</p>

                    Example: ``myfile.mp3``
                * - exists


                  - boolean
                  
                    .. raw:: html

                      <p>Whether the server has the file or not.</p>

                    Example: ``true``

              
      

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
              
      
Downloading an Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#downloading-an-attachment">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

      .. raw:: html

        <p>Identical to <a href="/central-api-submission-management/#downloading-an-attachment">the non-Draft version</a> of this endpoint.</p>

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

              
      
Uploading an Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#uploading-an-attachment">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

              
      
Clearing a Submission Attachment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/forms/{xmlFormId}/draft/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p>Identical to <a href="/central-api-submission-management/#clearing-a-submission-attachment">the non-Draft version</a> of this endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The `id` of the project this form belongs to.

          Example: ``1``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

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

              
      

