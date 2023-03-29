# st.checkbox

`st.checkbox` muestra un componente de casilla de verificación.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Código
Aquí se explica cómo usar `st.checkbox`:
```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A esto le sigue la creación de un encabezado para la aplicación:
```python
st.header('st.checkbox')
```

A continuación, haremos una pregunta a través de `st.write`:
```python
st.write ('What would you like to order?')
```

Luego vamos a proporcionar algunos elementos de menú para seleccionar:
```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

Finalmente, vamos a imprimir texto personalizado según la casilla de verificación que se seleccionó:
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## Otras lecturas
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
