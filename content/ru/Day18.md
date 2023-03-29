# День 18

# **st.file_uploader**

`st.file_uploader` отображает виджет загрузки файлов [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

По умолчанию загруженные файлы не могут превышать 200 МБ. Вы можете настроить это с помощью параметра конфигурации server.maxUploadSize. Для получения дополнительной информации о том, как установить параметры конфигурации, см. [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## **Код**

Вот как использовать `st.file_uploader`:

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

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st` и другие необходимые библиотеки, например:

```python
import streamlit as st
import pandas as pd
```

Затем следует создание текста заголовка для приложения:
```python
st.title('st.file_uploader')
```

Далее мы будем использовать `st.file_uploader`, чтобы отобразить виджет загрузки файлов для принятия файла, введенного пользователем:

```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

Наконец, мы определим условных операторов для первоначального отображения приветственного сообщения, предлагающего пользователям загрузить свой файл (как реализовано в условии `else` ). После загрузки файла операторы `if` активируются, и файл CSV считывается библиотекой `pandas` и отображается с помощью команды `st.write`.

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

## **Дальнейшее чтение**

1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Установить параметры конфигурации](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
