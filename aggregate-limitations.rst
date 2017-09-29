Aggregate Limitations
========================

- Push of data to the server should be serialized. Within ODK Aggregate, there is a global mutex (`TaskLock` across all server instances, mediated by the datastore layer) in the server when inserting submissions. Having multiple push requests occurring simultaneously will cause them to block on the mutex, chewing up their 60-second request limit, as they get processed in single file no matter how many server instances are spun up.

- The 60-second request limit can be very commonly exceeded over low-bandwidth connections, and even text-only submissions can be impacted on satellite connections. That is why ODK Collect splits submissions into multiple 10MB submission requests. The timer starts upon receipt of the first byte, so a slow connection can account for a sizeable portion of those 60 seconds. Same applies for sending a response. The processing on the server is generally negligible in relation to the transmission times.

.. note::
   
   - The above two limitations, the global mutex and the in-memory copies/full-packet-assembly, are a result of implementing on top of AppEngine and its Datastore.
   - A server that used database transactions and that used streaming servlet 3.0 functionality would have less trouble with concurrent requests.


- Pull of data can be overlapped. However, for submissions with many media attachments, keep in mind that ODK Aggregate holds all media attachments in memory, then copies them into the HttpEntity, so this can consume a fair amount of memory (everything is held in memory at least twice). The same memory consumption applies on pushes / submission of forms. i.e., you probably want to manage how many media attachment download requests you have in play at the same time.

- Spinning up of copies of the frontend will incur faster quota usage on AppEngine. For that reason, the Aggregate configuration here specifies a 14-second queuing time threshold before a new instance is spun up. Only if at least one request is queued for longer than 14 seconds will a new instance be spun up, and then that new instance will take about 30 seconds to become live. Leaving a 15-second processing interval. This is why ODK Collect tried twice before failing a submit.


- Aggregate 0.9.x has a 1000-record limit to the number of records it can display (this is by design); it does, however, still retain all records i.e. it will hold as many records as you've uploaded and does not loose or ignore the 1001st record, etc; in general, any webserver will have a limit to what it can display interactively (at some point it will run out of memory or time out). 

.. tip::
  
  - On Aggregate 0.9.x, we provide the Briefcase applet (one of the links on the top row) to allow you to extract your data from the server into a local CSV file for local processing. That should retrieve all data within the server, and should work regardless of the number of submissions you have uploaded.
  - Aggregate 1.0 has far fewer display restrictions; the latest iteration, RC2, has implemented display paging on the submissions display page so you can page through all the submissions on the server, rather than just the first 1000 (and you get to set the page size, as well).


- ODK Aggregate 1.4.7 and earlier use a deprecated `backends` technology. Google may terminate support for that at any time with little warning. You should consider upgrading to 1.4.8.  

- Aggregate v1.4.15 fixed rev 210 sync protocol. Prior to this User permissions were incorrectly being computed and filtered. This prevented resetting the server with new content from the device (but syncing with existing content worked fine). The rev 210 sync protocol is incompatible with anything prior to rev 210.

- Prior to Aggregate v1.4.14, the capability of Basic Auth being configured and working was not exposed in the wizard-based installer/configurer; existing passwords needed to be changed before they can be used in a Basic Auth configuration.

.. note::

   Aggregate v1.4.14 added SHA-1 library to browser so that Basic Auth can now be configured and will now work.


   



