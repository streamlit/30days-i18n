# Bored API ऐप बनाकर API का उपयोग कैसे करें

जब आप बोर हो जाते हैं तो Bored API ऐप आपके लिए मज़ेदार चीजें सुझाता है!

तकनीकी रूप से, यह Streamlit ऐप के भीतर API के उपयोग को भी प्रदर्शित करता है|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## कोड
यहां - Bored-API ऐप लागू करने का तरीका बताया गया है:
```python
import streamlit as st
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी और ऐसी ही `requests` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
import requests
```

ऐप का टाइटल `st.title` के माध्यम से प्रदर्शित होता है:
```python
st.title('🏀 Bored API app')
```

इसके बाद, हम **गतिविधि प्रकार** पर यूज़र इनपुट को `st.selectbox` कमांड के माध्यम से स्वीकार करेंगे:
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

ऊपर वर्णित चयनित गतिविधि को फिर f-string के माध्यम से URL में जोड़ा जाता है, जिसका उपयोग परिणामी JSON डेटा को पुनः प्राप्त करने के लिए किया जाता है:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

यहां, हम `st.expander` कमांड के द्वारा ऐप और JSON डेटा के बारे में जानकारी प्रदर्शित करेंगे.
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

फिर हम इस प्रकार की सुझाई गई गतिविधि प्रदर्शित करेंगे:
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

अंत में, हम सुझाई गई गतिविधि की संलग्न जानकारी भी प्रदर्शित करेंगे, जैसे `Number of Participants`, `Type of Activity` और `Price`|
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [Bored API](http://www.boredapi.com/)
