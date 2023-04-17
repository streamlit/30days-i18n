# st.selectbox

`st.selectbox` ermöglicht die Anzeige eines Auswahl-Widgets.

## Was bauen wir?

Eine einfache App, die den Benutzer fragt, was seine Lieblingsfarbe ist.

Ablauf der App:
1. Der Benutzer wählt eine Farbe aus
2. Die App zeigt die ausgewählte Farbe an

## Demo App
Die eingesetze Streamlit App sollte wie die im folgenden Link aussehen:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## Code
Hier ist der Code zur Implementierung der oben genannten App:
```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('st.selectbox')
```

Als nächstes erstellen wir eine Variable namens `option`, die Benutzereingaben in Form eines **select** Eingabe Widgets über den Befehl `st.selectbox()` akzeptiert.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```
Wie aus der obigen Code-Box ersichtlich, akzeptiert der Befehl `st.selectbox()` 2 Argumente:
1. Der Text, der über dem Auswahl-Widget steht, d.h. `'What is your favorite color?'`
2. Die möglichen Werte zum Auswählen: `('Blue', 'Red', 'Green')`

Zuletzt zeigen wir die ausgewählte Farbe wie folgt an:
```python
st.write('Your favorite color is ', option)
```

## Nächste Schritte
Jetzt, da die Streamlit App lokal erstellt ist, können wir sie auf [Streamlit Community Cloud](https://streamlit.io/cloud) bereitstellen.

## Referenzen 
Mehr über [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
