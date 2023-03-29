# বোর্ড এপিআই অ্যাপ তৈরি করে কীভাবে API ব্যবহার করবেন 

বোর্ড API অ্যাপটি আপনার জন্য মজাদার জিনিসগুলি প্রস্তাব করে যখন আপনি বিরক্ত হন!

টেকনিক্যালি, এটি একটি স্ট্রিমলিট অ্যাপের মধ্যে থেকে API-এর ব্যবহারও দেখায়।

## ডেমো অ্যাপ

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/)

## কোড
বোর্-API অ্যাপটি কীভাবে বাস্তবায়ন করবেন তা এখানে:
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


 
## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা এবং `requests` লাইব্রেরি ইম্পোর্ট করা:
```python
import streamlit as st
import requests
```

অ্যাপের শিরোনামটি `st.title` এর মাধ্যমে প্রদর্শিত হয়:
```python
st.title('🏀 Bored API app')
```

এরপর, আমরা `st.selectbox` কমান্ডের মাধ্যমে **অ্যাক্টিভিটি টাইপ**-এ ব্যবহারকারীর ইনপুট গ্রহণ করব:
```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

উপরে উল্লিখিত নির্বাচিত কার্যকলাপ তারপর একটি f-স্ট্রিং এর মাধ্যমে URL এ সংযুক্ত করা হয়, যা তারপর ফলাফল JSON ডেটা পুনরুদ্ধার করতে ব্যবহৃত হয়:
```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

এখানে, আমরা `st.expander` কমান্ডের মাধ্যমে অ্যাপ এবং JSON ডেটা সম্পর্কে তথ্য প্রদর্শন করব।
```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

তারপরে আমরা একটি প্রস্তাবিত কার্যকলাপ প্রদর্শন করব যেমন:
```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

অবশেষে, আমরা প্রস্তাবিত ক্রিয়াকলাপের সহগামী তথ্য যেমন `অংশগ্রহণকারীদের সংখ্যা`, `ক্রিয়াকলাপের প্রকার` এবং `মূল্য` প্রদর্শন করব।
```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## আরও পড়া
- [বোর্ড API](http://www.boredapi.com/)
