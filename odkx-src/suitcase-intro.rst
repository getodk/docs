ODK-X Suitcase
=================

.. _suitcase-intro:

:dfn:`ODK-X Suitcase` is a cross-platform tool that provides access to data on an ODK-X Cloud Endpoint from a personal computer.

Data downloaded from an :doc:`cloud-endpoints-intro` is stored as spreadsheets in CSV format. This format is compatible with most spreadsheet software, for example :program:`Excel` or :program:`Numbers`. Once downloaded, the spreadsheets will be available for offline viewing. Similarly, data to be uploaded to an ODK-X Cloud Endpoint must be stored in a properly formatted csv file.

.. _suitcase-install:

.. _suitcase-install-prereqs:

Prerequisites
-----------------------

  1. Set up an :doc:`cloud-endpoints-intro`

    .. note::

      Ensure you are using a compatible Cloud Endpoint from the same revision.

  2. Make sure :program:`Java` 7 or higher is installed on the computer you plan to use. If it is not, `download and install it <https://java.com/en/download/>`_.

.. _suitcase-intstall-app:

Installing ODK-X Suitcase
------------------------------

  1. Navigate to https://github.com/odk-x/suitcase/releases/latest and download the latest :file:`ODK-X Suitcase.jar` file.
  2. Double click the file to start. If that fails, try running:

    .. code-block:: console

      $ java -jar path/to/jar

  3. Alternatively you can use command line operation. For help on the command line interface type:

    .. code-block:: console

      $ java -jar path/to/jar --help

Using ODK-X Suitcase
------------------------------

.. _suitcase-using:

.. _suitcase-using-gui:

Graphical Interface
~~~~~~~~~~~~~~~~~~~~~~~~

If your ODK-X Cloud Endpoint allows for anonymous access then you can leave the :guilabel:`username` and :guilabel:`password` fields blank. Otherwise, please specify an ODK-X Cloud Endpoint username and password with sufficient permissions.

By default ODK-X Suitcase creates a :file:`Download` directory where the ODK-X Suitcase jar file is located and saves data in that directory. To specify a different directory for ODK-X Suitcase to store downloaded data in, click on the :guilabel:`...` button.

ODK-X Suitcase provides three options to customize the CSV file.

  - Download attachments:

    - If this option is selected, ODK-X Suitcase will download all attachments from the given table and the CSV generated will contain hyperlinks to the local files.
    - If this option is not selected, the CSV generated will contain hyperlink to the given ODK-X Cloud Endpoint.

  - Apply Scan formatting:

    - When this option is selected, ODK-X Suitcase will optimize the CSV by replacing certain columns added by ODK-X Scan.

  - Extra metadata columns

      - When this option is selected, two more columns will be included in the CSV, :th:`create_user` and :th:`last_update_user`.

.. _suitcase-using-cli:

Command Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODK-X Suitcase also provides a command line interface that can be easily called by scripts and other programs. The CLI has the same features as the graphical user interface. CSV files produced by the two interfaces should also be identical.

For a list of all available options, open command prompt/power shell or terminal. Type:

.. code-block:: console

  $ java -jar path/to/jar.jar --help

Combine the individual commands described in the help to perform the actions needed. Examples are as follows.

  - To download CSV of table *table_id* from app *default* with attachments as an anonymous user to the :file:`default` directory.

    .. code-block:: console

      $ java -jar suitcase.jar -download -a -cloudEndpointUrl "https://your-endpoint-server.com" -appId "default" -tableId "table_id"

  - To download CSV of table *table_id* from app *default* with attachments with username *user* and password *pass* to:file:` ~/Desktop`:

    .. code-block:: console

      $ java -jar suitcase.jar -download -a -cloudEndpointUrl "https://your-endpoint-server.com" -appId "default" -tableId "table_id" -username "user" -password "pass" -path "~/Desktop"

To script the CLI, write the commands you would like to execute in a scripting language (for example, Bash, Batch, Python, Ruby) and use a scheduler (such as Cron or Windows Task Scheduler) to schedule the tasks. To skip over ODK-X Suitcase's prompts to overwrite, pass :code:`-f` as an argument to ODK-X Suitcase.
