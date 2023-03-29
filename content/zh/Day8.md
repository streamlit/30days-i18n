# st.slider

`st.slider` 能够显示一个滑条输入组件。

支持一下几种数据类型：int、float、date、time 和 datetime。

## 我们要做什么？

我们今天要搭建一个简单的应用，来展示如何使用滑条组件接收各类来自用户的输入。

应用的流程：

1. 用户通过调整滑条来选择数值
2. 将用户所选数值显示出来

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)

## 代码

以下为 `st.slider` 的用法：

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# 样例 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 样例 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 样例 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
from datetime import time, datetime
```

然后紧跟着的是应用的标题文字：

```python
st.header('st.slider')
```

**样例 1**

基础滑条：

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

如你所见，`st.slider()` 命令被用作收集用户输入的年龄信息。

第一个参数为 **滑条** 组件上方的标题文字，此处为询问用户年龄：`'How old are you?'`。

接下来三个整数 `0, 130, 25` 分别代表最小值、最大值和默认数值。

**样例 2**

范围滑条：

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

范围滑条允许同时输入一对下界与上界数值。

第一个参数为 **范围滑条** 组件上方的标题文字，此处为询问数字范围：`'Select a range of values'`。

接下来三个参数 `0.0, 100.0, (25.0, 75.0)` 分别代表了最小值、最大值和默认的一对下界与上界数值 (25.0, 75.0) 。

**样例 3**

时间范围滑条：

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

时间范围滑条允许同时输入一对下界与上界时间。

第一个参数为 **时间范围滑条** 组件上方的标题文字，此处为询问预约时段：`'Schedule your appointment:'`。

这里下界与上界时间的默认值分别被设为 11:30 和 12:45。

**样例 4**

日期时间滑条：

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

日期时间滑条允许输入一个日期时间。

第一个参数为 **日期时间滑条** 组件上方的标题文字，此处为询问开始时间：`'When do you start?'`。

这里日期时间的默认值通过 `value` 参数被设为 2020 年 1 月 1 日 9:30。

## 延伸阅读

你可以探索与此相关的组件：

- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
