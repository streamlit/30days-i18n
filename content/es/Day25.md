# st.session_state

Definimos el acceso a una aplicación Streamlit en una pestaña del navegador como una sesión. Para cada pestaña del navegador que se conecta al servidor Streamlit, se crea una nueva sesión. Streamlit se vuelve a ejecutar de arriba a abajo cada vez que se interactúa con la misma. Cada repetición se realiza en blanco: no se comparten variables entre ejecuciones.

Session State es una forma de compartir variables entre ejecuciones, para cada sesión de usuario. Además de la capacidad de almacenar y conservar el estado, Streamlit también expone la capacidad de manipular el estado mediante Callbacks.

En este tutorial, ilustraremos el uso de Session State y los Callbacks a medida que construimos una aplicación de conversión de peso.

`st.session_state` permite la implementación de Session State en una aplicación Streamlit.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Code
Aquí se explica cómo usar `st.session_state`:
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

En primer lugar, comenzaremos creando el título de la aplicación:
```python
st.title('st.session_state')
```

A continuación, definimos funciones para la conversión de peso de libras a kg y viceversa:
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

Aquí, usamos `st.number_input` para permitir el ingreso de datos numéricos de los valores de peso:
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```
Las 2 funciones anteriores se activarán tan pronto como se ingrese un valor en el campo numérico creado con el comando `st.number_input`. Observe cómo la opción `on_change` especifica las 2 funciones `lbs_to_kg` y `kg_to_lbs`).

En pocas palabras, al ingresar un número en el campo `st.number_input`, estas funciones convierten el número.

Finalmente, los valores de peso en unidades `kg` y `lbs` almacenados en el estado de la sesión como `st.session_state.kg` y `st.session_state.lbs` se imprimirán a través de `st.write`:
```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

- ## Otras lecturas
- [Estado de la sesión](https://docs.streamlit.io/library/api-reference/session-state)
- [Agregar estado a las aplicaciones](https://docs.streamlit.io/library/advanced-features/session-state)
