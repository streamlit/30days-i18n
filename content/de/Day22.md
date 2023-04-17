# st.form

`st.form` erstellt ein Formular, das Elemente mit einer `Submit` Schaltfläche zusammenfasst.

Wenn ein Benutzer mit einem Widget interagiert, wird in der Regel die Streamlit-App neu gestartet.

Ein Formular ist ein Container, der andere Elemente und Widgets visuell zusammenfasst und eine `Submit` Schaltfläche enthält. Damit kann ein Benutzer beliebig oft mit mehreren Widgets interagieren, ohne dass ein erneuter Durchlauf erforderlich ist. Wenn der Submit-Button des Formulars gedrückt wird, werden alle Widgetwerte innerhalb des Formulars in einem einzigen Batch an Streamlit gesendet.

Um Elemente zu einem Formularobjekt hinzuzufügen, kann man die `with`-Notation verwenden (bevorzugt), oder Objektnotation, indem man einfach Methoden direkt auf dem Formular aufruft (wobei man zuerst das Formular der Variablen zuweist und anschließend Streamlit-Methoden darauf aufruft). Siehe in der Beispiel-App.

Für Formulare gibt es einige Beschränkungen:
- Jedes Formular muss `st.form_submit_button` enthalten.
- `st.button` und `st.download_button` können nicht zu einem Formular hinzugefügt werden.
- Formulare können überall in deiner App erscheinen (Sidebar, Spalten, etc.), aber sie können nicht in andere Formulare eingebettet werden.

Weitere Informationen über Formulare findet man in unserem [Blog Post](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Code
So wird `st.form` verwendet:
```python
import streamlit as st

st.title('st.form')

# Komplettes Beispiel für die Verwendung der 'with'-Notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    # Eingabe-Widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Jedes Formular muss eine 'Submit' Schaltfläche haben
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Kurzes Beispiel für die Verwendung der Objektnotation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('st.form')
```

### Erstes Beispiel
Beginnen wir mit dem ersten Beispiel, in dem wir den Befehl `st.form` mit der `with`-Notation verwenden. Innerhalb des Formulars fangen wir mit einer Zwischenüberschrift `Order your coffee` an und erstellen dann mehrere Eingabe-Widgets (`st.selectbox`, `st.select_slider` und `st.checkbox`), um Informationen über die Kaffeebestellung zu sammeln. Schließlich wird mit dem Befehl `st.form_submit_button` ein Submit-Button erstellt, der, wenn er angeklickt wird, alle Benutzereingaben als einen einzigen Batch von Informationen zur Verarbeitung an die App sendet.

```python
# Komplettes Beispiel für die Verwendung der 'with'-Notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Eingabe-Widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Jedes Formular muss eine 'Submit' Schaltfläche haben
    submitted = st.form_submit_button('Submit')
```

Als nächstes fügen wir die Logik hinzu, nachdem der Submit-Button angeklickt wurde. Standardmäßig wird beim Laden der Streamlit-App die `else`-Anweisung ausgeführt, und die Meldung `☝️ Place your order!` wird angezeigt. Nach dem Klick auf den Submit-Button werden alle Eingaben des Benutzers über die verschiedenen Widgets in verschiedenen Variablen gespeichert (z.B. `coffee_bean_val`, `coffee_roast_val`, etc.) und mit den Befehl `st.markdown` mithilfe von f-string ausgedruckt.

```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### Zweites Beispiel
Jetzt kommen wir zu dem zweiten Beispiel, wo man `st.form` mit Objektnotation benutzt. Hier wird der Befehl `st.form` der Variablen `form` zugewiesen. Anschließend werden verschiedene Streamlit-Befehle wie `slider` oder `form_submit_button` auf die Variable `form` verwendet.

```python
# Kurzes Beispiel für die Verwendung der Objektnotation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## Literaturhinweise
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Introducing Submit button and Forms](https://blog.streamlit.io/introducing-submit-button-and-forms/)
