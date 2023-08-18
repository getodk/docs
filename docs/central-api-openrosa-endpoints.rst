.. auto generated file - DO NOT MODIFY 

OpenRosa Endpoints
=======================================================================================================================

.. raw:: html
  
  <p><a href="https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI">OpenRosa</a> is an API standard which accompanies the ODK XForms XML standard, allowing compliant servers and clients to use a common protocol to communicate <code>Form</code>s and <code>Submission</code>s to each other. When survey clients like ODK Collect and Enketo submit Submission data to a Form, this is the API they use.</p><p>ODK Central is <em>not</em> a fully compliant OpenRosa server. OpenRosa requires compliance with five major components:</p><ol><li><p><a href="https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaMetaDataSchema"><strong>Metadata Schema</strong></a>, which defines a standard way to include metadata like the survey device ID and survey duration with a Submission. ODK Central will accept and return this data, but does nothing special with anything besides the <code>instanceId</code> at this time.</p></li><li><p><a href="https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaRequest"><strong>HTTP Request API</strong></a>, which defines a set of requirements every OpenRosa request and response must follow. ODK Central is fully compliant with this component, except that we do <em>not</em> require the <code>Date</code> header.</p></li><li><p><a href="https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI"><strong>Form Submission API</strong></a>, which defines how Submissions are submitted to the server. ODK Central is fully compliant with this component.</p></li><li><p><a href="https://bitbucket.org/javarosa/javarosa/wiki/AuthenticationAPI"><strong>Authentication API</strong></a>, which defines how users authenticate with the server. ODK Central provides <a href="/central-api-authentication">three authentication methods</a>. One of these is HTTPS Basic Authentication, which is recommended by the OpenRosa specification. However, because <a href="/central-api-authentication/#using-basic-authentication">we do not follow the try/retry pattern</a> required by the OpenRosa and the RFC specification, ODK Central is <em>not compliant</em> with this component. Our recommendation generally is to use <a href="/central-api-authentication/#app-user-authentication">App User Authentication</a> when submitting data from survey clients.</p></li><li><p><a href="https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI"><strong>Form Discovery (Listing) API</strong></a>, which returns a listing of Forms available for survey clients to download and submit to. At this time, ODK Central is <em>partially compliant</em> with this component: the server will return a correctly formatted <code>formList</code> response, but it does not currently handle the optional filter parameters.</p></li></ol><p>In practical usage, ODK survey clients like Collect will interact with Central in three places:</p><ul><li><p>The OpenRosa Form Listing API, <a href="/central-api-openrosa-endpoints/#openrosa-form-listing-api">documented below</a>, lists the Forms the client can retrieve.</p></li><li><p>The <a href="/central-api-form-management/#retrieving-form-xml">Form XML download</a> endpoint, a part of the standard REST API for Forms, is linked in the Form Listing response and allows clients to then download the ODK XForms XML for each form.</p></li><li><p>The OpenRosa Submission API, <a href="/central-api-openrosa-endpoints/#openrosa-form-submission-api">documented below</a>, allows survey clients to submit new Submissions to any Form.</p></li></ul><p>The Form Listing and Submission APIs are partitioned by Project, and their URLs are nested under the Project in question as a result. When you List or Submit, you will only be able to get forms from and submit submissions to that particular Project at a time.</p><p>Where the <strong>HTTP Request API</strong> OpenRosa standards specification requires two headers for any request, Central requires only one:</p><ul><li><p><code>X-OpenRosa-Version</code> <strong>must</strong> be set to exactly <code>1.0</code> or the request will be rejected.</p></li><li><p>But Central does not require a <code>Date</code> header field. You may set it if you wish, but it will have no effect on Central.</p></li></ul>

OpenRosa Form Listing API
-----------------------------------

**GET /v1/projects/{projectId}/formList**

