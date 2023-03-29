# st.slider

`st.slider` একটি স্লাইডার ইনপুট উইজেট প্রদর্শনের অনুমতি দেয়।

নিম্নলিখিত ডেটা প্রকারগুলি সমর্থিত: int, float, date, time, এবং datetime.

## আমরা কি নির্মাণ করছি?

একটি সাধারণ অ্যাপ যা স্লাইডার উইজেট সামঞ্জস্য করে ব্যবহারকারীর ইনপুট গ্রহণ করার বিভিন্ন উপায় দেখায়।

অ্যাপের প্রবাহ:
1. ব্যবহারকারী স্লাইডার উইজেট সামঞ্জস্য করে মান নির্বাচন করে
2. অ্যাপ নির্বাচিত মান প্রিন্ট করে

## ডেমো অ্যাপ

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/)


## কোড
এখানে কিভাবে st.slider ব্যবহার করবেন:

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

## লাইন-বাই-লাইন ব্যাখ্যা
একটি স্ট্রিমলিট অ্যাপ তৈরি করার সময় প্রথমেই যা করতে হবে তা হল `স্ট্রিমলিট` লাইব্রেরিকে `st` হিসেবে ইম্পোর্ট করা: 
```python
import streamlit as st
from datetime import time, datetime
```

এটি অ্যাপের জন্য একটি শিরোনাম পাঠ্য তৈরি করে অনুসরণ করা হয়:
```python
st.header('st.slider')
```

**উদাহরণ 1**

স্লাইডার:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

আমরা দেখতে পাচ্ছি, `st.slider()` কমান্ড
ব্যবহারকারীদের বয়স সম্পর্কে ব্যবহারকারীর ইনপুট সংগ্রহ করতে ব্যবহৃত হয়।

প্রথম ইনপুট আর্গুমেন্টটি **স্লাইডার** উইজেটের ঠিক উপরে লেখাটি প্রদর্শন করে যা জিজ্ঞেস করে `'আপনার বয়স কত?'`।

নিম্নলিখিত তিনটি পূর্ণসংখ্যা `০, ১৩০, ২৫` যথাক্রমে সর্বনিম্ন, সর্বোচ্চ এবং ডিফল্ট মানগুলিকে উপস্থাপন করে।

**উদাহরণ ২**

রেঞ্জ স্লাইডার:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

পরিসীমা স্লাইডার একটি নিম্ন এবং উপরের আবদ্ধ মান জোড়া নির্বাচন করার অনুমতি দেয়।

প্রথম ইনপুট আর্গুমেন্টটি **রেঞ্জ স্লাইডার** উইজেটের ঠিক উপরে লেখাটি প্রদর্শন করে যা জিজ্ঞাসা করে `'মানগুলির একটি পরিসর নির্বাচন করুন'`।

নিম্নলিখিত তিনটি আর্গুমেন্ট `০.০ , ১০০.০ , (২৫.০ , ৭৫.০)` ন্যূনতম এবং সর্বাধিক মানগুলিকে উপস্থাপন করে যখন শেষ টিপলটি নির্বাচিত নিম্ন (25.0) এবং উপরের (75.0) আবদ্ধ মান হিসাবে ব্যবহার করার জন্য ডিফল্ট মানগুলিকে নির্দেশ করে৷

**উদাহরণ ৩**

পরিসীমা সময় স্লাইডার:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

রেঞ্জ টাইম স্লাইডার ডেটটাইমের একটি নিম্ন এবং উপরের আবদ্ধ মান জোড়া নির্বাচন করার অনুমতি দেয়।

প্রথম ইনপুট আর্গুমেন্ট **রেঞ্জ টাইম স্লাইডার** উইজেটের ঠিক উপরে টেক্সট প্রদর্শন করে যা জিজ্ঞেস করে `'আপনার অ্যাপয়েন্টমেন্টের সময় নির্ধারণ করুন:'।

ডেটটাইমের নিম্ন এবং উপরের আবদ্ধ মান জোড়ার জন্য ডিফল্ট মান যথাক্রমে ১১:৩০ এবং ১২:৪৫ সেট করা হয়েছে।

**উদাহরণ ৪**

তারিখ সময় স্লাইডার:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

তারিখের সময় স্লাইডার একটি তারিখ সময় নির্বাচন করার অনুমতি দেয়।

প্রথম ইনপুট আর্গুমেন্ট **datetime** স্লাইডার উইজেটের ঠিক উপরে পাঠ্য প্রদর্শন করে যা জিজ্ঞাসা করে `'আপনি কখন শুরু করবেন?'`।

তারিখ সময়ের জন্য ডিফল্ট `মান` বিকল্প ব্যবহার করে ১ জানুয়ারী, ২০২০ ৯:৩০ এ সেট করা হয়েছিল

## আরও পড়া
এছাড়াও আপনি নিম্নলিখিত সম্পর্কিত উইজেট অন্বেষণ করতে পারেন:
- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)

