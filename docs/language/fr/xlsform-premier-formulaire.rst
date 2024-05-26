:og:image: https://docs.getodk.org/_static/img/premier_formulaire_xlsform.png

Tutoriel XLSForm : votre premier formulaire
===========================================

Les formulaires ODK sont créés en utilisant des feuilles de calcul qui suivent les règles du standard XLSForm.

L'utilisation d'un tableur pour concevoir des formulaires est très avantageuse car vous pouvez visualiser un maximum d'informations relatives à votre formulaire sur un seul écran, partager facilement votre définition de formulaire, et utiliser les fonctions très pratiques proposées par les tableurs (formules, copier/coller, mise en forme automatique, etc.) pour concevoir votre formulaire.

Quiconque dispose d'un tableur peut créer un formulaire ! En moins de 20 minutes, vous allez construire le formulaire de recensement d'établissements scolaires proposé ci-dessous.

..  youtube:: 22l0xHxJ3vo
   :width: 100%

Si vous souhaitez visualiser ce à quoi il ressemblera, vous pouvez essayer cet `aperçu web <https://demo.getodk.cloud/-/single/uvOoPKYmRSpeUTab5bflNBBMT37L0u7?st=es1kN9UyLfov8T1SZEB8QCTw9gaGp6$s73b9muqj4czHlVown2UAcmyLt3uGNkcN>`_.

Objectifs
---------

Dans ce tutoriel, vous allez :

* Concevoir un court formulaire utilisant différents types de questions
* Utiliser les principaux éléments de structures logiques de XLSForm
* Apprendre quelles ressources utiliser pour développer vos compétences

Prêt/prête à partir à la découverte d'XLSForm ? Alors en route !

Ouvrez le modèle de XLSForm
---------------------------
Vous pouvez utiliser n'importe que logiciel de tableur pour créer et modifier un XLSForm : Excel, Google Sheets, LibreOffice Calc, et d'autres. Choisissez celui que vous préférez pour ouvrir le modèle de XLSForm proposé ci-dessous :

* `Google Sheet <https://docs.google.com/spreadsheets/d/1v9Bumt3R0vCOGEKQI6ExUf2-8T72-XXp_CbKKTACuko>`_ (Utilisez  `Fichier > Créer une copie`)
* `Microsoft Excel (XLSX) file <https://github.com/getodk/xlsform-template/raw/main/ODK%20XLSForm%20Template.xlsx>`_

Ajoutons une question obligatoire de type "text"
------------------------------------------------

#. Dans le feuille ``survey``, utilisez la liste déroulante de la colonne ``type`` pour choisir ``text``. Ceci créera une question de type "text" à laquelle l'utilisateur pourra répondre.
#. Dans la colonne ``name``, mettez le nom du champ qui stockera la donnée et qui sera utilisé dans les analyses. Utilisons ``nom_etablissement``.
#. Dans la colonne ``label``, mettez le texte que verra le collecteur de données pour cette question : ``Quel est le nom de l'établissement ?``
#. Dans la colonne ``required``, mettez ``yes`` pour indiquer qu'une réponse à cette question est obligatoire.

Ajoutons une question obligatoire de type "image"
-------------------------------------------------

Dans la ligne sous la question du nom de l'établissement, ajoutez une question obligatoire pour prendre une photo de l'établissement.

#. Dans la colonne ``type``, mettez ``image``
#. Dans la colonne ``name``, mettez ``photo_etablissement``
#. Dans la colonne ``label``, mettez ``Prendre une photo de l'établissement ${nom_etablissement}``
#. Ajoutons une astuce pour donner aux collecteurs plus d’informations sur ce que nous voulons photographier. Dans la colonne ``hint``, mettez ``Inclure la porte d'entrée``
#. Dans la colonne ``required``, mettez ``yes``
#. Dans la colonne ``parameters``, mettez ``max-pixels=1024`` pour limiter la taille des images à 1024 pixels.

Ajoutons une question optionnelle de type "emplacement"
-------------------------------------------------------

