.. auto generated file - DO NOT MODIFY 

Accounts and Users
=======================================================================================================================

.. raw:: html
  
  <p>Today, there are two types of accounts: <code>Users</code>, which are the administrative accounts held by staff members managing the data collection process, and <code>App Users</code>, which are restricted access keys granted per Form within a Project to data collection clients in the field. Although both of these entities are backed by <code>Actor</code>s as we explain in the <a href="/central-api-authentication">Authentication section</a> above, there is not yet any way to directly create or manipulate an Actor. Today, you can only create, manage, and delete Users and App Users.</p><p>Actors (and thus Users) may be granted rights via Roles. The <code>/roles</code> Roles API is open for all to access, which describes all defined roles on the server. Getting information for an individual role from that same API will reveal which verbs are associated with each role: some role might allow only <code>submission.create</code> and <code>submission.update</code>, for example.</p><p>Right now, there are four predefined system roles: Administrator (<code>admin</code>), Project Manager (<code>manager</code>), Data Collector (<code>formfill</code>), and App User (<code>app-user</code>). Administrators are allowed to perform any action upon the server, while Project Managers are allowed to perform any action upon the projects they are assigned to manage.</p><p>Data Collectors can see all Forms in a Project and submit to them, but cannot see Submissions and cannot edit Form settings. Similarly, App Users are granted minimal rights: they can read Form data and create new Submissions on those Forms. While Data Collectors can perform these actions directly on the Central administration website by logging in, App Users can only do these things through Collect or a similar data collection client device.</p><p>The Roles API alone does not, however, tell you which Actors have been assigned with Roles upon which system objects. For that, you will need to consult the various Assignments resources. There are two, one under the API root (<code>/v1/assignments</code>), which manages assignments to the entire system, and another nested under each Project (<code>/v1/projects/…/assignments</code>) which manage assignments to that Project.</p>


Users
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>Presently, it is possible to create and list <code>User</code>s in the system, as well as to perform password reset operations. In future versions of this API it will be possible to manage existing user information and delete accounts as well.</p>

Listing all Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users**

.. raw:: html

  <p>Currently, there are no paging or filtering options, so listing <code>User</code>s will get you every User in the system, every time.</p><p>Optionally, a <code>q</code> querystring parameter may be provided to filter the returned users by any given string. The search is performed via a <a href="https://www.postgresql.org/docs/14/pgtrgm.html">trigram similarity index</a> over both the Email and Display Name fields, and results are ordered by match score, best matches first. Note that short search terms (less than 4 or 5 characters) may not return any results. Try a longer search if nothing is appearing.</p><p>If a <code>q</code> parameter is given, and it exactly matches an email address that exists in the system, that user's details will always be returned, even for actors who cannot <code>user.list</code>. The request must still authenticate as a valid Actor. This allows non-Administrators to choose a user for an action (eg grant rights) without allowing full search.</p><p>Actors who cannot <code>user.list</code> will always receive <code>[]</code> with a <code>200 OK</code> response.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - q

          *(query)*

        - string
        
          .. raw:: html

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
                * - email


                  - string
                  
                    .. raw:: html

                      <p>The email address of the user</p>


              
      

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

              
      
Creating a new User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/users**

.. raw:: html

  <p>All that is required to create a new user is an email address. That email address will receive a message instructing the new user on how to claim their new account and set a password.</p><p>Optionally, a password may also be supplied as a part of this request. If it is, the account is immediately usable with the given credentials. However, an email will still be dispatched with claim instructions as above.</p><p>Users are not able to do anything upon creation besides log in and change their own profile information. To allow Users to perform useful actions, you will need to <a href="/central-api-accounts-and-users/#assignments">assign them one or more Roles</a>.</p>

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "email": "my.email.address@getodk.org"
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

                      <p>The email address of the User account to be created.</p>

                * - password


                  - string
                  
                    .. raw:: html

                      <p>If provided, the User account will be created with this password. Otherwise, the user will still be able set their own password later.</p>

              
  
  
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

                * - email


                  - string
                  
                    .. raw:: html

                      <p>Only <code>User</code>s have email addresses associated with them</p>

              
      

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

              
      
Getting User details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users/{actorId}**

