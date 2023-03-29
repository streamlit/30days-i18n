# st.slider

`st.slider` permet l'affichage d'un slider.

Les types de données suivants sont pris en charge : int, float, date, time et datetime.

## Que construisons nous ?

Une application simple qui montre les différentes manières d'accepter les entrées de l'utilisateur en ajustant le slider.

 :
1. L'utilisateur sélectionne la valeur en ajustant le slider
2. L'application affiche la valeur sélectionnée

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## Code
Voici comment utiliser st.slider :

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```


## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
from datetime import time, datetime
```


Ensuite, créons un en-tête (header) pour l'application :
```python
st.header('st.slider')
```

**Exemple 1**

Slider de type `Classique`:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```


Comme nous pouvons le voir, la commande `st.slider()` est utilisée pour collecter les données sur l'âge des utilisateurs.

Le premier argument d'entrée affiche le texte juste au-dessus du slider demandant `'How old are you?'`.

Les trois nombres suivants "0, 130, 25" représentent les valeurs minimale, maximale et par défaut, respectivement.

**Exemple 2**

Slider de type `range`:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

Le slider de de type `range` permet de sélectionner une paire de valeurs limites inférieure et supérieure.

Le premier argument d'entrée affiche le texte juste au-dessus du widget **slider de de type `range`** demandant `'Select a range of values'`.

Les trois arguments suivants "0.0, 100.0, (25.0, 75.0)" représentent les valeurs minimale et maximale tandis que le dernier tuple indique les valeurs par défaut à utiliser comme valeurs de limite inférieure (25.0) et supérieure (75.0) sélectionnées.

**Exemple 3**

Slider de type `time`:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

Le slider `time` permet de sélectionner une paire de valeurs (inférieure et supérieure) d'heure.

Le premier argument d'entrée affiche le texte au-dessus du slider: `'Schedule your appointment:`.

Les valeurs inférieure et supérieure de `time` par défaut sont 11:30 et 12:45, respectivement.

**Exemple 4**

Slider de type `datetime`:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

Le slider de type `Datetime` permet de sélectionner une date et une heure spécifique.

Le premier argument d'entrée affiche le texte au-dessus du slider: `'When do you start?'`.

La valeur par défaut pour la date et l'heure a été définie à l'aide de l'option `value`, dans notre exemple : le 1er janvier 2020 à 9h30.

## Lectures complémentaires
Vous pouvez également explorer la documentation associée:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)