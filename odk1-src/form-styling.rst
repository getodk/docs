.. spelling::

  CSS
  Emoji
  bolding
  emoji
  md
  monospace
  supertext
  tt
  yn
	
Form Styling
==============

Labels, hints, and choices in an :doc:`xlsform`
can all be styled using 
:ref:`markdown-in-forms`, :ref:`html-in-forms`, and :ref:`emoji`.


.. _markdown-in-forms:

Markdown
---------

:doc:`xlsform` supports limited used of `Markdown`_.

.. _Markdown: https://en.wikipedia.org/wiki/Markdown

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

    
.. image:: /img/form-styling/h1-label.* 
  :alt: 
  
.. figure:: /img/form-styling/all-headers-label.* 
  :alt:
     
  A comparison of headline sizes. This exact effect :ref:`cannot be produced using Markdown <one-headline-only>`.
  
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint
  
  note, h1_label, # Largest Headline - H1, This note has a label with a Markdown-style header.
  note, all_headers, <h1>Largest Headline - H1</h1><h2>H2 Headline</h2><h3>H3 Headline</h3><h4>H4 Headline</h4><h5>H5 Headline</h5><h6>H6 Headline</h6>, Headers in the label.
  
.. warning::
  :name: one-headline-only
  
  If a Markdown header is used, 
  the label or hint can only be one line of text.
  Line breaks in the XLSForm cell will break the header styling.

  .. image:: /img/form-styling/broken-header.* 
    :alt:

  .. rubric:: XLSForm
  
  .. csv-table:: survey
    :header: type, name, label, hint
  
    note, broken_header, "| ## Attempted H2 Label Header
    | 
    | A line below the headline", "| ### Attempted H3 hint headline, 
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
  
.. _escaping-markdown:

Escaping Markdown
~~~~~~~~~~~~~~~~~~

.. versionadded:: 1.15

If you want to include literal asterisks or underscores,
escape them with a back-slash (``\``).
If you want to include a literal back-slash,
you'll need to escape that too.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, hint
  
  note, escape_md, \# This headline is normal sized, \*Asterisks\* and \_underscores\_ and one slash: \\
  
  
.. _html-in-forms:
  
HTML
-----

Collect forms support `a subset of HTML elements`__.

__ https://www.grokkingandroid.com/android-quick-tip-formatting-text-with-html-fromhtml/

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
  ":tc:`<span>`", "span (generic inline element, used for styling)"
  
.. warning::

  `Enketo`_ does not support HTML in forms.
  For Enketo compatibility,
  stick to :ref:`markdown-in-forms`.
  
  .. _Enketo: https://enketo.org/
  
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
The :tc:`style` attribute accepts CSS-like key-value pairs for setting color and font-family.

.. _the style attribute: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style 

- For ``color``, try one of the `named HTML color values`_ or use a `hex color`_.
- For ``font-family``, it is best to use `generic font categories`_
  rather than specific fonts:
  
  - serif
  - sans-serif
  - monospace
  - cursive
  - fantasy
  
  This will ensure support across most devices.
  You can also use specific font choices,
  but you should test these on the actual devices being used.

.. _named HTML color values: https://html-color-codes.info/color-names/
.. _hex color: http://www.color-hex.com/
.. _generic font categories: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#%3Cgeneric-name%3E
 
.. image:: /img/form-styling/going-red.* 
  :alt:
  
.. image:: /img/form-styling/going-green.* 
  :alt:

.. image:: /img/form-styling/cursive-text.* 
  :alt:
    
.. image:: /img/form-styling/styled-answers.* 
  :alt:
  
.. image:: /img/form-styling/combo-example.* 
  :alt:

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label
  
  note, red, Going <span style="color:red">red</span>
  note, green, Going <span style="color:#008000">green</span>
  note, cursive, <span style="font-family:cursive">Cursive text</span>
  select_one yn, colored_choices, Formatting works on labels for Choices also.
  note, combo, <h1> <span style="font-family:cursive;color:purple">Color and font styling can be combined.</span></h1>
  
.. csv-table:: choices
  :header: list_name, name, label

    yn, yes, <span style="color:green">Yes</span>
    yn, no, <span style="color:red">No</span>

.. _emoji:
    
Emoji
------

Emoji can be used in form labels, hints, and answer choices.

.. note::

  The exact visual representation of each emoji character
  is controlled by the device operating system,
  and may vary from device to device.
  If possible,
  you should check how your rendered forms look
  on the devices you are using for data collection.

.. image:: /img/form-styling/emoji.* 
  :alt:
  
.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label
  
  select_one pain, pain_level, What is your current pain level?
  
.. csv-table:: choices
  :header: list_name, name, label
  
  pain, 1, 🙂
  pain, 2, 😐
  pain, 3, 🙁
  pain, 4, 😦
  pain, 5, 😧
  pain, 6, 😩
  pain, 7, 😱

  
------

.. seealso:: 
  
  - `Styling prompts in XLSForm <http://xlsform.org/#styling>`_
  - :download:`Sample XLSForm with Style </downloads/form-styling/style-example.xlsx>`
