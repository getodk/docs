.. spelling::

  Anaranjado
  Azul
  Español
  Púrpura
  Qué
  Rojo
  Seleccione
  colores
  gustan
  prefs
  te
  tres
	
Form Language
===================

:doc:`collect-intro` and `XLSForm`_ support `multi-language forms`_.

.. _multi-language forms: http://xlsform.org/#language

To add additional languages to your XLSForm,
add columns of user-facing content with language-specific columns.

All columns representing user-facing text or media can be multi-lingual:

 - :th:`label`
 - :th:`hint`
 - :th:`media::*`
 - :th:`constraint_message`
 - :th:`required_message`

Each language column adds two colons and the language name,
followed by the `two letter language code` in parenthesis.

For example: 

- :th:`label::English (en)`
- :th:`hint::French (fr)`
- :th:`media::image::Español (es)`

.. note::

  All columns that can be made multi-lingual, need to be created as such for a multi-language form. For example, even if using the same image for a question prompt you will need a :th:`media::image::*` column for each language. However, you may provide the same media filename for each.

.. note::

  The text shown in Collect's user interface (e.g., buttons, menus, dialogs)
  is controlled by device language, not the form language.
  If you would like Collect's user interface to support your language,
  contribute translations at https://www.transifex.com/opendatakit.

.. _XLSForm: http://xlsform.org
.. _two letter language code: http://www.iana.org/assignments/language-subtag-registry/language-subtag-registry

.. rubric:: XLSForm -- Single language

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
  
.. image:: /img/form-language/colors-spanish.* 
  :alt: A multi-select widget in Collect. The label is "¿Qué colores te gustan?" The hint text is "Seleccione tres." The choices are Rojo, Azul, Amarillo, Verde, Anaranjado, and Púrpura.

  

.. warning:: 

  There is no fallback language.

  If you have specified languages for a column,
  the non-specific version of that column
  will be treated as if it were a separate language.
  (The :menuselection:`Change Language` menu will list it as :guilabel:`Default`.)

  Blank cells in a language-specific column
  will be blank in the form when that language is active,
  even if the "default" column has a value.

    
.. _switching-languages:
  
Switching languages
---------------------

Typically, if multiple languages are available on a form,
the form will display in the language set on the device.

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

