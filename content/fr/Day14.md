# Composants Streamlit

Les composants sont des modules Python tiers qui étendent les possibilités de Streamlit [[1](https://docs.streamlit.io/library/components)].

## Quels sont les composants disponibles ?

Il existe des dizaines de composants Streamlit présentés sur le site de Streamlit [[2](https://streamlit.io/components)].

Fanilo (un de nos plus fervent créateur) a crée une liste exhaustive des composants sur cet article wiki [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]. L'article répertorie 85 composants à compter d'Avril 2022.

## Comment les utiliser?

Les composants Streamlit s'installent simplement via `pip d'install`.

Dans ce tutoriel, commençons à utiliser le composant `streamlit_pandas_profiling` [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### Installer le composant

```bash
pip install streamlit_pandas_profiling
```

## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## Code
Voici comment créer une application Streamlit à l'aide d'un composant :

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st` ainsi que toutes les autres bibliothèques utilisées dans l'application :

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

Ensuite, créons un en-tête (header) pour l'application :
```python
st.header('`streamlit_pandas_profiling`')
```

Chargeons maintenant la base de données `Penguins` à l'aide de la commande `read_csv` de Pandas.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Enfin, le `Pandas Profiler` est généré via la commande `profile_report()`, et affiché à l'aide de `st_profile_report` :
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Créez vos propres composants

Si vous souhaitez créer votre propre composant, veuillez consulter les ressources suivantes :
- [Créer un composant](https://docs.streamlit.io/library/components/create)
- [Publier un composant](https://docs.streamlit.io/library/components/publish)
- [API des composants](https://docs.streamlit.io/library/components/components-api)
- [Article d'intro sur les composants](https://blog.streamlit.io/introducing-streamlit-components/)


Si vous préférez apprendre à l'aide de vidéos, notre ingénieur Tim Conkling vous a concocté d'excellents tutos, que vous pouvez consulter ci-dessous:
- [Comment construire un composant Streamlit | Partie 1 : Configuration et architecture](https://youtu.be/BuD3gILJW-Q)
- [Comment construire un composant Streamlit | Partie 2 : Partie 2 : Créer un widget Slider](https://youtu.be/QjccJl_7Jco)

## En savoir plus sur les composants
1. [Composants Streamlit - Documentation API](https://docs.streamlit.io/library/components)
2. [Composants Streamlit en vedette](https://streamlit.io/components)
3. [Composants Streamlit - Community Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)