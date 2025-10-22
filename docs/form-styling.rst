Form Styling
==============

Questions can include :ref:`media` such as images, sound or video.
Additionally, labels, hints, and choices in an :doc:`xlsform`
can all be styled using
:ref:`markdown-in-forms`, :ref:`HTML fonts and colors <custom-fonts-colors>`, and :ref:`emoji <emoji>`.

.. warning::

  Mobile forms in Collect and Web Forms support both HTML and Markdown styling.

  Mobile forms in Enketo only support Markdown styling, and styling is not supported in web form choice labels.

.. _media:

Media
------

Images, audio and video can help make your forms more accessible, especially for enumerators or participants with lower literacy. Question labels can include any combination of images, audio and video in addition to text. You can also specify media for :ref:`select choices <image-options>`.

To specify media for a question label, use the ``image``, ``audio`` and/or ``video`` columns on the ``survey`` sheet of your :doc:`xlsform`. When a form definition includes media, Central automatically detects which files are needed and :ref:`prompts you to attach them <central-forms-attachments>`. In Collect, files are stored :ref:`in your form's media folder <loading-form-media>`.

.. seealso:: Media can be :doc:`translated <form-language>` or :ref:`used for select choices <image-options>`.

.. _media-images:

Images
~~~~~~~~

Use the ``image`` column to specify an image in addition to or instead of a text ``label``.

.. image:: /img/form-styling/media-image.*
  :alt: A single select widget in Collect. The label text is "Do you want coffee?" The label text is accompanied by a picture of a mug of coffee. The options are "yes", "no", and "I don't know".
  :class: device-screen-vertical

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, image

  select_one yesnodk, coffee, Do you want coffee?, mug.jpg

.. csv-table:: choices
  :header: list_name, name, label

  yesnodk, y, yes
  yesnodk, n, no
  yesnodk, dk, I don't know

.. _big-image:

Bigger images for panning and zooming
"""""""""""""""""""""""""""""""""""""""

If your image is large or you would like to provide an alternative image with more detail, you can specify a filename in the ``big-image`` column. The image from the ``image`` column will be displayed inline with the question and tapping on it will show the image from the ``big-image`` column in a full-screen view that allows panning and zooming.

.. rubric:: XLSForm example using ``big-image``

.. csv-table:: survey
  :header: type, name, label, image, big-image

  note, instructions, Go to the spot marked by an X. Tap the map to make it bigger., map-small.jpg, map-big.jpg

.. _label-images-best-practices:

Best practices for images
""""""""""""""""""""""""""

.. seealso:: :ref:`Using images for select choices <image-options>` and :ref:`selects with images in Web Forms <web-forms-selects-images>`

Images can make forms easier to use and more engaging. Follow these tips to create images that enhance clarity and usability.

**Tip 1: Use cohesive images to reduce cognitive load**

* Make all images the same size (e.g. 300 x 300 pixels)
* Use images with similar colors and contrast
* Center the subject with equal whitespace around it
* Keep backgrounds simple and uncluttered

.. image:: /img/form-styling/label-images-cohesive.*
  :alt: Examples of how to use images in selects. The good example has images on a white background. The bad example uses images with the subject cropped.

**Tip 2: Use icons to simplify visuals**

* Use open source libraries to find a cohesive set of icons (more details below)
* Ensure the icons are large enough to recognize and understand
* Pick distinct icons so users can tell them apart
* Use icons with high color contrast and test in both light and dark modes

.. image:: /img/form-styling/label-images-icons.*
  :alt: Examples of how to use icons in selects. User friendly example includes consistent dark blue icons and the bad example uses low contrast icons and different sizes.

**Tip 3: For images in choices, test column layouts with real users**

* Get feedback on how many columns feel comfortable to view and tap
* Consider smaller screens — more than two columns can feel crowded
* Showing too many choices at once `can overwhelm users <https://lawsofux.com/choice-overload/>`_
* If using multiple columns, icons need to be recognizable at a small scale
* Keep labels short and specific to prevent awkward wrapping

.. _label-images-icon-library:

Using an icon library
""""""""""""""""""""""

If you don't have your own icon set, there are lots of great open-source options. Using icons from the same library, with the same style and weight, will make a better user experience. If one icon is big and bold in comparison to the others, it will slow down the user's decision making process because irregularity increases effort to make decisions (`Hick's Law <https://lawsofux.com/hicks-law/>`_).

**Icon libraries**:

* `Phosphor icons <https://phosphoricons.com/>`_
* `Google icons <https://fonts.google.com/icons>`_
* `Health icons <https://healthicons.org/>`_
* `Pictogrammers <https://pictogrammers.com/library/mdi/>`_ (extension of the Google icons above)

Once you've downloaded an icon that you want to use, you may want to add some white space around it so the icon doesn't look crowded with the screen edges or other content. One way to do this is by making a copy of `our icon template in Google Draw <https://docs.google.com/drawings/d/1fMdC8ZgSIpsNpl9grXr_6YQ9MZHvUn5Wr-4JnetJYok/edit>`_. Replace the image with each of your your downloaded icons and export the images with padding.

You could also use a design tool like `Figma <https://www.figma.com/community/icons?resource_type=mixed&editor_type=all&price=all&sort_by=all_time&creators=all>`_ or `Canva's icon maker <https://www.canva.com/create/icons/>`_ to create equal spacing around your icon or create your own.

