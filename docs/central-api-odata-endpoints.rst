.. auto generated file - DO NOT MODIFY 

OData Endpoints
=======================================================================================================================

.. raw:: html
  
  <p><a href="http://www.odata.org/">OData</a> is an emerging standard for the formal description and transfer of data between web services. In its most ambitious form, it aims to be <em>the</em> standard way for any REST or REST-like API to enable interoperability with other services, not unlike the API Blueprint format this document is written in. However, in practical usage today it is primarily a way for data-centric web services to describe and transfer their data to various clients for deeper analysis or presentation.</p><p>ODK Central implements the <a href="http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#_Toc505771292">4.0 Minimal Conformance level</a> of the specification. Our goal is to enable data analysis and reporting through powerful third-party tools, sending them the data over OData, rather than attempt to create our own analysis tools. Today, our implementation primarily targets <a href="https://docs.microsoft.com/en-us/power-bi/desktop-connect-odata">Microsoft Power BI</a> and <a href="https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_odata.html">Tableau</a>, two tools with reasonably robust free offerings that provide versatile analysis and visualization of data.</p><p>While OData itself supports data of any sort of structure, Power BI and Tableau both think in terms of relational tables. This presents an interesting challenge for representing ODK's <code>group</code> and <code>repeat</code> structures in OData. Our current solution is to treat every <code>repeat</code> in the <code>Form</code> definition as its own relational table, and we invent stable join IDs to relate the tables together.</p><p>In general, the OData standard protocol consists of three API endpoints:</p><ul><li><p>The <strong>Service Document</strong> describes the available resources in the service. We provide one of these for every <code>Form</code> in the system. As of version 2023.2, we also provide one for every <code>Dataset</code>.</p></li><li><p>The <strong>Metadata Document</strong> is a formal XML-based EDMX schema description of every data object we might return. It is linked in every OData response.</p></li><li><p>The actual data documents, linked from the Service Document, are a simple JSON representation of the submission data or entity, conforming to the schema we describe in our Metadata Document.</p></li></ul><p>As our focus is on the bulk-export of data from ODK Central so that more advanced analysis tools can handle the data themselves, we do not support most of the features at the Intermediate and above conformance levels, like <code>$sort</code> or <code>$filter</code>.</p>


OData Form Service
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>ODK Central presents one OData service for every <code>Form</code> it knows about. To access the OData service, simply add <code>.svc</code> to the resource URL for the given Form.</p>

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.svc**

