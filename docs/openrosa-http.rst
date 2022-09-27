HTTP Requests and Responses
================================

Much of OpenRosa communication comes in the form of HTTP requests and responses. In order to properly maintain appropriate formatting and compatibility over time, it is ideal for some information to be consistently provided on both sides of these interactions.

.. _openrosa-requests:

HTTP Requests
-----------------

HTTP requests (``GET``, ``POST``) should contain the following headers:

.. csv-table::
  :header: Header, Values, Required

  Accept-Language, The key for what language a response is expected in., No. Response acceptable in any locale
  X-OpenRosa-Version, 1.0, Yes
  Date, "The date on the device in format: `Mon, 14 Feb 2011 16:48:15 GMT`",	Yes
  
HTTP Requests may additionally specify whether the item count is to be included in the response envelope. This is done with a query parameter added to the URI.

.. csv-table::
  :header: Arg, Values, Required

  items, true|false, No. Defaults to false

.. _openrosa-responses:

HTTP Responses
-----------------

Servers should include the following headers in all responses.

.. csv-table::
  :header: Header, Values, Required

  Content-Language, `Two-letter language code (ISO 639-1) <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_, No. Recommended for internationalization. 
  X-OpenRosa-Version, 1.0, Yes
  Date, "The date on the server in the format: `Mon, 14 Feb 2011 16:48:15 GMT`", Yes

When a response is issued from an OpenRosa server, the format of the response payload will often be defined by the specific API (Form List, for instance). However, APIs which are fundamentally transactional (user registration, form submission, etc) all contain similar semantics. As such, they will utilize a shared XML Envelope of the format:

.. code-block:: none

  <OpenRosaResponse xmlns="http://openrosa.org/http/response" items=""> <!-- items: Optional number of how many payloads are included in this envelope -->
	   <message nature=""/>                                              <!-- 0 or 1: message payload to be displayed to the user. Nature is an optional tag to group messages by type -->
	   <!-- PAYLOADS HERE-->                                                              <!-- 0 or many: additional payloads to be parsed per platform-->
       </OpenRosaResponse>


For Example:

.. code-block:: xml

    <OpenRosaResponse xmlns="http://openrosa.org/http/response" items="3">
        <message nature="submit_success">Some message to be displayed to the user</message>
        <Registration xmlns="http://example.org/user/registration"/> <!-- optional -->
        <!--... Some platform specific response ...-->
    </OpenRosaResponse>
    
APIs using this response can then include their namespaced payload inside of the response. This response should be handled by the client the same way, regardless of the specific submission. That is, any time an OpenRosa response envelope is received, any of its payloads should be parsed properly.

Any responses included in the envelope that are unrecognized by the client should be ignored without error.

Since the server cannot receive confirmation that a response was successfully retrieved, any responses included in the envelope should be considered idempotent.

The message component of a response envelope should be returned (if possible) in the language specified by the ``Accept-Language`` header. The ``nature`` attribute of a message is an optional ID which can be used to categorize the type of a response. If the ``nature`` of two messages is identical in a bulk operation, for instance, the assumption is that only one of them need be presented to a user (presumably the newest).

As an example, if a server submits 4 xforms, and receives the responses

.. code-block:: xml

    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message nature="submit_success">Thanks, you've submitted 4 forms today </message>
  ...
    </OpenRosaResponse>
  ...
    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message nature="submit_success">Thanks, you've submitted 5 forms today </message>
  ...
    </OpenRosaResponse>
  ...
    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message nature="submit_user_registered">User 'paul' created succesfully!</message>
  ...
    </OpenRosaResponse>
  ...
    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message nature="submit_success">Thanks, you've submitted 6 forms today</message>
  ...
    </OpenRosaResponse>

A client could present a message like:

  **Bulk Submit Completed**
  
  - Thanks, you've submitted 6 forms today
  - User 'paul' created successfully!
