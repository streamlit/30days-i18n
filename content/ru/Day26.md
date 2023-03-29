# День 26

# **Как использовать API при создании приложения Bored API**

Приложение Bored API предлагает интересные занятия, когда вам скучно!

Технически оно также демонстрирует использование API в приложении Streamlit.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## **Код**

Как реализовать приложение Bored-API:

```python
import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st` и библиотеку `requests` следующим образом:
```python
import streamlit as st
import requests
```

Название приложения показывается через `st.title`:
```python
st.title('🏀 Bored API app')
```

Затем мы примем пользовательский ввод для **типа активности** с помощью команды `st.selectbox`:
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

Выбранное действие, упомянутое выше, затем добавляется к URL-адресу через f-string, которое затем используется для получения результирующих данных JSON:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

Здесь мы будем показывать информацию о приложении и о данных JSON с помощью команды `st.expander` .

```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

Затем мы покажем предлагаемое действие следующим образом:
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

Наконец, мы также покажем сопутствующую информацию о предлагаемом мероприятии, такую как `Number of Participants`, `Type of Activity`, и `Price`.

```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## **Дальнейшее чтение**

- [Bored API](http://www.boredapi.com/)
