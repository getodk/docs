*****************
Style Guide
*****************

.. _spelling-and-grammar:

Spelling and grammar
=======================

.. _american-spelling:

American spelling and grammar
-----------------------------

Whenever U.S. English and British (or other) English spelling or usage disagree, standard U.S. spelling and usage is preferred.

.. rubric:: Wrong

.. code-block:: rst

  The colour of the button is grey.

.. rubric:: Right

.. code-block:: rst

  The color of the button is gray.

.. code-block:: python
  :class: proselint-extra-checks
  
  @memoize
  def check_ukus(text):
      """UK vs. US spelling usage."""
      err = "style-guide.uk-us"
      msg = "uk-vs-us-spell-check. '{}' is the preferred spelling."

      preferences = [
          ["gray",                ["grey"]],
          ["color",               ["colour"]],
          ["accessorizing",       ["accessorising"]],
          ["acclimatization",     ["acclimatisation"]],
          ["acclimatize",         ["acclimatise"]],
          ["acclimatized",        ["acclimatised"]],
      ]

      return preferred_forms_check(text, preferences, err, msg)

      # This is a sample code. The complete code can be found in the file:
      # proselint-extra.py.

.. _quote-marks:
    
Quote marks
--------------

 - Quote marks should generally be avoided if possible.
 - *Smart* quotes (also known as *curly quotes* or *directional quotes*) are not permitted in source files.
 
.. _avoid-quotes:
 
Avoid quote marks
~~~~~~~~~~~~~~~~~~~~~

Quote marks are used in prose writing to indicate verbatim text. This is rarely useful in technical writing, as verbatim text usually requires a more specific semantic markup.

.. rubric:: Wrong

.. code-block:: rst

  Click the button that says, "Save."
  
.. rubric:: Right

.. code-block:: rst

  Click :guilabel:`Save`.
  
.. rubric:: Wrong

.. code-block:: rst

  You may see an error message that says, "Something went wrong."
  
.. rubric:: Right

.. code-block:: rst

  You may get an error: ``Something went wrong.``

.. code-block:: python
  :class: extra-checks

  def check_quotes(text):
      """Avoid using straight quotes."""
      err = "style-guide.check-quote"
      msg = "Avoid using quote marks."
      regex = r"\"[a-zA-z0-9 ]{1,15}\""

      errors = []

      for matchobj in re.finditer(regex, text):
          start = matchobj.start()+1
          end = matchobj.end()
          (row, col) = line_and_column(text, start)
          extent = matchobj.end()-matchobj.start()
          errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]  

      return errors
 
.. _straight-quote:
  
Straight quotes
~~~~~~~~~~~~~~~~~~

Any time that you *do* need to use quotation marks, use straight (or *plain*) quotes. Sphinx and Docutils will output the typographically correct quote style.

.. code-block:: python
  :class: extra-checks

  def check_curlyquotes(text):
      """Do not use curly quotes."""
      err = "style-guide.check-curlyquote"
      msg = "Do not use curly quotes. If needed use straight quotes."
      regex = r"\“[a-zA-z0-9 ]{1,15}\”"

      errors = []

      for matchobj in re.finditer(regex, text):
          start = matchobj.start()+1
          end = matchobj.end()
          (row, col) = line_and_column(text, start)
          extent = matchobj.end()-matchobj.start()
          errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]  

      return errors

.. _serial-comma:

Serial comma
-----------------

In a comma-delineated list of items, the penultimate item should be followed by a comma.

.. rubric:: Wrong

.. code-block:: rst

  Apples, oranges and pears.
  
.. rubric:: Right

.. code-block:: rst

  Apples, oranges, and pears.

.. code-block:: python
  :class: style-checks

  @memoize
  def check_comma(text):
      """Use serial comma after penultimate item."""
      err = "style-guide.serial-comma"
      msg = "Use serial comma after penultimate item."
      regex = "\,\s[a-zA-Z0-9]+\sand\s"

      return existence_check(text, [regex], err, msg, require_padding=False)

A bulleted list is often more clear than an inline list.

.. rubric:: Correct

