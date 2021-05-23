---
title: Python idomatique
draft: false
identifier: pyidiomatique
domaines: développement
subdomain: Python
url: /formations/developpement/python-idiomatique
weight: '4'
catchphrase: 'Utilisez enfin Python à sa pleine mesure ! Découvrez les bibliothèques
  internes et les mécanismes méconnus ou sous-exploités du langage qui vous permettront
  de gagner un temps précieux de mise en œuvre et apporteront plus de robustesse à
  vos applications. '
duration: '3 jours, 21 heures '
equilibre: 35% théorie / 65% pratique
pricing: 1650 € HT par stagiaire (pauses et repas inclus)
objectifs:
- 'S’approprier et s’orienter dans la grande diversité des bibliothèques internes
  de Python '
- Apprendre à privilégier l’utilisation de ces bibliothèques afin de faciliter la
  maintenance de vos applications
- 'Maîtriser l’utilisation des techniques avancées du langage Python : Context Manager,
  Closures, Fonctions avancées, Itérateurs'
- Choisir les bonnes structures de données en fonction de la complexité des cas d’usage
prerequis:
- bonne maîtrise des fondamentaux du langage Python
- 'pratique quasi quotidienne de ce langage. '
publics:
- développeurs confirmés
- 'débutant s’abstenir '
programme:
- title: Rappels sur les bibliothèques utiles
  elements:
  - title: La bibliothèque « logging »
    subelements:
    - Intérêt par rapport à la fonction print
    - 'Intérêts et principes '
    - Mise en oeuvre d’un premier exemple (par programmation ou par fichier de configuration)
    - Modifier les filtres
    - Point sur les traces en multi-threading, en multi-processing
  - title: Les arguments en ligne de commande
    subelements:
    - La variable « sys.argv »
    - La bibliothèque « argparse »
    - La bibliothèque externe « click »
  - title: Les fichiers de configuration
    subelements:
    - La bibliothèque « configparser »
    - La bibliothèque  « json »
    - Le traitement des fichiers YAML
- title: Les structures de données avancées et leurs outils
  elements:
  - title: Rappel sur les types en Python
    subelements:
    - Les types avancés (« Containers », « Collections », « Sequences », « Mapping »)
    - Propriétés des types et méthodes magiques (mutable, subscriptable, hashable,
      trucmuchable, …)
    - Introduction aux annotations
  - title: Programmation Orienté Objet Avancée
  - title: La bibliothèque « collections »
    subelements:
    - 'defaultdict, '
    - Counter
    - deque 
    - namedtuple
  - title: Les fonctions de manipulation des collections
    subelements:
    - Fonctions « map »/ « filter » vs générateurs à la volée
    - Fonctions “all” et “any”
    - La bibliothèque « itertools », les itérateurs
  - title: Les bibliothèques « heapq » et « bisect »
    subelements:
    - Intérêts
    - Exemple de mise en œuvre
- title: ' Techniques avancées'
  elements:
  - title: Fonctions avancées et pièges classiques
    subelements:
    - 'Le piège des paramètres par défaut de types mutables '
    - L’opérateur logique  « or » lors des affectations
    - 'Différentes façons de créer les fonctions (lambda, def) '
    - Espaces de noms et règle LEGB (variables « local », « non local », « global »
      et concept de closure)
    - Paramètres à volonté avec *args et **kwargs
    - 'Fonctions d’ordres supérieurs '
  - title: Les décorateurs (ou fonction englobante)
    subelements:
    - Présentation du concept
    - Les closures
    - Cas d’usage des décorateurs
    - Mise en œuvre (à l’aide de fonctions et de classes)
    - Paramètres de décorateurs
    - Études de décorateurs de la bibliothèque « functools » (@lru_cache, @wraps)
  - title: Les « Context Managers »
    subelements:
    - Présentation et cas d’usage (fichiers, bases de données, réseau, accès concurrent
      aux données...)
    - Intégration sur une classe avec les « dunder » méthodes spécifiques
    - Intégration sur une fonction avec la bibliothèque « contextlib »
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

Cette formation présente concepts avancés et peu connus de Python : structures internes avancées, décorateurs, gestionnaires de contexte, itérateurs et leurs mises en œuvre respectives.
