ODK Services: Internal Details
=====================================

.. _services-internal-details:

.. _services-sync-detail:

Sync Details
------------------

Syncing has two phases. In the first phase, data tables are created on the device that correspond to the data tables on the server, and the form definitions and other files on your device are made to exactly match those available on the server (updating them as needed).

.. warning::

  If a data table on the device does not exist on the server, the configuration files and all associated forms for that table will be removed from the device. To prevent data loss, the table itself will not be deleted, but, by removing all of the configuration files for that table, the data will generally be unusable.

In the second phase, it synchronizes the contents of the local data tables with the contents on the server, including any row-level file attachments associated with individual records in the data table. Row-level file attachments are bundled and synced one row at a time.

Unlike ODK Collect, where individual forms can be added and removed at will, ODK Services and the ODK 2 tools are organized Data Management Applications consisting of a set of interrelated data tables and forms. All the forms and tables on the server collectively define the Data Management Application* and ODK Services ensures that the device conforms to that Data Management Application definition. You can operate multiple independent Data Management Applications on a single device by placing their files and forms under different application folders within the :file:`/sdcard/opendatakit/` folder. Each such application will publish to a different ODK Cloud Endpoint. This is a significant and powerful change from the ODK 1 mindset.

.. _services-managing-app-files:

Database Details
---------------------------------------------

ODK 2 data is stored in a `SQLite Database <http://sqlite.org/index.html>`_ running on the Android device. After a device synchronizes with the server, this database will fully match the schema and contents of the database running in the :doc:`cloud-endpoints-intro`.

Each Survey form instance will write to a row in the database. However, this mapping is not one-to-one: the form may not fill the entire row's columns and another form might fill other fields in the same row. Furthermore, sub-forms allow you to launch forms that write to other database rows. See :doc:`app-designer-intro` and :doc:`survey-intro` for more details.

Data tables and schema can also be created manually and used as a back-end for your Data Management Application using :doc:`tables-intro`.

At any point you can copy the local database on the Android device onto your desktop computer and inspect its contents and schema. If your application name is *default* then the database is stored in:

  :file:`/sdcard/opendatakit/default/data/webDb`

To inspect the database, use the :code:`adb pull` command (Google documentation is available `here <https://developer.android.com/studio/command-line/adb.html#copyfiles>`_). Then use a program such as `DB Browser for SQLite <http://sqlitebrowser.org/>`_ to view the database. Further instructions are available in the :ref:`Application Designer Guide <app-designer-common-tasks-pushing>`.


