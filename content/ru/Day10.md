# День 10

# **st.selectbox**

`st.selectbox` позволяет отображать выбранный виджет.

## **Что мы строим?**

Простое приложение, которое спрашивает пользователя, какой у него любимый цвет.

Процесс приложения:

1. Пользователь выбирает цвет
2. Приложение распечатывает выбранный цвет

## **Демонстрационное приложение**

Развернутое приложение Streamlit должно выглядеть примерно так, как показано по ссылке ниже:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## **Код**

Вот код для реализации вышеупомянутого приложения:

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:
```python
st.header('st.selectbox')
```

Далее мы создадим переменную с именем `option`, которая будет принимать пользовательский ввод в виде виджета **выбора** ввода с помощью команды `st.selectbox()`.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```

Как видно из кода выше, команда `st.selectbox()` принимает 2 входных аргумента:

1. Текст над виджетом выбора, например `'What is your favorite color?'`
2. Возможные значения для выбора `('Blue', 'Red', 'Green')`

Наконец, мы распечатаем выбранный цвет следующим образом:

```python
st.write('Your favorite color is ', option)
```

## **Следующие шаги**

Теперь, когда вы создали приложение Streamlit локально, пришло время развернуть его в [Streamlit Community Cloud](https://streamlit.io/cloud).

## **Использованная литература**

Подробнее о [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
