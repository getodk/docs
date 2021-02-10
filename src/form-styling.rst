.. spelling::

  CSS
  Emoji
  bolding
  dk
  emoji
  md
  monospace
  supertext
  tt
  yesnodk
  yn

Form Styling
==============

Questions can include :ref:`media` such as images, sound or video.
Additionally, labels, hints, and choices in an :doc:`xlsform`
can all be styled using
:ref:`markdown-in-forms`, :ref:`fonts and colors <custom-fonts-colors>`, and :ref:`emoji`.

.. _media:

Media
------

You can include questions in your form that display images or that play video or
audio files by including a :th:`media` column in your `XLSForm <http://xlsform.org/#media>`_.
Files referenced should be included :ref:`in your form's media folder <loading-form-media>`.

Images
~~~~~~~~

Adding an image to a question displays the image as part of the question.

.. image:: /img/form-styling/media-image.*
  :alt: A single select widget in Collect. The label text is "Do you want coffee?" The label text is accompanied by a picture of a mug of coffee. The options are "yes", "no", and "I don't know".

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, media::image

  select_one yesnodk, coffee, Do you want coffee?, mug.jpg

.. csv-table:: choices
  :header: list_name, name, label

  yesnodk, y, yes
  yesnodk, n, no
  yesnodk, dk, I don't know

Audio
~~~~~~~~

Adding audio to a question adds a play/stop button that controls the audio clip.

.. image:: /img/form-styling/audio-image.*
  :alt: A single text widget in Collect. The label text is "How does this song make you feel?" The label text is accompanied by a button to play audio.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, media::audio

  text, feel, How does this song make you feel?, amazing.mp3

Video
~~~~~~~~

Adding video to a question adds a button that will play the video clip full screen when clicked.

.. image:: /img/form-styling/video-image.*
  :alt: A single integer widget in Collect. The label text is "How many people do you see in the video?" The label text is accompanied by a button to play video.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, media::video

  integer, people, How many people do you see in the video?, people.mp4

Autoplaying Media
~~~~~~~~~~~~~~~~~~~

Audio and video on questions can also be played automatically when a question is viewed by adding
an :th:`autoplay` column specifying either :th:`audio` or :th:`video`.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, media::audio, autoplay

  text, feel, How does this song make you feel?, amazing.mp3, audio

Some considerations for autoplaying:

* Audio/video included in select choices will be autoplayed after the question's media in display order
* If using a `field-list` appearance for a group no media will be autoplayed
* Appearances for selects that hide buttons will disable autoplay for media

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

For these reasons, we do not recommend using HTML in forms (except the ``<span>`` element :ref:`noted below <custom-fonts-colors>`).

.. seealso:: `The list of HTML tags currently supported in Collect <https://www.grokkingandroid.com/android-quick-tip-formatting-text-with-html-fromhtml>`_.


.. _custom-fonts-colors:

Fonts and colors
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


.. _alignment:

Text alignment
----------------

To add alignment to hint, label, and choice labels, use `the style attribute`_ on a :tc:`p` or :tc:`div` tag.

.. image:: /img/form-styling/text-alignment.*

.. csv-table:: survey
  :header: type, name, label, hint

  select_one options, select_question, <p style="text-align:center">Centered label</p>, <p style="text-align:center">Centered hint</p>

.. csv-table:: choices
  :header: list_name, name, label

  options, a, <p style="text-align:center">a</p>
  options, a, <p style="text-align:center">b</p>
  options, c, <p style="text-align:center">c</p>

.. note::

   The style will be applied to the list of selected choices and that this might have unexpected results especially if used with a select_multiple question.


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
