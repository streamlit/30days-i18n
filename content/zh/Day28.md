# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) 是一个提供了在 [Streamlit](https://streamlit.io/) 中显示 [SHAP](https://github.com/slundberg/shap) 图表的功能的 Streamlit 组件。

这个库由我们团队内的成员 [Snehan Kekre](https://github.com/snehankekre) 所开发，他也负责维护 [Streamlit 文档](https://docs.streamlit.io/) 网页。

首先，我们得安装 Streamlit （显然），然后使用 pip 安装 `streamlit-shap` 库：

```bash
pip install streamlit
pip install streamlit-shap
```

还有一些其他的依赖库需要安装（例如 `matplotlib`、`pandas`、`scikit-learn` 和 `xgboost`），如果还没装的话则需要安装一下。

## 示例应用

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## 代码

以下展示了如何使用 `streamlit-shap`：

```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

@st.experimental_memo
def load_data():
    return shap.datasets.adult()

@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model

st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")

with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit 组件 that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/).
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')

st.header('Input data')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('About the data'):
    st.write('Adult census data is used as the example dataset.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)

st.header('SHAP output')

# train XGBoost model
model = load_model(X, y)

# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## 逐行解释

创建 Streamlit 应用时要做的第一件事就是将 `streamlit` 库导入为 `st`：

```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

接下来，更改页面布局为宽屏模式，让 Streamlit 应用内容占满整个页宽。

```python
st.set_page_config(layout="wide")
```

然后我们载入 `shap` 库中提供的数据库：

```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

随后我们需要定义一个 `load_model` 函数，用于接收 `X, y` 两个矩阵作为输入，将数据分割为训练集与测试集，构建一个 `DMatrix` 对象然后搭建 XGBoost 模型。

```python
@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model
```

然后我们显示这个 Streamlit 应用的标题：

```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

加入一个“有关”拓展框来提供一些应用有关的细节信息：

```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/).
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

以下我们显示一个次标题，以及展示输入数据中 `X` 和 `y` 变量的拓展框：

```python
st.header('Input data')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('About the data'):
    st.write('Adult census data is used as the example dataset.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)
```

接下来我们为此后的 SHAP 输出显示一个次标题：

```python
st.header('SHAP output')
```

然后用此前实现的 `load_model` 函数来创建 XGBoost 模型：

```python
# train XGBoost model
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

这里我们将计算 SHAP 值，然后将其用于绘制 Waterfall 图和 Beeswarm 图。

```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

最后的最后，用 `shap.TreeExplainer` 调用 Tree SHAP 算法来解释生成的决策树模型，并且用 `shap.force_plot` 对其进行可视化：

```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## 延伸阅读

- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
