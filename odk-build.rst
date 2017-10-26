ODK Build
===========

:dfn:`ODK Build` is a form designer with a drag-and-drop user interface. Build is an HTML5 web application and works best for designing simple forms.

.. tip::

  For more powerful form designers, try :doc:`XLSForm <xlsform>`, `Vellum <https://github.com/dimagi/Vellum>`_, or `Kobo <http://www.kobotoolbox.org/>`_, or `Enketo <https://enketo.org/>`_ or `PurcForms <https://code.google.com/archive/p/purcforms/>`_.

.. _use-build:  

Using ODK Build
----------------

.. _create-form:

Form building
~~~~~~~~~~~~~~~

- Go to http://build.opendatakit.org and sign in.

.. image:: /img/odk-build/sign-in.png
   :alt: Image showing sign in window.

.. note::
  
  There is a `downloadable version of ODK Build <https://opendatakit.org/downloads/download-category/build/>`_ available.

- Add a new prompt, by dragging the elements from the bottom of the screen onto the blank canvas. 
- You can remove a prompt by clicking on :guilabel:`X` sign on the prompt.

.. image:: /img/odk-build/remove-prompt.png
   :alt: Image showing remove prompt option.

- For each prompt, modify its properties on the right portion of the screen. 

.. image:: /img/odk-build/properties.png
   :alt: Image showing properties section.

- Prompts can also be rearranged through drag and drop.

.. tip::

  When you start building a form on ODK Build, it is named as *Untitled Form*. To rename it click on :guilabel:`rename` next to the form name and give a name to your form.

.. image:: /img/odk-build/rename.png
   :alt: Image showing rename option.  

.. _build-menu:  

Build Menus
~~~~~~~~~~~~~~

.. _file-menu:

File Menu
"""""""""""

.. image:: /img/odk-build/file-menu.png
   :alt: Image showing file menu dropdown.

- Click on :menuselection:`New Form` to start creating a new form.
- Click on :menuselection:`Open Form...` to open a saved form and edit it. Select the form and click on :guilabel:`Open` option in the open form window. You can also delete a saved form by clicking on :guilabel:`X` beside the form name.

.. image:: /img/odk-build/open-form.png
   :alt: Image showing open form window.

- To save a form click on :menuselection:`Save`. If you want to save a edited version of a previously saved form as a new form, click on :menuselection:`Save Form as...` and provide a name to the form.
- To save your form on your local machine, click on :menuselection:`Save Form to File...`. You can open a form saved into your local machine by clicking on :menuselection:`Load Form from File...`.

.. note::

  Forms which are saved to your local machine have extension :file:`.odkbuild` and only these forms can be loaded into ODK Build.

- You can uplaod a form to Aggregate server by clicking on :menuselection:`Upload Form to Aggregate...`. In the window which opens up, enter the url for your Aggregate server. In the username and password box, you need to enter your Aggregate account credentials with Form Manager or greater capabilities. The account type in Aggregate has to be ODK, not Google. You may leave these blank if your Aggregate instance allows anonymous form uploading.  

.. image:: /img/odk-build/upload-form.png
   :alt: Image showing upload form window.  

- To view XML for your form, click on :menuselection:`Export to XML...`. You can download the :file:`.xml` file for your form by clicking on :guilabel:`Download` option in the ouput XML window.

.. image:: /img/odk-build/download-xml.png
   :alt: Image showing Download option.

- You can download :file:`.xlsx` file for your form by clicking on :menuselection:`Export to XLSForm.`

.. _edit-menu:

Edit Menu
""""""""""

.. image:: /img/odk-build/edit-menu.png
   :alt: Image showing edit menu dropdown.

You can add a new language for your form by clicking on :menuselection:`Manage Translations...`. 

.. image:: /img/odk-build/translations.png
   :alt: Image showing translation window.

When you add a new language, the language box will be displayed in the properties section of the form. 

.. image:: /img/odk-build/add-translation.png
   :alt: Image showing added language in properties section.

You can also remove any translation by clicking on :guilabel:`remove` option in the Translation box.

.. image:: /img/odk-build/remove-translation.png
   :alt: Image showing remove translation option.

You can change the form properties by clicking :menuselection:`Form Properties...`. A form properties window will appear, where you can enter the instance name, public key and submission url for your form. 

.. image:: /img/odk-build/form-properties.png
   :alt: Image showing form properties window.

Instance name specifies names you want to give to submiited data. You can see more info on public key :ref:`here <construct-key>`. Submission url directs your submissions somewhere other than the Aggregate that supplied the form. This is the ODK Aggregate website url with ``Aggregate.html`` replaced by submission.

.. tip::

  You can give a instance name which uses calculated expressions to name submissions based on submission data. Note that whatever you put in the instance name box should evaluate to a string.

  For example, you might use a concatenation of a unique student ID (sid) with the student name (s_name) as the name of the filled-in form. So you can provide a instance name as : **concat(${sid},' - ', ${s_name})**.
  
  This is implemented within the XML as an instanceName field within the meta block. If this value is present and not an empty string (""), it will be used as the name of the filled-in form. Otherwise, the current default naming, based upon the date the form was first saved, will be used.

  .. code-block:: xml

    <instance>
      <data id="build_example1_1508999324">
        <meta>
          <instanceID/>
          <instanceName/>
        </meta>
        <s_name/>
        <sid/>
      </data>
    </instance>   

.. figure:: /img/odk-build/instance-name.png
   :alt: Image showing instance name according to submitted data.   

   Instance name as **sid-s_name: 12345-Ankita**  

.. _view-menu:

View Menu
""""""""""

.. image:: /img/odk-build/view-menu.png
   :alt: Image showing view menu dropdown.

You can change the display language for your form by checking the language you want to use as display language.

.. image:: /img/odk-build/display-language.png
   :alt: Image showing display language selection.

You can collapse the question prompts by checking the :menuselection:`Collapse Questions` option.

.. image:: /img/odk-build/collapse-question.png
   :alt: Image showing collapsed questions.

.. _help-menu:

Help Menu
""""""""""

.. image:: /img/odk-build/help-menu.png
   :alt: Image showing help menu dropdown.

Unchecking the :menuselection:`Show Information` option will hide the information which is displayed in properties section.

.. image:: /img/odk-build/information-text.png
   :alt: Image showing information text.

Clicking on :menuselection:`About ODK Build...` option provides basic information about ODK Build.

.. image:: /img/odk-build/about.png
   :alt: Image showing information about ODK Build.
