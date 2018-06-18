Form Anatomy
==============

Form settings
-------------

In an XLSForm,
form settings such as title, id, and version number 
are defined in the **settings** tab of your spreadsheet.

.. csv-table:: settings
  :header: form_title, form_id, version
  
  Form Title, form_id, version


.. image:: /img/form-anatomy/form-in-list.* 
  :alt: The Fill Blank Form menu in the Collect app, 
        listing several forms available to fill out. 
	Highlighted is a form titled "Form Title". 
	The version string is "version".
 
:th: form_title
  The form title appears in all form list menus in Collect.
  If :th:`form_title` is not set in the XLSForm, 
  the file name of the :file:`.xls(x)` file
  (without the extension) 
  becomes the form_title at conversion.
  
  Form titles can include most characters, 
  including capital and lowercase letters,
  numbers, spaces, separators,
  and even emoji.
  
:th: form_id
  The form id is used to uniquely identify form definitions.
  If no form_id is set in the XLSForm,
  the file name of the :file:`.xls(x)` file
  becomes the form_id at conversion.
  
  We recommend that :th:`form_id` strings:
  
  - use ASCII characters (no emoji or international characters)
  - begin with a letter (not a number)
  - avoid spaces (use hyphens or underscores)
   
  Also, since :th:`form_id` is case sensitive,
  sticking with all lowercase letters
  will help you avoid common naming accidents.
  
:th:`version`
  The version number distinguishes between
  successive updates to a form definition.
  
  The :th:`version` attribute will accept non-number characters 
  and sequencing 
  (that is, how ODK knows determines that one version 
  is later than another verison)
  is based on lexical ordering.
  This means that :tc:`10` comes before `2`.
  
  .. tip::

    We recommend using a date string 
    and appending a two-digit revision number,
    in the form ``YYYYMMDDrr``.
    
    In this format, an update published on June 1, 2018
    would have the version number :tc:`2018060101`.
    A second revision published the same day would be :tc:`2018060102`.
    
    Alternate formats work, of course. 
    You just need to take lexical ordering into account.
    
  .. seealso:: :doc:`form-update` 

.. _form-question-anatomy:   

Form questions
---------------


.. csv-table:: survey
  :header: type, name, label, hint
  
  begin group, group-1, Group Label, Group hint
  string, labeled, Label, hint
  end group, ,


.. image:: /img/form-anatomy/model-form-question.* 
  :alt: A text question in the Collect app. 
        The form title is "Form Title". 
	The group name is "Group Name". 
	The label is "Label". 
	The hint text is "hint".
	The device keyboard is open.


:th:`name`
  Each form question and group must have a unique name.
  
  - Names can include letters or numbers,
    but should not begin with a number.
  
  - Names must not include spaces.
    (Forms that include row names with spaces
    will fail silently, causing unexpected problems.)

  - Names must not be repeated in the form.
  
:th:`label`
  The main question text that displays to the user.
  This can include :doc:`limited styling <form-styling>`,
  and can also be :doc:`internationalized <form-language>`.
  
  When questions are grouped,
  the :th:`label` attribute of the :tc:`begin group` or `begin repeat` row
  is displayed on individual widgets in the group,
  above the question label.
  (See the image above.)
  In the case of nest groups,
  the inner-most group label is shown on any question.
  
  Question and group labels also appear in the :ref:`jump menu <jump-menu>`.
  When a group is nested directly inside a repeat group,
  the inner group name is used in the jump menu.
  
:th:`hint`
  Explanatory text displayed to the user.
  
  The hint text can include :doc:`limited styling <form-styling>`
  and can also be :doc:`internationalized <form-language>`.
