# El arte de crear aplicaciones Streamlit

Hoy es el día 30 del desafío *#30DaysOfStreamlit*. Felicitaciones por llegar tan lejos en el desafío.

En este tutorial, vamos a poner nuestro nuevo conocimiento de Streamlit para resolver problemas del mundo real.

## Problema del mundo real

Como creador de contenido, tener acceso a las imágenes en miniatura de los videos de YouTube son recursos útiles para la promoción social y la creación de contenido.

Averigüemos cómo vamos a abordar este problema y crear una aplicación Streamlit.

## Solución

Hoy, vamos a crear `yt-img-app`, que es una aplicación Streamlit que puede extraer imágenes en miniatura de videos de YouTube.

En pocas palabras, estos son los 3 pasos simples que queremos que haga la aplicación Streamlit:

1. Aceptar una URL de YouTube como entrada de los usuarios
2. Realice el procesamiento de texto de la URL para extraer la identificación única del video de YouTube
3. Use el ID del video de YouTube como argumento para una función que recupera y muestra la imagen en miniatura

## Instrucciones

Para comenzar a usar la aplicación Streamlit, copie y pegue una URL de YouTube en el campo de texto.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## Código
Aquí se explica cómo construir la aplicación Streamlit `yt-img-app`:
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
  
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la biblioteca `streamlit` como `st` de la siguiente manera:
```python
import streamlit as st
```

A continuación, mostramos el título de la aplicación y el encabezado que lo acompaña:
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```
Mientras estamos en eso, también podríamos agregar un cuadro expandible.
```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
 
Here, we create selection box for accepting user input on the image quality to use.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

Se muestra un campo de texto para aceptar la URL del video de YouTube para luego extraer la imagen.
```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

Una función para realizar el procesamiento de texto de la URL.
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

Finalmente, usamos el control de flujo para determinar si mostrar un recordatorio para ingresar la URL (es decir, como en la declaración `else`) o mostrar la imagen en miniatura de YouTube (es decir, como en la declaración `if`).
```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## Resumen

En resumen, hemos visto que en la creación de cualquier aplicación Streamlit, normalmente comenzamos primero identificando y definiendo el problema. A continuación, ideamos una solución para abordar el problema dividiéndola en pasos granulares, que implementamos en la aplicación Streamlit.

Aquí, también tenemos que determinar qué datos o información necesitamos, el enfoque y el método a utilizar en el procesamiento de la información del usuario para obtener el resultado final deseado.

Espero que hayas disfrutado este tutorial, ¡Feliz Streamlit-ing!