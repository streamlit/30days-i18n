# st.latex

`st.latex` muestra expresiones matemáticas formateadas como LaTeX.

## Qué estamos construyendo?

Una aplicación simple que muestra una ecuación matemática utilizando la sintaxis de LaTeX a través del comando `st.latex`.

## Demo app
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## Código
Así es como se usa `st.latex`:
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un texto de encabezado:
```python
st.header('st.latex')
```

A continuación, mostramos la ecuación matemática a través de `st.latex`:
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Referencias
- Obtenga más información sobre [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) en la documentación de la API de Streamlit.