.. _label-images-accessible:

Making images accessible
""""""""""""""""""""""""""

Whether you're using images or icons, you should generally supplement them with brief written text in the ``label`` or ``hint``. When designing that text:

* Avoid writing "Image or picture of"
* Keep it short and specific
* Focus on the details

Audio
~~~~~~~~

Adding audio to a question adds a play/stop button that controls the audio clip.

.. image:: /img/form-styling/audio-image.*
  :alt: A single text widget in Collect. The label text is "How does this song make you feel?" The label text is accompanied by a button to play audio.
  :class: device-screen-vertical

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, audio

  text, feel, How does this song make you feel?, amazing.mp3

Video
~~~~~~~~

Adding video to a question adds a button that will play the video clip full screen when clicked.

.. image:: /img/form-styling/video-image.*
  :alt: A single integer widget in Collect. The label text is "How many people do you see in the video?" The label text is accompanied by a button to play video.
  :class: device-screen-vertical

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, video

  integer, people, How many people do you see in the video?, people.mp4

Autoplaying Media
~~~~~~~~~~~~~~~~~~~

Audio and video on questions can also be played automatically when a question is viewed by adding
an ``autoplay`` column specifying either ``audio`` or ``video``.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, audio, autoplay

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


A comparison of headline sizes. This exact effect :ref:`cannot be produced using Markdown <one-headline-only>`.

.. image:: /img/form-styling/all-headers-label.*
  :alt: A note widget in Collect. The label is six headlines of decreasing size, with text describing the size as: H1, H2, H3, H4, H5, H6.
  :class: device-screen-vertical

.. warning::
  :name: one-headline-only

  If a Markdown header is used,
  the label or hint can only be one line of text.
  Line breaks in the XLSForm cell will break the header styling.

  .. image:: /img/form-styling/broken-header.*
    :alt: A note widget in Collect. The label text is "## Attempted h2 Label Header (line break) A line below the headline". The hint text is "### Attempted H3 hint headline (line break) Here is some text below the headline."
    :class: device-screen-vertical

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

.. note::

  Single underscores are only treated as markdown when separated by white space. Example:
    - ✓ ``This text contains _italic_`` will be treated as markdown
    - ✕ ``This text contains_italic_`` will not be treated as markdown

.. image:: /img/form-styling/emphasis.*
  :alt: A note widget in Collect. The label text is "This label has bold and italic text." The hint text is "This hint has bold and italic text." The words "bold" and "italic" are styled to appear bold and italic.
  :class: device-screen-vertical

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
  :class: device-screen-vertical

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, hint

  note, hyperlink, This label [contains a link](http://example.com)., This hint [contains a link](http://example.com).

.. _escaping-markdown:

Escaping Markdown
~~~~~~~~~~~~~~~~~~

If you want to include literal asterisks or underscores,
escape them with a back-slash (``\``).
If you want to include a literal back-slash,
you'll need to escape that too.

.. rubric:: XLSForm

.. csv-table::
  :header: type, name, label, hint

  note, escape_md, \\# This headline is normal sized, An asterisk: \\* and an underscore: \\_ and one slash: \\\\\\

.. _inline-html:

Inline HTML
~~~~~~~~~~~~~

Many Markdown implementations support inline HTML,
but Collect and Web Forms only support a small subset of HTML elements.
Support of HTML is further limited because:

- Your exact device, operating system version,
  and other device-related factors
  will affect what HTML can be rendered, and how it is rendered.
- HTML is not supported
  by other form rendering tools in the XForms ecosystem.
  For example, HTML elements that work in Collect's mobile forms will not work in Central's Enketo-powered web forms.

For these reasons, we do not recommend using HTML in forms (except the ``<span>`` element :ref:`noted below <custom-fonts-colors>`).

.. seealso:: `The list of HTML tags currently supported in Collect <https://www.grokkingandroid.com/android-quick-tip-formatting-text-with-html-fromhtml>`_.


.. _custom-fonts-colors:

Fonts and colors
---------------------

To add custom styling to hint, label, and choice labels,
use `the style attribute`_ on a ``span`` tag.
The ``style`` attribute accepts CSS-like key-value pairs for setting ``color`` and ``font-family``.

.. _the style attribute: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style

- For ``color``, try one of the `named HTML color values`_ or use a `hex color`_.
- For ``font-family``, it is best to use `generic font categories`_
  rather than specific fonts:

  - serif
  - sans-serif
  - monospace
  - cursive

  This will ensure support across most devices.
  You can also use specific font choices,
  but you should test these on the actual devices being used.

.. _named HTML color values: https://html-color-codes.info/color-names/
.. _hex color: http://www.color-hex.com/
.. _generic font categories: https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#%3Cgeneric-name%3E

.. image:: /img/form-styling/fonts-good-and-bad-tips.*
  :alt: Use high-contrast colors and accessible fonts to enhance readability for all users

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

To add alignment to hint, label, and choice labels, use `the style attribute`_ on a ``p`` or ``div`` tag.

.. image:: /img/form-styling/text-alignment.*
  :class: device-screen-vertical

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
  :class: device-screen-vertical

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

  - :download:`Sample XLSForm with Style </downloads/form-styling/style-example.xlsx>`
