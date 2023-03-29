# 自定义 Streamlit 应用的主题

我们可以通过调整 `config.toml` 中的选项来自定义应用的主题，这个配置文件应当被放在与应用并行的 `.streamlit` 文件夹内。

## 我们要做什么？

我们今天要搭建一个简单的应用来展示自定义的主题。主要通过自定义 [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) 中的 HTML 十六进制色彩码来完成

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## 代码

以下是 [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) 文件中的内容：

```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

以下是 [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) 配置文件中的内容：

```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

紧跟着的是为应用创建一个标题：

```python
st.title('Theming with config.toml')
```

接下来我们将显示 `.streamlit/config.toml` 的文件内容，首先用 `st.write` 显示一个说明，然后是用 `st.code` 显示真正的文件内容：

```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

最终，我们在侧边栏中创建一个滑条组件，并且显示其所选数值：

```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

来看看我们在 `.streamlit/config.toml` 文件中为这个应用定义的颜色：

- `primaryColor="#F39C12"` - 将主强调色设为橙色。即滑条组件所用的橙色。
- `backgroundColor="#2E86C1"` - 将背景色设为蓝色。即主页面背景的蓝色。
- `secondaryBackgroundColor="#AED6F1"` - 将副强调色设为深灰。即侧边栏的背景色与主页面中代码框的背景色。
- `textColor="#FFFFFF"` - 将文本颜色设为白色。
- `font="monospace"` - 将字体设为等宽字体。

## 延伸阅读

- [主题](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML 色彩码](https://htmlcolorcodes.com/) 是一个能够帮助选择目标颜色的工具。
