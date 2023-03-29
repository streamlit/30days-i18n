# st.slider

`st.slider`स्लाइडर इनपुट विजेट को प्रदर्शित करने की अनुमति देता है.

निम्नलिखित डेटा प्रकार समर्थित हैं: इंट, फ्लोट, दिनांक, समय और datetime.

## हम क्या बना रहे हैं?

एक आसान ऐप जो स्लाइडर विजेट को समायोजित करके यूज़र इनपुट को स्वीकार करने के विभिन्न तरीकों को दिखाता है.

ऐप का फ़्लो:
1. यूज़र स्लाइडर विजेट को एडजस्ट करके मान का चयन करता है
2. ऐप चयनित मान को प्रिंट करता है

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## कोड
यहां बताया गया है कि `st.slider` का उपयोग कैसे करें:

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इस तरह `st` से इम्पोर्ट करना शुरू करना है:

```python
import streamlit as st
from datetime import time, datetime
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.slider')
```

**उदाहरण 1**

स्लाइडर:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

जैसा कि हम देख सकते हैं, `st.slider()` कमांड का उपयोग यूज़र की आयु के बारे में यूज़र इनपुट एकत्र करने के लिए किया जाता है.

पहला इनपुट तर्क **स्लाइडर** विजेट के ठीक ऊपर टेक्स्ट प्रदर्शित करता है जो `'How old are you?'` पूछ रहा है.

निम्नलिखित तीन पूर्णांक `0, 130, 25` क्रमशः न्यूनतम, अधिकतम और डिफ़ॉल्ट मान दर्शाते हैं.

**उदाहरण 2**

रेंज स्लाइडर:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

रेंज स्लाइडर एक निचले और ऊपरी बाउंड वैल्यू पेयर के चयन की अनुमति देता है.

पहला इनपुट तर्क **रेंज स्लाइडर** विजेट के ठीक ऊपर टेक्स्ट प्रदर्शित करता है जो `'Select a range of values'` पूछ रहा है.

निम्नलिखित तीन तर्क `0.0, 100.0, (25.0, 75.0)` न्यूनतम और अधिकतम मानों को दर्शाते हैं जबकि अंतिम टपल चयनित निम्न (25.0) और ऊपरी (75.0) बाध्य मानों के रूप में उपयोग करने के लिए डिफ़ॉल्ट मानों को दर्शाता है.

**उदाहरण 3**

रेंज टाइम स्लाइडर::

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

रेंज टाइम स्लाइडर datetime के लोअर और अपर बाउंड वैल्यू पेयर के चयन की अनुमति देता है.

पहला इनपुट तर्क **रेंज टाइम स्लाइडर** विजेट के ठीक ऊपर टेक्स्ट प्रदर्शित करता है जो `'Schedule your appointment:` पूछ रहा है.

datetime के लोअर और अपर बाउंड वैल्यू पेयर के लिए डिफ़ॉल्ट मान क्रमशः 11:30 और 12:45 पर सेट हैं.

**Eउदाहरण 4**

datetime स्लाइडर::

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

datetime स्लाइडर datetime के चयन की अनुमति देता है.

पहला इनपुट तर्क **datetime** स्लाइडर विजेट के ठीक ऊपर टेक्स्ट प्रदर्शित करता है जो `'When do you start?'` पूछ रहा है.

1 जनवरी, 2020 को 9:30 बजे के `value` विकल्प का उपयोग करके datetime के लिए डिफ़ॉल्ट मान सेट किया गया था

## इसी विषय से जुड़े कुछ और लिंक/लेख
आप निम्नलिखित संबंधित विजेट का भी पता लगा सकते हैं:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)
