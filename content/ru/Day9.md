# День 9

# **st.line_chart**

`st.line_chart` отображает линейный график.

Это синтаксический сахар вокруг `st.altair_chart`. Основное отличие состоит в том, что эта команда использует собственный столбец данных и индексы для определения спецификации диаграммы. В результате его легче использовать для многих сценариев «просто постройте это», но при этом он менее настраиваемый.

Если `st.line_chart` не угадывает спецификацию данных, попробуйте указать желаемую диаграмму с помощью st.altair_chart.

## **Что мы строим?**

Простое приложение для отображения линейной диаграммы.

Процесс приложения:

1. Создайте DataFrame Pandas из чисел, случайно сгенерированных с помощью NumPy.
2. Создайте и отобразите линейный график с помощью команды `st.line_chart()`.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## **Код**

Вот как использовать [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):

```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотекуи`streamlit` как `st`, а также другие библиотеки, например:

```python
import streamlit as st
import pandas as pd
import numpy as np
```

Далее мы создаем текст заголовка для приложения:

```python
st.header('Line chart')
```

Затем мы создаем DataFrame из случайно сгенерированных чисел, который содержит три столбца.

```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Наконец, линейная диаграмма создается с помощью `st.line_chart()` с DataFrame, хранящимся в переменной `chart_data`, в качестве входных данных:

```python
st.line_chart(chart_data)
```

## **Дальнейшее чтение**

Узнайте больше о следующей соответствующей команде Streamlit, на основе которой [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) работает:

- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
