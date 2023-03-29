# Polecenie st.experimental_get_query_params

Polecenie `st.experimental_get_query_params` umożliwia przechwycenie parametrów żądania bezpośrednio z adresu URL przeglądarki użytkownika.

## Przykładowa aplikacja

1. Poniższy link prowadzi do przykładowej aplikacji beż jakichkolwiek parametrów w adresie URL żądania (zwróć uwagę na komunikat o błędach):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/)

2. Poniższy link ładuje przykładową aplikację z parametrami żądania osadzonymi w adresie URL (tutaj nie ma już błędów): 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk)

## Kod

Oto jak używać polecenia `st.experimental_get_query_params`:
```python
import streamlit as st

st.title('Polecenie st.experimental_get_query_params')

with st.expander('O tej aplikacji'):
  st.write("`st.experimental_get_query_params` umożliwia przechwycenie parametrów żądania bezpośrednio z adresu URL przeglądarki użytkownika.")

# 1. Instrukcje
st.header('1. Instrukcje')
st.markdown('''
Dodaj na koniec obecnego adresu URL, który widzisz w pasku przeglądarki powyżej następującą treść:
`?name=Jack&surname=Beanstalk`
zaraz po głównej części `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
więc cały adres wygląda następująco: 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Zawartość st.experimental_get_query_params
st.header('2. Zawartość st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Pobieranie i wyświetlanie informacji z adresu URL
st.header('3. Pobieranie i wyświetlanie informacji z adresu URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Cześć **{firstname} {surname}**, jak się masz?')
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. 
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Polecenie st.experimental_get_query_params')
```

Dodajmy też rozszerzalną sekcję z informacjami o tej aplikacji:
```python
with st.expander('O tej aplikacji'):
  st.write("`st.experimental_get_query_params` umożliwia przechwycenie parametrów żądania bezpośrednio z adresu URL przeglądarki użytkownika.")
```

Następnie wytłumaczymy gościom naszej strony, w jaki sposób mogą przekazywać parametry do adresu URL:
```python
# 1. Instrukcje
st.header('1. Instrukcje')
st.markdown('''
Dodaj na koniec obecnego adresu URL, który widzisz w pasku przeglądarki powyżej następującą treść:
`?name=Jack&surname=Beanstalk`
zaraz po głównej części `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
więc cały adres wygląda następująco: 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
```

Potem wyświetlimy zawartość rezultatu działania polecenia `st.experimental_get_query_params`.

```python
# 2. Zawartość st.experimental_get_query_params
st.header('2. Zawartość st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

Na koniec przechwycimy i wyświetlimy wybrane informacje przekazane przez parametry zapytania w adresie URL:

```python
# 3. Pobieranie i wyświetlanie informacji z adresu URL
st.header('3. Pobieranie i wyświetlanie informacji z adresu URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Cześć **{firstname} {surname}**, jak się masz?')
```

## Zobacz też
- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)
