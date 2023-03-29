# st.latex

`st.latex` অংকের ফর্মুলা ল্যাটেক্স ব্যবহার করে দেখায়। 

## কি বানাচ্ছি আমরা?

একটি সহজ অ্যাপ যা LaTeX সিনট্যাক্স ব্যবহার করে একটি গাণিতিক সমীকরণ প্রদর্শন করে `st.latex` কমান্ড ব্যবহার করে।.

## ডেমো অ্যাপ
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## কোড
কিভাবে ব্যবহার করতে হয় `st.latex`:
```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

তারপর হেডার তৈরী করতে:
```python
st.header('st.latex')
```

অংকের ফর্মুলা `st.latex` দিয়ে দেখান:
```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## তথ্যসূত্র
- আরো পড়ুন [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) স্ট্রিমলিট API ডকুমেন্টেশনে।
