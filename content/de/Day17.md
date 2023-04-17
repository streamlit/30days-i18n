# st.secrets

`st.secrets` ermöglicht es dir, vertrauliche Informationen wie API-Schlüssel, Datenbank-Passwörter oder andere Anmeldedaten zu speichern.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Code
So wird `st.secrets` verwendet:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Dies wird gefolgt von dem Erstellen eines Titels für die App:
```python
st.title('st.secrets')
```

Zuletzt zeigen wir die gespeicherten Geheimdaten an:
```python
st.write(st.secrets['message'])
```

Es ist zu beachten, dass Geheimdaten in der Streamlit Community Cloud gespeichert werden können, wie in den Screenshots unten gezeigt.

Wenn man lokal arbeitet, können Daten in `.streamlit/secrets.toml` gespeichert werden. Achte darauf, dass du diese Datei nicht in ein GitHub-Repo hochlädst, wenn die App bereitgestellt wird.

## Literaturhinweise
- [Add secrets to your Streamlit apps](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Secrets management](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
