# streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) ist eine Streamlit-Komponente, die einen Wrapper zur Anzeige von [SHAP](https://github.com/slundberg/shap) Plots in [Streamlit](https://streamlit.io/) bereitstellt.

Die Bibliothek wird von unserem internen Mitarbeiter [Snehan Kekre](https://github.com/snehankekre) entwickelt, der auch die Website [Streamlit Documentation](https://docs.streamlit.io/) pflegt.

Zuerst muss man Streamlit installieren (natürlich!) und dann die Bibliothek `streamlit-shap` mit pip:
```bash
pip install streamlit
pip install streamlit-shap
```

Es gibt noch weitere Bibliotheken zu installieren (z.B. `matplotlib`, `pandas`, `scikit-learn` und `xgboost`), falls du dies noch nicht getan hast.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## Code
So wird `streamlit-shap` verwendet:
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

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

Als nächstes stellen wir das Seitenlayout so ein, dass die Inhalte der Streamlit-App die gesamte Seitenbreite einnehmen können.
```python
st.set_page_config(layout="wide")
```

Dann laden wir einen Datensatz aus der Bibliothek `shap`:
```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

Anschließend wird eine Funktion namens `load_model` definiert, die das Matrixpaar `X, y` als Eingabe annimmt, die Daten in Trainings-/ Testsätze aufteilt, eine `DMatrix` erstellt und ein XGBoost-Modell erstellt.
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

Dann wird der Titel der Streamlit-App angezeigt:
```python
st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")
```

Ein "Über" Ausklappfeld ist implementiert, um Details über die App bereitzustellen:
```python
with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')
```

Hier wird die Überschrift zusammen mit einem Ausklappfeld für die Eingabevariablen "X" und "y" angezeigt:
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

Hier wird die Überschrift für die anstehende SHAP-Ausgabe angezeigt:
```python
st.header('SHAP output')
```

Das XGBoost-Modell wird dann mithilfe der Funktion "load_model" erstellt, die oben implementiert wurde.

```python
# train XGBoost model
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

Hier werden die SHAP-Werte berechnet, die dann zur Erstellung der Wasserfall- und Beeswarm-Diagramme verwendet werden.
```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

Zum Schluss wird der Tree-SHAP-Algorithmus verwendet, um die Ergebnisse von Ensemble-Baummodellen mit dem Befehl `shap.TreeExplainer` zu erklären und mit dem Befehl `shap.force_plot` zu visualisieren:
```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## Literaturhinweise
- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
