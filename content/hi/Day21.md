# st.progress

`st.progress` एक प्रगति बार प्रदर्शित करता है जो पुनरावृत्ति की प्रगति के रूप में ग्राफ़िक रूप से अपडेट होता है|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## कोड
यहां बताया गया है कि `st.progress` का उपयोग कैसे करें:यहां बताया गया है कि <3/> का उपयोग कैसे करें:
```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी के साथ-साथ `time` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
import time
```

आगे, हम ऐप के लिए एक टाइटल टेक्स्ट बनाते हैं:
```python
st.title('st.progress')
```

`st.write` का उपयोग करके एक <Bold>About बॉक्स</Bold> बनाया जाता है और `st.expander` के माध्यम से विवरण प्रदर्शित किया जाता है:
```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

अंत में, हम प्रगति बार को परिभाषित करते हैं और इसे `0` के शुरुआती मान के साथ तुरंत चालू करते हैं|
फिर, `for` लूप `0` से `100` तक पहुंचने तक पुनरावृति करेगा|
प्रत्येक पुनरावृत्ति में, हम `my_bar` प्रगति बार में `1` का मान जोड़ने से पहले ऐप को `0.05` seconds तक प्रतीक्षा करने की अनुमति देने के लिए `time.sleep(0.05)` का उपयोग करते हैं और ऐसा करने में बार का ग्राफ़िकल प्रदर्शन प्रत्येक पुनरावृत्ति के साथ बढ़ता है|
```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
