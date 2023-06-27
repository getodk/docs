.. auto generated file - DO NOT MODIFY 

OData Endpoints
=======================================================================================================================

`OData <http://www.odata.org/>`__ is an emerging standard for the formal description and transfer of data between web services. In its most ambitious form, it aims to be *the*\  standard way for any REST or REST-like API to enable interoperability with other services, not unlike the API Blueprint format this document is written in. However, in practical usage today it is primarily a way for data-centric web services to describe and transfer their data to various clients for deeper analysis or presentation.

ODK Central implements the `4.0 Minimal Conformance level <http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#*Toc505771292>`__ of the specification. Our goal is to enable data analysis and reporting through powerful third-party tools, sending them the data over OData, rather than attempt to create our own analysis tools. Today, our implementation primarily targets `Microsoft Power BI <https://docs.microsoft.com/en-us/power-bi/desktop-connect-odata>`__ and `Tableau <https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples*\ odata.html>`__, two tools with reasonably robust free offerings that provide versatile analysis and visualization of data.

While OData itself supports data of any sort of structure, Power BI and Tableau both think in terms of relational tables. This presents an interesting challenge for representing ODK's ``group``\  and ``repeat``\  structures in OData. Our current solution is to treat every ``repeat``\  in the ``Form``\  definition as its own relational table, and we invent stable join IDs to relate the tables together.

In general, the OData standard protocol consists of three API endpoints:

* The **Service Document**\  describes the available resources in the service. We provide one of these for every ``Form``\  in the system. As of version 2023.2, we also provide one for every ``Dataset``\ .

* The **Metadata Document**\  is a formal XML-based EDMX schema description of every data object we might return. It is linked in every OData response.

* The actual data documents, linked from the Service Document, are a simple JSON representation of the submission data or entity, conforming to the schema we describe in our Metadata Document.

As our focus is on the bulk-export of data from ODK Central so that more advanced analysis tools can handle the data themselves, we do not support most of the features at the Intermediate and above conformance levels, like ``$sort``\  or ``$filter``\ .


OData Form Service
-----------------------------------------------------------------------------------------------------------------------

ODK Central presents one OData service for every ``Form``\  it knows about. To access the OData service, simply add ``.svc``\  to the resource URL for the given Form.

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.svc**

The Service Document is essentially the index of all available documents. From this document, you will find links to all other available information in this OData service. In particular, you will find the Metadata Document, as well as a data document for each table defined by the ``Form``\ .

You will always find a link to the ``/Submissions``\  subpath, which is the data document that represents the "root" table, the data from each ``Submission``\  that is not nested within any ``repeat``\ s.

This document is available only in JSON format.

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - @odata.context


                  - string
                  
                    

                * - value


                  - array
                  
                    

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - kind


                            - string
                            
                              

                          * - name


                            - string
                            
                              

                          * - url


                            - string
                            
                              


                     
              
      

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
                  
                    

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}.svc/$metadata**

The Metadata Document describes, in `EDMX CSDL <http://docs.oasis-open.org/odata/odata-csdl-xml/v4.01/odata-csdl-xml-v4.01.html>`__, the schema of all the data you can retrieve from the OData Form Service in question (essentially, this is the XForms form schema translated into the OData format). EDMX/CSDL is very similar in concept to UML: there are objects, they have properties, and some of those properties are relationships to other objects.

If you are writing a tool to analyze your own data, whose schema you already know and understand, there is very little reason to touch this endpoint at all. You can likely skip ahead to the data documents themselves and work directly with the simple JSON output returned by those endpoints. This endpoint is more useful for authors of tools which seek to generically work with arbitrary data whose schemas they cannot know in advance.

In general, the way we model the XForms schema in OData terms is to represent ``group``\ s as ``ComplexType``\ s, and ``repeat``\ s as ``EntityType``\ s. In the world of OData, the primary difference between these two types is that Entity Types require Primary Keys, while Complex Types do not. This fits well with the way XForms surveys tend to be structured.

