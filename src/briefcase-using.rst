Using ODK Briefcase
======================

.. _pull-forms:

Pulling forms
-------------

To pull blank forms and submissions:

1. Open the :guilabel:`Pull` tab.

2. Select a pull source option from the :guilabel:`Pull from` drop-down, and click on the :guilabel:`Configure` button. Fill in any information needed to use the selected source.

    See more on the various sources below.

3. Select the forms you want to pull and click :guilabel:`Pull`.

    You can see the details of the operation by clicking on the |details-button| button.

4. You can cancel an ongoing pull operation at any point by clicking :guilabel:`Cancel`.

.. _pull-from-central:

Central server
~~~~~~~~~~~~~~

Briefcase will ask for the following information when choosing a Central server as the pull source:

- A :guilabel:`URL`
- A :guilabel:`Project ID` number
- An :guilabel:`Email` address
- A :guilabel:`Password`

.. warning::

  The :guilabel:`Start pull from last submission pulled` setting will have no effect while pulling forms from a Central server.

.. tip::

  See :doc:`Using Central with Briefcase <central-briefcase>` for more on the limitations of using Briefcase with Central.

.. _pull-from-aggregate:

Aggregate server
~~~~~~~~~~~~~~~~

Briefcase will ask for the following information when setting an Aggregate server as the pull source:

- A :guilabel:`URL`
- A :guilabel:`Username` (optional)
- A :guilabel:`Password` (optional)

.. _pull-from-collect:

Collect directory
~~~~~~~~~~~~~~~~~

Briefcase will ask for the directory on your computer where you have placed Collect's :file:`/odk` directory. We recommend following these steps to get a copy of Collect's :file:`/odk` directory into your computer:

1. Ensure all filled-in forms are finalized.

    If you have incomplete forms that you cannot finalize before pulling into Briefcase, delete them. If you need to keep them, make a copy of :ref:`your Collect directory <collect-directory>` before deleting them, and restore it after you are finished.

2. Using your device, create a zip archive of :ref:`your Collect directory <collect-directory>` with a file managing app such as `OI File Manager <https://play.google.com/store/apps/details?id=org.openintents.filemanager>`_.
3. Transfer the zip file to your local hard drive via a USB cable. You can also use the Share feature in your file manager to transfer it to a third-party service like Google Drive then download it to your local hard drive.
4. Once the zip file is on your local hard drive, unzip the file.

.. warning::

  When pulling from Collect, Briefcase pulls incomplete, saved, or finalized forms. After you pull forms into Briefcase, it is important that you delete them from Collect. Otherwise, the next time you pull, you will create duplicates.

.. tip::

  If you have Android developer tools installed, another option is to use :doc:`the Android Debug Bridge <collect-adb>` to pull filled forms:

  .. code-block:: console

      $ adb pull <collect-directory>/instances

.. _pull-form-definition:

Form definition
~~~~~~~~~~~~~~~

Briefcase will ask for the location of the blank form definition in your computer.

.. warning::

  Ensure that all attached media is available relative to the form definition file location.

.. tip::

  This enables a workflow to upload blank form definitions with many media attachments to Aggregate:

  #. Pull the form using the :guilabel:`Pull from` option.
  #. :ref:`Push the form to your Aggregate server <push-to-aggregate>`.


.. _push-forms:

Pushing forms
-------------

To push blank forms and submissions:

1. Open the :guilabel:`Push` tab.

2. Select a push target option from the :guilabel:`Push to` drop-down, and click on the :guilabel:`Configure` button. Fill in any information needed to use the selected source.

    See more on the various targets below.

3. Select the forms you want to push and click :guilabel:`Push`.

    You can see the details of the operation by clicking on the |details-button| button.

4. You can cancel an ongoing push operation at any point by clicking :guilabel:`Cancel`.

.. _push-to-central:

Central server
~~~~~~~~~~~~~~

Briefcase will ask for the following information when using a Central server as the push target:

- A :guilabel:`URL`
- A :guilabel:`Project ID` number
- An :guilabel:`Email` address
- A :guilabel:`Password`

.. warning::

  Pushing forms and submissions to Central currently has the following limitations:

  - Central will reject files that might have already been pushed before, even if they're different the second time.
  - Central will reject submissions belonging to a form version that it doesn't know about.

