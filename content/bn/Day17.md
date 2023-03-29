# st.secrets

`st.secrets` গোপনীয় তথ্য যেমন  API keys, database passwords বা অন্যান্য গুরুত্বপূর্ণ তথ্য।

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## কোড
এইভাবে ব্যবহার করুন `st.secrets`:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

তারপর টাইটেল টেক্সট বানান:
```python
st.title('st.secrets')
```

অবশেষে, আমরা সঞ্চিত গোপনীয়তা প্রদর্শন করব:
```python
st.write(st.secrets['message'])
```

এটি উল্লেখ করা উচিত যে, নীচে দেখানো স্ক্রিনশটগুলিতে দেখানো হিসাবে স্ট্রিমলিট কমিউনিটি ক্লাউডে গোপনীয়তাগুলি সংরক্ষণ করা যেতে পারে।

স্থানীয়ভাবে কাজ করলে তথ্যগুলো `.streamlit/secrets.toml` এইখানে রাখুন , কিন্তু মনে রাখবেন যে গিটহাব রেপোতে ডিপ্লয় করার সময় এই ফাইলটি আপলোড করবেন না। 

## আরও পড়া
- [আপনার স্ট্রিমলিট অ্যাপে গোপনীয়তা যোগ করুন](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [গোপন ব্যবস্থাপনা](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
