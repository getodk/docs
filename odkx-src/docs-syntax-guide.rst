.. spelling::

  py
  ss

Docs Markup and Syntax Guide
================================

The ODK documentation is built using `Sphinx <http://sphinx-doc.org>`_, a static-site generator designed to create structured, semantic, and internally consistent documentation. Source documents are written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_, a semantic, extensible markup syntax similar to Markdown.

- `reStructuredText Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_ — Introduction to reStructuredText

  - `reStructuredText Quick Reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
  - `reStructuredText 1-page cheat sheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_

- `Sphinx Markup <http://www.sphinx-doc.org/en/stable/markup/index.html>`_ — Detailed guide to Sphinx's markup concepts and reStructuredText extensions

.. note::

  Sphinx and `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ can be very flexible. For the sake of consistency and maintainability, this guide is *highly opinionated* about how documentation source files are organized and marked up.


.. _indentation:

Indentation
--------------

Indentation is meaningful in Sphinx and `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ text. Usually, indenting a section means that is "belongs to" the line it is indented under. For example:

.. code-block:: rst

  .. figure:: path-to-image.*

    This is the caption of the figure. Notice that it is indented under the line defining the figure.

The rules for indentation are:

- Use **spaces, not tabs**.
- Generally, indent **two spaces**.

The exception to the two spaces rule is :ref:`ol`, where indentation follows the content of the list item.

.. code-block:: rst

  1. This is a list item.

     This is some additional content related to Item 1. Notice that it is indented to the same column as the first line of content. In this case, that's three (3) spaces.

  .
  .
  .

  10. The tenth item in a list.

      This related content will be indented four spaces.



.. _doc-files:

Documentation Files
----------------------

Sphinx document files have the ``.rst`` extension. File names should be all lowercase and use hyphens (not underscores or spaces) as word separators.

Normally, the title of the page should be the first line of the file, underlined with equal-signs.

.. code-block:: rst

  Title of Page
  ================

  Page content is here...

You can alternatively wrap the title in two lines of asterisks, in some cases. (This should not be your default choice.)

.. code-block:: rst

  *******************
  Title of Page
  *******************

  Page content here.

The asterisks style is useful when you are combining several existing documents and don't want to change every subsection headline. Or, you can use it when you are working on a document that you have reason to think might be split into separate documents in the future.

.. important::

  If you use the double-asterisks style, your major section headlines (`<h2>`) should use the equal-signs underline style. This allows major sections to be easily promoted to individual pages.

See :ref:`sections-titles` for more details.


.. _about-toc:

Tables of Content
--------------------

The :rst:dir:`toctree` directive defines a table of content. The content of a :rst:dir:`toctree` is a list of page file names, without the ``.rst`` extension. When rendered, the :rst:dir:`toctree` becomes an unordered list of page links, including links to sections and subsections of the included pages.

.. code-block:: rst

  .. toctree::

    page-name
    another-page
    this-other-page

The depth of section and subsection links to display in the output can be controlled using the :rst:role:`maxdepth` attribute. We typically use a depth of ``2``, but you should use your judgment if you feel it should be more or less in any given context.

.. code-block:: rst

  .. toctree::
    :maxdepth: 2

    this-page
    that-page
    thick-page
    flat-page


.. seealso::

  `The TOC Tree <http://www.sphinx-doc.org/en/stable/markup/toctree.html>`_

    The Sphinx documentation includes information about a number of other :rst:dir:`toctree` attributes.

.. _main-nav-menu:

Sidebar navigation menu
~~~~~~~~~~~~~~~~~~~~~~~~~

The :file:`index.rst` file serves as a front-page to the documentation and contains the main tables of content, defined using :rst:dir:`toctree` directives.

These :rst:dir:`toctree` directives control the sidebar navigation menu. To add a new document to a table of content, add the file name (without the ``.rst`` extension) to the relevant list of file names in :file:`index.rst`.

.. _secondary-tocs:

Secondary tables of content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collections of documents are sometimes given their own table of content on an individual page.

In these cases, the page containing the :rst:dir:`toctree` serves as a sort of intro page for the collection. That intro must, itself, be included in the :ref:`main-nav-menu`.