.. code-block:: rst

  You will need to be familiar with git, GitHub, and Python.
  
.. rubric:: Possibly Better

.. code-block:: rst

  You will need to be familiar with:
  
  - git
  - GitHub
  - Python
  
There's no hard rule about which to use in any situation. Use your judgement: try it both ways and see which is more clear.

.. _direct-address:

Direct Address
------------------

Direct address 
--- speaking directly to the reader using the second person "you" --- 
is preferred over
passive voice ("it can be done"),
first-person plural ("we can do it"),
or other constructions.

First person plural ("we") should only be used 
when speaking of the ODK project team
("We recommend...").

.. _ordered-vs-unordered:

Ordered and unordered lists
-----------------------------

An ordered list is numbered. It should be used when the order of the list is essential. For example, when enumerating a series of steps in a procedure.

.. rubric:: Wrong

.. code-block:: rst

  - First we do this.
  - And then we do this.
  - And then we do this.
  
.. rubric:: Right

.. code-block:: rst

  1. Do this.
  2. Do this.
  3. Do this.
  
An unordered list is bulleted. It should be used for a collection of items in which order is not essential.

.. rubric:: Wrong

.. code-block:: rst

  1. apples
  2. oranges
  3. bananas
  
.. rubric:: Right

.. code-block:: rst

  - apples
  - oranges
  - bananas

.. _avoid-latin:

Avoid Latin
-------------

Several Latin abbreviations are common in written English:

.. startignore

 - etc.
 - i.e.
 - e.g.
 - viz.
 - c.f.
 - n.b.
 - ibid.
 - q.v.

.. endignore
 
At best, these present a minor barrier to understanding. This is often made worse by unintentional misuse.

Avoid Latin abbreviations.

.. rubric:: Wrong

.. code-block:: rst

  If you are writing about a specific process (e.g., installing an application)...
  
.. rubric:: Right

.. code-block:: rst

  If you are writing about a specific process (for example, installing an application)...

.. code-block:: python
  :class: style-checks

  @memoize
  def check_latin(text):
      """Avoid using Latin abbreviations."""
      err = "style-guide.latin-abbr"
      msg = "Avoid using Latin abbreviations like \"etc.\", \"i.e.\"."

      list = [
          "etc\.", "etc", "\*etc\.\*", "\*etc\*",
          "i\.e\.", "ie", "\*ie\.\*", "\*ie\*",
          "e\.g\.", "eg", "\*eg\.\*", "\*eg\*",
          "viz\.", "viz", "\*viz\.\*", "\*viz\*",
          "c\.f\.", "cf", "\*cf\.\*", "\*cf\*",
          "n\.b\.", "nb", "\*nb\.\*", "\*nb\*",
          "q\.v\.", "qv", "\*qv\.\*", "\*qv\*",
          "ibid\.", "ibid", "\*ibid\.\*", "\*ibid\*",
        ]

      return existence_check(text, list, err, msg, ignore_case=True)


.. startignore

.. _etc:
  
Etc.
~~~~~~~~

*Et cetera* (or *etc.*) deserves a special mention.

*Et cetera* means "and all the rest," and is often used to indicate that there is more that could or should be said, but which is being omitted.

Writers often use *etc.* to gloss over details of the subject which they are not fully aware of. If you find yourself tempted use *etc.*, ask yourself if you really understand the thing you are writing about.


.. _avoid-unneeded-words:

Avoid unneeded words
-----------------------

.. _adverbs:

Adverbs
~~~~~~~~~~~

Adverbs often contribute nothing. Common offenders include:

 - simply
 - easily
 - just
 - very
 - really
 - basically
 - extremely
 - actually

.. rubric:: Wrong

.. code-block:: rst

  To open the file, simply click the button.
  
.. rubric:: Right

.. code-block:: rst

  To open the file, click the button.
  
.. rubric:: Wrong

.. code-block:: rst

  You can easily edit the form by...
  
.. rubric:: Right

.. code-block:: rst

  To edit the form...