.. _push-to-aggregate:

Aggregate server
~~~~~~~~~~~~~~~~

Briefcase will ask for the following information when using an Aggregate server as the push source:

- A :guilabel:`URL`
- A :guilabel:`Username` (optional)
- A :guilabel:`Password` (optional)

.. _pull-push-settings:

Pull and push settings
----------------------

The settings for push and pull can be configured in the :guilabel:`Settings` tab:

- You can set a number of :guilabel:`Maximum simultaneous HTTP connections`. This can be increased to speed-up big pull operations or decreased to prevent saturating server bandwidth.

- You can enable :guilabel:`Start pull from last submission pulled` to save time and bandwidth by not pulling from the first submission.

  - This is only available for Aggregate servers at this moment and only benefits forms with more than 100 submissions.

  - You can clear the pull history and pull every submission by clicking on :guilabel:`Clear pull history`.

- You can enable :guilabel:`Remember passwords (unencrypted)`. This will enable a couple of features:

  - Briefcase will remember the pull sources and push targets you configure when they require user credentials. As a result, you won't need to configure them when launching Briefcase again.

  - Briefcase will let you enable the :guilabel:`Pull before export` option when exporting forms.

- You can enable :guilabel:`Use HTTP proxy` to route your HTTP requests through a proxy host. You will have to provide the proxy's :guilabel:`Host` (IP address or hostname), and the :guilabel:`Port` number.

.. _briefcase-export-to-csv:

Export forms to CSV
-------------------

#. Open the :guilabel:`Export` tab.
#. Click on the :guilabel:`Set Default Configuration` button.

  - Set an :guilabel:`Export directory`.
  - If exporting :doc:`encrypted-forms`, set the corresponding :guilabel:`PEM file location`. See :ref:`the Encrypted forms section <create-key>` for more information.
  - If you wish, select a :guilabel:`Start date` and an :guilabel:`End date` to specify a limited date range to export.
  - Toggle export parameters as needed:

    - :guilabel:`Export media files` enables exporting media files into the chosen export directory
    - :guilabel:`Overwrite existing files` enables overwriting form submission data in the output files. The default behavior is to append data.
    - :guilabel:`Split select multiples` enables splitting select multiple fields. Enabling this setting will create an extra output column per select choice, with a `1` if the choice was selected, or `0` otherwise. This only affects select fields without a choice filter and that are not from an external file (including widgets with search appearance).
    - :guilabel:`Include GeoJSON` enables generating a GeoJSON file with spatial data from all exported submissions.
    - :guilabel:`Remove group names` enables removing non-repeat group names from column names in the CSV.
    - :guilabel:`Pull before export` enables trying to pull the selected forms in case there are new form submissions to be exported.

#. Select the forms to export.

   If you are selecting and exporting more than one form, you may need to set individual export settings. To do this, click the gear icon (:guilabel:`⚙`) next to the form name.

#. Click :guilabel:`Export`.

.. tip::

 To import CSVs into Excel, you cannot download and open in one step; nor can you double-click on the CSV. You must open Excel and choose Import. If you are asked, the file origin or encoding is UTF-8.

Output files
~~~~~~~~~~~~

Briefcase will generate a different number of files and directories depending on the form's contents and the export configuration selected by the user. This can include, per form:

  - One main CSV file. For example: `Form Name.csv`
  - If the form includes any repeat group, one CSV file for each one of them. For example: `Form Name-repeat group name.csv`
  - If any submission includes binary attachments, they are copied to a `media` directory, relative to the export directory. For example: `media/1538040007350.jpg`
  - If the user enables the :guilabel:`Include GeoJSON export` configuration option, one GeoJSON file with spatial data. For example: `Form Name.geojson`
  - If the form includes audit metadata:

    - One CSV file with audit data from all submissions. For example: `Form Name - audit.csv`
    - One CSV audit file for each exported submission in the `media` directory, relative to the export directory. For example: `media/audit-uuid56880d5e-ee8a-4832-b69d-6dfdd526e2dc.csv`

