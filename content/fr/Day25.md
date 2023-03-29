# st.session_state

L'accès à une application Streamlit se fait en initialisant une session dans un onglet de votre navigateur. Pour chaque onglet se connectant au serveur Streamlit, une nouvelle session est créée. Streamlit réexécute votre script de haut en bas chaque fois que vous interagissez avec votre app. Aucune variable n'est partagée entre les exécutions.

`Session State` est un moyen de partager des variables entre les exécutions, et ce, pour chaque session.

En plus de la possibilité de conserver l'état (state) de l'app, Streamlit permet aussi de modifier cet état à l'aide de Callbacks.

Dans ce tutoriel, nous allons illustrer l'utilisation de Session State et des Callbacks et créant un convertisseur de poids.

`st.session_state` est le widget qui permet l'implémentation de Session State dans une application Streamlit.

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Code
Voici comment utiliser `st.session_state` :

```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Nous allons ensuite créer un titre pour l'application :
```python
st.title('st.session_state')
```

Ensuite, nous définissons des fonctions pour la conversion du poids en livres (`lbs`) et kilogrammes (`kg`), et vice versa :
```python
def lbs_to_kg() :
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs() :
  st.session_state.lbs = st.session_state.kg*2.2046
```

Ici, nous utilisons `st.number_input` pour accepter les entrées numériques des valeurs de poids :
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

Les deux fonctions ci-dessus sont appelées dès qu'une valeur est entrée via `st.number_input`. Remarquez comment l'option `on_change` spécifie les deux fonctions `lbs_to_kg` et `kg_to_lbs`.

Enfin, les valeurs de poids en unités `kg` et `lbs` telles que stockées dans le Session State sous `st.session_state.kg` et `st.session_state.lbs` sont affichées via `st.write` :

```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Lectures complémentaires
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Ajouter Session State à votre application](https://docs.streamlit.io/library/advanced-features/session-state)