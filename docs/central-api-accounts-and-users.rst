.. auto generated file - DO NOT MODIFY 

Accounts and Users
=======================================================================================================================

Today, there are two types of accounts: ``Users``\ , which are the administrative accounts held by staff members managing the data collection process, and ``App Users``\ , which are restricted access keys granted per Form within a Project to data collection clients in the field. Although both of these entities are backed by ``Actor``\ s as we explain in the `Authentication section </central-api-authentication>`__ above, there is not yet any way to directly create or manipulate an Actor. Today, you can only create, manage, and delete Users and App Users.

Actors (and thus Users) may be granted rights via Roles. The ``/roles``\  Roles API is open for all to access, which describes all defined roles on the server. Getting information for an individual role from that same API will reveal which verbs are associated with each role: some role might allow only ``submission.create``\  and ``submission.update``\ , for example.

Right now, there are four predefined system roles: Administrator (``admin``\ ), Project Manager (``manager``\ ), Data Collector (``formfill``\ ), and App User (``app-user``\ ). Administrators are allowed to perform any action upon the server, while Project Managers are allowed to perform any action upon the projects they are assigned to manage.

Data Collectors can see all Forms in a Project and submit to them, but cannot see Submissions and cannot edit Form settings. Similarly, App Users are granted minimal rights: they can read Form data and create new Submissions on those Forms. While Data Collectors can perform these actions directly on the Central administration website by logging in, App Users can only do these things through Collect or a similar data collection client device.

The Roles API alone does not, however, tell you which Actors have been assigned with Roles upon which system objects. For that, you will need to consult the various Assignments resources. There are two, one under the API root (``/v1/assignments``\ ), which manages assignments to the entire system, and another nested under each Project (``/v1/projects/…/assignments``\ ) which manage assignments to that Project.


Users
-----------------------------------------------------------------------------------------------------------------------

Presently, it is possible to create and list ``User``\ s in the system, as well as to perform password reset operations. In future versions of this API it will be possible to manage existing user information and delete accounts as well.

Listing all Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users**

Currently, there are no paging or filtering options, so listing ``User``\ s will get you every User in the system, every time.

Optionally, a ``q``\  querystring parameter may be provided to filter the returned users by any given string. The search is performed via a `trigram similarity index <https://www.postgresql.org/docs/14/pgtrgm.html>`__ over both the Email and Display Name fields, and results are ordered by match score, best matches first. Note that short search terms (less than 4 or 5 characters) may not return any results. Try a longer search if nothing is appearing.

If a ``q``\  parameter is given, and it exactly matches an email address that exists in the system, that user's details will always be returned, even for actors who cannot ``user.list``\ . The request must still authenticate as a valid Actor. This allows non-Administrators to choose a user for an action (eg grant rights) without allowing full search.

Actors who cannot ``user.list``\  will always receive ``[]``\  with a ``200 OK``\  response.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - q

          *(query)*

        - string
        
          An optional search parameter.

          Example: ``alice``

  
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
              "email": "my.email.address@getodk.org"
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
                * - email


                  - string
                  
                    The email address of the user


              
      

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
                  
                    

              
      
Creating a new User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/users**

All that is required to create a new user is an email address. That email address will receive a message instructing the new user on how to claim their new account and set a password.

Optionally, a password may also be supplied as a part of this request. If it is, the account is immediately usable with the given credentials. However, an email will still be dispatched with claim instructions as above.

Users are not able to do anything upon creation besides log in and change their own profile information. To allow Users to perform useful actions, you will need to `assign them one or more Roles </central-api-accounts-and-users/#assignments>`__.

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "email": "my.email.address@getodk.org"
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
                  
                    The email address of the User account to be created.

                * - password


                  - string
                  
                    If provided, the User account will be created with this password. Otherwise, the user will still be able set their own password later.

              
  
  
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
            "email": "my.email.address@getodk.org"
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

                * - email


                  - string
                  
                    Only ``User``\ s have email addresses associated with them

              
      

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
                  
                    

              
      
Getting User details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users/{actorId}**

Typically, you supply the integer ID to get information about the user associated with that id.

