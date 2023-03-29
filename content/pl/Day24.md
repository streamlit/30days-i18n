# Polecenie st.cache

Polecenie `st.cache` pozwala zoptymalizować wydajność aplikacji Streamlit.

Streamlit dostarcza mechanizmy buforowania, który pozwalają Twojej aplikacji zachować wydajność nawet podczas ładowania danych z sieci, manipulowania dużymi zbiorami danych lub wykonywania kosztownych obliczeń. Służy do tego dekorator `@st.cache`.

Dekorowanie funkcji za pomocą `@st.cache` informuje bibliotekę Streamlit, że za każdym razem, gdy funkcja jest wywoływana, należy sprawdzić kilka rzeczy:

1. Z jakimi wejściowymi parametrami wywołano funkcję
2. Jakie wartości przyjmowały zewnętrzne parametry używane przez funkcję
3. Jakie było ciało funkcji
4. Jakie było ciało innych funkcji wywoływanych wewnątrz buforowanej funkcji


Jeśli Streamlit po raz pierwszy spotyka wywołanie funkcji z tymi konkretnymi wartościami tych czterech komponentów w tej dokładnej kombinacji i kolejności, to uruchamia funkcję i zapisuje jej wynik w pamięci podręcznej. Następnie, następnym razem, gdy buforowana funkcja zostanie wywołana, jeśli żaden z tych komponentów nie uległ zmianie, Streamlit całkowicie pominie wykonanie tej funkcji i zamiast tego zwróci jej wynik przechowywany w pamięci podręcznej.

Streamlit używa hashowania, aby śledzić opisane powyżej zmiany. Buforowanie można traktować jak słownik przechowujący klucze i wartości. Zawartością klucza jest funkcją skrótu wszystkich 4 komponentów, natomiast wartością jest wynik działania funkcji przekazany przez referencję.

Na koniec warto zauważyć, że `@st.cache` może przyjmować dodatkowe argumenty, aby skonfigurować sposób buforowania. Więcej informacji na ten temat można znaleźć w dokumentacji API.

## Sposób użycia

Możesz po prostu dodać dekorator `st.cache` przed definicją funkcji, której używasz w Twojej aplikacji. Zobacz przykład poniżej.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## Kod

Oto jak używać polecenia `st.cache`:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('Polecenie st.cache')

# Z użyciem buforowania
a0 = time()
st.subheader('Z użyciem st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Bez użycia buforowania
b0 = time()
st.subheader('Bez użycia st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przydadzą nam się również inne biblioteki.

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Polecenie st.cache')
```

Potem definiujemy dwie własne funkcję, które tworzą bardzo duże ramki danych. Pierwsza z tych funkcji będzie korzystać z dekoratora `st.cache` a druga nie.

```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

Na koniec uruchomimy nasze funkcje i zmierzymy czas ich wykonania za pomocą polecenia `time()`.

```python
# Using cache
a0 = time()
st.subheader('Z użyciem st.cache')

# Tutaj wykonujemy funkcję load_data_a i mierzymy czas

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Bez użycia st.cache')

# Tutaj wykonujemy funkcję load_data_b i mierzymy czas

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```
Zauważ, że przy pierwszym uruchomieniu czasy wykonania obu funkcji są zbliżone. Jednak przy kolejnym uruchomieniu czas wykonania dekorowanej funkcji znacznie się zmienia. Czy zauważyłeś przyspieszenie działania?

## Zobacz też
- [`st.cache` w dokumentacji](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [Zoptymalizuj wydajność z użyciem `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [Eksperymentalne polecenia buforowania](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
