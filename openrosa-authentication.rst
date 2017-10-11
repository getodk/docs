Authentication API
=====================

This standard specifies the Request and Response format through which OpenRosa compliant servers authorize HTTP transactions.

Overview
----------

This API provides a standardized means with which OpenRosa clients are authenticated with compliant servers.

OpenRosa compliant devices MUST support both:

- the subset of `RFC2617 Digest Authentication <https://tools.ietf.org/html/rfc2617#section-3>`_ defined below
- the `Basic Authentication mechanism also outlined in RFC2617 <https://tools.ietf.org/html/rfc2617#section-2>`_.

OpenRosa compliant servers MUST support at least one of either:

- the subset of `RFC2617 Digest Authentication <https://tools.ietf.org/html/rfc2617#section-3>`_ defined below
- the `Basic Authentication mechanism also outlined in RFC2617 <https://tools.ietf.org/html/rfc2617#section-2>`_.

We are following RFC2617 with additional OpenRosa compliance requirements defined in the implementation section below to ensure that the Digest Authentication implementations across devices do not compromise security and that they all implement a well-defined common subset of the RFC2617 Digest Authentication mechanism.

Data Security Considerations
-------------------------------

Any communication over HTTP (vs. HTTPS) can be observed by others and is susceptible to man-in-the-middle attacks (where a malicious intermediary inserts itself between the client and the server the client intended to contact). As a consequence, if communication is over HTTP, clients may be submitting their form data to a malicious intermediary. That intermediary will see the full contents of the form submission. Additionally, the intermediary may never forward the submission to the intended server --- the client can never be certain that the submitted data has been recorded on the intended server.

HTTPS requires that the server be configured with an SSL certificate issued by a signing authority. Man-in-the-middle attacks are possible over HTTPS if clients do not authenticate the server's SSL certificate (or, less commonly, if the client device or signing authority has been compromised).

OpenRosa compliant client devices MUST authenticate server certificates when establishing HTTPS channels to those servers.

Because client communications are often through unsecured hotspots, it is recommended that HTTPS (with the authentication of server certificates) be used for all communications.

Typical Interaction
--------------------

A typical transaction consists of the following steps.

1. The client asks for a resource that requires authentication but does not provide a user name and password. Typically this is because the user simply entered the address or followed a link to the page.

2. The server responds with the 401 response code, either requesting Digest Authentication and providing the authentication realm and a randomly-generated, single-use value called a nonce, or requesting Basic Authentication (in which case the server should also redirect and negotiate TLS channel security (https) if the client is not already communicating over https).

3. At this point, the client will present the authentication realm (typically a description of the computer or system being accessed) to the user and prompt for a user name and password. The user may decide to cancel at this point.

4. Once a user name and password have been supplied, the client re-sends the same request but adds an authentication header that includes the response code.

5. Assuming the username and password are valid,  the server accepts the authentication and the page is returned. If the user name is invalid and/or the password is incorrect, the server might return the `401` response code and the client would prompt the user again.

.. note::
  A client may already have the required user name and password without needing to prompt the user; for example, if they have previously been stored by a client.
  
For Basic Authentication, the "response" value is simply a base-64 compression of the user name concatenated with ":" and the plain-text password, as specified in RFC2617. 

.. warning:: 

  Anyone with a network sniffer could read this value, decompress it, and obtain the user name and password. Hence, it is critical that this information only be transmitted over HTTPS or some other secure transport.

  Even with HTTPS, sending this is not a highly secure practice.

For Digest Authentication, the "response" value is calculated in three steps, as follows. Where values are combined, they are delimited by colon symbols.

1. The MD5 hash of the combined user name, authentication realm and password is calculated. The result is referred to as HA1.
2. The MD5 hash of the combined method and digest URI is calculated, e.g. of "GET" and "/dir/index.html". The result is referred to as HA2.
3. The MD5 hash of the combined HA1 result, server nonce (nonce), request counter (nc), client nonce (cnonce), quality of protection code (qop) and HA2 result is calculated. The result, the user name and the cnonce are the "response" value provided by the client.

The Digest Authentication response value is thus sent in such a way that an adversary can extract the user name from the response, but cannot extract the password from the response. It can therefore be sent over an unsecured channel (for example, HTTP ).

.. note::

  Even with the more secure Digest Authentication, HTTPS is recommended. 

Implementation
-----------------

Servers which implement the Authorization API should follow the specifications provided below in order to be compliant with OpenRosa standards.

- All HTTP interactions MUST be HTTP 1.1
- Servers MUST conform to RFC2617 for returning one or more authentication schemes in their ``401`` challenge. These define the authentication interactions that the server is willing to accept from the client (for example: Basic, Digest)
- Any server interactions MAY be unauthenticated.
- Non-device (for example, browser) interactions for which the server requires authentication are NOT required to support Basic or the OpenRosa Restricted Digest authentication scheme. That is, they are allowed to only support Form-based or some other authentication scheme.
- Device-and-server interactions for which the server requires authentication MUST implement either Basic authentication or the OpenRosa Restricted Digest authentication scheme as detailed below. The server or device MAY additionally implement other authentication schemes.
- The device MUST make every effort to proactively supply an ``Authentication`` header line if the requested URI falls within the list of domain URIs covered by a previous authentication interaction. This is to minimize the number of authentication challenges.