#. Dans la colonne ``type``, mettez ``geopoint``
#. Dans la colonne ``name``, mettez ``emplacement_etablissement``
#. Dans la colonne ``label``, mettez ``Quel est l'emplacement de l'établissement "${nom_etablissement}" ?``

Ajoutons une question de type "integer" n'autorisant que des valeurs positives
------------------------------------------------------------------------------

#. Dans la colonne ``type``, mettez ``integer``
#. Dans la colonne ``name``, mettez ``nombre_eleves``
#. Dans la colonne ``label``, mettez ``Combien d'élèves sont inscrits ?``
#. Dans la colonne ``required``, mettez ``yes``
#. Faisons en sorte que seul un nombre positif puisse être renseigné. Dans la colonne ``constraint``, mettez ``. > 0`` pour spécifier que la valeur renseignée (``.``) doit être supérieure à 0.
#. Affichons un messages aux collecteurs de données s'ils renseignent une valeur non autorisée. Dans la colonne ``constraint_message``, mettez ``La valeur doit être un nombre positif``

Ajoutons une question permettant de choisir plusieurs réponses
--------------------------------------------------------------

Cette question portera sur les niveaux enseignés dans l'établissement. Nous proposerons quatre choix (maternelle, élémentaire, collège, lycée), et laisserons le collecteur de données en sélectionner un ou plusieurs.

#. Allez à la feuille "choices". Elle sert à définir les listes de choix utilisées dans les question de type "select".
#. Ajoutez un choix pour le niveau "maternelle" : 

   #. Dans la colonne ``list_name``, mettez le nom de la liste de choix qui contiendra les quatre options : ``niveaux``
   #. Dans la colonne ``name``, mettez la valeur qui sera stockée dans les données qui seront analysées : ``maternelle``
   #. Dans la colonne ``label``, mettez le texte qui sera montré au collecteur pour ce choix : ``maternelle (3-5 ans)``
   
#. Ajoutez un choix pour le niveau "élémentaire" : 

   #. Dans la colonne ``list_name``, mettez ``niveaux`` pour mettre ce choix dans la même liste que précédemment.
   #. Dans la colonne ``name``, mettez : ``elementaire``
   #. Dans la colonne ``label``, mettez : ``Elémentaire (6-11 ans)``
   
#. Ajoutez un choix pour le niveau "collège" : 

   #. Dans la colonne ``list_name``, mettez ``niveaux`` pour mettre ce choix dans la même liste que précédemment.
   #. Dans la colonne ``name``, mettez ``college``
   #. Dans la colonne ``label``, mettez ``Collège (11-15 ans)``
   
#. Ajoutez un choix pour le niveau "lycée" : 

   #. Dans la colonne ``list_name``, mettez ``niveaux`` pour mettre ce choix dans la même liste que précédemment.
   #. Dans la colonne ``name``, mettez ``lycee``
   #. Dans la colonne ``label``, mettez ``Lycée (15-18 ans)``
   
#. Retournez à la feuille ``survey``.
#. Dans la ligne qui suit la question ``nombre_eleves``, mettez ``select_multiple niveaux`` dans la colonne ``type``
  
   .. note::
     Votre logiciel vous montrera un avertissement de validation car il ne connaît pas le nom de votre liste (``niveaux``). Ceci est normal pour les questions de type "select" qui sont complétées par le nom de la liste et cet avertissement peut donc être ignoré.

#. Dans la colonne ``name``, mettez ``niveaux_enseignes``
#. Dans la colonne ``label``, mettez ``Quels niveaux sont enseignés ?``
#. Dans la colonne ``required``, mettez ``yes``
#. Faisons apparaître les choix horizontalement, les uns à coté des autres. Dans la colonne ``appearance``, mettez ``columns``.

Ajoutons une question qui sera montrée en fonction d'une réponse précédente
---------------------------------------------------------------------------
Elle portera sur les options enseignées au lycée.

