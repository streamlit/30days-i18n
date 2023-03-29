# День 24

# **st.cache**

`st.cache` позволяет оптимизировать производительность вашего приложения Streamlit.

Streamlit предоставляет механизм кэширования, который позволяет вашему приложению оставаться производительным даже при загрузке данных из Интернета, манипулировании большими наборами данных или выполнении дорогостоящих вычислений. Это делается с помощью декоратора `@st.cache`.

Когда вы помечаете функцию декоратором `@st.cache`, он сообщает Streamlit что при каждом вызове функции необходимо проверить несколько вещей:

1. Входные параметры, с которыми вы вызывали функцию
2. Значение любой внешней переменной, используемой в функции
3. Тело функции
4. Тело любой функции, используемой внутри кэшированной функции.

Если Streamlit впервые видит эти четыре компонента с такими точными значениями, именно в такой комбинации и порядке, он запускает функцию и сохраняет результат в локальном кэше. Затем при следующем вызове кэшированной функции, если ни один из этих компонентов не изменился, Streamlit просто пропустит выполнение функции и вместо этого вернет результат, ранее сохраненный в кэше.

Streamlit отслеживает изменения в этих компонентах с помощью кеширования. Думайте о кеше как о хранилище ключей и значений в памяти, где ключ представляет собой кэш всего вышеперечисленного, а значение — это фактический выходной объект, переданный по ссылке.

Наконец, `@st.cache` поддерживает аргументы для настройки поведения кэша. Дополнительную информацию о них можно найти в нашем справочнике по API.

## **Как использовать?**

Вы можете просто добавить декоратор `st.cache` в предыдущую строку пользовательской функции, которую вы определяете в своем приложении Streamlit. См. пример ниже.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## **Код**

Как использовать `st.cache`:

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, а также других библиотек используемых в приложении, следующим образом:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

Затем следует создание текста заголовка для приложения:
```python
st.title('Streamlit Cache')
```

Далее мы определим две пользовательские функции для создания большого DataFrame, где первая использует декоратор `st.cache`, а вторая нет:

```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Наконец, мы запускаем пользовательскую функцию, а также измеряем время выполнения с помощью команды `time()`.

```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

Обратите внимание, что первый запуск может обеспечить примерно одинаковое время выполнения. Перезагрузите приложение и обратите внимание на изменение времени выполнения при использовании декоратора `st.cache`. Вы не заметили увеличения скорости?

## **Дальнейшее чтение**

- [`st.cache` Документация API](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Оптимизируйте производительность с помощью `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Экспериментальные примитивы кэша](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
