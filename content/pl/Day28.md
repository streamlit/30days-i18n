# Komponent streamlit-shap

[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) jest komponentem biblioteki Streamlit, który dostarcza integracji z wykresami biblioteki [SHAP](https://github.com/slundberg/shap). 

Biblioteka jest rozwijana przez naszego kolegę [Snehana Kekre](https://github.com/snehankekre), który poza tym opiekuje się stroną [dokumentacji](https://docs.streamlit.io/).

Przede wszystkim zainstaluj bibliotekę Streamlit (oczywistość!) a następnie bibliotekę  `streamlit-shap`:

```bash
pip install streamlit
pip install streamlit-shap
```


Należy również mieć zainstalowane inne biblioteki (np. `matplotlib`, `pandas`, `scikit-learn` czy `xgboost`) więc upewnij się czy je masz.


## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-shap/)

## Kod

Oto jak korzystać z komponentu `streamlit-shap`:

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

st.title("Komponent `streamlit-shap` do wyświetlania wykresów SHAP w Streamlitowych aplikacjach")

with st.expander('O aplikacji'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) jest komponentem biblioteki Streamlit, który dostarcza integracji z wykresami biblioteki [SHAP](https://github.com/slundberg/shap). 
                    Biblioteka jest rozwijana przez naszego kolegę [Snehana Kekre](https://github.com/snehankekre), który poza tym opiekuje się stroną [dokumentacji](https://docs.streamlit.io/).
                ''')

st.header('Dane wejściowe')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('Informacje na temat danych'):
    st.write('Jako przykładowy zestaw danych użyto danych ze spisu ludności.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)

st.header('Wyniki')
 
# trenowanie modelu XGBoost
model = load_model(X, y)

# wyliczamy wartości przy użyciu biblioteki SHAP
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Wykres w postaci wodospadu'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Wykres w postaci plastra miodu'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Wykres siłowy'):
    st.subheader('Pierwszy wiersz danych')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('Pierwszy tysiąc wierszy danych')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przyda nam się również kilka innych bibliotek.
```python
import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd
```

Następnie zmienimy układ strony tak, aby treść naszej aplikacji wypełniała całą jej szerokość.
```python
st.set_page_config(layout="wide")
```

Potem załadujemy zbiór danych z biblioteki `shap`:
```python
@st.experimental_memo
def load_data():
    return shap.datasets.adult()
```

Teraz zdefiniujemy funkcję o nazwie `load_model` , która będzie przyjmować parametry `X, y` w postaci pary macierzy, 
podzieli dane na zestawy treningowe i testowe oraz skonstruuje macierz `DMatrix` i zbuduje model XGBoost.

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

Następnie podajemy tekst nagłówka aplikacji:

```python
st.title("Komponent `streamlit-shap` do wyświetlania wykresów SHAP w aplikacjach Streamlit")
```

Wyświetlamy również informacje o aplikacji za pomocą polecenia `st.expander`:


```python
with st.expander('O aplikacji'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) jest komponentem biblioteki Streamlit, który dostarcza integracji z wykresami biblioteki [SHAP](https://github.com/slundberg/shap). 
                    Biblioteka jest rozwijana przez naszego kolegę [Snehana Kekre](https://github.com/snehankekre), który poza tym opiekuje się stroną [dokumentacji](https://docs.streamlit.io/).
                ''')
```

Teraz wyświetlimy nagłówek razem z rozszerzalnym polem prezentującym informacje o danych wejściowych przechowywanych w zmiennych `X` oraz `y`.

```python
st.header('Dane wejściowe')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('Informacje na temat danych'):
    st.write('Jako przykładowy zestaw danych użyto danych ze spisu ludności.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)
```

Następnie wyświetlamy nagłówek informujący o spodziewanych wynikach z biblioteki SHAP:
```python
st.header('Wyniki')
```

Potem budowany jest model XGBoost. Zwraca go funkcja `load_model`, zaimplementowana powyżej:

```python
# trenowanie modelu XGBoost
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

model = load_model(X, y)
```

Dalej wyliczamy wartości SHAP, które są następnie użyte do stworzenia wykresów.

```python
# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Wykres w postaci wodospadu'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Wykres w postaci plastra miodu'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)
```

Na koniec używamy drzewiastych algorytmów SHAP, aby wyjaśnić wynik zwrócony przez nasz model. Można to zrobić przy użyciu obiektu typu `shap.TreeExplainer` oraz funkcji do wizualizacji o nazwie `shap.force_plot`.

```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)
```

## Zobacz też
- [`streamlit-shap`](https://github.com/snehankekre/streamlit-shap)
- [SHAP](https://github.com/slundberg/shap)
