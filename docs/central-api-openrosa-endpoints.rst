.. auto generated file - DO NOT MODIFY

OpenRosa Endpoints
=======================================================================================================================

`OpenRosa <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI>`__ is an API standard which accompanies the ODK XForms XML standard, allowing compliant servers and clients to use a common protocol to communicate ``Form``\ s and ``Submission``\ s to each other. When survey clients like ODK Collect and Enketo submit Submission data to a Form, this is the API they use.

ODK Central is *not*\  a fully compliant OpenRosa server. OpenRosa requires compliance with five major components:

1. `**Metadata Schema**\  <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaMetaDataSchema>`__, which defines a standard way to include metadata like the survey device ID and survey duration with a Submission. ODK Central will accept and return this data, but does nothing special with anything besides the ``instanceId``\  at this time.

2. `**HTTP Request API**\  <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaRequest>`__, which defines a set of requirements every OpenRosa request and response must follow. ODK Central is fully compliant with this component, except that we do *not*\  require the ``Date``\  header.

3. `**Form Submission API**\  <https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI>`__, which defines how Submissions are submitted to the server. ODK Central is fully compliant with this component.

4. `**Authentication API**\  <https://bitbucket.org/javarosa/javarosa/wiki/AuthenticationAPI>`__, which defines how users authenticate with the server. ODK Central provides `three authentication methods </reference/authentication>`__. One of these is HTTPS Basic Authentication, which is recommended by the OpenRosa specification. However, because `we do not follow the try/retry pattern </reference/authentication/https-basic-authentication/using-basic-authentication>`__ required by the OpenRosa and the RFC specification, ODK Central is *not compliant*\  with this component. Our recommendation generally is to use `App User Authentication </reference/authentication/app-user-authentication>`__ when submitting data from survey clients.

5. `**Form Discovery (Listing) API**\  <https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI>`__, which returns a listing of Forms available for survey clients to download and submit to. At this time, ODK Central is *partially compliant*\  with this component: the server will return a correctly formatted ``formList``\  response, but it does not currently handle the optional filter parameters.

In practical usage, ODK survey clients like Collect will interact with Central in three places:

* The OpenRosa Form Listing API, `documented below </reference/openrosa-endpoints/openrosa-form-listing-api>`__, lists the Forms the client can retrieve.

* The `Form XML download </reference/forms/individual-form/retrieving-form-xml>`__ endpoint, a part of the standard REST API for Forms, is linked in the Form Listing response and allows clients to then download the ODK XForms XML for each form.

* The OpenRosa Submission API, `documented below </reference/openrosa-endpoints/openrosa-form-submission-api>`__, allows survey clients to submit new Submissions to any Form.

The Form Listing and Submission APIs are partitioned by Project, and their URLs are nested under the Project in question as a result. When you List or Submit, you will only be able to get forms from and submit submissions to that particular Project at a time.

Where the **HTTP Request API**\  OpenRosa standards specification requires two headers for any request, Central requires only one:

* ``X-OpenRosa-Version``\  **must**\  be set to exactly ``1.0``\  or the request will be rejected.

* But Central does not require a ``Date``\  header field. You may set it if you wish, but it will have no effect on Central.

OpenRosa Form Listing API
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/formList**

This is the mostly standards-compliant implementation of the `OpenRosa Form Discovery (Listing) API <https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI>`__. We will not attempt to redocument the standard here.

The following aspects of the standard are *not*\  supported by ODK Central:

* The ``deviceID``\  may be provided with the request, but it will be ignored.

* The ``Accept-Language``\  header may be provided with the request, but it will be ignored.

* The ``?formID=``\  querystring parameter is not supported and will be ignored.

* The ``?verbose``\  querystring parameter is not supported and will be ignored.

* The ``?listAllVersions``\  querystring is not supported and will be ignored. Central does not yet support multiple active versions of the same Form.

* No ``<xforms-group/>``\  will ever be provided, as Central does not yet support this feature.

By default, the given ``<name/>``\  in the Form Listing response is the friendly name associated with the ``Form``\  (``<title>``\  in the XML and ``name``\  on the API resource). If no such value can be found, then the ``xmlFormId``\  will be given as the ``<name>``\  instead.

