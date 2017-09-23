Metadata Scheme
=================

This document details the MetaData scheme to be used in an :terms:`XForm` intended for use with OpenRosa compliant servers. This metadata is used to ensure that critical or extremely useful data pertaining to XForms and submissions made by client devices is captured and stored.

There are two types of metadata in a form submission. 

 - Form metadata — Data about the identity and version of the XForm used to create the data being submitted. 
 - Data about the submission itself.

XForm Metadata
----------------------------

The metadata describing the form identity and versioning is provided as required attributes within the top-level group of the default model instance of the form. Two attributes are required:

``version``
~~~~~~~~~~~~

A string value indicating the version number of the form. 

- MUST support a string value (not a number), to indicate an increment. 
- SHOULD support any string schema. 
- MUST support arbitrary strings up to 249 characters
- SHOULD support arbitrary-length strings

The value of ``version`` MUST be incremented when any part of the form changes. 

If ``version`` is not present, it is handled as NULL. 
  
Identity  
~~~~~~~~~~

One of:

- ``id``
- ``xmlns``  
  
These values should be in the form of ``scheme:value``. 

If specified, the id value takes precedence over any explicit ``xmlns`` declaration. 

For ``id``, the implementor's registered domain name should be used as part of the scheme (for example:``opendatakit.org:widgetForm``). 

Compliant systems MUST support ``id`` or ``xmlns`` lengths up to 249 chars; ideally, servers SHOULD be able to support arbitrary lengths.

Location of Submission Metadata
-----------------------------------

The ``metadata`` block is located within the Model block of an XForm. It consists of a group of elements that describe the required information that should be included in every xml submission made to the server.
Required and Optional elements
There are two types of fields to be used in the metadata block: required and optional fields.
Required fields are used primarily to facilitate in the storage/sorting of submissions on the server and are useful during analysis of the data included in submissions.
Optional fields, as the name implies, are not required for server operation but are fields that are commonly used for data analysis and can also be used for administration of submissions. All optional fields are recommended to be consumable by OpenRosa Servers.
Required elements
The following field (element) MUST be present in the metablock:
<instanceID/> - See the 'ID Formatting' Section
Optional elements
The following is a list of elements that are generally useful to include in the metablock:
<timeStart/>- A timestamp* of when form entry was started
<timeEnd/> - A timestamp* of when form entry ended
<userID /> - An ID linking a specific user to the xml submission. See the 'ID Formatting' section.
<deviceID /> - The ID of the specific device used to generate the submission. See the 'ID Formatting' section.
<deprecatedID /> - the <instanceID/> of the submission for which this is a revision. This revision will have been given a newly generated <instanceID/> and this field is populated by the prior value. Server software can use this field to unify multiple revisions to a submission into a consolidated submission record.
* See 'Additional ID Constraints' section
ID Formatting
ID's, such as InstanceID, deprecatedID, userID and, deviceID, must follow the format: Scheme:value For example: <instanceID>uuid:97267f98c989461995c6e47800fcde5d</instanceID> or <userID>openid:http://www.google.com/profiles/odkuser</userID>
a scheme:value pair format is used to allow a wide variety of identification schemes to be used and so avoids 'lock-in' into one particular identification system. This format will also be useful in the event of merging large data sets from different organisations, as the scheme:value pair should be treated as an opaque string and will therefore ensure that very few collisions occur.
Recommended Prefixes for IDs Recommended Prefixes for <deviceID /> imei: mac: uuid: 
Recommended Prefixes for <userID /> mailto: openid: 
Recommended Prefixes for <instanceID /> (and <deprecatedID />) uuid:
If the above prefixes are not utilized for an ID, the implementor MUST use their registered domain name in the prefix. For example: <userID>user.datahq.org:someuser</userID>
Additional ID Constraints
The combined scheme:value keypair MUST be no longer than 249 characters (ie, so that varchar(249) can be used). Server SHOULD be able to support an arbitrary length ID, however.
Only ONE type of each ID can be sent to the server. That is, only one deviceID, one userID, one instanceID, and one deprecatedID, etc. (with one scheme:value pair in each) can be sent in a submission.
Timestamps MUST follow the format specified by ISO 8601 
Metadata is Defined in the Model Definition
The elements that are being submitted to the server MUST be defined in the model within a <meta/> tag having the http://openrosa.org/xforms namespace. I.e., the model must look something like this:
<h:head>
  <h:title>Metablock example</h:title>
  <meta jr:name="myexample"/>
    <model>
       <instance>
          <data xmlns:jr="http://openrosa.org/xforms"
                id="example.org:myFormId"
                version="1" >
            <jr:meta>
	  <jr:timeStart/>
       <jr:timeEnd/>
    <jr:instanceID/>
        </jr:meta>
