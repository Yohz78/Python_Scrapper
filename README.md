# Projet 2 formation developpeur python : 
## Utiliser les bases de python pour l'analyse de marché :

Le but de ce programme est d'extraire les données des articles présentés sur le site internet 'https://books.toscrape.com/index.html'.
Les données et illustrations des articles de ce site sont enregistrées respectivement en .csv et en .jpg dans le dossier du projet.

---

## 1) Installation

### 1) Clonage et navigation dans le dossier

Pour faire fonctionner ce projet, il est nécessaire de le cloner via la commande 

`git clone https://github.com/yohz78/Projet2`

`cd Projet2`

### 2) Préparation de l'environnement virtuel

Il faut ensuite installer le paquet nécessaire à la création d'un environnement virtuel via la `commande pip install virtualenv`.

### 3) Création de l'environnement virtuel

Un environnement virtuel devra ensuite être créé via l'execution de la commande `py -m venv .venv`

### 4) Installation des paquets

 Une fois cela fait, il faudra procéder à l'installation des paquets présents dans requirements.txt via la commande `pip install -r requirements.txt`

---
##  2) Utilisation

### 1) Execution du programme

Lancez le fichier "Scrapper.py"

### 2) Récupérez vos données

Les données sont maintenant présentes dans le dossier du programme !

Versionnages :

V0.1 : Initialisation du projet

V0.2 : Utilisation de classes et de dictionnaires

V0.3 : Extraction complète des infos des produits d'une page

V0.4 : Extractions des produits d'une catégorie entière

V0.5 : Nettoyage, remise en forme du code

V0.6 : Extrait toutes les informations des produits du site

V0.7 : Capable d'exporter les informations d'une catégorie en CSV

V0.8 : Créé un CSV avec toutes les informations produits du site

V1.0 : Version finale nettoyée, extrait toutes les informations produits dans un CSV par catégorie, extrait et enregistre les images de chaque article du site.