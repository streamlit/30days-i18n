# st.selectbox

`st.selectbox` একটি নির্বাচিত উইজেট প্রদর্শনের অনুমতি দেয়।

## কি তৈরী করছি আমরা?

একটি সাধারণ অ্যাপ যা ব্যবহারকারীকে জিজ্ঞাসা করে তাদের প্রিয় রঙ কী।

অ্যাপের প্রবাহ:
1. ব্যবহারকারী একটি রঙ নির্বাচন করে
2. অ্যাপ নির্বাচিত রঙ প্রিন্ট করে

## ডেমো অ্যাপ
স্থাপন করা স্ট্রিমলিট অ্যাপটি নীচের লিঙ্কে দেখানোর মতো দেখতে হবে:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/)

## কোড
উপরে উল্লিখিত অ্যাপটি বাস্তবায়ন করার কোড এখানে:
```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## লাইন-বাই-লাইন ব্যাখ্যা 
একটি স্ট্রিমলিট অ্যাপ তৈরি করার সময় প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ব্যবহার করা:
```python
import streamlit as st
```

অ্যাপ হেডার তৈরী করার জন্য:
```python
st.header('st.selectbox')
```

তারপর `option` নামের ভ্যারিয়েবল তৈরী করুন যেটা ব্যবহারকারী থেকে ইনপুট নেবে **select** ইনপুট উইজেট দ্বারা `st.selectbox()` কমান্ডের সাথে।

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```
আমরা দেখতে পাচ্ছি যে `st.selectbox()` কমান্ড ২টি আর্গুমেণ্ট নিচ্ছে:
1. যে টেক্সটটি সিলেক্ট উইজেটের উপরে যায়, যা নাকি `'আপনার প্রিয় রং কি?'`
2. এই অপ্শন গুলি বাছা যেতে পারে `('নীল', 'লাল', 'সবুজ')`

অবশেষে, আমরা নির্বাচিত রঙটি নিম্নরূপ প্রিন্ট আউট করব:
```python
st.write('Your favorite color is ', option)
```

## পরবর্তী পদক্ষেপ
এখন আপনি স্থানীয়ভাবে স্ট্রিমলিট অ্যাপ তৈরি করেছেন, এটি এটি স্থাপন করার সময় [Streamlit Community Cloud](https://streamlit.io/cloud).

## তথ্যসূত্র
আরো দেখুন [`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)