.. raw:: html

  <p>Typically, you supply the integer ID to get information about the user associated with that id.</p><p>It is also possible to supply the text <code>current</code> instead of an integer ID; please see the following endpoint for documentation about this.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          .. raw:: html

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

                * - email


                  - string
                  
                    .. raw:: html

                      <p>Only <code>User</code>s have email addresses associated with them</p>

              
      

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

              
      
Deleting a User
^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/users/{actorId}**

.. raw:: html

  <p>Upon User deletion:</p><ul><li><p>The account will be removed,</p></li><li><p>the user will be logged out of all existing sessions,</p></li><li><p>and should the user attempt to reset their password, they will receive an email informing them that their account has been removed.</p></li></ul><p>The User record will remain on file within the database, so that when for example information about the creator of a Form or Submission is requested, basic details are still available on file. A new User account may be created with the same email address as any deleted accounts.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          .. raw:: html

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

              
      
Modifying a User
^^^^^^^^^^^^^^^^^^^^^^^^^^

**PATCH /v1/users/{actorId}**

.. raw:: html

  <p>You can <code>PATCH</code> JSON data to update User details. Not all user information is modifiable; right now, the following fields may be updated:</p><ul><li><p><code>displayName</code> sets the friendly display name the web interface uses to refer to the user.</p></li><li><p><code>email</code> sets the email address associated with the account.</p></li></ul><p>When user details are updated, the <code>updatedAt</code> field will be automatically updated.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          .. raw:: html

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

                      <p>The friendly display name that should be associated with this User.</p>

                * - email


                  - string
                  
                    .. raw:: html

                      <p>The email address that should be associated with this User.</p>

              
  
  
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

                * - email


                  - string
                  
                    .. raw:: html

                      <p>Only <code>User</code>s have email addresses associated with them</p>

              
      

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

              
      
Getting authenticated User details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/users/current**

.. raw:: html

  <p>Typically, you would get User details by the User's numeric Actor ID.</p><p>However, if you only have a Bearer token, for example, you don't have any information about the user attached to that session, including even the ID with which to get more information. So you can instead supply the text <code>current</code> to get the user information associated with the authenticated session.</p><p>If you <em>do</em> use <code>current</code>, you may request extended metadata. Supply an <code>X-Extended-Metadata</code> header value of <code>true</code> to additionally retrieve an array of strings of the <code>verbs</code> the authenticated User/Actor is allowed to perform server-wide.</p>

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

                * - email


                  - string
                  
                    .. raw:: html

                      <p>Only <code>User</code>s have email addresses associated with them</p>

                * - verbs


                  - array
                  
                    .. raw:: html

                      <p>The verbs the authenticated Actor is allowed to perform server-wide.</p>

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

              
      
Directly updating a user password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PUT /v1/users/{actorId}/password**

.. raw:: html

  <p>To directly update a user password, you will need to reprove the user's intention by supplying the <code>old</code> password alongside the <code>new</code>. If you simply want to initiate an email-based password reset process, see the following endpoint.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - actorId


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - old


                  - string
                  
                    .. raw:: html

                      <p>The user's current password.</p>

                * - new


                  - string
                  
                    .. raw:: html

                      <p>The new password that the user wishes to set.</p>

              
  
  
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

              
      
Initating a password reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/users/reset/initiate**

.. raw:: html

  <p>Anybody can initate a reset of any user's password. An email will be sent with instructions on how to complete the password reset; it contains a token that is required to complete the process.</p><p>The optional query parameter <code>invalidate</code> may be set to <code>true</code> to immediately invalidate the user's current password, regardless of whether they complete the reset process. This can be done if, for example, their password has been compromised. In order to do this, though, the request must be performed as an authenticated user with permission to do this. If invalidation is attempted without the proper permissions, the entire request will fail.</p><p>If the email address provided does not match any user in the system, that address will still be sent an email informing them of the attempt and that no account was found.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - invalidate

          *(query)*

        - boolean
        
          .. raw:: html

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

                      <p>The email address of the User account whose password is to be reset.</p>

              
  
  
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

              
      

App Users
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>App Users may only be created, fetched, and manipulated within the nested Projects subresource, as App Users themselves are limited to the Project in which they are created. Through the <code>App User</code>s API, you can create, list, and delete the App Users of any given Project. Because they have extremely limited permissions, App Users cannot manage themselves; only <code>User</code>s may access this API.</p><p>For more information about the <code>/projects</code> containing resource, please see the following section.</p>

