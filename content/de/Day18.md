# st.file_uploader

`st.file_uploader` zeigt ein Datei-Hochlade- (bzw. Uploader-) Widget an [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

Standardmäßig sind die hochgeladenen Dateien auf 200 MB begrenzt. Man kann dies mit der Konfigurationsoption server.maxUploadSize konfigurieren. Weitere Informationen zum Festlegen von Konfigurationsoptionen findet man unter [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Code
So wird `st.file_uploader` verwendet:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
import pandas as pd
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('st.file_uploader')
```

Als nächstes, verwenden wir `st.file_uploader`, um ein Widget für die Annahme von Benutzereingaben anzuzeigen:
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

Zuletzt definieren wir bedingte Anweisungen. Beim ersten Durchgang wird die `else`-Bedinging aktiviert und eine Willkommensnachricht angezeigt, die den Benutzer zum Hochladen seiner Datei auffordert. Nach dem Hochladen der Datei werden die `if`-Anweisungen aktiviert und die CSV-Datei wird von der `pandas` Bibliothek gelesen und mit dem Befehl `st.write` angezeigt.

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Literaturhinweise
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Set configuration options](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
