.. auto generated file - DO NOT MODIFY

Encryption
=======================================================================================================================

ODK Central supports two types of encryption:

1. The `old methodology <https://docs.getodk.org/encrypted-forms/>`__, where you generate an RSA keypair and use it with locally-downloaded encrypted data to decrypt submissions. We refer to these sorts of keys in this documentation as "self-supplied keys."

2. Managed Encryption, where Central will generate and store an RSA keypair for you, secured under a passphrase that Central does not save. The CSV export path can then decrypt all records on the fly given the passphrase.

Given the self-supplied key case, Central does not understand how to decrypt records, and the CSV export will export only metadata fields (and no binary attachments) for encrypted records. You may retrieve each data resource over the REST API and decrypt them yourself, or use ODK Briefcase to do this.

Managed Encryption is recommended for most people. The data is still encrypted "at rest" on the server, and the private key needed to decrypt the data is itself encrypted by the passphrase. Neither the passphrase nor the decrypted private key are ever stored; they are forgotten as soon as the server has finished the work at hand.

The relevant API operations are documented inline above; here we guide you through what exists from a high level.

To invoke Project Manage Encryption, you may use the web management interface, or you may `POST /projects/…/key </reference/project-management/projects/enabling-project-managed-encryption>`__.

To list all the encryption keys associated with the submissions on a given form, you can `GET /projects/…/forms/…/submissions/keys </reference/submissions/submissions/listing-encryption-keys>`__. This is particularly useful for obtaining the integer numeric ID associated with each key, which will be necessary to decrypt the records, as well as for obtaining reminder hints about each passphrase.

To perform decryption, you can `GET or POST /projects/…/forms/…/submissions.csv.zip </reference/submissions/submissions/exporting-form-submissions-to-csv>`__ with extra parameters to provide the necessary passphrases. If you are building a browser-based application, it is recommended that you ``POST``\  rather than ``GET``\ : please see the notes in the linked sections for additional details.

Note that the OData JSON API does not (presently) decrypt data. Any encrypted submissions will be returned only with basic metadata, like submission date and user.

