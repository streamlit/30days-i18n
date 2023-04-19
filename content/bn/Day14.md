# Streamlit Components

উপাদানগুলি হল তৃতীয় পক্ষের পাইথন মডিউল যা স্ট্রিমলিটের সাথে যা সম্ভব তা প্রসারিত করে [[1](https://docs.streamlit.io/library/components)]।

## কি স্ট্রিমলিট উপাদান পাওয়া যায়?

স্ট্রিমলিটের ওয়েবসাইটে বেশ কয়েক ডজন স্ট্রিমলিট উপাদান রয়েছে [[2](https://streamlit.io/components)].

ফ্যানিলোর উইকি দেখতে পারেন যেখানে প্রায় ৮৫টি উপাদান আছে [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]।  

## কিভাবে ব্যবহার করে?

স্ট্রিমলিট উপাদানগুলি কেবল একটি পিপ-ইনস্টল দূরে।

এই টিউটোরিয়ালে `streamlit_pandas_profiling` উপাদান দেখতে পারেন [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### কম্পোনেন্ট ইনস্টল করুন

```bash
pip install streamlit_pandas_profiling
```

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## কোড
একটি উপাদান ব্যবহার করে একটি স্ট্রিমলিট অ্যাপ কীভাবে তৈরি করবেন তা এখানে:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা এবং অন্নান্য লাইব্রেরি ইম্পোর্ট করা:
```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

তারপর হেডার টেক্সট বানান:
```python
st.header('`streamlit_pandas_profiling`')
```

হেডার বানানোর পর পেঙ্গুইনস ডাটাসেট লোড করুন `read_csv` ব্যবহার করে যা `pandas` লাইব্রেরিতে পাওয়া যায়। .
```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

পান্ডার `profile_report()` কমান্ড দিয়ে প্রোফাইল রিপোর্ট তৈরী করুন এবং দেখানোর জন্য এই কমান্ডটি `st_profile_report`:
```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## আপনার নিজস্ব উপাদান তৈরি

আপনি যদি নিজের উপাদান তৈরি করতে আগ্রহী হন, অনুগ্রহ করে নিম্নলিখিত সংস্থানগুলি দেখুন:
- [Create a Component](https://docs.streamlit.io/library/components/create)
- [Publish a Component](https://docs.streamlit.io/library/components/publish)
- [Components API](https://docs.streamlit.io/library/components/components-api)
- [Blog post on Components](https://blog.streamlit.io/introducing-streamlit-components/)

বিকল্পভাবে, আপনি যদি ভিডিও ব্যবহার করে শিখতে পছন্দ করেন, আমাদের প্রকৌশলী টিম কনক্লিং কিছু আশ্চর্যজনক টিউটোরিয়াল একত্র করেছেন:
- [How to build a Streamlit component | Part 1: Setup and Architecture](https://youtu.be/BuD3gILJW-Q)
- [How to build a Streamlit component | Part 2: Part 2: Make a Slider Widget](https://youtu.be/QjccJl_7Jco)

## উপাদান সম্পর্কে আরও পড়া
1. [Streamlit Components - API Documentation](https://docs.streamlit.io/library/components)
2. [Featured Streamlit Components](https://streamlit.io/components)
3. [Streamlit Components - Community Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
