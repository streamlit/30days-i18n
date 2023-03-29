# st.multiselect

`st.multiselect` muestra un componente de selección múltiple.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Código
Aquí se explica cómo usar `st.multiselect`:
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un encabezado para la aplicación:
```python
st.header('st.multiselect')
```

A continuación, vamos a utilizar el componente `st.multiselect` donde los usuarios podrán seleccionar uno o más colores de su elección.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Finalmente, escribiremos los colores seleccionados:
```python
st.write('You selected:', options)
```

## Otras lecturas
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
