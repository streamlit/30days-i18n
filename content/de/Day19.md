# Wie man deine Streamlit-App gestaltet

In diesem Tutorial werden wir die folgenden Befehle verwenden, um unsere Streamlit-App zu gestalten:
- `st.set_page_config(layout="wide")` - Zeigt den Inhalt der App im Wide-Modus an (sonst wird der Inhalt standardmäßig in einer Box mit festgelegter Breite umschlossen).
- `st.sidebar` - Platziert die Widgets oder Text-/Bildanzeigen in der Seitenleiste.
- `st.expander` - Platziert Text-/Bildanzeigen in einer ausklappbaren Containerbox.
- `st.columns` - Erstellt einen tabellarischen Bereich (oder Spalte), in dem Inhalte platziert werden können.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Code
So kannst du das Layout deiner Streamlit-App anpassen können:
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

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Zuerst legen wir das Seitenlayout fest, welches im `wide` Modus angezeigt wird. Dabei kann sich der Seiteninhalt auf die Breite des Browsers ausdehnen.
```python
st.set_page_config(layout="wide")
```

Als nächstes geben wir der Streamlit-App einen Titel.
```python
st.title('How to layout your Streamlit app')
```

Unter dem Titel der App befindet sich ein ausklappbares Feld mit der Überschrift `About this app`. Nach der Vergrößerung werden zusätzliche Details angezeigt.

```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Eingabe-Widgets zur Annahme von Benutzereingaben werden mit dem Befehl `st.sidebar` vor den Streamlit-Befehlen `text_input` und `selectbox` in der Seitenleiste platziert. Vom Benutzer eingegebene oder ausgewählte Eingabewerte werden den Variablen `user_name`, `user_emoji` und `user_food` zugewiesen und gespeichert.

```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Zuletzt erstellen wir mit dem Befehl `st.columns` drei Spalten, die `col1`, `col2` und `col3` entsprechen. Dann weisen wir jeder Spalte einen Inhalt zu, durch die Erstellung einzelne Codeblöcke, die mit der `with`-Anweisung beginnen. Darunter erstellen wir bedingte Anweisungen, die einen von 2 alternativen Texten anzeigen, je nachdem, ob der Benutzer seine Eingabedaten (in der Sidebar angegeben) eingegeben hat oder nicht. Standardmäßig wird der Text unter der `else`-Anweisung auf der Seite angezeigt. Nach der Benutzereingabe werden die entsprechenden Informationen, die der Benutzer an die App weitergibt, unter der Überschrift `Output` angezeigt.

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
Es ist auch erwähnenswert, dass f-Strings verwendet wurden, um vorgefertigten Text mit den vom Benutzer eingegebenen Werten zu kombinieren.


## Literaturhinweise
- [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
