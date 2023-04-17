# st.slider

`st.slider` ermöglicht es dir, eine interaktive Schieberegler bzw. Slider anzuzeigen.

Die folgenden Datentypen werden unterstützt: int, float, date, time, und datetime.

## Was bauen wir?

Eine einfache App, die verschiedene Möglichkeiten aufzeigt, wie man Benutzereingaben durch Einstellen des Sliders akzeptiert.

Ablauf der App:
1. Der Benutzer wählt einen Wert aus durch Einstellen des Sliders.
2. Die App zeigt den ausgewählten Wert an.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## Code
So wird st.slider verwendet:

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Beispiel 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Beispiel 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Beispiel 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Beispiel 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## Zeilenweise Erklärung 
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` zu importieren:
```python
import streamlit as st
from datetime import time, datetime
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('st.slider')
```

**Beispiel 1**

Slider:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

Wie wir sehen können, wird der Befehl "st.slider()` verwendet, um Eingaben über Alter zu sammeln.

Das erste Argument zeigt den Text `'How old are you?'` direkt über dem **slider** Widget an.

Die folgenden drei Zahlen `0, 130, 25` stehen jeweils für den Minimal-, Maximal- und Defaultwert.

**Beispiel 2**

Bereich-Slider:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

Mit dem Bereich-Slider kann man ein unterer und ein oberer Grenzwert eines Zahlenbereiches auswählen.

Das erste Argument zeigt den Text `'Select a range of values'` direkt über dem **range slider** Widget an.

Die erste zwei Argumente `0.0, 100.0` stehen für die Minimal- und Maximalwerte, während das letzte Tupel die Defaultwerte angibt, die als untere (`25.0`) und obere (`75.0`) Grenze verwendet werden sollen

**Beispiel 3**

Zeitbereich-Slider:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```
Mit dem Zeitbereich-Slider kann man ein unterer und ein oberer Grenzwert eines Zeitbereiches auswählen.

Das erste Argument zeigt den Text `'Schedule your appointment:'` direkt über dem **range time slider** Widget an.

Die Defaultwerte für die untere und obere Grenze des Zeitbereichs sind auf 11:30 bzw. 12:45 festgelegt.

**Beispiel 4**

Datum/Zeit (Datetime) Slider:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

Mit dem Datetime-Slider kann man ein Datum zusammen mit einer Uhrzeit auswählen.

Das erste Argument zeigt den Text `'When do you start?'` direkt über dem **datetime** Widget an.

Der Defaultwert wurde mit der Option `value` auf den 1. Januar 2020 um 9:30 Uhr festgelegt.

## Literaturhinweise
Man kann auch folgendes verwandtes Widget erkunden:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
