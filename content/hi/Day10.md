# st.selectbox

`st.selectbox` एक सिलेक्ट विजेट के प्रदर्शन की अनुमति देता है.

## हम क्या बना रहे हैं?

एक आसान ऐप जो यूज़र से पूछता है कि उनका पसंदीदा रंग क्या है.

ऐप का फ़्लो:
1. यूज़र एक रंग चुनता है
2. ऐप चुने गए रंग को प्रिंट करता है

## डेमो ऐप
डिप्लॉय किए गए Streamlit ऐप को नीचे दिए गए लिंक में दिखाए गए जैसा दिखना चाहिए:

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## कोड
उपरोक्त ऐप को लागू करने के लिए कोड यहां दिया गया है:

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इस तरह `st` से इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.selectbox')
```

इसके बाद, हम `option` नाम का एक वेरिएबल बनाएंगे, जिसे `st.selectbox()` कमांड के माध्यम से **सिलेक्ट** इनपुट विजेट के रूप में यूज़र इनपुट स्वीकार करेगा.

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```

जैसा कि हम उपरोक्त कोड बॉक्स से देख सकते हैं, `st.selectbox()` कमांड 2 इनपुट आर्ग्युमेंट्स को स्वीकार करता है:

1. टेक्स्ट जो सिलेक्ट विजेट पर जाता है, यानी <9/> `'What is your favorite color?'`
2. `('Blue', 'Red', 'Green')` से चुनने के लिए संभावित मान

अंत में, हम चुने हुए रंग को इस प्रकार प्रिंट करेंगे:

```python
st.write('Your favorite color is ', option)
```

## आगे के स्टेप्स

अब जब आपने Streamlit ऐप को स्थानीय रूप से बना लिया है, तो इसे [Streamlit Community Cloud](https://streamlit.io/cloud) पर डिप्लॉय करने का समय आ गया है.

## संदर्भ 
[`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox) के बारे में और अधिक जानकारी
