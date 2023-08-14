.. auto generated file - DO NOT MODIFY 

System Endpoints
=======================================================================================================================

There are some resources available for getting or setting system information and configuration. You can set the `Usage Reporting configuration </central-api-system-endpoints/#usage-reporting-configuration>`__ for the server, retrieve the `Server Audit Logs </central-api-system-endpoints/#server-audit-logs>`__, or perform a `Direct Backup </central-api-system-endpoints/#direct-backup>`__.


Usage Reporting Configuration
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 1.3)*\ 

Getting the current configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/config/analytics**

If the Usage Reporting configuration is not set, this endpoint will return a ``404``\ . Once the configuration is set, this endpoint will indicate whether the server will share usage data with the Central team. If the server will share usage data, and contact information was provided, this endpoint will also return the provided work email address and organization name.

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - key


                  - string
                  
                    The type of system configuration.

                * - setAt


                  - string
                  
                    ISO date format. The last time this system configuration was set.

                * - value


                  - object
                  
                    Details about the Usage Reporting configuration.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              ``true``\  if the server will share usage data with the Central team and ``false``\  if not.

                              Example: ``none``
                          * - email


                            - string
                            
                              The work email address to include with the metrics report.

                          * - organization


                            - string
                            
                              The organization name to include with the metrics report.

                     
              
      

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
                  
                    

              
      
Setting a new configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/config/analytics**

An Administrator can use this endpoint to choose whether the server will share anonymous usage data with the Central team. This configuration affects the entire server. Until the Usage Reporting configuration is set, Administrators will see a message on the Central administration website that provides further information.

If an Administrator specifies ``true``\  for ``enabled``\ , the server will share anonymous usage data monthly with the Central team. By specifying ``true``\ , the Administrator accepts the `Terms of Service <https://getodk.org/legal/tos.html>`__ and `Privacy Policy <https://getodk.org/legal/privacy.html>`__. The Administrator can also share contact information to include with the report.

If an Administrator specifies ``false``\  for ``enabled``\ , the server will not share anonymous usage data with the Central team. Administrators will no longer see the message on the administration website.

If the Usage Reporting configuration is already set, the current configuration will be overwritten with the new one.

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - enabled


                  - boolean
                  
                    See above.

                    Example: ``none``
                * - email


                  - string
                  
                    A work email address to include with the metrics report.

                * - organization


                  - string
                  
                    An organization name to include with the metrics report.

              
  
  
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - key


                  - string
                  
                    The type of system configuration.

                * - setAt


                  - string
                  
                    ISO date format. The last time this system configuration was set.

                * - value


                  - object
                  
                    Details about the Usage Reporting configuration.


                      
                    .. collapse:: expand
                      :class: nested-schema

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              ``true``\  if the server will share usage data with the Central team and ``false``\  if not.

                              Example: ``none``
                          * - email


                            - string
                            
                              The work email address to include with the metrics report.

                          * - organization


                            - string
                            
                              The organization name to include with the metrics report.

                     
              
      

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
                  
                    

              
      
Unsetting the current configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**DELETE /v1/config/analytics**

If the Usage Reporting configuration is unset, Administrators will once again see a message on the the Central administration website.

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
                  
                    

              
      

Usage Report Preview
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 1.3)*\ 

An Administrator of Central may opt in to sending periodic reports summarizing usage. Configuration of this reporting is described `here </central-api-system-endpoints/#usage-reporting-configuration>`__. For added transparency, the API provides a preview of the reported metrics.

Getting the Usage Report preview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/analytics/preview**

An Administrator can use this endpoint to preview the metrics being sent. The preview is computed on the fly and represents what the report would look like if sent at that time. This endpoint does not directly submit the Usage Report; that is handled internally as a scheduled Central task.

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
                  
                    

              
      

Server Audit Logs
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.6)*\ 

Many actions on ODK Central will automatically log an event to the Server Audit Log. Creating a new Form, for instance, will log a ``form.create``\  event, with information about the Actor who performed the action, and sometimes some additional details specific to the event.