It is also possible to supply the text ``current``\  instead of an integer ID; please see the following endpoint for documentation about this.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          Typically the integer ID of the `User`. For getting user details, you can also supply the text `current`, which will tell you about the currently authenticated user.

          Example: ``42``

  
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
            "email": "my.email.address@getodk.org"
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

                * - email


                  - string
                  
                    Only ``User``\ s have email addresses associated with them

              
      

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
                  
                    

              
      
Deleting a User
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/users/{actorId}**

Upon User deletion:

* The account will be removed,

* the user will be logged out of all existing sessions,

* and should the user attempt to reset their password, they will receive an email informing them that their account has been removed.

The User record will remain on file within the database, so that when for example information about the creator of a Form or Submission is requested, basic details are still available on file. A new User account may be created with the same email address as any deleted accounts.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          Typically the integer ID of the `User`. For getting user details, you can also supply the text `current`, which will tell you about the currently authenticated user.

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
                  
                    

              
      
Modifying a User
^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/users/{actorId}**

You can ``PATCH``\  JSON data to update User details. Not all user information is modifiable; right now, the following fields may be updated:

* ``displayName``\  sets the friendly display name the web interface uses to refer to the user.

* ``email``\  sets the email address associated with the account.

When user details are updated, the ``updatedAt``\  field will be automatically updated.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          The integer ID of the `User`.

          Example: ``42``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "displayName": "New Name",
            "email": "new.email.address@getodk.org"
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
                  
                    The friendly display name that should be associated with this User.

                * - email


                  - string
                  
                    The email address that should be associated with this User.

              
  
  
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
            "email": "my.email.address@getodk.org"
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

                * - email


                  - string
                  
                    Only ``User``\ s have email addresses associated with them

              
      

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
                  
                    

              
      
Getting authenticated User details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users/current**

Typically, you would get User details by the User's numeric Actor ID.

However, if you only have a Bearer token, for example, you don't have any information about the user attached to that session, including even the ID with which to get more information. So you can instead supply the text ``current``\  to get the user information associated with the authenticated session.

If you *do*\  use ``current``\ , you may request extended metadata. Supply an ``X-Extended-Metadata``\  header value of ``true``\  to additionally retrieve an array of strings of the ``verbs``\  the authenticated User/Actor is allowed to perform server-wide.

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

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
            "email": "my.email.address@getodk.org",
            "verbs": [
              "project.create",
              "project.update"
            ]
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

                * - email


                  - string
                  
                    Only ``User``\ s have email addresses associated with them

                * - verbs


                  - array
                  
                    The verbs the authenticated Actor is allowed to perform server-wide.

                    Example: ``null``
                    
    

                     
              
      

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
                  
                    

              
      
Directly updating a user password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PUT /v1/users/{actorId}/password**

To directly update a user password, you will need to reprove the user's intention by supplying the ``old``\  password alongside the ``new``\ . If you simply want to initiate an email-based password reset process, see the following endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          The integer ID of the `User`.

          Example: ``42``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "old": "old.password",
            "new": "new.password"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - old


                  - string
                  
                    The user's current password.

                * - new


                  - string
                  
                    The new password that the user wishes to set.

              
  
  
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
                  
                    

              
      
Initating a password reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/users/reset/initiate**

Anybody can initate a reset of any user's password. An email will be sent with instructions on how to complete the password reset; it contains a token that is required to complete the process.

The optional query parameter ``invalidate``\  may be set to ``true``\  to immediately invalidate the user's current password, regardless of whether they complete the reset process. This can be done if, for example, their password has been compromised. In order to do this, though, the request must be performed as an authenticated user with permission to do this. If invalidation is attempted without the proper permissions, the entire request will fail.

If the email address provided does not match any user in the system, that address will still be sent an email informing them of the attempt and that no account was found.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - invalidate

          *(query)*

        - boolean
        
          Specify `true` in order to immediately invalidate the user's present password.

          Example: ``true``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "email": "my.email.address@getodk.org"
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
                  
                    The email address of the User account whose password is to be reset.

              
  
  
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
                  
                    

              
      

App Users
-----------------------------------------------------------------------------------------------------------------------

