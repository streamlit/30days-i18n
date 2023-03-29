# Polecenie st.latex

Polecenie `st.latex` służy do wyświetlania matematycznych wzorów sformułowanych przy użyciu notacji LaTeX.

## Co będziemy budować?

Prostą aplikację, która wyświetla matematyczne rówania korzystając ze składni LaTeXa przy użyciu polecenia `st.latex`.

## Przykładowa aplikacja
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## Kod

Oto jak używać polecenia `st.latex`:

```python
import streamlit as st

st.header('Polecenie st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.

```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Polecenie st.latex')
```

Na koniec wyświetlimy matematyczne równanie, wykorzystując polecenie `st.latex`:
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## Zobacz też
- Przeczytaj więcej na temat polecenia [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) w oficjalnej dokumentacji.
