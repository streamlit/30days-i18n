# Mise en place d'un environnement de développement local

Avant de pouvoir réellement commencer à créer des applications Streamlit, nous devrons d'abord configurer un environnement de développement.

Commençons par installer et configurer un environnement conda.

## **Installer Conda**
- Installez `conda` en allant sur https://docs.conda.io/en/latest/miniconda.html et choisissez votre système d'exploitation (Windows, Mac ou Linux).
- Téléchargez et exécutez le programme d'installation pour installer `conda`.

## **Créer un nouvel environnement Conda**
Maintenant que vous avez installé conda, créons un environnement conda pour gérer toutes les dépendances de la bibliothèque Python.

Pour créer un nouvel environnement avec Python 3.9, saisissez ce qui suit :
```bash
conda create -n stenv python=3.9
```

où `create -n stenv` créera un environnement conda nommé `stenv` et `python=3.9` configurera l'environnement conda avec Python version 3.9.

## **Activer l'environnement conda**

Pour utiliser un environnement conda que nous venons de créer et qui s'appelle `stenv`, entrez ce qui suit dans la ligne de commande :

```bash
conda activate stenv
```

## **Installez la bibliothèque Streamlit**

Il est maintenant temps d'installer la bibliothèque `streamlit` :
```bash
pip install streamlit
```

## **Lancement de la démo Streamlit**
Pour lancer la démo Streamlit (Figure 1), saisissez :
```bash
streamlit hello
```
