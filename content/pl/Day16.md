# Dostosowywanie wyglądu aplikacji

Używając parametrów w pliku `config.toml`, można w łatwy sposób skonfigurować wizualne aspekty aplikacji. Plik `config.toml` znajduje się w ukrytym podkatalogu o nazwie `.streamlit` wewnątrz tego samego katalogu, w którym znajduje się aplikacja.

## Co będziemy budować?

Prostą aplikację, która pokazuje efekty dostosowania graficznego motywu aplikacji. Można to zrobić poprzez zmianę heksadecymalnych kodów kolorów wewnątrz pliku [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml).


## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## Kod
Oto kod, który należy umieścić w pliku [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) file:
```python
import streamlit as st

st.title('Dostosowywanie wyglądu aplikacji')

st.write('Zawartość pliku `.streamlit/config.toml` dla tej aplikacji')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Wybierz liczbę:', 0, 10, 5)
st.write('Twoja wybrana liczna to:', number)
```

Oto zawartość pliku [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml):
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. 
```python
import streamlit as st
```
Następnie podajemy tekst nagłówka aplikacji:

```python
st.title('Dostosowywanie wyglądu aplikacji')
```

Potem wyświetlimy zawartość pliku `.streamlit/config.toml` do czego użyjemy polecenia `st.write` aby wyświetlić informację na temat pliku, oraz polecenia `st.code` aby wyświetlić właściwy kod:

```python
st.write('Zawartość pliku `.streamlit/config.toml` dla tej aplikacji')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

Na koniec stworzymy widżet suwaka oraz wyświetlimy jego bieżącą wartość:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Przyjrzyjmy się różnym kolorom, które określiliśmy dla naszej aplikacji poprzez ustawienie ich wewnątrz pliku `.streamlit/config.toml`
- `primaryColor="#F39C12"` - Tutaj ustawiamy główny kolor aplikacji na pomarańczowy. Zwróć uwagę na pomarańczowe kolory widżetu suwaka.
- `backgroundColor="#2E86C1"` - Tu ustawiamy kolor tła na niebieski. Zauważ, że tło głównego panelu jest teraz niebieskie.
- `secondaryBackgroundColor="#AED6F1"` - W tym miejscu ustawiamy drugi kolor tła na ciemnoszary. Dzięki temu panel boczny oraz pole kodu mają teraz ciemnoszare tła. 
- `textColor="#FFFFFF"` - Kolor tekstu jest ustawiony na biały.
- `font="monospace"` - Ta opcja spowoduje wybranie czcionki o stałej szerokości.


## Zobacz też
- [Ostylowanie aplikacji](https://docs.streamlit.io/library/advanced-features/theming)
- [Kody kolorów w HTML](https://htmlcolorcodes.com/) jest doskonałym narzędziem do wybierania interesujących kolorów.
