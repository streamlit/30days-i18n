# st.multiselect

`st.multiselect` 显示一个多选组件。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## 代码

以下展示了如何使用 `st.multiselect`：

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.multiselect')
```

接下来我们用 `st.multiselect` 组件来接收来自用户的一个或多个选择的颜色。

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

最后我们将所选颜色显示出来：

```python
st.write('You selected:', options)
```

## 延伸阅读

- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
