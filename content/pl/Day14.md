# Komponenty

Komponenty są zewnętrznymi modułami Pythona, które rozszerzają możliwości biblioteki Streamlit [[1](https://docs.streamlit.io/library/components)].

## Jakie komponenty są dostępne?

Na stronie biblioteki Streamlit znajduje się kilkadziesiąt komponentów [[2](https://streamlit.io/components)].

Fanilo (twórca biblioteki) skomponował listę najciekawszych komponentów i umieścił ją na stronie [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)] W kwietniu 2022, na liście znajdowało się 85 komponentów.

## Jak używać komponentów?

Jak każdy ogólnodostępny moduł Pythona, komponenty można zainstalować poleceniem `pip install`.

W dzisiejszej lekcji będziemy używać komponentu o nazwie `streamlit_pandas_profiling` [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### Instalacja komponentu

```bash
pip install streamlit_pandas_profiling
```

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## Kod

Oto jak stworzyć aplikację w technologii Streamlit, która wykorzystuje komponent:

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przydadzą nam się również inne biblioteki, w tym oczywiście nasz komponent.

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

Następnie podajemy tekst nagłówka aplikacji:

```python
st.header('`Komponent streamlit_pandas_profiling`')
```

W kolejnym kroku ładujemy przykładowy zbiór danych o pingwinach wykorzystując polecenie `read_csv` dostarczane przez bibliotekę `pandas`.

```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

Na koniec generujemy raport z danych używając polecenia `profile_report()` i wyświetlamy go za pomocą `st_profile_report`:
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## Tworzenie własnych komponentów

Jeśli chciałabyś tworzyć własne komponenty, sprawdź poniższe materiały (po angielsku):
- [Tworzenie komponentu](https://docs.streamlit.io/library/components/create)
- [Publikowanie komponentu](https://docs.streamlit.io/library/components/publish)
- [Interfejs komponentów](https://docs.streamlit.io/library/components/components-api)
- [Post na blogu o komponentach](https://blog.streamlit.io/introducing-streamlit-components/)

Poza tym, jeśli wolisz się uczyć z filmików, to Tim Conkling, nasz inżynier przygotował kilka świetnych wideo poradników:
- [Jak zbudować komponent | Część 1: Przygotowanie i architektura](https://youtu.be/BuD3gILJW-Q)
- [Jak zbudować komponent | Część 2: Twój własny widżet suwaka](https://youtu.be/QjccJl_7Jco)

## Więcej na temat komponentów
1. [Komponenty-dokumentacja API](https://docs.streamlit.io/library/components)
2. [Wybrane komponenty](https://streamlit.io/components)
3. [Dyskusja społeczności na temat nowych komponentów](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
