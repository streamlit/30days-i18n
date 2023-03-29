# st.checkbox

`st.checkbox` 显示一个勾选组件。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## 代码

以下展示了如何使用 `st.checkbox`：

```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.checkbox')
```

接下来我们用 `st.write` 显示一个问题（“您想要点什么”）：

```python
st.write ('What would you like to order?')
```

然后我们提供几个菜单选项可供勾选：

```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

最后我们根据用户的勾选来输出不同的文字：

```python
if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## 延伸阅读

- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