Most other types map to ``String``\ . The exceptions are numbers, which map either to ``Int64``\  or ``Decimal``\  as appropriate, datetime fields which are always ``DateTimeOffset``\ , date fields which become ``Date``\ , and geography points which will appear as ``GeographyPoint``\ , ``GeographyLineString``\ , or ``GeographyPolygon``\  given a ``geopoint``\ , ``geotrace``\ , or ``geoshape``\ .

We also advertise the relationships between tables (the point at which a ``repeat``\  connects the parent data to the repeated subtable) using the ``NavigationProperty``\ . This should allow clients to present the data in an interconnected way, without the user having to specify how the tables connect to each other.

This implementation of the OData standard includes a set of Annotations describing the supported features of the service in the form of the `Capabilities Vocabulary <https://github.com/oasis-tcs/odata-vocabularies/blob/master/vocabularies/Org.OData.Capabilities.V1.md>`__. In general, however, you can assume that the server supports the Minimal Conformance level and nothing beyond.

While the latest 4.01 OData specification adds a new JSON EDMX CSDL format, most servers and clients do not yet support that format, and so for this release of ODK Central only the older XML EDMX CSDL format is available.

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

The data documents are the straightforward JSON representation of each table of ``Submission``\  data. They follow the `corresponding specification <http://docs.oasis-open.org/odata/odata-json-format/v4.01/odata-json-format-v4.01.html>`__, but apart from the representation of geospatial data as GeoJSON rather than the ODK proprietary format, the output here should not be at all surprising. If you are looking for JSON output of Submission data, this is the best place to look.

The ``$top``\  and ``$skip``\  querystring parameters, specified by OData, apply ``limit``\  and ``offset``\  operations to the data, respectively. The ``$count``\  parameter, also an OData standard, will annotate the response data with the total row count, regardless of the scoping requested by ``$top``\  and ``$skip``\ . While paging is possible through these parameters, it will not greatly improve the performance of exporting data. ODK Central prefers to bulk-export all of its data at once if possible.

As of ODK Central v1.1, the ```$filter``\  querystring parameter <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*Toc31358948>`__ is partially supported. In OData, you can use ``$filter``\  to filter by any data field in the schema. The operators ``lt``\ , ``le``\ , ``eq``\ , ``ne``\ , ``ge``\ , ``gt``\ , ``not``\ , ``and``\ , and ``or``\  are supported. The built-in functions ``now``\ , ``year``\ , ``month``\ , ``day``\ , ``hour``\ , ``minute``\ , ``second``\  are supported. These supported elements may be combined in any way, but all other ``$filter``\  features will cause an error.

The fields you can query against are as follows:

| Submission Metadata         | REST API Name | OData Field Name          |
| --------------------------- | ------------- | ------------------------- |
| Submitter Actor ID          | ``submitterId``\  | ``*\ *system/submitterId``\     |
| Submission Timestamp        | ``createdAt``\    | ``*\ *system/submissionDate``\  |
| Submission Update Timestamp | ``updatedAt``\    | ``*\ *system/updatedAt``\       |
| Review State                | ``reviewState``\  | ``*\ *system/reviewState``\     |

Note that the ``submissionDate``\  has a time component. This means that any comparisons you make need to account for the full time of the submission. It might seem like ``$filter=*\ *system/submissionDate le 2020-01-31``\  would return all results on or before 31 Jan 2020, but in fact only submissions made before midnight of that day would be accepted. To include all of the month of January, you need to filter by either ``$filter=*\ *system/submissionDate le 2020-01-31T23:59:59.999Z``\  or ``$filter=*\ *system/submissionDate lt 2020-02-01``\ . Remember also that you can `query by a specific timezone <https://en.wikipedia.org/wiki/ISO*\ 8601#Time*offsets*\ from*UTC>`__.

Please see the `OData documentation <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*\ Toc31358948>`__ on ``$filter``\  `operations <http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec*BuiltinFilterOperations>`__ and `functions <http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec*\ BuiltinQueryFunctions>`__ for more information.

