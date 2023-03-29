# Polecenie st.multiselect

Polecenie `st.multiselect` służy do wyświetlenia widżetu wielokrotnego wyboru.

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej jak ta tutaj:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## Kod

Oto jak będziemy używać polecenia `st.multiselect`:

```python
import streamlit as st

st.header('Polecenie st.multiselect')

options = st.multiselect(
     'Jakie są Twoje ulubione kolory?',
     ['Zielony', 'Żółty', 'Czerwony', 'Niebieski'],
     ['Żółty', 'Czerwony'])

st.write('Wybrałeś:', options)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. 
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Polecenie st.multiselect')
```

Teraz stworzymy widżet za pomocą polecenia `st.multiselect`. Dzięki temu użytkownicy będą mogli wybrać swoje ulubione kolory.

```python
options = st.multiselect(
     'Jakie są Twoje ulubione kolory?',
     ['Zielony', 'Żółty', 'Czerwony', 'Niebieski'],
     ['Żółty', 'Czerwony'])
```

Na koniec wyświetlamy wybór dokonany przez użytkownika:
```python
st.write('Wybrałeś:', options)
```

## Zobacz też
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
