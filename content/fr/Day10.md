# st.selectbox

`st.selectbox` permet l'affichage d'un widget de sélection.

## Que construisons nous ?

Une application simple qui demande à l'utilisateur quelle est sa couleur préférée.

Déroulement de l'application :
1. L'utilisateur sélectionne une couleur
2. L'application affiche la couleur sélectionnée

## Application de démonstration
L'application Streamlit déployée devrait ressembler à celle illustrée dans le lien ci-dessous :

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## Code
Voici le code pour implémenter l'application mentionnée ci-dessus :

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un en-tête (header) pour l'application :
```python
st.header('st.selectbox')
```

Maintenant, nous allons créer une variable appelée `option` qui acceptera notre widget de sélection via la commande `st.selectbox()`.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```

Comme nous le voyons dans le code ci-dessus, la commande `st.selectbox()` accepte 2 arguments :
1. Le texte qui se trouve au-dessus du widget de sélection, c'est-à-dire `'What is your favorite color?'`
2. Les valeurs possibles à sélectionner parmi `('Blue', 'Red', 'Green')`

Enfin, imprimons la couleur sélectionnée comme suit :
```python
st.write('Votre couleur préférée est ', option)
```

## Prochaine étape
Maintenant que vous avez créé l'application Streamlit localement, il est temps de la déployer sur [Streamlit Community Cloud](https://streamlit.io/cloud)!

## Références
En savoir plus sur [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)