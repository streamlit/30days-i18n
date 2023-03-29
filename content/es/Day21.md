# st.progress

`st.progress` muestra una barra de progreso que se actualiza gráficamente a medida que avanza la iteración.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## Código
Así es como se usa `st.progress`:
```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` junto con `time` de la siguiente manera:
```python
import streamlit as st
import time
```

A continuación, creamos un título para la aplicación:
```python
st.title('st.progress')
```

Se crea un cuadro **Acerca de** usando `st.expander` y la descripción se muestra a través de `st.write`:
```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

Finalmente, definimos una barra de progreso y la instanciamos con un valor inicial `0`. Luego, un ciclo `for` va a iterar desde `0` hasta `100`. Por cada iteración, usamos `time.sleep(0.05)` para permitir a la aplicación esperar durante `0.05` antes de sumar `1` a la barra de progreso `my_bar` y al hacerlo, la representación gráfica de la barra aumenta con cada iteración.
```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Otras lecturas
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
