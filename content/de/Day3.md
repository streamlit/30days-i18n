# st.button

`st.button` erlaubt es dir, eine interaktive Schaltfläche anzuzeigen.

## Was bauen wir?

Eine einfache App, welche abhängig davon, ob auf die Schaltfläche geklickt wurde, alternative Nachrichten anzeigt.

Fluss der App:

1. Standardmäßig zeig die App `Goodbye` an
2. Wenn die Schaltfläche gedrückt wurde, zeigt die App die alternative Nachricht `Why hello there` an

## Demo App

Die veröffentlichte Streamlit App sollte so ähnlich aussehen wie diejenige hinter folgendem Link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Code

Hier ist der Code um die oben erwähnte App zu erstellen:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Zeilen-für-Zeilen Erklärung 

Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` zu importieren:

```python
import streamlit as st
```

This is followed by creating a header text for the app:

```python
st.header('st.button')
```

Next, we will use conditional statements `if` and `else` for printing alternative messages.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

Wie wir an der obigen Codebox sehen können, akzeptiert der `st.button()` Befehl das `label` Argument `Say hello`, welches als Text des Knopfes angezeigt wird.

Der `st.write` Befehl wird dazu benutzt, entweder `Why hello there` oder `Goodbye` als Textnachrichten anzuzeigen, je nachdem, ob der Knopf gedrückt wurde. Die Implementierung sieht folgendermaßen aus:

```python
st.write('Why hello there')
```

and

```python
st.write('Goodbye')
```

Es ist wichtig zu verstehen, dass die obigen `st.write` Ausdrücke innerhalb der `if` und `else` Bedingungen platziert sind. Damit wird die oben genannte alternative Anzeige der Nachrichten erreicht.

## Nächste Schritte

Nun da wir die Streamlit App lokal erstellt haben, ist es an der Zeit, sie auf [Streamlit Community Cloud](https://streamlit.io/cloud) zu veröffentlichen. Das wird in einer der nächsten Herausforderungen näher erläutert.

Wir zeigen den kompletten Code direkt hier auf der Website (wie in der Codebox oben dargestellt), weil es deine erste Woche ist.
Für die nächsten Herausforderungen empfehlen wir, dass du zuerst versuchst die Streamlit Apps selbst zu implementieren.

Nicht verzweifeln, falls du mal nicht weiterkommen solltest. Du kannst jederzeit einen Blick auf die Lösung werfen.

## Referenzen

Lies mehr über [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) in der Streamlit API Dokumentation.
