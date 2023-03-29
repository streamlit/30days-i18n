# st.multiselect

`st.multiselect` affiche un widget multiselect.

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Code
Voici comment utiliser `st.multiselect` :

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un texte d'en-tête pour l'application :
```python
st.header('st.multiselect')
```

Ensuite, nous allons utiliser le widget `st.multiselect` pour accepter les entrées où les utilisateurs pourront sélectionner une ou plusieurs couleurs de leur choix.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Enfin, écrivon les couleurs sélectionnées :

```python
st.write('You selected:', options)
```

## Lectures complémentaires
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)