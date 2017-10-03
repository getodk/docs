Form List API
==============

This standard specifies how clients discover a list of available blank forms on a server.

Discovery Request
--------------------

The discovery request should be sent in compliance with the HTTP 1.1 protocol.

If a server will filter the set of forms based upon the user's identity, then the server should require that the user be authenticated through either the :doc:`openrosa-authentication` or through an alternative authentication mechanism. The server can then make use of the user's authenticated identity through those mechanisms to filter the set of forms to be returned.

The device will make a discovery request to a configured URI with a single query parameter, the ``deviceID``. The ``deviceID`` should be the same id as provided by the default population mechanism defined in the :doc:`openrosa-metadata`. The server may filter the set of forms returned using this information. 

.. warning::

  The ``deviceID`` is advisory information only, and is inherently not authoritative. Anyone can claim to have a given IMEI, for example.
  
Together, the authentication and ``deviceID`` enable a server to tailor the set of forms to both the user and the device (and therefore the device's capabilities).

Query Parameters
~~~~~~~~~~~~~~~~~~~

Optional query parameters MAY also be supplied:

- ``formID`` If specified, the server MUST return information for only this formID.
- ``verbose`` If specified with the value true, the server MAY include a ``<descriptionText/>`` or ``<descriptionUrl>`` element providing a longer description of an XForm.
- ``listAllVersions`` If specified, provides a listing of all hosted versions of each form (including the ``<version>`` element) in the response document (see below).

If not supplied or not present, the server MUST NOT include this optional information in its response.

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

