.. spelling::

  viewport

ODK Tables Web Pages
========================

.. _tables-web-pages:


Tables does not impose any structure to the HTML files a user may write. While the `odkDataIf` and `odkCommonIf` interfaces will always be injected into the WebKit, it is up to the user whether or not they make use of them (which generally means loading the `odkData` and `odkCommon` wrapper objects). A typical HTML file might be as follows:

.. code-block:: html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link href="../../../assets/css/your.css" type="text/css" rel="stylesheet" />
            <script type="text/javascript" src="../../../assets/commonDefinitions.js"></script>
            <script type="text/javascript" src="../tableSpecificDefinitions.js"></script>
            <script type="text/javascript" src="../../../../system/js/odkCommon.js"></script>
            <script type="text/javascript" src="../../../../system/js/odkData.js"></script>
            <script type="text/javascript" src="../../../../system/tables/js/odkTables.js"></script>
            <script type="text/javascript" src="../../../assets/libs/jquery-3.2.1.js"></script>
            <script type="text/javascript" src="../js/example.js"></script>
        </head>
        <body>
            <br>
            <a href="#" onclick="odkTables.openTableToListView(null,
              'visit',
              'plot_id = ?',
              [exampleResultSet.getRowId(0)],
              'config/tables/example/html/example_list.html');">Examples</a>
            <script>
                $(display);  // calls the display() function in example.js when document ready
            </script>
        </body>
    </html>

The :code:`DOCTYPE` header defines the file compliance level (in this case, HTML 4.01 Transitional).

The :code:`<head>` section sets the viewport and loads your CSS file. It will then typically load the 5 standard JavaScript files needed to support translations and the injected interfaces (:file:`commonDefinitions.js`, :file:`tableSpecificDefinitions.js`, :file:`odkCommon.js`, :file:`odkData.js`, and :file:`odkTables.js`). This example then loads the 3rd-party JavaScript libraries that the user needs and which the user has provided in the :file:`/config/assets/libs` directory and, finally, loads the JavaScript file they crafted that is specific to this web page (:file:`example.js`).

Once all the scripts and resources on the page have loaded, the script tag at the bottom of the :code:`<body>` section will invoke the display() function which was presumably specified in the user's :file:`example.js` file.

If the web page can launch other web pages or external applications, and if it cares about the status of those requests or needs to process the extras in the result intents returned from those requests (e.g., to interpret a barcode), then the user's :code:`display()` function, after it has initialized the page, should register a listener for action outcomes and call that listener once, directly, to process any outcome received prior to that registration (it will commonly be the case that these will have been received prior to the registration of this listener).

See the comments at the top of the :file:`odkCommon.js` file for details.
