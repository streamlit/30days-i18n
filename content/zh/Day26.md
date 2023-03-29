# 通过构建 Bored API 应用学习如何使用 API

Bored API 应用可以在你无聊的时候建议你做些有意思的事！

技术上来说，这也演示了如何在 Streamlit 应用内使用 API。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## 代码

以下是如何实现上述 Bored API 应用：

```python
import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`，并且导入要用到的 `requests` 库：

```python
import streamlit as st
import requests
```

然后用 `st.title` 显示应用的标题：

```python
st.title('🏀 Bored API app')
```

接下来我们将通过 `st.selectbox` 命令接收用户输入的**活动类型**：

```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

上述选择的活动类型会通过 `f`-字符串追加到请求链接之后，然后被用于请求 JSON 数据：

```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

以下我们将通过 `st.expander` 命令显示应用的说明以及获取到的 JSON 数据：

```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

然后我们会像下面这样将建议的活动显示出来

```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

最后，我们也会显示所建议活动随附的信息，比如参与人数、活动类型与价格。

```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 延伸阅读

- [Bored API](http://www.boredapi.com/)
