# Polecenie st.form

Polecenie `st.form` tworzy formularz, który grupuje elementy wraz z przyciskiem Wyślij ("Submit").

Zazwyczaj, kiedy użytkownik wchodzi w interakcję z jakimkolwiek widżetem na stronie, cały kod aplikacji Streamlit jest wykonywany od początku.

Formularz jest specjalnym kontenerem, który wizualnie grupuje inne elementy i widżety oraz zawiera przycisk do wysłania danych. W tym przypadku użytkownik może dowolnie modyfikować wartości któregokolwiek widżetu wchodzącego w skład formularza, nie powodując przy tym ponownego wykonania aplikacji. Dopiero kiedy użytkownik wciśnie przycisk, wszystkie dane z formularza zostaną zebrane i wysłane na serwer celem przetworzenia.

Aby dodać elementy do formularza można użyć wyrażenia `with` (co jest zalecane) albo można też dodać elementy bezpośrednio do obiektu formularza poprzez wykonywanie zdefiniowanych na nim metod. Poniżej zobaczymy przykłady obu notacji.

Formularze mają kilka ograniczeń:
- każdy formularz musi zawierać specjalny typ przycisku `st.form_submit_button`.
- Inne rodzaje przycisków, takie jak `st.button` czy `st.download_button` nie mogą być dodane do formularza.
- Formularze mogą być dodane do aplikacji wszędzie (w panelu bocznym, kolumnach, itd) ale nie mogą zawierać w sobie innych formularzy.

Możesz dowiedzieć się więcej o formularzach, czytając naszego [bloga](https://blog.streamlit.io/introducing-submit-button-and-forms/).


## Przykładowa aplikacja

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## Kod

Oto przykład użycia polecenia `st.form`:

```python
import streamlit as st

st.title('Polecenie st.form')

# Pełny przykład z wykorzystaniem wyrażenia "with"
st.header('1. Przykład użycia notacji ze słowem kluczowym `with`')
st.subheader('Ekspres do kawy')

with st.form('my_form'):
    st.subheader('**Zamów kawę**')
    
    # Wejściowe widżety
    coffee_bean_val = st.selectbox('Rodzaj ziaren', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Stopień palenia', ['Jasny', 'Średni', 'Ciemny'])
    brewing_val = st.selectbox('Metoda parzenia', ['Aeropress', 'Przelew', 'French press', 'Kawiarka', 'Siphon'])
    serving_type_val = st.selectbox('Sposób podania', ['Gorąca', 'Z lodem', 'Frappe'])
    milk_val = st.select_slider('Ilość mleka', ['Bez', 'Mała', 'Średnia', 'Duża'])
    owncup_val = st.checkbox('Własny kubek')
    
    # Każdy formularz musi posiadać przycisk do wysłania
    submitted = st.form_submit_button('Wyślij')

if submitted:
    st.markdown(f'''
        ☕ Zamówiono:
        - Rodzaj ziaren: `{coffee_bean_val}`
        - Stopień palenia: `{coffee_roast_val}`
        - Metoda parzenia: `{brewing_val}`
        - Sposób podania: `{serving_type_val}`
        - Ilość mleka: `{milk_val}`
        - Własny kubek: `{owncup_val}`
        ''')
else:
    st.write('☝️ Złóż zamówienie!')


# Skrócony przykład użycia notacji obiektowej
st.header('2. Przykład użycia notacji obiektowej')

form = st.form('my_form_2')
selected_val = form.slider('Wybierz wartość')
form.form_submit_button('Wyślij')

st.write('Wybrana wartość: ', selected_val)
```

## Wyjaśnienie działania, linijka po linijce

Pierwszą rzeczą, jaką trzeba zrobić tworząc aplikację jest zaimportowanie biblioteki streamlit jako st.
```python
import streamlit as st
```

Następnie podajemy tekst nagłówka aplikacji:
```python
st.title('Polecenie st.form')
```

### Pierwszy przykład

Zacznijmy od przykładu, w którym zastosujemy polecenie `st.form` w połączeniu z wyrażeniem `with`. Tworzenie formularza rozpoczniemy od umieszczenia w jego wnętrzu nagłówka z napisem `Zamów kawę` a następnie dodamy do niego kilka widżetów (takich jak `st.selectbox`, `st.select_slider` czy `st.checkbox`) aby pobrać informacje na temat zamawianej kawy. Na koniec dodamy jeszcze przycisk do przesyłania danych, używając polecenia `st.form_submit_button`. Kiedy przycisk zostanie wciśnięty, wszystkie dane zostaną przesłane na serwer, aby je przetworzyć.

```python
# Pełny przykład z wykorzystaniem wyrażenia "with"
st.header('1. Przykład użycia notacji ze słowem kluczowym `with`')
st.subheader('Ekspres do kawy')

with st.form('my_form'):
    st.subheader('**Zamów kawę**')
    
    # Wejściowe widżety
    coffee_bean_val = st.selectbox('Rodzaj ziaren', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Stopień palenia', ['Jasny', 'Średni', 'Ciemny'])
    brewing_val = st.selectbox('Metoda parzenia', ['Aeropress', 'Przelew', 'French press', 'Kawiarka', 'Siphon'])
    serving_type_val = st.selectbox('Sposób podania', ['Gorąca', 'Z lodem', 'Frappe'])
    milk_val = st.select_slider('Ilość mleka', ['Bez', 'Mała', 'Średnia', 'Duża'])
    owncup_val = st.checkbox('Własny kubek')
    
    # Każdy formularz musi posiadać przycisk do wysłania
    submitted = st.form_submit_button('Wyślij')
```

Następnie dodamy logikę, która obsłuży przetwarzanie przesłanych danych. Domyślnie, kiedy aplikacja załaduje się po raz pierwszy, zostanie wykonany blok kodu poniżej słowa kluczowego `else` i zobaczymy komunikat o treści `☝️ Złóż zamówienie!`. Natomiast po przesłaniu danych z formularza poprzez kliknięcie przycisku `Wyślij`, dane wybrane przez użytkownika za pomocą różnych widżetów zostaną przypisane do kilku zmiennych (np. `coffee_bean_val`, `coffee_roast_val`, itd.) i zostanie wywołane polecenie `st.markdown`, które przy użyciu f-stringa wypisze szczegóły zamówienia.

```python
if submitted:
    st.markdown(f'''
        ☕ Zamówiono:
        - Rodzaj ziaren: `{coffee_bean_val}`
        - Stopień palenia: `{coffee_roast_val}`
        - Metoda parzenia: `{brewing_val}`
        - Sposób podania: `{serving_type_val}`
        - Ilość mleka: `{milk_val}`
        - Własny kubek: `{owncup_val}`
        ''')
else:
    st.write('☝️ Złóż zamówienie!')
```


### Drugi przykład
Zobaczmy teraz jak można używać polecenia `st.form` w połączeniu z notacją obiektową. W tym przykładzie rezultat polecenia `st.form`  jest przypisany do zmiennej o nazwie `form`. Następnie różne polecenia, takie jak `slider` czy `form_submit_button` są wywoływane na zmiennej `form`.


```python
# Skrócony przykład użycia notacji obiektowej
st.header('2. Przykład użycia notacji obiektowej')

form = st.form('my_form_2')
selected_val = form.slider('Wybierz wartość')
form.form_submit_button('Wyślij')

st.write('Wybrana wartość: ', selected_val)
```

## Zobacz też
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [Wprowadzenie do formularzy](https://blog.streamlit.io/introducing-submit-button-and-forms/)