.. csv-table:: Summary Table
  :header: Output file, How many?, Conditions, Path, Example

  Main CSV, One, , `./`, `Form Name.csv`
  Repeat CSV, One per repeat group, , `./`, `Form Name-repeat group name.csv`
  Binary attachment, As many as there are in submissions, , `./media`, `media/1538040007350.jpg`
  GeoJSON, One, The user enables `Include GeoJSON export`, `./`, `Form Name.geojson`
  Audit CSV, One, The form includes audit metadata, `./`, `Form Name - audit.csv`
  Individual audit CSV, One per submission, The form includes audit metadata, `./media`, `audit-uuid56880d5e-ee8a-4832-b69d-6dfdd526e2dc.csv`

There's more information available about the CSV file content structure and filename patterns in `the export format documentation`_.

.. _the export format documentation: https://github.com/getodk/briefcase/blob/master/docs/export-format.md

.. _cli-use:

Working with the command line
-----------------------------

Briefcase has a command line interface (CLI) to enable scripting of many of the actions that can be taken in the graphical user interface (GUI).

.. versionadded:: 1.4.4
  A CLI was added.

.. versionadded:: 1.9.0
  The CLI first takes an operation parameter and then modifiers to that operation

.. _briefcase-cli-help:

Getting CLI help
~~~~~~~~~~~~~~~~

To get help about the command line operation:

.. code-block:: console

  $ java -jar {path/to/briefcase-jar-file} --help

.. _pull-from-aggregate-cli:

Pulling forms from Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CLI flag: `-plla` or `--pull_aggregate`
- Usage:

  .. code-block:: console

      $ java -jar {path/to/briefcase-jar-file} --pull_aggregate --storage_directory {path/to/briefcase-storage-location} --aggregate_url {aggregate-url} --odk_username {username} --odk_password {password}

- Help section:

  .. code-block:: none

      Params for -plla operation:
        -p,--odk_password <arg>              ODK Password
        -sd,--storage_directory <arg>        Briefcase storage directory
        -u,--odk_username <arg>              ODK Username
        -url,--aggregate_url <arg>           Aggregate server URL
      Optional params for -plla operation:
        -id,--form_id <arg>                  Form ID
        -ii,--include_incomplete             Include incomplete submissions
        -mhc,--max_http_connections <arg>    Maximum simultaneous HTTP connections (defaults to 8)
        -sfd,--start_from_date <arg>         Start pull from date
        -sfl,--start_from_last               Start pull from last submission pulled

.. warning::

  This CLI operation **will pull all forms** Briefcase has permissions to if no `-id` parameter is defined.

.. _pull-from-collect-cli:

Pulling forms from Collect
~~~~~~~~~~~~~~~~~~~~~~~~~~

This command assumes you have already copied and unzipped the :file:`odk` file :ref:`as described here <pull-from-collect>`.

- CLI flag: `-pc` or `--pull_collect`
- Usage:

  .. code-block:: console

      $ java -jar {path/to/briefcase-jar-file} --pull_collect --storage_directory {path/to/briefcase-storage-location} --odk_directory {path/to/unzipped-odk-file}

- Help section:

  .. code-block:: none

      Params for -pc operation:
        -od,--odk_directory <arg>           ODK directory
        -sd,--storage_directory <arg>       Briefcase storage directory
      Optional params for -pc operation:
        -id,--form_id <arg>                 Form ID

.. warning::

  This CLI operation **will pull all forms** present on the :file:`odk` directory if no `-id` parameter is defined.

.. _push-to-aggregate-cli:

Pushing forms to Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~~

- CLI flag: `-psha` or `--push_aggregate`
- Usage:

  .. code-block:: console

      $ java -jar {path/to/briefcase-jar-file} --push_aggregate --form_id {form-id} --storage_directory {path/to/briefcase-storage-location} --aggregate_url {aggregate-url} --odk_username {username} --odk_password {password}

- Help section:

  .. code-block:: none

      Params for -psha operation:
        -id,--form_id <arg>                  Form ID
        -p,--odk_password <arg>              ODK Password
        -sd,--storage_directory <arg>        Briefcase storage directory
        -u,--odk_username <arg>              ODK Username
        -url,--aggregate_url <arg>           Aggregate server URL
      Optional params for -psha operation:
        -fsb,--force_send_blank              Force sending the blank form to the Aggregate instance
        -mhc,--max_http_connections <arg>    Maximum simultaneous HTTP connections (defaults to 8)

