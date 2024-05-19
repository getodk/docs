XLSForm
=======

.. _xlsform-introduction:

:dfn:`XLSForm` est un standard pour concevoir des formulaires dans Excel. Les formulaires XLSForm sont simples à prendre en main et le standard permet de définir des formulaires complexes. 

Les formulaires XLSForm peuvent être créés et modifiés par toute application permettant de produire des documents ``.xlsx``. Cela signifie qu'ils sont "portables" et qu'ils peuvent tirer profit des nombreuses fonctions généralement disponibles dans les tableurs, telles que les formules, les commentaires et la gestion des versions. 

De nombreux utilisateurs utilisent Google Sheets ou Excel pour le web afin de pouvoir collaborer ou partager publiquement leurs formulaires. Le meilleur moyen de débuter avec XLSForm est d'utiliser le tutoriel ci-dessous.

* :doc:`Tutoriel XLSForm <xlsform-premier-formulaire>`

Si vous êtes plus aventureux, vous pouvez ignorer ce tutoriel, faire une copie du modèle ci-dessous, et apprendre par vous même à concevoir votre formulaire.

* `Google Sheet <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_ (utilisez `Fichier > Créer une copie`)
* `Microsoft Excel (XLSX) file <https://github.com/getodk/xlsform-template/raw/main/ODK%20XLSForm%20Template.xlsx>`_

Une fois votre formulaire conçu, vous pouvez :ref:`le télécharger directement sur votre serveur ODK Central <central-forms-upload>`. Si votre serveur ODK ne dispose pas des dernières fonctionnalités d'XLSForm ou si vous souhaitez avoir un aperçu de votre formulaire dans un navigateur web, essayez `XLSForm Online <https://getodk.org/xlsform>`_.

La documentation d'ODK propose tous les exemples de conception dans des formulaires XLSForm et décrit comment les formulaires XLSForm sont utilisés par les outils d'ODK. Le `Formulaire "All Widgets" <https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ>`_ contient des exemples pour chacun des différents types de questions.

.. _survey-sheet:

La feuille survey
-----------------

A minima, un XLSForm contient une feuille nommée **survey** pour décrire les types et l'ordre des questions du formulaire. Elle doit contenir ces trois colonnes :

- ``type``: le type du champ représenté par chaque ligne. Les types supportés ainsi que leurs apparences sont décrits :doc:`ici <form-question-types>`.
- ``name``: le nom du champ représenté par chaque ligne. Ce nom sera utilisé dans vos données. Il ne peut pas contenir d'espace et doit débuter par une lettre ou un tiret bas. Utilisez un nom court et porteur de sens. Par exemple : ``date_de_naissance``.
- ``label``: la question affichée à l'utilisateur pour le champ représenté par chaque ligne. Par exemple : ``Quand ${first_name} est-il/elle né(e) ?`` Ce texte peut :ref:`référencer d'autres champs <variables>` ou :doc:`être traduit <form-language>`.

La feuille "survey" peut contenir de nombreuses autres colonnes pour représenter différents :doc:`types de questions <form-question-types>` et :doc:`logiques de formulaires <form-logic>`. Vous pouvez voir les colonnes les plus couramment utilisées dans `ce modèle <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_.

.. _choices-sheet:

La feuille choices
------------------

Si vous avez des :ref:`questions à choix multiples <select-widgets>`, une feuille **choices** sera nécessaire pour spécifier les réponses possibles pour ces questions. Elle doit contenir ces trois colonnes :