The contents of a :rst:dir:`toctree` appear as section links in another :rst:dir:`toctree` it is included in. That is, if a :rst:dir:`toctree` in :file:`index.rst` lists ``survey-using``, and :file:`survey-using.rst` has a :rst:dir:`toctree`, then the contents of that second :rst:dir:`toctree` will appear in the :ref:`main-nav-menu`, as sub-items to :doc:`survey-using`. (Indeed, this is precisely the case in the docs currently.)

How ODK Docs uses main and secondary tables of content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Major topics get a :rst:dir:`toctree` in :file:`index.rst`

  Major topics include things like:

  - Each major product (Collect, Aggregate, Briefcase)
  - Large, general categories like Contributing

  Major topic tables of content include both sub-collection intro pages and also individual pages that don't fit into a sub-collection.

  The :rst:role:`caption` attribute of the :rst:dir:`toctree` directive defines the section label in the :ref:`main-nav-menu`.

- Within a large topic, documents are grouped into collections of related pages, defined by a :rst:dir:`toctree` on a topic intro page.

  Intro pages (pages that contain secondary :rst:dir:`toctree` directives) may include additional content, introducing the collection or providing contextual wayfinding. However, this is not always necessary or desirable. Use your judgment, and avoid stating things just for the sake of having some text. ("Here are the pages in this collection.")

  We also (very occasionally) include :rst:dir:`toctree` directives in sub-collection pages.

.. tip::

  If it's not obvious where a new document should appear in the navigation, the best practice is to simply ask about it in the GitHub issue driving the new page.

