Form List API
==============

This standard specifies how clients discover a list of available blank forms on a server.

.. _discovery-request:

Discovery Request
--------------------

The discovery request should be sent in compliance with the HTTP 1.1 protocol.

If a server will filter the set of forms based upon the user's identity, then the server should require that the user be authenticated through either the :doc:`openrosa-authentication` or through an alternative authentication mechanism. The server can then make use of the user's authenticated identity through those mechanisms to filter the set of forms to be returned.

The device will make a discovery request to a configured URI with a single query parameter, the ``deviceID``. The ``deviceID`` should be the same id as provided by the default population mechanism defined in the :doc:`openrosa-metadata`. The server may filter the set of forms returned using this information. 

.. warning::

  The ``deviceID`` is advisory information only, and is inherently not authoritative. Anyone can claim to have a given IMEI, for example.
  
Together, the authentication and ``deviceID`` enable a server to tailor the set of forms to both the user and the device (and therefore the device's capabilities).

.. _discovery-request-query-parameters:

Query Parameters
~~~~~~~~~~~~~~~~~~~

Optional query parameters MAY also be supplied:

- ``formID`` If specified, the server MUST return information for only this formID.
- ``verbose`` If specified with the value true, the server MAY include a ``<descriptionText/>`` or ``<descriptionUrl>`` element providing a longer description of an XForm.
- ``listAllVersions`` If specified, provides a listing of all hosted versions of each form (including the ``<version>`` element) in the response document (see below).

If not supplied or not present, the server MUST NOT include this optional information in its response.

.. _discovery-request-header:

Request Header
~~~~~~~~~~~~~~~~~~

Requests from the device SHOULD set the ``Accept-Language`` header to indicate the preferred language of the form name  

.. admonition:: Read More
 
  The ``Accept-Language`` HTTP header is documented here:
  
  http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4 
  
  and an article on its evolving use for determining locale is here:
  
  http://www.w3.org/International/questions/qa-accept-lang-locales

Aside from the query parameters, the structure of the server URI and whether the request is made over ``http`` or ``https``, is entirely implementor- and server- dependent. 

Compliant servers MUST NOT require additional query parameters on this request. 

Compliant devices MUST be able to handle arbitrary ``http`` and ``https`` URIs and must be able to :doc:`authenticate <openrosa-authentication>` with the server during this transaction, if required by the server.

.. _successful-response-document:

Successful Response Document
------------------------------

If accepted by the server, the server will respond with a ``Content-Type: text/xml; charset=utf-8`` response. An example of such a document is shown below:

.. code-block:: xml

  <?xml version='1.0' encoding='UTF-8' ?>
  <xforms xmlns="http://openrosa.org/xforms/xformsList">
    <xform>
      <formID>mydomain.org:formId</id>
      <name>Form with zero or more additional files</name>
      <version>1.1</version>
      <hash>md5:c28fc778a9291672badee04ac880a05d</hash>
      <descriptionText>A possibly very long description of the form</descriptionText>
      <downloadUrl>http://myhost.com/app/path/getMe/formIdA</downloadUrl>
      <manifestUrl>http://myothehost.com/app/path/getOtherStuff?formId=formIdA</namifestUrl>
    </xform>
    <xform>
      <formID>http://mydomain.org/uniqueFormXmlns</id>
      <name>Form without additional files</name>
      <version>v50 alpha</version>
      <hash>md5:c28fc778a9291672badee04ac770a05d</hash>
      <descriptionUrl>http://mysecondhost.com/a/description/getMe@formId=uniqueKey</descriptionUrl>
      <downloadUrl>http://mysecondhost.com/a/different/path/getMe@formId=uniqueKey</downloadUrl>
    </xform>
    <xforms-group>
       <groupID>someId</groupID>
       <name>Short name of grouping</name>
       <listUrl>http://whateverhost.com/other/path/forDownload?group=fido</listUrl>
       <descriptionText>Longer description of what is here</descriptionText>
       <descriptionUrl>http://morehost.com/description/link</descriptionUrl>
    </xforms-group>
  </xforms>

  
  
This document consists of:

- a top-level ``<xforms/>`` element in the ``http://openrosa.org/xforms/xformsList`` namespace enclosing,

  - zero or more ``<xform/>`` tags followed by 
  - zero or more ``<xforms-group>`` tags. 
  
Within each of the ``<xform/>`` tags, there must be exactly one of each of the following:

- ``<formID/>``
- ``<name/>``
- ``<version/>``
- ``<hash/>``
- ``<downloadUrl/>`` 
 
There may be zero or one 

- ``<descriptionText/>``
- ``<descriptionUrl/>``
- ``<manifestUrl/>``

Within each ``<xforms-group>`` tag, there must be exactly one of each of the following:

- ``<groupID/>``
- ``<name/>``
- ``<listUrl/>``

There may be zero or one 

- ``<descriptionText/>``
- ``<descriptionUrl/>``

The ``<xform/>`` tag provides information about a single form. The ``<xforms-group/>`` tag provides information about a group of forms; a further enumeration of the forms within that group can be obtained through the ``<listUrl/>`` of that group (which returns an ``<xforms/>`` document). Groups can be used to define sets of forms that a user may wish to download together (such as for clinical studies, for example).


.. _elements-within-xform:

Elements within ``<xform/>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``<formID/>`` The :ref:`form identity as defined in the metadata <form-identity>`.
-  ``<name/>`` The user-friendly display name of the form. The server may localize this name (translate it) based upon the ``Accept-Language:`` header on the incoming request. Devices **SHOULD** send this header and servers **MAY** return different name and description text based upon its value. The default behavior is to return the text within the ``<title>`` element of the XForm.
-  ``<version/>`` The :ref:`form version as defined in the metadata <form-version>` The device **MAY** use this to determine if its XForm definition is out of sync with the server (over time, the server may roll the current version forward or backward).
-  ``<hash/>`` The hash value of the form definition file available for download. The only hash values currently supported are MD5 hashes of the file contents; they are prefixed by ``md5:``. If the hash value identified in the form list differs from the hash value for a previously-downloaded form definition file, then the file should be re-fetched from the server.
-  ``<downloadUrl/>`` A fully formed URI for downloading the form to the device. It may be a valid http or https URI of any structure; the server may require authentication; the server may require a secure (https) channel, etc.
-  ``<manifestUrl/>`` A URI from which the device can obtain a manifest defining additional supporting objects and files. *Optional*
-  ``<descriptionText/>`` A detailed text explanation of the form. *Optional, only returned if* ``verbose=true``. 
-  ``<descriptionUrl/>`` A fully qualified URI pointing to a media (audio, video) description of the form. *Optional, only returned if* ``verbose=true``. 

.. tip::
  A media description of the form (audio or video) can be especially useful in low-literacy populations.


.. _elements-within-xform-group:
  
Elements within ``<xforms-group/>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``<groupID/>`` The unique id for this group. It is locale-invariant (in contrast to the ``<name/>`` element, below).
-  ``<name/>`` The user-friendly display name of the xforms group. The server may localize this name (translate it) based upon the ``Accept-Language:`` header on the incoming request. Devices **SHOULD** send this header and servers **MAY** return different name and description text based upon its value.
-  ``<listUrl/>`` A fully qualified URI for obtaining the ``<xforms/>`` document of this grouping of forms. (That is, the endpoint for the Form List API). It may be a valid http or https URI of any structure; the server may require authentication; the server may require a secure (https) channel, etc.
-  ``<descriptionText/>`` A detailed text explanation of the form group. *Optional, only returned if* ``verbose=true``. 
-  ``<descriptionUrl/>`` A fully qualified URI pointing to a media (audio, video) description of the form group. *Optional, only returned if* ``verbose=true``. 


.. note::

  -  The server **MAY** dynamically construct the download and manifest URLs based upon the user identity and device id.
  -  The manifest **MAY** include additional (implementation specific) elements and data. These MUST be dealt with gracefully (ignored) by the client if it does not know how to interpret these fields.

  
.. _manifest-document:

The Manifest Document
--------------------------

The structure of the manifest document returned by the manifest URI is as follows:

.. code-block:: xml

  <?xml version='1.0' encoding='UTF-8' ?>
  <manifest xmlns="http://openrosa.org/xforms/xformsManifest">
   <mediaFile>
    <filename>badger.png</filename>
    <hash>md5:c28fc778a9291672baddd04ac880a05d</hash>
    <downloadUrl>http://funk.appspot.com/binaryData?blobKey=%3A477e3</downloadUrl>
   </mediaFile>
   <mediaFile>
    <filename>path/to/agilefrog.png</filename>
    <hash>md5:9fd39ac868eccdc0c134b3b7a6a25eb7</hash>
    <downloadUrl>http://other.appspot.com/blobSource?foo=222</downloadUrl>
   </mediaFile>
  </manifest>

This document consists of:

- a top-level ``<manifest/>`` tag in the ``http://openrosa.org/xforms/xformsManifest`` namespace enclosing 

  - zero or more ``<mediaFile/>`` tags. 
  - Within each of the ``<mediaFile/>`` tags, there must be exactly one of each of the following:
  
    - ``<filename/>``
    - ``<hash/>``
    - ``<downloadUrl/>``

.. _elements-within-mediafile:

Elements within ``<mediaFile/>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``<filename/>`` The unique un-rooted file path for this media file. This un-rooted path must not start with a drive name or slash and must not contain relative path navigations (for example, ``.`` or ``..``).
-  ``<hash/>`` The hash value of the media file available for download. The only hash values currently supported are MD5 hashes of the file contents; they are prefixed by ``md5:``. If the hash value identified in the manifest differs from the hash value for a previously-downloaded media file, then the file should be re-fetched from the server.
-  ``<downloadUrl/>`` A fully qualified URI for downloading the media file to the device. It may be a valid http or https URI of any structure; the server may require authentication; the server may require a secure (https) channel, etc.
