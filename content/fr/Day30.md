# L'art de créer des applications Streamlit

Aujourd'hui, c'est l'ultime défi de notre challenge *#30DaysOfStreamlit*!

Félicitations pour votre persévérance, que de chemin parcouru !

Dans ce tutoriel, nous allons mettre à profit toutes les connaissances acquises durant le challenge pour créer des applications qui nous aideront à résoudre des problèmes de la vie de tous les jours !

## Problème du monde réel

En tout bon créateur de contenu qui se respecte, l'accès aux images miniatures ("thumbnails" en anglais) des vidéos YouTube est une ressource très utile pour la création de contenu et leur promotion sur les réseaux sociaux.

Voyons comment nous allons résoudre ce problème via une app Streamlit!


## Solution

Aujourd'hui, nous allons créer `yt-img-app`, qui est une app Streamlit capable d'extraire des thumbnails de vidéos YouTube.

Voici les 3 étapes :

1. Acceptez une URL YouTube
2. Effectuez un traitement de texte sur cette l'URL pour extraire l'identifiant unique de la vidéo YouTube 
3. Utilisez cet identifiant comme entrée pour une fonction qui récupère et affiche ces "thumbnails"

## Des instructions

Pour commencer à utiliser l'application Streamlit, copiez et collez une URL YouTube dans la zone de saisie de texte.

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## Code
Voici comment créer l'application Streamlit `yt-img-app` :
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('Application d'extraction d'images miniatures YouTube')
with st.expander('About this app'):
  st.write('Cette application récupère l'image miniature d'une vidéo YouTube.')
  
# Paramètres des images
st.sidebar.header('Paramètres')
img_dict = {'Max' : 'maxresdefault', 'Élevé' : 'hqdefault', 'Moyen' : 'mqdefault', 'Standard' : 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Sélectionner la qualité d'image', ['Max', 'Elevé', 'Moyen', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Coller l'URL YouTube', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  si 'youtu.be' dans input_url :
    ytid = input_url.split('/')[-1]
  si 'youtube.com' dans input_url :
    ytid = input_url.split('=')[-1]
  retour ytid

# Afficher l'image miniature YouTube
si yt_url != '' :
  ytid = get_ytid(yt_url) # yt ou yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('URL de l'image miniature de la vidéo YouTube : ', yt_img)
else:
  st.write('☝️ Entrez l'URL pour continuer ...')
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, nous affichons le titre de l'application et l'en-tête qui l'accompagne :
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```
Ajoutons ensuite une boîte extensible 'About this app' :

```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video')
 
Puis, créons une selectbox qui propose differenmtes options sur la qualité d'image à utiliser.

```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

Une zone de saisie de texte s'affiche pour accepter la saisie de l'URL de la vidéo à utiliser pour extraire l'image.
```python
yt_url = st.text_input('Coller l'URL YouTube', 'https://youtu.be/JwSS70SZdyM')
```

Insérons maintenant une fonction pour effectuer le traitement de texte de l'URL:

```python
def get_ytid(input_url):
  si 'youtu.be' dans input_url :
    ytid = input_url.split('/')[-1]
  si 'youtube.com' dans input_url :
    ytid = input_url.split('=')[-1]
  retour ytid
```

Enfin, utilisons un "control flow" pour déterminer s'il faut afficher l'image miniature YouTube (voir l'instruction `if` dans le code ci dessous), ou un call-out a propos de l'URL (voir l'instruction `else`) :


```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## Résumé

En résumé, nous avons vu que lors de la création de toute application Streamlit, nous commençons par identifier le problème.

Nous concevons ensuite une solution pour résoudre ce problème, en le décomposant en étape par étape ; Étapes que nous implémentons bloc par bloc dans l'app Streamlit.

Nous devons également déterminer les données dont nous avons besoin comme entrées d'utilisateurs, la méthode à utiliser pour traiter ces données afin de produire le résultat final souhaité.

J'espère que vous avez apprécié ce tutoriel, Happy Streamlit-ing !