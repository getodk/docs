Application Designer Directory Structure
============================================

.. _app-designer-dirs:

There are many folders and files within the :file:`Application Designer` directory. Fortunately, the only ones that are of interest for a non-software-developer are:

  - :file:`app/` - folder containing everything that will be pushed to the Android device.
  - :file:`Gruntfile.js` - contains the definitions of tasks that push files to the Android device, launch the :program:`Chrome` browser, and pull data and log files off the Android device.

Initially, you will only be concerned with the contents of your :file:`app/` directory -- the set of files that are placed on the Android device. As your sophistication grows, you may want to define your own :program:`grunt` tasks to automate repetitive steps in your deployment and device management processes. Adding or modifying tasks is beyond the scope of this document; please refer to the :program:`grunt` website (see :doc:`getting-started-2-architect` for the link to that site).

For completeness, here is the full list of the files and sub-folder in this directory. Again, you generally do not need to be concerned with the contents or specifics of any of these:

  - :file:`app/` - folder containing everything that will be pushed to the Android device.
  - :file:`devEnv/` - contains the HTML for the 6 tabs of the Application Designer.
  - :file:`grunttemplates/` - contains template files used by :program:`grunt` tasks.
  - :file:`node_modules/` - contains additional software installed by :program:`npm`, such as external tools used by :program:`grunt`.
  - :file:`scanFormDesigner/` - contains the Scan Form Designer tool.
  - :file:`test/` - contains tests of the computer-based simulated device environment.
  - :file:`themeGenerator/` - contains the HTML and JavaScript for the ODK ThemeGenerator CSS style and theme customization tool (accessed via the **Customize** tab).
  - :file:`xlsxconverter/` - contains the HTML and JavaScript for the ODK XLSX Converter tool that converts XLSX form definitions into formDef.json files (accessed via the **XLSX Converter** tab).
  - :file:`.bowerrc` - JSON configuration for the :program:`bower` tool.
  - :file:`.editorconfig` - when your text editors are configured to use it, enables consistent formatting to files across all contributors to your application design. See `EditorConfig <https://github.com/editorconfig/>`_.
  - :file:`.hgignore` - source code management configuration.
  - :file:`.hgtags` - source code management configuration.
  - :file:`.jshintrc` - configuration for JSHint - a program that flags suspicious usage in programs written in JavaScript.
  - :file:`bower.json` - used to control library management through :program:`bower`. By default, the :file:`.bowerrc` file has been configured to install these libraries in :file:`app/framework/libs/` so that you have access to them when your app is pushed to the phone.
  - :file:`deleteDefAndProp.sh` - MacOSX shell script to traverse the relevant parts of the :file:`app/` directory and delete the :file:`definition.csv` and :file:`properties.csv` files.
  - :file:`Gruntfile.js` - contains the definitions of tasks that push files to the Android device, launch the :program:`Chrome` browser, and pull data and log files off the Android device.
  - :file:`index.html` - the main HTML for the ODK Application Designer web page.
  - :file:`macGenConverter.js` - MacOSX command-line wrapper for the XLSX Converter tool (converts a single XLSX file piped into :program:`stdin` into a :file:`formDef.json` on :program:`stdOut`).
  - :file:`macGenFormDef.sh` - MacOSX shell script to traverse relevant parts of the :file:`app/` directory and generate :file:`formDef.json` files from XLSX files.
  - :file:`package.json` - configuration information for :program:`npm`.
  - :file:`README` - description linking back to this document.

.. _app-designer-dirs-app:

The :file:`app/` Folder
--------------------------

Everything in this folder mimics what is on the Android device. The directory looks as follows:

  - :file:`config` - user-defined configuration for your application.
  - :file:`data` - file attachments, and, on the device, the database.
  - :file:`output` - on the device, logging files and exported CSV and media files.
  - :file:`system` - files managed by the ODK tools (do not modify).

.. _app-designer-dirs-app-config:

The :file:`app/config/` Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This folder is synced to the device. It contains all of the form and table configuration files and initialization scripts. This is the sub-folder in which you will be primarily working.

This folder contains:

  - :file:`assets`
  - :file:`tables`

.. _app-designer-dirs-app-config-assets:

The :file:`app/config/assets/` Folder
""""""""""""""""""""""""""""""""""""""""""

  - :file:`css/` - contains the common CSS files for ODK Tables detail, list and home screens, and for app forms in ODK Survey (:file:`odk_survey.css`).
  - :file:`csv/` - contains the data files to be initially read and loaded into the ODK Survey and Tables databases.
  - :file:`fonts/` - contains the fonts used throughout the application.
  - :file:`framework/` - contains the :file:`framework.xlsx` and other relevant framework files.
  - :file:`img/` - contains the images used throughout the application.
  - :file:`js/` - contains JavaScript used by the ODK Tables custom home screen and/or the ODK Survey custom forms list
  - :file:`libs/` - contains the various libraries used throughout the application like jQuery and D3.
  - :file:`tables.init` - contains the initialization directives for which data (CSV) files should be loaded at initial start-up of the ODK tools.
  - :file:`index.html` - the HTML for the ODK Tables custom home screen, if it is enabled in the ODK Tables configuration settings.

