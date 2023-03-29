# Cómo diseñar su aplicación Streamlit

En este tutorial, usaremos los siguientes comandos para diseñar nuestra aplicación Streamlit:
- `st.set_page_config(layout="wide")` - Muestra el contenido de la aplicación en modo ancho (de lo contrario, de forma predeterminada, el contenido se encapsula en un cuadro de ancho fijo).
- `st.sidebar` - Coloca los componentes o visualizaciones de texto/imagen en la barra lateral.
- `st.expander` - Coloca visualizaciones de texto/imagen dentro de una caja contenedora plegable.
- `st.columns` - Crea un espacio tabular (o columna) para contener lo que necesites.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Código
Aquí le mostramos cómo personalizar el diseño de su aplicación Streamlit:
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

Comenzaremos definiendo primero el diseño de la página que se mostrará en el modo "wide" (ancho), lo que permite que el contenido de la página se expanda al ancho del navegador.
```python
st.set_page_config(layout="wide")
```

A continuación, le daremos un título a la aplicación Streamlit.
```python
st.title('How to layout your Streamlit app')
```

Un cuadro expandible titulado `About this app` se coloca debajo del título de la aplicación. Tras la expansión, veremos detalles adicionales.
```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Los componentes que aceptan datos de entrada se posicionan en la barra lateral utilizando el comando `st.sidebar` previo a los comandos `text_input` y `selectbox`. Los datos ingresados o seleccionados por el usuario son asignados y guardados en las variables `user_name`, `user_emoji` y `user_food`.
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Finalmente, crearemos 3 columnas usando el comando `st.columns` que corresponde a `col1`, `col2` y `col3`. Luego, asignamos contenidos a cada una de las columnas mediante la creación de bloques de código individuales que comienzan con la instrucción `with`. Debajo de esto, creamos declaraciones condicionales que muestran 1 de 2 textos alternativos dependiendo de si el usuario proporcionó datos (especificados en la barra lateral) o no. De forma predeterminada, la página muestra texto debajo de la instrucción `else`. Al proporcionar datos, la información correspondiente del usuario se muestra bajo el encabezado `Output`.
```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```
También vale la pena señalar que las cadenas `f` se usaron para combinar texto preestablecido junto con los valores proporcionados por el usuario.

## Otras lecturas
- [Diseños y contenedores](https://docs.streamlit.io/library/api-reference/layout)
