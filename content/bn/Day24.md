# st.cache

`st.cache` আপনাকে আপনার Streamlit অ্যাপের কর্মক্ষমতা অপ্টিমাইজ করতে দেয়।

Streamlit একটি ক্যাশিং প্রক্রিয়া প্রদান করে যা ওয়েব থেকে ডেটা লোড করার সময়, বড় ডেটাসেটগুলিকে ম্যানিপুলেট করা বা ব্যয়বহুল গণনা করার সময়ও আপনার অ্যাপটিকে পারফরম্যান্ট থাকতে দেয়৷ এটি `@st.cache` ডেকোরেটর দিয়ে করা হয়।

আপনি যখন `@st.cache` ডেকোরেটর দিয়ে একটি ফাংশন চিহ্নিত করেন, তখন এটি স্ট্রিমলিটকে বলে যে যখনই ফাংশনটি বলা হয় তখন এটি কয়েকটি জিনিস পরীক্ষা করতে হবে:

১. ইনপুট পরামিতি যা দিয়ে আপনি ফাংশন কল করেছেন
২. ফাংশনে ব্যবহৃত যেকোনো বাহ্যিক চলকের মান
৩. ফাংশনের মূল অংশ
৪. ক্যাশড ফাংশনের ভিতরে ব্যবহৃত যেকোনো ফাংশনের বডি

যদি এই প্রথমবার স্ট্রিমলিট এই চারটি উপাদানকে এই সঠিক মানগুলির সাথে দেখে থাকে এবং এই সঠিক সংমিশ্রণ এবং ক্রমে, এটি ফাংশনটি চালায় এবং ফলাফলটিকে একটি স্থানীয় ক্যাশে সংরক্ষণ করে। তারপরে, পরের বার ক্যাশে করা ফাংশনটি কল করা হলে, যদি এই উপাদানগুলির কোনোটিই পরিবর্তিত না হয়, তবে স্ট্রিমলিট শুধুমাত্র ফাংশনটি সম্পূর্ণরূপে চালানো এড়িয়ে যাবে এবং পরিবর্তে, ক্যাশে পূর্বে সংরক্ষিত আউটপুটটি ফিরিয়ে দেবে।

স্ট্রিমলিট যেভাবে এই উপাদানগুলির পরিবর্তনগুলি ট্র্যাক রাখে তা হল হ্যাশিংয়ের মাধ্যমে৷ ক্যাশেটিকে একটি ইন-মেমরি কী-ভ্যালু স্টোর হিসাবে ভাবুন, যেখানে কীটি উপরের সমস্তটির একটি হ্যাশ এবং মানটি রেফারেন্স দ্বারা পাস করা প্রকৃত আউটপুট অবজেক্ট।

অবশেষে, `@st.cache` ক্যাশের আচরণ কনফিগার করতে আর্গুমেন্ট সমর্থন করে। আপনি আমাদের API রেফারেন্সে সেগুলি সম্পর্কে আরও তথ্য পেতে পারেন।

## কিভাবে ব্যবহার করে?

আপনি আপনার Streamlit অ্যাপে সংজ্ঞায়িত একটি কাস্টম ফাংশনের পূর্ববর্তী লাইনে সহজভাবে `st.cache` ডেকোরেটর যোগ করতে পারেন। নীচের উদাহরণ দেখুন। 

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/)

## কোড
এখানে কিভাবে `st.cache` ব্যবহার করবেন:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## লাইন-বাই-লাইন ব্যাখ্যা
স্ট্রিমলিট অ্যাপ তৈরী করার জন্য প্রথম জিনিসটি হলো `streamlit` লাইব্রেরি `st` হিসেবে ইম্পোর্ট করা এবং অন্নান্য লাইব্রেরি ইম্পোর্ট করা:
```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

এটি অ্যাপের জন্য একটি শিরোনাম পাঠ্য তৈরি করে অনুসরণ করা হয়:
```python
st.title('Streamlit Cache')
```

এর পরে, আমরা একটি বড় ডেটাফ্রেম তৈরি করার জন্য 2টি কাস্টম ফাংশন সংজ্ঞায়িত করব যেখানে প্রথমটি `st.cache` ডেকোরেটর ব্যবহার করে যখন দ্বিতীয়টি করে না:
```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

অবশেষে, আমরা কাস্টম ফাংশন চালাই যখন `time()` কমান্ড ব্যবহার করে রান টাইম টাইমিং করি।
```python
# Using cache
a0 = time()
st.subheader('Using st.cache')

# We insert the load_data_a function here

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

# We insert the load_data_b function here

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

লক্ষ্য করুন কিভাবে প্রথম রান মোটামুটি অনুরূপ রান টাইম প্রদান করতে পারে। অ্যাপটি পুনরায় লোড করুন এবং `st.cache` ডেকোরেটর ব্যবহার করার সময় কীভাবে রান টাইম পরিবর্তিত হয় তা লক্ষ্য করুন। আপনি কি কোন গতি বৃদ্ধি পর্যবেক্ষণ করেছেন?

## Further reading
- [`st.cache` API ডকুমেন্টেশন](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- [সঙ্গে কর্মক্ষমতা অপ্টিমাইজ করুন `st.cache`দিয়ে](https://docs.streamlit.io/library/advanced-features/caching)
- [পরীক্ষামূলক ক্যাশে](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)