....
  </data>
       </instance>
....
A<meta/> tag, if present, can appear anywhere in the model. Only the first tag appearing in the model (in the OpenRosa XForms namespace) is automatically populated by the device. I.e., if you have a complex form and want to transmit a composed subset of fields to your server, you will need to set up calculations to populate the nested fragment's <meta/> tag from the values in those in the first instance. Note also that the nested group being transmitted to the server will need to have attributes specifying the version and id so that the server can properly handle the submission.
If a <meta/> tag is present in the model, it MUST contain within it all the required fields, each appearing exactly once. The ordering of those fields can vary. If they are to be included in the form submission, the optional fields (<userID/>, <deviceID/> and <deprecatedID/>) defined above and any other optional fields MUST also be specified in this data block. i.e., all data elements that might be sent to the server must be explicitly specified in this data block.
The optional fields <userID/>, <deviceID/> and <deprecatedID/> may or may not be populated by the device; however, if they are present, the device SHOULD make a best effort at setting these values. NOTE: except for the <timeEnd/> field, these fields are expected to be set at the start of a form. There is no guarantee that the submitted form will have been completed entirely by the same user or even on the same device on which it was started.
NOTE: bind entries are not required for these values. If omitted, the data types are assumed to be string values. If you need the times to be treated as javarosa datetimes within your xform (when you, e.g., reference them in a calculation), you will need to include a bind entry identifying them as a datetime type.
Notes



Example
This is example is taken from a hypothetical xform and does not represent a submission ready to be submitted to the server.
<h:head>
<h:title>Metablock example</h:title>
<model>
           <instance>
<data xmlns:jr="http://openrosa.org/xforms"
                      xmlns="http://example.org/meta"
                      version="1" >
		      <jr:meta>
<jr:deviceID/>
<jr:timeStart/>
<jr:timeEnd/>
<jr:instanceID/>
</jr:meta>

....
</data>
</instance>
....

</h:head>
....

Below is an example of an instance meta block (as part of a full instance) ready to be submitted to the server.
<?xml version='1.0'?>
<data version="1" xmlns:jr="http://openrosa.org/xforms" xmlns="http://example.org/meta">
               <jr:meta>
	       <jr:deviceID>uuid:38DN0236SAKWJOJNQB3XJI9RW</jr:deviceID>
	       <jr:timeStart>2010-08-12T04:08:29.765-5:00</jr:timeStart>
	       <jr:timeEnd>2010-08-12T04:10:23.062-5:00</jr:timeEnd>
	       <jr:instanceID>uuid.dimagi.org:GEPSJLOGH13TY8L77066GEJJW</jr:instanceID>
                        <jr:userID>chwid.dimagi.org:Akende</jr:userID>
	       </jr:meta>

<!-- Example instance data follows -->
  <TextSection0_data>yes</TextSection0_data>
  <ENUMID_data>V -14-4</ENUMID_data>
  <TextSection1_data>yes</TextSection1_data>
  <PROV_data>Zambezia</PROV_data>
  <DIST_data>Milange</DIST_data>
  <DIST_COD_data>10</DIST_COD_data>
  <POST_data>Milange</POST_data>
  <POST_COD_data>1</POST_COD_data>
  <LOC_data>Milange</LOC_data>
  <LOCTYPE_data>Urban</LOCTYPE_data>
  <VILLAGE_data>Samora-Machel</VILLAGE_data>
  <VILlAGE_COD_data>2</VILlAGE_COD_data>
  <ENUM_data>66</ENUM_data>
  <SURVEYLOC_data>-16.9089355 36.75921051 635.0 4.0</SURVEYLOC_data>
  ...
</data>
~