.. note::

  For wayfinding purposes, we sometimes create an :ref:`ul` of page links rather than a :rst:dir:`toctree` directive. (For example, see :file:`collect-intro`. We do this when using a :rst:dir:`toctree` would create redundant links in the :ref:`main-nav-menu`.

.. admonition:: Why are the docs files not grouped into folders in the source?

  We use :rst:dir:`toctree` directives as our primary way of organizing the documentation for readers. We do not organize the source ``rst`` files into subfolders.

  The reason is that if we put them into topic-related subfolders, it would affect the URI of the document. Keeping all of our document files in a single flat directory results in a flat URI structure. Every page's URI looks like ``docs.odk-x.org/page-name``.

  If we used subdirectories, then our URIs would look like ``docs.odk-x.org/subdirectory-name/page-name``. This would mean that our URIs would change every time we moved a document from one folder to another, greatly increasing the time cost and broken-link risk of reorganizing the docs.


.. _sections-titles:

Sections and Titles
-----------------------

Headlines require two lines:

- the text of the headline, followed by
- a line filled with a single character.

Each level in a headline hierarchy uses a different character:

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

If you need to combine several existing pages together, or want to start a single-page doc that you think might be split into individual pages later on, you can add a top-level title, demoting the other headline types by one.

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

  The exact order of underline characters is flexible in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_. However, this specific ordering should be used throughout the ODK documentation.

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

The section label is usually a slugified version of the section title.

Section titles must be unique throughout the entire documentation set. Therefore, if you write a common title that might appear in more than one document (*Learn More* or *Getting Started*, for example), you'll need to include additional words to make the label unique. The best way to do this is to add a meaningful work from the document title.

.. code-block:: rst

  ODK Aggregate
  ===============

  ODK Aggregate is a server application...

  .. _aggregate-getting-started:

  Getting Started
  -----------------

.. _basic-markup:

Basic Markup
-------------

.. _escaping-characters:

Escaping characters
~~~~~~~~~~~~~~~~~~~~~

Markup characters can be escaped using the ``\`` character.

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

.. note::

  See :ref:`ordered-vs-unordered` in the :doc:`docs-style-guide` for details on when to use ordered and unordered lists.

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
  a list with several term-definition pairs

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

The :rst:role:`csv-table` role is used to create a table from CSV (comma-separated values) data. CSV is a common data format generated by spreadsheet applications and commercial databases. The data may be internal (an integral part of the document) or external (a separate file).

You can import the date either using 'file' or 'url'. When using 'file' it contains the local file system path to a CSV data file. When using 'url' it contains an Internet URL reference to a CSV data file.


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

  The special value ``auto`` may be used by writers to decide whether to delegate the determination of column widths to the backend.

  In most cases, the best result is either the default or ``auto``. If you're unsure, try it both ways and see which looks better to you.

.. rst:role:: header

  Contains column titles. It must use the same CSV format as the main CSV data.

.. rst:role:: delim

  Contains a one character string used to separate fields. Default value is comma. It must be a single character or Unicode code.

  The only reason to use something other than a comma is when copying large blocks of content from another source that uses a different style. If you are creating new table content yourself, use the comma.

  .. code-block:: rst

    .. csv-table:: Table using # as delimiter
      :header: "Name", "Grade"
      :widths: auto
      :delim: #

      "Peter"#"A"
      "Paul"#"B"

    .. csv-table:: Table using | as delimiter
      :header: "Name", "Grade"
      :widths: auto
      :delim: |

      "Peter"|"A"
      "Paul"|"B"

.. rst:role:: align

  It specifies the horizontal alignment of the table. It can be `left`, `right` or `center`.

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


For more details, refer to this `guide on CSV Tables <http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4>`_.

.. note::

  In almost all cases, :rst:dir:`csv-table` is the easiest and most maintainable way to insert a table into a document. It should be preferred unless there is a compelling reason to use one of the other styles.

.. _sphinx-markup:

Sphinx-specific Markup
--------------------------

.. _roles-and-directives:

Roles and directives
~~~~~~~~~~~~~~~~~~~~~~~~

A :dfn:`role` is an inline markup construct that wraps some text, similar to an HTML or XML tag. They look like this::

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


**To recap:** If you do not include an explicit ``target``, the text inside the role will be understood as the target, and the anchor text for the link in the output will be the title of the target.

For example:

.. code-block:: rst

  - Link to this document:

    - :doc:`contributing`
    - :doc:`anchor text <contributing>`

  - Link to this section:

    - :ref:`cross-referencing`
    - :ref:`anchor text <cross-referencing>`

- Link to this document:

  - :doc:`contributing`
  - :doc:`anchor text <contributing>`

- Link to this section:

  - :ref:`cross-referencing`
  - :ref:`anchor text <cross-referencing>`

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

  In some situations you might not be clear about which option (:rst:role:`menuselection` or :rst:role:`guilabel`) to use. GUIs in real life can sometimes be ambiguous. The general rule is:

  - Actual UI text will always receive :rst:role:`guilabel` role unless the text could reasonably be understood to be part of a menu.
  - If the actual UI text could be understood as a menu, :rst:role:`menuselection` should be used.

  These both render the same on output, so don't worry too much if you get it wrong. Just use your judgment and take your best guess.

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

.. rst:role:: gesture

  Describes a touch screen gesture.

  .. code-block:: rst

    :gesture:`Swipe Left`


.. _writing-about-forms:

Writing about forms
~~~~~~~~~~~~~~~~~~~~~~~

We have added several custom text roles for writing about forms and the XForms and XLSForm formats.

.. rst:role:: th

  Used to refer to a table header cell.

.. rst:role:: tc

  Used to refer to a table cell.

  .. code-block:: rst

    External App String Widget
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    The external app widget is displayed when the :th:`appearance` attribute begins with :tc:`ex:`.

.. rst:role:: formstate

  Specifies the state of the form in :doc:`survey-using`, which could be one of the following:

  - Blank
  - Finalized
  - Saved
  - Sent
  - Deleted

  .. code-block:: rst

    :formstate:`Sent`


.. _misc-markup:

Other Semantic Markup
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst:role:: dfn

  Marks the defining instance of a term outside the glossary.

  .. code-block:: rst

    :dfn:`ODK-X is a suite of open source applications that help organizations engaged in enumerator-mediated data collection.

.. rst:role:: file

  Marks the name of a file or directory. Within the contents, you can use curly braces to indicate a "variable" part.

  .. code-block:: rst

    is installed in :file:`/usr/lib/python2.{x}/site-packages`

  In the built documentation, the ``x`` will be displayed differently to indicate that it is variable.

.. rst:role:: program

  Marks the name of an executable program.

  .. code-block:: rst

    launch the :program:`ODK Aggregate Installer`


.. _images-and-figures:

Images and Figures
~~~~~~~~~~~~~~~~~~~~~~

.. _pngs-only:

PNGs only
"""""""""""

All still images used in ODK Docs should be PNG files.
This helps us keep our image compression tooling simple,
and generally results in higher-quality screenshots.

Whenever possible,
you should generate your images as PNGs
rather than converting to PNGs from another format.
If you have to start in another format,
use lossless formats whenever possible.
These include BMP, GIF, and TIFF.
(Avoid JPG/JPEG if possible,
as this is a lossy format
that does not replicate screenshots very well.)

.. _where-to-put-image-files:

Where to put image files
"""""""""""""""""""""""""""

Image files should be put in the :file:`/src/img/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

.. _image-compression:

Image compression
""""""""""""""""""""

Before committing images locally,
run lossless compression on them
using one of the following tools:

- `ImageOptim`_
- `Pngout`_

.. _ImageOptim: https://imageoptim.com/howto.html
.. _Pngout: http://docs.ewww.io/article/13-installing-pngout/

.. _inserting-image:

Inserting images in a document
""""""""""""""""""""""""""""""""""

To place an image in a document, use the :rst:dir:`image` directive.

.. code-block:: rst

  .. image:: /img/{document-subdirectory}/{file}.*
    :alt: Alt text. Every image should have descriptive alt text.

Note the literal asterisk (``*``) at the end, in place of a file extension. Use the asterisk, and omit the file extension.

.. _figures:

Inserting images with captions (figures)
""""""""""""""""""""""""""""""""""""""""""

Use :rst:dir:`figure` to markup an image with a caption.

.. code-block:: rst

  .. figure:: /img/{document-subdirectory}/{file}.*
    :alt: Alt text. Every image should have descriptive alt text.

    The rest of the indented content will be the caption. This can be a short sentence or several paragraphs. Captions can contain any other rst markup.


.. _inline-images:

Inline images
"""""""""""""""

To information on creating inline images, see :ref:`substitutions`.

.. _image-file-names:

Image File Names
""""""""""""""""""

Image file names should:

- be short yet descriptive
- contain only lower case characters and (in :ref:`sequentially-numbered-images` only) numbers
- have no spaces
- use hyphens as the separator

Good image file names:

- :file:`survey-home-screen.png`
- :file:`build-data-export-menu.png`

Bad image file names:

- :file:`Survey home screen.png`
- :file:`survey_home_screen.png`
- :file:`3987948p2983768ohl84692p094.jpg-large`

.. _sequentially-numbered-images:

Sequentially numbered images
''''''''''''''''''''''''''''''

In the case of sequentially numbered images, the numbers should:

- be zero-indexed
- have two digits with leading zeroes
- be separated from the rest of the file name with a hyphen
- be placed at the end of the file name

Good sequentially numbered image file names:

- :file:`map-widget-00`, :file:`map-widget-01`, :file:`map-widget-02`

Bad sequentially numbered image file names:

- :file:`1-map-widget`, :file:`2-map-widget`
- :file:`map-widget_00`, :file:`map-widget_01`
- :file:`map-widget-1`, :file:`map-widget-2`

.. _screenshots:


Screenshots from ODK Collect
"""""""""""""""""""""""""""""""

If you have set up Android Debug Bridge, you can connect your Android device to your computer and take screenshots from the command line.

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
  - follow the :ref:`image-file-names` guidelines

.. warning::
  Make sure you do not overwrite an existing image.

.. tip::
  If you have a problem running ss.py, check to make sure your Python 3 virtual environment is activated.


.. tip::

  Be sure to obscure any personally-identifiable information from screen shots. Crop to the smallest relevant screen area. Annotate screen shots with arrows or circles to indicate relevant information.


.. _videos:

Videos
~~~~~~~~

Video files should be put in the :file:`/src/vid/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

The purpose of on page videos is to illustrate complicated user interactions that might be difficult to describe otherwise. Longer tutorial videos should be hosted elsewhere and, if appropriate, linked to from the docs. Therefore:

- The length of the videos must be less than a minute.
- Videos should have no audio.


To insert a video, use the custom :rst:dir:`video` directive.

.. rst:directive:: .. video:: path/to/video

  Specify the source path of the video and a descriptive alt content in the video directive. Alternate content is displayed when the video cannot be played. It can contain long texts as well as any other rst content.

  .. code-block:: rst

    .. video:: /vid/{document-subdirectory}/{file}.ext

      Alt content. Every video should have descriptive alt content.

  The following optional attributes are supported:

  .. rst:role:: autoplay

    Specifies whether the video should start playing as soon as it is ready. Can take boolean value: true, false, yes or no. Default is **no**.

    It is almost never a good idea to turn ``autoplay`` on.

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

      Images to be used as poster for a video should be in the same directory as the video and should have a filename like :file:`[same-file-name-as-video]-poster.ext`.

  .. rst:role:: class

    Specifies a class for the video element.

  For more details on these attributes, see `this guide <https://www.w3schools.com/tags/tag_video.asp>`_.

  To add a video in a document with the above options, you can do the following:

  .. code-block:: rst

    .. video:: /vid/{document-subdirectory}/{file}.ext
      :autoplay: yes/no
      :controls: yes/no
      :muted: yes/no
      :loop: yes/no
      :class: class-name
      :preload: auto/metadata/none
      :poster:: /vid/{document-subdirectory}/{file}.ext

      Alt content. Every video should have descriptive alt content.

.. _capturing-video-from-collect:

Capturing video from Android
"""""""""""""""""""""""""""""""

`Android Debug Bridge (ADB) <https://developer.android.com/studio/command-line/adb.html>`_ can be used to capture a screen recording from an Android app.

.. code-block:: console

  $ adb shell screenrecord /sdcard/example.mp4

On pressing the enter key the video recording starts. Recording stops automatically after 3 minutes. Since videos have to be less than a minute, press :kbd:`CTRL C` to stop the recording.

The video file is saved in your Android device to a file at :file:`/sdcard/example.mp4` file.

To pull the video locally:

.. code-block:: console

  $ adb pull /sdcard/example.mp4 local/path/to/save/to



.. _downloads:

Downloadable files
~~~~~~~~~~~~~~~~~~~~

Downloadable files should be put in the :file:`/src/downloads/` directory in the source, and they should be in a subdirectory with the same name as the document in which they appear. (That is, the filename without the ``.rst`` extension.)

To place a downloadable file in a document, use the :rst:role:`download` role.

.. code-block:: rst

  See this :download:`example script </downloads/contributing/example_script.py>` to understand the procedure better.

.. _code-samples:

Code Samples
~~~~~~~~~~~~~~

Use the :rst:dir:`code-block` directive to insert code samples. Specify the language on the same line as the directive for syntax highlighting.

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


.. _substitutions:

Substitutions
~~~~~~~~~~~~~~~~~

Substitutions are a useful way to define a value which is needed in many places.

Substitution definitions are indicated by an explicit markup start (".. ") followed by a vertical bar, the substitution text (which gets substituted), another vertical bar, whitespace, and the definition block.

A substitution definition block may contain inline-compatible directives such as :ref:`image  <images-and-figures>` or `replace <http://docutils.sourceforge.net/docs/ref/rst/directives.html#replace>`_. For more information, refer this `guide <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#substitution-definitions>`_.

You can define the value once like this:

.. code-block:: rst

  .. |RST| replace:: `reStructuredText <http://docutils.sourceforge.net/rst.html>`_

and then reuse it like this:

.. code-block:: rst

  We use |RST| to write documentation source files.

Here, ``|RST|`` will be replaced by `reStructuredText <http://docutils.sourceforge.net/rst.html>`_

You can also create a reference with styled text:

.. code-block:: rst

  .. |github| replace:: **ODK-X Github**
  .. github: https://github.com/odk-x/

You can use the hyperlink reference by appending a "_" at the end of the vertical bars, for example:

.. code-block:: rst

  You can ask about your problem on |github|_.

.. |github| replace:: **ODK-X Github**
.. _github: https://github.com/odk-x/

You can ask about your problem on |github|_.

The ``rst_epilog`` in :file:`conf.py` contains a list of global substitutions that can be used from any file. The list is given below:

- If you want to create a hyperlink reference for ODK-X Github, you can use ``|github|_``.

  .. code-block:: rst

    You can use |github|_ to ask your questions.

  You can use |github|_ to ask your questions.

|

- To create a hyperlink reference for docs related issues, use ``|docs-issue|_``.

  .. code-block:: rst

    If you find a problem, file an |docs-issue|_.

  If you find a problem, file an |docs-issue|_.

|

- To create a hyperlink reference for ODK-X Forum, use ``|forum|_``.

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
