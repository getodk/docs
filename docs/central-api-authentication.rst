.. auto generated file - DO NOT MODIFY 

Authentication
=======================================================================================================================

.. raw:: html
  
  <p>In ODK Central, the server thinks about identity and permissioning in terms of one core concept: the <code>Actor</code>. No matter how you authenticate with the API, you are doing so as an Actor of some kind or another, and when permissions are assigned and checked, they are done against the authenticated Actor.</p><p>In practice, there are two types of Actors available in the system today:</p><ul><li><p><code>User</code>s are accounts used by the staff members who manage the server and the data collection campaigns. They each have a set of rights assigned to them via Roles and Assignments. They are the only account types that have passwords associated with them. They also always have an email address. Users can authenticate using <strong>Session Bearer Tokens</strong> or using <strong>HTTPS Basic</strong> authentication.</p></li><li><p><code>App User</code>s are only allowed to access the OpenRosa parts of the API: in essence, they are allowed to list forms, download form definitions, and create new submissions against those forms. They can only authenticate using <strong>App User URL</strong>s.</p></li></ul><p>Next, you will find documentation on each of the three authentication methods described above. It is best not to present multiple credentials. If you do, the first <em>presented</em> scheme out of <code>/key</code> token, Bearer, Basic, then Cookie will be used for the request. If the multiple schemes are sent at once, and the first matching scheme fails, the request will be immediately rejected.</p><p><strong>Note:</strong> If Single Sign-on with Open ID Connect is enabled on the ODK Central, you can neither use HTTP Basic Authentication nor login with <code>POST /v1/session</code> endpoint.</p>


Session Authentication
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>This is the authentication method used by the ODK Central Frontend packaged with Central Backend. Only <code>User</code>s can authenticate this way. It consists mostly of two steps:</p><ol><li><strong>Logging in</strong>: presenting an Email Address and a Password for verification, after which a new <code>Session</code> is created. Associated with the Session is an expiration and a bearer token. Sessions expire 24 hours after they are created.</li><li><strong>Using the session</strong>: each request to the API needs a header attached to it: <code>Authorization: Bearer {token}</code>. This authenticates that particular request as belonging to the Session we created by logging in.</li></ol><p>You might notice that Step 2 greatly resembles how OAuth 2.0 works. This was an intentional first step towards OAuth support, and should make the forward migration of your code easier down the road.</p>

Logging in
^^^^^^^^^^^^^^^^^^^^

**POST /v1/sessions**

.. raw:: html

  <p>In order to log a <code>User</code> in to a new <code>Session</code>, you must provide their credentials, in JSON format.</p><p>For security reasons, the only possible results are success or failure. No detail is provided upon failure.</p><p>Successful responses will come with an HTTP-Only, Secure-Only cookie. This cookie is primarily meant for use by the Central frontend, and we do not recommend relying upon it. It will only work on <code>GET</code> requests, and it will only work over HTTPS.</p>

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "email": "my.email.address@getodk.org",
            "password": "my.super.secure.password"
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
                
                
                * - email


                  - string
                  
                    .. raw:: html

                      <p>The <code>User</code>'s full email address.</p>

                    Example: ``my.email.address@getodk.org``
                * - password


                  - string
                  
                    .. raw:: html

                      <p>The <code>User</code>'s password.</p>

                    Example: ``my.super.secure.password``
              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "createdAt": "2018-04-18T03:04:51.695Z",
            "expiresAt": "2018-04-19T03:04:51.695Z",
            "token": "lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7"
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

                * - expiresAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                * - token


                  - string
                  
                    .. raw:: html

                      <p>The bearer token associated with the session. It consists only of URL-safe characters, so it should never need any escaping.</p>

              
      

  **HTTP Status: 401**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "401.2",
            "message": "Could not authenticate with the provided credentials."
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

                    Example: ``401.2``
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Could not authenticate with the provided credentials.``
              
      
Using the session
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/example1**

.. raw:: html

  <p>Once you have logged in, to use your session token to authenticate with any action, supply it in a request header <code>Authorization</code> with a value of <code>Bearer {token}</code>, as seen here.</p><p><em>(There is not really anything at <code>/v1/example1</code>; this section only demonstrates how generally to use Session Bearer Token Authentication.)</em></p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - Authorization

          *(header)*

        - string
        
          .. raw:: html

            Bearer encoding of the credentials

          Example: ``Bearer lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7``

  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Success``
              
      
Logging out / Revoking an App User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/sessions/{token}**

