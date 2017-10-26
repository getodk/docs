Form Submission API
======================

This standard defines the API for submitting data to an OpenRosa compliant server and receiving a response from the server about the submission. This API is designed to provide a base level of interoperability between OpenRosa clients and servers while enabling application-specific extensions as well.

.. _form-submission:

Form Submission
--------------------

OpenRosa servers must be able to receive XForms which are submitted by clients over HTTP. 

There are 3 major categories of requirements for submission which must be fulfilled: 

- channel
- content
- correctness.

.. _channel:

Channel
~~~~~~~~~~~~

OpenRosa servers MUST provide a URI capable of accepting HTTP POST Requests. Access controls, firewalls and geographic or networking restrictions MAY limit the origins and/or clients that can access the server.

The server MUST support HTTP 1.1 chunked transfer encoding for receiving the POST content. There is no minimum set of standards for timeouts, maximum content length, or other http configurations, but servers are encouraged to support lenient connections and the largest possible content size, since many of the connections will be from unreliable channels and in environments where splitting content up is impractical.

For maximum compatibility with J2ME clients, it is recommended that a server SHOULD NOT issue redirects. 

.. note::
  Using digest authentication and https when communicating with a server does not require any redirects --- you can have authentication and secure transport without redirects.

.. _content:

Content
~~~~~~~~~~

OpenRosa submissions (and responses) MUST provide headers conforming to the :doc:`OpenRosa Request standard <openrosa-http>`.

Successful server responses MUST include an ``X-OpenRosa-Accept-Content-Length`` header in addition to the :ref:`required OpenRosa Request response headers <openrosa-responses>`. The ``X-OpenRosa-Accept-Content-Length`` header specifies this server's recommended maximum size for a POST body, in bytes.

Servers SHOULD include this header in their error responses. However, clients MUST NOT rely on the presence of this header (or any OpenRosa header) in every error response.

.. note:: 
  Overly-large requests sent to Google AppEngine will be rejected prior to being sent to any server, and will therefore not contain this (or any) OpenRosa header.
  
OpenRosa submissions are POSTed to servers as a multipart MIME Envelope with at least 1 part --- the XML content of the form itself. Each of these parts should adhere to the following requirements

.. _mime-envelope:

