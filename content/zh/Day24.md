# st.cache

`st.cache` 使得你可以优化 Streamlit 应用的性能。

Streamlit 提供了一个缓存机制，使你的应用即便是在从互联网加载数据、操作大数据集或者进行大开销的计算时仍可以保持高性能。这主要通过 `@st.cache` 装饰器来实现。

当你用 `@st.cache` 装饰器标记一个函数时，它将告诉 Streamlit 在该函数执行前需要做如下一些检查：

1. 函数的输入参数是否发生了变化
2. 函数中使用的外部变量是否发生了变化
3. 函数的主体是否发生了变化
4. 函数中用到的所有函数的主体是否发生了变化

如果以上任意一项不满足，即 Streamlit 第一次见到这四者的这种顺序组合时，它将会执行这个函数，并且将结果存储于本地缓存中。然后当下一次该带缓存的函数被调用时，如果以上四项均未发生改变，则 Streamlit 会直接跳过函数执行，而直接从缓存中调用先前的结果并返回。

Streamlit 通过哈希散列来追踪这些条件的变化。你可以把缓存当成一种存储在内存之中的键值对结构，其中上述四项总和的哈希值为键，以函数实际返回的引用为值。

最后，`@st.cache` 支持一些参数来配置缓存的行为。详见我们的 API 参考。

## 如何使用？

你可以简单地将 `st.cache` 装饰器添加至在应用中定义的函数的前一行。见如下样例。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## 代码

一下展示了如何使用 `st.cache`：

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`，以及导入其他要用到的库：

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

紧跟着的是为应用创建一个标题：

```python
st.title('Streamlit Cache')
```

接下来，我们定义了两个函数，用于生成大数据框，其中第一个函数使用了 `st.cache`，而第二个函数则不然：

```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

最后，我们调用自定义的函数，并且用 `time()` 命令对其计时。

```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

注意到第一次运行时两者速度差距不大。重新加载应用后即可见到使用了 `st.cache` 装饰器的函数运行时长的变换。你看到这其中的速度提升了吗？

## 延伸阅读

- [`st.cache` API 文档](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [使用 `st.cache` 优化性能](https://docs.streamlit.io/library/advanced-features/caching)
- [试验性缓存机制](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
