Aggregate Limitations
========================

This is a listing of known limitations and potential "gotchas" users of Aggregate may encounter.

Pushing Data to Aggregate on Google App Engine
-------------------------------------------------

If Aggregate is :doc:`installed on Google App Engine <aggregate-app-engine>`, using the default datastore as described in our documentation, a combination of request time limits and datastore implementation create the following issues.

Simultaneous push requests will block each other and may time out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within ODK Aggregate, there is a global mutex (*TaskLock* across all server instances, mediated by the datastore layer) in the server when inserting submissions. Having multiple push requests occurring simultaneously will cause them to block on the mutex, chewing up their 60-second request limit, as they get processed in single file no matter how many server instances are spun up.

The solution to this is: **Serialize your push requests.**

Time limit may be exceeded on low-bandwidth connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 60-second request limit can be very commonly exceeded over low-bandwidth connections, and even text-only submissions can be impacted on satellite connections. That is why ODK Collect splits submissions into multiple 10MB submission requests. The timer starts upon receipt of the first byte, so a slow connection can account for a sizeable portion of those 60 seconds. The same applies for sending a response. The processing on the server is generally negligible in relation to the transmission times.

.. note::
   
   - The above two limitations, the global mutex and the in-memory copies/full-packet-assembly, are a result of implementing on top of AppEngine and its Datastore.
   - A server that used database transactions and that used streaming servlet 3.0 functionality would have less trouble with concurrent requests.

Media held in memory
----------------------

When a form submission is uploaded, and when blank forms are downloaded, all the associated media files are held in memory at the same time, twice. For forms with a lot of media files, this can consume a lot of memory.

The previous section already suggested serializing form submission uploads. This is not absolutely critical for form downloads, but you should probably manage how many form download requests are being handled concurrently, in order to avoid memory problems.

..  Spinning up of copies of the frontend will incur faster quota usage on AppEngine. For that reason, the Aggregate configuration here specifies a 14-second queuing time threshold before a new instance is spun up. Only if at least one request is queued for longer than 14 seconds will a new instance be spun up, and then that new instance will take about 30 seconds to become live. Leaving a 15-second processing interval. This is why ODK Collect tried twice before failing a submit.

Uploading blank forms with media exceeding 10MB
-------------------------------------------------

Adding blank forms through the ODK Aggregate website is limited to an overall form and media size of 10MB. Beyond that, you have to perform multiple uploads of the form definition file with different subsets of the media files in order to fully upload the blank form and its media attachments.

An easier solution is use :doc:`ODK Briefcase <briefcase-intro>`.

Issues with older version of Aggregate
----------------------------------------

Aggregate < 1.4.8 used deprecated technology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate 1.4.7 and earlier use a deprecated backend technology. Google may terminate support for that at any time with little warning. You should consider upgrading.

Aggregate 1.4.15 changed sync protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate 1.4.15 fixed the ODK 2.0 rev 210 sync protocol. Prior to this, user permissions were incorrectly being computed and filtered. This prevented resetting the server with new content from the device (but syncing with existing content worked fine). The rev 210 sync protocol is incompatible with anything prior to rev 210.

Basic Auth broken prior to Aggregate 1.4.14
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`openrosa` servers are :doc:`required to implement at least one authentication protocol <openrosa-authentication>` as outlined in `RFC2617 <the capability of Basic Auth>`_.

- a subset of `RFC2617 Digest Authentication <https://tools.ietf.org/html/rfc2617#section-3>`_
- `Basic Authentication <https://tools.ietf.org/html/rfc2617#section-2>`_.

Aggregate v1.4.14 added an SHA-1 library so that Basic Auth is possible. Prior to this, Basic Auth was not possible.

.. note:: 

  Basic Auth is not exposed in the setup wizard. Additionally, it requires that default passwords be changed.


   