Authentication
-----------------

Clients MUST NOT include authentication credentials in the URL to the server. That is, this syntax is strictly forbidden:

.. code-block:: none
  
  http://username:password@myhost.org/mypage

Basic Authentication
~~~~~~~~~~~~~~~~~~~~~~~~
    
Basic Authentication MUST NOT be performed over a non-secure (HTTP) connection.

Once the client is aware that basic authentication is required, it SHOULD proactively supply the basic authentication credentials on every secure request to the server, rather than wait for the server to reject the request with a ``401`` response.

.. _openrosa-restrcted-digest-authentication:

OpenRosa Restricted Digest Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
This is the `Digest Access Authentication Scheme (RFC 2617 Section 3) <https://tools.ietf.org/html/rfc2617#section-3>`_ with the following restrictions:
    
- algorithm --- server MUST omit or specify "MD5"
- domain --- server MUST specify to help device with proactive inclusion of Authenticate: header records.
- qop --- device MUST support: omitted and "auth"; server MAY request any of these.
- opaque --- device MUST return if supplied; server MAY supply this or omit it
- stale --- device MUST make every effort to not prompt the user for username and password if this is TRUE but instead recompute the key with previously cached values for the username and password.
- cnonce --- device SHOULD use a string representation of at least a 48-bit random value (a random UUID has 126-bit randomness) for the cnonce.
    
Digest Authentication Security Considerations
""""""""""""""""""""""""""""""""""""""""""""""""

Digest Authentication is based upon the MD5 hash algorithm which is now considered too weak for mainstream cryptographic uses. Digest Authentication remains viable only when the cnonce and nonce values are random and reasonably long. The use of longer random strings (e.g., random UUIDs have 126 bits of randomness) is critical for the continued use of this authentication mechanism.

Digest Authentication Calculations
"""""""""""""""""""""""""""""""""""

RFC2069

.. code-block:: none

  HA1 = MD5(A1) = MD5(username:realm:password)

  HA2 = MD5(A2) = MD5(method:digestURI)

  response = MD5(HA1:nonce:HA2)

RFC 2617 (HTTP Authentication: Basic and Digest Access Authentication)

.. code-block:: none

  HA1 = MD5(A1) = MD5(username:realm:password)

  if qop directive's value is "auth" or unspecified, then HA2 is:

    HA2 = MD5(A2) = MD5(method:digestURI)

  if qop directive's value is "auth-int" then HA2 is:

    HA2 = MD5(A2) = MD5(method:digestURI:MD5(entityBody))

  if qop directive's value is "auth" or "auth-int" then compute the response:

    response = MD5(HA1:nonce:nonceCount:clientNonce:qop:HA2)

  if qop directive is unspecified

    response = MD5(HA1:nonce:HA2)

(the above shows that when qop is not specified, the simpler RFC2069 standard is followed)

Digest Authentication Example Interaction
"""""""""""""""""""""""""""""""""""""""""""

No authentication
''''''''''''''''''''''''''''''''

Request:

.. code-block:: http

  GET /dir/index.html HTTP/1.0

Response:

.. code-block:: http

  HTTP/1.0 401 Unauthorized
  Server: HTTPd/0.9
  Date: Sun, 10 Apr 2005 20:26:47 GMT
  WWW-Authenticate: Digest realm="testrealm@host.com",
                         qop="auth,auth-int",
			 nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
			 opaque="5ccc069c403ebaf9f0171e9517f40e41"
  Content-Type: text/html
  Content-Length: 311

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd">
  
  <HTML>
    <HEAD>
      <TITLE>Error</TITLE>
      <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
    </HEAD>
    <BODY>
      <H1>401 Unauthorized.</H1>
    </BODY>
  </HTML>

Request with username and password
'''''''''''''''''''''''''''''''''''''

Request 
(username "Mufasa", password "Circle Of Life")

.. code-block:: http

  GET /dir/index.html HTTP/1.0
  Host: localhost
  Authorization: Digest username="Mufasa",
			realm="testrealm@host.com",
			nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
			uri="/dir/index.html",
			qop=auth,
			nc=00000001,
			cnonce="0a4f113b",
			response="6629fae49393a05397450978507c4ef1",
			opaque="5ccc069c403ebaf9f0171e9517f40e41"
			
Response

.. code-block:: http

  HTTP/1.0 200 OK
  Server: HTTPd/0.9
  Date: Sun, 10 Apr 2005 20:27:03 GMT
  Content-Type: text/html
  Content-Length: 7984
  
  
Example calculation of response using MD5

.. code-block:: none

  HA1 = MD5( "Mufasa:testrealm@host.com:Circle Of Life" )
      = 939e7578ed9e3c518a452acee763bce9

  HA2 = MD5( "GET:/dir/index.html" )
      = 39aff3a2bab6126f332b942af96d3366

  Response = MD5( "939e7578ed9e3c518a452acee763bce9:\
		   dcd98b7102dd2f0e8b11d0f600bfb0c093:\
		   00000001:0a4f113b:auth:\
		   39aff3a2bab6126f332b942af96d3366" )
	   = 6629fae49393a05397450978507c4ef1
