# День 25

# **st.session_state**

Мы определяем доступ к приложению Streamlit на вкладке браузера как session. Для каждой вкладки браузера, которая подключается к серверу Streamlit, создается новый session. Streamlit перезапускает ваш скрипт сверху вниз каждый раз, когда вы взаимодействуете с приложением. Каждый повтор происходит с чистого листа: никакие переменные не используются совместно.

Session State—это способ обмена переменными между повторами для каждого session. В дополнение к возможности сохранять state, Streamlit также предоставляет возможность манипулировать состоянием с помощью Callbacks.

В этом руководстве мы проиллюстрируем использование Session State и Callbacks при создании приложения для преобразования веса.

`st.session_state` позволяет реализовать Session State в приложении Streamlit.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## **Код**

Вот как использовать `st.session_state`:

```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:
```python
import streamlit as st
```

Во-первых, мы начнем с создания заголовка приложения:

```python
st.title('st.session_state')
```

Затем мы определяем пользовательские функции для преобразования веса из фунтов в кг и наоборот:

```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

Здесь мы используем `st.number_input`, чтобы принимать числовые значения значений веса:

```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

Вышеупомянутые 2 пользовательские функции будут вызываться, как только числовое значение будет введено в числовое поле, созданное с помощью команды `st.number_input`. Обратите внимание, как параметр `on_change` определяет две пользовательские функции lbs_to_kg и `kg_to_lbs`).

В двух словах, при вводе числа в поле `st.number_input` число преобразуется этими пользовательскими функциями.

Наконец, значения веса в единицах `kg` и `lbs`, сохраненные в Session State как `st.session_state.kg` и `st.session_state.lbs`, будут распечатаны с помощью `st.write`:

```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## **Дальнейшее чтение**

- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Добавить statefulness в приложения](https://docs.streamlit.io/library/advanced-features/session-state)
