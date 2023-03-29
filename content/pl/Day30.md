# Sztuka budowania aplikacji

Przed nami ostatni dzień wyzwania Streamlit w 30 dni. Gratulacje, że nadal jesteś z nami!

Podczas dzisiejszej lekcji postaramy się wykorzystać naszą nowo zdobytą wiedzę do zmierzenia się z rzeczywistym problemem.

## Nasz problem

Dostęp do miniatur z filmów w YouTube były bardzo przydatny różnym twórcom internetowych treści. Są to przydatne zasoby, pomocne na przykład podczas promocji w mediach społecznościowych.

Zastanówmy się, w jaki sposób możemy ugryźć ten problem poprzez zbudowanie aplikacji w technologii Streamlit.

## Rozwiązanie

Dzisiaj stworzymy aplikację o nazwie `yt-img-app`, która potrafi pobrać miniatury obrazów z filmików na YouTubie.

W uproszczeniu cały proces składa się z trzech kroków:

1. Pobranie od użytkownika linku do filmiku
2. Wyciągnięcie z linku unikalnego identyfikatora filmiku
3. Użycie identyfikatora jako wejścia do specjalnej funkcji, która wygeneruje link do miniatury.


## Instrukcje

Aby skorzystać z aplikacji, którą budujemy będzie trzeba skopiować adres URL filmiku na YouTubie i wkleić go w polu tekstowym.

## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## Kod
Oto w jaki sposób zbudować aplikację `yt-img-app`:
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('Pobierz obrazki z filmiku na YouTubie')

with st.expander('O tej aplikacji'):
  st.write('Ta aplikacja pobiera miniatury obrazów z filmików na YuTubie')
  
# Ustawienia obrazków
st.sidebar.header('Ustawienia')
img_dict = {'Maksymalna': 'maxresdefault', 'Wysoka': 'hqdefault', 'Średnia': 'mqdefault', 'Standardowa': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Wybierz jakość miniatur', ['Maksymalna', 'Wysoka', 'Średnia', 'Standardowa'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Wkej link do filmiku', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Wyświetl miniaturę filmiku
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('Miniatura znajduje się tutaj: ', yt_img)
else:
  st.write('☝️ Podaj adres URL filmiku aby kontynuować ...')
```

## Wyjaśnienie działania, linijka po linijce
Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('🖼️ yt-img-app')
st.header('Pobierz obrazki z filmiku na YouTubie')
```

Skoro już przy tym jesteśmy, to możemy dodać też sekcję o aplikacji w postaci rozszerzalnego kontenera:
```python
with st.expander('O tej aplikacji'):
  st.write('Ta aplikacja pobiera miniatury obrazów z filmików na YuTubie')
```  

Teraz stworzymy pole wyboru, za pomocą którego przyjmiemy od użytkownika informacje o preferowanej jakości miniatur

```python
# Ustawienia obrazków
st.sidebar.header('Ustawienia')
img_dict = {'Maksymalna': 'maxresdefault', 'Wysoka': 'hqdefault', 'Średnia': 'mqdefault', 'Standardowa': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Wybierz jakość miniatur', ['Maksymalna', 'Wysoka', 'Średnia', 'Standardowa'])
img_quality = img_dict[selected_img_quality]
```

Dodamy również pole tekstowe akceptujące link do filmiku na YouTubie, z którego użytkownik chce wyciągnąć miniatury.

```python
yt_url = st.text_input('Wkej link do filmiku', 'https://youtu.be/JwSS70SZdyM')
```

Następnie napiszemy własną funkcję, która wyciąga identyfikator z adresu URL
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

Na koniec użyjemy wyrażenia warunkowego, aby zdecydować, czy powinniśmy wyświetlić komunikat z prośbą o podanie linka do filmiku (kod w we wciętym bolku pod słowem kluczowym `else`) czy wyświetlić pobraną miniaturę (kod pod słowem kluczowym `if`).

```python
# Wyświetl miniaturę filmiku
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('Miniatura znajduje się tutaj: ', yt_img)
else:
  st.write('☝️ Podaj adres URL filmiku aby kontynuować ...')
```

## Podsumowanie

Przy tworzeniu dowolnej aplikacji w technologii Streamlit zwykle zaczynamy od zidentyfikowania i zdefiniowania problemu. Następnie opracowujemy rozwiązanie, dzieląc go na szczegółowe kroki, które implementujemy w naszej aplikacji.

Musimy się również zastanowić, jakich danych potrzebujemy pobrać od użytkowników, oraz w jaki sposób należy ten dane przetworzyć, aby uzyskać pożądany wynik.

Mamy nadzieję, że podobał Ci się ten samouczek, udanego tworzenia własnych aplikacji!
