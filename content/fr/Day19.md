# Améliorer la mise en page de votre app Streamlit

Dans ce tutoriel, nous allons utiliser les commandes suivantes pour mettre en page notre application Streamlit :
- `st.set_page_config(layout="wide")` - Affiche le contenu de l'application en mode "large".
- `st.sidebar` - Place les widgets dans la barre latérale.
- `st.expander` - Place les widgets dans un expander.
- `st.columns` - Crée une colonne dans lequel le contenu peut être placé.

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Code
Voici comment personnaliser la mise en page de votre application Streamlit :
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Définissons la mise en page en mode "large", qui permet au contenu de la page de s'étendre à la largeur du navigateur :

```python
st.set_page_config(layout="wide")
```

Ensuite, donnons un titre à l'application Streamlit :
```python
st.title('Comment mettre en page votre application Streamlit')
```

Une zone extensible `About this app` placée sous le titre :

```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Les widgets `text_input` et `selectbox` sont placés dans la barre latérale via la commande `st.sidebar`. Ces valeurs sont stockées dans les variables `user_name`, `user_emoji` et `user_food`:
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Enfin, nous allons créer 3 colonnes à l'aide de la commande `st.columns` : `col1`, `col2` et `col3`.

Attribuons un contenu à chacune de nos colonnes en créant des blocs de code commençant par l'instruction `with`.

Ensuite, créons les instructions conditionnelles qui affichent un texte alternatif sur deux selon que l'utilisateur ajoute ses données ou non.

Par défaut, la page affiche le texte sous l'instruction `else`.

Lors de la saisie, les informations que l'utilisateur donne à l'application sont affichées sous l'en-tête 'Output' :


```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

Il convient également de noter que des `f-strings` sont utilisées pour combiner les textes statiques avec les valeurs fournies par l'utilisateur.

## Lectures complémentaires
- [Mises en page et conteneurs](https://docs.streamlit.io/library/api-reference/layout)