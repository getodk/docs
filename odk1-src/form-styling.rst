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
:ref:`markdown-in-forms` and :ref:`emoji`.


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
  :alt: A note widget in Collect. The label is a large headline reading "Largest Headline - H1". The hint text is "This note has a label with a Markdown-style header."
  
.. figure:: /img/form-styling/all-headers-label.* 
  :alt: A note widget in Collect. The label is six headlines of decreasing size, with text describing the size as: H1, H2, H3, H4, H5, H6.
     
  A comparison of headline sizes. This exact effect :ref:`cannot be produced using Markdown <one-headline-only>`.
  
  
.. warning::
  :name: one-headline-only
  
  If a Markdown header is used, 
  the label or hint can only be one line of text.
  Line breaks in the XLSForm cell will break the header styling.

  .. image:: /img/form-styling/broken-header.* 
    :alt: A note widget in Collect. The label text is "## Attempted h2 Label Header (line break) A line below the headline". The hint text is "### Attempted H3 hint headline (line break) Here is some text below the headline."

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
  :alt: A note widget in Collect. The label text is "This label has bold and italic text." The hint text is "This hint has bold and italic text." The words "bold" and "italic" are styled to appear bold and italic.
  
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
  :alt: A note widget in Collect. The label text is "This label contains a link." The hint text is "This hint contains a link." In both cases, the words "contains a link" are hyperlinks.
  
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

.. _inline-html:

Inline HTML
~~~~~~~~~~~~~

Many Markdown implementations support inline HTML,
but Collect only supports a small subset of HTML elements.
Support of HTML is further limited because:

- Your exact Android device, operating system version,
  and other device-related factors
  will affect what HTML can be rendered, and how it is rendered.
- HTML is not supported
  by other form rendering tools in the XForms ecosystem.
  For example, HTML elements that work in Collect may not work in Enketo.

For these reasons, we do not recommend using HTML in forms (except the ``<span>`` element :ref:`noted below <custom-styling>`).

.. seealso:: `The list of HTML tags currently supported in Collect <https://www.grokkingandroid.com/android-quick-tip-formatting-text-with-html-fromhtml>`_.

  
.. _custom-styling:
  
Custom font styling
---------------------

To add custom styling to hint, label, and choice labels,
use `the style attribute`_ on a :tc:`span` tag.
The :tc:`style` attribute accepts CSS-like key-value pairs for setting ``color`` and ``font-family``.

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

.. note::

   These two attributes, ``color`` and ``font-family``, are the only style attributes supported in Collect.

.. image:: /img/form-styling/going-red.* 
  :alt: A note widget in Collect. The label text is "Going red", and the word "red" is colored red. The hint text is the source markup for the label: Going <span style="color:red">red</span>
  
.. image:: /img/form-styling/going-green.* 
  :alt: A note widget in Collect. The label text is "Going green", and the word "green" is colored green. This hint text is the source markup for the label: Going <span style="color:#008000">green</span>

.. image:: /img/form-styling/cursive-text.* 
  :alt: A note widget in Collect. The label text is "Cursive text", style in a cursive font. The hint text is the source markup for the label: <span style="font-family:cursive">Cursive text</span>
    
.. image:: /img/form-styling/styled-answers.* 
  :alt: A single select widget in Collect. The label text is "Formatting works on labels for choices also." The choices are "Yes" (which is colored green) and "No" (which is colored red).
  
.. image:: /img/form-styling/combo-example.* 
  :alt: A note widget in Collect. The label text is "Color and font styling can be combined." The label is large, purple, and in cursive.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label
  
  note, red, Going <span style="color:red">red</span>
  note, green, Going <span style="color:#008000">green</span>
  note, cursive, <span style="font-family:cursive">Cursive text</span>
  select_one yn, colored_choices, Formatting works on labels for Choices also.
  note, combo, # <span style="font-family:cursive;color:purple">Color and font styling can be combined.</span>
  
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
  :alt: A single select widget in Collect. The label text is "What is your current pain level?" The options are seven increasingly-unhappy emoji faces.
  
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
