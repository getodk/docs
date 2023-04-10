.. auto generated file - DO NOT MODIFY

System Endpoints
=======================================================================================================================

There are some resources available for getting or setting system information and configuration. You can set the `Usage Reporting configuration </reference/system-endpoints/usage-reporting-configuration>`__ for the server, retrieve the `Server Audit Logs </reference/system-endpoints/server-audit-logs>`__, or perform a `Direct Backup </reference/system-endpoints/direct-backup>`__.

Getting the current configuration
-----------------------------------------------------------------------------------------------------------------------

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

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              ``true``\  if the server will share usage data with the Central team and ``false``\  if not.

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Setting a new configuration
-----------------------------------------------------------------------------------------------------------------------

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

                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - enabled


                            - boolean
                            
                              ``true``\  if the server will share usage data with the Central team and ``false``\  if not.

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Unsetting the current configuration
-----------------------------------------------------------------------------------------------------------------------

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

              
      
  
Getting the Usage Report preview
-----------------------------------------------------------------------------------------------------------------------

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
Getting Audit Log Entries
-----------------------------------------------------------------------------------------------------------------------

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


    

              
      

  **HTTP Status: 400**

  Content Type: application/json; extended

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "pencil",
            "details": {},
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

                * - details


                  - object
                  
                    a subobject that contains programmatically readable details about this error

                * - message


                  - string
                  
                    None

              
      

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

              
      
  
Using an Encryption Passphrase
-----------------------------------------------------------------------------------------------------------------------

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
                  
                    None

                * - message


                  - string
                  
                    None

              
      
  
