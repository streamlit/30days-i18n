# День 21

# **st.progress**

`st.progress` отображает индикатор выполнения, который графически обновляется по мере выполнения итерации.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## **Код**

Как использовать `st.progress`:

```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st` вместе с библиотекой `time` следующим образом:

```python
import streamlit as st
import time
```

Далее мы создаем текст заголовка для приложения:

```python
st.title('st.progress')
```

Поле **О программе** создается с помощью `st.expander`, а описание отображается с помощью `st.write`:

```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

Наконец, мы определяем индикатор выполнения и создаем его экземпляр с начальным значением `0`. Затем цикл for будет повторяться от `0` до `100`. В каждой итерации мы используем `time.sleep(0.05)`, чтобы позволить приложению ждать `0,05`, прежде чем добавить значение `1` в индикатор выполнения `my_bar`, при этом графическое отображение полосы увеличивается с каждой итерацией.

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## **Дальнейшее чтение**

- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
