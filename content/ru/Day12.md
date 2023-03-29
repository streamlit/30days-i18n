# День 12

# **st.checkbox**

`st.checkbox` отображает виджет «флажок».

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## **Код**

Вот как использовать `st.checkbox`:

```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:

```python
st.header('st.checkbox')
```

Далее мы собираемся задать вопрос через `st.write`:
```python
st.write ('What would you like to order?')
```

Затем мы собираемся предоставить некоторые пункты меню, чтобы их отметить:

```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

Наконец, мы собираемся напечатать пользовательский текст в зависимости от того, какой флажок установлен:

```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## **Дальнейшее чтение**

- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
