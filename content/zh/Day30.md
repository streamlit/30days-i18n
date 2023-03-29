# 创建 Streamlit 应用之艺术

今天是 _#30 天学 Streamlit_ 挑战的第 30 天。祝贺你已经走到这里了。

在这片教程中，我们将会用到这个学习挑战中新学的知识来创建一个解决真实世界问题的 Streamlit 应用。

## 真实世界问题

作为一个内容创作者，能够访问到 YouTube 视频的缩略图将会是社会推广和内容创作的重要资源。

让我们想个办法解决这个问题并且搭建一个 Streamlit 应用。

## 解决方案

今天我们将搭建一个 `yt-img-app`，它将是一个能够从 YouTube 视频提取缩略图的 Streamlit 应用。

简单来说，我们想要这个 Streamlit 应用做的事可以分为三步：

1. 接收用户输入的 YouTube 链接
2. 对链接进行文本处理，提取出 YouTube 视频独特的标识 ID
3. 用这个 YouTube 视频的 ID 作为一个自定义函数的输入，获取然后显示 YouTube 视频的缩略图

## 简介

要是用这个 Streamlit 应用，只需要在文本输入框中复制粘贴进一个 YouTube 链接即可。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## 代码

以下展示了如何搭建这个 `yt-img-app` Streamlit 应用：

```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
```

接下来我们显示应用的标题以及紧随其后的副标题：

```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```

来都来了，再加个“有关信息”拓展框也不是不行。

```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
```

以下我们创建一个用于让用户选择图像质量的选择框。

```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

显示一个文本输入框来接收用户输入的需要获取缩略图的 YouTube 视频链接。

```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

定义一个函数来处理输入的链接。

```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

最后我们用流程控制来决定是要提示用户输入链接（见 `else` 语句部分）还是要显示 YouTube 缩略图（见 `if` 语句部分）。

```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## 总结

总的来说，我们已经见识到了如何创建一个 Streamlit 应用，通常首先是明确和确定需求问题。然后我们设计一个解决方案将问题拆解为细粒度的步骤，然后我们在 Streamlit 应用中逐步实现。

此时我们同样需要决定用户需要输入的数据或者信息、处理用户输入的方式方法，才能产出满意的结果。

希望你能从本教程中有所收获，祝你 Streamlit 用得开心！
