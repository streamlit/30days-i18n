# Day 17

# **st.secrets**

`st.secrets` позволяет хранить конфиденциальную информацию, такую как ключи API, пароли к базам данных или другие учетные данные.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## **Код**

Вот как использовать `st.secrets`:

```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:

```python
st.title('st.secrets')
```

Наконец, мы будем отображать сохраненные секреты:

```python
st.write(st.secrets['message'])
```
Следует отметить, что секреты могут храниться в облаке Streamlit, как показано на скриншотах ниже.

Если вы работаете локально, их можно хранить в `.streamlit/secrets.toml`, но не загружайте его в репозиторий GitHub при развертывании приложения.

## **Дальнейшее чтение**

- [Добавьте секреты в свои приложения Streamlit](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Управление секретами](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
