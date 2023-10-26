*********************
Security and Privacy
*********************

.. _security-and-privacy:

This document details known security and privacy considerations of the ODK software.

.. _license:

License 
-------

The ODK software is released under the `Apache 2 License`_.

.. _Apache 2 License: http://www.apache.org/licenses/LICENSE-2.0

All other artifacts (for example, the ODK website and this documentation) are released under the `Creative Commons Attribution 4.0 International License <cc-by-4>`_.

.. _cc-by-4: https://creativecommons.org/licenses/by/4.0/

All our installers, programs, source code, and documentation are provided AS-IS with no warranty or conditions, and without any liability obligations. See the license text for details.

.. _communication-channels:

Communication Channels
----------------------

Outside of usage analytics (typically opt-out) and crash reports (typically required), ODK software does not transmit or communicate any information (e.g., survey data) back to ODK's maintainers. When we do gather data, we default to anonymous or aggregate methods.

The software we have written does not have any mechanisms that might allow us to access or control your devices or systems.

There is always the possibility that hackers can discover and exploit deficiencies or bugs in our software or in 3rd-party libraries to access or control your devices or systems.

.. _3rd-party-software:

3rd-party Software
------------------

Our software uses a number of open-source 3rd-party libraries from well-known and/or reputable sources, and a few from obscure sources. We do not vet the security of those software libraries.

Your security staff may want to review the libraries and source code on `GitHub <https://github.com/getodk>`_.

.. _security-privacy-odk-websites:

Websites
--------

Our websites under the getodk.org domain use cookies and log all interactions. We also use web analytics tools (for example, Google Analytics) that may track visitors and their access patterns on our web properties.

.. _security-privacy-google-play-store:

Google Play Store
-----------------------

Downloads from the Google Play Store are compiled into aggregated usage statistics.

Crash reports you elect to send are provided to us anonymously. By design, these do not contain device or user specific data.

.. _security-privacy-odk-aggregate:

ODK Aggregate
--------------

.. _odk-aggregate-communications:

Communications
~~~~~~~~~~~~~~

When setting up your own web server to run ODK Aggregate, if you do not configure the server and ODK Aggregate to use an SSL certificate, a determined observer can see all data communicated to and from that server.

:ref:`encrypted-form-security` can prevent a determined observer from viewing encrypted form data being sent via insecure HTTP, but it cannot prevent the observer from silently removing encryption from form definitions and capturing any unencrypted form data that is then submitted.

Only transmissions over a secure HTTPS connection are obscured from observers and prevent tampering in transmission.

.. _odk-aggregate-deployments:

Google App Engine and other Hosting Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With all 3rd party hosting services, you should expect your data to be viewable by the support staff of the hosting service. Different services go to differing lengths to restrict access to, encrypt, and/or secure the data and communications within their data centers.

:ref:`encrypted-form-security` can prevent hosting services from viewing encrypted form data at rest, but cannot prevent the hosted service from silently removing encryption from form definitions and viewing any unencrypted form data that is then submitted.

See :doc:`aggregate-deployment-planning` for other considerations.

.. _odk-aggregate-username-authentication:

Username Authentication
~~~~~~~~~~~~~~~~~~~~~~~

When authenticating ODK Aggregate usernames and passwords, the ODK tools use DigestAuth. This enables secure username/password authentication even while communicating with servers over HTTP. When using DigestAuth, the password is not sent over the network.

An encoded form of the username's password is stored on the server. If that encoded value is stolen or revealed, it can allow others to log in and interact with the server as that user.

.. _security-privacy-odk-briefcase:

ODK Briefcase
-------------

We gather aggregate user behavior through Google Analytics and gather crash logs through Sentry. We use secure HTTPS communication to transfer this data to ODK's maintainers. Users may disable analytics in the settings of the application. Crash logging cannot be disabled.

.. _security-privacy-odk-collect:

ODK Collect
-----------

We gather aggregate user behavior through Google Analytics and gather crash logs through Google Firebase Crashlytics. We use secure HTTPS communication to transfer this data to ODK's maintainers. Users may disable analytics and crash logging in the settings of the application.

