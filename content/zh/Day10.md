# st.selectbox

`st.selectbox` 显示一个选择组件

## 我们要做什么？

我们今天要搭建一个简单的应用，询问用户最喜欢的颜色。

应用的流程：

1. 用户选择一个颜色
2. 显示用户选择的颜色

## 示例应用

我们将要部署的 Streamlit 应用应该看起来和下面链接中的这个差不多：

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## 代码

以下是实现上述应用的代码：

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.selectbox')
```

接下来，我们创建一个名为 `option` 的变量来存放来自 `st.selectbox()` 命令的用户**选择**输入。

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```

从上面的代码框可见，`st.selectbox()` 命令接收两个输入参数：

1. 组件上方的标题文字，也就是这里的 `'What is your favorite color?'`
2. 备选的数值，此处为 `('Blue', 'Red', 'Green')`

最后，我们用如下命令显示用户所选的颜色。

```python
st.write('Your favorite color is ', option)
```

## 接下来做什么？

现在你已经在本地创建好了 Streamlit 应用，是时候将其部署到 [Streamlit Community Cloud](https://streamlit.io/cloud) 了。

## 参考资料

更多有关 [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox) 的说明。
