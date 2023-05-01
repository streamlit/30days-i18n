# Streamlit 组件s

Streamlit 组件s 是第三方的 Python 模块，对 Streamlit 进行拓展 [[1](https://docs.streamlit.io/library/components)].

## 有哪些可用的 Streamlit 组件s？

好几十个精选 Streamlit 组件s 罗列在 Streamlit 的网站上 [[2](https://streamlit.io/components)].

Fanilo（一位 Streamlit 创作者）在 wiki 帖子中组织了一个很棒的 Streamlit 组件s 列表 [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]。截至 2022 年 4 月，其列出了约 85 个 Streamlit 组件s 。

## 如何使用？

Streamlit 组件s 只需要通过 pip 安装即可使用。

在这篇教程中，我们将教会你如何使用 `streamlit_pandas_profiling` 组件 [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### 安装组件

```bash
pip install streamlit_pandas_profiling
```

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## 代码

以下是如何使用这个组件来构建 Streamlit 应用：

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`，以及导入其他要用到的库：

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

然后紧跟着的是应用的标题文字：

```python
st.header('`streamlit_pandas_profiling`')
```

接下来我们使用 `pandas` 中的 `read_csv` 命令载入 Penguins 数据集。

```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

最后，由 `profile_report()` 命令生成分析报告，并用 `st_profile_report` 显示出来：

```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## 制作你自己的组件

如果你对于制作自己的组件感兴趣，请查阅以下这些资源：

- [制作组件](https://docs.streamlit.io/library/components/create)
- [发布组件](https://docs.streamlit.io/library/components/publish)
- [组件 API](https://docs.streamlit.io/library/components/components-api)
- [有关组件的博客帖子](https://blog.streamlit.io/introducing-streamlit-components/)

如果你更愿意通过视频学习，我们的工程师 Tim Conkling 也做了一些超棒的教程：

- [如何构建一个 Streamlit 组件s | Part 1: 配置与架构](https://youtu.be/BuD3gILJW-Q)
- [如何构建一个 Streamlit 组件s | Part 2: 制作一个滑条组件](https://youtu.be/QjccJl_7Jco)

## 有关组件的延伸阅读

1. [Streamlit 组件s - API 文档](https://docs.streamlit.io/library/components)
2. [精选 Streamlit 组件s ](https://streamlit.io/components)
3. [Streamlit 组件s - 社区追踪](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