.. warning::

  This CLI operation will only update the blank form if it does not already exist, whereas the GUI will always update the form.

.. _export-to-csv-cli:

Exporting forms to CSV
~~~~~~~~~~~~~~~~~~~~~~

- CLI flag: `-e` or `--export`
- Usage:

  .. code-block:: console

    $ java -jar {path/to/briefcase-jar-file} --export --form_id {form-id} --storage_directory {path/to/briefcase-storage-location} --export_directory {path/to/output-directory} --export_filename {output-file-name.csv}

- Help section:

  .. code-block:: none

      Params for -e operation:
        -ed,--export_directory <arg>        Export directory
        -f,--export_filename <arg>          Filename for export operation
        -id,--form_id <arg>                 Form ID
        -sd,--storage_directory <arg>       Briefcase storage directory
      Optional params for -e operation:
        -em,--exclude_media_export          Exclude media in export
        -end,--export_end_date <arg>        Export end date (inclusive) (yyyy-MM-dd or yyyy/MM/dd)
        -ig,--include_geojson               Include a GeoJSON file with spatial data
        -oc,--overwrite_csv_export          Overwrite files during export
        -pb,--pull_before                   Pull before export
        -pf,--pem_file <arg>                PEM file for form decryption
        -rgn,--remove_group_names           Remove group names from column names
        -ssm,--split_select_multiples       Split select multiple fields
        -start,--export_start_date <arg>    Export start date (inclusive) (yyyy-MM-dd or yyyy/MM/dd)

.. _clear-saved-preferences:

Clear saved preferences
~~~~~~~~~~~~~~~~~~~~~~~

- CLI flag: `-c` or `--clear_prefs`
- Usage:

  .. code-block:: console

    $ java -jar {path/to/briefcase-jar-file} --clear_prefs

.. _briefcase-log-files:

Briefcase log files
-------------------

Briefcase creates a log file with warnings and errors that might be useful for troubleshooting.

.. _briefcase-default-log-file-location:

Default log file location
~~~~~~~~~~~~~~~~~~~~~~~~~

If something goes wrong while using Briefcase and you look for help, it's possible that you're asked to provide your log file.

The default location for the log file is the directory where you are when launching Briefcase, and the default filename is "briefcase.log"

Briefcase will create the log file on launch if it doesn't previously exist. Otherwise, it will append lines at the end of a pre-existing log file.

.. _briefcase-custom-log-configuration:

How to use a custom log configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optionally, you can use a custom log configuration file to override the default log settings on Briefcase.

First, you need to create a "logback.xml" file somewhere in your computer to contain your custom log configuration. This is a sample configuration file you can use as a template:

.. code-block:: xml

  <configuration>
    <appender name="ROLLINGFILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
      <file>briefcase.log</file>
      <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
        <fileNamePattern>briefcase.%d{yyyy-MM-dd}.log</fileNamePattern>
        <maxHistory>30</maxHistory>
        <totalSizeCap>100MB</totalSizeCap>
      </rollingPolicy>
      <encoder>
        <pattern>%d [%thread] %-5level %logger{36} - %msg%n</pattern>
      </encoder>
    </appender>

    <root level="info">
      <appender-ref ref="ROLLINGFILE" />
    </root>
  </configuration>


Check the full syntax of Logback configuration files `here`_.

  .. _here: https://logback.qos.ch/manual/configuration.html#syntax

You can set all sorts of new log configurations to adapt Briefcase to your needs:

 - Set a fixed log file location
 - Fine tune the log's verbosity by setting a different log level
 - Silence specific log lines while keeping others
 - Set a custom log format (see the `Encoders`_ chapter)
 - Set custom appenders, to define a file rolling policy (daily, by log file size, for example), for example (see the `Appenders`_ chapter)

  .. _Encoders: https://logback.qos.ch/manual/encoders.html
  .. _Appenders: https://logback.qos.ch/manual/appenders.html

Once you have your configuration file ready, you can use it by adding a `-Dlogging.config` argument when launching Briefcase:

.. code-block:: console

  $ java -Dlogging.config="{path/to/logback.xml}" -jar {path/to/briefcase-jar-file}

.. |details-button| image:: img/briefcase-using/details-button.png
   :align: top
