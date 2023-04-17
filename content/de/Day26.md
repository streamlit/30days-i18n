# How to use API by building the Bored API app

Die Bored API-App schlägt dir lustige Dinge vor, wenn dir langweilig ist!

Eigentlich demonstriert es auch die Verwendung von APIs innerhalb einer Streamlit-App.
## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## Code
So wird eine Bored-API App erstellt:
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

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
import requests
```

Der Titel der App wird mit `st.title` angezeigt:
```python
st.title('🏀 Bored API app')
```

Als nächstes wird Benutzereingaben zur **activity type** mithilfe des Befehls `st.selectbox` angenommen:
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

Die oben genannte ausgewählte Aktivität wird dann mit einem f-String an die URL angehängt, die dann zum Abrufen der resultierenden JSON-Daten verwendet wird:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Hier werden wir Informationen über die App und die JSON-Daten mit dem Befehl `st.expander` anzeigen:
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

Wir werden dann eine vorgeschlagene Aktivität anzeigen:
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

Zuletzt zeigen wir auch die begleitenden Informationen zu der vorgeschlagenen Aktivität an, wie z.B. die Anzahl der Teilnehmer, die Art der Aktivität und den Preis.
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## Literaturhinweise
- [Bored API](http://www.boredapi.com/)
