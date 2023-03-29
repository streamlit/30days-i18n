# st.checkbox

`st.checkbox` চেকবক্স উইজেট দেখায়।

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/)

## কোড
`st.checkbox` ব্যবহার করার জন্য:
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

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

তারপর হেডার তৈরী করতে:
```python
st.header('st.checkbox')
```

একটি প্রশ্ন জিজ্ঞাসা করুন `st.write' দ্বারা:
```python
st.write ('What would you like to order?')
```

আমরা তারপরে টিক দেওয়ার জন্য কিছু মেনু আইটেম সরবরাহ করতে যাচ্ছি:
```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

অবশেষে, কোন চেকবক্সে টিক দেওয়া হয়েছে তার উপর নির্ভর করে আমরা কাস্টম টেক্সট প্রিন্ট করতে যাচ্ছি:
```python
if icecream:
     st.write("Great! Here's some more 🍦")
    
if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
```  

## আরও পড়া
- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)
