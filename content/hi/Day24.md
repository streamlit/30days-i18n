# st.cache

`st.cache` आपको अपने Streamlit ऐप के प्रदर्शन को अनुकूलित करने की अनुमति देता है|

Streamlit एक कैशिंग प्रणाली प्रदान करता है जो आपके ऐप को वेब से डेटा लोड करने, बड़े डेटासेट में हेरफेर करने या बड़ी लागत की गणना करने पर भी प्रदर्शन करने की अनुमति देता है|
यह `@st.cache` डेकोरेटर के साथ किया जाता है|

जब आप किसी फ़ंक्शन को `@st.cach` डेकोरेटर के साथ मार्क करते हैं, तो यह Streamlit को बताता है कि जब भी फ़ंक्शन को कॉल किया जाता है, तो उसे कुछ चीजों की जांच करने की ज़रूरत होती है:

1. वे इनपुट पैरामीटर जिन्हें आपने फ़ंक्शन के साथ कॉल किया था
2. फ़ंक्शन में उपयोग किए गए किसी बाहरी वेरिएबल का मान
3. फ़ंक्शन का मुख्य भाग
4. कैश्ड फ़ंक्शन के अंदर उपयोग किए गए किसी भी फ़ंक्शन का मुख्य भाग

यदि यह पहली बार है जब Streamlit ने इन चार कंपोनेंट्स को इन सटीक मानों के साथ देखा है और इस सटीक संयोजन और क्रम में, यह फ़ंक्शन चलाता है और परिणाम को स्थानीय कैश में संग्रहीत करता है|
फिर, अगली बार कैश्ड फ़ंक्शन को कॉल किया जाता है, यदि इनमें से कोई भी कंपोनेंट नहीं बदला गया है, तो Streamlit फ़ंक्शन को पूरी तरह से निष्पादित करना छोड़ देगा और इसके बजाय, कैश में पहले से संग्रहीत आउटपुट को वापस कर देगा|
 
जिस तरह से Streamlit इन कंपोनेंट्स में बदलाव का ट्रैक रखता है, वह हैशिंग के माध्यम से होता है|
कैश को इन-मेमोरी की-वैल्यू स्टोर के रूप में सोचें, जहां की उपरोक्त सभी का हैश है और वैल्यू संदर्भ द्वारा पास किया गया वास्तविक आउटपुट ऑब्जेक्ट है|

अंत में, `@st.cache` कैश के व्यवहार को कॉन्फ़िगर करने के लिए आर्ग्युमेंट्स का समर्थन करता है|
आप हमारे API संदर्भ में उन पर अधिक जानकारी प्राप्त कर सकते हैं|

## कैसे उपयोग करें?

आप अपने Streamlit ऐप में आपके द्वारा परिभाषित कस्टम फ़ंक्शन की पहले की लाइन पर `st.cache` डेकोरेटर जोड़ सकते हैं|
नीचे दिया गया उदाहरण देखें|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## कोड
यहां `st.cache` को उपयोग करने का तरीका बताया गया है:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी के साथ-साथ ऐप में उपयोग की जाने वाली अन्य लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

इसके बाद ऐप के लिए एक टाइटल टेक्स्ट बनाया जाता है:
```python
st.title('Streamlit Cache')
```

इसके बाद, हम एक बड़े DataFrame को जनरेट करने के लिए 2 कस्टम फ़ंक्शंस को परिभाषित करेंगे, जहां पहला `st.cache` डेकोरेटर का उपयोग करता है जबकि दूसरा नहीं करता है:
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

अंत में, हम `time()` कमांड का उपयोग करते हुए रन टाइम का समय निर्धारित करते हुए कस्टम फ़ंक्शन चलाते हैं|
```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

ध्यान दें कि पहला रन लगभग समान रन टाइम कैसे प्रदान कर सकता है|
ऐप को फिर से लोड करें और ध्यान दें कि `st.cache` डेकोरेटर का उपयोग करते समय रन टाइम कैसे बदलता है|
क्या आपने गति में कोई वृद्धि देखी?

## इस विषय से संबंधित कुछ और लिंक/लेख
- [`st.cache` API दस्तावेज़ीकरण](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [इसके साथ प्रदर्शन को आप्टमाइज़ करें `st.cache`](https://docs.streamlit.io/library/advanced-features/caching)
- [इक्स्पेरिमेन्टल कैश प्रिमिटिव्स](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
