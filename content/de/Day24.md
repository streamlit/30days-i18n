# st.cache

`st.cache` ermöglicht es dir, die Leistung deiner Streamlit-App zu optimieren.

Streamlit bietet einen Caching-Mechanismus, der es deiner App ermöglicht, beim Laden von Daten aus dem Web, bei der Bearbeitung großer Datensätze oder bei rechenintensiven Anwendungen performant zu bleiben. Dies wird mit dem Dekorator `@st.cache` erreicht.

Wenn du eine Funktion mit dem @st.cache-Dekorator markieren, wird es mit Streamlit mitgeteilt, dass es bei jedem Aufruf der Funktion einige Dinge überprüfen muss:

1. Die Eingabeparameter, mit denen die Funktion aufgerufen wurde
2. Der Wert einer externen Variable, die in der Funktion verwendet wird
3. Der Funktionsrumpf
4. Jeder Funktionsrumpf, der innerhalb der gecachten Funktion verwendet wird

Wenn Streamlit diese vier Komponenten zum ersten Mal mit genau diesen Werten und in genau dieser Kombination und Reihenfolge gesehen hat, führt es die Funktion aus und speichert das Ergebnis in einem lokalen Cache. Wenn sich dann beim nächsten Aufruf der gecachten Funktion keine dieser Komponenten geändert hat, überspringt Streamlit die Ausführung der Funktion ganz und gibt stattdessen die zuvor im Cache gespeicherte Ausgabe zurück.

Streamlit verfolgt die Änderungen in den Komponenten durch Hashing. Stell dir den Cache als einen In-Memory Key-Value-Store vor, bei dem der Schlüssel ein Hash aller oben genannten Komponenten und der Wert das Ausgabeobjekt ist, das als Referenz übergeben wird.

Schließlich unterstützt `@st.cache` Argumente, um das Verhalten des Caches zu konfigurieren. Weitere Informationen dazu findet man in unserer API-Referenz.

## Wie wird es verwendet?

Man kann einfach den Dekorator `st.cache` in die vorangehende Zeile einer Funktion einfügen, die du in deiner Streamlit-App definierst. Siehe das Beispiel unten.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Code
So wird `st.cache` verwendet:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('Streamlit Cache')
```

Als nächstes werden wir 2 Funktionen zur Erzeugung eines großen DataFrame definieren, wobei die erste den Dekorator `st.cache` verwendet und die zweite nicht:
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Zuletzt führen wir die benutzerdefinierte Funktion aus, wobei wir auch die Laufzeit mit dem Befehl `time()` messen.

```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Es ist zu bemerken, dass der erste Durchlauf in etwa die gleiche Laufzeit ergibt. Lade die App neu und beobachte, wie sich die Laufzeit bei Verwendung des Dekorators "st.cache" ändert. Konntest du einen Geschwindigkeitszuwachs feststellen?

## Literaturhinweise
- [`st.cache` API Documentation](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Optimize performance with `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Experimental cache primitives](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
