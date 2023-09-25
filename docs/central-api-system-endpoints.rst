.. auto generated file - DO NOT MODIFY 

System Endpoints
=======================================================================================================================

.. raw:: html
  
  <p>There are some resources available for getting or setting system information and configuration. You can set the <a href="/central-api-system-endpoints/#usage-reporting-configuration">Usage Reporting configuration</a> for the server, retrieve the <a href="/central-api-system-endpoints/#server-audit-logs">Server Audit Logs</a>, or perform a <a href="/central-api-system-endpoints/#direct-backup">Direct Backup</a>.</p>


Usage Reporting Configuration
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.3)</em></p>

Getting the current configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/config/analytics**

.. raw:: html

  <p>If the Usage Reporting configuration is not set, this endpoint will return a <code>404</code>. Once the configuration is set, this endpoint will indicate whether the server will share usage data with the Central team. If the server will share usage data, and contact information was provided, this endpoint will also return the provided work email address and organization name.</p>

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "key": "some_type",
            "setAt": "2018-01-06T00:32:52.787Z",
            "value": {
              "enabled": true,
              "email": "my.email.address@getodk.org",
              "organization": "Organization Name"
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
                
                
                * - key


                  - string
                  
                    .. raw:: html

                      <p>The type of system configuration.</p>

                * - setAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this system configuration was set.</p>

                * - value


                  - object
                  
                    .. raw:: html

                      <p>Details about the Usage Reporting configuration.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              .. raw:: html

                                <p><code>true</code> if the server will share usage data with the Central team and <code>false</code> if not.</p>

                              Example: ``none``
                          * - email


                            - string
                            
                              .. raw:: html

                                <p>The work email address to include with the metrics report.</p>

                          * - organization


                            - string
                            
                              .. raw:: html

                                <p>The organization name to include with the metrics report.</p>

                     
              
      

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

              
      
Setting a new configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/config/analytics**

.. raw:: html

  <p>An Administrator can use this endpoint to choose whether the server will share anonymous usage data with the Central team. This configuration affects the entire server. Until the Usage Reporting configuration is set, Administrators will see a message on the Central administration website that provides further information.</p><p>If an Administrator specifies <code>true</code> for <code>enabled</code>, the server will share anonymous usage data monthly with the Central team. By specifying <code>true</code>, the Administrator accepts the <a href="https://getodk.org/legal/tos.html">Terms of Service</a> and <a href="https://getodk.org/legal/privacy.html">Privacy Policy</a>. The Administrator can also share contact information to include with the report.</p><p>If an Administrator specifies <code>false</code> for <code>enabled</code>, the server will not share anonymous usage data with the Central team. Administrators will no longer see the message on the administration website.</p><p>If the Usage Reporting configuration is already set, the current configuration will be overwritten with the new one.</p>

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "enabled": true,
            "email": "my.email.address@getodk.org",
            "organization": "Organization Name"
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
                
                
                * - enabled


                  - boolean
                  
                    .. raw:: html

                      <p>See above.</p>

                    Example: ``none``
                * - email


                  - string
                  
                    .. raw:: html

                      <p>A work email address to include with the metrics report.</p>

                * - organization


                  - string
                  
                    .. raw:: html

                      <p>An organization name to include with the metrics report.</p>

              
  
  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "key": "some_type",
            "setAt": "2018-01-06T00:32:52.787Z",
            "value": {
              "enabled": true,
              "email": "my.email.address@getodk.org",
              "organization": "Organization Name"
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
                
                
                * - key


                  - string
                  
                    .. raw:: html

                      <p>The type of system configuration.</p>

                * - setAt


                  - string
                  
                    .. raw:: html

                      <p>ISO date format. The last time this system configuration was set.</p>

                * - value


                  - object
                  
                    .. raw:: html

                      <p>Details about the Usage Reporting configuration.</p>


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              .. raw:: html

                                <p><code>true</code> if the server will share usage data with the Central team and <code>false</code> if not.</p>

                              Example: ``none``
                          * - email


                            - string
                            
                              .. raw:: html

                                <p>The work email address to include with the metrics report.</p>

                          * - organization


                            - string
                            
                              .. raw:: html

                                <p>The organization name to include with the metrics report.</p>

                     
              
      

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

              
      
Unsetting the current configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/config/analytics**

.. raw:: html

  <p>If the Usage Reporting configuration is unset, Administrators will once again see a message on the the Central administration website.</p>

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
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

              
      

Usage Report Preview
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.3)</em></p><p>An Administrator of Central may opt in to sending periodic reports summarizing usage. Configuration of this reporting is described <a href="/central-api-system-endpoints/#usage-reporting-configuration">here</a>. For added transparency, the API provides a preview of the reported metrics.</p>

Getting the Usage Report preview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/analytics/preview**

.. raw:: html

  <p>An Administrator can use this endpoint to preview the metrics being sent. The preview is computed on the fly and represents what the report would look like if sent at that time. This endpoint does not directly submit the Usage Report; that is handled internally as a scheduled Central task.</p>

.. dropdown:: Request

  This endpoint doesn't take any request parameter or data
  
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

              
      

Server Audit Logs
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.6)</em></p><p>Many actions on ODK Central will automatically log an event to the Server Audit Log. Creating a new Form, for instance, will log a <code>form.create</code> event, with information about the Actor who performed the action, and sometimes some additional details specific to the event.</p><p>Any time an audit action is logged, the request headers are checked. If <code>X-Action-Notes</code> are provided anywhere, those notes will be logged into the audit entries as well. Note that some requests generate multiple audit entries; in these cases, the <code>note</code> will be attached to every entry logged.</p><p>Server Audit Logs entries are created for the following <code>action</code>s:</p><ul><li><code>user.create</code> when a new User is created.</li><li><code>user.update</code> when User information is updated, like email or password.</li><li><code>user.assignment.create</code> when a User is assigned to a Server Role.</li><li><code>user.assignment.delete</code> when a User is unassigned from a Server Role.</li><li><code>user.session.create</code> when a User logs in.</li><li><code>user.delete</code> when a User is deleted.</li><li><code>project.create</code> when a new Project is created.</li><li><code>project.update</code> when top-level Project information is updated, like its name.</li><li><code>project.delete</code> when a Project is deleted.</li><li><code>form.create</code> when a new Form is created.</li><li><code>form.update</code> when top-level Form information is updated, like its name or state.</li><li><code>form.update.draft.set</code> when a Draft Form definition is set.</li><li><code>form.update.draft.delete</code> when a Draft Form definition is deleted.</li><li><code>form.update.publish</code> when a Draft Form is published to the Form.</li><li><code>form.attachment.update</code> when a Form Attachment binary is set or cleared.</li><li><code>form.submissions.export</code> when a Form's Submissions are exported to CSV.</li><li><code>form.delete</code> when a Form is deleted.</li><li><code>form.restore</code> when a Form that was deleted is restored.</li><li><code>form.purge</code> when a Form is permanently purged.</li><li><code>field_key.create</code> when a new App User is created.</li><li><code>field_key.assignment.create</code> when an App User is assigned to a Server Role.</li><li><code>field_key.assignment.delete</code> when an App User is unassigned from a Server Role.</li><li><code>field_key.session.end</code> when an App User's access is revoked.</li><li><code>field_key.delete</code> when an App User is deleted.</li><li><code>public_link.create</code> when a new Public Link is created.</li><li><code>public_link.assignment.create</code> when a Public Link is assigned to a Server Role.</li><li><code>public_link.assignment.delete</code> when a Public Link is unassigned from a Server Role.</li><li><code>public_link.session.end</code> when a Public Link's access is revoked.</li><li><code>public_link.delete</code> when a Public Link is deleted.</li><li><code>submission.create</code> when a new Submission is created.</li><li><code>submission.update</code> when a Submission's metadata is updated.</li><li><code>submission.update.version</code> when a Submission XML data is updated.</li><li><code>submission.attachment.update</code> when a Submission Attachment binary is set or cleared, but <em>only via the REST API</em>. Attachments created alongside the submission over the OpenRosa <code>/submission</code> API (including submissions from Collect) do not generate audit log entries.</li><li><code>dataset.create</code> when a Dataset is created.</li><li><code>dataset.update</code> when a Dataset is updated.</li><li><code>dataset.update.publish</code> when a Dataset is published.</li><li><code>entity.create</code> when an Entity is created.</li><li><code>entity.create.error</code> when there is an error during entity creation process.</li><li><code>config.set</code> when a system configuration is set.</li><li><code>analytics</code> when a Usage Report is attempted.</li><li>Deprecated: <code>backup</code> when a backup operation is attempted for Google Drive backups.</li></ul>