A ``<manifestUrl/>``\  property will be given per ``<xform>``\  if and only if that form is expected to have media or data file attachments associated with it, based on its XForms definition. It will appear even if no attachments have actually been uploaded to the server to fulfill those expectations.

This resource always requires authentication. If a valid Actor is authenticated at all, a form list will always be returned, filtered by what that Actor is allowed to access.

If you haven't already, please take a look at the **HTTP Request API**\  notes above on the required OpenRosa headers.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <?xml version="1.0" encoding="UTF-8"?>
          <xforms xmlns="http://openrosa.org/xforms/xformsList">
            <xform>
              <formID>basic</formID>
              <name>basic</name>
              <version></version>
              <hash>md5:a64817a5688dd7c17563e32d4eb1cab2</hash>
              <downloadUrl>https://your.odk.server/v1/projects/7/forms/basic.xml</downloadUrl>
              <manifestUrl>https://your.odk.server/v1/projects/7/forms/basic/manifest</manifestUrl>
            </xform>
            <xform>
              <formID>simple</formID>
              <name>Simple</name>
              <version></version>
              <hash>md5:</hash>
              <downloadUrl>https://your.odk.server/v1/projects/7/forms/simple.xml</downloadUrl>
            </xform>
          </xforms>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
OpenRosa Form Submission API
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/projects/{projectId}/submission**

This is the fully standards-compliant implementation of the `OpenRosa Form Submission API <https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI>`__. We will not attempt to redocument the submission part of the standard here, but please read further for information about *updating*\  submissions with new data.

Some things to understand when using this API for any reason:

* ODK Central will always provide an ``X-OpenRosa-Accept-Content-Length``\  of 100 megabytes. In reality, this number depends on how the server has been deployed. The default Docker-based installation, for example, is limited to 100MB at the nginx layer.

* The ``xml*submission*\ file``\  may have a Content Type of either ``text/xml``\  *or*\  ``application/xml``\ .

* Central supports the ``HEAD``\  request preflighting recommended by the specification, but does not require it. Because our supported authentication methods do not follow the try/retry pattern, only preflight your request if you want to read the ``X-OpenRosa-Accept-Content-Length``\  header or are concerned about the other issues listed in the standards document, like proxies.

* As stated in the standards document, it is possible to submit multimedia attachments with the ``Submission``\  across multiple ``POST``\  requests to this API. *However*\ , we impose the additional restriction that the Submission XML (``xml*submission*\ file``\ ) *may not change*\  between requests. If Central sees a Submission with an ``instanceId``\  it already knows about but the XML has changed in any way, it will respond with a ``409 Conflict``\  error and reject the submission.

* Central will never return a ``202``\  in any response from this API.

* If you haven't already, please take a look at the **HTTP Request API**\  notes above on the required OpenRosa headers.

You can use this endpoint to submit *updates*\  to an existing submission. To do so, provide additionally a ```deprecatedID``\  metadata XML node <https://getodk.github.io/xforms-spec/#metadata>`__ with the ``instanceID``\  of the submission you are replacing. Some things to understand when submitting updates:

* The new XML entirely replaces the old XML. No merging will be performed. So your new submission must contain exactly the current data.

* If the ``deprecatedID``\  you provide has already been deprecated, your request will be rejected with a ``409 Conflict``\  and a useful error message.

* If the submission you are deprecating had media files uploaded for it, any of those that are still relevant will be carried over to the new version by filename reference. Any files you provide will overwrite these carryovers.

* Just as with initial submission, you can send multiple requests to this endpoint to submit additional media files if they do not comfortably fit in a single request. Also the same as initial submission, you'll need to provide exactly the same XML to make this happen. For updates, this will need to include the ``deprecatedID``\ .

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 201**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="">full submission upload was successful!</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 400**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">A resource already exists with a attachment file name of attachment1.jpg.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">The authenticated actor does not have rights to perform that action.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 409**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">A submission already exists with this ID, but with different XML. Resubmissions to attach additional multimedia must resubmit an identical xml_submission_file.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
OpenRosa Form Manifest API
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/manifest**

*(introduced: version 0.2)*\ 

