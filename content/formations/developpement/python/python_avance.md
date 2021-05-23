---
title: Python avancé
draft: false
identifier: pyavance
domaines: développement
subdomain: Python
url: /formations/developpement/python-avance
weight: '3'
catchphrase: Pendant cette formation centrée sur le pragmatisme, vous découvrirez
  comment fonctionnent vraiment les fonctions, le modèle objet et l’écosystème de
  bibliothèque.
duration: 4j soit 28h
equilibre: 35% théorie / 65% pratique
pricing: 1650 € HT (pauses et repas inclus)
objectifs:
- 'Utiliser les techniques avancées du langage Python : “Context Manager”, “Closures”,
  Decorateurs, fonctions avancées'
- Identifier les patrons de conceptions (Design Patterns) à utiliser dans des cas
  spécifiques
- Analyser les performances d’un programme python pour en identifier les goulots d’étranglement
  à optimiser
- Packager et déployer ses bibliothèques
- Identifier et utiliser les bibliothèques incontournables du langage pour réaliser
  des développements complexes rapidement
prerequis:
- 'Connaitre et maitriser la syntaxe de base de python, la création de fonctions ainsi
  que les notions de programmation orientée objet (attribut, classes…). '
- 'Être à l’aise avec la ligne de commande. '
- Une connaissance des bonnes pratiques en développement (gestion de version, configuration
  d’éditeurs de texte) est un plus pour certaines parties
publics:
- Développeurs
- Ingénieurs
- 'chercheurs ayant une bonne connaissance de Python. '
programme:
- title: Le langage Python
  elements:
  - title: Présentation / historique et contexte / philosophie
  - title: 'Cas d’utilisation et de non utilisation '
  - title: Présentation des outils de développement
  free_text: 'TP : installation d’un interpréteur Python, d’un éditeur de texte et
    familiarisation avec les outils'
- title: Rappels sur Python
  elements:
  - title: Formatage et affichage des variables
  - title: La gestion d’erreur et la compréhension des exceptions
  - title: Fonctions.
    subelements:
    - Portée des variables et la règle LEGB
    - Les lambda expression
    - Les générateurs
  - title: La structuration du code en modules.
  - title: L'utilisation des fichiers et encodage de caractères.
  free_text: 'TP : exercices permettant d’illustrer la spécificité d’un code Pythonique'
- title: Python avancé
  elements:
  - title: 'Usages avancés des fonctions '
    subelements:
    - Fonctions d’ordre supérieur
    - 'Présentation des décorateurs et de leurs usages classiques '
    - Décorateurs de la bibliothèque standard
  - title: Les classes de la bibliothèque collections
  - title: Les méthodes magiques des classes
  - title: 'Générateurs, coroutines et le mot clé yield '
  - title: Gestionnaires de contextes (context manager), définition et cas d’usages
    subelements:
    - 'Sous forme de classe Sous forme de fonctions '
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
    - 'Le débogueur textuel de python '
    - Les débogueurs graphiques
  free_text: 'TP : Configurer son éditeur de code pour intégrer des outils de QA,
    ajout de tests unitaires sur des codes précédents '
- title: Programmation orientée objet avancée
  elements:
  - title: Rappel des spécificités des objets en Python
  - title: Définition et utilisation des différents types de méthodes en Python
    subelements:
    - Les méthodes classiques
    - Les méthodes de classe
    - Les méthodes statiques
  - title: Le “duck typing” et l’interprétation
  - title: Spécificité de l’accès aux attributs en Python
    subelements:
    - Les méthodes magiques __getattribute__ et __getattr__
    - Les “property” pour l’encapsulation
  - title: 'L’héritage multiple et ses cas d’utilisation '
  - title: Les patrons de conception (design patterns)
    subelements:
    - Le concept de design patterns et leur utilité
    - Présentation de quelques design patterns connus et leurs cas d’utilisation classique
  free_text: 'TP : exercices sur la modélisation pythonique des objets en utilisant
    les différents mécanismes vus en classe. Utilisation de designs patterns pour
    organiser un code '
- title: Améliorer les performances de codes Python
  elements:
  - title: Mesurer les performances
    subelements:
    - Analyser les temps de réponses(« timeit » & « cprofile », techniques de visualisations)
  - title: Examiner la consommation mémoire
  - title: Initiation aux traitements répartis
    subelements:
    - 'Utilisation du multiprocessing '
    - 'Présentation du concept de “Map Reduce” '
    - 'Présentation du module Dask '
  free_text: 'TP : identification des goulots d’étranglement et optimisation des performances
    d’un programme simple '
- title: Utilisation de bibliothèques classiques de l’écosystème
  elements:
  - title: Découvrir les points importants pour choisir une bibliothèque
  - title: Installer correctement une bibliothèque Python
  - title: Étudier et parcourir la documentation d’une bibliothèque pour implémenter
      nos besoins
  free_text: 'TP : Mise en pratique sur un cas d’analyse de données (écosystème scientifique)
    ou un cas intéressant les stagiaires'
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

Cette formation vise d’une part à vous  donner une compréhension des mécanismes subtils qui font la force de Python (les opérations paresseuses et les générateurs, les fonctions avancées et les décorateurs, l’orienté objet et l’accès aux attributs). D’autre part, seront abordées les bonnes pratiques de développement (formatage du code, tests et mock, isoler et rendre reproductibles les projets...). 