Any time an audit action is logged, the request headers are checked. If ``X-Action-Notes``\  are provided anywhere, those notes will be logged into the audit entries as well. Note that some requests generate multiple audit entries; in these cases, the ``note``\  will be attached to every entry logged.

Server Audit Logs entries are created for the following ``action``\ s:

* ``user.create``\  when a new User is created.
* ``user.update``\  when User information is updated, like email or password.
* ``user.assignment.create``\  when a User is assigned to a Server Role.
* ``user.assignment.delete``\  when a User is unassigned from a Server Role.
* ``user.session.create``\  when a User logs in.
* ``user.delete``\  when a User is deleted.
* ``project.create``\  when a new Project is created.
* ``project.update``\  when top-level Project information is updated, like its name.
* ``project.delete``\  when a Project is deleted.
* ``form.create``\  when a new Form is created.
* ``form.update``\  when top-level Form information is updated, like its name or state.
* ``form.update.draft.set``\  when a Draft Form definition is set.
* ``form.update.draft.delete``\  when a Draft Form definition is deleted.
* ``form.update.publish``\  when a Draft Form is published to the Form.
* ``form.attachment.update``\  when a Form Attachment binary is set or cleared.
* ``form.submissions.export``\  when a Form's Submissions are exported to CSV.
* ``form.delete``\  when a Form is deleted.
* ``form.restore``\  when a Form that was deleted is restored.
* ``form.purge``\  when a Form is permanently purged.
* ``field*key.create``\  when a new App User is created.
* ``field*\ key.assignment.create``\  when an App User is assigned to a Server Role.
* ``field*key.assignment.delete``\  when an App User is unassigned from a Server Role.
* ``field*\ key.session.end``\  when an App User's access is revoked.
* ``field*key.delete``\  when an App User is deleted.
* ``public*\ link.create``\  when a new Public Link is created.
* ``public*link.assignment.create``\  when a Public Link is assigned to a Server Role.
* ``public*\ link.assignment.delete``\  when a Public Link is unassigned from a Server Role.
* ``public*link.session.end``\  when a Public Link's access is revoked.
* ``public*\ link.delete``\  when a Public Link is deleted.
* ``submission.create``\  when a new Submission is created.
* ``submission.update``\  when a Submission's metadata is updated.
* ``submission.update.version``\  when a Submission XML data is updated.
* ``submission.attachment.update``\  when a Submission Attachment binary is set or cleared, but *only via the REST API*\ . Attachments created alongside the submission over the OpenRosa ``/submission``\  API (including submissions from Collect) do not generate audit log entries.
* ``dataset.create``\  when a Dataset is created.
* ``dataset.update``\  when a Dataset is updated.
* ``dataset.update.publish``\  when a Dataset is published.
* ``entity.create``\  when an Entity is created.
* ``entity.create.error``\  when there is an error during entity creation process.
* ``config.set``\  when a system configuration is set.
* ``analytics``\  when a Usage Report is attempted.
* Deprecated: ``backup``\  when a backup operation is attempted for Google Drive backups.

Getting Audit Log Entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/audits**

This resource allows access to those log entries, with some paging and filtering options. These are provided by querystring parameters: ``action``\  allows filtering by the action types listed above, ``start``\  and ``end``\  allow filtering by log timestamp (see below), and ``limit``\  and ``offset``\  control paging. If no paging parameters are given, the server will attempt to return every audit log entry that it has.

The ``start``\  and ``end``\  parameters work based on exact timestamps, given in `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ format. It is possible to provide just a datestring (eg ``2000-01-01``\ ), in which case midnight will be inferred. But this value alone leaves the timezone unspecified. When no timezone is given, the server's local time will be used: the standard `Docker deployment <https://docs.getodk.org/central-install/>`__ will always set server local time to UTC, but installations may have been customized, and there is no guarantee the UTC default hasn't been overridden.

