# Cómo usar la API creando la aplicación Bored API

¡La aplicación Bored API sugiere cosas divertidas para que hagas cuando estés aburrido!

Técnicamente, también demuestra el uso de API desde dentro de una aplicación Streamlit.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## Código
Aquí se explica cómo implementar la aplicación Bored-API:
```python
import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la librería `streamlit` como `st` y la también `requests` de la siguiente manera:
```python
import streamlit as st
import requests
```

El título de la aplicación se muestra a través de `st.title`:
```python
st.title('🏀 Bored API app')
```

A continuación, aceptaremos el **tipo de actividad** mediante el comando `st.selectbox`:
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

La actividad seleccionada mencionada anteriormente se agrega a la URL a través de f-string, que luego se usa para recuperar los datos JSON resultantes:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Aquí, mostraremos información sobre la aplicación y los datos JSON a través del comando `st.expander`.
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

Luego mostraremos una actividad sugerida así:
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

Finalmente, también mostraremos la información correspondiente a la actividad sugerida, como el `Número de participantes`, `Tipo de actividad` y `Precio`.
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## Otras lecturas
- [Bored API](http://www.boredapi.com/)
