# st.progress

`st.progress` 显示一个随着循环进度更新的进度条。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## 代码

以下展示了如何使用 `st.progress`：

```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`，并且导入要用到的 `time` 库：

```python
import streamlit as st
import time
```

接下来为应用创建标题文字：

```python
st.title('st.progress')
```

用 `st.expander` 创建一个 **About box**，在其中用 `st.write`显示描述信息：

```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

最后，我们定义一个进度条，并且以 0 为初值将其实例化。然后一个 `for` 循环将从 `0` 遍历至 `100`。在每个循环中，我们用 `time.sleep(0.05)` 来让应用等待 `0.05` 秒再令 `my_bar` 进度条数值加 `1`，这样能够以图像的形式显示出进度条随每个循环增长。

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 延伸阅读

- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
