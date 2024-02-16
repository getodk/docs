Form language
===================

.. seealso::

  Guide: :doc:`guide-form-language`

:doc:`XLSForm <xlsform>` supports multi-language forms.

To add additional languages to your XLSForm,
add columns of user-facing content with language-specific columns. All columns from the ``survey`` and ``choices`` sheets representing user-facing text or media can be multi-lingual:

- ``label``
- ``hint``
- ``image``
- ``audio``
- ``video``
- ``constraint_message``
- ``required_message``
- ``guidance_hint``

Each language column adds two colons and the language name,
followed by the `two letter language code <http://www.iana.org/assignments/language-subtag-registry/language-subtag-registry>`_ in parentheses. For example:

- ``label::English (en)``
- ``hint::Arabic (ar)``
- ``image::Español (es)``

.. note::

  The text shown in Collect's user interface (e.g., buttons, menus, dialogs) is controlled by application, not the form. See :ref:`user interface settings <interface-settings>` for how to change the interface language.

  If you are using a RTL language (e.g., Arabic), set both Collect's user interface language and the form language to ensure proper RTL layout.

.. rubric:: XLSForm --- Single language

.. csv-table:: survey
  :header: type, name, label, hint

  select_multiple colors, color_prefs, What colors do you like?, Select three.

.. csv-table:: choices
  :header: list_name, name, label

  colors, red, Red
  colors, blue, Blue
  colors, yellow, Yellow
  colors, green, Green
  colors, orange, Orange
  colors, purple, Purple

.. rubric:: XLSForm --- Multiple languages

.. csv-table:: survey
  :header: type, name, label::English (en), label::Español (es), hint::English (en), hint::Español (es)

  select_multiple colors, color_prefs, What colors do you like?, ¿Qué colores te gustan?, Select three., Seleccione tres.

.. csv-table:: choices
  :header: list_name, name, label::English (en), label::Español (es)

  colors, red, Red, Rojo
  colors, blue, Blue, Azul
  colors, yellow, Yellow, Amarillo
  colors, green, Green, Verde
  colors, orange, Orange, Anaranjado
  colors, purple, Purple, Púrpura


.. image:: /img/form-language/colors-english.*
  :alt: A multi-select widget in Collect. The label is "What colors do you like?" The hint text is "Select three." The choices are: Red, Blue, Yellow, Green, Orange, and Purple.
  :class: device-screen-vertical

.. image:: /img/form-language/colors-spanish.*
  :alt: A multi-select widget in Collect. The label is "¿Qué colores te gustan?" The hint text is "Seleccione tres." The choices are Rojo, Azul, Amarillo, Verde, Anaranjado, and Púrpura.
  :class: device-screen-vertical



.. warning::

  There is no fallback language.

  If you have specified languages for a column,
  the non-specific version of that column
  will be treated as if it were a separate language.
  (The :menuselection:`Change Language` menu will list it as :guilabel:`Default`.)

  To avoid this, all columns that can be made multi-lingual need to be created
  as such for a multi-language form. For example, even if using the same image
  for a question prompt you will need a ``image::*`` column for each
  language. However, you may provide the same media filename for each.

  Blank cells in a language-specific column
  will be blank in the form when that language is active,
  even if the "default" column has a value.

.. rubric:: XLSForm --- Multiple languages with media example

.. csv-table:: survey
  :header: type, name, label::English (en), label::Español (es), image::Español (es), image::English (en)

  text, coffee, Do you want coffee?, ¿Quieres café?, mug_es.jpg, mug_en.jpg


.. _switching-languages:

Switching languages
---------------------

If your form defines multiple languages and you know most of your data collectors will need to use the same one, you should set an explicit default language. You can do this in your XLSForm's **settings** sheet:

.. rubric:: XLSForm --- setting a default language

.. csv-table:: settings
  :header: form_id, version, default_language

  my_form, 2024050301, Español (es)

Otherwise, Collect will default to the first language defined.

To switch between available languages on a form,
go to :menuselection:`⋮ --> Change Language`.

.. video:: /vid/form-language/language-switch.mp4

.. note::

  Collect will remember the last language
  you switched to on a form,
  even if you switch device language.

  Changing the form's language display
  will not change the device language.
  If you are in a context that requires switching languages often,
  make sure you know where to do this in your device's
  :menuselection:`Settings` menu.

