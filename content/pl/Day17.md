# Obiekt st.secrets

Obiekt `st.secrets` umożliwia przechowywanie poufnych informacji, takich jak klucze API, hasła do baz danych czy inne dane uwierzytelniające.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Kod
Oto jak korzystać z `st.secrets`:
```python
import streamlit as st

st.title('Obiekt st.secrets')

st.write(st.secrets['message'])
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Obiekt st.secrets')
```

Na koniec wyświetlamy zapisany sekret:
```python
st.write(st.secrets['message'])
```

Należy zauważyć, że sekrety mogą być przechowywane w Społecznościowej Chmurze Streamlit, jak pokazano na zrzutach ekranu poniżej.

Kiedy pracujemy lokalnie, sekrety mogą być przechowywane w pliku `.streamlit/secrets.toml`, ale upewnij się, aby nie dodać ich do repozytorium ani nie przesłać do serwisu GitHub podczas wdrażania aplikacji.

## Zobacz też
- [Dodwanie sekretów do Twojej aplikacji](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Zarządzanie sekretami](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
