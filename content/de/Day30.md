# Die Kunst der Erstellung von Streamlit-Apps

Heute ist Tag 30 des Wettbewerbs *#30DaysOfStreamlit*. Herzlichen Glückwunsch, dass du so weit gekommen bist.

In diesem Tutorial werden wir unser neu erworbenes Wissen aus dieser Herausforderung nutzen, um Streamlit-Apps zur Lösung realer Probleme zu erstellen.

## Real existierendes Problem

Als Content-Ersteller ist der Abruf von Vorschaubildern (Thumbnails) der YouTube-Videos eine nützliche Ressource für die soziale Werbung und die Erstellung von Content.

Lass uns herausfinden, wie wir dieses Problem angehen und eine Streamlit-App bauen können.

## Lösung

Heute werden wir `yt-img-app` bauen, eine Streamlit-App, die Vorschaubilder aus YouTube-Videos extrahieren kann.

Kurzgesagt, hier sind die 3 einfachen Schritte, die wir mit der Streamlit-App durchführen wollen:

1. Annehmung einer YouTube-URL als Benutzereingabe
2. Durchführen einer Textverarbeitung der URL, um die eindeutige YouTube-Video-ID zu extrahieren
3. Verwendung der YouTube-Video-ID als Eingabe für eine Funktion, die das Vorschaubild von YouTube-Videos abruft und anzeigt

## Anleitung

Um die Streamlit-App zu verwenden, kopiere eine YouTube-URL und füge sie in das Textfeld ein.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/)

## Code
So baut man die `yt-img-app` Streamlit App:
```python
import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
  
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## Zeilenweise Erklärung
Der erste Schritt für das Erstellen einer Streamlit App ist es, die `streamlit` Bibliothek als `st` sowie andere Bibliotheken zu importieren:
```python
import streamlit as st
```

Als nächstes zeigen wir der Titel der App und die dazugehörige Überschrift an:
```python
st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```
Wo wir gerade dabei sind, können wir auch gleich eine ausklappbare Box einbauen.
```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
 
Hier erstellen wir ein Auswahlfeld, in das der Benutzer die gewünschte Bildqualität eingeben kann.
```python
# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

Es wird ein Eingabefeld angezeigt, in das der Benutzer die URL des YouTube-Videos eingeben kann, aus dem das Bild extrahiert werden soll.
```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

Eine Funktion, die die Textverarbeitung der Eingabe-URL durchführt:
```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

Zuletzt verwenden wir Verzweigung, um zu bestimmen, ob die Eingabeaufforderung der URL angezeigt werden soll (d.h. wie in der `else`-Anweisung) oder ob das YouTube-Thumbnail-Bild angezeigt werden soll (d.h. wie in der `if`-Anweisung).
```python
# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
```

## Zusammenfassung

Insgesamt haben wir gesehen, dass wir bei der Erstellung einer Streamlit-App in der Regel damit beginnen, das Problem zu identifizieren und zu definieren. Als nächstes entwickeln wir eine Lösung für das Problem, indem wir es in einzelne Schritte zerlegen, die wir in der Streamlit-App implementieren. 

Hier müssen wir auch festlegen, welche Daten oder Informationen wir als Eingabe von den Nutzern benötigen und welchen Ansatz und welche Methode wir bei der Verarbeitung der Nutzereingaben verwenden wollen, um die gewünschte Endausgabe zu erzeugen.

Wir hoffen, dass dir dieses Tutorial gefallen hat. Viel Spaß beim Streamlit-ing!