- ``list_name``: l'identifiant unique d'un ensemble de choix. Il ne peut pas contenir d'espaces et doit débuter par une lettre ou un "underscore". Utilisez un nom court et porteur de sens. Par exemple : ``oui_non_peut_etre``.
- ``name``: le nom du champ représenté par la chaque ligne. Il ne peut contenir d'espace et doit débuter par une lettre ou un "underscore". Ce nom sera la valeur stockée dans vos données, il est donc préférable d'utiliser des valeurs courtes et descriptives (par exemple, ``o`` pour Oui et ``n`` pour Non).
- ``label``: le texte affiché à l'utilisateur du formulaire pour chacun des choix représentés par chaque ligne. Par exemple : ``Oui``, ``Non``, et ``Peut-être``. Ce texte peut :ref:`faire référence à d'autres champs <variables>` ou :doc:`être traduit en différentes langues<form-language>`.

Les choix portant le même nom de liste font partie d'un même ensemble et ils apparaîtront ensemble pour une question. Ces ensembles peuvent être réutilisés pour plusiers questions au sein du formulaire (par exemple, les questions pour lesquelles une réponse oui/non/peut-être est attendue).

.. _settings-sheet:

La feuille settings
-------------------

Vous pouvez aussi intégrer une feuille **settings** afin d'identifier de manière unique votre définition de formulaire et sa version courante. Nous recommandons de spécifier a minima les colonnes suivantes :

- ``form_title``: Le titre qui sera affiché par les outils pour lister le formulaire.
- ``form_id``: L'identifiant unique de ce formulaire dans les outils qui l'utilisent. Il ne doit pas contenir d'espace et doit débuter par une lettre ou un "underscore". Utilisez un nom porteur de sens de moins de 64 caractères. Par exemple : ``inventaire_des_arbres_2021``.
- ``version``: Le code unique de la version courante du formulaire. Une convention est d'utiliser un format tel que yyyymmddrr. Par exemple, ``2017021501`` est la première révision du 15 février 2017.
- ``instance_name``: Une :ref:`expression <expressions>` qui sera utilisée pour nommer une instance spécifique de ce formulaire. Par exemple, ``concat(${prenom}, "-", ${age})``. :ref:`En savoir plus <instance-name>`.

Les autres colonnes disponibles sont :

- ``default_language``: Sépcifie la langue par défaut d'un formulaire disposant de plusieurs traductions. Pour de plus amples informations sur l'utilisation de plusieurs langues, référez vous à :ref:`multi-language forms <switching-languages>`.
- ``public_key``: Cet attribut est nécessaire pour activer :ref:`le chiffrement <defining-encrypted-form>`. Il représente une clé RSA publique encodée en base64. La clé privée correspondante sera requise pour déchiffrer les soumissions et ne devra pas être incluse dans la définition du formulaire.
- ``auto_send``: Quand elle est paramétrée à "true", chaque formulaire finalisé sera automatiquement envoyé dés qu'une connexion sera disponible. Si cette valeur est renseignée, elle écrasera le paramètre :ref:`Envoi automatique <auto-send>` défini au niveau de l'application.
- ``auto_delete``: Quand elle est paramétrée à "true", les formulaires envoyés avec succès seront immédiatement supprimés du terminal. Si cette valeur est renseignée, elle écrasera le paramètre :ref:`Supprimer après envoi <delete-after-send>` défini au niveau de l'application.

.. _instance-name:

Nommer les formulaires remplis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dans la feuille **settings** d'un formulaire XLSForm, vous pouvez ajouter une colonne ``instance_name`` et spécifier une :ref:`expression <expressions>` pour utiliser une valeur contenue dans le formulaire dans son nom. Ce nom sera affiché en plusieurs endroit pour faciliter la collecte de données et l'analyse. Vous devriez utiliser un nom qui identifie de manière unique le formulaire et les données qu'il contient. Par exemple :

- Si un formulaire contient les données relatives à un objet du monde réel, tel qu'une personne ou un banc public, votre expression ``instance_name`` pourra inclure des informations pour identifier de manière unique l'objet décrit comme le nom de la personne ou l'emplacement du banc.
- Si un formulaire contient les données d'une observation, considérez d'inclure la date et l'heure de l'observation dans l'expression ``instance_name``.
- Si votre définition de formulaire contient un "repeat", considérez l'utilisation du nombre de répétitions dans l'expression ``instance_name``.

.. _instance-name-collect:

Filled form names in Collect
""""""""""""""""""""""""""""

Chaque formulaire rempli est identifié par son nom d'instance ``instance_name`` dans les listes :guilabel:`Editer les Formulaires Sauvegardés`, :guilabel:`Envoyer les formulaires finalisés` et :guilabel:`Voir les Formulaires Envoyés` de :doc:`Collect <collect-intro>`. 

Pour les "workflows" dans lesquels les formulaires doivent être saisis en plusieurs étapes, une valeur d'``instance_name`` explicite facilitera la recherche d'un formulaire à éditer. Si des formulaires doivent être édités sous certaines conditions (par exemple s'il manquait des habitants lors de l'enquête), vous pouvez inclure ce statut dans le nom de l'instance (``instance_name``).

Dans la liste :guilabel:`Voir les Formulaires Envoyés`, le nom d'instance (``instance_name``) peut aider à identifier les collectes de données achevées. Par exemple si les enquêteurs doivent interviewer 25 personnes spécifiques, et que l'``instance_name`` identifie chacun des répondants, ils peuvent vérifier dans :guilabel:`Voir les Formulaires Envoyés` quels ensembles d'entretiens sont finalisés.

L'``instance_name`` d'un formulaire envoyé est conservé après sa suppression. Cela permet de confirmer quel travail a été effectué, même si les soumissions sont paramétrées pour être :ref:`supprimées après envoi <delete-after-send>`. Par ailleurs, cela signifie que des données sensibles sont à prohiber dans la valeur d'``instance_name``.

Le nom d'instance est aussi utilisé pour identifier les formulaires dans :doc:`la carte des formulaires remplis <collect-form-map>` dans Collect.

.. _instance-name-central:

Noms des formulaires remplis dans Central
"""""""""""""""""""""""""""""""""""""""""

Chaque soumission dans Central a sa propre :ref:`page de détail <central-submissions-details>` qui fournit des informations basiques sur la soumission, un historique de l'activité et des discussions relatives à cette soumission.

Le titre du haut est extrait du nom d'instance (``instance_name``) et utiliser des noms explicites facilite la navigation en les affichant en haut de page et dans le titre du navigateur et de l'onglet.

.. _entities-sheet:

La feuille entities
-------------------

Les :doc:`Entitiés <central-entities>` vous permettent de partager de l'information entre vos formulaires afin que vous puissiez collecter des données longitudinales, faire des suivis dans le temps et mettre en œuvre des processus complexes.

Visitez :doc:`la page Entités <central-entities>` pour en apprendre plus à propos des entités et comment les utiliser.