# Jak korzystać z API budując aplikację Bored API

Aplikacja Bored API sugeruje ciekawe rzeczy, które możesz zrobić, kiedy Ci się nudzi!


Z technicznego punktu widzenia, pokazuje również użycie API z poziomu aplikacji Streamlit.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## Kod

Oto jak zaimplementować aplikację Bored-API:

```python
import streamlit as st
import requests

st.title('🏀 Aplikacja Bored API')

st.sidebar.header('Wejście')
selected_type = st.sidebar.selectbox('Wybierz typ aktywności', ["edukacja", "rekreacja", "społeczność", "zrób to sam", "dobroczynność", "gotowanie", "relaks", "muzyka", "zabijanie czasu"])

activity_translations = {
   "edukacja": "education",
   "rekreacja": "recreational",
   "społeczność": "social",
   "zrób to sam": "diy",
   "dobroczynność": "charity",
   "gotowanie": "cooking",
   "relaks": "relaxation",
   "muzyka":  "music",
   "zabijanie czasu": "busywork"
}

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={activity_translations[selected_type]}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('O tej aplikacji'):
    st.write('Czujesz się znudzony? Aplikacja **Bored API** potrafi podpowiedzieć zajęcia, dzięki którym zwalczysz nudę. Ta aplikacja korzysta z Bored API.')
with c2:
  with st.expander('Dane w formacie JSON'):
    st.write(suggested_activity)
    
st.header('Sugerowane zajęcie')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Liczba uczestników', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Rodzaj aktywności', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Cena', value=suggested_activity['price'], delta='')
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. 
```python
import streamlit as st
import requests
```

Tytuł aplikacji jest wyświetlony przy użyciu polecenia `st.title`:
```python
st.title('🏀 Aplikacja Bored API')
```

Następne pobierzemy od użytkownika informację na temat **typu aktywności** za pomocą polecenia `st.selectbox`:

```python
st.sidebar.header('Wejście')
selected_type = st.sidebar.selectbox('Wybierz typ aktywności', ["edukacja", "rekreacja", "społeczność", "zrób to sam", "dobroczynność", "gotowanie", "relaks", "muzyka", "zabijanie czasu"])
```

Wybrana aktywność jest następnie tłumaczona na język angielski i dopisywana poprzez f-string do adresu URL, spod którego będziemy pobierać odpowiedź z zewnętrznego serwera z postaci danych w formacie JSON.


```python
activity_translations = {
   "edukacja": "education",
   "rekreacja": "recreational",
   "społeczność": "social",
   "zrób to sam": "diy",
   "dobroczynność": "charity",
   "gotowanie": "cooking",
   "relaks": "relaxation",
   "muzyka":  "music",
   "zabijanie czasu": "busywork"
}

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={activity_translations[selected_type]}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Tutaj wyświetlamy informacje o aplikacji oraz dane w formacie JSON używając polecenia `st.expander`

```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('O tej aplikacji'):
    st.write('Czujesz się znudzony? Aplikacja **Bored API** potrafi podpowiedzieć zajęcia, dzięki którym zwalczysz nudę. Ta aplikacja korzysta z Bored API.')
with c2:
  with st.expander('Dane w formacie JSON'):
    st.write(suggested_activity)
```

Następnie wyświetlamy sugerowaną aktywność:

```python
st.header('Sugerowane zajęcie')
st.info(suggested_activity['activity'])
```

Na koniec wyświetlamy dodatkowe informacje na temat sugerowanego zajęcia, takie jak liczba uczestników, rodzaj aktywności czy cena.

```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Liczba uczestników', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Rodzaj aktywności', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Cena', value=suggested_activity['price'], delta='')
```

## Zobacz też
- [Bored API](http://www.boredapi.com/)