.. raw:: html

  <p>This is the mostly standards-compliant implementation of the <a href="https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI">OpenRosa Form Discovery (Listing) API</a>. We will not attempt to redocument the standard here.</p><p>The following aspects of the standard are <em>not</em> supported by ODK Central:</p><ul><li><p>The <code>deviceID</code> may be provided with the request, but it will be ignored.</p></li><li><p>The <code>Accept-Language</code> header may be provided with the request, but it will be ignored.</p></li><li><p>The <code>?formID=</code> querystring parameter is not supported and will be ignored.</p></li><li><p>The <code>?verbose</code> querystring parameter is not supported and will be ignored.</p></li><li><p>The <code>?listAllVersions</code> querystring is not supported and will be ignored. Central does not yet support multiple active versions of the same Form.</p></li><li><p>No <code>&lt;xforms-group/&gt;</code> will ever be provided, as Central does not yet support this feature.</p></li></ul><p>By default, the given <code>&lt;name/&gt;</code> in the Form Listing response is the friendly name associated with the <code>Form</code> (<code>&lt;title&gt;</code> in the XML and <code>name</code> on the API resource). If no such value can be found, then the <code>xmlFormId</code> will be given as the <code>&lt;name&gt;</code> instead.</p><p>A <code>&lt;manifestUrl/&gt;</code> property will be given per <code>&lt;xform&gt;</code> if and only if that form is expected to have media or data file attachments associated with it, based on its XForms definition. It will appear even if no attachments have actually been uploaded to the server to fulfill those expectations.</p><p>This resource always requires authentication. If a valid Actor is authenticated at all, a form list will always be returned, filtered by what that Actor is allowed to access.</p><p>If you haven't already, please take a look at the <strong>HTTP Request API</strong> notes above on the required OpenRosa headers.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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
--------------------------------------

**POST /v1/projects/{projectId}/submission**

.. raw:: html

  <p>This is the fully standards-compliant implementation of the <a href="https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI">OpenRosa Form Submission API</a>. We will not attempt to redocument the submission part of the standard here, but please read further for information about <em>updating</em> submissions with new data.</p><p>Some things to understand when using this API for any reason:</p><ul><li><p>ODK Central will always provide an <code>X-OpenRosa-Accept-Content-Length</code> of 100 megabytes. In reality, this number depends on how the server has been deployed. The default Docker-based installation, for example, is limited to 100MB at the nginx layer.</p></li><li><p>The <code>xml_submission_file</code> may have a Content Type of either <code>text/xml</code> <em>or</em> <code>application/xml</code>.</p></li><li><p>Central supports the <code>HEAD</code> request preflighting recommended by the specification, but does not require it. Because our supported authentication methods do not follow the try/retry pattern, only preflight your request if you want to read the <code>X-OpenRosa-Accept-Content-Length</code> header or are concerned about the other issues listed in the standards document, like proxies.</p></li><li><p>As stated in the standards document, it is possible to submit multimedia attachments with the <code>Submission</code> across multiple <code>POST</code> requests to this API. <em>However</em>, we impose the additional restriction that the Submission XML (<code>xml_submission_file</code>) <em>may not change</em> between requests. If Central sees a Submission with an <code>instanceId</code> it already knows about but the XML has changed in any way, it will respond with a <code>409 Conflict</code> error and reject the submission.</p></li><li><p>Central will never return a <code>202</code> in any response from this API.</p></li><li><p>If you haven't already, please take a look at the <strong>HTTP Request API</strong> notes above on the required OpenRosa headers.</p></li></ul><p>You can use this endpoint to submit <em>updates</em> to an existing submission. To do so, provide additionally a <a href="https://getodk.github.io/xforms-spec/#metadata"><code>deprecatedID</code> metadata XML node</a> with the <code>instanceID</code> of the submission you are replacing. Some things to understand when submitting updates:</p><ul><li><p>The new XML entirely replaces the old XML. No merging will be performed. So your new submission must contain exactly the current data.</p></li><li><p>If the <code>deprecatedID</code> you provide has already been deprecated, your request will be rejected with a <code>409 Conflict</code> and a useful error message.</p></li><li><p>If the submission you are deprecating had media files uploaded for it, any of those that are still relevant will be carried over to the new version by filename reference. Any files you provide will overwrite these carryovers.</p></li><li><p>Just as with initial submission, you can send multiple requests to this endpoint to submit additional media files if they do not comfortably fit in a single request. Also the same as initial submission, you'll need to provide exactly the same XML to make this happen. For updates, this will need to include the <code>deprecatedID</code>.</p></li></ul>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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
