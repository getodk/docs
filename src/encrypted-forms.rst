*****************************
Encrypted Forms
*****************************

.. seealso:: ODK Central can :ref:`manage encryption for your projects <central-encryption-modes>`.

.. _encrypted-forms:

Overview
====================
Encrypted forms provide a mechanism to keep your data private even when using **http:** for communications (for example, when you do not have an **SSL certificate** or **https:** is not available). Encrypted forms may also enable Google App Engine deployments (and deployments using other web database services, such as, AWS) to comply with data privacy laws, eliminating the necessity for setting up your own servers to meet those requirements.

Encrypted forms apply asymmetric public key encryption at the time the form is finalized within ODK Collect. This encrypted form can then be submitted to a server. ODK Central provides `a managed encryption option <central-encryption>` which means a decrypted data file can securely be downloaded without using any other tool. Central self-managed encryption and other servers require using ODK Briefcase to download and decrypt the data. Briefcase, when supplied with the asymmetric private key (which Briefcase never stores), can then decrypt and export the form data as a CSV file for your use.

The finalized form's data (and media attachments) are encrypted before being submitted to a server and remain encrypted while stored on the server. When using Briefcase, the data remains encrypted as it is pulled, where it is again stored in encrypted form.

.. note::

  - A server cannot present or share the data with another service since the encryption obscures the entire contents of the form and the server never possesses the asymmetric key required to decrypt the form.
  - When using encrypted forms, the server serves only as a data aggregation point.

The non-encrypted data is available on the ODK Collect device during data collection and whenever a form is saved without marking it as complete. Once you mark a form as complete (finalize it), Collect will generate a random 256-bit symmetric key, encrypt the form contents and all attachments with this key, then construct a submission manifest which describes the encrypted submission and an asymmetric-key encryption of the symmetric key used for the encryption. This manifest is the "form" that is uploaded to a server, with the encrypted form contents and its encrypted attachments appearing as attachments to this submission manifest "form."

.. _security-concerns:

Security Concerns
====================
While ODK Collect attempts to remove all unencrypted copies of a finalized form and its attachments from the device, because ODK Collect uses third-party applications for image capture, etc., and because of the potential for Forced Close events during the clean-up process, we cannot guarantee that all copies will have been destroyed. Furthermore, because of the way an SD card writes and deletes information, there is a possibility of this data being recoverable from the free space on the SD card. Your organization should investigate the extra steps needed to ensure all data is deleted from the SD cards on your ODK Collect devices and should establish procedures to periodically wipe and reinstall those devices.

.. note::

  Encrypting a form ensures that the finalized form is not readable and is not tampered with. However, there is nothing preventing a malicious adversary from the wholesale replacement of a finalized form with falsified data or the synthesis and submission of extra data — these are not contingencies that encrypted forms seek to address.

.. _defining-encrypted-form:

Defining an Encrypted Form
===========================

In :doc:`XLSForm <xlsform>`, form encryption is enabled from the :ref:`settings sheet <settings-sheet>`. Encrypted forms must specify a :th:`public_key` on this worksheet. See below to learn how to generate a public-private key pair. It is also recommended to set an explicit :th:`submission_url` to make sure the submission goes to the intended destination. Central, this is the server URL configured in Collect for the App User followed by `/submission`. For Aggregate, this is the url with Aggregate.html replaced by `submission`.

.. rubric:: XLSForm --- configuring encryption

.. csv-table:: settings
  :header: form_id, version, submission_url, public_key

  my_form, 2024050301, https://my-server/submission, MIIBIjANB...JCwIDAQAB

.. _create-RSA-key:

Creating RSA Key pair
===========================

RSA public-private key pairs are generated using the OpenSSL software package. This is pre-installed on macOS and Linux but needs to be downloaded and installed on Windows.

.. _install-openssl:

Install OpenSSL (Windows only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Windows, download and run the OpenSSL installer appropriate for your system from OpenSSL for Windows. When it asks whether to copy the DLLs to the Windows system directory or to the :file:`/bin` directory, choose the :file:`/bin` directory (either will work, but this will minimize the pollution of the Windows system directory)

.. _construct-key:

Constructing the RSA Key Pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are on Windows, open a PowerShell or command prompt window. Change directories to the :file:`/bin` directory in the OpenSSL directory.

.. code-block:: doscon

  > cd C:\OpenSSL-Win32\bin

If you are on a Mac, open the terminal. Change directories to your Desktop.

.. code-block:: console

  $ cd ~/Desktop

.. _create-key:

Create a private key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following command will create a 2048-bit private key and write it to the :file:`MyPrivateKey.pem` file. This may complain about a missing configuration file. You can ignore this warning.

If you are on Windows, run:

.. code-block:: doscon

  > openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048

.. warning::

  **On Powershell**

    Check **$env:path** to be sure :file:`path\\OpenSSL-Win64\\bin` is in there.If it is not, run the following command in Powershell:

  .. code-block:: console

    > $env:path = $env:path + ";path to OpenSSL-Win64\bin"

If you are on a Mac, run:

.. code-block:: console

  $ openssl genrsa -out MyPrivateKey.pem 2048

.. _extract-key:

Extract a public key
~~~~~~~~~~~~~~~~~~~~~~~~~

Next, you need to extract the public key for this private key.

Run the following command:

.. code-block:: console

  openssl rsa -in MyPrivateKey.pem -inform PEM -out MyPublicKey.pem -outform PEM -pubout

This may also complain about a missing configuration file. You can ignore this warning.

.. _store-use-keys:

Storing and using the keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Move the :file:`MyPrivateKey.pem` file to a secure location. It does not have a password encoding it, so anyone can decrypt your data if they have access to this file. This is the private key file that you will give to ODK Briefcase when decrypting the data.

.. _update-keys:

Updating the public_key field in the XLSForm settings worksheet.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the :file:`MyPublicKey.pem` file and copy the resulting very-long string inside **----BEGIN/END----** lines and paste it into the **public_key field** in the XLSForm settings worksheet. This very-long string will become the *base64RsaPublicKey* attribute in the resulting encrypted form definition.

.. note::

  - You  need to be especially careful that this is ONLY the public key and not the contents of the original public-private key file (which would also appear to work but provide no security).


.. tip::

  - You can use Notepad (Windows) or TextEdit (Mac) to open :file:`MyPublicKey.pem`
  - Alternatively, you can use the command ``less MyPublicKey.pem`` to print the contents into the terminal and directly copy/paste from there.

.. seealso::

   - For reference, you can check out the `tutorial encrypted-XLSForm <https://docs.google.com/spreadsheets/d/1O2VW5dNxXeyr-V_GB3spS6QPX4rtqtt7ijqP_uZLU3I/edit#gid=390337726>`_. It is for viewing purposes only but you can make your own copy to edit it.

.. _encrypt-operations:

Operations
===========================

Operationally, you would add the form definition to the server identified in the ``<submission>`` tag's action attribute, and deploy everything using Collect, figure out how you want to implement a periodic SD Card wiping protocol for your devices, and you're done. Submissions will be encrypted when marked as complete. Once the data is on your server, use :doc:`Briefcase <briefcase-intro>` to download the encrypted submissions to your desktop computer, and then specify the private key PEM file when decrypting and generating the CSV files.

.. note::
  - ODK Central or ODK Aggregate will only hold the encrypted submission with no access to the private key
  - ODK Briefcase will emit the CSV with an extra final column that indicates whether the signature of the encrypted file was good or bad.  It would be bad if any of the attachments are missing or if there was tampering (other than the wholesale replacement of a submission, which can't be detected).
