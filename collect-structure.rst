***********************************************************
Structure of ODK Collect directory in Android file system
***********************************************************

After installation of ODK collect, you can try out the app by :ref:`downloading blank example forms <in-app-get-blank-forms>`, as soon as you download a blank form you would be able see odk directory in the internal storage or external storage depending on the settings of your android device. The structure of the directory is explained below.

.. _directory-structure:

Directory Structure
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
	├── forms.db
	├── forms.db-journal
	├── instances.db
	└── instances.db-journal
	
Inside :file:`ODK` directory, there are four subdirectories which are as follows:

.. image:: /img/collect-structure/directory.*
  :alt: Image showing folders inside odk directory
  :class: device-screen-vertical

.. _forms-directory:

forms Directory
~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/sample-form.*
  :alt: Image showing forms and Sample form-media directory
  :class: device-screen-vertical

:file:`forms` folder contains all the forms, fetched from aggregate server, also forms designed by users do not have to be uploaded to Aggregate for them to be used. They can be manually added to the forms directory. The :file:`Sample form-media` directory holds :file:`csv` files.

.. tip::

  If your :file:`.csv` files contain very sensitive data, you may not want to upload that data to your server. Instead, you can upload a blank :file:`.csv` file as part of your form, then replace it with the real :file:`.csv` file by hand-copying that file onto each of your devices. You can hand-copy your :file:`.csv` file in media subdirectory associated with your form in this case Sample-form-media directory. That way, sensitive pre-loaded data never passes through the server.

.. _instances-directory:

instances Directory
~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/instances.*
  :alt: Image showing folder inside instance directory
  :class: device-screen-vertical
  
.. image:: /img/collect-structure/instances-form.*
  :alt: Image showing files inside formID_yyyy-mm-dd_hh-MM-ss directory
  :class: device-screen-vertical

Submissions are located under this directory. This directory will contain subdirectories with names of the form: :file:`formID_yyyy-mm-dd_hh-MM-ss`. Within each of these subdirectories are the submission data file (named: :file:`formID_yyyy-mm-dd_hh-MM-ss.xml`),and associated data files for the images, audio clips, video clips, etc. linked with this submission.

.. _layers-directory:

layers Directory
~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/sample-layer.*
  :alt: Image showing layer folder inside odk directory
  :class: device-screen-vertical
  
.. image:: /img/collect-structure/tiles.*
  :alt: Image showing tiles inside layer directory
  :class: device-screen-vertical

:file:`layers` directory contains offline map tiles which are in the subdirectories of :file:`/odk/layers`, here the subdirectory is Sample layer. Under the Sample layer subdirectory is sample *MapBox mbtile* file.

.. _meta-directory:

metadata Directory
~~~~~~~~~~~~~~~~~~~~

.. image:: /img/collect-structure/metadata.*
  :alt: Image dhowing files inside metadata folder
  :class: device-screen-vertical

:file:`metadata` folder contains databases, that track some high level file information about forms and instances such as status of all completed and incomplete form submissions on the phone. It conatins some checksum files that are used to ensure that the data within a file is complete and has not become corrupt. The incomplete/finalized/sent status of the filled-in forms are stored in :file:`instances.db` file and the status of the blank forms is stored in :file:`forms.db` file.
   
.. warning::

 The databases present in the :file:`metadata` folder are not automatically regenerated, merged or combined, and if damaged can cause some problems, for example, if you delete :file:`instances.db` the sent forms would be available again for submission.
   