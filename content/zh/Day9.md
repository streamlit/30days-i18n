# st.line_chart

`st.line_chart` 显示一个折线图。

这是围绕 `st.altair_chart` 实现的一个语法糖。最主要的区别是这个命令使用数据本身的列名与索引来确定图表的参数，因此简单易用，适合于很多“画个图看看”的场景，但较难调整样式和选项。

如果 `st.line_chart` 不能正确猜到数据的结构，请尝试使用 `st.altair_chart` 手动指定参数来生成你想要的图表。

## 我们要做什么？

我们今天要搭建一个简单的应用，显示一个折线图。

应用的流程：

1. 使用 `NumPy` 随机出一些数字，并用其创建一个 `Pandas` 数据框
2. 使用 `st.line_chart()` 命令创建并显示折线图

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## 代码

以下为 [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) 的用法：

```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
import pandas as pd
import numpy as np
```

然后紧跟着的是应用的标题文字：

```python
st.header('Line chart')
```

接着我们用随机生成的数字新建一个三列的数据框。

```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

最后，使用 `st.line_chart()` 创建一个折线图，以此前创建的数据框 `chart_data` 作为输入数据：

```python
st.line_chart(chart_data)
```

## 延伸阅读

阅读更多 [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) 所依赖的相关 Streamlit 命令：

- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
