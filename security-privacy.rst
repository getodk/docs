*********************
Security and Privacy
*********************

.. _security-and-privacy:

Below is an attempt to enumerate known security and privacy considerations of the ODK software.

1. License Terms
------------------

The ODK software is released under the `Apache 2 License <http://www.apache.org/licenses/LICENSE-2.0>`_.

All our installers, programs, and source code are provided AS-IS with no warranty or conditions, and without any liability obligations. See the license text for details.

2. Communication Channels
---------------------------

None of the downloadable ODK software transmits or communicates any information back to us and the software we have written does not have any mechanisms that might allow us to access or control your devices or systems.

There is always the possibility that hackers can discover and exploit deficiencies or bugs in our software or in 3rd-party libraries to access or control your devices or systems.

Our user website (`opendatakit <https://opendatakit.org/>`_.org) does not knowingly use cookies, does not knowingly contain 3rd party ads, and does not collect personally identifiable information from the general public.

3.3rd-party Software
----------------------

Our software uses a number of open-source 3rd-party libraries from well-known and/or reputable sources, and a few from obscure sources. We do not vet the security of those software libraries.

Your security people may want to review the libraries and source code on our `source code site <https://github.com/opendatakit/opendatakit/>`_.

4. ODK Aggregate Communications
---------------------------------

When setting up your own webserver to run :ref:`ODK Aggregate <aggregate-introduction>`, if you do not configure the server and :ref:`ODK Aggregate <aggregate-introduction>` to use an SSL certificate, a determined observer can see all data communicated to and from that server.

Only transmissions over an https:// connection are obscured from observers.

The definition of an encrypted form (:ref:`check here <encrypted-forms>`) is transmitted in plaintext (unencrypted) to the device. When a filled-in submission for an encrypted form is finalized, it is encrypted on the device and transmitted in encrypted form. While this may meet requirements for obscured transmission over unsecured http:// connections, unsecured connections still allow observers to alter the form definition to potentially remove the encryption, capture any filled-in forms, or potentially intercept and thereby prevent their transmission to your server.

5. ODK Aggregate Deployments to Google App Engine or Other Hosting Services
-------------------------------------------------------------------------------------------------------------

With all 3rd party hosting services, you should expect your data to be viewable by the support staff of the hosting service. Different services go to differing lengths to restrict access to, encrypt, and/or secure the data and communications within their data centers.

The form definition and associated media files of an encrypted form (:ref:`ODK see here <encrypted-forms>`) are stored on the server in plaintext (unencrypted). When a filled-in submission for an encrypted form is finalized, it is encrypted on the device and transmitted to the server in encrypted form, where it is stored. The secret key required for decryption is not stored on the server, thereby preventing anyone at the hosting service from seeing your filled-in form data and attachments unless they break the encryption.

See :ref:`Deployment Planning <deployment-planning>` for other considerations.

6. Encrypted Form Security
---------------------------

The form definition and associated media files of an :ref:`ODK encrypted form <encrypted-forms>` are stored on the server in plaintext (unencrypted). And are transmitted and stored on the devices in plaintext.

Prior to finalizing a filled-in form, all form data and attachments are stored in plaintext (unencrypted) on the device.

At the time a filled-in form is finalized, a random 256-bit encryption/decryption key is generated for that filled-in form using the SecureRandom number generator (`found here <https://docs.oracle.com/javase/7/docs/api/java/security/SecureRandom.html>`_). This ensures that every filled-in form has its own unique 256-bit encryption/decryption key.

The filled-in form data and all media attachments are then encrypted with that key using 256-bit AES Cipher Feedback (CFB) streaming-block encryption. Once encrypted, all plaintext files and attachments for that filled-in form are deleted.

The random key is then padded and encrypted using the RSA public key declared in the form definition (recommended to be 2048-bit) and the OAEPWithSHA256AndMGF1Padding algorithm. The resulting encrypted key is transmitted to the server along with the encrypted data and encrypted attachments. This submission includes a signature field that enables the software to detect tampering to any of the encrypted attachments or to the encrypted form data.

On the device, copies of the deleted (plaintext) filled-in form data and attachments may remain in the free-list of the SDCard until they are overwritten with new content.

On the server, if an observer were able to access your encrypted data, since each filled-in submission uses a different key, each submission would need to be cracked separately.

At this point in time, cracking AES encryption is viewed as impossible for all but the most advanced governmental agencies (e.g., the NSA).


7. ODK Aggregate Username Authentication
---------------------------------------------------------------------------