.. _app-designer-dirs-app-config-tables:

The :file:`app/config/tables/` Folder
""""""""""""""""""""""""""""""""""""""""""

This folder has a predefined directory structure, but the content is entirely dependent upon the needs of your application.

The zip file for the ODK Application Designer populates this with all the subfolders used by each of the ODK Tables and the ODK Survey demonstration zip files. Ultimately, when you have completed your application design, this folder will contain none of these original folders but would instead contain only the folders which you have created.

.. note::

  Unlike ODK Collect, which stores each submission in a separate file, ODK Survey and ODK Tables store their combined collected submission data in data tables (one row per submission).

ODK Tables can display the contents of a table through one or more custom list views; it can display individual submissions through one or more custom detail views. Graphical views are simply list views in which the data is presented graphically using a library such as D3. All of these custom views are defined here.

ODK Survey, unlike ODK Collect, has the additional flexibility of supporting multiple forms to create, access and update data within a single common data table. This enables creating multi-stage workflows such as initial screenings and follow-ups, or registrations and status-updates (submission data can be editable, or not, based upon the form used at that workflow stage).

To accommodate these various capabilities, the :file:`tables` directory is structured such that individual data tables each have their own directory within the :file:`tables` directory. The table's *table_id* is the name of this sub-directory. When defining a new data table, begin with a form whose form id is the table id.

.. _app-designer-dirs-app-config-tables-id:

The :file:`app/config/tables/table_id/` Folder
'''''''''''''''''''''''''''''''''''''''''''''''

A canonical :file:`table_id` sub-folder contains:

  - :file:`definition.csv` - defines the data columns in this table. Generated when the *form_id* XLSX file underneath this :file:`table_id` is processed by the XLSX Converter.
  - :file:`properties.csv` - defines the appearance properties for this table. Example properties are the detail view HTML file name, the list view HTML file name, the default view type of the table, etc. Generated when the *form_id* XLSX file underneath this :file:`table_id` is processed by the XLSX Converter.
  - :file:`forms/` - contains directories for each ODK Survey form that manipulates this table. The names of these sub-directories are the *form_id* values of those forms. Within each sub-directory, there is a :file:`form_id.xlsx` file defining the ODK Survey form and the :file:`formDef.json` generated by the XLSX Converter when it processed that form definition file. If the form has form-specific images or media files, custom CSS, layouts, or prompt types, those files should reside within the form's sub-directory (nested sub-folders are permitted).
  - :file:`html/` the custom HTML files for the ODK Tables list and details views of the table's contents.
  - :file:`css/` - contains CSS files specific to this table.
  - :file:`js/` the JavaScript files needed for the custom ODK Tables HTML list and detail views (found in the :file:`html/` directory).

ODK Scan is currently split in where it stores its configuration for mark-sense forms. The current location for the ODK Scan templates is under :file:`app/config/scan/form_templates` directory.  This will likely change and lead to additional sub-directories here.

.. _app-designer-dirs-app-data:

The :file:`app/data/` Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ODK Application Designer stores user data in this directory. The database itself is in the :file:`webDb` directory. Any data files associated with a row in the database are stored within this folder under the :file:`tables/<table-id>/instances` directory.

.. _app-designer-dirs-app-output:

The :file:`app/output/` Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ODK Application Designer provides various :program:`grunt` tasks to pull files off the Android device. These files include JSON objects for debugging, exported CSVs, and the database itself. The :program:`grunt` tasks store these files here. There is also a logging directory which contains logs that are useful for debugging issues.

.. _app-designer-dirs-app-system:

The :file:`app/system/` Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This folder contains the files that the ODK tools depend upon and which are expected to be changed only when different versions of the ODK APKs are released.

.. warning::

  Files in this folder are managed by the ODK tools. If you change any of these files, the tools may detect the change and restore the file when they next start. The goal is that only the ODK core team should have to modify things in this folder. If you feel you need to modify anything in this directory, please contact us.

The general structure is:

  - :file:`js/` - contains JavaScript for the Java to JavaScript interfaces common to both ODK Table and ODK Survey.
  - :file:`libs/` - contains 3rd party JavaScript libraries used by ODK Tables and ODK Survey.
  - :file:`survey/` - contains JavaScript used by ODK Survey to render forms.
  - :file:`tables/` - contains JavaScript used by ODK Tables to render the custom home screen, list, detail, and graphical views created by the Application Designer.
  - :file:`tables.deleting` - information related to data deletion
  - :file:`tables.pending` - information related to pending data changes
  - :file:`index.html` - the generic HTML for all ODK Survey forms.

