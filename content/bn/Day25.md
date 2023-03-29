# st.session_state

আমরা একটি অধিবেশন হিসাবে একটি ব্রাউজার ট্যাবে একটি স্ট্রিমলিট  অ্যাপ্লিকেশন অ্যাক্সেস করবো।  স্ট্রিমলিট সার্ভারের সাথে সংযোগকারী প্রতিটি ব্রাউজার ট্যাবের জন্য, একটি নতুন সেশন তৈরি করা হয়। আপনি যখনই আপনার অ্যাপের সাথে ইন্টারঅ্যাক্ট করেন তখনই স্ট্রিমলিট আপনার স্ক্রিপ্ট উপরে থেকে নীচে পুনরায় চালায়। প্রতিটি পুনঃরান একটি ফাঁকা স্লেটে সঞ্চালিত হয়: রানের মধ্যে কোন ভেরিয়েবল ভাগ করা হয় না।

সেশন স্টেট হল প্রতিটি ব্যবহারকারীর সেশনের জন্য রিরানগুলির মধ্যে ভেরিয়েবল শেয়ার করার একটি উপায়। স্টেট সঞ্চয় এবং স্থায়ী করার ক্ষমতা ছাড়াও, স্ট্রিমলিট কলব্যাক ব্যবহার করে স্টেট ম্যানিপুলেট করার ক্ষমতাও প্রকাশ করে।

এই টিউটোরিয়ালে, আমরা একটি ওজন রূপান্তর অ্যাপ তৈরি করার সময় সেশন স্টেট এবং কলব্যাকের ব্যবহার ব্যাখ্যা করব।

`st.session_state` একটি Streamlit অ্যাপে সেশন স্টেট বাস্তবায়নের অনুমতি দেয়।   

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/)

## কোড
এইভাবে ব্যবহার করুন `st.session_state`:
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

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

প্রথমত, আমরা অ্যাপটির শিরোনাম তৈরি করে শুরু করব:
```python
st.title('st.session_state')
```

এর পরে, আমরা পাউন্ড থেকে কেজি ওজন রূপান্তরের বা তার বিপরীত করার জন্য কাস্টম ফাংশন সংজ্ঞায়িত করি:
```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

এখানে, আমরা ওজন মানের সংখ্যাসূচক ইনপুট গ্রহণ করতে `st.number_input` ব্যবহার করি:
```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

উপরের 2টি কাস্টম ফাংশনগুলিকে 'st.number_input` কমান্ড ব্যবহার করে তৈরি করা নম্বর বাক্সে একটি সংখ্যাসূচক মান প্রবেশ করানো হবে। লক্ষ্য করুন কিভাবে `on_change` বিকল্পটি 2টি কাস্টম ফাংশন `lbs_to_kg` এবং `kg_to_lbs` নির্দিষ্ট করে।

সংক্ষেপে, `st.number_input` বাক্সে একটি সংখ্যা প্রবেশ করালে সংখ্যাটি এই কাস্টম ফাংশন দ্বারা রূপান্তরিত হয়।

পরিশেষে, `kg` এবং `lbs` ইউনিটের ওজনের মানগুলি সেশন স্টেটে `st.session_state.kg` এবং `st.session_state.lbs` হিসাবে সংরক্ষিত এর মাধ্যমে প্রিন্ট করা হবে
`st.write`:
```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## আরও পড়া
- [সেশন স্টেট](https://docs.streamlit.io/library/api-reference/session-state)
- [অ্যাপ্লিকেশানগুলিতে স্টেট যুক্ত করুন](https://docs.streamlit.io/library/advanced-features/session-state)