MIME Envelope
"""""""""""""""
- Content Type: multipart/form-data
- Contains Exactly 1 XForm Part
- Contains 0 or More Additional Parts

.. _xform-part:

XForm Part
"""""""""""""

- Content Type: text/xml
- Name: xml_submission_file

.. _additional-parts:

Additional Parts
""""""""""""""""""

- Content Type: arbitrary
- Name: matches an appropriate element inside of the XForm Element's XML.

Servers MAY be more permissive than this specification (for example, allowing multipart/mixed for the mime envelope), but MUST be capable of recognizing and properly receiving submissions in this format.

.. _correctness:

Correctness
~~~~~~~~~~~~~~

The server MUST consume an entire HTTP POST in conformance with that protocol. Once a POST is received, the range and structure of the server's response is specified below.

.. _extended-transmission-considerations:

Extended Transmission Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the client is capable of negotiating authenticated and/or secure transmissions to the server, it is recommended that the client first attempt a ``HEAD`` request to the server to negotiate the authentication and channel security prior to the first ``POST`` of the data, regardless of any channel security stated in the ``<submission>`` element of the form. This ensures that submitted data is not inadvertently sent in the clear on that first request due to the client device possessing an out-of-date form definition with inaccurate ``<submission>`` content. 

Issuing a ``HEAD`` request first also reduces overall transmission bandwidth in instances where client authentication occurs. Most authentication handshake protocols require the complete re-``POST`` of the original request after the authentication is complete. By delaying the ``POST`` of the data until after the authentication has been negotiated on the ``HEAD`` request, overall transmission bandwidth is reduced.

The client, upon receiving the ``HEAD`` response, can check that the response contains the ``X-OpenRosa-Version`` header to indicate that the host is an OpenRosa server (as opposed to a network login screen or proxy page). In this way, the server can change the scheme from ``http`` to ``https`` or update the submission page URL without a wasted redirect during the actual submission process. The client can also use the value of the ``X-OpenRosa-Accept-Content-Length`` header to inform itself of how big a POST body should be sent to this server. ODK Collect also requires a 204 (No Content) status code in the HEAD response.

If a full ``POST`` of the form's XML submission and its additional parts (for example, captured image, audio or video clips) would exceed the size specified in the ``X-OpenRosa-Accept-Content-Length`` header (the *maxSize*), it is recommended that the client split the ``POST`` into multiple individual ``POST`` requests, each containing the form's XML submission and one or more additional parts such that each partial ``POST`` request is no greater than *maxSize*; if a single additional part is greater than *maxSize*, the ``POST`` should contain the form's XML submission and that single additional part. Regardless of whether the client observes and honors the ``X-OpenRosa-Accept-Content-Length`` header, a compliant server with give its best effort to accept submissions of any length.

The ``X-OpenRosa-Accept-Content-Length`` header is provided to avoid failures that may otherwise arise due to restrictions on the overall size of ``HTTP`` messages, or due to physical or virtual memory configurations of the server.

The form's XML submission is sent on each ``POST`` so that a client can avoid having any knowledge about the content of the files it is shipping around. Doing so also places the fewest restrictions on how the server handles the submission.

.. _rationale-for-sending-form-xml-submission:

Rationale for sending the form's XML submission
""""""""""""""""""""""""""""""""""""""""""""""""""

To avoid sending the form's XML submission, you would need to inspect the submission and send up its identifiying information. By avoiding inspection of the submission, a much simpler Ajax-enabled webpage could conform to this API.

On the server, having just the ``instanceID`` sent on subsequent ``POST`` requests might not be sufficient to process the request --- sending only this information would burden those server implementations with maintaining a mapping from the instanceID to the natural key for this data. Not sending the form's XML submission in subsequent POSTs biases against some server designs.

Finally, since most XML submission documents are smaller than 2K bytes, and if you have a 10M byte threshold for splitting a submission across multiple requests (a reasonable lower limit), you're burning only 0.02% of your bandwidth with the retransmission.

.. _server-response-format:

Server Response Format
--------------------------

The server response format will be XML formatted, and the response body will be an :ref:`OpenRosa Response <openrosa-responses>`.

Example response:

.. code-block:: xml

    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message>Form Received! You've submitted 5 forms today</message>
    </OpenRosaResponse>

If the server is RESTful, the server MAY return an ``HTTP`` URI (using the standard ``HTTP`` Location header) where the form can be found.

A form should not be assumed to be submitted until a ``201`` or ``202`` response code is received with an OpenRosaResponse envelope body.

.. _server-status-codes:

Server Status Codes
~~~~~~~~~~~~~~~~~~~~~

Server status codes will be the same as `standard http codes <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>`_. These use the general classification:

201-202
  Successfully received by server.

4XX
  Client Error

5XX
  Server Error

.. note:: 

  ``1XX`` (informational) and ``3XX`` (redirection) probably do not apply to these POSTs.
  
Some common interpretations of codes are below, but more could apply.

.. csv-table::
  :header: Code, HTTP Meaning, ODK Meaning	

  200, UNUSED, "Since the request is a post, a 200 response is not a sign of a successful submission. Many intermediate proxies will return a 200 response for gateway pages on WI-FI, etc, so receiving a 200 shouldn't be assumed to be meaningful."	
  201, Form Received, Everything went great. Thanks for submitting.
  202, Accepted, "We got and saved your data, but may not have fully processed it. You should not try to resubmit."	
  204, No Content, Status returned in response to a HEAD request.	
  401, Unauthorized, Client tried to post something it didn't have permission to post.
  403, Forbidden, You're not allowed to post to this server.	
  404, Not Found, "Unknown URI endpoint, domain, or other"	
  413, Request too large, The request body is too large for the server to process
  500, Internal Server Error, Something went awry on the server and we're not sure what it was
