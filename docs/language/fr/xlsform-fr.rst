XLSForm
=======

.. _xlsform-introduction:

:dfn:`XLSForm` est un standard pour concevoir des formulaires dans Excel. Les formulaires XLSForm (XLSForms dans la suite de la page) sont simples à prendre en main et le standard permet de définir des formulaires complexes. 

Les formulaires XLSForm peuvent être créés et modifiés par toute application permettant de produire des documents ``.xlsx``. Cela signifie qu'ils sont "portables" et qu'ils peuvent tirer parti de nombreuses fonctions généralement disponibles dans les tableurs, telles que les formules, les commentaires et la gestion des versions. 

De nombreux utilisateurs utilisent Google Sheets ou Excel pour le web afin de pouvoir collaborer ou partager publiquement leurs formulaires. Le meilleur moyen de débuter avec XLSForm est d'utiliser le tutoriel ci-dessous.

* :doc:`Tutoriel XLSForm <xlsform-premier-formulaire>`

Si vous êtes plus aventureux, vous pouvez ignorer ce tutoriel, faire une copie du modèle ci-dessous, et apprendre à concevoir votre formulaire ainsi.

* `Google Sheet <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_ (utilisez `Fichier > Créer une copie`)
* `Microsoft Excel (XLSX) file <https://github.com/getodk/xlsform-template/raw/main/ODK%20XLSForm%20Template.xlsx>`_

Une fois conçu votre formulaire, vous pouvez :ref:`télécharger votre XLSForm directement sur votre serveur ODK Central <central-forms-upload>`. Si votre serveur ODK ne dispose pas des dernières fonctionnalités d'XLSForm ou si vous souhaitez avoir un aperçu de votre formulaire dans un navigateur web, essayez `XLSForm Online <https://getodk.org/xlsform>`_.

La documentation ODK montre tous les exemples de conception dans des formulaires XLSForm et décrit comment les formulaires XLSForm sont utilisés par les outils ODK. Le `Formulaire All Widgets <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ>`_ contient des exemples de chacun des différents types de qustions.

.. _survey-sheet:

La feuille survey
-----------------

A minima, un XLSForm contient une feuille nommée **survey** pour décrire les types et l'ordre des questions du formulaire. Elle doit contenir ces trois colonnes :

- ``type``: le type du champ représenté par chaque ligne. Les types supportés ainsi que leurs apparences sont décrits :doc:`ici <form-question-types>`.
- ``name``: le nom du champ représenté par chaque ligne. Ce nom sera utilisé dans vos données. Il ne peut pas contenir d'espace et doit débutr par une lettre ou un tiret bas. Utilisez un nom court et porteur de sens. Par exemple : ``date_de_naissance``.
- ``label``: la question affichée à l'utilisateur pour le champ représenté par chaqiue ligne. Par exemple : ``Quand ${first_name} est-il/elle né(e) ?`` Ce texte peut :ref:`reférencer d'utres champs <variables>` ou :doc:`être traduit <form-language>`.

La feuille "survey" peut avoir de nombreuses autres colonnes pour représenter différents :doc:`types de questions <form-question-types>` et :doc:`logiques de formulaires <form-logic>`. Vous pouvez voir les colonnes les plus couramment utilisées dans `ce modèle <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_.

.. _choices-sheet:

La feuille choices
------------------

If you have :ref:`multiple choice questions <select-widgets>`, you will also need a **choices** sheet to specify choices for those questions. It must have these three columns:

- ``list_name``: The unique ID that identifies a group of choices. It may not contain spaces and must start with a letter or underscore. Use a short and descriptive name. For example: ``yes_no_maybe``.
- ``name``: the name of the field represented by each row. It may not contain spaces and must start with a letter or underscore. This name will be used in your data results so it's best to use a short and descriptive name (e.g., ``y`` for Yes and ``n`` for No).
- ``label``: the user-visible text for the choice represented by each row. For example: ``Yes``, ``No``, and ``Maybe``. This text can :ref:`reference other fields <variables>` or :doc:`have translations <form-language>`.

Choices with the same list name are considered part of a related set of choices and will appear together for a question. This also allows a set of choices to be reused for multiple questions (for example, yes/no questions).

