# День 22

# **st.form**

`st.form` создает форму, которая объединяет элементы вместе с кнопкой "Отправить".

Как правило, всякий раз, когда пользователь взаимодействует с виджетом, приложение Streamlit перезапускается.

Форма — это контейнер, который визуально группирует вместе другие элементы и виджеты и содержит кнопку «Отправить». Здесь пользователь может взаимодействовать с одним или несколькими виджетами столько раз сколько ему нужно, без повторного запуска. Наконец, когда на форме нажата кнопка «Отправить», все значения виджетов внутри формы будут отправлены в Streamlit одним пакетом.

Чтобы добавить элементы в объект формы, вы можете использовать нотацию `with` (предпочтительно) или использовать ее как нотацию объекта, просто вызывая методы непосредственно в форме (сначала присваивая ее переменной, а затем применяя методы Streamlit). См. пример приложения.

Формы имеют несколько ограничений:

- Каждая форма должна содержать `st.form_submit_button`.
- `st.button` и `st.download_button` нельзя добавить в форму.
- Формы могут появляться в любом месте вашего приложения (боковая панель, столбцы, и т. д.), но их нельзя встраивать в другие формы.

Для получения дополнительной информации о формах ознакомьтесь с нашим [блогом](https://blog.streamlit.io/introduction-submit-button-and-forms/).

## **Демонстрационное приложение**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## **Код**

Как использовать `st.form`:

```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## **Построчное объяснение**

Самое первое, что нужно сделать при создании приложения Streamlit, это импортировать библиотеку `streamlit` как `st`, например:

```python
import streamlit as st
```

Затем следует создание текста заголовка для приложения:

```python
st.title('st.form')
```

### **Первый пример**

Начнем с первого примера—здесь мы применим команду `st.form` через нотацию `with`. Внутри формы мы начнем с написания подзаголовка `Order your coffee`, затем создадим несколько виджетов ввода (`st.selectbox`, `st.select_slider` и `st.checkbox`) для сбора информации о заказе кофе. Наконец, с помощью команды `st.form_submit_button` создается кнопка отправки, которая при нажатии отправляет ввод пользователя в виде единого пакета информации в приложение для обработки.

```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

Далее мы добавим логику того, что происходит после нажатия кнопки отправки. По умолчанию, всякий раз, когда загружается приложение Streamlit, будет выполняться оператор else, и мы видим сообщение `☝️ Разместите заказ!`. При нажатии на кнопку отправки все введенные пользователем данные через различные виджеты сохраняются в нескольких переменных (например, `coffee_bean_val`, `coffee_roast_val` и т. д.) и распечатываются с помощью команды `st.markdown` с помощью f-string.

```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```

### **Второй пример**

Давайте теперь перейдем ко второму примеру использования `st.form` в качестве обозначен я объекта. Здесь команда `st.form` назначается переменной `form`. Впоследствии к переменной `form` применяются различные команды Streamlit, такие как `slider` или `form_submit_button`.

```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## **Дальнейшее чтение**

- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Представляем кнопку «Отправить» и Формы](https://blog.streamlit.io/introduction-submit-button-and-forms/)
