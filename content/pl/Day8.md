# Polecenie st.slider

Polecenie `st.slider` umożliwia wyświetlanie widżetu suwaka.

Suwak wspiera następujące typy danych w Pythonie: int, float, date, time, oraz datetime.

## Co będziemy budować?

Stworzymy prostą aplikację pokazującą różne sposoby przechwytywania danych wprowadzanych przez użytkowników za pomocą suwaka. 

Przebieg aplikacji:
1. Użytkownik ustawia wybraną wartość chwytając za suwak
2. Aplikacja wyświetla ustawioną wartość

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej jak ta tutaj:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## Kod
Polecenie st.slider używamy w następujący sposób:

```python
import streamlit as st
from datetime import time, datetime

st.header('Polecenie st.slider')

# Przykład 1

st.subheader('Suwak')

age = st.slider('Ile masz lat?', 0, 130, 25)
st.write("Mam ", age, 'lat')

# Przykład 2

st.subheader('Suwak z zakresem')

values = st.slider(
     'Wybierz zakres wartości',
     0.0, 100.0, (25.0, 75.0))
st.write('Wybrany zakres:', values)

# Przykład 3

st.subheader('Suwak z zakresem czasu')

appointment = st.slider(
     "Zaplanuj wizytę:",
     value=(time(11, 30), time(12, 45)))
st.write("Jesteś umówiony na:", appointment)

# Przykład 4

st.subheader('Suwak z datą i czasem')

start_time = st.slider(
     "Kiedy zaczynasz?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Czas rozpoczęcia:", start_time)

```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. Przyda nam się również standardowa biblioteka do obsługi czasu i dat:
```python
import streamlit as st
from datetime import time, datetime
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Polecenie st.slider')
```

**Przykład 1**

Suwak:

```python
st.subheader('Suwak')

age = st.slider('Ile masz lat?', 0, 130, 25)
st.write("Mam ", age, 'lat')
```

W tym przykładzie polecenie `st.slider()` służy do pobrania od użytkownika informacji o jego wieku.

W pierwszym argumencie tego polecenia podajemy tekst, który zostanie wyświetlony powyżej widżetu **suwaka**. W naszym przypadku jest to pytanie `'Ile masz lat?'`.

Kolejne trzy całkowitoliczbowe argumenty `0, 130, 25` reprezentują odpowiednio minimalną, maksymalną i domyślną wartość suwaka.

**Przykład 2**

Suwak z zakresem:

```python
st.subheader('Suwak z zakresem')

values = st.slider(
     'Wybierz zakres wartości',
     0.0, 100.0, (25.0, 75.0))
st.write('Wybrany zakres:', values)
```

Suwak zakresu pozwala na określenie pary liczb: początku i końca zakresu.

Pierwszy argument wyświetla tekst powyżej **suwaka zakresu**, w tym przykładzie będzie to `'Wybierz zakres wartości'`.

Kolejne trzy pozycyjne argumenty `0.0, 100.0, (25.0, 75.0)` reprezentują odpowiednio wartości minimalną i maksymalną, podczas gdy ostatni argument w postaci dwuelementowej krotki określa domyślne wartości początku i końca zakresu.

**Przykład 3**

Suwak z zakresem czasu:

```python
st.subheader('Suwak z zakresem czasu')

appointment = st.slider(
     "Zaplanuj wizytę:",
     value=(time(11, 30), time(12, 45)))
st.write("Jesteś umówiony na:", appointment)
```

Suwak z zakresem czasu pozwala na wybranie początka i końca zakresu będących czasem.

Pierwszy argument wyświetla tekst powyżej **suwaka z zakresem czasu**, w tym przykładzie będzie to tekst `'Zaplanuj wizytę:`.

Domyślnymi wartościami dla dolnego i górnego końca zakresu będą odpowiednio godziny 11:30 oraz 12:45.

**Przykład 4**

Suwak z datą i czasem:

```python
st.subheader('Suwak z datą i czasem')

start_time = st.slider(
     "Kiedy zaczynasz?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Czas rozpoczęcia:", start_time)
```

Ten suwak pozwala na ustawienie zarówno daty, jak i czasu.

Pierwszy argument wyświetla tekst powyżej **suwaka z datą i czasem**, w tym przykładzie będzie to tekst `'Kiedy zaczynasz?'`.

Wartość domyślna dla suwaka została przekazana poprzez parametr o nazwie `value` i określona na 1 stycznia 2020 roku o godzinie 9:30.

## Zobacz też
Kliknij poniżej, aby przeczytać o podobnym widżecie, który radzi sobie z kategoriami wartości:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
