Using ODK Briefcase
======================

.. _pull-from-aggregate:

Pulling forms from Aggregate
-----------------------------

To download blank forms and completed form instances from an :doc:`Aggregate <aggregate-intro>` server:

#. Open the :guilabel:`Pull` tab.
#. Select *Aggregate* in the :guilabel:`Pull data from` drop-down.
#. Click the :guilabel:`Connect` button and enter the URL and login credentials for your Aggregate server.

   If you have anonymous login enabled on Aggregate, no login credentials are needed here.
   
   To connect to the `Aggregate Demo Server`_, the URL is https://opendatakit.appspot.com.
   
   .. _Aggregate Demo Server: https://opendatakit.appspot.com

#. Select the forms you want to download and click :guilabel:`Pull`. The selected forms will be pulled to :file:`ODK Briefcase Storage` on your local system.

   For each selected form, Briefcase will pull down:
   
   - The form definition file (that is, the blank XForm).
   - All media associated with the form.
   - Completed form instances.

   If you have previously pulled the form:
   
   - New instances will be downloaded to the same location as previously downloaded ones.
   - The form definition file and media files will not be re-copied.
   
   .. warning::

     If your local copy and the remote copy of the blank form definition file are different, the pull will be aborted.

     .. rubric:: Workaround
     
     If the form definition has changed, but the changes only affect the question text and do not alter the structure of the collected data (or change the form ID or version), you can:
     
     #. In :guilabel:`Settings`, temporarily change the location of :file:`ODK Briefcase Storage`.
     #. Pull data into to the new location.
     #. Manually copy the instances from the temporary location to your original storage location.
     #. Update :guilabel:`Settings` back to the original storage location.


.. _push-to-aggregate:

Pushing forms to Aggregate
--------------------------------

To upload blank forms and completed form instances to :doc:`Aggregate <aggregate-intro>`:

#. Open the :guilabel:`Push` tab.
#. Select *Aggregate* in the :guilabel:`Push data to` drop-down.
#. Click the :guilabel:`Connect` button and enter the URL and login credentials for your Aggregate server.

   If you have anonymous login enabled on Aggregate, no login credentials are needed here.
   
   To connect to the `Aggregate Demo Server`_, the URL is https://opendatakit.appspot.com.
   
   .. _Aggregate Demo Server: https://opendatakit.appspot.com

#. Select the forms you want to upload and click :guilabel:`Push`. The selected forms will be pushed from :file:`ODK Briefcase Storage` on your local system to the Aggregate server.

   For each selected form, Briefcase will upload:
   
   - If not on the server already:
   
     - The form definition file (that is, the blank XForm).
     - All media associated with the form.
   
   - Completed form instances.

   .. warning::

     If your local copy and the remote copy of the blank form definition file are different, the push will be aborted.
   
     .. rubric:: Workaround
     
     If the form definition has changed, but the changes only affect the question text and do not alter the structure of the collected data (or change the form ID or version), you can:
     
     #. In :guilabel:`Settings`, temporarily change the location of :file:`ODK Briefcase Storage`.
     #. Manually copy the form directory from your original storage location to the temporary location.
     #. Replace the local form definition file with a copy of the version from your Aggregate server.
     #. Push your form instances. 
     #. Update :guilabel:`Settings` back to the original storage location.
     
.. tip::
       
  .. Move this to Aggregate docs, or the Agg-v-Briefcase page.
       
  .. _aggregate-upgrade-with-briefcase:
       
  By pulling data into the local Briefcase Storage location and then pushing data up to an Aggregate instance, Briefcase provides a mechanism to transfer data across upgrade-incompatible versions of Aggregate.


.. _pull-from-collect:

Pulling forms from Collect
---------------------------

#. Ensure all filled-in forms are finalized. 

   If you have incomplete forms that you cannot finalize before pulling into Briefcase, delete them. If you need to keep them, make a copy of :file:`/sdcard/odk` before deleting them, and restore it after you are finished.

#. Create a zip archive of the entire :file:`odk` directory.

   .. tip::
   
     You'll need to use an app for this. 
     
     One option is `OI File Manager <https://play.google.com/store/apps/details?id=org.openintents.filemanager>`_.
     
#. Connect your Android device to your computer using a USB cable and choose to mount it as a Media device.
#. Copy the zip file you created from the Android device to your local hard drive.
#. Once it is copied onto your local hard drive, unzip the file.
#. In Briefcase, open the :guilabel:`Pull` tab.
#. Select *Custom Path to ODK Directory* in the :guilabel:`pull data from` drop-down.
#. Select the unzipped :file:`odk` folder.
#. Click :guilabel:`Pull`.
#. On the Android device, open ODK Collect and delete the filled-in forms.


   .. tip::
  
     - You can use the *Custom path to ODK Directory* any time you want to pull forms from custom location.
     - You can confirm that the forms have been successfully pulled into Briefcase by confirming a successful pull status or by verifying the data appearing in a :ref:`CSV export file <briefcase-export-to-csv>`.

.. warning::

  Briefcase cannot discriminate between duplicate form instances. After you pull completed forms into Briefcase, it is important that you delete them from Collect. Otherwise, the next time you pull in forms, you will create duplicates.

.. note:: 

  ODK Briefcase does not support pushing blank forms to ODK Collect. Instead, :ref:`manually load the forms on your ODK Collect device <loading-forms-directly>`.

.. _briefcase-export-to-csv:

Export forms to CSV
---------------------

#. Open the :guilabel:`Export` tab.
#. Choose an Export Location.
#. If exporting :doc:`encrypted-forms`, identify the location of your :ref:`PEM file <create-key>`.
#. If you wish, select Start and End dates to specify a limited date range to export.
#. Select the forms to export.

   If you are selecting and exporting more than one form,
   you may need to individualize your export settings
   (export location, PEM file, start date, end date).
   To do this,
   click the gear icon (:guilabel:`⚙`) next to the form name.
   
#. Click :guilabel:`Export`.


.. _cli-use:

Working with the command line
-------------------------------

.. versionadded:: 1.4.4
  A CLI was added.

.. versionadded:: 1.9.0
  The CLI first takes an operation parameter and then modifiers to that operation

.. _pull-from-aggregate-cli:
  
Pulling form data from Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ java -jar {path/to/briefcase-jar-file} --form_id {form-id} --storage_directory {path/to/briefcase-storage-location} --aggregate_url {aggregate-url} --odk_username {username} --odk_password {password}

.. _pull-from-collect-cli:
  
Pulling form data from Collect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This command assumes you have already copied and unzipped the :file:`odk` file :ref:`as described here <pull-from-collect>`.

.. code-block:: console

  $ java -jar {path/to/briefcase-jar-file} --form_id {form-id} --storage_directory {path/to/briefcase-storage-location} --odk_directory {path/to/unzipped-odk-file}

.. _export-to-csv-cli:
  
Exporting form data to CSV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

  $ java -jar {path/to/briefcase-jar-file} --form_id {form-id} --storage_directory {path/to/briefcase-storage-location} --export_directory {path/to/output-directory} --export_filename {output-file-name.csv}

.. _briefcase-cli-help:
  
Getting CLI help
~~~~~~~~~~~~~~~~~~~

To get help about the command line operation:

.. code-block:: console

  $ java -jar {path/to/briefcase-jar-file} --help
