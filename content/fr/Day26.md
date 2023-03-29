# Comment utiliser des APIs dans Streamlit (via l'app `Bored API`)

L'application [Bored API](http://www.boredapi.com/) vous suggère des choses amusantes à faire lorsque vous vous ennuyez ("bored" en anglais) !

Construire cette app aussi une façon ludique de comprendre comment utiliser des APIs au sein d'une app Streamlit.


## Application de démonstration

[![Application Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## Code
Voici comment implémenter l'application Bored-API :
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

## Explication ligne par ligne
La première chose à faire lors de la création d'une app Streamlit est d'importer la bibliothèque `streamlit` as `st`, comme suit :
```python
import streamlit as st
```

Pour le bon fonctionnement de cette app, nous avons aussi besoin d'obtenir des informations sur le Web. Nous pouvons *scraper* ces infos facilement via la bibliothèque `⁣requests`, que nous importons comme ceci :

```python
import requests
```


Le titre de l'app est affiché via `st.title` :
```python
st.title('🏀 Bored API app')
```

Ensuite, acceptons la saisie de l'utilisateur pour l'**activity type**, via la commande `st.selectbox` :
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

L'activité sélectionnée ci-dessus est ajoutée à l'URL via f-string, qui est ensuite utilisée pour récupérer les données JSON résultantes :

```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Affichons ensuite des informations sur l'app ainsi que les données JSON via la commande `st.expander`.
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

Imprimons une activité suggérée, par exemple :

```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

Enfin, affichons également les infos suivantes telles que le `Nombre de participants`, le `Type d'activité` et le `Prix`:

```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## Lectures complémentaires
- [Bored API](http://www.boredapi.com/)
