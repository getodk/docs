.. spelling::

  formIds
  tableId
  tableIds
  langCode

Internationalization
=========================

.. _internationalization:

.. contents:: :local:

Internationalization of web page content is achieved through the API exposed in the `odkCommon` object and the configuration contained in the XLSX files for the framework form and for the forms with formIds that match their tableIds::

    /opendatakit/{appName}/config
       /assets/framework/forms/framework/framework.xlsx
       /tables/{tableId}/forms/{tableId}/{tableId}.xlsx

Within the framework XLSX file, the `framework_translations` sheet defines the translations for all of the Survey form labels and prompts. On this page, the :th:`string_token` column contains the identifier for a particular label or prompt translation. The :th:`text.default` column provides the default translation for that label or prompt, and all subsequent :th:`text.{langCode}` columns provide translations for each of those specific language codes (e.g., {langCode} might be :tc:`es` for Spanish). If the label or prompt supports image or media enhancements, there will also be :th:`image.default` and :th:`image.{langCode}` or :th:`audio...` or :th:`video...` columns providing differing content for those.

Also within the framework XLSX file, there can be an optional `common_translations` sheet following the same format as the `framework_translations` sheet. This can be used to provide an application-wide set of translations.

Similarly, within the :file:`{tableId}.xlsx` file, there can be an optional `table_specific_translations` sheet that also follows the same format as the `framework_translations` sheet. This is used to provide a table-specific set of translations.

.. _internationalization-locales:

Defining the Available Locales
---------------------------------

The list of `{appName}`-wide locales and the default locale are specified on the framework form's `settings` sheet. Individual Survey forms may define additional translations, but those will be form-specific and are not available to Tables web pages.

Locales are defined in two steps.

First, the :tc:`survey` row under the :th:`setting_name` column on the `settings` sheet should have an explicit translation for each locale. Do this by creating columns labeled :th:`display.title.text.{langCode}` for each locale `{langCode}`. It is recommended that you use the Android 2-letter language codes. These are the  2-letter ISO 639-1 language codes, with the exception that :tc:`iw` is used for Hebrew, :tc:`ji` is used for Yiddish, and :tc:`in` is used for Indonesian. Using these 2-letter codes will enable use of the Android system locale for selection of the display language if the `{apppName}` is so configured.

Second, for each of these `{langCode}` values, create a row on the `settings` sheet with that `{langCode}` value under the :th:`setting_name` column. Then create columns labeled :th:`display.locale.text.{langCode}` across the top of the `settings` sheet. Provide translations for this language choice or, alternatively, define those translations on the `common_translations` sheet and reference the corresponding `string_token` under a single :th:`display.locale` column.

The default locale will be the top-most `{langCode}` locale that you specify on the `settings` sheet.

.. _internationalization-survey:

Referencing Translations in Survey XLSX Files
-----------------------------------------------------

To reference these translations within a question prompt in a survey, instead of specifying a value under a :th:`display.prompt.text` column, you would create a :th:`display.prompt` column and place the `string_token` from the translations sheet into that column, leaving any :th:`display.prompt....` columns empty.  The same applies for hint and title text.

And, finally, in all surveys, you can always provide on-the-spot translations for a prompt label by creating another column :th:`display.prompt.text.{langCode}` and specifying the translation for that language code directly on the survey sheet.

.. _internationalization-tables:

Referencing translations in Tables Web Pages
----------------------------------------------------

In order to access translations, your web page must load the :file:`commonDefinitions.js` file and the :file:`tableSpecificDefinitions.js` files. Within Tables web pages, you can then obtain the appropriate translation via:

.. code-block:: javascript

    var locale = odkCommon.getPreferredLocale();
    // obtain the text translation for the 'my_string_token' token.
    var translatedString = odkCommon.localizeText(locale, 'my_string_token');

Additional methods are available within `odkCommon` to test whether a translation exists, and to obtain a localized image, audio or video URL.  Refer to that file for the available methods.

.. _internationalization-locales-list:

Accessing the List of Locales and Default Locale
----------------------------------------------------

And finally, to access the list of locales, you can directly access that via:

.. code-block:: javascript

    window.odkCommonDefinitions._locales.value

This is an array of objects (no particular order). Each object has a :th:`display.locale` entry that can be translated to the current display language, and a :th:`name` which is the `{langCode}` for that locale.

And the default locale is available at:

.. code-block:: javascript

    window.odkCommonDefinitions._default_locale.value

.. _internationalization-xlsxconverter:

XLSXConverter Production of Translations
-------------------------------------------

After defining your translations on the framework and tableId XLSX files, the XLSXConverter must be run on these files to generate the translation files.

When the XLSXConverter processes the :file:`framework.xlsx` file and emits two files (in addition to the :file:`formDef.json`)::

    /opendatakit/{appName}/config
       /assets/commonDefinitions.js
       /assets/framework/frameworkDefinitions.js

Of these, the :file:`frameworkDefinitions.js` just contains a representation for the content of the `framework_translations` sheet.

The :file:`commonDefinitions.js` contains the content of the `common_translations` sheet and the list of locales and the default locale from the `settings` sheet (as described in the previous section)

When the XLSXConverter processes the :file:`{tableId}.xlsx` file, it emits three files (in addition to the :file:`formDef.json`)::

    /opendatakit/{appName}/config
       /tables/{tableId}/definition.csv -- data definition
       /tables/{tableId}/properties.csv -- table properties
       /tables/{tableId}/tableSpecificDefinitions.js

The last of these, :file:`tableSpecificDefinitions.js`, holds a representation for the content of the `table_specific_translations` sheet.

