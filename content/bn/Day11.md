# st.multiselect

`st.multiselect` একটি মাল্টিসিলেক্ট উইজেট প্রদর্শন করে।

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/)

## কোড
চিন্তার কারণ নেই। এইভাবে ব্যবহার করুন `st.multiselect`:
```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

তারপর হেডার তৈরী করতে:
```python
st.header('st.multiselect')
```

তারপর `st.multiselect` উইজেট যা তিনটি অপ্শন দেখাবে, তার কোড এটি। ব্যবহারকারী তিনটির মধ্যে একটি রং বেছে নেবে।

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

অবশেষে, আমরা নির্বাচিত রং লিখব:
```python
st.write('You selected:', options)
```

## আরও পড়া
- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