.. raw:: html

  <p>Logging out is not strictly necessary for Web Users; all sessions expire 24 hours after they are created. But it can be a good idea, in case someone else manages to steal your token. It is also the way Public Link and App User access are revoked. To do so, issue a <code>DELETE</code> request to that token resource.</p><p><strong>Revoking an App User</strong></p><p>The token associated with a App User is actually just its Session Token. As a result, although a App User Token can uniquely be used as a URL prefix as described here, the session associated with it can be revoked in exactly the same way a session is logged out, by issuing a <code>DELETE</code> request to its Session resource.</p><p>Note, however, that a App User cannot revoke itself; a <code>User</code> must perform this action.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          .. raw:: html

            The session bearer token, obtained at login time.

          Example: ``lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7``

  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

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
              
      
Logging out current session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/sessions/current**

.. raw:: html

  <p>This endpoint causes the current session to log itself out. Logging out is not strictly necessary for Web Users; all sessions expire 24 hours after they are created. But it can be a good idea, in case someone else manages to steal your token.</p><p>Only the session that was used to authenticate the request is logged out. If the Actor associated with the session has other sessions as well, those are not logged out.</p>

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

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
              
      

HTTPS Basic Authentication
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>Standard HTTP Basic Authentication is allowed, but <strong>strongly discouraged</strong>. This is because the server must verify your password with every single request, which is very slow to compute: typically, this will add hundreds of milliseconds to each request. For some one-off tasks and in cases where there is no other choice, it is reasonable to choose Basic authentication, but wherever possible we strongly encourage the use of any other authentication method.</p><p>In addition, because credentials are sent in plaintext as part of the request, <strong>the server will only accept Basic auth over HTTPS</strong>. If your ODK Central server is set up over plain HTTP, it will not accept Basic auth.</p>

Using Basic Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/example2**

.. raw:: html

  <p>To use HTTPS Basic Authentication, attach an <code>Authorization</code> header formatted so:</p><p><code>Authorization: Basic bXkuZW1haWwuYWRkcmVzc0BvcGVuZGF0YWtpdC5vcmc6bXkucGFzc3dvcmQ=</code></p><p>As given by <a href="https://en.wikipedia.org/wiki/Basic_access_authentication">the standard</a>, the text following the <code>Basic</code> marker here is a base64 encoding of the credentials, provided in the form <code>email:password</code> (in this example <code>my.email.address@getodk.org:my.password</code>).</p><p>Unlike the standard, we do not require the client to first send an unauthenticated request and retry the request only after receiving a <code>WWW-Authenticate</code> response, and in fact we will never send the <code>WWW-Authenticate</code> header. This is mostly because, as noted above, we generally discourage the use of this authentication method, and would rather not advertise its use openly. As a result, if you wish to use Basic Authentication, directly supply the header on any request that needs it.</p><p><em>(There is not really anything at <code>/v1/example2</code>; this section only demonstrates how generally to use Basic Authentication.)</em></p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - Authorization

          *(header)*

        - string
        
          .. raw:: html

            Base64 encoding of the credentials

          Example: ``Basic bXkuZW1haWwuYWRkcmVzc0BvcGVuZGF0YWtpdC5vcmc6bXkucGFzc3dvcmQ=``

  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Success``
              
      

App User Authentication
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>App Users are only allowed to list and download forms, and upload new submissions to those forms. Primarily, this is to allow clients like ODK Collect to use the OpenRosa API (<code>/formList</code> and <code>/submission</code>), but any action in this API reference falling into those categories will be allowed.</p><p>Rvoking an App User is same as deleting session token. You can do this by calling <a href="/central-api-authentication/#logging-out-revoking-an-app-user">DELETE /sessions/{appUser}</a>.</p>

Using App User Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/key/{appUser}/example3**

.. raw:: html

  <p>To use App User Authentication, first obtain a App User, typically by using the configuration panel in the user interface, or else by using the <a href="/central-api-accounts-and-users/#app-users">App User API Resource</a>. Once you have the token, you can apply it to any eligible action by prefixing the URL with <code>/key/{appUser}</code> as follows:</p><p><code>/v1/key/!Ms7V3$Zdnd63j5HFacIPFEvFAuwNqTUZW$AsVOmaQFf$vIC!F8dJjdgiDnJXXOt/example/request/path</code></p><p><em>(There is not really anything at <code>/v1/example3</code>; this section only demonstrates how generally to use App User Authentication.)</em></p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - appUser


        - string
        
          .. raw:: html

            The App User token. As with Session Bearer tokens, these tokens only contain URL-safe characters, so no escaping is required.

          Example: ``!Ms7V3$Zdnd63j5HFacIPFEvFAuwNqTUZW$AsVOmaQFf$vIC!F8dJjdgiDnJXXOt``

  
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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Success``
              
      

