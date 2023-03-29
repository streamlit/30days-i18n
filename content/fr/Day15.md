# st.latex

`st.latex` affiche des expressions mathématiques au format LaTeX.

## Que construisons nous ?

Une application simple qui affiche une équation mathématique utilisant la syntaxe LaTeX via la commande `st.latex`.

## Application de démonstration
[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## Code
Voici comment utiliser `st.latex` :
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     une + ar + une r^2 + une r^3 + \cdots + une r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` comme ceci :
```python
import streamlit as st
```

Ensuite, créons un en-tête (header) pour l'application :
```python
st.header('st.latex')
```

Ensuite, nous affichons l'équation mathématique via `st.latex` :
```python
st.latex(r'''
     une + ar + une r^2 + une r^3 + \cdots + une r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Références
- En savoir plus sur [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex).