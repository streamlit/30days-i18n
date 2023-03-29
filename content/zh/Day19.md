# 如何布局你的 Streamlit 应用

在这篇教程中，我们将用以下几个命令来布局我们的 Streamlit 应用：

- `st.set_page_config(layout="wide")` - 将应用的内容以宽屏模式呈现（默认情况下以一固定宽度的列的形式呈现）
- `st.sidebar` - 将组件/文字/图片显示在侧边栏中
- `st.expander` - 将组件/文字/图片显示在一个可折叠的容器中
- `st.columns` - 创建表格布局（或列布局）来容纳内容

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## 代码

以下展示了如何自定义你的 Streamlit 应用布局：

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

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

我们首先令页面的显示模式变为宽屏模式，页面内容将占据浏览器的全部宽度进行显示。

```python
st.set_page_config(layout="wide")
```

接下来，我们为这个 Streamlit 应用设置一个标题。

```python
st.title('How to layout your Streamlit app')
```

在应用标题下方创建一个标题名为 `About this app` 的可折叠区域。在展开时，我们可以看到其其中包含的额外细节。

```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

通过在 `text_input` 和 `selectbox` 之前加上 `st.sidebar` 命令，我们将用于接收用户输入的组件放入侧边栏内。用户输入或选择的数值将被赋值并存储在 `user_name`、`user_emoji` 和 `user_food` 变量之中。

```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

最后，我们使用 `st.columns` 命令创建三列，分别名为 `col1`、`col2` 和 `col3`。然后我们使用独立的 `with` 语句将内容放入每列之中。其中我们创建了三个条件分支语句，根据用户是否在侧边栏中提供了输入来显示不同的文字。默认情况下显示的均为 `else` 语句下的内容。如果用户提供了对应的输入，则会显示在 `Output` 标题下方。

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

值得注意的是，这里我们用 `f`-字符串来将固定的信息与用户的输入数值相结合。

## 延伸阅读

- [布局与容器](https://docs.streamlit.io/library/api-reference/layout)
