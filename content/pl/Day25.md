# Obiekt stanu sesji - st.session_state

Dostęp do aplikacji Streamlit w zakładce przeglądarki definiujemy jako sesję. Dla każdej karty przeglądarki, która łączy się z serwerem Streamlit, tworzona jest nowa sesja. Streamlit ponownie uruchamia cały skrypt od początku do końca każdym razem, gdy wchodzisz w interakcję z aplikacją. Każda ponowne uruchomienie odbywa się z czystą sesją: żadne zmienne nie są współdzielone między kolejnymi uruchomieniami.

Stan sesji jest sposobem na przechowywanie wartości zmiennych pomiędzy kolejnymi wykonaniami aplikacji, oddzielnie dla każdej sesji.
Oprócz możliwości przechowywania stanu Streamlit pozwala na zmianę stanu za pomocą callbacków.

Podczas dzisiejszej lekcji pokażemy, w jaki sposób używać stanu sesji i callbacków podczas budowania aplikacji do konwersji jednostek.

Obiekt `st.session_state` pozwala na dostęp do danych sesji w aplikacji Streamlit.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## Kod

Oto jak używać objektu `st.session_state`:
```python
import streamlit as st

st.title('Obiekt st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Wejście')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Funty:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilogramy:", key = "kg", on_change = kg_to_lbs)

st.header('Wyjście')
st.write("Obiekt st.session_state:", st.session_state)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st. 
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Obiekt st.session_state')
```

Potem zdefiniujemy własne funkcje do przeliczania wagi z funtów na kilogramy i odwrotnie:

```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

W tym miejscu korzystamy z `st.number_input` aby pobrać wejściowe wartości wagi do przeliczenia
```python
st.header('Wejście')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Funty:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilogramy:", key = "kg", on_change = kg_to_lbs)
```

Te dwie powyższe funkcje zostaną wywołane, kiedy tylko numeryczna wartość zostanie wpisana w jeden z widżetów wygenerowanych za pomocą polecenia `st.number_input`. Zwróć uwagę, że opcja `on_change` w jednym z widżetów wskazuje na funkcję `lbs_to_kg` a w drugim na `kg_to_lbs`.

W skrócie, po wprowadzeniu liczby w polu `st.number_input` jest ona konwertowana przez jedną z naszych funkcji.

Na koniec wartości wagi w kilogramach (`kg`) i funtach (`lbs`) zostają zapisane w stanie sesji jako `st.session_state.kg` and `st.session_state.lbs` a ich wartości wypisane poprzez polecenie `st.write`:

```python
st.header('Wyjście')
st.write("Objekt st.session_state:", st.session_state)
```

## Zobacz też
- [Stan sesji](https://docs.streamlit.io/library/api-reference/session-state)
- [Dodawanie stanowości do aplikacji](https://docs.streamlit.io/library/advanced-features/session-state)