.. _security-privacy-xlsform-online:

XLSForm Online
--------------

We require secure HTTPS connections to XLSForm Online. We gather aggregate user behavior through Google Analytics. We use secure HTTPS communication to transfer this data to ODK's maintainers.

XLSForm Online stores both your submitted XLS and the generated XML form for a period of time on its disk drive before being deleted. This is necessary for the operation of the tool.


Cross-tool Concerns
-------------------

.. _encrypted-form-security:

Encrypted Form Security
~~~~~~~~~~~~~~~~~~~~~~~

The form definition and associated media files of an :ref:`ODK encrypted form <encrypted-forms>` are stored on the server in plaintext (unencrypted). The form definition and media files are transmitted as plaintext (but perhaps through a secure HTTPS connection) to client devices (e.g., an Android phone running ODK Collect) and stored in plaintext.

All form data (e.g., incomplete forms, saved forms) and media files are stored in plaintext on the client device until they are finalized. It is only once the form data is finalized that those files are encrypted.

At the time form data and media attachments are finalized, a random 256-bit encryption/decryption key is generated for that form data using the SecureRandom number generator (`found here <https://docs.oracle.com/javase/7/docs/api/java/security/SecureRandom.html>`_). This ensures that every finalized form has its own unique 256-bit encryption/decryption key.

The form data and media attachments are then encrypted with that key using 256-bit AES Cipher Feedback (CFB) streaming-block encryption. Once encrypted, all plaintext form data and attachments that were used in that process are deleted.

The random key is then padded and encrypted using the RSA public key declared in the form definition (recommended to be 2048-bit) and the OAEPWithSHA256AndMGF1Padding algorithm. The resulting encrypted key is transmitted to the server along with the encrypted data and encrypted attachments. This submission includes a signature field that enables the software to detect tampering to any of the encrypted attachments or to the encrypted form data.

On the device, copies of the deleted plaintext form data and attachments may remain in the free-list of the SD card until they are overwritten with new content.

On the server, if an observer were able to access your encrypted form data, since each form submission uses a different key, each submission would need to be cracked separately.

The secret key required for decryption is never stored on the server, thereby preventing anyone from seeing your form data and attachments unless they break the encryption.

Currently, cracking AES encryption is viewed as impossible for all but the most advanced governmental agencies (for example, the NSA).

.. _identifying-information-transmission-storage:

Identifying Information Transmission and Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During data submission, some identifying information is transmitted and stored on the server:

  - ODK Collect passes the deviceID of the device to the server during the submission process. The HEAD request that initiates the submission is a URL of the form: ``.../submission?deviceID=imei%3A9117DD011813771``. The ODK Aggregate server does not store this deviceID in any database tables, but it will generally be emitted into the webserver access log. This deviceID uniquely identifies the device from which the data is submitted. This can be useful when correlating events on the server with interactions from specific devices. Because this is logged, it is likely that a submission can be correlated with a device, and therefore a data collector.

  - If ODK Aggregate is configured to require authentication for submission (that is, if the Data Collector permission is NOT granted to the anonymousUser), then the username that authenticated is written into the audit fields of the data tables storing the submission. If the anonymousUser is granted Data Collector privileges, no authentication is performed, and anonymousUser is written into those fields. The content of these audit fields is not exposed in exported CSV files, ODK Briefcase data pulls, or published to downstream systems. However, because it is present in the database tables, you can definitely correlate this authenticated username with the submitted data.

While interacting with an ODK Aggregate website, any actions that require authentication and that modify the server settings, set of form definitions, filters, exports, publishers, or data tables, will cause the authenticated username to be written into the audit fields of the database tables that are being updated. If these modifications result in delete actions being performed against a database table, then this authenticated username will be identified in the server log together with summary information on what was deleted.

----

.. seealso::

  `Towards a Secure Framework for mHealth <http://bora.uib.no/handle/1956/10652/>`_. 
    A Case Study in Mobile Data Collection Systems. Samson Hussien Gejibo. Ph.D. Dissertation at the University of Bergen, 2015.
