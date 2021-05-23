---
title: Python et la programmation objet
draft: false
identifier: pyobjet
domaines: développement
subdomain: Python
url: /formations/developpement/python-objet
weight: '2'
catchphrase: Découvrez la programmation orientée objet en Python pour réaliser des
  programmes multiplateformes robustes et fiables.
duration: 5 jours, soit 35h
equilibre: 35% théorie / 65% pratique
pricing: 1²650 € HT (pauses et repas inclus)
objectifs:
- Maîtriser la syntaxe du langage Python
- Acquérir les grandes notions de la programmation objet
- Choisir et utiliser les modules Python pour résoudre un problème spécifique
- Concevoir des interfaces graphiques
- Analyser un projet Python pour déterminer sa qualité de code
- Utiliser des tests unitaires pour améliorer la qualité d’un code
prerequis:
- Être à l’aise avec un langage de programmation proche (C / C++ / Java / PHP / …)
  et connaitre les concepts de variables, types, fonctions, ...
- La connaissance de Python n’est pas nécessaire, mais souhaitable. La connaissance
  préalable de la programmation orientée objet n’est pas nécessaire.
publics:
- Développeurs
- Ingénieurs
- Chercheurs
- chefs de projets proches du développement
programme:
- title: Le langage Python
  elements:
  - title: Présentation / historique et contexte / philosophie
  - title: 'Cas d’utilisation et de non utilisation '
  - title: Présentation des outils de développement
  free_text: 'TP : installation d’un interpréteur Python, d’un éditeur de texte et
    familiarisation avec les outils'
- title: Syntaxe basique de Python
  elements:
  - title: Variables et types classiques (assignation, modification…)
    subelements:
    - Affichage des variables
    - Conventions et règles de nommage.
  - title: 'La manipulation des différents types '
    subelements:
    - Numériques
    - chaînes de caractères
    - Autres conteneurs (listes, tuple et dictionnaires)
  - title: Les blocs, les commentaires.
    subelements:
    - Les conditions (if/elif/else) et la manipulation de variables booléennes (création,
      composition)
    - Les boucles while et for (gestion de l’itération avec break / continue)
    - La fonction range.
  - title: La gestion d’erreur et la compréhension des exceptions
  - title: Création, documentation et utilisation de fonctions.
    subelements:
    - Portée des variables et la règle LEGB
    - Les lambda expression
    - Les générateurs / itérateurs
  - title: La structuration du code en modules.
  - title: L'utilisation des fichiers.
  free_text: 'TP : exercices permettant de se familiariser avec le langage (syntaxe,
    itérations et conditions, ouverture de fichiers) et d’illustrer la spécificité
    d’un code Pythonique'
- title: Qualité de code (QA)
  elements:
  - title: 'Les environnements virtuels pour gérer facilement les projets '
    subelements:
    - 'Le concept et les cas d’usages des environnements virtuels '
    - 'Installation de bibliothèques tierces avec pip '
    - Création et évolution d’environnements virtuels
  - title: Les outils d’analyse statique et l’annotation de type
    subelements:
    - 'Présentation du concept '
    - Présentation des outils (pylint, mypy)
  - title: 'Le formatage '
    subelements:
    - Présentation de la PEP 8
    - Utilisation d’autoformatter (black, autopep8)
  - title: La gestion de la documentation
    subelements:
    - Écriture de la documentation (docstring, formattage)
    - 'Les outils d’extraction de documentation '
  - title: Les tests unitaires
    subelements:
    - Le concept de tests unitaires
    - Les outils de tests unitaires (unittest, pytest) en python, notion de couverture
      de tests et génération de rapports
    - Présentation du concept de développement piloté par les tests (TDD)
    - L'automatisation des tests, l'agrégation de tests.
    - Intégration dans un pipeline d’intégration continue (CI)
  - title: 'Débogage '
    subelements:
    - Le concept de déboguer du code
    - 'Le débugueur textuel de python '
    - Les débugueurs graphiques
  free_text: 'TP : Configurer son éditeur de code pour intégrer des outils de QA,
    ajout de tests unitaires sur des codes précédents '
- title: Présentation de la Programmation Orientée Objet (POO)
  elements:
  - title: Les principes du paradigme Objet.
  - title: La définition d'un objet (état, comportement, identité).
  - title: La notion de classe, d'attributs et de méthodes.
  - title: La communication entre les objets.
    subelements:
    - L'héritage et la notion de polymorphisme.
    - Composition de classes.
  - title: Modélisation de programmes avec l’UML
    subelements:
    - Les diagrammes de classes, de séquences, d'activités…
    - Notion de modèle de conception (Design Pattern).
  free_text: 'TP : Modéliser un cas concret en UML (identification des classes et
    de leurs relations)'
- title: Programmation Objet en Python
  elements:
  - title: Les particularités du modèle Objet de Python.
  - title: L'écriture de classes et leur instanciation.
    subelements:
    - Les méthodes et attributs en pratique
    - La modification d’attribut
    - Le paramètre “self”
    - 'Les méthodes magiques pour modifier le comportement de ses classes '
  - title: L'héritage et le polymorphisme.
  - title: 'Le duck typing '
  - title: Création d’exceptions spécifiques
  free_text: 'TP : Pratique des différents concepts à l’aide d’un ensemble d’exercices
    simples.'
- title: Les bibliothèques
  elements:
  - title: Qu’est-ce qu’une bibliothèque
  - title: La bibliothèque standard et ses différents modules
    subelements:
    - 'Manipulation de fichiers '
    - 'Manipulation réseau '
    - Expressions régulières
    - Manipulation de bases de données
    - '… '
  - title: Les bibliothèques tierces
    subelements:
    - 'Identification et installation '
    - Découvertes de quelques bibliothèques incontournables (téléchargement de ressources
      internet, manipulation de données…)
  free_text: 'TP : réalisation d’un mini-projet permettant de manipuler plusieurs
    bibliothèques '
sessions:
- city: Lyon
  date: 21-22 juin 2021
  image: /imgs/photos/villes/lyon3.jpg
- city: Lille
  date: 14-15 juin 2021
  image: /imgs/photos/villes/lille.jpg
- city: Paris
  date: 28-29 juin 2021
  image: /imgs/photos/villes/paris3.jpg

---

Après avoir (re)vu la syntaxe du langage et (re)découvert les mécanismes de la programmation objet, vous aurez une base de connaissance solide. La suite du cours se concentrera sur les bonnes pratiques (évaluation de la qualité d’un code, tests, partage d’environnement) et l’utilisation de différentes bibliothèques pour gérer les cas de la vie réelle (manipulation de bases de données, lecture / écriture de fichiers, gestion d’une arborescence de dossiers / fichiers)
