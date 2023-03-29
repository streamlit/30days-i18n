# Polecenie st.selectbox

Polecenie `st.selectbox` umożliwia wyświetlanie widżetu wyboru elementów.

## Co będziemy budować?

Prostą aplikację, pozwalającą użytkownikowi wybrać jego ulubiony kolor.

Przebieg aplikacji:
1. Użytkownik wybiera kolor za pomocą widżetu
2. Aplikacja wyświetla wybór użytkownika

## Przykładowa aplikacja
Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej tak jak ta tutaj: 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## Kod

Oto w jaki sposób zaimplementujemy naszą aplikację:

```python
import streamlit as st

st.header('Polecenie st.selectbox')

option = st.selectbox(
     'Jaki jest Twój ulubiony kolor?',
     ('Niebieski', 'Czerwony', 'Zielony'))

st.write('Twój ulubiony kolor to ', option)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Polecenie st.selectbox')
```

Potem stworzymy zmienną, którą nazwiemy `option`. Będziemy w niej przechowywać wybór użytkownika dokonany przy użyciu widgetu stworzonego poleceniem `st.selectbox()`.

```python
option = st.selectbox(
     'Jaki jest Twój ulubiony kolor?',
     ('Niebieski', 'Czerwony', 'Zielony'))
```
Jak widać na powyższym przykładzie, polecenie `st.selectbox()` przyjmuje 2 argumenty wejściowe:
1. Tekst, który zostanie wyświetlony nad widżetem, np. `'Jaki jest Twój ulubiony kolor?'`
2. Zestaw możliwych odpowiedzi `('Niebieski', 'Czerwony', 'Zielony')`

Na koniec, wyświetlamy wybraną przez użytkownika wartość:
```python
st.write('Twój ulubiony kolor to ', option)
```

## Kolejne kroki
Teraz umiesz już tworzyć różne aplikacje lokalnie, dlatego nadszedł czas na ich wdrożenie w [chmurze](https://streamlit.io/cloud).

## Zobacz też 
Przeczytaj pełną dokumentację polecenia [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
