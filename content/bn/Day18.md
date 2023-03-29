# st.file_uploader

`st.file_uploader` ফাইল দেখায় আপ্লোডার উইজেট দ্বারা। [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

গতানুগতিক ভাবে আপলোড করা ফাইল ২০০ MB পর্যন্ত সীমাবদ্ধ। আপনি server.maxUploadSize কনফিগার অপশন ব্যবহার করে এটি কনফিগার করতে পারেন। কনফিগার বিকল্পগুলি কীভাবে সেট করবেন সে সম্পর্কে আরও তথ্যের জন্য, দেখুন। [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## কোড
এইভাবে ব্যবহার করুন `st.file_uploader`:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা এবং অন্নান্য লাইব্রেরি ইম্পোর্ট করা:
```python
import streamlit as st
import pandas as pd
```

তারপর টাইটেল টেক্সট বানান:
```python
st.title('st.file_uploader')
```

এখন আমরা ব্যবহার করবো `st.file_uploader` ফাইল আপলোডার উইজেট দেখানোর জন্য যা নাকি ইউসার ইনপুট ফাইল নেয়:
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

অবশেষে, আমরা ব্যবহারকারীদের তাদের ফাইল আপলোড করার জন্য আমন্ত্রণ জানিয়ে একটি স্বাগত বার্তা প্রদর্শনের জন্য শর্তসাপেক্ষ বিবৃতি সংজ্ঞায়িত করি (`else` কন্ডিশনে বলা আছে). ফাইল আপলোড করার পর `if` স্টেটমেন্টসগুলো চালু হয় এবং CSV ফাইল `pandas` লাইব্রেরি দিয়ে পড়ে `st.write` দিয়ে দেখানো হয়।
```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## আরও পড়া
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [কনফিগারেশন বিকল্প সেট করুন](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
