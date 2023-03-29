# How to layout your Streamlit app

In this tutorial, we're going to use the following commands to layout our Streamlit app:
- `st.set_page_config(layout="wide")` - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.
- `st.sidebar` - Places the widgets or text/image displays in the sidebar.
- `st.expander` - Places text/image displays inside a collapsible container box.
- `st.columns` - Creates a tabular space (or column) within which contents can be placed inside.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Code
Here's how to customize the layout of your Streamlit app:
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

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

We'll start by first defining the page layout to be displayed in the `wide` mode, which allows the page content to expand to the browser's width.
```python
st.set_page_config(layout="wide")
```

Next, we'll give the Streamlit app a title.
```python
st.title('How to layout your Streamlit app')
```

An expandable box titled `About this app` is placed under the app title. Upon expansion, we'll see additional details inside.
```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Input widgets for accepting user input is placed in the sidebar as specified by using the `st.sidebar` command before the Streamlit commands `text_input` and `selectbox`. Input values entered or selected by the user are assigned and stored in the `user_name`, `user_emoji` and `user_food` variables.
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Finally, we'll create 3 columns using the `st.columns` command which corresponds to `col1`, `col2` and `col3`. Then, we assign contents to each of the column by creating individual code blocks starting with the `with` statement. Underneath this, we create conditional statements that display 1 of 2 alternative text depending on whether the user had provided their input data (specified in the sidebar) or not. By default, the page displays text under the `else` statement. Upon providing user input, the corresponding information that the user gives to the app is displayed under the `Output` header text.
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
It is also worthy to note that `f` strings were used to combine pre-canned text together with the user provided values. 

## Further reading
- [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