.. _settings-sheet:

La feuille settings
-------------------

You should also include a **settings** sheet to uniquely identify your form definition and its current version. We recommend specifying at least the following columns:

- ``form_title``: The title that will be displayed by tools that list this form.
- ``form_id``: The unique ID that identifies this form to tools that use it. It may not contain spaces and must start with a letter or underscore. Use a descriptive name no more than 64 characters. For example: ``bench_inventory_2021``.
- ``version``: The unique version code that identifies the current state of the form. A common convention is to use a format like yyyymmddrr. For example, ``2017021501`` is the 1st revision from Feb 15th, 2017.
- ``instance_name``: An :ref:`expression <expressions>` that will be used to represent a specific filled form created from this form definition. For example, ``concat(${first_name}, "-", ${age})``. :ref:`Learn more <instance-name>`.

Other available columns are:

- ``default_language``: Specifies the default language name in a form that has multiple defined languages. For more information on using multiple languages, refer to :ref:`multi-language forms <switching-languages>`.
- ``public_key``: This attribute is necessary for enabling :ref:`encryption <defining-encrypted-form>`. It represents a base64-encoded RSA public key. The corresponding private key will be required for decrypting submissions and should not be included in the form definition.
- ``auto_send``: When set to true, any finalized forms will be automatically sent as soon as a connection becomes available. If present, it will override the app-level :ref:`Auto send <auto-send>` setting.
- ``auto_delete``: When set to true, successfully submitted forms will be immediately deleted from the device. If present, it will override the app-level :ref:`Delete after send <delete-after-send>` setting.

.. _instance-name:

Naming filled forms
~~~~~~~~~~~~~~~~~~~

In an XLSForm's **settings** sheet, you can add an ``instance_name`` column and specify an :ref:`expression <expressions>` to use a specific filled form's contents in its name. This name will be shown in several places to help guide data collection and analysis. You should pick a name that uniquely identifies the filled form and the data it had captured. For example:

- If a single filled form represents data about a real-world thing like a person or park bench, your ``instance_name`` expression should include some information to uniquely identify the thing like the person's name or the park bench's location and current status.
- If a single filled form represents data about an observation, consider including the date and time of the observation in the ``instance_name`` expression.
- If your form definition includes a repeat, consider including the repeat count in the ``instance_name`` expression.

.. _instance-name-collect:

Filled form names in Collect
""""""""""""""""""""""""""""

Each filled form is identified by its ``instance_name`` value in :doc:`Collect <collect-intro>`'s :guilabel:`Edit Saved Form`, :guilabel:`Send Finalized Form` and :guilabel:`View Sent Form` lists. 

In workflows where forms have to be be filled in multiple different steps, a useful ``instance_name`` expression will make it much easier to find which filled form to edit. If forms only have to be edited under certain conditions (e.g. not all household members were available), you can include this status in the ``instance_name``.

In the :guilabel:`View Sent Form` list, ``instance_name`` can be helpful to identify which data collection tasks have been completed. For example, if a data collector needs to interview 25 specific people and the ``instance_name`` for each filled form identifies the respondent, they can go to :guilabel:`View Sent Form` to verify which subset of interviews they have already completed. 

A sent form's ``instance_name`` is maintained after it is deleted. This makes it possible to confirm what work has been completed even if submissions are configured to :ref:`delete after send <delete-after-send>`. However, it does mean sensitive data should be avoided in ``instance_name``.

The ``instance_name`` is also used to identify filled forms in Collect's :doc:`filled form map <collect-form-map>`.

.. _instance-name-central:

Filled form names in Central
""""""""""""""""""""""""""""

Each submission in Central has its own :ref:`detail page <central-submissions-details>` which provides basic information about the submission, an activity history of action and discussion on that submission.

The title at the top is pulled from the ``instance_name`` and it makes navigation much easier to have friendly names at the top of the page and in the web browser title and tab.

.. _entities-sheet:

The entities sheet
-------------------

:doc:`Entities <central-entities>` let you share information between forms so you can collect longitudinal data, manage cases over time, and support other complex workflows.

Review the :doc:`Entities page <central-entities>` to learn more about what Entities are and how to use them.