#. Dans la colonne ``type``, mettez ``text``
#. Dans la colonne ``name``, mettez ``options_lycee``
#. Dans la colonne ``label``, mettez ``Quelles sont les options proposées au Lycée ?``
#. Dans la colonne ``required``, mettez ``yes``
#. Affichons cette question seulement si l'établissement est un lycée. Dans la colonne ``relevant``, mettez ``selected(${niveaux_enseignes}, 'lycee')``

Définissons un titre et un identifiant pour ce formulaire
---------------------------------------------------------

#. Allez à la feuille ``settings``.
#. Dans la colonne ``form_title``, mettez le titre que verront les utilisateurs du formulaire : ``Recensement des établissements scolaires 2024``
#. Dans la colonne ``form_id``, mettez an ID qui identifie de manière unique ce formulaire : ``recensement_etablissements_scolaires_24``
#. Dans la colonne ``instance_name``, mettez un nom qui identifie chaque soumission de données de ce formulaire : ``${nom_etablissement}``

Testez votre formulaire dans Central
------------------------------------

.. note::
   Vous n'avez pas encore de serveur ODK Central ? :ref:`getting-started-get-central` ou utilisez `XLSForm Online <https://getodk.org/xlsform>`_ pour tester votre formulaire dans un navigateur web.

#. Enregistrez ou téléchargez votre formulaire dans un fichier XLSX.
#. Connectez vous à votre serveur Central.
#. Si vous n'avez pas encore de Projet, créez en un en nommez le.
#. Cliquez sur le bouton "Nouveau" à coté de ``Formulaires``.
#. Glissez et déposez votre fichier XLSX ou cliquez sur le bouton "Parcourir".
   
   .. image:: ../../img/language/fr/xlsform-premier-formulaire/upload-formulaire-recensement-etablissments.*
     :scale: 30%
     :alt: La boite de dialogue de chargement de formulaire d'ODK Central.

#. Cliquez sur le bouton :guilabel:`Aperçu` pour voir votre formulaire dans votre navigateur web 🎉
  
   .. image:: ../../img/language/fr/xlsform-premier-formulaire/ebauche-formulaire-recensement-etablissments.*
     :alt: ODK Central affichant une ébauche du formulaire de recensement des établissements scolaires. Il y a un cadre rouge autour du bouton "Aperçu".

   .. image:: ../../img/language/fr/xlsform-premier-formulaire/apercu-formulaire-recensement-etablissments.*
     :alt: ODK Central affichant un aperçu web du formulaire de recensement des établissements scolaires.
     :align: center

#. Pour voir le formulaire dans l'application mobile `ODK Collect <https://play.google.com/store/apps/details?id=org.odk.collect.android>`_, cliquez sur l'onglet guilabel:`Tester` et scannez le QR code avec Collect.

A vous de jouer
---------------

#. Pouvez vous rendre la question de la localisation obligatoire ?
#. Pouvez vous faire en sorte de n'afficher la question du niveau enseigné seulement si au moins 100 élèves sont inscrits ?
#. Pouvez vous afficher les options du niveau d'enseignement verticalement plutôt qu'horizontalement ? (Astuce : la mise en forme verticale est l'apparence par défaut des questions de type "select")

Prochaines étapes
-----------------
Félicitations ! Vous venez de concevoir un premier formulaire qui utilise la plupart des briques de XLSForm. Vous trouverez ci-dessous des ressources pour développer vos compétences.

* Approfondissez votre compréhension

  * :doc:`Introduction à XLSForm <xlsform>`
  * :doc:`Types de question <form-question-types>`
  * :ref:`Questions obligatoires<requiring-responses>`
  * :ref:`Constraintes à la saisie <constraints>`
  * :ref:`Questions de type "select" <select-widgets>`
  * :ref:`Conditionner l'affichage des questions (Relevance) <relevants>`

* Élargissez vos connaissances

  * :ref:`groups`
  * :doc:`form-styling`
  * :doc:`form-language`
  * :doc:`form-operators-functions`

* :doc:`Introduction à ODK Collect <collect-intro>`
