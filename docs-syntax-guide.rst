Writing in Sphinx
====================

The ODK documentation is built using `Sphinx <http://sphinx-doc.org>`_, a static-site generator designed to create structured, semantic, and internally consistent documentation. Source documents are written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, a semantic, extensible markup syntax similar to Markdown.

- `reStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_ — Introduction to reStructuredText

  - `reStructuredText Quick Reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
  - `reStrcuturedTest 1-page cheat sheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_

- `Sphinx Markup <http://www.sphinx-doc.org/en/stable/markup/index.html>`_ — Detailed guide to Sphinx's markup concepts and reStructuredText extensions

.. note::

  Sphinx and reStructuredText can be very flexible. For the sake of consistency and maintainability, this guide is *highly opinionated* about how documentation source files are organized and marked up.


.. _indentation:

Indentation
--------------

Indentation is meaningful in Sphinx and reStructured text.

- Use **spaces, not tabs**.
- Indent **two spaces**.

.. _doc-files:

Documentation Files
----------------------

Sphinx document files have the ``.rst`` extension. File names should be all lowercase and use hyphens (not underscores or spaces) as word separators.

Normally, the title of the page should be the first line of the file, followed by the line of equal-signs.

.. code-block:: rst

  Title of Page
  ================

  Page content is here...

You can also wrap the title in two lines of asterisks.

.. code-block:: rst

  *******************
  Title of Page
  *******************

  Page content here.