As of ODK Central v1.2, you can use ``%24expand=*``\  to expand all repeat repetitions. This is helpful if you'd rather get one nested JSON data payload of all hierarchical data, rather than retrieve each of repeat as a separate flat table with references.

The *nonstandard*\  ``$wkt``\  querystring parameter may be set to ``true``\  to request that geospatial data is returned as a `Well-Known Text (WKT) string <https://en.wikipedia.org/wiki/Well-known*text>`__ rather than a GeoJSON structure. This exists primarily to support Tableau, which cannot yet read GeoJSON, but you may find it useful as well depending on your mapping software. **Please note**\  that both GeoJSON and WKT follow a ``(lon, lat, alt)``\  coördinate ordering rather than the ODK-proprietary ``lat lon alt``\ . This is so that the values map neatly to ``(x, y, z)``\ . GPS accuracy information is not a part of either standards specification, and so is presently omitted from OData output entirely. GeoJSON support may come in a future version.

As of ODK Central v2022.3, the ```$select``\  query parameter <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*\ Toc31358942>`__ is supported with some limitations:

+ ``$select``\  and ``$expand``\  can't be used together.

+ Child properties of repeats can't be requested using ``$select``\ 

As the vast majority of clients only support the JSON OData format, that is the only format ODK Central offers.

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
        
          The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - table


        - string
        
          The name of the table to be returned. These names can be found in the output of the [Service Document](/reference/odata-endpoints/odata-form-service/service-document).

          Example: ``Submissions``
      * - %24skip

          *(query)*

        - number
        
          If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24wkt

          *(query)*

        - boolean
        
          If set to `true`, geospatial data will be returned as Well-Known Text (WKT) strings rather than GeoJSON structures.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - %24expand

          *(query)*

        - string
        
          Repetitions, which should get expanded. Currently, only `*` is implemented, which expands all repetitions.

          Example: ``*``
      * - %24select

          *(query)*

        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - @odata.context


                  - string
                  
                    

                * - value


                  - array
                  
                    

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - __id


                            - string
                            
                              

                          * - age


                            - number
                            
                              

                          * - meta


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - instanceID


                                      - string
                                      
                                        

                               
                          * - name


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
                  
                    

              
      
Data Download Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /#/dl/projects{projectId}/forms/{xmlFormId}/submissions/{instanceId}/attachments/{filename}**

*(introduced: version 1.2)*\ 

This route is a web browser oriented endpoint intended for user-interactive usage only. It's not part of the Central API, but is documented here as it can be useful.

If you are writing or configuring an OData client and have submission media files to deal with, you can run into authentication problems directly fetching or linking the media file URLs that are provided in the OData feed. This can be due to several reasons: if the user is not logged into the Central administration site (and thus has no valid cookie), if the request comes from a foreign origin (and thus cookies are not sent by the browser), and more.

To help manage this, the frontend provides a ``/#/dl``\  path that allows file download. Just take a normal attachment download path and replace the ``/v1``\  near the beginning of the path with ``/#/dl``\ , and the user will be taken to a page managed by the Central administration website that will ensure the user is logged in, and offer the file as a download.

Because this ``/#/dl``\  path returns a web page that causes a file download rather than directly returning the media file in question, it cannot be used to directly embed or retrieve these files, for example in a ``<img>``\  tag.

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
        
          The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - instanceId


        - string
        
          The `instanceId` of the Submission being referenced.

          Example: ``uuid:85cb9aff-005e-4edd-9739-dc9c1a829c44``
      * - filename


        - string
        
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

ODK Central presents one OData service for every ``Dataset``\  as a way to get an OData feed of ``Entities``\ . To access the OData service, simply add ``.svc``\  to the resource URL for the given Dataset.

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/datasets/{name}.svc**

The Service Document provides a link to the main source of information in this OData service: the list of ``Entities``\  in this ``Dataset``\ , as well as the Metadata Document describing the schema of this information.

