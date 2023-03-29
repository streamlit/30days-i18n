# st.progress

`st.progress` একটি অগ্রগতি বার প্রদর্শন করে যা পুনরাবৃত্তির অগ্রগতির সাথে সাথে গ্রাফিকভাবে আপডেট হয়।

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/)

## Code
এইভাবে ব্যবহার করুন `st.progress`:
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

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা। তার সাথে `time` লাইব্রেরি ইম্পোর্ট করা হয়েছে:
```python
import streamlit as st
import time
```

এর পরে, আমরা অ্যাপটির জন্য একটি শিরোনাম পাঠ্য তৈরি করি:
```python
st.title('st.progress')
```

একটি **সম্পর্কে বাক্স** তৈরি করা হয় `st.expander` ব্যবহার করে এবং বিবরণ `st.write` এর মাধ্যমে প্রদর্শিত হয়:
```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

অবশেষে, আমরা একটি অগ্রগতি বার সংজ্ঞায়িত করি এবং এটিকে `0` এর প্রারম্ভিক মান দিয়ে ইনস্ট্যান্টিয়েট করি। তারপর, একটি `for` লুপ `0` থেকে `100` এ পৌঁছানো পর্যন্ত পুনরাবৃত্তি করবে। প্রতিটি পুনরাবৃত্তিতে, আমরা `time.sleep(0.05)` ব্যবহার করি যাতে অ্যাপটিকে `my_bar` প্রগ্রেস বারে `1` এর মান যোগ করার আগে `0.05` এর জন্য অপেক্ষা করার অনুমতি দেওয়া হয় এবং এইভাবে বারের গ্রাফিকাল প্রদর্শন বৃদ্ধি পায় প্রতিটি পুনরাবৃত্তির সাথে।

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## আরও পড়া
- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)
