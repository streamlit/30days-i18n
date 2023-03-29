# st.latex

`st.latex` 以 LaTeX 语法显示数学公式。

## 我们要做什么？

我们今天要搭建一个简单的应用，使用 `st.latex` 命令显示数学公式。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## 代码

以下展示了如何使用 `st.latex`：

```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.latex')
```

接下来我们使用 `st.latex` 来显示一个数学式子：

```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## 参考资料

- 阅读更多 Streamlit API 文档中有关 [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) 的内容
