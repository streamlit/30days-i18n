# st.multiselect

`st.multiselect` zeigt ein Mehrfachauswahl- bzw. Multiselect-Widget an.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Code
So wird `st.multiselect` verwendet:
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('st.multiselect')
```

Als nächstes, werden wir das Widget `st.multiselect` verwenden, um Eingaben zu akzeptieren, bei denen die Benutzer eine oder mehrere Farben auswählen können.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Zuletzt zeigen wir die ausgewählten Farben an:
```python
st.write('You selected:', options)
```

## Literaturhinweise
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
