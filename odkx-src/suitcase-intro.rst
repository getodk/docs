ODK-X Suitcase
=================

.. _suitcase-intro:

:dfn:`ODK-X Suitcase` is a cross-platform tool that allows updates and downloads of data on an ODK-X Cloud Endpoint from a personal computer.

Data downloaded from :doc:`cloud-endpoints-intro` are stored as spreadsheets in CSV format. This format is compatible with most spreadsheet software, for example :program:`Excel` or :program:`Numbers`. Once downloaded, the spreadsheets will be available for offline viewing.

Similarly, in order to add, delete, or update data, the data to be uploaded to an ODK-X Cloud Endpoint must be stored in a properly formatted CSV file.

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
  2. Double click the file to start. If that fails, try running the following, updating the path to where you downloaded download the latest :file:`ODK-X Suitcase.jar` file and replacing jar.jar with the filename of the downloaded :file:`ODK-X Suitcase.jar`.

    .. code-block:: console

      $ java -jar path/to/jar.jar

  3. Alternatively you can use command line operation. For help on the command line interface type:

    .. code-block:: console

      $ java -jar path/to/jar.jar --help


Using ODK-X Suitcase
------------------------------

.. _suitcase-using:

.. _suitcase-using-gui:

Graphical Interface
~~~~~~~~~~~~~~~~~~~~~~~~

The first screen when you open ODK-X Suitcase will ask for your ODK-X :guilabel:`Cloud Endpoint Address`, the :guilabel:`App ID`, and your :guilabel:`username` and :guilabel:`password`. If your ODK-X Cloud Endpoint allows for anonymous access then you can leave the :guilabel:`username` and :guilabel:`password` fields blank. Otherwise, please specify an ODK-X Cloud Endpoint username and password with sufficient permissions.

There are two options at the top of the graphical interface:
  - :guilabel:`Download`, to download existing data from the server
  - :guilabel:`Upload` to delete, upload new, or update data. :guilabel:`Upload` also includes an option to :guilabel:`Reset`  the server. Note that there is no warning or confirmation - if you press the :guilabel:`Reset` button it will reset the server.

When uploading, you need a correctly formatted CSV -- follow the instructions for :ref:`suitcase-csv` then modify the :guilabel:`Upload` field to that file path or click on the :guilabel:`...` button.

When downloading, you will need to specify the *table_id*. By default ODK-X Suitcase creates a :file:`Download` directory where the ODK-X Suitcase jar file is located and saves data in that directory in a *table_id* sub-folder with a corresponding *link_unformatted.csv* that has all of the data for that table downloaded from the server. To specify a different directory for ODK-X Suitcase to store downloaded data in, modify the :guilabel:`Save to` field or click on the :guilabel:`...` button.

ODK-X Suitcase provides three options to customize the CSV file download.

  - Download attachments:

    - If this option is selected, ODK-X Suitcase will download all attachments from the given table and the CSV generated will contain hyperlinks to the local files.
    - If this option is not selected, the CSV generated will contain hyperlink to the given ODK-X Cloud Endpoint.

  - Apply Scan formatting:

    - When this option is selected, ODK-X Suitcase will optimize the CSV by replacing certain columns added by ODK-X Scan.

  - Extra metadata columns

      - When this option is selected, two more columns will be included in the CSV, :th:`create_user` and :th:`last_update_user`.

.. tip::

    If your data are collected in a language that uses UTF-8 coding (for example, Arabic) you will need to add *-Dfile.encoding=UTF8* to the command line to open ODK-X Suitcase

.. _suitcase-using-cli:

Command Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODK-X Suitcase also provides a command line interface (CLI) that can be easily called by scripts and other programs. The CLI has the same features as the graphical user interface. CSV files produced by the two interfaces should also be identical.

The CLI can be used for downloads, updates, uploads, and resetting the server. For a list of all available options, open command prompt/power shell or terminal. Type the following, updating the path to where you downloaded download the latest :file:`ODK-X Suitcase.jar` file and replacing jar.jar with the filename of the downloaded :file:`ODK-X Suitcase.jar` .

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

.. _suitcase-csv:

Preparing your CSV for upload
------------------------------

In order to add, delete, or update data on the ODK-X Cloud Endpoint, you will need to create a CSV. You will need a separate CSV file for each *table_id* and these CSV files need to be named *table_id.csv*

The first column of the CSV must have the header :th:`operation`.
The value in the :th:`operation` column instructs ODK-X Suitcase how to handle that row.
The valid values for this :th:`operation` column are:  :th:`UPDATE`, :th:`FORCE_UPDATE`, :th:`NEW` and :th:`DELETE`

  - :th:`UPDATE` is used for updating data that already exists on the server. The update is done by matching on the :th:`_id` column. The :th:`_id` for an instance can be found by downloading the data using ODK-X suitcase.
  - :th:`FORCE_UPDATE` is used for updating data with a more aggressive strategy, if -:th:`UPDATE` failed.
  - :th:`NEW` is used for adding new rows (instances) to the server
  - :th:`DELETE` is used for deleting rows (instances) from the server by matching on the :th:`_id` column.

The CSV file must also include :th:`_id` and :th:`_form_id` columns. If you are updating particular variables in the server, the column headers for the variables you are updating will also need to be added with the edited values.

An example of a CSV to upload:

.. csv-table:: Example Spreadsheet
  :header: "operation", "_id", "_form_id","age"

  "DELETE","1201", "students"
  "UPDATE", "1423", "students", 17
  "NEW", "1533", "students"

You can then use either the command line or the graphical interface to upload the CSV and update your data on the ODK-X Cloud Endpoint.

.. tip::

    Using ODK-X Suitcase to download a CSV from your server and modifying that CSV can provide much of the structure and data you need for your CSV upload.
