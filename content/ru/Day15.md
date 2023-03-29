# День 15

# **st.latex**

`st.latex` отображает математические выражения в формате LaTeX.

## **Что мы строим?**

Простое приложение, которое отображает математическое уравнение с использованием синтаксиса LaTeX с помощью команды `st.latex`.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## **Код**

Вот как использовать `st.latex`:

```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:
```python
st.header('st.latex')
```

Затем мы отображаем математическое уравнение через `st.latex`:

```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## **Использованная литература**

– Узнайте больше о [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) в документации по API Streamlit.
