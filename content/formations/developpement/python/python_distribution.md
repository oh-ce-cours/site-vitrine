---
title: Distribuer son code Python
draft: true
identifier: pysharing
domaines: développement
subdomain: Python
url: /formations/developpement/python-partager-son-code-python
weight: '7'
catchphrase: 'Découvrez comment utiliser correctement les modules de l’écosystème
  Python et les techniques pour diffuser vos propres bibliothèques. . '
duration: 2j - 14 heures
equilibre: 35% théorie / 65% pratique
pricing: 1400 € HT par stagiaire (pauses et repas inclus)
objectifs:
- Identifier et appliquer les bonnes pratiques d’installation de dépendances sur un
  projet Python
- Packager et déployer ses bibliothèques
prerequis:
- Bonnes maitrise de Python (syntaxe, fonctions, orienté objet, notion de modules
  et d’imports)
publics:
- Développeurs
- Ingénieurs
- ' chefs de projets proches du développement.'
programme:
- title: Rappels sur la gestion de bibliothèques Python
  elements:
  - title: Les mécanismes d’import de code en Python et les chemins utilisés
    subelements:
    - Qu’est-ce qu’un module python?
    - Le cas de la bibliothèque standard
    - 'L’installation de modules tiers (avec pip ou un gestionnaire de paquet Linux)
      et le dossier site-packages '
    - Importer du code et des modules
    - Le PYTHONPATH et sa manipulation (au niveau de l’OS ou en Python directement)
  - title: Les différentes façons de partager du code Python
    subelements:
    - Les sources
    - 'Les wheels '
    - Les autres gestionnaires de paquets
  - title: 'Les environnements virtuels pour gérer facilement les projets '
    subelements:
    - 'Le concept et les cas d’usages des environnements virtuels '
    - Création et évolution d’environnements virtuels
    - La notion de requirements.txt
  - title: 'Le cas des bibliothèques complexes '
    subelements:
    - Reproduire une configuration de compilation
    - Rôle de Docker, Vagrant, Ansible par rapport aux virtualenv
  free_text: 'TP : importer et installer des bibliothèques, même anciennes que l’on
    doit compiler localement. Utilisation des fichiers de requirements pour réinstaller
    un projet et des environnements virtuels pour passer d’un projet à un autre.'
- title: Création de bibliothèques pour contribuer à l’écosystème Python
  elements:
  - title: 'Rappel sur PyPI et pip '
  - title: 'La structure d’un module python '
    subelements:
    - 'Arborescence standard '
    - Les fichiers sources
    - Les fichiers de tests
    - Les autres fichiers
  - title: Les fichiers de description du paquet
    subelements:
    - Setup.py
    - 'Setup.cfg '
    - L’ajout de fichiers tiers (données…)
    - La création d’interface en ligne de commande (avec les entry points)
  - title: 'La création proprement dite du paquet (source et wheel) et sa diffusion
      sur PyPI publique ou en privé (sur un dépôt git) '
  - title: 'Comment intégrer du code natif à un projet '
    subelements:
    - 'Les étapes de la compilation '
    - La création de wheels pour les différentes architectures
  - title: Les autres moyens d’empaqueter (conda…)
  free_text: 'TP : création d’un paquet simple et mise à disposition sur le dépôt
    de tests de PyPI et sur un git public'
- title: Création et partage de programmes autonomes
  elements:
  - title: 'Présentation de l’outil PyInstaller '
    subelements:
    - Gestion des bibliothèques
    - Gestion des fichiers tiers
    - Utilisation sous Windows, Linux et MacOs
  - title: Présentation de InnoSetup
  free_text: 'TP : création d’un exécutable à partir d’un programme de démonstration
    et installation sur un poste n’ayant pas Python'
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

Dans cette formation, vous verrez, dans un premier temps, comment profiter de l’écosystème des bibliothèques Python, nous verrons comment installer correctement des bibliothèques et rendre vos installations facilement duplicables . Dans un second temps, vous découvrirez comment contribuer à l’écosystème en ajoutant vos propres bibliothèques. 
