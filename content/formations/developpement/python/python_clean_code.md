---
title: Clean Code en Python et gestion de code legacy
draft: true
identifier: pycleancode
domaines: développement
subdomain: Python
url: /formations/developpement/python-clean-code-et-legacy
weight: '6'
catchphrase: Apprenez à organiser des projets Python faciles à faire évoluer.  Ces
  techniques vous seront également utiles pour maintenir facilement des projets complexes.
duration: 3j soit 21h
equilibre: 35% théorie / 65% pratique
pricing: 1700 € HT par stagiaire (pauses et repas inclus)
objectifs:
- Identifier les principaux éléments qui forment le « Clean Code » quel que soit le
  langage et en particulier dans le cas de Python
- Analyser un code existant pour en critiquer son organisation
- Utiliser ces éléments sur un projet exemple, ainsi que sur du code existant
- Concevoir des codes faciles à faire évoluer
- Identifier l’intérêt d’un outil de festion de version
prerequis:
- De bonnes connaissances de Python (aucun problème sur la syntaxe, connaissance de
  l’orienté objet)
- Connaissance du développement logiciel en général
publics:
- Chef de projet en développement
- Développeur
- Testeur ayant une fibre développement
- Architecte
- Technical Leader
programme:
- title: Bonnes pratiques
  elements:
  - title: Formatage du code
  - title: Conventions de nommage (PEP8)
  - title: Concepts de DRY (Don’t Repeat Yourself) et KISS (Keep It Single Stupid)
  - title: Gestion des paramètres dans les fonctions
  - title: Gestion de la documentation en Python (via les ‘Docstring’)
  - title: Annotation de types pour faciliter la revue de code et la mise en oeuvre
      des outils d'analyse statique
  free_text: 'TP : ajouter de la documentation à un code Python, faire évoluer les
    nommages de variables d’un code existant'
- title: Organisation d'un projet en python
  elements:
  - title: 'Notion de découpage en fichiers, en dossiers. '
  - title: 'Impact sur les ’import” '
  - title: Rôle des fichiers classiques (__init__.py, __main__.py)
  - title: 'La structuration classique d’un fichier  '
- title: Utiliser les fonctions de python pour améliorer son code
  elements:
  - title: Utilisation des ‘fonctions spécifiques’ versus ‘fonctions builtins’ de
      la bibliothèque standard (Avantages / Inconvénients)
  - title: Le meilleur code est pas de code
  - title: 'Méthodes magiques '
  - title: Décorateurs
  - title: 'Gestionnaire de contexte '
  free_text: 'TP : illustration des différentes techniques sur des cas simples'
- title: Point sur la gestion de versions
  elements:
  - title: Intérêt d’un outil de gestion de versions
  - title: Utilisation pour revenir en arrière et développer de nouvelles fonctionnalités
  - title: Intérêt des messages de commit
  - title: Parcours de l’historique
- title: Les principes en Programmation Orientée Objet
  elements:
  - title: Présentation des principes SOLID
    subelements:
    - Single responsibility principle
    - The open/closed principle
    - Liskov's substitution principle
    - Interface segregation
    - Dependency inversion
  - title: La loi de Demeter
  - title: Reconnaître / écrire un code de qualité
  free_text: 'TP : mise en œuvre sur un kata de programmation  '
- title: Les patrons de conception (design patterns)
  elements:
  - title: Le concept de design patterns et leur utilité
  - title: Présentation de quelques design patterns connus et leurs cas d’utilisation
      classique
  free_text: 'TP : Un cas d’usage implémentant le design pattern Observer,  le design
    pattern Adapter, .'
- title: 'Tests unitaires et refactoring '
  elements:
  - title: Les principes de refactoring et de tests unitaires
  - title: Les outils de tests unitaires (unittest, pytest) en python, notion de couverture
      de tests et génération de rapports
  - title: Présentation du concept de développement piloté par les tests (TDD)
  - title: L'automatisation des tests, l'agrégation de tests.
  - title: Intégration dans un pipeline d’intégration continue (CI)
  free_text: 'TP : mise en oeuvre sur un kata de programmation'
- title: Maintenir un code existant (code legacy)
  elements:
  - title: 'Techniques de navigation dans un nouveau projet '
  - title: L’analyse statique du code et l’annotation de code
  - title: Analyse dynamique du code avec “pycallgraph”, “sys.trace”
  - title: Analyse des dépendances du code / gestion des versions
  - title: Les techniques de refactoring sur du code existant (ajout de tests unitaires,
      notion de gold standard…)
  free_text: 'TP : application des techniques vues en cours sur un kata de programmation
    classique'
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

Dans cette formation pragmatique, vous verrez les différentes techniques et bonnes pratiques, reconnues dans le domaine du développement logiciel (quel qu'en soit le langage), tout en mettant un accent particulier sur les codes en Python. Vous apprendrez ainsi les grands principes permettant de reconnaître les problèmes classiques (code smell) et comment les régler. Finalement, vous appliquerez ces techniques pour maintenir et faire évoluer des codes existants. 