------------------------------------

**GET /v1/projects/{projectId}/forms/{xmlFormId}/manifest**

.. raw:: html

  <p><em>(introduced: version 0.2)</em></p><p>This is the fully standards-compliant implementation of the <a href="https://bitbucket.org/javarosa/javarosa/wiki/FormListAPI#!the-manifest-document">OpenRosa Form Manifest API</a>. We will not attempt to redocument the standard here.</p><p>A Manifest document is available at this resource path for any form in the system. However:</p><ul><li><p>A link to this document will not be given in the <a href="/central-api-openrosa-endpoints/#openrosa-form-listing-api">Form Listing API</a> unless we expect the form to have media or data file attachments based on the XForms definition of the form.</p></li><li><p>The Manifest will only output information for files the server actually has in its possession. Any missing expected files will be omitted, as we cannot provide a <code>hash</code> or <code>downloadUrl</code> for them.</p></li><li><p>For Attachments that are linked to a Dataset, the value of <code>hash</code> is calculated using the MD5 of the last updated timestamp of the Dataset, instead of the content of the Dataset.</p></li></ul>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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


              

    
              
      

Draft Testing Endpoints
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.8)</em></p><p>To facilitate testing, there is an alternative collection of OpenRosa endpoints that will give access to the draft version of a form and allow submitting test submissions to it. If you are using User or App User authentication, you can use the following resources without the <code>/test/{token}</code> prefix with your existing authentication.</p><p>Otherwise, and in particular if you plan to test your form in Collect or another OpenRosa-compliant client, you will likely want to use the <code>/test</code> Draft Token prefix. It functions similarly to the standard OpenRosa support, with App User authentication, but instead of a <code>/key</code> route prefix they feature a <code>/test</code> route prefix, and they point directly at each form (example: <code>/test/lSpA…EjR7/projects/1/forms/myform/draft</code>).</p><p>You can get the appropriate Draft Token for any given draft by <a href="/central-api-form-management/#getting-draft-form-details">requesting the Draft Form</a>.</p><p>The <code>/test</code> tokens are not actual App Users, and Central does not keep track of user identity when they are used.</p><p>With the <code>/test</code> prefix, the following resources are available:</p>

OpenRosa Form Listing API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/formList**

.. raw:: html

  <p>Identical to the <a href="/central-api-openrosa-endpoints/#openrosa-form-listing-api">non-Draft version</a>, but will only list the Draft Form to be tested.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          .. raw:: html

            The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/submission**

.. raw:: html

  <p>Identical to the <a href="/central-api-openrosa-endpoints/#openrosa-form-submission-api">non-Draft version</a>, but will only submit to (and allow submissions to) the Draft Form to be tested.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          .. raw:: html

            The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/draft/manifest**

.. raw:: html

  <p>Identical to the <a href="/central-api-openrosa-endpoints/#openrosa-form-manifest-api">non-Draft version</a>.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          .. raw:: html

            The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
      * - X-OpenRosa-Version

          *(header)*

        - string
        
          .. raw:: html

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/test/{token}/projects/{projectId}/forms/{xmlFormId}/attachments/{filename}**

.. raw:: html

  <p>Identical to the <a href="/central-api-form-management/#downloading-a-form-attachment">non-Draft version</a>.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          .. raw:: html

            The authentication Draft Token associated with the Draft Form in question.

          Example: ``IeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QP``
      * - projectId


        - number
        
          .. raw:: html

            The numeric ID of the Project

          Example: ``7``
      * - xmlFormId


        - string
        
          .. raw:: html

            The `xmlFormId` of the Form being referenced.

          Example: ``simple``
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

        <p>Identical to the <a href="/central-api-form-management/#downloading-a-form-attachment">non-Draft version</a>.</p>

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

              
      

