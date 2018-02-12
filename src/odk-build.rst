ODK Build
===========

:dfn:`ODK Build` is a form designer with a drag-and-drop user interface. Build is an HTML5 web application and works best for designing simple forms.

.. tip::

  For a more powerful form designer from Open Data Kit, try :doc:`XLSForm <xlsform>`.

  You may also be interested in form design tools from other organizations:

  - `Vellum <https://github.com/dimagi/Vellum>`_
  - `Kobo <http://www.kobotoolbox.org/>`_
  - `Enketo <https://enketo.org/>`_ 
  - `PurcForms <https://code.google.com/archive/p/purcforms/>`_.

.. _use-build:  

Using ODK Build
----------------

Go to http://build.opendatakit.org and sign in.

.. image:: /img/odk-build/sign-in.png
   :alt: Image showing sign in window.

.. note::
  
  There is a `downloadable version of ODK Build <https://opendatakit.org/downloads/download-category/build/>`_ available.

.. tip::

  Clicking on :menuselection:`About ODK Build...` option in the :guilabel:`Help` menu provides basic information about ODK Build.

  .. image:: /img/odk-build/about.png
    :alt: Image showing information about ODK Build.


.. _create-forms:

Creating and Saving forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Options to create, open and save forms are available in the :guilabel:`File` menu.

.. image:: /img/odk-build/file-menu.png
   :alt: Image showing file menu dropdown.

- Click on :menuselection:`New Form` to start creating a new form.

.. tip::

  When you start building a form on ODK Build, it is named as *Untitled Form*. To rename it click on :guilabel:`rename` next to the form name and give a name to your form.

  .. image:: /img/odk-build/rename.png
    :alt: Image showing rename option.  

- Click on :menuselection:`Open Form...` to open a saved form and edit it. Select the form and click on :guilabel:`Open` option in the open form window. You can also delete a saved form by clicking on :guilabel:`X` beside the form name.

.. image:: /img/odk-build/open-form.png
   :alt: Image showing open form window.

- To save a form click on :menuselection:`Save`. If you want to save an edited version of a previously saved form as a new form, click on :menuselection:`Save Form as...` and provide a name to the form.
- To save your form on your local machine, click on :menuselection:`Save Form to File...`. You can open a form saved into your local machine by clicking on :menuselection:`Load Form from File...`.

.. note::

  Forms which are saved to your local machine have extension :file:`.odkbuild` and only these forms can be loaded into ODK Build.  

.. _build-forms:

Form building
~~~~~~~~~~~~~~~

- Add a new prompt, by dragging the elements from the bottom of the screen onto the blank canvas. 
- You can remove a prompt by clicking on :guilabel:`X` sign on the prompt.

.. image:: /img/odk-build/remove-prompt.png
   :alt: Image showing remove prompt option.

- For each prompt, modify its properties on the right portion of the screen. 

.. image:: /img/odk-build/properties.png
   :alt: Image showing properties section.

- Prompts can also be rearranged through drag and drop.

- You can collapse the question prompts by checking the :menuselection:`Collapse Questions` option in the :guilabel:`View` menu.

.. image:: /img/odk-build/view-menu.png
   :alt: Image showing view menu dropdown.

.. image:: /img/odk-build/collapse-question.png
   :alt: Image showing collapsed questions.

- Information about prompts is displayed in the properties section.

.. image:: /img/odk-build/information-text.png
   :alt: Image showing information text.

- Unchecking the :menuselection:`Show Information` option in the :guilabel:`Help` menu will hide the information which is displayed in properties section.

.. image:: /img/odk-build/help-menu.png
   :alt: Image showing help menu dropdown.   
   
.. _upload-forms:

Upload forms to Aggregate
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can upload a form to Aggregate server by clicking on :menuselection:`Upload Form to Aggregate...` in the :guilabel:`File` menu. In the window which opens up, enter the url for your Aggregate server. In the username and password box, you need to enter your Aggregate account credentials with Form Manager or greater capabilities. The account type in Aggregate has to be ODK, not Google. You may leave these blank if your Aggregate instance allows anonymous form uploading.  

.. image:: /img/odk-build/upload-form.png
   :alt: Image showing upload form window.  

.. _forms-export:

Export forms
~~~~~~~~~~~~~   

- To view XML for your form, click on :menuselection:`Export to XML...` in the :guilabel:`File` menu. You can download the :file:`.xml` file for your form by clicking on :guilabel:`Download` option in the output XML window.

.. image:: /img/odk-build/download-xml.png
   :alt: Image showing Download option.

- You can download :file:`.xlsx` file for your form by clicking on :menuselection:`Export to XLSForm` in the :guilabel:`File` menu.

.. _form-properties:

Changing form properties
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can change the form properties by clicking :menuselection:`Form Properties...` in the :guilabel:`Edit` menu. 

.. image:: /img/odk-build/edit-menu.png
   :alt: Image showing edit menu dropdown.

A form properties window will appear, where you can enter the instance name, public key and submission url for your form. 

.. image:: /img/odk-build/form-properties.png
   :alt: Image showing form properties window.

Instance name specifies names you want to give to submitted data. You can see more info on public key :ref:`here <construct-key>`. Submission url directs your submissions somewhere other than the Aggregate that supplied the form. This is the ODK Aggregate website url with ``Aggregate.html`` replaced by submission.

.. tip::

  You can give an instance name which uses calculated expressions to name submissions based on submission data. Note that whatever you put in the instance name box should evaluate to a string.

  For example, you might use a concatenation of a unique student ID (sid) with the student name (s_name) as the name of the filled-in form. So you can provide a instance name as : **concat(${sid},' - ', ${s_name})**.
  
  This is implemented in XML as an instanceName field within the meta block. If this value is present and not an empty string (""), it will be used as the name of the filled-in form. Otherwise, the current default naming, based upon the date the form was first saved, will be used.

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

.. _manage-translation:

Add, remove and display new languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add a new language for your form by clicking on :menuselection:`Manage Translations...` in the :guilabel:`Edit` menu. 

.. image:: /img/odk-build/translations.png
   :alt: Image showing translation window.

When you add a new language, the language box will be displayed in the properties section of the form. 

.. image:: /img/odk-build/add-translation.png
   :alt: Image showing added language in properties section.

You can also remove any translation by clicking on :guilabel:`remove` option in the Translation box.

.. image:: /img/odk-build/remove-translation.png
   :alt: Image showing remove translation option.

You can change the display language for your form by checking the language you want to use as display language in the :guilabel:`View` menu.

.. image:: /img/odk-build/display-language.png
   :alt: Image showing display language selection.   
