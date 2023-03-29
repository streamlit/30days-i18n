# st.session_state

हम सेशन के रूप में ब्राउज़र टैब में Streamlit ऐप के लिए ऐक्सेस को परिभाषित करते हैं|
Streamlit सर्वर से कनेक्ट होने वाले प्रत्येक ब्राउज़र टैब के लिए, एक नया सेशन बनाया जाता है|
हर बार जब आप अपने ऐप के साथ इंटरैक्ट करते हैं तो Streamlit आपकी स्क्रिप्ट को ऊपर से नीचे तक रीरन करता है|
प्रत्येक रीरन एक खाली स्लेट में होता है: रनों के बीच कोई वेरिएबल शेयर नहीं किया जाता है|

सेशन स्टेट प्रत्येक यूज़र सेशन के लिए रीरन के बीच वेरिएबल शेयर करने का एक तरीका है|
स्टेट को संग्रहीत करने और बनाए रखने की क्षमता के अलावा, Streamlit कॉलबैक का उपयोग करके स्टेट में हेरफेर करने की क्षमता को भी उजागर करता है|

इस ट्यूटोरियल में, हम एक वेट कन्वर्ज़न ऐप बनाते समय सेशन स्टेट और कॉलबैक के उपयोग को स्पष्ट करेंगे|

`st.session_state` Streamlit ऐप में सेशन स्टेट के इम्प्लिमेन्टेशन की अनुमति देता है|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## कोड
यहां `st.session_state` को उपयोग करने का तरीका बताया गया है:
```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को `st` के रूप में इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
```

सबसे पहले, हम ऐप का शीर्षक बनाकर शुरुआत करेंगे:
```python
st.title('st.session_state')
```

इसके बाद, हम वेट कन्वर्ज़न के लिए lbs से किलो और किलो से lbs के लिए कस्टम फ़ंक्शन परिभाषित करते हैं:
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

यहां, हम वज़न मानों के संख्यात्मक इनपुट स्वीकार करने के लिए `st.number_input` उपयोग करते हैं:
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```
`st.number_input` कमांड का उपयोग करके बनाए गए नंबर बॉक्स में एक संख्यात्मक मान दर्ज करते ही उपरोक्त 2 कस्टम फ़ंक्शंस को कॉल किया जाएगा|
ध्यान दें कि `on_change` विकल्प 2 कस्टम फ़ंक्शंस `lbs_to_kg` और `kg_to_lbs` कैसे निर्दिष्ट करता है).

संक्षेप में, <11/> बॉक्स में एक नंबर दर्ज करने पर नंबर इन कस्टम फ़ंक्शंस द्वारा परिवर्तित हो जाता है|

अंत में, `kg` और `lbs` इकाइयों में वज़न मान सेशन स्टेट में `st.session_state.kg` और `st.session_state.lbs` के रूप में संग्रहीत किया जाएगा जो `st.write` के माध्यम से प्रिंट किया जाएगा:
```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## आगे पढ़े
- [सेशन स्टेट](https://docs.streamlit.io/library/api-reference/session-state)
- [ऐप्स में स्टेटफुलनेस जोड़ें](https://docs.streamlit.io/library/advanced-features/session-state)
