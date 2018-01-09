Structure of ODK Collect Directory in Android File System
============================================================

After installation of ODK collect, odk directory would be created in the internal storage or external storage depending on the settings of your android device. The subdirectories are forms, instances, layers, metadata and settings respectively. The structure of the directory is explained below.

.. _directory-structure:

Directory structure
----------------------

::

 odk
 ├── forms
 │   ├── Sample-form-media
 │   └── Sample form.xml
 │  
 ├── instances
 │   └── formID_yyyy-mm-dd_hh-MM-ss
 │       └── formID_yyyy-mm-dd_hh-MM-ss.xml
 │  
 ├── layers
 │   └── Sample layer
 │        └── file.mbtiles
 │
 └── metadata  
 │	├── forms.db
 │	├── forms.db-journal
 │	├── instances.db
 │	└── instances.db-journal
 │ 
 ├── settings

.. _forms-directory:

:guilabel:`forms` Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/sample-form.*
  :alt: Image showing forms and Sample form-media directory
  :class: device-screen-vertical

The :file:`forms` folder contains forms, fetched from aggregate server. Forms designed by users do not have to be uploaded to aggregate server  for them to be used, they can be manually added to the forms directory. The :file:`Sample form-media` directory holds media files for image based forms and :file:`csv` files. CSV is a simple file format used to store tabular data, such as a spreadsheet or database.

.. tip::

  If your :file:`.csv` files contain very sensitive data, you may not want to upload that data to your server. Instead, you can upload a blank :file:`.csv` file as part of your form, then replace it with the real :file:`.csv` file by :doc:`loading that file <collect-adb>` onto each of your devices. You can load your :file:`.csv` file directly in media subdirectory associated with your form in this case Sample-form-media directory. That way, sensitive pre-loaded data never passes through the server.

.. _instances-directory:

:guilabel:`instances` Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/instances.*
  :alt: Image showing folder inside instance directory
  :class: device-screen-vertical
  
.. image:: /img/collect-structure/instances-form.*
  :alt: Image showing files inside formID_yyyy-mm-dd_hh-MM-ss directory
  :class: device-screen-vertical

Form instances are located in this directory. This directory will contain subdirectories with names of the form: :file:`formID_yyyy-mm-dd_hh-MM-ss`. Within each of these subdirectories are the form instance data file (named: :file:`formID_yyyy-mm-dd_hh-MM-ss.xml`), and associated data files for the images, audio clips and video clips linked with this form instance.

.. _layers-directory:

:guilabel:`layers` Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/sample-layer.*
  :alt: Image showing layer folder inside odk directory
  :class: device-screen-vertical
  
.. image:: /img/collect-structure/tiles.*
  :alt: Image showing tiles inside layer directory
  :class: device-screen-vertical

The :file:`layers` directory contains offline map tiles which are in the subdirectories of :file:`/odk/layers`, here the subdirectory is Sample layer. Under the Sample layer subdirectory is sample *MapBox mbtile* file.

.. _meta-directory:

:guilabel:`metadata` Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/metadata.*
  :alt: Image dhowing files inside metadata folder
  :class: device-screen-vertical

The :file:`metadata` directory contains databases, that track some high level file information about forms and instances such as status of all completed and incomplete form submissions on the phone. It conatins some checksum files that are used to ensure that the data within a file is complete and has not become corrupt. The state of the form instance (:formstate:`incomplete`, :formstate:`finalized`, :formstate:`sent`) is stored stored in :file:`instances.db` file and the status of the blank forms is stored in :file:`forms.db` file.
   
.. warning::

  The databases present in the :file:`metadata` folder are not automatically regenerated, merged, or combined. Therefore, tampering can cause unexpected problems. For example, if you delete :file:`instances.db`,  :formstate:`sent` forms would become available again for submission.

.. note::

  For information on the :file:`settings` directory, refer to 
   