App Users may only be created, fetched, and manipulated within the nested Projects subresource, as App Users themselves are limited to the Project in which they are created. Through the ``App User``\ s API, you can create, list, and delete the App Users of any given Project. Because they have extremely limited permissions, App Users cannot manage themselves; only ``User``\ s may access this API.

For more information about the ``/projects``\  containing resource, please see the following section.

Listing all App Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/app-users**

Currently, there are no paging or filtering options, so listing ``App User``\ s will get you every App User in the system, every time.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally retrieve the ``lastUsed``\  timestamp of each App User, as well as to retrieve the details of the ``Actor``\  the App User was ``createdBy``\ .

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; extended

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
              "projectId": 1,
              "createdBy": {
                "createdAt": "2018-04-18T23:19:14.802Z",
                "displayName": "My Display Name",
                "id": 115,
                "type": "user",
                "updatedAt": "2018-04-18T23:42:11.406Z",
                "deletedAt": "2018-04-18T23:42:11.406Z"
              },
              "lastUsed": "2018-04-14T08:34:21.633Z"
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
                  
                    If present, this is the Token that can be used to authenticate a request as this ``App User``\ . If not present, this ``App User``\ 's access has been revoked.

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - projectId


                  - number
                  
                    The ID of the ``Project``\  that this ``App User``\  is bound to.

                    Example: ``1``

              
      **Extended App Users**

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
                  
                    If present, this is the Token that can be used to authenticate a request as this ``App User``\ . If not present, this ``App User``\ 's access has been revoked.

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - projectId


                  - number
                  
                    The ID of the ``Project``\  that this ``App User``\  is bound to.

                    Example: ``1``
                * - createdBy


                  - object
                  
                    The ``Actor``\  that created this ``App User``\ 


                      
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
                     
                * - lastUsed


                  - string
                  
                    ISO date format. The last time this ``App User``\  was used to authenticate a request.

                    Example: ``2018-04-14 08:34:21.633000+00:00``

              
      

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
                  
                    

              
      
Creating a new App User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/app-users**

The only information required to create a new ``App User``\  is its ``displayName``\  (this is called "Nickname" in the administrative panel).

When an App User is created, they are assigned no rights. They will be able to authenticate and list forms on a mobile client, but the form list will be empty, as the list only includes Forms that the App User has read access to. Once an App User is created, you'll likely wish to use the `Form Assignments resource </central-api-form-management/#form-assignments>`__ to actually assign the ``app-user``\  role to them for the Forms you wish.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "displayName": "My Display Name"
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
                  
                    The friendly nickname of the ``App User``\  to be created.

              
  
  
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
            "projectId": 1
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
                  
                    If present, this is the Token that can be used to authenticate a request as this ``App User``\ . If not present, this ``App User``\ 's access has been revoked.

                * - projectId


                  - number
                  
                    The ID of the ``Project``\  that this ``App User``\  is bound to.

              
      

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
                  
                    

              
      
Deleting a App User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/app-users/{id}**

You don't have to delete a ``App User``\  in order to cut off its access. Using a ``User``\ 's credentials you can simply `log the App User's session out </central-api-authentication/#revoking-an-app-user>`__ using its token. This will end its session without actually deleting the App User, which allows you to still see it in the configuration panel and inspect its history. This is what the administrative panel does when you choose to "Revoke" the App User.

That said, if you do wish to delete the App User altogether, you can do so by issuing a ``DELETE``\  request to its resource path. App Users cannot delete themselves.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          The numeric ID of the App User

          Example: ``16``
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``

  
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
                  
                    

              
      

Roles
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.5)*\ 

The Roles API lists and describes each known Role within the system. Right now, Roles may not be created or customized via the API, but this will likely change in the future.

Each Role contains information about the verbs it allows its assignees to perform. Some Roles have a system name associated with them; the Roles may always be referenced by this system name in request URLs, and system Roles are always read-only.

Listing all Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/roles**

