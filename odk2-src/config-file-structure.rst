Application Configuration File Structure
==========================================

.. _config-structure:

A complimentary description is provided in the user-level documentation. The tool suite stores its configuration and data files on the SDCard in a directory structure rooted at `opendatakit`. The directories underneath this are *application names* and provide isolation of data and configuration from one user-defined application to the next. By default, if not specified, the *application name* is assumed to be `default`. Underneath this are 4 top-level directories::

    /opendatakit/{appName}
        /config
            /assets -- common shared configuration
                app.properties -- application properties
                index.html -- HTML home page for Tables (if configured)
                /css -- common css files
                /fonts -- common font files
                /img -- common image files
                /js -- common javascript files written by you
                /libs -- common 3rd party javascript libraries
                ... additional directories and files
                ...
                tables.init -- identifies what to process during initialization
                /csv/{tableId}[.{qualifier}].csv
                /csv/{tableId}/instances/{cleanrowId}/{row-level-attachment-files}
                ...
                /commonDefinitions.js -- shared translations (available in all webkits)
                /framework/frameworkDefinitions.js -- Survey template translations
                /framework/forms/framework/framework.xlsx -- XLSX framework form
                /framework/forms/framework/formDef.json   -- created from XLSX

            /tables
                /{tableId}/definition.csv  -- defines the data model of the table
                /{tableId}/properties.csv  -- properties of the tableId
                /{tableId}/forms/{formId}/{formId}.xlsx   -- XLSX form
                /{tableId}/forms/{formId}/formDef.json    -- created from XLSX
                ... optional additional form definition files
                /{tableId}/forms/{formId}/customTheme.css
                /{tableId}/forms/{formId}/customStyles.css
                /{tableId}/forms/{formId}/customPromptTypes.js
                /{tableId}/forms/{formId}/customScreeenTypes.js
                /{tableId}/forms/{formId}/{other-files}
                ... end optional additional form definition files
                /{tableId}/html/{optional-html-files}.html
                /{tableId}/js/{optional-js-files}.js
                ... any other directories and files you might want
                ...
        /data       - database and file attachments for this application
        /system     - internally managed javascript files and configuration
            /js/odkData.js
            /js/odkCommon.js
            /tables/js/odkTables.js -- wrapper for odkTables functionality
            /survey/js/odkSurvey.js -- wrapper for odkSurvey functionality
            ... the remaining files are not directly accessed
            /lib/...  -- 3rd party libraries used by Survey
            index.html -- Survey top-level HTML
            /js/mock/... -- mock interfaces used in App Designer
            /survey/js/... -- Survey javascript
            /survey/templates/... -- ODK Survey handlebars templates
        /output     - holds logging files, exported data
        /permanent  - available for device-only content (e.g., map tiles)

