# st.slider

`st.slider` permite la visualización de un control deslizante.

Se admiten los siguientes tipos de datos: int, float, date, time y datetime.

## Que estamos construyendo?

Una aplicación simple que muestra diferentes maneras de como aceptar datos del usuario con el control deslizante

Comportamiento de la aplicación:
1. El usuario selecciona el valor ajustando el control deslizante
2. La aplicación imprime el valor seleccionado

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## Código
He aquí cómo usar st.slider:

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Ejemplo 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Ejemplo 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Ejemplo 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Ejemplo 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la biblioteca `streamlit` como `st` así:
```python
import streamlit as st
from datetime import time, datetime
```

A esto le sigue la creación de un texto de encabezado para la aplicación::
```python
st.header('st.slider')
```

**Ejemplo 1**

Deslizador:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

Como podemos ver, el comando `st.slider()`
se utiliza para recopilar información del usuario sobre la edad de los usuarios.

El primer argumento de entrada muestra el texto justo encima del componente **slider** que pregunta `'How old are you?'`.

Los siguientes tres enteros `0, 130, 25` representan los valores mínimo, máximo y predeterminado, respectivamente.

**Ejemplo 2**

Slider de rango:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

El control deslizante de rango permite la selección de un par de valores límite inferior y superior.

El primer argumento muestra el texto justo encima del control deslizante de **rango** que pregunta `'Select a range of values'`.

Los siguientes tres argumentos `0.0, 100.0, (25.0, 75.0)` representan los valores mínimo y máximo, mientras que la última tupla indica los valores predeterminados que se utilizarán como valores límite inferior (25.0) y superior (75.0) seleccionados.

**Ejemplo 3**

Deslizador para rango de tiempo:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

El control deslizante de rango de tiempo permite la selección de un par de valores límite inferior y superior de fecha y hora.

El primer argumento muestra el texto justo encima del control deslizante de **rango de tiempo** que pregunta `'Schedule your appointment:`.

Los valores predeterminados para los pares de valores límite inferior y superior de fecha y hora se establecen en 11:30 y 12:45, respectivamente.

**Ejemplo 4**

Datetime slider:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

El control deslizante de datetime permite la selección de una fecha y hora.

El primer argumento muestra el texto justo encima del control deslizante **datetime** que pregunta `'When do you start?'`.

El valor predeterminado para la fecha y hora se estableció mediante la opción `value` para que sea el 1 de enero de 2020 a las 9:30

## Otras lecturas
También puede explorar el siguiente componente relacionado:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
