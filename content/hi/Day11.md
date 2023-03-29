# st.multiselect

`st.multiselect` एक मल्टीसिलेक्ट विजेट प्रदर्शित करता है.

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## कोड

यहां बताया गया है कि `st.multiselect` का उपयोग कैसे करें:

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इस तरह `st` से इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.multiselect')
```

इसके बाद, हम इनपुट स्वीकार करने के लिए `st.multiselect` विजेट का उपयोग करने जा रहे हैं, जहां यूज़र अपनी पसंद के एक या अधिक रंगों का चयन कर सकेंगे.

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

अंत में, हम चुने हुए रंगों को लिखेंगे:

```python
st.write('You selected:', options)
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
