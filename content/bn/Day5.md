# st.write

`st.write` স্ট্রিমলিট অ্যাপে টেক্সট এবং আর্গুমেন্ট লেখার অনুমতি দেয়।

পাঠ্য প্রদর্শন করতে সক্ষম হওয়ার পাশাপাশি, নিম্নলিখিতগুলি `st.write()` কমান্ডের মাধ্যমেও প্রদর্শিত হতে পারে:


- প্রিন্ট স্ট্রিং; `st.markdown()` এর মতো কাজ করে
- একটি পাইথন `dict` প্রদর্শন করে
- প্রদর্শন করে `pandas` ডেটাফ্রেমকে টেবিল হিসেবে প্রদর্শন করা যেতে পারে
- `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh` থেকে প্লট/গ্রাফ/চিত্র
- এবং আরও (দেখুন [এপিআই ডক্সে st.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## আমরা কি নির্মাণ করছি?

পাঠ্য, সংখ্যা, ডেটাফ্রেম এবং প্লট প্রদর্শনের জন্য `st.write()` কমান্ড কীভাবে ব্যবহার করতে হয় তার বিভিন্ন উপায় দেখানো একটি সাধারণ অ্যাপ।

## ডেমো অ্যাপ

স্থাপন করা স্ট্রিমলিট অ্যাপটি নীচের লিঙ্কে দেখানোর মতো দেখতে হবে:

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## কোড

এখানে কিভাবে st.write ব্যবহার করবেন:

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## লাইন-বাই-লাইন ব্যাখ্যা

একটি স্ট্রিমলিট অ্যাপ তৈরি করার সময় প্রথমেই যা করতে হবে তা হল `streamlit` লাইব্রেরিকে `st` এর মতো আমদানি করে শুরু করা:

```python
import streamlit as st
```

এটি অ্যাপের জন্য একটি শিরোনাম পাঠ্য তৈরি করে অনুসরণ করা হয়:

```python
st.header('st.write')
```

**উদাহরণ 1**
এর মৌলিক ব্যবহারের ক্ষেত্রে পাঠ্য এবং মার্কডাউন-ফরম্যাট করা পাঠ্য প্রদর্শন করা হয়:

```python
st.write('Hello, *World!* :sunglasses:')
```

**উদাহরণ 2**
উপরে উল্লিখিত হিসাবে, এটি অন্যান্য ডেটা বিন্যাস যেমন সংখ্যা প্রদর্শন করতে ব্যবহার করা যেতে পারে:

```python
st.write(1234)
```

**উদাহরণ ৩**
ডাটাফ্রেম এছাড়াও নিম্নলিখিত হিসাবে প্রদর্শিত হতে পারে:

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**উদাহরণ ৪**
আপনি একাধিক আর্গুমেন্ট পাস করতে পারেন:

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**উদাহরণ ৫**
অবশেষে, আপনি নিম্নরূপ একটি ভেরিয়েবলে পাস করে প্লটগুলিও প্রদর্শন করতে পারেন:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## ডেমো অ্যাপ

স্থাপন করা স্ট্রিমলিট অ্যাপটি নীচের লিঙ্কে দেখানোর মতো দেখতে হবে:

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## পরবর্তী পদক্ষেপ

এখন যেহেতু আপনি স্থানীয়ভাবে স্ট্রিমলিট অ্যাপ তৈরি করেছেন, এটিকে [স্ট্রীমলিট কমিউনিটি ক্লাউড](https://streamlit.io/cloud) এ স্থাপন করার সময় এসেছে যা একটি আসন্ন চ্যালেঞ্জে শীঘ্রই ব্যাখ্যা করা হবে।

কারণ এটি আপনার চ্যালেঞ্জের প্রথম সপ্তাহ, আমরা এই ওয়েবপৃষ্ঠার ভিতরেই সম্পূর্ণ কোড (উপরের কোড বক্সে দেখানো হয়েছে) এবং সমাধান (ডেমো অ্যাপ) প্রদান করি।

পরবর্তী চ্যালেঞ্জগুলিতে এগিয়ে যাওয়ার জন্য, আপনাকে প্রথমে Streamlit অ্যাপটি প্রয়োগ করার চেষ্টা করার পরামর্শ দেওয়া হচ্ছে।

আপনি আটকে গেলে চিন্তা করবেন না, আপনি সবসময় সমাধানটি উঁকি দিতে পারেন।

## আরও পড়া

[`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) ছাড়াও, আপনি পাঠ্য প্রদর্শনের অন্যান্য উপায়গুলি অন্বেষণ করতে পারেন:

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
