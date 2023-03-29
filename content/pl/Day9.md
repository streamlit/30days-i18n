# Polecenie st.line_chart

Polecenie `st.line_chart` wyświetla wykres liniowy.

Tak naprawdę to polecenie korzysta pod spodem z metody `st.altair_chart`. Główna różnica jest taka, że to polecenie nie wymaga dodatkowych parametrów do konfiguracji wykresu. Dzięki temu jest łatwiejsze w użyciu bo działa na zasadzie: „weź te dane i zrób z nich wykres”, ale jednocześnie jest mniej konfigurowalne.

Jeśli `st.line_chart` nie skonfiguruje wykresu według Twoich oczekiwań, możesz zawsze użyć polecenia `st.altair_chart` i ręcznie podać dodatkowe parametry.

## Co będziemy dziś budować?

Prostą aplikację, która wyświetla wykres liniowy.

Przebieg aplikacji:
1. Generowanie ciągu liczb losowych za pomocą biblioteki `NumPy` i stworzenie z nich ramki danych biblioteki `Pandas`.
2. Stworzenie i wyświetlenie wykresu liniowego przy użyciu polecenia `st.line_chart()`.

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej jak ta tutaj:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Kod

Polecenie [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) używamy w następujacy sposób:

```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Wykres liniowy')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przydadzą nam się również biblioteki `Pandas` oraz `NumPy`.

```python
import streamlit as st
import pandas as pd
import numpy as np
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Line chart')
```

Potem tworzymy ramkę danych na podstawie losowo wygenerowanych liczb i umieszczamy je w 3 kolumnach.
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Pora na stworzenie wykresu za pomocą polecenia `st.line_chart()` poprzez podanie ramki danych przechowywanej w zmiennej `chart_data` podanej na wejście do naszego polecenia:

```python
st.line_chart(chart_data)
```

## Zobacz też
Dowiedz się więcej o poleceniu, które [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) wywołuje pod spodem:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
