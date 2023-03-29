# st.session_state

我们将通过一个浏览器标签页访问 Streamlit 应用定义为一个会话（Session）。每个连接至 Streamlit 服务器的标签页都将创建一个会话。每当你与应用中组件交互时，Streamlit 将从上到下地重新运行整个应用。每次重新运行都将会清空历史：没有变量将被保留下来。

而会话状态（Session State）是一个在同一会话的不同次重新运行间共享变量的方法。除了能够存储和保留状态，Streamlit 还提供了使用回调函数更改状态的支持。

在此教程中，我们将构建一个重量换算应用，并描述会话状态以及回调函数的用法。

`st.session_state` 将允许我们在 Streamlit 应用中使用会话状态。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## 代码

以下展示了如何使用 `st.session_state`：

```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

首先我们创建一个应用的标题：

```python
st.title('st.session_state')
```

接下来，我们定义两个函数来实现对以磅和千克为单位的重量进行换算。

```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

这里我们使用了 `st.number_input` 来接收表示重量的数值输入：

```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

当用户在 `st.number_input` 生成的窗口中输入数字时，应用会调用以上两个函数。注意
`on_change` 参数分别指定了使用哪个回调函数（`lbs_to_kg` 与 `kg_to_lbs`）。

概括来说，当 `st.number_input` 接收到输入时，该数值会被回调函数换算为不同单位。

最后，以 `kg` 和 `lbs` 为单位的重量会以 `st.session_state.kg` 和 `st.session_state.lbs` 存储在会话状态中，并且能够用 `st.write` 将其显示出来：

```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 延伸阅读

- [会话状态](https://docs.streamlit.io/library/api-reference/session-state)
- [让你的应用“充满状态”](https://docs.streamlit.io/library/advanced-features/session-state)
