# Streamlit Komponenten

Komponenten sind Python-Module von Drittanbietern, die die Möglichkeiten von Streamlit erweitern [[1](https://docs.streamlit.io/library/components)].

## Welche Streamlit-Komponenten gibt es?

Es gibt mehrere Streamlit-Komponenten, die auf der Streamlit-Website [[2](https://streamlit.io/components)] vorgestellt werden.

Fanilo (ein Streamlit-Entwickler) hat eine erstaunliche Liste von Streamlit-Komponenten in einem Wiki-Beitrag [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)] zusammengestellt, die seit April 2022 etwa 85 Streamlit Komponenten auflistet.

## Wie wird es verwendet?

Streamlit-Komponenten brauchen nur eine einfache pip-Installation.

In diesem Tutorial zeigen wir dir, wie man die Komponente `streamlit_pandas_profiling` verwenden kann [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### Komponente installieren

```bash
pip install streamlit_pandas_profiling
```

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## Code
So erstellt man eine Streamlit App mithilfe einer Komponent:
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

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('`streamlit_pandas_profiling`')
```

Als nächstes laden wir den Penguins-Datensatz mit dem Befehl `read_csv` von `pandas`.
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Zuletzt wird der Profiling-Bericht von `pandas` mit dem Befehl `profile_report()` erstellt und mit `st_profile_report` angezeigt:
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Eigene Komponenten erstellen

Wenn du daran interessiert bist, deine eigene Komponente zu erstellen, schau dir die folgenden Ressourcen an:
- [Create a Component](https://docs.streamlit.io/library/components/create)
- [Publish a Component](https://docs.streamlit.io/library/components/publish)
- [Components API](https://docs.streamlit.io/library/components/components-api)
- [Blog post on Components](https://blog.streamlit.io/introducing-streamlit-components/)

Wenn du lieber mit Videos lernen möchten, hat unser Entwickler Tim Conkling ein paar tolle Tutorials zusammengestellt:
- [How to build a Streamlit component | Part 1: Setup and Architecture](https://youtu.be/BuD3gILJW-Q)
- [How to build a Streamlit component | Part 2: Part 2: Make a Slider Widget](https://youtu.be/QjccJl_7Jco)

## Weitere Informationen über Komponenten
1. [Streamlit Components - API Documentation](https://docs.streamlit.io/library/components)
2. [Featured Streamlit Components](https://streamlit.io/components)
3. [Streamlit Components - Community Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