.. code-block:: python
  :class: style-checks

  @memoize
  def check_adverb(text):
      """Avoid using unneeded adverbs."""
      err = "style-guide.unneed-adverb"
      msg = "Avoid using unneeded adverbs like \"just\", \"simply\"."

      list = [
          "simply",
          "easily",
          "just",
          "very",
          "really",
          "basically",
          "extremely",
          "actually",
      ]

      return existence_check(text, list, err, msg, ignore_case=True)

  
.. _filler-phrases:  
  
Filler words and phrases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many words and phrases provide no direct meaning. They are often inserted to make a sentence seem more formal, or to simulate a perceived style of business communication. These should be removed.

Common filler phrases and words include:

- to the extent that
- for all intents and purposes
- when all is said and done
- from the perspective of
- point in time

This list is not exhaustive. These "canned phrases" are pervasive in technical writing. Remove them whenever they occur.

.. code-block:: python
  :class: style-checks

  @memoize
  def check_filler(text):
      """Avoid using filler phrases."""
      err = "style-guide.filler-phrase"
      msg = "Avoid using filler phrases like \"to the extent that\"."

      list = [
          "to the extent that",
          "when all is said and done",
          "from the perspective of",
          "point in time",
      ]

      return existence_check(text, list, err, msg, ignore_case=True)


.. endignore

.. _semicolons:

Semicolons
-------------

Semicolons are used to separate two independent clauses which could stand as individual sentences but which the writer feels would benefit by close proximity.

Semicolons can almost always be replaced with periods (full stops). This rarely diminishes correctness and often improves readability.

.. rubric:: Correct

.. code-block:: rst

  These "canned phrases" are pervasive in technical writing; remove them whenever they occur.
  
.. rubric:: Better

.. code-block:: rst

  These "canned phrases" are pervasive in technical writing. Remove them whenever they occur.

.. code-block:: python
  :class: style-checks

  @memoize
  def check_semicolon(text):
      """Avoid using semicolon."""
      err = "style-guide.check-semicolon"
      msg = "Avoid using semicolon."
      regex = ";"

      return existence_check(text, [regex], err, msg, require_padding=False)


.. _pronouns:
    
Pronouns
----------

.. _third-person-pronouns:

Third-person personal pronouns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. startignore

Third-person personal pronouns are:

- he/him/his
- she/her/her(s)
- they/them/their(s) 

.. note:: 

  While some people consider *they/them/their* to be non-standard (or "incorrect") as third-person singular, it has gained wide use as a gender-neutral or gender-ambiguous alternative to *he* or *she*.

There are two issues with personal pronouns:

- gender bias
- clarity

To avoid gender bias, the third person gender-neutral *they/then/their(s)* is preferred over *he* or *she* pronouns when writing about abstract individuals.

.. endignore

.. rubric:: Wrong

.. code-block:: rst

  The enumerator uses his device.
  
.. rubric:: Right

.. code-block:: rst

  The enumerator uses their device.


Unfortunately, *they/them/their* is not a perfect solution. Since it is conventionally used as a plural pronoun, it can cause confusion.

Therefore, avoid the use of personal pronouns whenever possible. They are often out of place in technical writing anyway. Rewriting passages to avoid personal pronouns often makes the writing more clear.

.. rubric:: Correct

.. code-block:: rst

  When using Collect, first the enumerator opens the app on their device. Then they complete the survey.
  
.. rubric:: Better

.. code-block:: rst

  To use Collect:
  
  - open the app
  - complete the survey

.. code-block:: python
  :class: style-checks

  @memoize
  def check_pronoun(text):
      """Avoid using third-person personal pronouns."""
      err = "style-guide.personal-pronoun"
      msg = "Avoid using third-person personal pronouns like \"he\", \"she\". In case of absolute need, prefer using \"they\"."

      list = [
          "he",
          "him",
          "his",
          "she",
          "her",
          "hers",
      ]

      return existence_check(text, list, err, msg, ignore_case=True)


.. _same:  
  
"Same"
~~~~~~~~~

*Same*, when used as an impersonal pronoun, is non-standard in Modern American English. It should be avoided.

.. rubric:: Wrong

