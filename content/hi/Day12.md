# st.checkbox

`st.checkbox` एक चेकबॉक्स विजेट प्रदर्शित करता है.

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## कोड

यहां बताया गया है कि `st.checkbox` का उपयोग कैसे करें:

```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इस तरह `st` से इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.checkbox')
```

इसके बाद, हम `st.write` के माध्यम से एक प्रश्न पूछने जा रहे हैं:

```python
st.write ('What would you like to order?')
```

फिर हम टिक करने के लिए कुछ मेनू आइटम प्रदान करने जा रहे हैं:

```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

अंत में, हम कस्टम टेक्स्ट प्रिंट करने जा रहे हैं, जिसके आधार पर चेकबॉक्स पर टिक किया गया था:

```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
