# st.line_chart

`st.line_chart` zeigt ein Liniendiagramm an.

Dies ist syntaktischer Zucker um `st.altair_chart`. Der wesentliche Unterschied besteht darin, dass dieser Befehl die eigenen Spalten und Indizes der Daten verwendet, um die Spezifikationen des Diagramms zu festlegen. Das Ergebnis ist, dass dieser Befehl für viele ["Just plot this"] Szenarien einfacher zu verwenden ist, während er weniger flexibel ist.

Wenn `st.line_chart` die Datenspezifikation nicht richtig errät, versuche mit `st.altair_chart` dein gewünschtes Diagramm zu spezifizieren.

## Was bauen wir?

Eine einfache App, wodurch ein Liniendiagramm angezeigt wird.

Ablauf der App:
1. Erstellen eines `Pandas` DataFrame mit `NumPy` generierten Zufallszahlen.
2. Erstellen und Anzeigen des Liniendiagramms mit dem Befehl `st.line_chart()`.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Code
So wird [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) verwendet:
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

Dies wird gefolgt von dem Erstellen einer Überschrift für die App:
```python
st.header('Line chart')
```

Dann erstellen wir einen DataFrame mit zufällig generierten Zahlen, der 3 Spalten enthält.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Zum Schluss wird ein Liniendiagramm mit `st.line_chart()` erstellt, wobei der in der Variablen `chart_data` gespeicherte DataFrame als Eingabedaten verwendet wird:
```python
st.line_chart(chart_data)
```

## Literaturhinweise
Lies mehr über den folgenden verwandten Streamlit Befehl, auf dem [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) basiert ist:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
