Using ODK-X Suitcase
=====================

.. _suitcase-using:

.. _suitcase-using-gui:

Graphical Interface
-----------------------

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
----------------------------------

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

