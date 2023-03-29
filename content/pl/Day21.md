# Polecenie st.progress

Polecenie `st.progress` wyświetla pasek postępu, który aktualizuje się w kolejnych iteracjach.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## Kod

Oto jak używać polecenia `st.progress`:
```python
import streamlit as st
import time

st.title('Polecenie st.progress')

with st.expander('O tej aplikacji'):
     st.write('Możesz teraz wyświetlić postęp obliczeń za pomocą polecenia `st.progress`.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przyda nam się również standardowa biblioteka do obsługi czasu:
```python
import streamlit as st
import time
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Polecenie st.progress')
```

Informacja **O tej aplikacji** jest stworzona za pomocą polecenia `st.expander` a opis jest wyświetlony przy użyciu polecenie `st.write`:
```python
with st.expander('O tej aplikacji'):
     st.write('Możesz teraz wyświetlić postęp obliczeń za pomocą polecenia `st.progress`.')
```

Na koniec definiujemy pasek postępu i inicjujemy go początkową wartością `0`. Następnie, w każdym obiegu pętli używamy wyrażenia `time.sleep(0.05)` aby zaczekać `0.05` sekundy przed zwiększeniem postępu paska `my_bar` o 1, dzięki czemu zawartość paska zaktualizuje się. W sumie pętla wykona się 100 razy, doprowadzając postęp paska do końca.

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## Zobacz też
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
