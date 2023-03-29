# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) एक Streamlit कंपोनेंट है जो [Streamlit](https://streamlit.io/) में [SHAP](https://github.com/slundberg/shap) प्लॉट प्रदर्शित करने के लिए एक रैपर प्रदान करता है|

लाइब्रेरी को हमारे इन-हाउस स्टाफ़ [स्नेहन केकरे](https://github.com/snehankekre) द्वारा विकसित किया गया है जो [Streamlit दस्तावेज़ीकरण](https://docs.streamlit.io/) वेबसाइट का रखरखाव भी करता है|

सबसे पहले, Streamlit इंस्टॉल करें (बेशक!) फिर `streamlit-shap` लाइब्रेरी को pip इंस्टॉल करें:
```bash
pip install streamlit
pip install streamlit-shap
```

यदि आपने अभी तक ऐसा नहीं किया है तो इंस्टॉल करने के लिए अन्य पूर्वापेक्षित लाइब्रेरी भी हैं (उदा. `matplotlib`,`pandas`, `scikit-learn` और `xgboost`)|


## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## कोड
यहां बताया गया है कि `streamlit-shap` का उपयोग कैसे करें:
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

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करना शुरू करना है:
```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

इसके बाद, हम पेज लेआउट को इस तरह चौड़ा करेंगे कि Streamlit ऐप की सामग्री पूरे पेज की चौड़ाई में फैल सके|
```python
st.set_page_config(layout="wide")
```

फिर, हम `shap` लाइब्रेरी से डेटासेट में लोड करेंगे:
```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

इसके बाद, हम `X, y` मैट्रिक्स जोड़ी को इनपुट के रूप में लेने के लिए `load_model` कहे जाने वाले फ़ंक्शन को निश्चित करेंगे, डेटा को ट्रेन/टेस्ट सेट में विभाजित करेंगे, एक XGBoost मॉडल का निर्माण और `DMatrix` को निर्मित करेंगे|
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

तब Streamlit ऐप का टाइटल प्रदर्शित होता है:
```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

ऐप के विवरण प्रदान करने के लिए एक एक्सपांडर बॉक्स लागू किया गया है:
```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

यहां, हम इनपुट डेटा के `X` और `y` वेरिएबल्स के एक्सपांडर बॉक्स के साथ हेडर टेक्स्ट प्रदर्शित करेंगे:
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

यहां, हम आने वाले SHAP आउटपुट के लिए हेडर टेक्स्ट प्रदर्शित करेंगे:
```python
st.header('SHAP output')
```

XGBoost मॉडल तब उस `load_model` फ़ंक्शन का उपयोग करके बनाया गया है जो अभी ऊपर लागू किया गया था| अंत में,
```python
# train XGBoost model
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

यहां, हम SHAP मानों की गणना करेंगे, जिनका उपयोग Waterfall और Beeswarm प्लॉट बनाने के लिए किया जाता है.
```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

अंत में, ट्री SHAP एल्गोरिदम का उपयोग `shap.TreeExplainer` कमांड के माध्यम से एन्सेम्बल ट्री मॉडल के आउटपुट की व्याख्या करने और `shap.force_plot` कमांड के माध्यम से विज़ुअलाइज़ करने के लिए किया जाता है:
```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
