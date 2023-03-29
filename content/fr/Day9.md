# st.line_chart

`st.line_chart` affiche un graphique linéaire.

Il s'agit d'un sucre syntaxique d'`st.altair_chart`. La principale différence est que cette commande utilise les colonnes et indices de la base de données pour déterminer le graphique. Il est plus facile à utiliser tout en étant moins personnalisable.

Si `st.line_chart` ne devine pas correctement, essayez de spécifier le graphique souhaité à l'aide de `st.altair_chart`.

## Que construisons nous ?

Une application simple pour afficher un graphique linéaire:

1. Créez un DataFrame `Pandas` à partir de nombres générés aléatoirement via `NumPy`.
2. Créez et affichez le graphique linéaire via la commande `st.line_chart()`.

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Code
Voici comment utiliser [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) :
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` ainsi que d'autres bibliothèques comme celle-ci :

```python
import streamlit as st
import pandas as pd
import numpy as np
```

Ensuite, nous créons un en-tête (header) pour l'application :

```python
st.header('Line chart')
```

Ensuite, nous créons un DataFrame de nombres générés aléatoirement contenant 3 colonnes.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Enfin, un graphique linéaire est créé en utilisant `st.line_chart()` et le DataFrame stockée dans la variable `chart_data` comme donnée d'entrée :

```python
st.line_chart(chart_data)
```

## Lectures complémentaires
En savoir plus sur la commande [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) 