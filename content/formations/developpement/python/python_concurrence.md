---
title: Programmation concurrente en Python
draft: false
identifier: pyconcurrent
domaines: développement
subdomain: Python
url: /formations/developpement/python-programmation-concurrente
weight: '5'
catchphrase: Cette formation a pour objectif de présenter diverses façons de paralléliser
  vos traitements en Python afin de tirer parti des architectures multi-cœurs ou multi-machines
  modernes.
duration: '2 jours, 14 heures '
equilibre: 35% théorie / 65% pratique
pricing: 1200 € HT par stagiaire (pauses et repas inclus)
objectifs:
- Découvrir et explorer les différentes techniques de traitements parallèles.
- Acquérir les concepts de la programmation parallèle, de synchronisation et de partages
  de données
- Sachez identifier les portions de programme qui sont parallélisables
- Sachez repérer les goulots d’étranglements dans votre code
- Identifier les parties de code consommatrices en temps de traitement, en ressources,
  qui sont candidates à des optimisations
prerequis:
- Bonne maîtrise et bonne pratique du langage Python
- Connaissance de la problématique de la parallélisation dans d’autres langages sera
  clairement un avantage
publics:
- développeurs, chercheurs, ingénieurs confrontés à des problèmes d’optimisation de
  temps de traitement
- débutants s’abstenir
programme:
- title: Rappels et bibliothèques d’outils
  elements:
  - title: Mesurer les performances
    subelements:
    - Analyser les temps de réponses
    - Les profilers de la bibliothèque standard python (timeit, cprofile)
    - Les profilers tiers
    - Techniques de visualisation
    - Examiner la consommation mémoire (gestion des structures complexes, le garbage
      collector, la bibliothèque externe memory_profiler)
  - title: Rappel sur la gestion des erreurs
    subelements:
    - Concept et mise en œuvre des exceptions
  free_text: 'TP : identification des goulots d’étranglement et optimisation des performances
    d’un programme simple '
- title: Principe de programmation concurrente et première mise en œuvre
  elements:
  - title: Présentation des cas d’utilisation (découpage des temps de traitement,
      répartition de l’utilisation mémoire, gestion des taches longues ou bloquantes)
    subelements:
    - Contrôler l’accès aux ressources
    - Utiliser les temps d’attente liés aux entrées / sorties pour effectuer d’autres
      traitements
    - Répartir la charge des traitements lourds, longs.
  - title: 'Présentation des différents concepts et du vocabulaire '
- title: Introduction à la programmation concurrente avec la bibliothèque « threading »
  elements:
  - title: Rappel sur la gestion mémoire
  - title: Création de Threads en Python (fonctions et classes)
  - title: 'La communication inter-tâche '
    subelements:
    - Principe
    - 'Les outils : verrou, sémaphore, évènement, queue'
  - title: "\tCas d’usages et limitations"
  - title: "\tLes traces en multi-tâche"
  - title: "\tArrêt propre des Threads"
  free_text: 'TP : création d’un ordonnanceur de threads, avec mise en place d’un
    arrêt propre des threads lancés'
- title: 'La programmation multi-processus :  la bibliothèque « multiprocessing »'
  elements:
  - title: "\tCas d’usages et architecture map / reduce"
  - title: "\tNotion de Pools"
  - title: "\tLes traces en multi-processus"
  free_text: 'TP : Mise en œuvre d’un découpage de traitements longs puis d’agrégation
    des résultats'
- title: 'La programmation asynchrone : la bibliothèque « asyncio »'
  elements:
  - title: "\tPrincipe et cas d’usage"
  - title: "\tLes « futures », les tasks"
  - title: "\tLe lancement des futures, la gestion des futures"
  - title: "\tLa boucle locale"
  - title: "\tLa gestion des tâches longues"
- title: Initiation aux traitements répartis (sur plusieurs machines)
  elements:
  - title: 'Mise en œuvre en python natif : '
    subelements:
    - Avec la bibliothèque « multiprocessing » et les managers
  - title: Autres mises en œuvre existantes
    subelements:
    - 'La bibliothèque externe « RPyc» '
    - La bibliothèque externe « ray »
    - Découverte des bibliothèques externes “Dask”
    - Allez plus loin (discussion autour de Spark, Airflow)
  free_text: 'TP :  mise en œuvre des différentes bibliothèques et restitution en
    groupes'
- title: Synthèse sur les cas d’usage
  elements:
  - title: Dans quels cas utiliser le multithreading, le multiprocessing, la programmation
      asynchrone et la programmation répartie ?
  - title: Réflexions sur le SPMD (Single Program Multiple Data), MPSD (Multple Instructions
      Single Data)
  - title: 'Discussion sur les temps incompressibles (loi d''Amdahl) et la séparabilité
      des données '
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

Apprenez et mettez en œuvre des techniques de l’écosystème Python pour optimiser, accélérer et répartir vos traitements. 