This is the fully standards-compliant implementation of the `OpenRosa Form Manifest API <https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI#!the-manifest-document>`__. We will not attempt to redocument the standard here.

A Manifest document is available at this resource path for any form in the system. However:

* A link to this document will not be given in the `Form Listing API </reference/openrosa-endpoints/openrosa-form-listing-api>`__ unless we expect the form to have media or data file attachments based on the XForms definition of the form.

* The Manifest will only output information for files the server actually has in its possession. Any missing expected files will be omitted, as we cannot provide a ``hash``\  or ``downloadUrl``\  for them.

* For Attachments that are linked to a Dataset, the value of ``hash``\  is calculated using the MD5 of the last updated timestamp of the Dataset, instead of the content of the Dataset.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <?xml version="1.0" encoding="UTF-8"?>
          <manifest xmlns="http://openrosa.org/xforms/xformsManifest">
            <mediaFile>
              <filename>question1.jpg</filename>
              <hash>md5:a64817a5688dd7c17563e32d4eb1cab2</hash>
              <downloadUrl>https://your.odk.server/v1/projects/7/forms/basic/attachments/question1.jpg</downloadUrl>
            </mediaFile>
            <mediaFile>
              <filename>question2.jpg</filename>
              <hash>md5:a6fdc426037143cf71cced68e2532e3c</hash>
              <downloadUrl>https://your.odk.server/v1/projects/7/forms/basic/attachments/question2.jpg</downloadUrl>
            </mediaFile>
          </manifest>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">The authenticated actor does not have rights to perform that action.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
OpenRosa Form Listing API
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/formList**

Identical to the `non-Draft version </reference/openrosa-endpoints/openrosa-form-listing-api/openrosa-form-listing-api>`__, but will only list the Draft Form to be tested.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <?xml version="1.0" encoding="UTF-8"?>
          <xforms xmlns="http://openrosa.org/xforms/xformsList">
            <xform>
              <formID>basic</formID>
              <name>basic</name>
              <version></version>
              <hash>md5:a64817a5688dd7c17563e32d4eb1cab2</hash>
              <downloadUrl>https://your.odk.server/v1/test/IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP/projects/7/forms/basic/draft.xml</downloadUrl>
              <manifestUrl>https://your.odk.server/v1/test/IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP/projects/7/forms/basic/draft/manifest</manifestUrl>
            </xform>
          </xforms>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
OpenRosa Form Submission API
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/submission**

Identical to the `non-Draft version </reference/openrosa-endpoints/openrosa-form-submission-api/openrosa-form-submission-api>`__, but will only submit to (and allow submissions to) the Draft Form to be tested.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 201**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="">full submission upload was successful!</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 400**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">A resource already exists with a attachment file name of attachment1.jpg.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">The authenticated actor does not have rights to perform that action.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 409**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">A submission already exists with this ID, but with different XML. Resubmissions to attach additional multimedia must resubmit an identical xml_submission_file.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
OpenRosa Form Manifest API
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/manifest**

Identical to the `non-Draft version </reference/openrosa-endpoints/openrosa-form-manifest-api/openrosa-form-manifest-api>`__.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          e.g. 1.0

          Example: ``1.0``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <?xml version="1.0" encoding="UTF-8"?>
          <manifest xmlns="http://openrosa.org/xforms/xformsManifest">
            <mediaFile>
              <filename>question.jpg</filename>
              <hash>md5:a64817a5688dd7c17563e32d4eb1cab2</hash>
              <downloadUrl>https://your.odk.server/v1/test/IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP/projects/7/forms/basic/draft/attachments/question.jpg</downloadUrl>
            </mediaFile>
          </manifest>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

  **HTTP Status: 403**

  Content Type: text/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="0">
            <message nature="error">The authenticated actor does not have rights to perform that action.</message>
          </OpenRosaResponse>
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
  
Downloading a Form Attachment
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/attachments/{filename}**

Identical to the `non-Draft version </reference/forms/individual-form/downloading-a-form-attachment>`__.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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

      **Identical to the `non-Draft version &lt;/reference/forms/individual-form/downloading-a-form-attachment&gt;`__.**

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

              
      
  
