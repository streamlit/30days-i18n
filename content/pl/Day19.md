# Jak rozmieścić widżety wewnątrz Twojej aplikacji.

Dzisiaj poznamy następujące polecenia pomagające rozplanować wizualne elementy Twojej aplikacji:


- `st.set_page_config(layout="wide")` - Wyświetla zawartość aplikacji w trybie "szerokim" (w innym przypadku, domyślnie, treść aplikacji będzie umieszczona w polu o stałej szerokości).
- `st.sidebar` - Umieszcza widżety w panelu bocznym.
- `st.expander` - Umieszcza widżety wewnątrz kontenera, który można zmniejszać.
- `st.columns` - Tworzy kolumny, wewnątrz których można umieszczać zawartość.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## Kod
Oto jak dostosować rozmieszczenie wizualnych elementów w Twojej aplikacji:

```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('Jak rozmieścić widżety wewnątrz Twojej aplikacji')

with st.expander('O tej aplikacji'):
  st.write('Ta aplikacja pokazuje różne sposoby aranżacji wizualnych elementów.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Wejście')
user_name = st.sidebar.text_input('Jak masz na imię?')
user_emoji = st.sidebar.selectbox('Wybierz emotkę', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Co najbardziej lubisz jeść?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Wyjście')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Cześć {user_name}!')
  else:
    st.write('👈  Proszę, podaj swoje **imię**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} to Twoja ulubiona **emotka**!')
  else:
    st.write('👈 Wybierz swoją **emotkę**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** jest Twoją ulubioną **potrawą**!')
  else:
    st.write('👈 Wybierz swoją ulubioną **potrawę**!')
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
```

Zaczniemy od ustawienia "szerokiego" trybu aplikacji, co pozwoli zawartości zająć całą szerokość przeglądarki.
```python
st.set_page_config(layout="wide")
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Jak rozmieścić widżety wewnątrz Twojej aplikacji')
```

Rozszerzalny kontener pod tytułem `O tej aplikacji` zostanie umieszczony poniżej nagłówka. Po rozwinięciu zobaczymy w środku dodatkowe szczegóły.
```python
with st.expander('O tej aplikacji'):
  st.write('Ta aplikacja pokazuje różne sposoby aranżacji wizualnych elementów.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

Widżety akceptujące informacje od użytkowników są umieszczone w panelu bocznym za pomocą polecenia `st.sidebar` przed wywołaniem komend `text_input` oraz `selectbox`. Wartości wpisane bądź wybrane przez użytkownika są przypisane i przechowywane wewnątrz zmiennych o nazwie `user_name`, `user_emoji` oraz `user_food`.

```python
st.sidebar.header('Wejście')
user_name = st.sidebar.text_input('Jak masz na imię?')
user_emoji = st.sidebar.selectbox('Wybierz emotkę', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('Co najbardziej lubisz jeść?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Na koniec stworzymy 3 kolumny wykorzystując polecenie `st.columns`, którego wynik rozpakujemy do zmiennych `col1`, `col2` and `col3`. Następnie rozmieścimy treści wewnątrz każdej z kolumn, za pomocą wciętych bloków, zaczynających się poniżej wyrażenia `with`. Stworzymy pod nim wyrażenia warunkowe, które wyświetlą różne komunikaty w zależności od tego czy użytkownik wybrał wejściowe wartości (z bocznego panelu) czy nie. Domyślnie, strona wyświetli tekst, który można znaleźć poniżej każdego wyrażenia `else`. Po podaniu wartości przez użytkownika, komunikat informujący o jego wyborze zostanie wyświetlona poniżej nagłówka pod tytułem `Wyjście`.

```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Cześć {user_name}!')
  else:
    st.write('👈  Proszę, podaj swoje **imię**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} to Twoja ulubiona **emotka**!')
  else:
    st.write('👈 Wybierz swoją **emotkę**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** jest Twoją ulubioną **potrawą**!')
  else:
    st.write('👈 Wybierz swoją ulubioną **potrawę**!')
```
Warto też zauważyć, że do połączenia gotowego tekstu z wartościami podanymi przez użytkownika zostały użyte f-stringi.

## Zobacz też
- [Rozmieszczenie i kontenery](https://docs.streamlit.io/library/api-reference/layout)
