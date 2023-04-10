.. auto generated file - DO NOT MODIFY

Authentication
=======================================================================================================================

In ODK Central, the server thinks about identity and permissioning in terms of one core concept: the ``Actor``\ . No matter how you authenticate with the API, you are doing so as an Actor of some kind or another, and when permissions are assigned and checked, they are done against the authenticated Actor.

In practice, there are two types of Actors available in the system today:

* ``User``\ s are accounts used by the staff members who manage the server and the data collection campaigns. They each have a set of rights assigned to them via Roles and Assignments. They are the only account types that have passwords associated with them. They also always have an email address. Users can authenticate using **Session Bearer Tokens**\  or using **HTTPS Basic**\  authentication.

* ``App User``\ s are only allowed to access the OpenRosa parts of the API: in essence, they are allowed to list forms, download form definitions, and create new submissions against those forms. They can only authenticate using **App User URL**\ s.

In a future version of the API, programmatic consumers will be more directly supported as their own Actor type, which can be granted limited permissions and can authenticate over **OAuth 2.0**\ .

Next, you will find documentation on each of the three authentication methods described above. It is best not to present multiple credentials. If you do, the first *presented*\  scheme out of ``/key``\  token, Bearer, Basic, then Cookie will be used for the request. If the multiple schemes are sent at once, and the first matching scheme fails, the request will be immediately rejected.

Logging in
-----------------------------------------------------------------------------------------------------------------------

**POST /v1/sessions**

In order to log a ``User``\  in to a new ``Session``\ , you must provide their credentials, in JSON format.

For security reasons, the only possible results are success or failure. No detail is provided upon failure.

Successful responses will come with an HTTP-Only, Secure-Only cookie. This cookie is primarily meant for use by the Central frontend, and we do not recommend relying upon it. It will only work on ``GET``\  requests, and it will only work over HTTPS.

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "email": "pencil",
            "password": "pencil"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - email


                  - string
                  
                    The ``User``\ 's full email address.

                * - password


                  - string
                  
                    The ``User``\ 's password.

              
  
  
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - createdAt


                  - string
                  
                    ISO date format

                * - expiresAt


                  - string
                  
                    ISO date format

                * - token


                  - string
                  
                    The bearer token associated with the session. It consists only of URL-safe characters, so it should never need any escaping.

              
      

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

              
      
  
Using Basic Authentication
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/example**

To use HTTPS Basic Authentication, attach an ``Authorization``\  header formatted so:

``Authorization: Basic bXkuZW1haWwuYWRkcmVzc0BvcGVuZGF0YWtpdC5vcmc6bXkucGFzc3dvcmQ=``\ 

As given by `the standard <https://en.wikipedia.org/wiki/Basic*access*\ authentication>`__, the text following the ``Basic``\  marker here is a base64 encoding of the credentials, provided in the form ``email:password``\  (in this example ``my.email.address@getodk.org:my.password``\ ).

Unlike the standard, we do not require the client to first send an unauthenticated request and retry the request only after receiving a ``WWW-Authenticate``\  response, and in fact we will never send the ``WWW-Authenticate``\  header. This is mostly because, as noted above, we generally discourage the use of this authentication method, and would rather not advertise its use openly. As a result, if you wish to use Basic Authentication, directly supply the header on any request that needs it.

*(There is not really anything at ``/v1/example``\ ; this section only demonstrates how generally to use Basic Authentication.)*\ 

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - Authorization

          *(header)*

        - string
        
          Base64 encoding of the credentials

          Example: ``Basic bXkuZW1haWwuYWRkcmVzc0BvcGVuZGF0YWtpdC5vcmc6bXkucGFzc3dvcmQ=``

  
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

              
      
  
Revoking an App User
-----------------------------------------------------------------------------------------------------------------------

**DELETE /v1/sessions/{token}**

The token associated with a App User is actually just its Session Token. As a result, although a App User Token can uniquely be used as a URL prefix as described here, the session associated with it can be revoked in exactly the same way a session is logged out, by issuing a ``DELETE``\  request to its Session resource.

Note, however, that a App User cannot revoke itself; a ``User``\  must perform this action.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - token


        - string
        
          The session bearer token, obtained at login time.

          Example: ``lSpAIeksRu1CNZs7!qjAot2T17dPzkrw9B4iTtpj7OoIJBmXvnHM8z8Ka4QPEjR7``

  
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

              
      
  
Using App User Authentication
-----------------------------------------------------------------------------------------------------------------------

**GET /v1/key/{appUser}/example**

To use App User Authentication, first obtain a App User, typically by using the configuration panel in the user interface, or else by using the `App User API Resource </reference/accounts-and-users/app-users>`__. Once you have the token, you can apply it to any eligible action by prefixing the URL with ``/key/{appUser}``\  as follows:

``/v1/key/!Ms7V3$Zdnd63j5HFacIPFEvFAuwNqTUZW$AsVOmaQFf$vIC!F8dJjdgiDnJXXOt/example/request/path``\ 

*(There is not really anything at ``/v1/example``\ ; this section only demonstrates how generally to use App User Authentication.)*\ 

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - appUser


        - string
        
          The App User token. As with Session Bearer tokens, these tokens only contain URL-safe characters, so no escaping is required.

          Example: ``!Ms7V3$Zdnd63j5HFacIPFEvFAuwNqTUZW$AsVOmaQFf$vIC!F8dJjdgiDnJXXOt``

  
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

              
      
  