This document is available only in JSON format.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``7``
      * - name


        - string
        
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
                  
                    

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/datasets/{name}.svc/$metadata**

The Metadata Document describes, in `EDMX CSDL <http://docs.oasis-open.org/odata/odata-csdl-xml/v4.01/odata-csdl-xml-v4.01.html>`__, the schema of all the data you can retrieve from the OData Dataset Service in question. Essentially, these are the Dataset properties, or the schema of each ``Entity``\ , translated into the OData format.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
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
                      </ComplexType>
                  </Schema>
                  <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="org.opendatakit.user.trees">
                      <EntityType Name="Entities">
                          <Key>
                              <PropertyRef Name="__id"/>
                          </Key>
                          <Property Name="__id" Type="Edm.String"/>
                          <Property Name="__system" Type="org.opendatakit.entity.metadata"/>
                          <Property Name="name" Type="Edm.String"/>
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

A data document is the straightforward JSON representation of all the ``Entities``\  in a ``Dataset``\ .

The ``$top``\  and ``$skip``\  querystring parameters, specified by OData, apply ``limit``\  and ``offset``\  operations to the data, respectively. The ``$count``\  parameter, also an OData standard, will annotate the response data with the total row count, regardless of the scoping requested by ``$top``\  and ``$skip``\ . While paging is possible through these parameters, it will not greatly improve the performance of exporting data. ODK Central prefers to bulk-export all of its data at once if possible.

The ```$filter``\  querystring parameter <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*Toc31358948>`__can be used to filter by any data field in the system-level schema, but not the Dataset properties. The operators ``lt``\ , ``le``\ , ``eq``\ , ``ne``\ , ``ge``\ , ``gt``\ , ``not``\ , ``and``\ , and ``or``\  are supported. The built-in functions ``now``\ , ``year``\ , ``month``\ , ``day``\ , ``hour``\ , ``minute``\ , ``second``\  are supported.

The fields you can query against are as follows:

| Entity Metadata         | OData Field Name     |
| ------------------------| -------------------- |
| Entity UUID             | ``*\ *id``\                |
| Entity Name (same as UUID) | ``name``\             |
| Entity Label            | ``label``\               |
| Entity Creator Actor ID | ``*\ *system/creatorId``\  |
| Entity Timestamp        | ``*\ *system/createdAt``\  |

Note that ``createdAt``\  is a time component. This means that any comparisons you make need to account for the full time of the entity. It might seem like ``$filter=*\ *system/createdAt le 2020-01-31``\  would return all results on or before 31 Jan 2020, but in fact only entities made before midnight of that day would be accepted. To include all of the month of January, you need to filter by either ``$filter=*\ *system/createdAt le 2020-01-31T23:59:59.999Z``\  or ``$filter=*\ *system/createdAt lt 2020-02-01``\ . Remember also that you can `query by a specific timezone <https://en.wikipedia.org/wiki/ISO*\ 8601#Time*offsets*\ from*UTC>`__.

Please see the `OData documentation <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*\ Toc31358948>`__ on ``$filter``\  `operations <http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec*BuiltinFilterOperations>`__ and `functions <http://docs.oasis-open.org/odata/odata/v4.01/cs01/part1-protocol/odata-v4.01-cs01-part1-protocol.html#sec*\ BuiltinQueryFunctions>`__ for more information.

The ```$select``\  query parameter <http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#*Toc31358942>`__ will return just the fields you specify and is supported on ``*\ *id``\ , ``*\ *system``\ , ``*\ *system/creatorId``\  and ``*\ _system/createdAt``\ , as well as on user defined properties.

As the vast majority of clients only support the JSON OData format, that is the only format ODK Central offers.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - name


        - string
        
          Name of the Dataset

          Example: ``people``
      * - %24skip

          *(query)*

        - number
        
          If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/createdAt) lt year(now())``
      * - %24select

          *(query)*

        - string
        
          If provided, will return only the selected fields.

          Example: ``__id, label, name``

  
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
                  
                    

              
      

