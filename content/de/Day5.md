# st.write

`st.write` erlaubt es, Texte und Argumente in der Streamlit App zu schreiben.

Zusätzlich zum Anzeigen von Text, können folgende Befehle / Objekte mittels `st.write()` angezeigt werden:

- Zeigt Strings an; funktioniert wie `st.markdown()`
- Zeigt ein Python `dict` Object an
- `pandas` DataFrame kann als Tabelle dargestellt werden
- Plots/Graphen/Bilder von `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
- Und mehr (siehe [st.write on API docs](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## Was bauen wir?

Eine einfache Streamlit App, welche die verschiedenen Wege demonstiert, in welchen der `st.write()` Befehl verwendet werden kann, um Text, Nummern, Pandas DataFrames und Graphen angezeigt werden können.

## Demo App

Die veröffentlichte Streamlit App sollte ungefähr so aussehen, die hier verlinkte:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Code

So wird `st.write` verwendet:

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Zeilen-für-Zeilen Erklärung

Die allerste Sache

Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` zu importieren:

```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:

```python
st.header('st.write')
```

**Beispiel 1**
Die standardmäßige Verwendung ist das Anzeigen von (Markdown) Text:

```python
st.write('Hello, *World!* :sunglasses:')
```

**Beispiel 2**
Wie oben beschrieben, kann der Befehl auch zum Anzeigen anderer Datenformate verwendet werden, wie zum Beispiel Nummern:

```python
st.write(1234)
```

**Beispiel 3**
DataFrames können ebenfalls angezeigt werden:

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**Beispiel 4**
Du kannst mehrere Argumente verwenden:

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**Beispiel 5**
Zum Schluss kannst du auch Grafiken anzeigen lassen, indem du sie einer Variable hinzufügst und dann `st.write` mit dieser Variable aufrufst:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Demo App

Die veröffentlichte Streamlit App sollte so ähnlich aussehen wie die hinter folgendem Link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Nächste Schritte

Nun da wir die Streamlit App lokal erstellt haben, ist es an der Zeit, sie auf [Streamlit Community Cloud](https://streamlit.io/cloud) zu veröffentlichen. Das wird in einer der nächsten Herausforderungen näher erläutert.

Wir zeigen den kompletten Code direkt hier auf der Website (wie in der Codebox oben dargestellt), weil es deine erste Woche ist.
Für die nächsten Herausforderungen empfehlen wir, dass du zuerst versuchst die Streamlit Apps selbst zu implementieren.

Nicht verzweifeln, falls du mal nicht weiterkommen solltest. Du kannst jederzeit einen Blick auf die Lösung werfen.

## Zum weiteren Lesen

Neben [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) kannst du noch andere Wege erkunden, Text anzeigen zu lassen:

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