.. code-block:: rst

  ODK Collect is an Android app. The same can be used for...
  
.. rubric:: Right

.. code-block:: rst

  ODK Collect is an Android app. It can be used for...

.. rubric:: Right

.. code-block:: rst
  
  ODK Collect is an Android app that is used to...

.. code-block:: python
  :class: style-checks

  @memoize
  def check_same(text):
      """Avoid using impersonal pronoun same."""
      err = "style-guide.check-same"
      msg = "Avoid using \"The same\"."
      regex = "\. The same"

      return existence_check(text, [regex], err, msg, ignore_case=False, 
                         require_padding=False)

.. _titles-style-guide:  
  
Titles 
------------

.. _title-casing:

Title case and sentence case
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document titles should be in ``Title Case`` -- that is, all meaningful words are to be capitalized.

Section titles should use ``Sentence case`` -- that is, only the first word should be capitalized, along with any proper nouns or other words usually capitalized in a sentence.

.. _title-verb-forms:

Verb forms
-----------

If a document or section describes a procedure that someone might do, use a verb ending in *-ing*. (That is, a `gerund <https://en.wikipedia.org/wiki/Gerund>`_.) Do not use the "How to..." construction.

.. rubric:: Wrong

.. code-block:: rst

  How to install ODK Collect
  --------------------------
    
.. rubric:: Right

.. code-block:: rst

  Installing ODK Collect
  ----------------------
    
If section title is a directive to do something (for example, as a step in a procedure), use an imperative. 

.. code-block:: rst

  Installing ODK Aggregate
  ------------------------
  
  Download ODK Aggregate
  ~~~~~~~~~~~~~~~~~~~~~~

  Section content here.

.. code-block:: python
  :class: style-checks

  @memoize
  def check_howto(text):
      """Avoid using how to construct."""
      err = "style-guide.check-howto"
      msg = "Avoid using \"How to\" construction."
      regex = "(How to.*)(\n)([=~\-\"\*]+)"

      return existence_check(text, [regex], err, msg, require_padding=False)
  
.. _section-label-style-guide:  
  
Section labels
~~~~~~~~~~~~~~~~

Section titles should almost always be preceded by labels.

The only exception is very short subsections that repeat --- like the **Right** and **Wrong** titles in this document or the **XLSForm Rows** and **XForm XML** sections in the :doc:`form-question-types` document.

In these cases, you may want to use the :rst:dir:`rubric` directive.

.. code-block:: python
  :class: extra-checks

  def check_label(text):
      """Prefer giving a section label."""
      err = "style-guide.check-label"
      msg = "Add a section label if required."
      regex = r"(.*\n)(( )*\n)(.+\n)(([=\-~\"\']){3,})"

      errors = []
      sym_list = ['===','---','~~~','"""','\'\'\'']
      is_doc_title = True

      for matchobj in re.finditer(regex, text):
          if is_doc_title:
              is_doc_title = False
              continue
          label = matchobj.group(1)
          start = matchobj.start()+1
          end = matchobj.end()
          (row, col) = line_and_column(text, start)
          row = row + 2
          if any(word in text.splitlines(True)[row] for word in sym_list):
              row = row - 1
          col = 0
          extent = matchobj.end()-matchobj.start()
          catches = tuple(re.finditer(r"\.\. _", label))
          if not len(catches):
              errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]

      return errors       

    
.. _other-title-considerations:
      
Other titling considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Do not put step numbers in section titles.
- Readers skim. Section titles should be clear and provide information.

  
.. _writing-about-code:
  
Writing code and writing about code
======================================

ODK Documentation includes code samples in a number of languages. Make sure to follow generally accepted coding style for each language. 

.. _indenting:

Indenting
------------

In code samples:

- Use spaces, not tabs.
- Two spaces for logical indents in most languages.

  - Python samples must use `four spaces per indent level <https://www.python.org/dev/peps/pep-0008/#indentation>`_.
  
- Strive for clarity. Sometimes nonstandard indentation, especially when combined with non-syntactic line breaks, makes things easier to read.

  - Make sure that line breaks and indentation stay within the valid syntax of the language.