For this reason, **we recommend always setting a timezone**\  when querying based on ``start``\  and ``end``\ : either by appending a ``z``\  to indicate UTC (eg ``2000-01-01z``\ ) or by explicitly specifying a timezone per ISO 8601 (eg ``2000-01-01+08``\ ). The same applies for full timestamps (eg ``2000-01-01T12:12:12z``\ , ``2000-01-01T12:12:12+08``\ ).

``start``\  may be given without ``end``\ , and vice versa, in which case the timestamp filter will only be bounded on the specified side. They are both inclusive (``>=``\  and ``<=``\ , respectively).

This endpoint supports retrieving extended metadata; provide a header ``X-Extended-Metadata: true``\  to additionally expand the ``actorId``\  into full ``actor``\  details, and ``acteeId``\  into full ``actee``\  details. The ``actor``\  will always be an Actor, but the ``actee``\  may be an Actor, a Project, a Form, or some other type of object depending on the type of action.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - action

          *(query)*

        - string
        
          The name of the `action` to filter by.

          Example: ``form.create``
      * - start

          *(query)*

        - string
        
          The timestamp before which log entries are to be filtered out.

          Example: ``2000-01-01z``
      * - end

          *(query)*

        - string
        
          The timestamp after which log entries are to be filtered out.

          Example: ``2000-12-31T23:59.999z``
      * - limit

          *(query)*

        - number
        
          The maximum number of entries to return.

          Example: ``100``
      * - offset

          *(query)*

        - number
        
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


      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The ID of the actor, if any, that initiated the action.

                    Example: ``42``
                * - action


                  - string
                  
                    The action that was taken.

                    Example: ``form.create``
                * - acteeId


                  - string
                  
                    The ID of the permissioning object against which the action was taken.

                    Example: ``85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - details


                  - object
                  
                    Additional details about the action that vary according to the type of action.

                * - loggedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18T23:19:14.802Z``

              

      .. list-table::
        :class: schema-table-wrap

        * - array


            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - actorId


                  - number
                  
                    The ID of the actor, if any, that initiated the action.

                    Example: ``42``
                * - action


                  - string
                  
                    The action that was taken.

                    Example: ``form.create``
                * - acteeId


                  - string
                  
                    The ID of the permissioning object against which the action was taken.

                    Example: ``85cb9aff-005e-4edd-9739-dc9c1a829c44``
                * - details


                  - object
                  
                    Additional details about the action that vary according to the type of action.

                * - loggedAt


                  - string
                  
                    ISO date format

                    Example: ``2018-04-18T23:19:14.802Z``
                * - actor


                  - object
                  
                    


                      
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
                     
                * - actee


                  - object
                  
                    The details of the actee given by ``acteeId``\ . Depending on the action type, this could be a number of object types, including an ``Actor``\ , a ``Project``\ , or a ``Form``\ .


              
      

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
                  
                    

                    Example: ``400``
                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    

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
              
      

Direct Backup
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 1.1)*\ 

ODK Central offers an HTTP endpoint that will immediately perform a backup on the system database and send that encrypted backup as the response. To use it, ``POST``\  with an encryption passphrase.

Note that performing the backup takes a great deal of time, during which the request will be held open. As a result, the endpoint will trickle junk data every five seconds while that processing is occurring to prevent the request from timing out. Depending on how much data you have, it can take many minutes for the data stream to speed up to a full transfer rate.

Using an Encryption Passphrase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**POST /v1/backup**

Use the ``POST``\  verb to start a direct download ad-hoc backup. You will want to supply a ``passphrase``\  with your chosen encryption passphrase. It is possible to omit this, in which case the backup will still be encrypted, but it will decrypt given an empty passphrase.

Please see the section notes above about the long-running nature of this endpoint.

.. dropdown:: Request



  **Request body**

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "passphrase": "my-password"
          }

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - passphrase


                  - string
                  
                    The passphrase with which to encrypt the backup.

              
  
  
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
                  
                    

                * - message


                  - string
                  
                    

              
      

