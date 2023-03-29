# st.write

`st.write` permet d'écrire du texte et des arguments dans l'application Streamlit.

En plus de pouvoir afficher du texte, les éléments suivants peuvent également être affichés via la commande `st.write()` :


- Affiche un `dict` Python
- Les DataFrames `pandas` peuvent être affichés
- Tracés et graphiques de `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
- Fonctionne aussi comme `st.markdown()`
- Et plus (voir [st.write on API docs](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## Que construisons nous ?

Une application simple montrant les différentes manières d'utiliser la commande `st.write()` pour afficher du texte, des nombres, des DataFrames et des graphiques.

## Application de démonstration

L'application Streamlit déployée devrait ressembler à celle illustrée dans le lien ci-dessous :

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Code

Voici comment utiliser st.write :

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'première colonne' : [1, 2, 3, 4],
     'deuxième colonne' : [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Ci-dessous se trouve un DataFrame :', df, 'Ci-dessus se trouve un DataFrame.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Explication ligne par ligne

La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st`, comme ceci :

```python
import streamlit as st
```

Ensuite, créons un en-tête (header) pour l'application :

```python
st.header('st.write')
```

**Exemple 1**
Afficher du texte et du texte au format Markdown :

```python
st.write('Hello, *World!* :sunglasses:')
```

**Exemple 2**
Afficher d'autres formats de données tels que des nombres :

```python
st.write(1234)
```

**Exemple 3**
Les DataFrames peuvent également être affichées, comme suit :

```python
df = pd.DataFrame({
     'première colonne' : [1, 2, 3, 4],
     'deuxième colonne' : [10, 20, 30, 40]
     })
st.write(df)
```

**Exemple 4**
Vous pouvez passer plusieurs arguments :

```python
st.write('le DataFrame est au dessus:', df, 'le DataFrame est en dessous.')
```

**Exemple 5**
Enfin, vous pouvez également afficher des graphiques en les intégrant à une variable, comme suit :

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Application de démonstration

L'application Streamlit déployée devrait ressembler à celle illustrée dans le lien ci-dessous :

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Prochaines étapes

Maintenant que vous avez créé l'application Streamlit localement, il est temps de la déployer sur [Streamlit Community Cloud](https://streamlit.io/cloud) comme on vous l'expliquera dans un prochain défi.

Comme il s'agit de la première semaine de votre défi, nous fournissons le code complet (code ci-dessus) et la solution (l'app de démonstration) sur cette page Web.

Pour progresser dans les prochains défis, il est recommandé d'essayer d'implémenter l'app Streamlit vous-même! Ne vous inquiétez pas si vous êtes bloqué, vous pouvez toujours jeter un coup d'œil à la solution.

## Lectures complémentaires

En plus de [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write), vous pouvez explorer les autres façons d'afficher du texte :

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)