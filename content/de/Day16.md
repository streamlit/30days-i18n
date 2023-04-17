# Anpassen des Themas von Streamlit-Apps

We can customize the theme by adjusting parameters in `config.toml`, which is a configuration file stored in the same folder as the app in the `.streamlit` folder.
Wir können das Thema anpassen, indem wir die Parameter in der Konfigurationsdatei `config.toml` anpassen, die im gleichen Ordner wie die App im Ordner `.streamlit` gespeichert ist.

## Was bauen wir?

Eine einfache App, die das Ergebnis unserer Themenanpassung zeigt. Dies wird durch die Anpassung des HTML-HEX-Codes in der Datei [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) ermöglicht.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Code
Hier ist der Code für die [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) Datei:
```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Here's the code to the [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) file:
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('Theming with config.toml')
```

Als nächstes werden wir den Inhalt der Datei `.streamlit/config.toml` zeigen. Wir zeigen zuerst eine Anmerkung mit `st.write` an und dann den eigentlichen Code mit `st.code`:
```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

Zuletzt erstellen wir ein Slider-Widget in der Seitenleiste und zeigen die ausgewählte Zahl an:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Schauen wir uns auf die individuelle Farben, die wir in dieser App verwendet haben und die in der Datei `.streamlit/config.toml` angegeben sind:
- `primaryColor="#F39C12"` - Damit wird die Primärfarbe auf Orange eingestellt. Siehe die orangen Farben im Slider-Widget.
- `backgroundColor="#2E86C1"` - Damit wird die Hintergrundfarbe auf Blau eingestellt. Siehe, dass das Hauptpanel eine blaue Hintergrundfarbe hat.
- `secondaryBackgroundColor="#AED6F1"` - Damit wird die sekundäre Hintergrundfarbe auf Dunkelgrau eingestellt. Siehe die graue Hintergrundfarbe der Seitenleiste und die Hintergrundfarbe der Codebox im Hauptfenster.
- `textColor="#FFFFFF"` - Die Textfarbe wird auf weiß eingestellt.
- `font="monospace"` - Damit wird der Font auf eine Festbreitenschrift (`monospace`) eingestellt. 

## Literaturhinweise
- [Theming](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML Color Codes](https://htmlcolorcodes.com/) ist ein Hilfsmittel, um interessanter Farben zu auswählen.