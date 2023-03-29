
# st.checkbox

`st.checkbox` affiche un widget de type checkbox.

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Code
Voici comment utiliser `st.checkbox` :
```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```


## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un en-tête (header) pour l'application :
```python
st.header('st.checkbox')
```

Ensuite, nous allons poser une question via `st.write` :
```python
st.write ('What would you like to order?')
```

Nous allons ensuite fournir quelques éléments de menu à cocher :

```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

Enfin, nous allons afficher un texte personnalisé en fonction de la case cochée :
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## Lectures complémentaires
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)