Using two spaces keeps code sample lines shorter, which makes them easier to view.

.. rubric:: Example of indenting for clarity

.. code-block:: HTTP

  HTTP/1.0 401 Unauthorized
  Server: HTTPd/0.9
  Date: Sun, 10 Apr 2005 20:26:47 GMT
  WWW-Authenticate: Digest realm="testrealm@host.com",
			   qop="auth,auth-int",
			   nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
			   opaque="5ccc069c403ebaf9f0171e9517f40e41"
  Content-Type: text/html
  Content-Length: 311

.. _meaningful-names:

Meaningful names
-----------------

When writing sample code, avoid meaningless names.

.. rubric:: Wrong

.. code-block:: python

  def myFunction(foo):

    for bar in foo:
       bar[foo] = foo[spam] + spam[foo]

    return foobar

.. _xml-html-style-guide:

XML and HTML
---------------

Some of the terms often used to describe XML and HTML code structures are imprecise or confusing. For clarity, we restrict certain terms and uses.

Likewise, coding practices and styles for XML and HTML vary widely. For the sake of clarity and consistency, samples should follow the guidelines set forth here.

.. _xml-element:

Element
~~~~~~~~~~~

The following piece of code represents an **element**:

.. code-block:: xml

  <element>
    Some content.
  </element>

.. note:: 

  An element is **not** a *block* or a *tag*.
  
  - *Tag* is defined below.
  - *Block* has a specific meaning in HTML and XML templates, and should generally be avoided outside those contexts.

.. _xml-tag:
  
Tag
~~~~~~

A **tag** is the token that begins or ends an element.

.. code-block:: xml

  <element>  <!-- The opening tag of this element. -->
    Some content.
  </element> <!-- The closing tag. -->
  
The word *tag* has often been used to refer to the entire element. For clarity, we will avoid that here.


.. _xml-node:

Node
~~~~~

The word *node* is often used interchangeably with *element*.

For clarity, we make the following distinction:

- An HTML or XML document has *elements*, not *nodes*.
- A *node* is part of a "live" DOM tree or other dynamic representation.

  - An XML or HTML element becomes an *element node* in a DOM tree.
  - There are also other types of nodes in a DOM tree.

.. _xml-attributes-values:

Attributes and values
~~~~~~~~~~~~~~~~~~~~~~~

An element may have attributes. Attributes have values. Values are wrapped in straight double-quotes.

.. code-block:: xml

  <element attribute="value">
    Content.
  </element>
  
Other names for attributes, such as *variables* or *properties*, should be avoided.

.. _xml-element-content:
  
Element content
~~~~~~~~~~~~~~~~

The code between the opening and closing tags of an element is the content. Content can include other elements, which are called *child elements*.

.. code-block:: xml

  <element>
    Content.
    <child-element>
      More content.
    </child-element>
  </element>
  
When an element is empty, it can be called a *null element*.

.. code-block:: xml

  <null-element attribute="value" />

In XML, null element tags always self-close. This is not the case in HTML. 

- HTML elements that are always null (for example, `<img>`) do not need to be self-closed.
- Empty HTML elements that normally accept content have a separate closing tag.

.. code-block:: html

  <img src="awesome-picture.jpeg">

  <script src="some-javascript.js"></script>

.. _xml-capitalization:
  
Capitalization
~~~~~~~~~~~~~~~~

For all HTML samples, tag names and attribute names should be ``all lowercase``. 

Newly-written XML examples should also be ``all lowercase``.

XML examples that show actual code generated by tools in the ODK ecosystem should replicate that code exactly, regardless of its capitalization practice.

.. _odk-jargon:

ODK jargon
=============

.. _writing-about-odk:

ODK and ODK Docs
-------------------

.. startignore

.. rubric:: Wrong

- Odk
- odk
- Open data kit
- OpenDataKit
- the Open Data Kit
- ODK docs
- ODK documentation

.. rubric:: Right

- ODK
- Open Data Kit
- ODK Docs
- ODK Documentation

.. rubric:: Probably want to avoid...

