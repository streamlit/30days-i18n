# st.line_chart

`st.line_chart` একটি লাইন চার্ট প্রদর্শন করে।

এটি `st.altair_chart` এর চারপাশে বানানো। প্রধান পার্থক্য হল এই কমান্ডটি চার্টের বৈশিষ্ট্য বের করতে ডেটার নিজস্ব কলাম এবং সূচক ব্যবহার করে। ফলস্বরূপ এটি অনেক "শুধু এই প্লট" পরিস্থিতিতে ব্যবহার করা সহজ, যদিও কম কাস্টমাইজযোগ্য।

যদি `st.line_chart` ডেটা স্পেসিফিকেশন সঠিকভাবে অনুমান না করে, তাহলে st.altair_chart ব্যবহার করে আপনার কাঙ্খিত চার্ট নির্দিষ্ট করার চেষ্টা করুন।

## আমরা কি নির্মাণ করছি?

একটি লাইন চার্ট প্রদর্শনের জন্য একটি সহজ অ্যাপ।

অ্যাপের প্রবাহ:
১. 'NumPy' এর মাধ্যমে এলোমেলোভাবে তৈরি হওয়া সংখ্যাগুলি থেকে একটি 'Pandas' ডেটাফ্রেম তৈরি করুন৷
২. `st.line_chart()` কমান্ডের মাধ্যমে লাইন চার্ট তৈরি করুন এবং প্রদর্শন করুন।

## ডেমো অ্যাপ

[![স্ট্রিমলিট অ্যাপ](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## কোড
এখানে কিভাবে ব্যবহার করবেন [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## লাইন-বাই-লাইন ব্যাখ্যা
একটি স্ট্রিমলিট অ্যাপ তৈরি করার সময় প্রথমেই যে কাজটি করতে হবে তা হল `স্ট্রিমলিট` লাইব্রেরিকে `st` হিসেবে ও অন্যান্য লাইব্রেরি ইম্পোর্ট করা:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

এর পরে, আমরা অ্যাপের জন্য একটি শিরোনাম পাঠ্য তৈরি করি:
```python
st.header('Line chart')
```

তারপর আমরা এলোমেলোভাবে তৈরি করা সংখ্যাগুলির একটি ডেটাফ্রেম তৈরি করি যাতে ৩টি কলাম থাকে।
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```


অবশেষে, ইনপুট ডেটা হিসাবে `chart_data` ভেরিয়েবলে সংরক্ষিত ডেটাফ্রেমের সাথে `st.line_chart()` ব্যবহার করে একটি লাইন চার্ট তৈরি করা হয়:
```python
st.line_chart(chart_data)
```

## আরও পড়া
নিম্নলিখিত সম্পর্কিত স্ট্রিমলিট  কমান্ড সম্পর্কে আরও পড়ুন যেটি থেকে [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) এর উপর ভিত্তি করে:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
