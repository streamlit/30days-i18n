# st.write

`st.write` 能够在 Streamlit 应用中输出文字等内容。

除了能够输出文字，`st.write()` 命令还能够输出...

- 输出字符串，类似于 `st.markdown()`
- 输出 Python 的 `dict` 字典对象
- 输出 `pandas` DataFrame，将数据框显示为表格
- 输出用 `matplotlib`、`plotly`、`altair`、`graphviz`、`bokeh` 等库所作的图表
- 以及更多！（见 [API 文档中对 st.write 的描述](https://docs.streamlit.io/library/api-reference/write-magic/st.write)）

## 我们要做什么？

我们今天要搭建一个简单的应用，来展示使用 `st.write()` 命令输出各种文字、数字、数据框和图表。

## 示例应用

我们将要部署的 Streamlit 应用应该看起来和下面链接中的这个差不多：

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## 代码

以下是如何使用 `st.write` 的代码：

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1

st.write('Hello, *World!* :sunglasses:')

# 样例 2

st.write(1234)

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.write')
```

**样例 1**

`st.write` 的基本用法就是现实文字和使用 Markdown 语法的文本：

```python
st.write('Hello, *World!* :sunglasses:')
```

**样例 2**

前面提到，`st.write` 还能够输出其他数据类型，比如数字：

```python
st.write(1234)
```

**样例 3**

数据框也能够通过如下语句显示：

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**样例 4**

你也能传入多个参数，比如：

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**样例 5**

最后，你也可以显示各种图表，只需传入图表对象即可：

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## 接下来做什么？

现在你已经在本地创建好了 Streamlit 应用，是时候将其部署到 [Streamlit Community Cloud](https://streamlit.io/cloud) 了，我们在接下来的挑战中很快就会介绍到。

因为这是你挑战的第一周，因此我们在网页中直接提供了完整的代码（正如前面的代码框所示）和解决方案（示例程序）。

在接下来的挑战中，我们更推荐你首先尝试靠自己搭建 Streamlit 应用。

如果你卡住了，不必担心，可以随时看一眼解决方案是如何实现的。

## 延伸阅读

除了 [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write)，你还可以探索一下其他显示文本的方法：

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
