# Polecenie st.button

Polecenie `st.button` umożliwia wyświetlenie widżetu przycisku.

## Co będziemy budować?

Dziś stworzymy prostą aplikację, która wyświetla różne wiadomości w zależności od tego, czy przycisk został wciśnięty, czy nie.

Przebieg aplikacji:

1. Domyślnie aplikacja wyświetla napis `Do widzenia!`
2. Jeśli przycisk został wciśnięty, aplikacja wyświetla inną wiadomość `Hej! Jak się masz?`

## Przykładowa aplikacja

Po uruchomieniu Twoja aplikacja powinna wyglądać mniej więcej jak ta tutaj:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Kod

Poniżej kod, który implementuje naszą aplikację:

```python
import streamlit as st

st.header('Polecenie st.button')

if st.button('Przywitaj się'):
     st.write('Hej! Jak się masz?')
else:
     st.write('Do widzenia!')
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki `streamlit` jako `st` w ten sposób:

```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:

```python
st.header('Polecenie st.button')
```

Potem użyjemy wyrażeń warunkowych `if` oraz `else` żeby zdecydować, jaka wiadomość zostanie wyświetlona.

```python
if st.button('Przywitaj się'):
     st.write('Hej! Jak się masz?')
else:
     st.write('Do widzenia!')
```

Jak widać na przykładzie powyżej, polecenie `st.button()` przyjmuje parametr o nazwie `label`, do którego przekazaliśmy ciąg znaków `Przywitaj się`, który zostanie etykietą naszego przycisku.

Polecenie `st.write` jest z kolei używane do wyświetlenia wiadomości, którą będzie albo `Hej! Jak się masz?`, albo `Do widzenia!` w zależności od tego, czy przycisk został kliknięty, czy nie. Wyświetlanie wiadomości jest zaimplementowane tutaj:


```python
st.write('Hej! Jak się masz?')
```

oraz tutaj:

```python
st.write('Do widzenia!')
```

Warto zauważyć, że powyższe polecenia `st.write` są umieszczone poniżej wyrażeń warunkowych `if` oraz `else` we wciętych blokach kodu w tym celu, aby wyświetlić inną wiadomość w zależności od tego, czy warunek został spełniony, czy też nie.

## Kolejne kroki

Po stworzeniu pierwszej aplikacji lokalnie przyszedł czas na jej uruchomienie w [Społecznościowej Chmurze Streamlit](https://streamlit.io/cloud), co zostanie wyjaśnione w następnym wyzwaniu.


Ponieważ jest to Twój pierwszy tydzień nauki, udostępniamy pełny kod (powyżej) wraz z rozwiązaniem (przykładową aplikacją) bezpośrednio na tej stronie internetowej.

W kolejnych wyzwaniach staraj się najpierw samodzielnie napisać kod aplikacji, a potem porównać go z rozwiązaniem.

Nie martw się, jeśli utkniesz, możesz zawsze sprawdzić oficjalne rozwiązanie, ponieważ wszystkie prezentowane problemy mają dołączone rozwiązanie.

## Przypisy

Dowiedz się więcej o metodzie [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) z dokumentacji.
