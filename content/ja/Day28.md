# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)は、[Streamlit](https://streamlit.io/)で[SHAP](https://github.com/slundberg/shap)プロットを表示するためのラッパーを提供するStreamlitコンポーネントです。

このライブラリは、社内で[Streamlit Documentation](https://docs.streamlit.io/)ウェブサイトも管理しているスタッフの[Snehan Kekre](https://github.com/snehankekre)によって開発されました。

まず、Streamlitをインストールし、`streamlit-shap`ライブラリをpipでインストールします。

```bash
pip install streamlit
pip install streamlit-shap
```

まだインストールしていない場合は、他の必須ライブラリ（`matplotlib`、`pandas`、`scikit-learn`、`xgboost`など）もインストールする必要があります。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/ "Streamlitアプリ")

## コード

`streamlit-shap`の使い方は次のとおりです。

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
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
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
 
# XGBoostモデルをトレーニングします
model = load_model(X, y)

# SHAP値を計算します
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

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

次に、Streamlitアプリのコンテンツがページ幅全体に広がるように、ページレイアウトを幅広に設定します。

```python
st.set_page_config(layout="wide")
```

次に、`shap`ライブラリからデータセットを読み込みます。

```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

続いて、`X, y`マトリックスペアを入力として取り込むための`load_model`という関数を定義し、データをtrain/testセットに分割して`DMatrix`を構築し、XGBoostモデルを構築します。

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

Streamlitアプリのタイトルが表示されます。

```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

アプリの詳細を表示するバージョン情報展開ボックスが実装されます。

```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

ここでは、ヘッダーテキストと、入力データの`X`変数と`y`変数の展開ボックスを表示します。

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

ここでは、これから出力されるSHAPのヘッダーテキストを表示します。

```python
st.header('SHAP output')
```

上記で実装した`load_model`関数を使用してXGBoostモデルが構築されます。最後に

```python
# XGBoostモデルをトレーニングします
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

ここでは、SHAP値を計算し、その値を使ってWaterfallとBeeswarmのプロットを作成します。

```python
# SHAP値を計算します
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

最後に、Tree SHAPアルゴリズムを使用して、`shap.TreeExplainer`コマンドでアンサンブルツリーモデルの出力を説明し、`shap.force_plot`コマンドで視覚化します。

```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## 参考文献

- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)