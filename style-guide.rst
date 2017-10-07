*****************
Style Guide
*****************


Spelling and Grammar
=======================

.. _american-spelling:

American spelling and grammar
-----------------------------

Whenever U.S. English and British (or other) English spelling or usage disagree, standard U.S. spelling and usage is preferred.

.. rubric:: Right

  The color of the button is gray.

.. rubric:: Wrong

  The colour of the button is grey

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

  Click the button that says, "Save."
  
.. rubric:: Right

  Click :guilabel:`Save`.
  
.. rubric:: Wrong

  You may see an error message that says, "Something went wrong."
  
.. rubric:: Right

  You may get an error: ``Something went wrong.``


  
Straight quotes
~~~~~~~~~~~~~~~~~~

Any time that you *do* need to use quotation marks, use straight (or *plain*) quotes. Sphinx and Docutils will output the typographically correct quote style.

Serial comma
-----------------

In a comma-delineated list of items, the penultimate item should followed by a comma.

.. rubric:: Wrong

  Apples, oraanges and pears.
  
.. rubric:: Right

  Apples, oranges, and pears.
  
In technical writer, a bulleted list is often more clear than an inline list.

.. rubric:: Correct

  You will need to be familiar with git, GitHub, and Python.
  
.. rubric:: Possibly Better

  You will need to be familiar with:
  
  - git
  - GitHub
  - Python
  
There's no hard rule about which to use in any situation. Use your judgement: try it both ways and see which is more clear.

.. _avoid-unneeded-word:

Avoid unneeded words
-----------------------

Adverbs
~~~~~~~~~~~

Adverbs often contribute nothing.

Common offenders include:

 - simply
 - easily
 - just
 - very
 - really
 - basically

.. rubric:: Wrong

  To open the file, simply click the button.
  
.. rubric:: Right

  To open the file, click the button.
  
.. rubric:: Wrong

  You can easily edit the form by...
  
.. rubric:: Right

  To edit the form...
  
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

.. _semicolons:

Semicolons
-------------

Semicolons are used to separate to independent clauses which could stand as individual sentences but which the writer feels would benefit by close proximity.

Semicolons can almost always be replaced with periods (full stops). This rarely diminishes correctness and often improves readability.

.. rubric:: Correct

  These "canned phrases" are pervasive in technical writing; remove them whenever they occur.
  
.. rubric:: Better

  These "canned phrases" are pervasive in technical writing. Remove them whenever they occur.


  
Writing code and writing about code
======================================

ODK Documentation includes code samples in a number of languages. Make sure to follow generally accepted coding style for each language. 


Indenting
------------

In code samples:

- Use spaces, not tabs.
- Two spaces for logical indents in most languages.

  - Python samples must use `four spaces per indent level <https://www.python.org/dev/peps/pep-0008/#indentation>`.
  
- Strive for clarity. Sometimes nonstandard indentation, especially when combined with non-semantic line breaks, makes things easier to read.

  - Make sure that line breaks and indentation stay within the valid syntax of the language.

Using two spaces keeps code sample lines shorter, which makes them easier to view.


.. rubric:: Example of indenting for clarity

  .. code-block: HTTP
  
    HTTP/1.0 401 Unauthorized
    Server: HTTPd/0.9
    Date: Sun, 10 Apr 2005 20:26:47 GMT
    WWW-Authenticate: Digest realm="testrealm@host.com",
			     qop="auth,auth-int",
			     nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
			     opaque="5ccc069c403ebaf9f0171e9517f40e41"
    Content-Type: text/html
    Content-Length: 311



XML and HTML
---------------

Some of the terms often used to describe XML and HTML code structures are imprecise or confusing. For clarity, we restrict certain terms and uses.

Element
~~~~~~~~~~~

The following piece code represents an **element**:

.. code-block:: xml

  <element>
    Some content.
  </element>

.. note:: 

  An element is **not** a *block* or a *tag*.
  
  - *Tag* is defined below.
  - *Block* has a specific meaning if HTML and XML templates, and should generally be avoided outside those contexts.

Tag
~~~~~~

A **tag** is the token that begins or ends an element.

.. code-block:: xml

  <element>  <!-- The opening tag of this element. -->
    Some content.
  </element> <!-- The closing tag. -->
  
The word *tag* has often been used to refer to the entire element. For clarity, we will avoid that here.


Node
~~~~~

The word *node* is often used interchangeably with *element*.

For clarity, we make the following distinction:

- An *element* is a piece of XML or HTML code.
- A *node* is an element rendered into a DOM tree or other dynamic representation.

Attributes and values
~~~~~~~~~~~~~~~~~~~~~~~

An element may have attributes. Attributes have values. Values are wrapped in straight double-quotes.

.. code-block:: xml

  <element attribute="value">
    Content.
  </element>
  
Content
~~~~~~~~~~

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

Capitalization
~~~~~~~~~~~~~~~~

For all HTML samples, tag names and attribute names should be ``all lowercase``. 

Newly-written XML examples should also be ``all lowercase``.

XML examples that show actual code generated by tools in the ODK ecosystem should replicate that code exactly, regardless of its capitalization practice.

