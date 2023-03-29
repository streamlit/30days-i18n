# Polecenie st.write

Polecenie `st.write` pozwala na wyświetlenie tekstu oraz innych treści bezpośrednio w aplikacji. 


Polecenie `st.write()` może być użyte do wyświetlenia następujących rzeczy:


- Ciągów znaków (stringów); wtedy to polecenie działa podobnie do `st.markdown()`
- Zawartości struktur słownikowych, `dict` w Pythonie
- Zawartości ramek danych z biblioteki `pandas` w postaci tabel
- Wykresów/obrazów/grafik wygenerowanych przy użyciu bibliotek `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
- Oraz więcej (sprawdź w [dokumentacji metody st.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## Co będziemy dziś budować?

Stworzymy prostą aplikację pokazującą różne sposoby wykorzystania polecenia `st.write()` do wyświetlenia tekstu, liczb, danych i wykresów.

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej jak ta tutaj:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Kod

Zobaczmy, jak używać polecenia st.write:

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('Polecenie st.write')

# Przykład 1

st.write('Witaj, *Świecie!* :sunglasses:')

# Przykład 2

st.write(1234)

# Przykład 3

df = pd.DataFrame({
     'pierwsza kolumna': [1, 2, 3, 4],
     'druga kolumna': [10, 20, 30, 40]
     })
st.write(df)

# Przykład 4

st.write('Poniżej znajduję ramka danych:', df, 'Powyżej znajduje się ramka danych.')

# Przykład 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki `streamlit` jako `st` w ten sposób:

```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:

```python
st.header('Polecenie st.write')
```

**Przykład 1**
Podstawowym zastosowaniem jest wyświetlanie tekstu, który może zawierać dodatkowe formatowanie (jako Markdown) i emoji:

```python
st.write('Witaj, *Świecie!* :sunglasses:')
```

**Przykład 2**
Można również wyświetlać liczby bez konieczności konwertowania ich do stringów.

```python
st.write(1234)
```

**Przykład 3**
Ramki danych (DataFrames) również mogą być wyświetlone w następujący sposób:

```python
df = pd.DataFrame({
     'pierwsza kolumna': [1, 2, 3, 4],
     'druga kolumna': [10, 20, 30, 40]
     })
st.write(df)
```

**Przykład 4**
Możesz przekazywać wiele argumentów:

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**Przykład 5**
Ponadto możesz również wyświetlać wykresy w ten sposób:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Kolejne kroki

Po stworzeniu pierwszej aplikacji lokalnie przyszedł czas na jej uruchomienie w [Społecznościowej Chmurze Streamlit](https://streamlit.io/cloud), co zostanie wyjaśnione w następnych wyzwaniach.

Ponieważ jest to Twój pierwszy tydzień nauki, udostępniamy pełny kod (powyżej) wraz z rozwiązaniem (przykładową aplikacją) bezpośrednio na tej stronie internetowej.

W kolejnych wyzwaniach staraj się najpierw samodzielnie napisać kod aplikacji, a potem porównać go z rozwiązaniem.

Nie martw się, jeśli utkniesz, możesz zawsze sprawdzić oficjalne rozwiązanie, ponieważ wszystkie prezentowane problemy mają dołączone rozwiązanie.

## Zobacz też

Poza poleceniem [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write), możesz poczytać o innych sposobach wyświetlania tekstu:

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