The asterisks style is useful when you are combining several existing documents (and don't want to change every subsection headline) or when you are working on a document that might be split into separate documents in the future.

See :ref:`sections-titles` for more details.

.. _custom-css:

Custom CSS
------------

You can add custom styling in :file:`_static/css/custom.css`. Whenever you add any custom styling, add short comments describing the changes made and the PR number in which the changes were made.

For example:

.. code-block:: css

  /* Example css PR #xyx */

  div[class^='example'] {
    color: black;
  }

There are various sections in the :file:`custom.css` file:

- Styling for rst roles and directives
- Responsive css
- Styling for JS implementation
- Utility classes

Each of these sections are enclosed between start and end comments. Make sure you add your code to the relevant section. If you don't find any section relevant, add a new section and add your code there.

For example:

.. code-block:: css

  /* New section starts */

  /* Example css PR #xyx */

  div[class^='example'] {
    color: black;
  }
  
  /* New section ends */ 

.. _about-toc:

Table of Contents
--------------------

The ``index.rst`` file serves as a front-page to the documentation and contains the table of contents. The table of contents controls the documentation navigation menu. To add a new document to the table of contents, add the file new (without the ``.rst`` extension) to the list of file names in ``index.rst``.


.. _sections-titles:

Sections and Titles
-----------------------

Headlines require two lines: the text of the headline, followed by a line filled with a single character. Each level in a headline hierarchy uses a different character:

.. code-block:: rst

  Title of the Page - <h1> - Equal Signs
  =========================================


  Major Section - <h2> - Hyphens
  ---------------------------------


  Subsection - <h3> - Tildes
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  Sub-subsection - <h4> - Double Quotes
  """""""""""""""""""""""""""""""""""""""


  Sub-sub-subsection - <h5> - Single Quotes
  ''''''''''''''''''''''''''''''''''''''''''''

If you need to combine several existing pages together, or want to start a single-page doc that you think might be split into individual pages later on, you can add a top-level title, demoting the other headline types by one:

.. code-block:: rst

  ************************************************
  Page Title - <h1> - Asterisks above and below
  ************************************************


  Major Section - <h2> - Equal Signs
  =======================================


  Subsection - <h3> - Hyphens
  ---------------------------------


  Sub-subsection - <h4> - Tildes
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  Sub-sub-subsection - <h5> - Double Quotes
  """""""""""""""""""""""""""""""""""""""""""""

  Sub-sub-sub-subsection - <h6> - Single Quotes
  ''''''''''''''''''''''''''''''''''''''''''''''''''


In either case, the underline of characters needs to be *longer than* the line of text. In the case of the asterisks, the two lines of asterisks need to be the same length.

.. note::

  The exact order of underline characters is flexible in reStructuredText. However, this specific ordering should be used throughout the ODK documentation.

.. _section-labels:

Section labels
~~~~~~~~~~~~~~~~

In order to facilitate efficient :ref:`cross-referencing`, sections should be labeled. This is done on the line above the section title. The format is:

- two dots
- underscore
- section label

  - lowercase
  - hyphen separators

- a single colon

.. code-block:: rst

  .. _section-label:

  Section Title
  ----------------

  Lorem ipsum content of section blah blah.

The section label is a slugified version of the section title.

Section titles must be unique throughout the entire documentation set. Therefore, if you write a common title that might appear in more than one document (*Learn More* or *Getting Started*, for example), you'll need to include additional words to make the label unique. The best way to do this is to add a meaningful work from the document title.

.. code-block:: rst

  ODK Aggregate
  ===============

  ODK Aggregate is a server application...

  .. _aggregate-getting-started:

  Get Started
  -----------------

.. _basic-markup:

Basic Markup
-------------


.. note:: Escaping Characters

  Markup characters can be escaped using the ``\`` characters.

  .. code-block:: rst

    *Italic.*

    \*Not italic, surrounded by asterisks.\*

  *Italic.*

  \*Not italic, surrounded by asterisks.\*

.. _inline-markup:

Emphasis and Inline Literal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

  Single asterisks for *italic text* (``<em>``).

  Double asterisks for **bold text** (``<strong>``).

  Double back-ticks for ``inline literal text`` (``<code>``).


Single asterisks for *italic text* ( ``<em>`` ).

Double asterisks for **bold text** ( ``<strong>`` ).

Double back-ticks for ``inline literal text`` ( ``<code>`` ).

.. note::

  The **bold**, *italic*, and ``inline literal`` styles do not carry semantic meaning. They should not be used when a more semantically appropriate markup construct is available; for example, when :ref:`writing about GUI text <interface-writing>`.


.. _hyperlinks:

Hyperlinks
~~~~~~~~~~~~

**External** hyperlinks — that is, links to resources *outside* the documentation — look like this:

.. code-block:: rst

  This is a link to `example <http://example.com>`_.

This is a link to `example <http://example.com>`_.

You can also use "reference style" links:

.. code-block:: rst

  This is a link to `example`_.

  .. _example: http://example.com

This may help make paragraphs with *a lot* of links more readable. In general, the inline style is preferable. If you use the reference style, be sure to keep the link references below the paragraph where they appear.

.. code-block:: rst

  You can also simply place an unadorned URI in the text: http://example.com

You can also simply place an unadorned URI in the text: http://example.com

.. _lists:

Lists
~~~~~~~~~

.. _ul:

Unordered (bullet) lists
"""""""""""""""""""""""""""

.. code-block:: rst

  Bulleted lists ( ``<ul>`` ):

  - use hyphens
  - are unindented at the first level
  - must have a blank line before and after

    - the blank line requirement means that nested list items will have a blank line before and after as well

    - you may *optionally* put a blank line *between* list items


Bulleted lists ( ``<ul>`` ):

- use hyphens
- are unindented at the first level
- must have a blank line before and after

  - the blank line requirement means that nested list items will have a blank line before and after as well

  - you may *optionally* put a blank line *between* list items


.. _ol:

Ordered (numbered) lists
""""""""""""""""""""""""""

.. code-block:: rst

  Numbered lists ( ``<ol>`` ):

  1. Start each line with a number and period
  2. Can begin on any number
  3. Must have a blank line before and after
  4. Can have nested sub-lists

     a. nested lists are numbered separately
     b. nested lists need a blank line before and after

  #. Can have automatic number with the ``#`` character.

Numbered lists ( ``<ol>`` ):

1. Start each line with a number and period
2. Can begin on any number
3. Must have a blank line before and after
4. Can have nested sub-lists

   a. nested lists are numbered separately
   b. nested lists need a blank line before and after

#. Can have an automatic number with the ``#`` character.

.. _dl:

Definition Lists
"""""""""""""""""""

.. code-block:: rst

  Definition list ( ``<dl>`` )
    a list with several term-definition pairs

  Terms
    should not be indented

  Definitions
    should be indented under the term

  Line spacing
    there should be a blank line between term-definition pairs


Definition list ( ``<dl>`` )
  a list with several term-defition pairs

Terms
  should not be indented

Definitions
  should be indented under the term

Line spacing
  there should be a blank line between term-definition pairs


.. _paragraph-markup:

Paragraph-level Markup
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

  Paragraphs are separated by blank lines. Line breaks in the source code do not create line breaks in the output.

  This means that you *could*, in theory,
  include a lot of arbitrary line breaks
  in your source document files.
  These line breaks would not appear in the output.
  Some people like to do this because they have been trained
  to not exceed 80 column lines, and they like
  to write .txt files this way.
  Please do not do this.

  There is **no reason** to put a limit on line length in source files for documentation, since this is prose and not code. Therefore, please do not put arbitrary line breaks in your files.

Paragraphs are separated by blank lines. Line breaks in the source code do not create line breaks in the output.

This means that you *could*, in theory,
include a lot of arbitrary line breaks
in your source document files.
These line breaks would not appear in the output.
Some people like to do this because they have been trained
to not exceed 80 column lines, and they like
to write .txt files this way.
Please do not do this.

There is **no reason** to put a limit on line length in source files for documentation, since this is prose and not code. Therefore, please do not put arbitrary line breaks in your files.

Block Quotes
""""""""""""""

.. code-block:: rst

  This is not a block quote. Block quotes are indented, and otherwise unadorned.

    This is a block quote.
    — Adam Michael Wood


This is not a block quote. Block quotes are indented, and otherwise unadorned.

  This is a block quote.
  — Adam Michael Wood


Line Blocks
""""""""""""

.. code-block:: rst

  | Line blocks are useful for addresses,
  | verse, and adornment-free lists.
  |
  | Each new line begins with a
  | vertical bar ("|").
  |     Line breaks and initial indents
  |     are preserved.


| Line blocks are useful for addresses,
| verse, and adornment-free lists.
|
| Each new line begins with a
| vertical bar ("|").
|     Line breaks and initial indents
|     are preserved.


.. _tables:

Tables
""""""""

.. _grid-table:

Grid style
''''''''''''

.. code-block:: rst

  +------------+------------+-----------+
  | Header 1   | Header 2   | Header 3  |
  +============+============+===========+
  | body row 1 | column 2   | column 3  |
  +------------+------------+-----------+
  | body row 2 | Cells may span columns.|
  +------------+------------+-----------+
  | body row 3 | Cells may  | - Cells   |
  +------------+ span rows. | - contain |
  | body row 4 |            | - blocks. |
  +------------+------------+-----------+

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

.. _simple-table:

Simple style
''''''''''''''


.. code-block:: rst

  =====  =====  ======
     Inputs     Output
  ------------  ------
    A      B    A or B
  =====  =====  ======
  False  False  False
  True   False  True
  False  True   True
  True   True   True
  =====  =====  ======

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

.. _csv-table:

CSV Table
'''''''''''

The `csv-table` directive is used to create a table from CSV (comma-separated values) data. CSV is a common data format generated by spreadsheet applications and commercial databases. The data may be internal (an integral part of the document) or external (a separate file).


.. code-block:: rst

  .. csv-table:: Example Table
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


.. csv-table:: Example Table
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"   

Some of the options recognized are:

.. rst:role:: widths 
    
  Contains a comma or space-separated list of relative column widths. The default is equal-width columns.
   
  .. note::

    The special value *auto* may be used by writers to decide whether to delegate the determination of column widths to the backend.

.. rst:role:: header 

  Contains column titles. It must use the same CSV format as the main CSV data.  

.. rst:role:: delim
  
  Contains a one character string used to separate fields. Default value is comma. It must be a single character or Unicode code.

  .. code-block:: rst

    .. csv-table:: Table using # as delimiter
      :header: "Name", "Grade"
      :widths: auto
      :delim: #

      "Peter"#"A"
      "Paul"#"B"

    .. csv-table:: Table using # as delimiter
      :header: "Name", "Grade"
      :widths: auto
      :delim: #

      "Peter"#"A"
      "Paul"#"B"

.. rst:role:: align

  It specifies the horizontal alignment of the table. It can be `left` ,`right` or `center`. 

  .. code-block:: rst

    .. csv-table:: Table aligned to right
      :header: "Name", "Grade"
      :align: right

      "Peter", "A"
      "Paul", "B"

    .. csv-table:: Table aligned to right
      :header: "Name", "Grade"
      :align: right

      "Peter", "A"
      "Paul", "B"

.. rst:role:: file
  
  Contains the local filesystem path to a CSV data file.

.. rst:role:: url

  Contains an Internet URL reference to a CSV data file.

.. note::

  - There is no support for checking that the number of columns in each row is the same. However, this directive supports CSV generators that do not insert "empty" entries at the end of short rows, by automatically adding empty entries.

    .. code-block:: rst

      .. csv-table:: Table with different number of columns in each row
         :header: "Name", "Grade"
   
         "Peter"
         "Paul", "B"

   .. csv-table:: Table with different number of columns in each row
      :header: "Name", "Grade"
   
      "Peter"
      "Paul", "B"

  - Whitespace delimiters are supported only for external CSV files.


For more details, refer this `guide on CSV Tables <http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4>`_.

.. _sphinx-markup:

Sphinx-specific Markup
--------------------------

Roles and directives
~~~~~~~~~~~~~~~~~~~~~~~~

A *role* is an inline markup construct that wraps some text, similar to an HTML or XML tag. They look like this::

  :rolename:`some text`

A directive is a block-level markup construct. They look like this::

  .. directivename:: additional info or options here
    :option: optional-value
    :option: optional-value

    Content of block here, indented.

  This is no longer part of the block controlled by the directive.

Most of the Sphinx-specific and ODK-specific markup will use one or both of these constructs.

.. _cross-referencing:

Cross referencing
~~~~~~~~~~~~~~~~~~~~

Cross referencing is linking internally, from one place in the documentation to another. This is **not** done using the :ref:`hyperlinks` syntax, but with one of the several roles:

.. code-block:: rst

  :role:`target`
    becomes...
      <a href="target">reference title</a>

  :role:`anchor text <target>`
    becomes...
      <a href="target">anchor text</a>


.. rst:role:: doc

  - Links to documents (pages)
  - *target* is the file name, without the ``.rst`` extension
  - *title* is the first :ref:`headline <doc-files>` ( ``<h1>`` ) of the page

.. rst:role:: ref

  - Links to :ref:`sections <sections-titles>`
  - *target* is the :ref:`section-labels`
  - *title* is the :ref:`section title (headline) <sections-titles>`


.. rst:role:: term

  - Links to items in the :doc:`glossary`
  - *target* is the term, in the glossary
  - *title* is the term itself

**To recap:** If you do not include an explicit ``<target>``, the text inside the role will be understood as the target, and the anchor text for the link in the output will be the title of the target.

For example:

.. code-block:: rst

  - Link to this document:

    - :doc:`contributing`
    - :doc:`anchor text <contributing>`

  - Link to this section:

    - :ref:`cross-referencing`
    - :ref:`anchor text <cross-referencing>`

  - Link to a term:

    - :term:`participant`
    - :term:`anchor text <participant>`

- Link to this document:

  - :doc:`contributing`
  - :doc:`anchor text <contributing>`

- Link to this section:

  - :ref:`cross-referencing`
  - :ref:`anchor text <cross-referencing>`

- Link to a term:

  - :term:`participant`
  - :term:`anchor text <participant>`

.. _interface-writing:

Writing about User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several roles are used when describing user interactions.

.. rst:role:: guilabel

  Marks up *actual UI text* of form labels or buttons.

  .. code-block:: rst

    Press the :guilabel:`Submit` button.

.. rst:role:: menuselection

  Marks up the *actual UI text* of a navigation menu or form select element.

  .. code-block:: rst

    Select :menuselection:`Help` from menu.

  When writing about multi-level menus, use a single ``:menuselection:`` role, and separate menu choices with ``-->``.

  .. code-block:: rst

    To save your file, go to :menuselection:`File --> Save` in the Main Menu.

.. note::

  In some situations you might not be clear about which option to use from ``:menuselection:`` and ``:guilabel:``, in which case you should refer to the following rule that we observe in our writing.

  - Actual UI text will always receive ``:guilabel:`` role unless the text could reasonably be understood to be part of a menu.
  - If the actual UI text could be understood as a menu, ``:menuselection:`` should be used.

.. rst:role:: kbd

  Marks up a sequence of literal keyboard strokes.

  .. code-block:: rst

    To stop the local server, type :kbd:`CTRL C`.

.. rst:role:: command

  Marks up a terminal command.

  .. code-block:: rst

    To build the documentation, use :command:`sphinx-build`.

.. rst:role:: option

  Marks up a terminal command option.

  .. code-block:: rst

    The :option:`-b html` option specifies the HTML builder.

.. _custom-text-roles:

Custom Text Roles
~~~~~~~~~~~~~~~~~~~

**Custom Text Roles** signify that the enclosed text should be interpreted in a specific way.

Custom text roles used in ODK documentation are:

.. rst:role:: th

  Stands for table head and refers to a table header cell in the body of text.

.. rst:role:: tc

  Stands for table cell and describes the table cells in the body of text.

  .. code-block:: rst

    External App String Widget
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`.

.. rst:role:: formstate

  Specifies the state of the form which could be one of the following:

  - Blank
  - Finalized
  - Saved
  - Sent
  - Deleted

  .. code-block:: rst

    :formstate:`Sent`

.. rst:role:: gesture

  Describes a touch screen gesture.

  .. code-block:: rst

    :gesture:`Swipe Left`

.. _misc-markup:

Other Semantic Markup
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst:role:: abbr

  Marks up an abbreviation. If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML.

  .. code-block:: rst

    :abbr:`ODK (Open Data Kit)`

.. rst:role:: dfn

  Marks the defining instance of a term outside the glossary.

  .. code-block:: rst

    :dfn:`Open Data Kit` (ODK) is a suite of open source applications that help organizations engaged in enumerator-mediated data collection.

.. rst:role:: file

  Marks the name of a file or directory. Within the contents, you can use curly braces to indicate a “variable” part.

  .. code-block:: rst

    is installed in :file:`/usr/lib/python2.{x}/site-packages`

  In the built documentation, the ``x`` will be displayed differently to indicate that it is variable.

.. rst:role:: program

  Marks the name of an executable program.

  .. code-block:: rst

    launch the :program:`ODK Aggregate Installer`

.. _images:

Images and Figures
~~~~~~~~~~~~~~~~~~~~~~

Image files should be put in the :file:`/img/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

You must perform lossless compression on the source images. Following tools can be used to optimize the images:

- **ImageOptim** is a tool that allows us to optimize the images. It is not format specific which means it can optimize both jpeg as well as png images. You can download it `from here <https://imageoptim.com/howto.html>`_ . After launching ImageOptim.app, dragging and dropping images into its window gives you an in-place optimized file.

- **Pngout** is another option for optimizing png images. Installation and usage instructions can be found `here <http://docs.ewww.io/article/13-installing-pngout/>`_ .

- **Mozjpeg** can be used to optimize jpeg images. Installation and related information can be found on `this link <https://nystudio107.com/blog/installing-mozjpeg-on-ubuntu-16-04-forge/>`_ .

To place an image in a document, use the ``image`` directive.

.. code-block:: rst

  .. image:: /img/{document-subdirectory}/{file}.*
    :alt: Alt text. Every image should have descriptive alt text.

Note the *literal* asterisk at the end *in place of a file extension*. Use the asterisk, and omit the file extension.

Use the ``figure`` to markup an image with a caption.

.. code-block:: rst

  .. figure:: /img/{document-subdirectory}/{file}.*
    :alt: Alt text. Every image should have descriptive alt text.

    The rest of the indented content will be the caption. This can be a short sentence or several paragraphs. Captions can contain any other rst markup.

.. _substitutions:

Substitutions
"""""""""""""""

Substitutions are a useful way to define a value which is needed in many places. Substitution definitions are indicated by an explicit markup start (".. ") followed by a vertical bar, the substitution text (which gets substituted), another vertical bar, whitespace, and the definition block. A substitution definition block may contain inline-compatible directives such as :ref:`image <images>` or `replace <http://docutils.sourceforge.net/docs/ref/rst/directives.html#replace>`_. For more information, refer this `guide <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions>`_.

You can define the value once like this:

.. code-block:: rst 

  .. |RST| replace:: reStructuredText
  
and then reuse it like this:

.. code-block:: rst 

  We use |RST| to write documentation source files.
  
Here, ``|RST|`` will be replaced by reStructuredText

You can also create a reference with styled text:

.. code-block:: rst
  
  .. |slack| replace:: **ODK Slack**
  .. slack: https://opendatakit.slack.com

You can use the hyperlink reference by appending a "_" at the end of the vertical bars, for example:

.. code-block:: rst

  You can ask about your problem in |slack|_.

.. |slack| replace:: **ODK Slack**
.. _slack: https://opendatakit.slack.com  

You can ask about your problem in |slack|_.

The ``rst_epilog`` in :file:`conf.py` contains a list of global substitutions that can be used from any file. The list is given below:

- If you want to create a hyperlink reference for ODK Slack, you can use ``|odk-slack|_``.

  .. code-block:: rst

    You can use |odk-slack|_ to ask your questions.
  
  You can use |odk-slack|_ to ask your questions.
  
|
  
- To create a hyperlink reference for docs related issues, use ``|docs-issue|_``.

  .. code-block:: rst
  
    If you find a problem, file an |docs-issue|_.
	
  If you find a problem, file an |docs-issue|_.
  
|
 
- To create a hyperlink reference for ODK Forum, use ``|forum|_``.

  .. code-block:: rst
  
    You can ask support questions in |forum|_.
	
  You can ask support questions in |forum|_.

|  
  
- To create a hyperlink reference for contributors guide, use ``|contrib-guide|_``.

  .. code-block:: rst
    
	Be sure to read the |contrib-guide|_.
	
  Be sure to read the |contrib-guide|_.

You can add inline images in the document using substitutions. The following block of code substitutes arrow in the text with the image specified.  

.. code-block:: rst 

  The |arrow| icon opens the jump menu.
  
  .. |arrow| image:: /img/{document-subdirectory}/{file}.*
             :alt: Alt text.

			 
.. _image-names:

Image File Names
""""""""""""""""""

Image file names should:

- be short yet descriptive
- contain only lower case characters
- have no spaces
- use hyphens as the separator

Good image file names:

- :file:`collect-home-screen.png`
- :file:`build-data-export-menu.png`

Bad image file names:

- :file:`Collect home screen.png`
- :file:`collect_home_screen.png`
- :file:`3987948p2983768ohl84692p094.jpg-large`

.. tip::

  Be sure to obscure any personally-identifiable information from screen shots. Crop to the smallest relevant screen area. Annotate screen shots with arrows or circles to indicate relevant information.

.. _screenshots:

Screenshots from ODK Collect
"""""""""""""""""""""""""""""""

If you have set up local :ref:`android-tools`, you can connect your Android device to your computer and take screenshots from the command line.

- Connect your device via USB
- Enable Developer Settings

  - :menuselection:`Settings --> About phone`
  - Tap :menuselection:`Build number` seven (7) times

- Turn on USB Debugging

  - :menuselection:`Settings --> Developer options --> USB debugging`

Now, at the command line, from the root directory of the :file:`odk-docs` repo:

.. code-block:: console

  python ss.py {document-name}/{image-name}

- ``{document-name}`` is the filename (without extension) where the image will be used.
- ``{image-name}`` is the name (without extension) given to the image.
  - follow the :ref:`image-names` guidelines

.. warning::
  Make sure you do not overwrite an existing image.

.. tip::
  If you have a problem running ss.py, check to make sure your :ref:`Python 3 virtual environment <docs-venv>` is activated.

.. _videos:

Videos
~~~~~~~~

Video files should be put in the :file:`/vid/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

The length of the videos must be less than a minute.

We have a custom video directive to add a video: 

.. rst:directive:: video

  You should specify the source address of the video and a descriptive alt content in the video directive. Alternate content is displayed when the video cannot be played. It can contain long texts as well as any other rst content. 

  So to add a video in a document, you can do the following:

  .. code-block:: rst

    .. video:: /vid/{document-subdirectory}/{file}.mp4
    
      Alt content. Every video should have descriptive alt content.

  Following options are supported:

  .. rst:role:: autoplay 

    Specifies whether the video should start playing as soon as it is ready. Can take boolean value: true, false, yes or no. Default is **no**.

  .. rst:role:: controls

    Specifies whether the video controls should be displayed. Can take boolean value: true, false, yes or no. Default is **yes**.

  .. rst:role:: muted

    Specifies whether the audio output of the video should be muted. Can take boolean value: true, false, yes or no. Default is **yes**.

  .. rst:role:: loop 

    Specifies whether the video should start over again, every time it is finished. Can take boolean value: true, false, yes or no. Default is **no**.   

  .. rst:role:: preload   

    Specifies if and how the author thinks the video should be loaded when the page loads. Can take one of the following three values: **auto**, **metadata** or **none**.

  .. rst:role:: poster  

    Contains the source address for an image to be shown while the video is downloading, or until the user hits the play button.

    .. note::

      Images to be used as poster for a video should be in the same directory as the video and should have a name of format :file:`[same-file-name-as-video]-poster.ext`.

  .. rst:role:: class 

    Specifies a class for the video element.

  For more details on these attributes, see `this guide <https://www.w3schools.com/tags/tag_video.asp>`_.

  To add a video in a document with the above options, you can do the following:

  .. code-block:: rst

    .. video:: /vid/{document-subdirectory}/{file}.mp4
      :autoplay: yes/no
      :controls: yes/no
      :muted: yes/no
      :loop: yes/no
      :class: class-name
      :preload: auto/metadata/none
      :poster:: /vid/{document-subdirectory}/{file}.ext

      Alt content. Every video should have descriptive alt content.

**ADB or Android Debug Bridge** can be used to capture a screen recording from collect. This can be done by entering:

.. code-block:: console

  $ adb shell screenrecord /sdcard/example.mp4

On pressing the enter key the video recording starts. Recording stops automatically after 3 minutes but since video length has to be less than a minute, to stop the recording in between simply press :command:`Ctrl+C`.

The video file is saved in your Android device to a file at :file:`/sdcard/example.mp4` file.

To pull the video locally just type the following command and hit :command:`Enter`.

.. code-block:: console

  $ adb pull /sdcard/example.mp4 localsavelocation

where localsavelocation is the location where you want to save your file locally.

.. _downloads:

Downloadable files
~~~~~~~~~~~~~~~~~~~~

Downloadable files should be put in the :file:`/downloads/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

To place a downloadable file in a document, use the ``download`` directive.

.. code-block:: rst

  See this :download:`example script </downloads/contributing/example_script.py>` to understand the procedure better.

.. _code-samples:

Code Samples
~~~~~~~~~~~~~~

Use the ``code-block`` directive to markup code samples. Specify the language on the same line as the directive for syntax highlighting.

.. code-block:: rst

  .. code-block:: rst

    Use the ``code-block`` directive to markup code samples.

  .. code-block:: python

    print("Hello ODK!")

  .. code-block:: console

    $ python --version

  .. code-block:: java

    public class HelloWorld {

        public static void main(String[] args) {
            // Prints "Hello, World" to the terminal window.
            System.out.println("Hello, World");
        }

    }

.. note::
  
  **rst** code-blocks wrap overflow lines by default. To unwrap overflow lines, use **unwrap** class with **rst** code-blocks.

  .. code-block:: rst

    .. code-block:: rst
      :class: unwrap

  Code-blocks for other languages don't wrap overflow lines. Instead of wrapping, you need to scroll side-ways. To wrap overflow lines with other code-blocks, use **wrap** class with them.

  .. code-block:: rst

    .. code-block:: python
      :class: wrap

