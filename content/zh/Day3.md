# st.button

`st.button` 会显示一个按钮组件。

## 我们要做什么？

我们今天要搭建一个简单的应用，根据按钮是否按下的状态，显示不同的文字消息。

应用的流程：

1. 默认情况下输出 `Goodbye`
2. 一旦按下按钮，则会变为显示 `Why hello there`

## 示例应用

我们将要部署的 Streamlit 应用应该看起来和下面链接中的这个差不多：

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## 代码

以下是实现前述应用的代码：

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.button')
```

接下来，我们会使用条件分支语句 `if` 和 `else` 来显示不同的消息：

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

由这段代码可见， `st.button()` 语句接收了一个值为 `Say hello` 的 `label` 参数，会作为显示在按钮上的文字。

`st.write` 命令被用作显示文字消息，取决于按钮是否按下，显示的要么是 `Why hello there`，要么是 `Goodbye`，即如下两个语句:

```python
st.write('Why hello there')
```

和

```python
st.write('Goodbye')
```

需要注意的是，以上 `st.write` 语句是在 `if` 和 `else` 条件分支内的，才能达到前述显示不同消息的效果。

## 接下来做什么？

现在你已经在本地创建好了 Streamlit 应用，是时候将其部署到 [Streamlit Community Cloud](https://streamlit.io/cloud) 了，我们在接下来的挑战中很快就会介绍到。

因为这是你挑战的第一周，因此我们在网页中直接提供了完整的代码（正如前面的代码框所示）和解决方案（示例程序）。

在接下来的挑战中，我们更推荐你首先尝试靠自己搭建 Streamlit 应用。

如果你卡住了，不必担心，可以随时看一眼解决方案是如何实现的。

## 参考资料

有关 [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) 的说明详见 Streamlit API 文档。
