Aggregate Limitations
========================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

This is a listing of known limitations and potential "gotchas" users of Aggregate may encounter.

Media held in memory
----------------------

When a form submission is uploaded, and when blank forms are downloaded, all the associated media files are held in memory at the same time, twice. For forms with a lot of media files, this can consume a lot of memory.

It is not absolutely critical to serialize form downloads, but you should probably manage how many form download requests are being handled concurrently, in order to avoid memory problems.

Uploading blank forms with media exceeding 10 MB
-------------------------------------------------

Adding blank forms through the ODK Aggregate website is limited to an overall form and media size of 10 MB. Beyond that, you have to perform multiple uploads of the form definition file with different subsets of the media files in order to fully upload the blank form and its media attachments.

An easier solution is to use :doc:`ODK Briefcase <briefcase-intro>`.

Issues with older versions of Aggregate
----------------------------------------

Aggregate < 1.4.8 used deprecated technology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate 1.4.7 and earlier use a deprecated backend technology. Google may terminate support for that at any time with little warning. You should consider upgrading.

Aggregate 1.4.15 changed sync protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate 1.4.15 fixed the ODK-X rev 210 sync protocol. Prior to this, user permissions were incorrectly being computed and filtered. This prevented resetting the server with new content from the device (but syncing with existing content worked fine). The rev 210 sync protocol is incompatible with anything prior to rev 210.

Basic Auth broken prior to Aggregate 1.4.14
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`openrosa` servers are :doc:`required to implement at least one authentication protocol <openrosa-authentication>` as outlined in `RFC2617 <https://datatracker.ietf.org/doc/html/rfc2617>`_.

- a subset of `RFC2617 Digest Authentication <https://tools.ietf.org/html/rfc2617#section-3>`_
- `Basic Authentication <https://tools.ietf.org/html/rfc2617#section-2>`_.

Aggregate v1.4.14 added an SHA-1 library so that Basic Auth is possible. Prior to this, Basic Auth was not possible.

.. note::

  Basic Auth is not exposed in the setup wizard. Additionally, it requires that default passwords be changed.