.. raw:: html

  <p>The Service Document is essentially the index of all available documents. From this document, you will find links to all other available information in this OData service. In particular, you will find the Metadata Document, as well as a data document for each table defined by the <code>Form</code>.</p><p>You will always find a link to the <code>/Submissions</code> subpath, which is the data document that represents the &quot;root&quot; table, the data from each <code>Submission</code> that is not nested within any <code>repeat</code>s.</p><p>This document is available only in JSON format.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "@odata.context": "https://your.odk.server/v1/projects/7/forms/sample.svc/$metadata",
            "value": [
              {
                "kind": "EntitySet",
                "name": "Submissions",
                "url": "Submissions"
              },
              {
                "kind": "EntitySet",
                "name": "Submissions.children.child",
                "url": "Submissions.children.child"
              }
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
                
                
                * - @odata.context


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - value


                  - array
                  
                    .. raw:: html

                      <span></span>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - kind


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - name


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - url


                            - string
                            
                              .. raw:: html

                                <span></span>


                     
              
      

  **HTTP Status: 403**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

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

              
      

  **HTTP Status: 406**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

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

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.svc/$metadata**

.. raw:: html

  <p>The Metadata Document describes, in <a href="http://docs.oasis-open.org/odata/odata-csdl-xml/v4.01/odata-csdl-xml-v4.01.html">EDMX CSDL</a>, the schema of all the data you can retrieve from the OData Form Service in question (essentially, this is the XForms form schema translated into the OData format). EDMX/CSDL is very similar in concept to UML: there are objects, they have properties, and some of those properties are relationships to other objects.</p><p>If you are writing a tool to analyze your own data, whose schema you already know and understand, there is very little reason to touch this endpoint at all. You can likely skip ahead to the data documents themselves and work directly with the simple JSON output returned by those endpoints. This endpoint is more useful for authors of tools which seek to generically work with arbitrary data whose schemas they cannot know in advance.</p><p>In general, the way we model the XForms schema in OData terms is to represent <code>group</code>s as <code>ComplexType</code>s, and <code>repeat</code>s as <code>EntityType</code>s. In the world of OData, the primary difference between these two types is that Entity Types require Primary Keys, while Complex Types do not. This fits well with the way XForms surveys tend to be structured.</p><p>Most other types map to <code>String</code>. The exceptions are numbers, which map either to <code>Int64</code> or <code>Decimal</code> as appropriate, datetime fields which are always <code>DateTimeOffset</code>, date fields which become <code>Date</code>, and geography points which will appear as <code>GeographyPoint</code>, <code>GeographyLineString</code>, or <code>GeographyPolygon</code> given a <code>geopoint</code>, <code>geotrace</code>, or <code>geoshape</code>.</p><p>We also advertise the relationships between tables (the point at which a <code>repeat</code> connects the parent data to the repeated subtable) using the <code>NavigationProperty</code>. This should allow clients to present the data in an interconnected way, without the user having to specify how the tables connect to each other.</p><p>This implementation of the OData standard includes a set of Annotations describing the supported features of the service in the form of the <a href="https://github.com/oasis-tcs/odata-vocabularies/blob/master/vocabularies/Org.OData.Capabilities.V1.md">Capabilities Vocabulary</a>. In general, however, you can assume that the server supports the Minimal Conformance level and nothing beyond.</p><p>While the latest 4.01 OData specification adds a new JSON EDMX CSDL format, most servers and clients do not yet support that format, and so for this release of ODK Central only the older XML EDMX CSDL format is available.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

            <?xml version="1.0" encoding="UTF-8"?>
            <edmx:Edmx xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Version="4.0">
              <edmx:DataServices>
                <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="org.opendatakit.user.simple">
                  <EntityType Name="Submissions">
                    <Key><PropertyRef Name="__id"/></Key>
                    <Property Name="__id" Type="Edm.String"/>
                    <Property Name="meta" Type="org.opendatakit.user.simple.meta"/>
                    <Property Name="name" Type="Edm.String"/>
                    <Property Name="age" Type="Edm.Int64"/>
                  </EntityType>
                  <ComplexType Name="meta">
                    <Property Name="instanceID" Type="Edm.String"/>
                  </ComplexType>
                  <EntityContainer Name="simple">
                    <EntitySet Name="Submissions" EntityType="org.opendatakit.user.simple.Submissions">
                      <Annotation Term="Org.OData.Capabilities.V1.ConformanceLevel" EnumMember="Org.OData.Capabilities.V1.ConformanceLevelType/Minimal"/>
                      <Annotation Term="Org.OData.Capabilities.V1.BatchSupported" Bool="false"/>
                      <Annotation Term="Org.OData.Capabilities.V1.CountRestrictions">
                        <Record><PropertyValue Property="Countable" Bool="true"/></Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                        <Record>
                          <PropertyValue Property="NonCountableProperties">
                            <Collection>
                              <String>eq</String>
                            </Collection>
                          </PropertyValue>
                        </Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                        <Record>
                          <PropertyValue Property="Filterable" Bool="true"/>
                          <PropertyValue Property="RequiresFilter" Bool="false"/>
                          <PropertyValue Property="NonFilterableProperties">
                            <Collection>
                              <PropertyPath>meta</PropertyPath>
                              <PropertyPath>name</PropertyPath>
                              <PropertyPath>age</PropertyPath>
                            </Collection>
                          </PropertyValue>
                        </Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.SortRestrictions">
                        <Record><PropertyValue Property="Sortable" Bool="false"/></Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.ExpandRestrictions">
                        <Record><PropertyValue Property="Expandable" Bool="false"/></Record>
                      </Annotation>
                    </EntitySet>
                  </EntityContainer>
                </Schema>
              </edmx:DataServices>
            </edmx:Edmx>
          

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


              

    
              
      

  **HTTP Status: 406**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Data Document
^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.svc/{table}**

.. raw:: html

  <p>The data documents are the straightforward JSON representation of each table of <code>Submission</code> data. They follow the <a href="http://docs.oasis-open.org/odata/odata-json-format/v4.01/odata-json-format-v4.01.html">corresponding specification</a>, but apart from the representation of geospatial data as GeoJSON rather than the ODK proprietary format, the output here should not be at all surprising. If you are looking for JSON output of Submission data, this is the best place to look.</p><p>The <code>$top</code> and <code>$skip</code> querystring parameters, specified by OData, apply <code>limit</code> and <code>offset</code> operations to the data, respectively. The <code>$count</code> parameter, also an OData standard, will annotate the response data with the total row count, regardless of the scoping requested by <code>$top</code> and <code>$skip</code>. If <code>$top</code> parameter is provided in the request then the response will include <code>@odata.nextLink</code> that you can use as is to fetch the next set of data. While paging is possible through these parameters, it will not greatly improve the performance of exporting data. ODK Central prefers to bulk-export all of its data at once if possible.</p><p>As of ODK Central v1.1, the <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358948"><code>$filter</code> querystring parameter</a> is partially supported. In OData, you can use <code>$filter</code> to filter by any data field in the schema. The operators <code>lt</code>, <code>le</code>, <code>eq</code>, <code>ne</code>, <code>ge</code>, <code>gt</code>, <code>not</code>, <code>and</code>, and <code>or</code> are supported. The built-in functions <code>now</code>, <code>year</code>, <code>month</code>, <code>day</code>, <code>hour</code>, <code>minute</code>, <code>second</code> are supported. These supported elements may be combined in any way, but all other <code>$filter</code> features will cause an error.</p><p>The fields you can query against are as follows:</p><table><thead><tr>  <th>Submission Metadata</th>  <th>REST API Name</th>  <th>OData Field Name</th></tr></thead><tbody><tr>  <td>Submitter Actor ID</td>  <td><code>submitterId</code></td>  <td><code>__system/submitterId</code></td></tr><tr>  <td>Submission Timestamp</td>  <td><code>createdAt</code></td>  <td><code>__system/submissionDate</code></td></tr><tr>  <td>Submission Update Timestamp</td>  <td><code>updatedAt</code></td>  <td><code>__system/updatedAt</code></td></tr><tr>  <td>Review State</td>  <td><code>reviewState</code></td>  <td><code>__system/reviewState</code></td></tr></tbody></table><p>You can use <code>$root</code> expression to filter subtables (repeats) by Submission Metadata, you'll have to prefix above fields by <code>$root/Submissions/</code> in the filter criteria. For example, to filter a repeat table by Submission Timestamp you can pass <code>$filter=$root/Submissions/__system/submissionDate gt 2020-01-31T23:59:59.999Z</code> in the query parameter.</p><p>Note that the <code>submissionDate</code> has a time component. This means that any comparisons you make need to account for the full time of the submission. It might seem like <code>$filter=__system/submissionDate le 2020-01-31</code> would return all results on or before 31 Jan 2020, but in fact only submissions made before midnight of that day would be accepted. To include all of the month of January, you need to filter by either <code>$filter=__system/submissionDate le 2020-01-31T23:59:59.999Z</code> or <code>$filter=__system/submissionDate lt 2020-02-01</code>. Remember also that you can <a href="https://en.wikipedia.org/wiki/ISO_8601#Time_offsets_from_UTC">query by a specific timezone</a>.</p><p>Please see the <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358948">OData documentation</a> on <code>$filter</code> <a href="http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec_BuiltinFilterOperations">operations</a> and <a href="http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec_BuiltinQueryFunctions">functions</a> for more information.</p><p>As of ODK Central v1.2, you can use <code>%24expand=*</code> to expand all repeat repetitions. This is helpful if you'd rather get one nested JSON data payload of all hierarchical data, rather than retrieve each of repeat as a separate flat table with references.</p><p>The <em>nonstandard</em> <code>$wkt</code> querystring parameter may be set to <code>true</code> to request that geospatial data is returned as a <a href="https://en.wikipedia.org/wiki/Well-known_text">Well-Known Text (WKT) string</a> rather than a GeoJSON structure. This exists primarily to support Tableau, which cannot yet read GeoJSON, but you may find it useful as well depending on your mapping software. <strong>Please note</strong> that both GeoJSON and WKT follow a <code>(lon, lat, alt)</code> coördinate ordering rather than the ODK-proprietary <code>lat lon alt</code>. This is so that the values map neatly to <code>(x, y, z)</code>. GPS accuracy information is not a part of either standards specification, and so is presently omitted from OData output entirely. GeoJSON support may come in a future version.</p><p>As of ODK Central v2022.3, the <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358942"><code>$select</code> query parameter</a> is supported with some limitations:</p><ul><li><p><code>$select</code> and <code>$expand</code> can't be used together.</p></li><li><p>Child properties of repeats can't be requested using <code>$select</code></p></li></ul><p>As the vast majority of clients only support the JSON OData format, that is the only format ODK Central offers.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - table


        - string
        
          .. raw:: html

            The name of the table to be returned. These names can be found in the output of the [Service Document](/central-api-odata-endpoints/#service-document).

          Example: ``Submissions``
      * - %24skip

          *(query)*

        - number
        
          .. raw:: html

            If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          .. raw:: html

            If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          .. raw:: html

            If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24wkt

          *(query)*

        - boolean
        
          .. raw:: html

            If set to `true`, geospatial data will be returned as Well-Known Text (WKT) strings rather than GeoJSON structures.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - %24expand

          *(query)*

        - string
        
          .. raw:: html

            Repetitions, which should get expanded. Currently, only `*` is implemented, which expands all repetitions.

          Example: ``*``
      * - %24select

          *(query)*

        - string
        
          .. raw:: html

            If provided, will return only the selected fields.

          Example: ``__id, age, name, meta/instanceID``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "@odata.context": "https://your.odk.server/v1/projects/7/forms/simple.svc/$metadata#Submissions",
            "value": [
              {
                "__id": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
                "age": 25,
                "meta": {
                  "instanceID": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44"
                },
                "name": "Bob"
              },
              {
                "__id": "uuid:297000fd-8eb2-4232-8863-d25f82521b87",
                "age": 30,
                "meta": {
                  "instanceID": "uuid:297000fd-8eb2-4232-8863-d25f82521b87"
                },
                "name": "Alice"
              }
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
                
                
                * - @odata.context


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - value


                  - array
                  
                    .. raw:: html

                      <span></span>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - __id


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - age


                            - number
                            
                              .. raw:: html

                                <span></span>

                          * - meta


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - instanceID


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                               
                          * - name


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

              
      

  **HTTP Status: 406**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "406.1",
            "message": "Requested format not acceptable; this resource allows: (application/json, json)."
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

              
      

  **HTTP Status: 501**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "501.1",
            "message": "The requested feature $unsupported is not supported by this server."
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

              
      
Data Download Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /#/dl/projects{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

.. raw:: html

  <p><em>(introduced: version 1.2)</em></p><p>This route is a web browser oriented endpoint intended for user-interactive usage only. It's not part of the Central API, but is documented here as it can be useful.</p><p>If you are writing or configuring an OData client and have submission media files to deal with, you can run into authentication problems directly fetching or linking the media file URLs that are provided in the OData feed. This can be due to several reasons: if the user is not logged into the Central administration site (and thus has no valid cookie), if the request comes from a foreign origin (and thus cookies are not sent by the browser), and more.</p><p>To help manage this, the frontend provides a <code>/#/dl</code> path that allows file download. Just take a normal attachment download path and replace the <code>/v1</code> near the beginning of the path with <code>/#/dl</code>, and the user will be taken to a page managed by the Central administration website that will ensure the user is logged in, and offer the file as a download.</p><p>Because this <code>/#/dl</code> path returns a web page that causes a file download rather than directly returning the media file in question, it cannot be used to directly embed or retrieve these files, for example in a <code>&lt;img&gt;</code> tag.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - instanceId


        - string
        
          .. raw:: html

            The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
          .. raw:: html

            The name of the file to be retrieved.

          Example: ``file1.jpg``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: text/html

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          (html markup data)
          

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      

OData Dataset Service
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p>ODK Central presents one OData service for every <code>Dataset</code> as a way to get an OData feed of <code>Entities</code>. To access the OData service, simply add <code>.svc</code> to the resource URL for the given Dataset.</p>

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/datasets/{name}.svc**

.. raw:: html

  <p>The Service Document provides a link to the main source of information in this OData service: the list of <code>Entities</code> in this <code>Dataset</code>, as well as the Metadata Document describing the schema of this information.</p><p>This document is available only in JSON format.</p>

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
      * - name


        - string
        
          .. raw:: html

            The `name` of the `Dataset` whose OData service you wish to access.

          Example: ``trees``

  
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

              
      

  **HTTP Status: 406**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "406.1",
            "message": "Requested format not acceptable; this resource allows: (application/json, json)."
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

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/datasets/{name}.svc/$metadata**

.. raw:: html

  <p>The Metadata Document describes, in <a href="http://docs.oasis-open.org/odata/odata-csdl-xml/v4.01/odata-csdl-xml-v4.01.html">EDMX CSDL</a>, the schema of all the data you can retrieve from the OData Dataset Service in question. Essentially, these are the Dataset properties, or the schema of each <code>Entity</code>, translated into the OData format.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          <?xml version="1.0" encoding="UTF-8"?>
          <edmx:Edmx xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Version="4.0">
              <edmx:DataServices>
                  <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="org.opendatakit.entity">
                      <ComplexType Name="metadata">
                          <Property Name="createdAt" Type="Edm.DateTimeOffset"/>
                          <Property Name="creatorId" Type="Edm.String"/>
                          <Property Name="creatorName" Type="Edm.String"/>
                          <Property Name="updates" Type="Edm.Int64"/>
                          <Property Name="updatedAt" Type="Edm.DateTimeOffset"/>
                      </ComplexType>
                  </Schema>
                  <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="org.opendatakit.user.trees">
                      <EntityType Name="Entities">
                          <Key>
                              <PropertyRef Name="__id"/>
                          </Key>
                          <Property Name="__id" Type="Edm.String"/>
                          <Property Name="__system" Type="org.opendatakit.entity.metadata"/>
                          <Property Name="label" Type="Edm.String"/>
                          <Property Name="geometry" Type="Edm.String"/>
                          <Property Name="species" Type="Edm.String"/>
                          <Property Name="circumference_cm" Type="Edm.String"/>
                      </EntityType>
                      <EntityContainer Name="trees">
                          <EntitySet Name="Entities" EntityType="org.opendatakit.user.trees.Entities">
                              <Annotation Term="Org.OData.Capabilities.V1.ConformanceLevel" EnumMember="Org.OData.Capabilities.V1.ConformanceLevelType/Minimal"/>
                              <Annotation Term="Org.OData.Capabilities.V1.BatchSupported" Bool="false"/>
                              <Annotation Term="Org.OData.Capabilities.V1.CountRestrictions">
                                  <Record>
                                      <PropertyValue Property="Countable" Bool="true"/>
                                  </Record>
                              </Annotation>
                              <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                                  <Record>
                                      <PropertyValue Property="NonCountableProperties">
                                          <Collection>
                                              <String>eq</String>
                                          </Collection>
                                      </PropertyValue>
                                  </Record>
                              </Annotation>
                              <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                                  <Record>
                                      <PropertyValue Property="Filterable" Bool="true"/>
                                      <PropertyValue Property="RequiresFilter" Bool="false"/>
                                      <PropertyValue Property="NonFilterableProperties">
                                          <Collection>
                                              <PropertyPath>geometry</PropertyPath>
                                              <PropertyPath>species</PropertyPath>
                                              <PropertyPath>circumference_cm</PropertyPath>
                                          </Collection>
                                      </PropertyValue>
                                  </Record>
                              </Annotation>
                              <Annotation Term="Org.OData.Capabilities.V1.SortRestrictions">
                                  <Record>
                                      <PropertyValue Property="Sortable" Bool="false"/>
                                  </Record>
                              </Annotation>
                              <Annotation Term="Org.OData.Capabilities.V1.ExpandRestrictions">
                                  <Record>
                                      <PropertyValue Property="Expandable" Bool="false"/>
                                  </Record>
                              </Annotation>
                          </EntitySet>
                      </EntityContainer>
                  </Schema>
              </edmx:DataServices>
          </edmx:Edmx>
          

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


              

    
              
      

  **HTTP Status: 406**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Data Document
^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/datasets/{name}.svc/Entities**

.. raw:: html

  <p>A data document is the straightforward JSON representation of all the <code>Entities</code> in a <code>Dataset</code>.</p><p>The <code>$top</code> and <code>$skip</code> querystring parameters, specified by OData, apply <code>limit</code> and <code>offset</code> operations to the data, respectively. The <code>$count</code> parameter, also an OData standard, will annotate the response data with the total row count, regardless of the scoping requested by <code>$top</code> and <code>$skip</code>. If <code>$top</code> parameter is provided in the request then the response will include <code>@odata.nextLink</code> that you can use as is to fetch the next set of data.</p><p>The <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358948"><code>$filter</code> querystring parameter</a>can be used to filter by any data field in the system-level schema, but not the Dataset properties. The operators <code>lt</code>, <code>le</code>, <code>eq</code>, <code>ne</code>, <code>ge</code>, <code>gt</code>, <code>not</code>, <code>and</code>, and <code>or</code> are supported. The built-in functions <code>now</code>, <code>year</code>, <code>month</code>, <code>day</code>, <code>hour</code>, <code>minute</code>, <code>second</code> are supported.</p><p>The fields you can query against are as follows:</p><table><thead><tr>  <th>Entity Metadata</th>  <th>OData Field Name</th></tr></thead><tbody><tr>  <td>Entity UUID</td>  <td><code>__id</code></td></tr><tr>  <td>Entity Name (same as UUID)</td>  <td><code>name</code></td></tr><tr>  <td>Entity Label</td>  <td><code>label</code></td></tr><tr>  <td>Entity Creator Actor ID</td>  <td><code>__system/creatorId</code></td></tr><tr>  <td>Entity Timestamp</td>  <td><code>__system/createdAt</code></td></tr><tr>  <td>Entity Update Timestamp</td>  <td><code>__system/updatedAt</code></td></tr></tbody></table><p>Note that <code>createdAt</code> and <code>updatedAt</code> are time components. This means that any comparisons you make need to account for the full time of the entity. It might seem like <code>$filter=__system/createdAt le 2020-01-31</code> would return all results on or before 31 Jan 2020, but in fact only entities made before midnight of that day would be accepted. To include all of the month of January, you need to filter by either <code>$filter=__system/createdAt le 2020-01-31T23:59:59.999Z</code> or <code>$filter=__system/createdAt lt 2020-02-01</code>. Remember also that you can <a href="https://en.wikipedia.org/wiki/ISO_8601#Time_offsets_from_UTC">query by a specific timezone</a>.</p><p>Please see the <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358948">OData documentation</a> on <code>$filter</code> <a href="http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec_BuiltinFilterOperations">operations</a> and <a href="http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec_BuiltinQueryFunctions">functions</a> for more information.</p><p>The <a href="http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#_Toc31358942"><code>$select</code> query parameter</a> will return just the fields you specify and is supported on <code>__id</code>, <code>__system</code>, <code>__system/creatorId</code>, <code>__system/createdAt</code> and <code>__system/updatedAt</code>, as well as on user defined properties.</p><p>As the vast majority of clients only support the JSON OData format, that is the only format ODK Central offers.</p>

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
      * - name


        - string
        
          .. raw:: html

            Name of the Dataset

          Example: ``people``
      * - %24skip

          *(query)*

        - number
        
          .. raw:: html

            If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          .. raw:: html

            If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          .. raw:: html

            If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/createdAt) lt year(now())``
      * - %24select

          *(query)*

        - string
        
          .. raw:: html

            If provided, will return only the selected fields.

          Example: ``__id, label, name``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "@odata.context": "https://your.odk.server/v1/projects/7/datasets/trees.svc/$metadata#Entities",
            "value": [
              {
                "__id": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
                "label": "25cm purpleheart",
                "geometry": "32.7413996 -117.1394617 53.80000305175781 13.933,",
                "species": "purpleheart,",
                "circumference_cm": 2,
                "__system": {
                  "createdAt": "2022-12-09T19:41:16.478Z",
                  "creatorId": 39,
                  "creatorName": "Tree surveyor",
                  "updates": "1,",
                  "updatedAt": "2023-04-31T19:41:16.478Z",
                  "version": 1
                }
              },
              {
                "__id": "aeebd746-3b1e-4a24-ba9d-ed6547bd5ff1",
                "label": "345cm mora",
                "__system": {
                  "createdAt": "2023-04-09T19:10:16.128Z",
                  "creatorId": 39,
                  "creatorName": "Tree surveyor",
                  "updates": "1,",
                  "updatedAt": "2023-04-31T19:41:16.478Z",
                  "version": 2
                },
                "geometry": "47.722581 18.562111 0 0,",
                "species": "mora,",
                "circumference_cm": 345
              }
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
                
                
                * - @odata.context


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - value


                  - array
                  
                    .. raw:: html

                      <span></span>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - __id


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - label


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - __system


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

                                          <span></span>

                                    * - creatorId


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                    * - creatorName


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                    * - updates


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                                    * - updatedAt


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                               
                          * - geometry


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - species


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - circumference_cm


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

              
      

  **HTTP Status: 406**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "406.1",
            "message": "Requested format not acceptable; this resource allows: (application/json, json)."
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

              
      

  **HTTP Status: 501**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "501.1",
            "message": "The requested feature $unsupported is not supported by this server."
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

              
      

Draft Testing
-----------------------------------------------------------------------------------------------------------------------

.. raw:: html
  
  <p><em>(introduced: version 0.8)</em></p><p>To facilitate testing, there is an alternative collection of OData endpoints that will give access to the submissions uploaded to a Draft Form. This can be useful for ensuring that changes to your form do not break downstream dashboards or applications.</p><p>They are all identical to the non-Draft OData endpoints, but they will only return the Draft Form schema and Submissions.</p>

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.svc**

.. raw:: html

  <p>Identical to <a href="/central-api-odata-endpoints/#service-document">the non-Draft version</a> of this endpoint.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "@odata.context": "https://your.odk.server/v1/projects/7/forms/sample.svc/$metadata",
            "value": [
              {
                "kind": "EntitySet",
                "name": "Submissions",
                "url": "Submissions"
              },
              {
                "kind": "EntitySet",
                "name": "Submissions.children.child",
                "url": "Submissions.children.child"
              }
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
                
                
                * - @odata.context


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - value


                  - array
                  
                    .. raw:: html

                      <span></span>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - kind


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - name


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - url


                            - string
                            
                              .. raw:: html

                                <span></span>


                     
              
      

  **HTTP Status: 403**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

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

              
      

  **HTTP Status: 406**

  Content Type: application/json; charset=utf-8; odata.metadata=minimal

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

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.svc/$metadata**

.. raw:: html

  <p>Identical to <a href="/central-api-odata-endpoints/#metadata-document">the non-Draft version</a> of this endpoint.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

            <?xml version="1.0" encoding="UTF-8"?>
            <edmx:Edmx xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx" Version="4.0">
              <edmx:DataServices>
                <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="org.opendatakit.user.simple">
                  <EntityType Name="Submissions">
                    <Key><PropertyRef Name="__id"/></Key>
                    <Property Name="__id" Type="Edm.String"/>
                    <Property Name="meta" Type="org.opendatakit.user.simple.meta"/>
                    <Property Name="name" Type="Edm.String"/>
                    <Property Name="age" Type="Edm.Int64"/>
                  </EntityType>
                  <ComplexType Name="meta">
                    <Property Name="instanceID" Type="Edm.String"/>
                  </ComplexType>
                  <EntityContainer Name="simple">
                    <EntitySet Name="Submissions" EntityType="org.opendatakit.user.simple.Submissions">
                      <Annotation Term="Org.OData.Capabilities.V1.ConformanceLevel" EnumMember="Org.OData.Capabilities.V1.ConformanceLevelType/Minimal"/>
                      <Annotation Term="Org.OData.Capabilities.V1.BatchSupported" Bool="false"/>
                      <Annotation Term="Org.OData.Capabilities.V1.CountRestrictions">
                        <Record><PropertyValue Property="Countable" Bool="true"/></Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                        <Record>
                          <PropertyValue Property="NonCountableProperties">
                            <Collection>
                              <String>eq</String>
                            </Collection>
                          </PropertyValue>
                        </Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.FilterFunctions">
                        <Record>
                          <PropertyValue Property="Filterable" Bool="true"/>
                          <PropertyValue Property="RequiresFilter" Bool="false"/>
                          <PropertyValue Property="NonFilterableProperties">
                            <Collection>
                              <PropertyPath>meta</PropertyPath>
                              <PropertyPath>name</PropertyPath>
                              <PropertyPath>age</PropertyPath>
                            </Collection>
                          </PropertyValue>
                        </Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.SortRestrictions">
                        <Record><PropertyValue Property="Sortable" Bool="false"/></Record>
                      </Annotation>
                      <Annotation Term="Org.OData.Capabilities.V1.ExpandRestrictions">
                        <Record><PropertyValue Property="Expandable" Bool="false"/></Record>
                      </Annotation>
                    </EntitySet>
                  </EntityContainer>
                </Schema>
              </edmx:DataServices>
            </edmx:Edmx>
          

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


              

    
              
      

  **HTTP Status: 406**

  Content Type: application/xml

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          No Example

    .. tab-item:: Schema


      .. list-table::
        :class: schema-table-wrap

        * - string


              

    
              
      
Data Document
^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.svc/{table}**

.. raw:: html

  <p>Identical to <a href="/central-api-odata-endpoints/#data-document">the non-Draft version</a> of this endpoint.</p>

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

            The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - table


        - string
        
          .. raw:: html

            The name of the table to be returned. These names can be found in the output of the [Service Document](/central-api-odata-endpoints/#service-document).

          Example: ``Submissions``
      * - %24skip

          *(query)*

        - number
        
          .. raw:: html

            If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          .. raw:: html

            If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          .. raw:: html

            If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24wkt

          *(query)*

        - boolean
        
          .. raw:: html

            If set to `true`, geospatial data will be returned as Well-Known Text (WKT) strings rather than GeoJSON structures.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          .. raw:: html

            If provided, will filter responses to those matching the query. Only [certain fields](/central-api-odata-endpoints/#data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - %24expand

          *(query)*

        - string
        
          .. raw:: html

            Repetitions, which should get expanded. Currently, only `*` is implemented, which expands all repetitions.

          Example: ``*``
      * - %24select

          *(query)*

        - string
        
          .. raw:: html

            If provided, will return only the selected fields.

          Example: ``__id, age, name, meta/instanceID``

  
.. dropdown:: Response

  **HTTP Status: 200**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "@odata.context": "https://your.odk.server/v1/projects/7/forms/simple.svc/$metadata#Submissions",
            "value": [
              {
                "__id": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44",
                "age": 25,
                "meta": {
                  "instanceID": "uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44"
                },
                "name": "Bob"
              },
              {
                "__id": "uuid:297000fd-8eb2-4232-8863-d25f82521b87",
                "age": 30,
                "meta": {
                  "instanceID": "uuid:297000fd-8eb2-4232-8863-d25f82521b87"
                },
                "name": "Alice"
              }
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
                
                
                * - @odata.context


                  - string
                  
                    .. raw:: html

                      <span></span>

                * - value


                  - array
                  
                    .. raw:: html

                      <span></span>

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - __id


                            - string
                            
                              .. raw:: html

                                <span></span>

                          * - age


                            - number
                            
                              .. raw:: html

                                <span></span>

                          * - meta


                            - object
                            
                              .. raw:: html

                                <span></span>


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - instanceID


                                      - string
                                      
                                        .. raw:: html

                                          <span></span>

                               
                          * - name


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

              
      

  **HTTP Status: 406**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "406.1",
            "message": "Requested format not acceptable; this resource allows: (application/json, json)."
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

              
      

  **HTTP Status: 501**

  Content Type: application/json

  .. tab-set::

    .. tab-item:: Example

      .. code-block::

          {
            "code": "501.1",
            "message": "The requested feature $unsupported is not supported by this server."
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

              
      