Listing all App Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/app-users**

.. raw:: html

  <p>Currently, there are no paging or filtering options, so listing <code>App User</code>s will get you every App User in the system, every time.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally retrieve the <code>lastUsed</code> timestamp of each App User, as well as to retrieve the details of the <code>Actor</code> the App User was <code>createdBy</code>.</p>

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

                      <p>If present, this is the Token that can be used to authenticate a request as this <code>App User</code>. If not present, this <code>App User</code>'s access has been revoked.</p>

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Project</code> that this <code>App User</code> is bound to.</p>

                    Example: ``1``

              
      .. raw:: html

        <p>Extended App Users</p>

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

                      <p>If present, this is the Token that can be used to authenticate a request as this <code>App User</code>. If not present, this <code>App User</code>'s access has been revoked.</p>

                    Example: ``d1!E2GVHgpr4h9bpxxtqUJ7EVJ1Q$Dusm2RBXg8XyVJMCBCbvyE8cGacxUx3bcUT``
                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Project</code> that this <code>App User</code> is bound to.</p>

                    Example: ``1``
                * - createdBy


                  - object
                  
                    .. raw:: html

                      <p>The <code>Actor</code> that created this <code>App User</code></p>


                      
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
                     
                * - lastUsed


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this <code>App User</code> was used to authenticate a request.</p>

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

              
      
Creating a new App User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/projects/{projectId}/app-users**

.. raw:: html

  <p>The only information required to create a new <code>App User</code> is its <code>displayName</code> (this is called &quot;Nickname&quot; in the administrative panel).</p><p>When an App User is created, they are assigned no rights. They will be able to authenticate and list forms on a mobile client, but the form list will be empty, as the list only includes Forms that the App User has read access to. Once an App User is created, you'll likely wish to use the <a href="/central-api-form-management/#form-assignments">Form Assignments resource</a> to actually assign the <code>app-user</code> role to them for the Forms you wish.</p>

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

  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "displayName": "My Display Name"
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

                      <p>The friendly nickname of the <code>App User</code> to be created.</p>

              
  
  
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

                      <p>If present, this is the Token that can be used to authenticate a request as this <code>App User</code>. If not present, this <code>App User</code>'s access has been revoked.</p>

                * - projectId


                  - number
                  
                    .. raw:: html

                      <p>The ID of the <code>Project</code> that this <code>App User</code> is bound to.</p>

              
      

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

              
      
Deleting a App User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/projects/{projectId}/app-users/{id}**

.. raw:: html

  <p>You don't have to delete a <code>App User</code> in order to cut off its access. Using a <code>User</code>'s credentials you can simply <a href="/central-api-authentication/#revoking-an-app-user">log the App User's session out</a> using its token. This will end its session without actually deleting the App User, which allows you to still see it in the configuration panel and inspect its history. This is what the administrative panel does when you choose to &quot;Revoke&quot; the App User.</p><p>That said, if you do wish to delete the App User altogether, you can do so by issuing a <code>DELETE</code> request to its resource path. App Users cannot delete themselves.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - number
        
          .. raw:: html

            The numeric ID of the App User

          Example: ``16``
      * - projectId


        - number
        
          .. raw:: html

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

              
      

Roles
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.5)</em></p><p>The Roles API lists and describes each known Role within the system. Right now, Roles may not be created or customized via the API, but this will likely change in the future.</p><p>Each Role contains information about the verbs it allows its assignees to perform. Some Roles have a system name associated with them; the Roles may always be referenced by this system name in request URLs, and system Roles are always read-only.</p>

Listing all Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/roles**

.. raw:: html

  <p>Currently, there are no paging or filtering options, so listing <code>Role</code>s will get you every Role in the system, every time. There are no authorization restrictions upon this endpoint: anybody is allowed to list all Role information at any time.</p>

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

                      <p>The numerical ID of the Role.</p>

                    Example: ``4``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The human-readable name for the Role.</p>

                    Example: ``Project Manager``
                * - system


                  - string
                  
                    .. raw:: html

                      <p>The system name of the Role. Roles that have system names may not be modified.</p>

                    Example: ``manager``
                * - verbs


                  - array
                  
                    .. raw:: html

                      <p>The array of string verbs this Role confers.</p>

                    Example: ``["project.update", "project.delete"]``
                    
    

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-09-18 23:42:11.406000+00:00``

              
      
