# st.form

`st.form` একটি ফর্ম তৈরি করে যা একটি "Submit" বাটন দিয়ে উপাদানগুলিকে ব্যাচ করে।

সাধারণত, যখনই একজন ব্যবহারকারী একটি উইজেটের সাথে ইন্টারঅ্যাক্ট করে, স্ট্রিমলিট অ্যাপটি পুনরায় চালু হয়।

একটি ফর্ম হল একটি ধারক যা দৃশ্যত অন্যান্য উপাদান এবং উইজেটগুলিকে একত্রে গোষ্ঠীবদ্ধ করে এবং একটি জমা বোতাম ধারণ করে৷ এখানে, একজন ব্যবহারকারী পুনঃরান না ঘটিয়ে এক বা একাধিক উইজেটের সাথে যতবার খুশি ততবার ইন্টারঅ্যাক্ট করতে পারে। অবশেষে, যখন ফর্মের জমা দেওয়ার বোতামটি চাপা হয়, তখন ফর্মের ভিতরের সমস্ত উইজেট মান একক ব্যাচে স্ট্রিমলিটে পাঠানো হবে।

একটি ফর্ম অবজেক্টে উপাদান যোগ করতে, আপনি `সহ` স্বরলিপি ব্যবহার করতে পারেন (পছন্দের) অথবা আপনি ফর্মে সরাসরি পদ্ধতিগুলি কল করে এটিকে অবজেক্ট নোটেশন হিসেবে ব্যবহার করতে পারেন (প্রথমে এটি একটি ভেরিয়েবলে বরাদ্দ করে এবং পরবর্তীতে স্ট্রিমলিট পদ্ধতি প্রয়োগ করে এটা)। উদাহরণ অ্যাপে দেখুন।

ফর্মের কিছু সীমাবদ্ধতা আছে:
- প্রতিটি ফর্মে অবশ্যই একটি `st.form_submit_button` থাকতে হবে।
- `st.button` এবং `st.download_button` কোনো ফর্মে যোগ করা যাবে না।
- ফর্মগুলি আপনার অ্যাপের যে কোনও জায়গায় (সাইডবার, কলাম, ইত্যাদি) প্রদর্শিত হতে পারে তবে সেগুলি অন্য ফর্মগুলির মধ্যে এম্বেড করা যাবে না৷

ফর্ম সম্পর্কে আরও তথ্যের জন্য দেখুন [ব্লগ পোস্ট](https://blog.streamlit.io/introducing-submit-button-and-forms/).

## ডেমো অ্যাপ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## কোড
এখানে কিভাবে `st.form` ব্যবহার করবেন:
```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা:
```python
import streamlit as st
```

এটি অ্যাপের জন্য একটি টাইটেল পাঠ্য তৈরি করে অনুসরণ করা হয়:
```python
st.title('st.form')
```

### প্রথম উদাহরণ
প্রথম উদাহরণ দিয়ে শুরু করা যাক, এখানে আমরা `st.form` কমান্ডটি `with` নোটেশনের মাধ্যমে প্রয়োগ করব। ফর্মের ভিতরে, আমরা একটি উপশিরোনাম লিখতে শুরু করব `আপনার কফি অর্ডার করুন` তারপর কফির অর্ডার সম্পর্কে তথ্য সংগ্রহ করতে বেশ কিছু ইনপুট উইজেট (`st.selectbox`, `st.select_slider` এবং `st.checkbox`) তৈরি করব। অবশেষে, `st.form_submit_button` কমান্ডের মাধ্যমে একটি সাবমিট বোতাম তৈরি করা হয়, যেটিতে ক্লিক করা হলে তা প্রক্রিয়াকরণের জন্য অ্যাপে তথ্যের একক ব্যাচ হিসাবে সমস্ত ব্যবহারকারীর ইনপুট পাঠাবে।
```python
# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
```

এরপরে, সাবমিট বোতামে ক্লিক করার পর কী ঘটবে তার যুক্তি যোগ করব। ডিফল্টরূপে, যখনই স্ট্রিমলিট অ্যাপটি লোড হবে তখনই `অন্য` বিবৃতিটি চালানো হবে এবং আমরা একটি বার্তা দেখতে পাব `☝️ আপনার অর্ডার দিন!`৷ যেখানে সাবমিট বোতামে ক্লিক করার পরে, বিভিন্ন উইজেটের মাধ্যমে সমস্ত ব্যবহারকারীর দেওয়া ইনপুট বিভিন্ন ভেরিয়েবলে সংরক্ষণ করা হয় (যেমন `coffee_bean_val`, `coffee_roast_val` ইত্যাদি) এবং f এর সাহায্যে `st.markdown` কমান্ডের মাধ্যমে প্রিন্ট আউট করা হয় f-string দিয়ে।

```python
if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')
```


### দ্বিতীয় উদাহরণ
এখন অবজেক্ট নোটেশন হিসেবে `st.form` ব্যবহার করার দ্বিতীয় উদাহরণে যাওয়া যাক। এখানে, `st.form` কমান্ডটি `form` ভেরিয়েবলে বরাদ্দ করা হয়েছে। পরবর্তীকালে, বিভিন্ন Streamlit কমান্ড যেমন `slider` বা `form_submit_button` `form` ভেরিয়েবলে প্রয়োগ করা হয়।
```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## আরও পড়া
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [স্ট্রিমলিট বাটন এবং ফর্ম](https://blog.streamlit.io/introducing-submit-button-and-forms/)
