# st.session_state

Wir definieren den Zugriff auf eine Streamlit-App in einer Browser-Tab als eine Session (Sitzung). Für jeden Browser-Tab, die sich mit dem Streamlit-Server verbindet, wird eine neue Sitzung erstellt. Streamlit führt dein Skript von vorne bis hinten aus jedes Mal, wenn du mit deiner App interagierst. Jede Wiederholung findet in einer leeren Umgebung statt: Es werden keine gemeinsamen Variablen zwischen den Durchläufen benutzt.

Der Session-State (Sitzungszustand) ist eine Möglichkeit, Variablen zwischen den Wiederholungen der einzelnen Benutzersitzungen gemeinsam zu nutzen. Neben der Möglichkeit, den Zustand zu speichern und beizubehalten, bietet Streamlit auch die Möglichkeit, den Zustand mithilfe von Callbacks zu manipulieren.

In diesem Tutorial werden wir die Verwendung von Session-State und Callbacks zeigen, während wir eine App zur Gewichtsumwandlung erstellen.

`st.session_state` ermöglicht die Implementierung des Sessionsstatus in einer Streamlit-App.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Code
So wird `st.session_state` verwendet:
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('st.session_state')
```

Als nächstes definieren wir Funktionen für die Gewichtsumrechnung von Pfund in Kilo und umgekehrt:
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

Hier verwenden wir `st.number_input`, um numerische Eingaben für die Gewichtswerte zu annehmen:
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

Die obigen 2 definierten Funktionen werden aufgerufen, sobald ein numerischer Wert in das Zahlenfeld eingegeben wird, das durch den Befehl `st.number_input` erstellt wurde. Es ist zu bemerken, dass die Option `on_change` die beiden Funktionen (`lbs_to_kg` und `kg_to_lbs`) festlegt. 

Kurz gesagt wird die Zahl durch diese Funktionen bei der Eingabe einer Zahl in das Feld `st.number_input` umgewandelt.

Zuletzt werden die Gewichtswerte in den Einheiten `kg` und `lbs` mit `st.write` ausgedruckt, die im Session-State als `st.session_state.kg` und `st.session_state.lbs` gespeichert sind:

```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## Literaturhinweise
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Add statefulness to apps](https://docs.streamlit.io/library/advanced-features/session-state)
