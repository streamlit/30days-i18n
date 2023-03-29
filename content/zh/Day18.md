# st.file_uploader

`st.file_uploader` 显示一个上传文件的组件 [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)]。

默认情况下，上传的文件大小不能超过 200MB。你可以在通过 `server.maxUploadSize` 选项对其进行配置。更多有关如何配置选项的内容请见 [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## 代码

以下展示了如何使用 `st.file_uploader`：

```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`，以及导入其他依赖库：

```python
import streamlit as st
import pandas as pd
```

紧跟着的是为应用创建一个标题：

```python
st.title('st.file_uploader')
```

接下来我们将用 `st.file_uploader` 来显示一个文件上传的组件来接收用户的文件输入：

```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

最后，我们用条件分支语句来首先显示一个欢迎消息，提示用户上传文件（`else` 分支实现）。一旦有文件上传，则进入 `if` 分支并且使用 `pandas` 库读入 CSV 文件，然后使用 `st.write` 命令进行显示。

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## 延伸阅读

1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [设置配置选项](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