Getting Audit Log Entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/audits**

.. raw:: html

  <p>This resource allows access to those log entries, with some paging and filtering options. These are provided by querystring parameters: <code>action</code> allows filtering by the action types listed above, <code>start</code> and <code>end</code> allow filtering by log timestamp (see below), and <code>limit</code> and <code>offset</code> control paging. If no paging parameters are given, the server will attempt to return every audit log entry that it has.</p><p>The <code>start</code> and <code>end</code> parameters work based on exact timestamps, given in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. It is possible to provide just a datestring (eg <code>2000-01-01</code>), in which case midnight will be inferred. But this value alone leaves the timezone unspecified. When no timezone is given, the server's local time will be used: the standard <a href="https://docs.getodk.org/central-install/">Docker deployment</a> will always set server local time to UTC, but installations may have been customized, and there is no guarantee the UTC default hasn't been overridden.</p><p>For this reason, <strong>we recommend always setting a timezone</strong> when querying based on <code>start</code> and <code>end</code>: either by appending a <code>z</code> to indicate UTC (eg <code>2000-01-01z</code>) or by explicitly specifying a timezone per ISO 8601 (eg <code>2000-01-01+08</code>). The same applies for full timestamps (eg <code>2000-01-01T12:12:12z</code>, <code>2000-01-01T12:12:12+08</code>).</p><p><code>start</code> may be given without <code>end</code>, and vice versa, in which case the timestamp filter will only be bounded on the specified side. They are both inclusive (<code>&gt;=</code> and <code>&lt;=</code>, respectively).</p><p>This endpoint supports retrieving extended metadata; provide a header <code>X-Extended-Metadata: true</code> to additionally expand the <code>actorId</code> into full <code>actor</code> details, and <code>acteeId</code> into full <code>actee</code> details. The <code>actor</code> will always be an Actor, but the <code>actee</code> may be an Actor, a Project, a Form, or some other type of object depending on the type of action.</p>

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - action

          *(query)*

        - string
        
          .. raw:: html

            The name of the `action` to filter by.

          Example: ``form.create``
      * - start

          *(query)*

        - string
        
          .. raw:: html

            The timestamp before which log entries are to be filtered out.

          Example: ``2000-01-01z``
      * - end

          *(query)*

        - string
        
          .. raw:: html

            The timestamp after which log entries are to be filtered out.

          Example: ``2000-12-31T23:59.999z``
      * - limit

          *(query)*

        - number
        
          .. raw:: html

            The maximum number of entries to return.

          Example: ``100``
      * - offset

          *(query)*

        - number
        
          .. raw:: html

            The zero-indexed number of entries to skip from the result.

          Example: ``200``

  
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

                    Example: ``400``
                * - details


                  - object
                  
                    .. raw:: html

                      <p>a subobject that contains programmatically readable details about this error</p>

                * - message


                  - string
                  
                    .. raw:: html

                      <span></span>

                    Example: ``Could not parse the given data (2 chars) as json.``
              
      

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
              
      

Direct Backup
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 1.1)</em></p><p>ODK Central offers an HTTP endpoint that will immediately perform a backup on the system database and send that encrypted backup as the response. To use it, <code>POST</code> with an encryption passphrase.</p><p>Note that performing the backup takes a great deal of time, during which the request will be held open. As a result, the endpoint will trickle junk data every five seconds while that processing is occurring to prevent the request from timing out. Depending on how much data you have, it can take many minutes for the data stream to speed up to a full transfer rate.</p>

Using an Encryption Passphrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/backup**

.. raw:: html

  <p>Use the <code>POST</code> verb to start a direct download ad-hoc backup. You will want to supply a <code>passphrase</code> with your chosen encryption passphrase. It is possible to omit this, in which case the backup will still be encrypted, but it will decrypt given an empty passphrase.</p><p>Please see the section notes above about the long-running nature of this endpoint.</p>

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "passphrase": "my-password"
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
                
                
                * - passphrase


                  - string
                  
                    .. raw:: html

                      <p>The passphrase with which to encrypt the backup.</p>

              
  
  
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

              
      

