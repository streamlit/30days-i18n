# День 11

# **st.multiselect**

`st.multiselect` отображает виджет множественного выбора.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## **Код**

Вот как использовать `st.multiselect`:

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

Далее мы собираемся использовать виджет `st.multiselect`, чтобы принимать ввод, где пользователи смогут выбрать один или несколько цветов по своему выбору.

`options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])`

Наконец, мы выпишем выбранные цвета:
```python
st.write('You selected:', options)
```

## **Дальнейшее чтение**

- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
