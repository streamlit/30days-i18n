# st.experimental_get_query_params

`st.experimental_get_query_params` ব্যবহারকারীর ব্রাউজারের URL থেকে সরাসরি কোয়েরি প্যারামিটার পুনরুদ্ধারের অনুমতি দেয়।

## ডেমো অ্যাপ

১. নিচের লিঙ্কটি কোন কোয়েরি প্যারামিটার ছাড়াই ডেমো অ্যাপ লোড করে (ত্রুটির বার্তাটি লক্ষ্য করুন):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/)

২. নিম্নলিখিত লিঙ্কটি ডেমো অ্যাপটিকে কোয়েরি প্যারামিটার সহ লোড করে (এখানে কোনও ত্রুটি বার্তা নেই):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk)

## কোড
এখানে কিভাবে ব্যবহার করতে হয় `st.experimental_get_query_params`:
```python
import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

এর পরে, আমরা অ্যাপটিকে একটি শিরোনাম দেব:
```python
st.title('st.experimental_get_query_params')
```

এর একটি ড্রপ-ডাউন বক্সও যোগ করা যাক:
```python
with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

তারপর, আমরা অ্যাপের দর্শকদের সরাসরি URL-এ কোয়েরি প্যারামিটারগুলি কীভাবে পাস করতে পারে সে সম্পর্কে নির্দেশনা প্রদান করব:
```python
# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
```

পরবর্তীকালে, আমরা `st.experimental_get_query_params` কমান্ডের বিষয়বস্তু প্রদর্শন করব।
```python
# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

অবশেষে, আমরা URL এর ক্যোয়ারী প্যারামিটার থেকে নির্বাচনী তথ্য নির্বাচন করব এবং প্রদর্শন করব:
```python
# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## আরও পড়া
- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)
