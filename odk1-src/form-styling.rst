.. spelling::

  CSS
  bolding
  monospace
  tt
  yn
	
Form Styling
==============

Labels, hints, and choices can all be styled in an :doc:`xlsform`.

.. seealso:: 
  
  - `Styling prompts in XLSForm <http://xlsform.org/#styling>`_
  - :download:`Sample XLSForm with Style </downloads/form-styling/style-example.xlsx>`

.. _markdown-in-forms:

Markdown
---------

:doc:`xlsform` supports limited used of `Markdown`_.

.. _markdown-headers:

Headers
~~~~~~~~

Labels and hints can be styled with one of six header levels.

.. code-block:: none

  # Header H1
  
  ## Header H2
  
  ### Header H3
  
  #### Header H4
  
  ##### Header H5
  
  ###### Header H6


If a markdown header is used, 
the label or hint can only be one line of text.
Line breaks in the XLSForm cell will break the header styling.

.. image:: /img/form-styling/h1-label.* 
  :alt:
  
.. image:: /img/form-styling/h2-label-h3-hint.* 
  :alt:

.. image:: /img/form-styling/broken-header.* 
  :alt:
     
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint
  
  note, h1_label, # Largest Headline - H1, This note has a label with a Markdown-style header.
  note, h2_label_h3_hint, ## H2 Label, ### This hint is H3.
  note, broken_header, "| ## Attempted H2 Label Header
  | 
  | A line below the headline",	"| ### Attempted H3 hint headline, 
  | 
  | Here is some text below the headline."

.. _markdown-emphasis:
  
Emphasis
~~~~~~~~~~

Collect's Markdown support also includes 
**bold** and *italic* styling.

.. code-block:: none

  _italic_

  *italic*

  __bold__

  **bold**

.. note::

  The label of a form widget is already bold,
  so bolding text within the label has no effect.
  Similarly, the hint text of a form widget is already in italics,
  so italicizing text within the hint has no effect.
  
.. image:: /img/form-styling/emphasis.* 
  :alt:
  
.. rubric:: XLSForm

.. csv-table::
  :header: type, name, hint, label
  
  note, emphasis, This label has **bold** and *italic* text., This hint has **bold** and *italic* text.  
  
.. _markdown-hyperlinks:
  
Hyperlinks
~~~~~~~~~~~
  
Collect's Markdown support include hyperlinks,
which will open in the device's default browser.

.. code-block:: none

  [Link anchor text](link.url)
  
.. image:: /img/form-styling/hyperlinks.* 
  :alt:
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint
  
  note, hyperlink, This label [contains a link](http://example.com)., This hint [contains a link](http://example.com).
  
.. _html-in-forms:
  
HTML
-----

Collect Forms support a subset of inline HTML elements.

.. csv-table::
  :header: tag, format
  
  ":tc:`<b>`", bold
  ":tc:`<i>`", italic
  ":tc:`<u>`", underline
  ":tc:`<sub>`", subtext
  ":tc:`<sup>`", supertext
  ":tc:`<big>`", big
  ":tc:`<small>`", small
  ":tc:`<tt>`", monospace (teletype)
  ":tc:`<h1>,<h2>,<h3>,<h4>,<h5>,<h6>`", headlines
  ":tc:`<font>`", font face and color
  ":tc:`<blockquote>`", for longer quotes
  ":tc:`a`", link
  ":tc:`p`", paragraph
  ":tc:`<br>`", line break
  ":tc:`<span>`", span (generic inline element, used for styling)
  
.. image:: /img/form-styling/html-styling.* 
  :alt:
  
.. csv-table:: survey
  :header: type, name, label, hint
  
  note,	html, "<h2>Label heading</h2><p>If you need a headline and additional text, use HTML instead of Markdown.</p>", <p>Hint text can have <b>bold</b>, <i>italic</i>, and <u>underlined</u> words. Words can be raised with <sup>superscript</sup> or lowered with <sub>subscript</sub>. Use <tt>tt</tt> for <tt>monospace</tt>."

  
.. _style-attribute:
  
Styling with the style attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add custom styling to hint, label, and choice labels,
use `the style attribute`_.
The :tc:`style` attribute accepts CSS-like key-value pairs for setting color font-family.

.. _the style attribute: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style 

For color, try one of the `named HTML color values`_ of use a `hex color`_.

.. _named HTML color values: https://html-color-codes.info/color-names/
.. _hex color: http://www.color-hex.com/
 
.. image:: /img/form-styling/going-red.* 
  :alt:
  
.. image:: /img/form-styling/going-green.* 
  :alt:

  
.. image:: /img/form-styling/cursive-text.* 
  :alt:
    
.. image:: /img/form-styling/styled-answers.* 
  :alt:

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label
  
  note, red, Going <span style="color:red">red</span>
  note, green, Going <span style="color:green">green</span>
  note, cursive, <span style="font-family:cursive">Cursive text</span>
  select_one yn, colored_choices, Formatting works on labels for Choices also.
  
.. csv-table:: choices
  :header: list_name, name, label

    yn, yes, <span style="color:green">Yes</span>
    yn, no, <span style="color:red">No</span>
