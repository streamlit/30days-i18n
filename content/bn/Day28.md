# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) একটি স্ট্রিমলিট উপাদান যা [SHAP](https://github.com/slundberg/shap) প্লটগুলি প্রদর্শনের জন্য একটি মোড়ক সরবরাহ করে [স্ট্রিমলিট](https://streamlit.io/)।

লাইব্রেরিটি আমাদের ইন-হাউস স্টাফ [স্নেহান কেকরে](https://github.com/snehankekre) দ্বারা তৈরি করা হয়েছে, যিনি [স্ট্রিমলিট ডকুমেন্টেশন](https://docs.streamlit.io/) ওয়েবসাইটও রক্ষণাবেক্ষণ করেন।

প্রথমে, স্ট্রিমলিট ইনস্টল করুন (অবশ্যই!) তারপর পিপ ইন্সটল করুন `streamlit-shap` লাইব্রেরি:
```bash
pip install streamlit
pip install streamlit-shap
```

এছাড়াও ইনস্টল করার জন্য অন্যান্য পূর্বশর্ত লাইব্রেরি রয়েছে (যেমন `matplotlib`, `pandas`, `scikit-learn` এবং `xgboost`) যদি আপনি এখনও তা না করে থাকেন।


## ডেমো অ্যাপ

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## কোড
এখানে কিভাবে `স্ট্রিমলিট-শেপ` ব্যবহার করবেন:
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

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

এর পরে, আমরা পৃষ্ঠার বিন্যাসটিকে এমনভাবে প্রশস্ত করতে সেট করব যাতে স্ট্রিমলিট অ্যাপের বিষয়বস্তু পুরো পৃষ্ঠার প্রস্থকে ছড়িয়ে দিতে পারে।
```python
st.set_page_config(layout="wide")
```

তারপর, আমরা `shap` লাইব্রেরি থেকে একটি ডেটাসেটে লোড করব:
```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```


পরবর্তীকালে, আমরা ইনপুট হিসাবে `X, y` ম্যাট্রিক্স জোড়া নেওয়ার জন্য `load_model` নামক একটি ফাংশন নির্ধারণ করব, ট্রেন/পরীক্ষা সেটে ডেটা বিভাজন সম্পাদন করব, একটি `DMatrix` নির্মাণ করব এবং একটি XGBoost মডেল তৈরি করব।
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

স্ট্রিমলিট অ্যাপের শিরোনামটি তারপর প্রদর্শিত হয়:
```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

অ্যাপটির বিশদ বিবরণ দেওয়ার জন্য একটি সম্প্রসারণকারী বাক্স প্রয়োগ করা হয়েছে:
```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

এখানে, আমরা ইনপুট ডেটার `X` এবং `y` ভেরিয়েবলের এক্সপেন্ডার বক্স সহ হেডার টেক্সট প্রদর্শন করব:
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

এখানে, আমরা আসন্ন SHAP আউটপুটের জন্য হেডার টেক্সট প্রদর্শন করব:
```python
st.header('SHAP output')
```


XGBoost মডেলটি 'load_model' ফাংশন ব্যবহার করে তৈরি করা হয়েছে যা উপরে প্রয়োগ করা হয়েছে। অবশেষে,
```python
# train XGBoost model
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

এখানে, আমরা SHAP মানগুলি গণনা করব, যা ওয়াটারফল এবং বিস্বার্ম প্লটস তৈরি করতে ব্যবহৃত হয়।
```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

অবশেষে, Tree SHAP অ্যালগরিদমগুলি `shap.TreeExplainer` কমান্ডের মাধ্যমে এনসেম্বল ট্রি মডেলের আউটপুট ব্যাখ্যা করতে ব্যবহৃত হয় এবং `shap.force_plot` কমান্ডের মাধ্যমে ভিজ্যুয়ালাইজ করা হয়:
```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## আরও পড়া
- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
