# স্ট্রিমলিট অ্যাপের থিম কাস্টমাইজ করা

We can customize the theme by adjusting parameters in `config.toml`, which is a configuration file stored in the same folder as the app in the `.streamlit` folder.

## কি বানাচ্ছি আমরা?

একটি সাধারণ অ্যাপ যা থিম কাস্টমাইজ করে। This is made possible by customizing the  code inside the [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) এই ফাইলটির ভেতরে HTML HEX কোড পরিবর্তণ করে তা সম্ভব.

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## কোড
অ্যাপের কোড এইখানে [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py):
```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

কনফিগারেশন ফাইলের কোড এইখানে [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml):
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

তারপর অ্যাপের জন্য টাইটেল টেক্সট বানান:
```python
st.title('Theming with config.toml')
```

কনফিগারেশন ফাইল `.streamlit/config.toml` তার বিষয়বস্তু `st.write` দিয়ে দেখান এবং আসল কোডের জন্য `st.code` ব্যবহার করুন:
```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

অবশেষে, আমরা নির্বাচিত নম্বর প্রদর্শন করে সাইডবারে একটি স্লাইডার উইজেট তৈরি করছি:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

আসুন এখন আমরা এই অ্যাপটিতে ব্যবহার করেছি এমন কাস্টম রঙগুলি দেখে নেওয়া যাক `.streamlit/config.toml` কনফিগারেশন ফাইলে:
- `primaryColor="#F39C12"` - এটি প্রাথমিক রঙ কমলা সেট করে। স্লাইডার উইজেটে কমলা রঙগুলি লক্ষ্য করুন।
- `backgroundColor="#2E86C1"` - এটি পটভূমির রঙকে নীলে সেট করে। লক্ষ্য করুন মূল প্যানেলে একটি নীল পটভূমির রঙ রয়েছে।
- `secondaryBackgroundColor="#AED6F1"` - এটি সেকেন্ডারি পটভূমির রঙকে গাঢ় ধূসরে সেট করে। সাইডবারের ধূসর পটভূমির রঙ এবং প্রধান প্যানেলে কোড বক্সের পটভূমির রঙ লক্ষ্য করুন।
- `textColor="#FFFFFF"` - পাঠ্যের রঙ সাদাতে সেট করা হয়েছে।
- `font="monospace"` - এটি ফন্টটিকে মনোস্পেসে সেট করে।


## আরও পড়া
- [Theming](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML Color Codes](https://htmlcolorcodes.com/) আগ্রহের রং নির্বাচন করার জন্য একটি দুর্দান্ত হাতিয়ার।
