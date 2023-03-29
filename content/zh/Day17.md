# st.secrets

`st.secrets` 使你可以存储一些秘密信息，例如 API 密钥、数据库密码等其他验证信息。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## 代码

以下展示了如何使用 `st.secrets`：

```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

紧跟着的是为应用创建一个标题：

```python
st.title('st.secrets')
```

最后我们显示存储的秘密：

```python
st.write(st.secrets['message'])
```

需要注意的是，你可以通过如下截图所示方法，将秘密存入 Streamlit Community Cloud配置中。

如果在本地运行程序的话，你也可以将秘密存入 `.streamlit/secrets.toml` 文件内，但是切记避免在部署应用时将此文件上传至 GitHub 仓库。

## 延伸阅读

- [向你的 Streamlit 应用添加秘密](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [管理秘密](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