Getting Role Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/roles/{id}**

.. raw:: html

  <p>Getting an individual Role does not reveal any additional information over listing all Roles. It is, however, useful for direct lookup of a specific role:</p><p>The <code>id</code> parameter for Roles here and elsewhere will accept the numeric ID associated with that Role, <em>or</em> a <code>system</code> name if there is one associated with the Role. Thus, you may request <code>/v1/roles/admin</code> on any ODK Central server and receive information about the Administrator role.</p><p>As with Role listing, there are no authorization restrictions upon this endpoint: anybody is allowed to get information about any Role at any time.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - id


        - string
        
          .. raw:: html

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

      .. raw:: html

        <span></span>

      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - id


                  - number
                  
                    .. raw:: html

                      <p>The numerical ID of the Role.</p>

                    Example: ``4``
                * - name


                  - string
                  
                    .. raw:: html

                      <p>The human-readable name for the Role.</p>

                    Example: ``Project Manager``
                * - system


                  - string
                  
                    .. raw:: html

                      <p>The system name of the Role. Roles that have system names may not be modified.</p>

                    Example: ``manager``
                * - verbs


                  - array
                  
                    .. raw:: html

                      <p>The array of string verbs this Role confers.</p>

                    Example: ``["project.update", "project.delete"]``
                    
    

                     
                * - createdAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-04-18 23:42:11.406000+00:00``
                * - updatedAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format</p>

                    Example: ``2018-09-18 23:42:11.406000+00:00``
              
      

Assignments
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.5)</em></p><p>There are multiple Assignments resources. This one, upon the API root (<code>/v1/assignments</code>), manages Role assignment to the entire system (e.g. if you are assigned a Role that gives you <code>form.create</code>, you may create a form anywhere on the entire server).</p><p>The <a href="/central-api-project-management/#project-assignments">Project Assignments resource</a>, nested under Projects, manages Role assignment to that Project in particular, and all objects within it. And the <a href="/central-api-form-management/#form-assignments">Form Assignments resource</a> allows even more granular assignments, to specific Forms within a Project. All of these resources have the same structure and take and return the same data types.</p><p>Assignments may be created (<code>POST</code>) and deleted (<code>DELETE</code>) like any other resource in the system. Here, creating an Assignment grants the referenced Actor the verbs associated with the referenced Role upon all system objects. The pathing for creation and deletion is not quite REST-standard: we represent the relationship between Role and Actor directly in the URL rather than as body data: <code>assignments/{role}/{actor}</code> represents the assignment of the given Role to the given Actor.</p>

Listing all Assignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/assignments**

.. raw:: html

  <p>This will list every server-wide assignment, in the form of <code>actorId</code>/<code>roleId</code> pairs. It will <em>not</em> list Project-specific Assignments. To find those, you will need the <a href="/central-api-project-management/#project-assignments">Assignments subresource</a> within Projects.</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to expand the <code>actorId</code> into a full <code>actor</code> objects. The Role reference remains a numeric ID.</p>

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

        <p>Extended Assignment</p>

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
              
      
Listing all Actors assigned some Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/assignments/{roleId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, this endpoint lists all <code>Actors</code> that have been assigned that Role on a server-wide basis.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          .. raw:: html

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

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

              
      
Assigning an Actor to a server-wide Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, assigns that Role to that Actor across the entire server.</p><p>No <code>POST</code> body data is required, and if provided it will be ignored.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          .. raw:: html

            Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``admin``
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

              
      
Stripping an Role Assignment from an Actor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/assignments/{roleId}/{actorId}**

.. raw:: html

  <p>Given a <code>roleId</code>, which may be a numeric ID or a string role <code>system</code> name, and a numeric <code>actorId</code>, unassigns that Role from that Actor across the entire server.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - roleId


        - string
        
          .. raw:: html

            Typically the integer ID of the `Role`. You may also supply the Role `system` name if it has one.

          Example: ``admin``
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

              
      

