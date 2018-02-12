*****************************
Form Uploader
*****************************

Use ODK Form Uploader to easily upload a blank form and its media files to ODK Aggregate.

.. note::

  - Adding blank forms through the ODK Aggregate website is limited to an overall form and media size of 10MB; beyond that, you have to perform multiple uploads of the form definition file with different subsets of the media files in order to fully upload the blank form and its media attachments. 
  - If you have many media attachments or more than 10MB of media attachments, Form Uploader provides a quick and easy means to upload forms into ODK Aggregate.

.. _install-form-uploader:
 
Installation
====================

1. Make sure latest version of Java is installed on the computer you plan to use. If it is not, `download and install it <https://java.com/en/download/index.jsp>`_.
2. `Download <https://opendatakit.org/downloads/download-info/odk-formuploader/>`_ the latest version of ODK Form Uploader
3. Double click the file to start. If that fails, try running ``java -jar path_to_jar`` from the command line.

.. warning::

  - On Windows use ``java -jar "path_to_jar"``

.. _form-uploader-usage:

Usage
====================

1. Choose the form definition file (**.xml**) to upload.
2. For Installation and setup of ODK Aggregate, follow the steps mentioned :doc:`here <aggregate-install>`.
3. Specify the ODK Aggregate server. When specifying the ODK Aggregate server, either leave the username blank if the *anonymousUser* is granted Form Manager permissions, or specify  an ODK Aggregate user (Account Type '**ODK**') that has been granted Form Manager permissions. ODK Form Uploader does not work with Google accounts (Account Type '**Google**').
4. Specify the URL and Password.
5. Click :guilabel:`Upload Form`.

.. note::

  - ODK Form Uploader will look for a matching media directory and upload the form definition file and all media files to the ODK Aggregate server.
  - For example, when the form definition file is named :file:`myForm.xml`, that form definition and all files in the matching media directory :file:`myForm-media` will be uploaded. Note that the media directory should not contain any nested directories.

