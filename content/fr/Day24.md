# st.cache

`st.cache` vous permet d'optimiser les performances de votre application Streamlit!

Streamlit fournit un mécanisme de mise en cache qui permet à votre app de rester performante même lors du chargement (ou de la manipulation) de large quantité de données, ou bien encore de l'exécution de calculs complexes.

Ceci est possible grâce au décorateur `@st.cache`.

Lorsque vous ajoutez le décorateur `@st.cache` à une fonction Python, cela indique à Streamlit qu'à chaque fois que la fonction est appelée, elle doit vérifier quelques éléments :

1. Les paramètres d'entrée avec lesquels vous avez appelé la fonction
2. Les valeurs des variables externes utilisées dans la fonction
3. Le corps de toute fonction utilisée dans la fonction mise en cache

Si c'est la première fois que Streamlit voit ces trois composants (dans cette combinaison et cet ordre précis), il exécute la fonction et stocke le résultat dans un cache local.

Lorsque la fonction mise en cache une seconde fois, Streamlit ignorera l'exécution de la fonction et, à la place, renverra la sortie précédemment stockée dans le cache !

Magique ! N'est-ce pas ?

`@st.cache` prend aussi en compte les arguments pour configurer le comportement du cache. Vous pouvez trouver plus d'informations sur ces derniers dans notre [Documentation API](https://docs.streamlit.io/library/api-reference/performance/st.cache).


## Comment utiliser `st.cache`?


Il suffit d'ajouter le décorateur `st.cache` au-dessus d'une fonction Python, c'est aussi simple que cela !

Voyons l'exemple ci-dessous.

## Démo

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Code
Voici comment utiliser `st.cache` :

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```


## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` ainsi que d'autres bibliothèques utilisées dans l'application comme ceci :
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

Ensuite, créons un titre pour l'application :
```python
st.title('Streamlit Cache')
```

Ensuite, nous définirons deux fonctions personnalisées pour générer un DataFrame: la première utilise le décorateur `st.cache`, tandis que la seconde ne l'utilise pas :
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Enfin, nous exécutons la fonction personnalisée tout en chronométrant le temps d'exécution à l'aide de la commande `time()`.
```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Notez comme la première exécution est similaire dans les deux cas. Maintenant, rechargez l'app et notez comment le temps d'exécution change lorsque vous utilisez le décorateur `st.cache`. 

Avez-vous observé un temps de chargement plus rapide ?


## Lectures complémentaires
- [Documentation API `st.cache`](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Optimiser les performances avec `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Primitives de cache expérimentales](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)