When authenticating :ref:`ODK Aggregate <aggregate-introduction>` usernames and passwords, the ODK tools use DigestAuth. This enables secure username/password authentication even while communicating with servers over http:// (when using DigestAuth, the password is not sent over the network).

An encoded form of the username's password is stored on the server. If that encoded value is stolen or revealed, it can allow others to log in and interact with the server as that user.


8. Google Gmail Authentication
-------------------------------

For authentication of Google accounts (Gmail or Google Apps), :ref:`ODK Aggregate <aggregate-introduction>` accepts OAuth2 tokens with rights to view a user's e-mail address (just the address - not the e-mail or user profile) as proof-of-identity.

*This is a very weak proof-of-identity*; every time you authorize Google to share your e-mail address with other sites or applications, those sites or applications have the permissions necessary to act on your behalf on :ref:`ODK Aggregate <aggregate-introduction>` (should they want to).

For this reason, it may be inappropriate to declare and grant Google e-mail addresses access to your site; this access is required for ODK 2.0 Sync functionality at rev 128 and earlier.


9. Identifying Information Transmission and Storage
------------------------------------------------------

During data submission, some identifying information is transmitted and stored on the server:

.. pull-quote::

  1. :ref:`ODK Collect <collect-introduction>` passes the deviceID of the device to the server during the submission process. (the HEAD request that initiates the submission is a URL of the form: .../submission?deviceID=imei%3A9117DD011813771 ). The :ref:`ODK Aggregate <aggregate-introduction>` server does not store this deviceID in any database tables, but it will generally be emitted into the webserver access log. This deviceID uniquely identifies the device from which the data is submitted. This can be useful when correlating events on the server with interactions from specific devices. Because this is logged, it is likely that a submission can be correlated with a device, and therefore a data collector.
  2. If :ref:`ODK Aggregate <aggregate-introduction>` is configured to require authentication (username / password or Google account) for submission (i.e., the Data Collector permission is NOT granted to the anonymousUser), then the username (or Google account) that authenticated is written into the audit fields of the data tables storing the submission. If the anonymousUser is granted Data Collector privileges, no authentication is performed, and "anonymousUser" is written into those fields. The content of these audit fields is not exposed in exported CSV files, ODK Briefcase data pulls, or published to downstream systems. However, because it is present in the database tables, you can definitely correlate this authenticated username or Google account with the submitted data.

While interacting with an :ref:`ODK Aggregate <aggregate-introduction>` website, any actions that require authentication and that modify the server settings, set of form definitions, filters, exports, publishers, or data tables, etc., will cause the authenticated username or Google account to be written into the audit fields of the database tables that are being updated. If these modifications result in delete actions being performed against a database table, then this authenticated username or Google account will be identified in the server log together with summary information on what was deleted.

10. ODK Collect
-----------------

We gather anonymous aggregate user behavior through Google Analytics. We use secure HTTPS communication to transfer this data off the device and the data are available to ODK's maintainers. Users may disable analytics in the settings of :ref:`ODK Collect <collect-introduction>`.

11. ODK Build
---------------

We require secure HTTPS connections to ODK Build. We gather anonymous aggregate user behavior through Google Analytics. We use secure HTTPS communication to transfer this data and the data are available to ODK's maintainers.

12. Online XLSForm tool
-------------------------

The online :ref:`XLSForm <xlsform-introduction>` tool does not use a secure connection. This means that your form definition files (both XLS and XML) are visible to a determined observer when submitted and downloaded from that site, as are any reported errors in the form.

Furthermore, the online XLSForm tool stores both your submitted XLS and the generated XML form for a period of time on its disk drive before being deleted (this is necessary for the operation of the tool).

The offline XLSForm tool and the ODK Validate tool, because they operate locally without any network communications, provide a secure alternative to the convenience of this online tool.

13. Websites
-------------

Our websites, downloads site, and the online XLSForm tool can or do use cookies and can or do log all interactions. We also utilize security software, spam-blocking, and web-analytics tools (e.g., Google Web Analytics) that may track visitors and their access patterns on our web properties.

14. Google Play Store
-----------------------

Downloads from the Google Play store are compiled into aggregated usage statistics on our management portal.

Crash reports you elect to send are provided to us as anonymous crash reports. By design, these do not contain survey field values or other device- or user- specific data.

15. Other Resources
---------------------

`Towards a Secure Framework for mHealth <http://bora.uib.no/handle/1956/10652/>`_. A Case Study in Mobile Data Collection Systems. Samson Hussien Gejibo. Ph.D. Dissertation at the University of Bergen, 2015.