Draft Testing
-----------------------------------------------------------------------------------------------------------------------

*(introduced: version 0.8)*\ 

To facilitate testing, there is an alternative collection of OData endpoints that will give access to the submissions uploaded to a Draft Form. This can be useful for ensuring that changes to your form do not break downstream dashboards or applications.

They are all identical to the non-Draft OData endpoints, but they will only return the Draft Form schema and Submissions.

Service Document
^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.svc**

Identical to `the non-Draft version </reference/odata-endpoints/odata-form-service/service-document>`__ of this endpoint.

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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - @odata.context


                  - string
                  
                    

                * - value


                  - array
                  
                    

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - kind


                            - string
                            
                              

                          * - name


                            - string
                            
                              

                          * - url


                            - string
                            
                              


                     
              
      

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
                  
                    

              
      
Metadata Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GET /v1/projects/{projectId}/forms/{xmlFormId}/draft.svc/$metadata**

Identical to `the non-Draft version </reference/odata-endpoints/odata-form-service/metadata-document>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
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

Identical to `the non-Draft version </reference/odata-endpoints/odata-form-service/data-document>`__ of this endpoint.

.. dropdown:: Request

  **Parameters**

  .. list-table::
      :widths: 25 75
      :class: schema-table
      
      
      * - projectId


        - number
        
          The numeric ID of the Project

          Example: ``16``
      * - xmlFormId


        - string
        
          The `xmlFormId` of the `Form` whose OData service you wish to access.

          Example: ``simple``
      * - table


        - string
        
          The name of the table to be returned. These names can be found in the output of the [Service Document](/reference/odata-endpoints/odata-form-service/service-document).

          Example: ``Submissions``
      * - %24skip

          *(query)*

        - number
        
          If supplied, the first `$skip` rows will be omitted from the results.

          Example: ``10``
      * - %24top

          *(query)*

        - number
        
          If supplied, only up to `$top` rows will be returned in the results.

          Example: ``5``
      * - %24count

          *(query)*

        - boolean
        
          If set to `true`, an `@odata.count` property will be added to the result indicating the total number of rows, ignoring the above paging parameters.

          Example: ``true``
      * - %24wkt

          *(query)*

        - boolean
        
          If set to `true`, geospatial data will be returned as Well-Known Text (WKT) strings rather than GeoJSON structures.

          Example: ``true``
      * - %24filter

          *(query)*

        - string
        
          If provided, will filter responses to those matching the query. Only [certain fields](/reference/odata-endpoints/odata-form-service/data-document) are available to reference. The operators `lt`, `le`, `eq`, `neq`, `ge`, `gt`, `not`, `and`, and `or` are supported, and the built-in functions `now`, `year`, `month`, `day`, `hour`, `minute`, `second`.

          Example: ``year(__system/submissionDate) lt year(now())``
      * - %24expand

          *(query)*

        - string
        
          Repetitions, which should get expanded. Currently, only `*` is implemented, which expands all repetitions.

          Example: ``*``
      * - %24select

          *(query)*

        - string
        
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


      .. list-table::
        :class: schema-table-wrap

        * - object


              

            .. list-table::
                :widths: 25 75
                :class: schema-table
                
                
                * - @odata.context


                  - string
                  
                    

                * - value


                  - array
                  
                    

                    Example: ``null``
                    
                      .. list-table::
                          :widths: 25 75
                          :class: schema-table
                          
                          
                          * - __id


                            - string
                            
                              

                          * - age


                            - number
                            
                              

                          * - meta


                            - object
                            
                              


                                
                              .. collapse:: expand
                                :class: nested-schema

                                .. list-table::
                                    :widths: 25 75
                                    :class: schema-table
                                    
                                    
                                    * - instanceID


                                      - string
                                      
                                        

                               
                          * - name


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
                  
                    

              
      