- Open Data Kit Documentation

.. code-block:: python
  :class: style-checks

  @memoize
  def check_odkspell(text):
      """ODK spelling usage."""
      err = "style-guide.spelling-odk"
      msg = "ODK spell check. '{}' is the preferred usage."

      preferences = [

          ["Open Data Kit",         ["Open data kit"]],
          ["Open Data Kit",         ["OpenDataKit"]],
          ["ODK",                   ["Odk"]],
          ["ODK",                   ["{0} odk"]],
          ["ODK Docs",              ["ODK docs"]],
          ["ODK Documentation",     ["ODK documentation"]]
      ]

      return preferred_forms_check(text, preferences, err, msg, ignore_case=False)

.. _odk-app-project-names:

ODK app and project names
---------------------------

ODK includes a number of components, including:

- Collect
- Aggregate
- Briefcase

These should always be capitalized.

The **ODK** prefix (as in, *ODK Collect*) should be used the first time a document mentions the app or project, or any other time it would be unclear.

A few projects should *always* use the **ODK** prefix:

- ODK XForm
- ODK Javarosa
- ODK Docs

.. code-block:: python
  :class: style-checks

  @memoize
  def check_appspell(text):
      """ODK spelling usage."""
      err = "style-guide.spelling-odk"
      msg = "ODK spell check. '{}' is the preferred usage."

      preferences = [
          ["Aggregate",             ["{0} aggregate"]],
          ["Briefcase",             ["{0} briefcase"]]
      ]

      return preferred_forms_check(text, preferences, err, msg, ignore_case=False)

.. _xform-xlsform:

XForms and XLSForm
-------------------

- *XForms* refers to XML-encoded forms. 
- *XLSForm* refers to a spreadsheet format used to define forms. 

.. rubric:: Wrong

- Xforms
- X-Forms
- xforms
- XFORMS
- XForm (no *s*, when referring to the specification)

- xlsform
- XLSform
- Xlsform

.. rubric:: Right

- XForms
- an Xform (when referring to a single form)
- XLSForm

.. code-block:: python
  :class: style-checks

  @memoize
  def check_formspell(text):
      """ODK spelling usage."""
      err = "style-guide.spelling-odk"
      msg = "ODK spell check. '{}' is the preferred usage."

      preferences = [
          ["XForms",                ["Xforms"]],
          ["XForms",                ["X-Forms"]],
          ["XForms",                ["{0} xforms"]],
          ["XForms",                ["XFORMS"]],
          ["an XForm",              ["a XForm"]],
          ["an XLSForm",            ["a XLSForm"]],
          ["XLSForm",               ["{0} xlsform"]],
          ["XLSForm",               ["XLSform"]],
          ["XLSForm",               ["Xlsform"]]
      ]

      return preferred_forms_check(text, preferences, err, msg, ignore_case=False)

.. _writing-about-xform:

XForms Spec, XForms Tools, XForms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*XForms* can refer to:

- The `XML-based form format <https://en.wikipedia.org/wiki/XForms>`_
- The `official XForms specification from the W3C <https://www.w3.org/TR/2009/REC-xforms-20091020/>`_
- The `ODK XForms Specification <https://opendatakit.github.io/xforms-spec/>`_, which is a subset of the full W3C recommendation.
- The general idea of an XML-based form.

*XForm* (without an *s*) refers to:

- A specific XML document that encodes a form.

When writing about any of these things, make sure you are clear --- in your mind as well as in your writing --- which one you are talking about.

.. _writing-about-xlsform:

XLSForm
~~~~~~~~~

*XLSForm* can refer to:

- The `XLSForm format for describing form in an Excel spreadsheet <http://xlsform.org/>`_
- A spreadsheet file that describes a form using the format.
- An `online tool <https://docs.opendatakit.org/xlsform/>`_ and an `offline tool <https://gumroad.com/l/xlsform-offline>`_ for converting :file:`*.xls(x)` files to XForm documents. 

When writing about any of these things, make sure you are clear --- in your mind as well as in your writing --- which one you are talking about.

.. endignore
