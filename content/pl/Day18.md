# Polecenie st.file_uploader

Polecenie `st.file_uploader` wyświetla widżet do przesyłania plików [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

Domyślnie, przesyłane pliki nie mogą być większe niż 200MB. Możesz to skonfigurować za pomocą opcji o nazwie server.maxUploadSize. Po więcej informacji na temat opcji, zajrzyj na [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## Kod
Oto jak używać polecenia `st.file_uploader`:
```python
import streamlit as st
import pandas as pd

st.title('Polecenie st.file_uploader')

st.subheader('Prześlij plik CSV')
uploaded_file = st.file_uploader("Wybierz plik z dysku")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('Ramka danych')
  st.write(df)
  st.subheader('Podstawowe informacje o zawartości pliku')
  st.write(df.describe())
else:
  st.info('☝️ Prześlij plik CSV')
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
import pandas as pd
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Polecenie st.file_uploader')
```

Potem skorzystamy z polecenia `st.file_uploader` aby wyświetlić widżet do przesyłania plików wskazanych przez użytkownika:
```python
st.subheader('Prześlij plik CSV')
uploaded_file = st.file_uploader(("Wybierz plik z dysku")
```

Na koniec napiszemy wyrażenie warunkowe, aby na początku wyświetlić wiadomość powitalną, zachęcającą użytkowników do przesłania pliku (implementacja znajduje się poniżej klauzuli `else`). Po przesłaniu pliku aktywuje się blok poniżej wyrażenia `if` i przesłany plik CSV zostanie odczytany przez bibliotekę `pandas` i wyświetlony za pomocą komendy `st.write`.

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

## Zobacz też
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Opcje konfiguracji](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
