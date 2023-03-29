# День 19

# **Как оформить приложение Streamlit**

На этом уроке мы будем использовать следующие команды для макета нашего приложения Streamlit:

- `st.set_page_config(layout="wide")` – отображает содержимое приложения в расширенном режиме (в противном случае по умолчанию содержимое заключено в поле фиксированной ширины).
- `st.sidebar` – размещает виджеты или текст/изображения на боковой панели.
- `st.expander` – размещает дисплеи с текстом/изображением внутри складной коробки-контейнера.
- `st.columns` – создает табличное пространство (или столбец), внутри которого может быть размещено содержание.

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## **Код**

Как настроить макет вашего приложения Streamlit:

```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Мы начнем с определения макета страницы, который будет отображаться в режиме `wide`, который позволяет содержимому страницы расширяться до ширины браузера.

```python
st.set_page_config(layout="wide")
```

Далее мы дадим приложению Streamlit название.

```python
st.title('How to layout your Streamlit app')
```

Раскрывающееся поле под названием `About this app` находится под заголовком приложения. После расширения, внутри мы увидим дополнительные детали.

```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Виджеты ввода для приема пользовательского ввода размещаются на боковой панели, как указано с помощью команды `st.sidebar` перед командами Streamlit `text_input` и `selectbox`. Входные значения, введенные или выбранные пользователем, назначаются и сохраняются в переменных `user_name`, `user_emoji`, и `user_food`.

```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Наконец, мы создадим 3 столбца с помощью команды `st.columns`, которая соответствует `col1`, `col2`, и `col3`. Затем мы назначаем содержимое каждому столбцу, создавая отдельные блоки кода, начиная с оператора `with`. Под этим мы создаем условные операторы, которые отображают 1 из 2 альтернативных текстов в зависимости от того, предоставил ли пользователь свои входные данные (указанные на боковой панели) или нет. По умолчанию на странице отображается текст под оператором `else`. После ввода данных соответствующая информация которую пользователь предоставляет приложению отображается под текстом заголовка `Output`.

```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

Также стоит отметить, что строки `f` использовались для объединения предварительно подготовленного текста с предоставленными пользователем значениями.

## **Дальнейшее чтение**

- [Макеты и контейнеры](https://docs.streamlit.io/library)
