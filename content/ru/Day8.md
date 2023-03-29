# День 8

# **st.slider**

`st.slider` позволяет отображать виджет ввода слайдера.

Поддерживаются следующие типы данных: int, float, date, time, и datetime.

## **Что мы строим?**

Простое приложение, которое показывает различные способы принятия пользовательского ввода путем настройки виджета slider.

Процесс приложения:

1. Пользователь выбирает значение, настраивая виджет slider.
2. Приложение распечатывает выбранное значение.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)

## **Код**

Вот как использовать st.slider:

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
from datetime import time, datetime
```

Затем следует создание текста заголовка для приложения:

```python
st.header('st.slider')
```

**Пример 1**

Slider:


```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

Как вы видите, команда `st.slider()` используется для сбора информации о возрасте пользователей.

Первый входной аргумент отображает текст чуть выше **slider** виджета с вопросом `'How old are you?'`.

Следующие три целых числа `0, 130, 25` представляют минимальное значение, максимальное значение, и значение по умолчанию соответственно.

**Пример 2**

Range slider:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

Range slider позволяет выбрать пару значений нижней и верхней границы.

Первый входной аргумент отображает текст чуть выше **range slider** виджета с вопросом `'Select a range of values'`.

Следующие три аргумента `0,0, 100,0, (25,0, 75,0)` представляют минимальное и максимальное значения, а последний кортеж обозначает значения по умолчанию для использования в качестве выбранных нижних (25,0) и верхних (75,0) граничных значений.

**Пример 3**

Range time slider:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

Range time slider позволяет выбрать пару значений нижней и верхней границ даты и времени.

Первый входной аргумент отображает текст чуть выше **range time slider** виджета с запросом `'Schedule your appointment:`.

По умолчанию, значения для пар значений нижней и верхней границ даты и времени установлены на 11:30 и 12:45 соответственно.

**Пример 4**

Datetime slider:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

Datetime slider позволяет выбрать дату и время.

Первый входной аргумент отображает текст прямо над виджетом **datetime** ползунком с запросом `'When do you start?'`.

По умолчанию, значение для даты и времени было установлено с помощью параметра `value`: 1 января 2020 года, 9:30.

## **Дальнейшее чтение**

Вы также можете изучить следующий соответствующий виджет:

- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