Currently, there are no paging or filtering options, so listing ``Role``\ s will get you every Role in the system, every time. There are no authorization restrictions upon this endpoint: anybody is allowed to list all Role information at any time.

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          [
            {
              "id": 4,
              "name": "Project Manager",
              "system": "manager",
              "verbs": [
                "project.update",
                "project.delete"
              ],
              "createdAt": "2018-01-19T23:58:03.395Z",
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
                
                
                * - id


                  - number
                  
                    The numerical ID of the Role.

                    Example: ``4``
                * - name


                  - string
                  
                    The human-readable name for the Role.

                    Example: ``Project Manager``
                * - system


                  - string
                  
                    The system name of the Role. Roles that have system names may not be modified.

                    Example: ``manager``
                * - verbs


                  - array
                  
                    The array of string verbs this Role confers.

                    Example: ``["project.update", "project.delete"]``
                    
    

                     
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-09-18 23:42:11.406000+00:00``

              
      
Getting Role Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/roles/{id}**

Getting an individual Role does not reveal any additional information over listing all Roles. It is, however, useful for direct lookup of a specific role:

The ``id``\  parameter for Roles here and elsewhere will accept the numeric ID associated with that Role, *or*\  a ``system``\  name if there is one associated with the Role. Thus, you may request ``/v1/roles/admin``\  on any ODK Central server and receive information about the Administrator role.

As with Role listing, there are no authorization restrictions upon this endpoint: anybody is allowed to get information about any Role at any time.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``1``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "id": 4,
            "name": "Project Manager",
            "system": "manager",
            "verbs": [
              "project.update",
              "project.delete"
            ],
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
                
                
                * - id


                  - number
                  
                    The numerical ID of the Role.

                    Example: ``4``
                * - name


                  - string
                  
                    The human-readable name for the Role.

                    Example: ``Project Manager``
                * - system


                  - string
                  
                    The system name of the Role. Roles that have system names may not be modified.

                    Example: ``manager``
                * - verbs


                  - array
                  
                    The array of string verbs this Role confers.

                    Example: ``["project.update", "project.delete"]``
                    
    

                     
                * - createdAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-09-18 23:42:11.406000+00:00``
              
      

Assignments
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.5)*\ 

There are multiple Assignments resources. This one, upon the API root (``/v1/assignments``\ ), manages Role assignment to the entire system (e.g. if you are assigned a Role that gives you ``form.create``\ , you may create a form anywhere on the entire server).

The `Project Assignments resource </central-api-project-management/#project-assignments>`__, nested under Projects, manages Role assignment to that Project in particular, and all objects within it. And the `Form Assignments resource </central-api-form-management/#form-assignments>`__ allows even more granular assignments, to specific Forms within a Project. All of these resources have the same structure and take and return the same data types.

Assignments may be created (``POST``\ ) and deleted (``DELETE``\ ) like any other resource in the system. Here, creating an Assignment grants the referenced Actor the verbs associated with the referenced Role upon all system objects. The pathing for creation and deletion is not quite REST-standard: we represent the relationship between Role and Actor directly in the URL rather than as body data: ``assignments/{role}/{actor}``\  represents the assignment of the given Role to the given Actor.

Listing all Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/assignments**

This will list every server-wide assignment, in the form of ``actorId``\ /``roleId``\  pairs. It will *not*\  list Project-specific Assignments. To find those, you will need the `Assignments subresource </central-api-project-management/#project-assignments>`__ within Projects.

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to expand the ``actorId``\  into a full ``actor``\  objects. The Role reference remains a numeric ID.

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

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

              
      **Extended Assignment**

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
              
      
Listing all Actors assigned some Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/assignments/{roleId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, this endpoint lists all ``Actors``\  that have been assigned that Role on a server-wide basis.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``admin``

  
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
                  
                    

                * - message


                  - string
                  
                    

              
      
Assigning an Actor to a server-wide Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , assigns that Role to that Actor across the entire server.

No ``POST``\  body data is required, and if provided it will be ignored.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``admin``
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
                  
                    

              
      
Stripping an Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/assignments/{roleId}/{actorId}**

Given a ``roleId``\ , which may be a numeric ID or a string role ``system``\  name, and a numeric ``actorId``\ , unassigns that Role from that Actor across the entire server.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``admin``
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
                  
                    

              
      

