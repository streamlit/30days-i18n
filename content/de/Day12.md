# st.checkbox

`st.checkbox` zeigt ein Kontrollkästchen- bzw. Checkbox-Widget an.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Code
So wird `st.checkbox` verwendet:
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

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('st.checkbox')
```

Als nächstes werden wir eine Frage mit `st.write` stellen:
```python
st.write ('What would you like to order?')
```

Wir werden dann einige Menüpunkte zum Ankreuzen bereitstellen:
```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

Zuletzt werden wir einen bestimmten Text anzeigen, je nachdem, welches Kästchen angekreuzt wurde:
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## Literaturhinweise
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
