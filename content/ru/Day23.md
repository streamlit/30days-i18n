# День 23

# **st.experimental_get_query_params**

`st.experimental_get_query_params` позволяет извлекать параметры запроса непосредственно из URL-адреса браузера пользователя.

## **Демонстрационное приложение**

1. Следующая ссылка загружает демонстрационное приложение без параметров запроса (обратите внимание на сообщение об ошибке):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/)

2. Следующая ссылка загружает демонстрационное приложение с параметрами запроса (здесь нет сообщения об ошибке):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk)

## **Код**

Как использовать `st.experimental_get_query_params`:

```python
import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:
```python
import streamlit as st
```

Далее мы дадим приложению название:
```python
st.title('st.experimental_get_query_params')
```

Давайте также добавим раскрывающийся список «О программе»:

```python
with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

Затем мы предоставим инструкции посетителям приложения о том, как они могут передавать параметры запроса прямо в URL-адрес:

```python
# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
```

Впоследствии мы покажем содержимое команды `st.experimental_get_query_params` .
```python
# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

Наконец, мы выберем и покажем выборочную информацию из параметра запроса URL:
```python
# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## **Дальнейшее чтение**

- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)
