# st.file_uploader

`st.file_uploader` muestra un componente para subir archivos [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

De forma predeterminada, los archivos cargados están limitados a 200 MB. Puede configurar esto usando server.maxUploadSize. Para obtener más información sobre utilizar las opciones de configuración, consulte [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Código
Aquí se explica cómo usar `st.file_uploader`:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` y otras de la siguiente manera:
```python
import streamlit as st
import pandas as pd
```

A esto le sigue la creación de un título para la aplicación:
```python
st.title('st.file_uploader')
```

A continuación, usaremos `st.file_uploader` para mostrar un componente de carga de archivos:
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

Finalmente, definimos la condición para mostrar inicialmente un mensaje de bienvenida invitando a los usuarios a cargar su archivo (como se implementa en la condición `else`). Al cargar el archivo, la condición `if` se activa y la biblioteca `pandas` lee el archivo CSV y lo muestra a través del comando `st.write`.
```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Otras lecturas
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Establecer opciones de configuración](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
