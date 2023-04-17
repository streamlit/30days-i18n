# st.latex

`st.latex` zeigt LaTeX-formatierte mathematische Ausdrücke an. 

## Was bauen wir?

Eine einfache App, die mithilfe des Befehls `st.latex` eine mathematische Gleichung in LaTeX-Syntax anzeigt.

## Demo App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## Code
So wird `st.latex` verwendet:
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('st.latex')
```

Als nächstes, zeigen wir mit `st.latex` die mathematische Gleichung:
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Referenzen
- Lies mehr über [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) in der Streamlit-API-Dokumentation.
