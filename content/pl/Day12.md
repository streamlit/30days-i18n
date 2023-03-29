# Polecenie st.checkbox

Polecenie `st.checkbox` wyświetla widżet pola wyboru.

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej tak jak ta tutaj:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## Kod
Oto jak będziemy używać polecenia `st.checkbox`:

```python
import streamlit as st

st.header('Polecenie st.checkbox')

st.write ('Co chciałbyś zamówić?')

icecream = st.checkbox('Lody')
coffee = st.checkbox('Kawę')
cola = st.checkbox('Colę')

if icecream:
     st.write("Świetnie! Oto Twoje lody 🍦")
    
if coffee: 
     st.write("Super, oto Twoja kawa ☕")

if cola:
     st.write("Proszę bardzo 🥤")
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st:

```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.header('Polecenie st.checkbox')
```

Teraz zadamy użytkownikowi pytanie wyświetlając je w aplikacji poleceniem `st.write':
```python
st.write ('Co chciałbyś zamówić?')
```

Po czym zaprezentujemy kilka opcji z menu do wyboru:
```python
icecream = st.checkbox('Lody')
coffee = st.checkbox('Kawę')
cola = st.checkbox('Colę')
```

Na koniec wypiszemy tekst, w zależności o tego, które pozycje zostały wybrane:

```python
if icecream:
     st.write("Świetnie! Oto Twoje lody 🍦")
    
if coffee: 
     st.write("Super, oto Twoja kawa ☕")

if cola:
     st.write("Proszę bardzo 🥤")
```  

## Zobacz też
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
