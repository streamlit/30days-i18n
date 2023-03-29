# st.experimental_get_query_params

`st.experimental_get_query_params` यूज़र के ब्राउज़र के URL से सीधे क्वेरी पैरामीटर को फिर से प्राप्त करने की अनुमति देता है!

## डेमो ऐप

1. निम्न लिंक डेमो ऐप को बिना किसी क्वेरी पैरामीटर के लोड करता है (त्रुटि संदेश देखें):

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/)

2. निम्न लिंक डेमो ऐप को क्वेरी पैरामीटर के साथ लोड करता है (यहां कोई त्रुटि संदेश नहीं है):

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk)

## कोड
यहां बताया गया है कि `st.experimental_get_query_params` का उपयोग कैसे करें:
```python
import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
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

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करना शुरू करना है:

```python
import streamlit as st
```

आगे, हम ऐप को एक शीर्षक देंगे:
```python
st.title('st.experimental_get_query_params')
```

आइए About ड्रॉप-डाउन बॉक्स भी जोड़ें:
```python
with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

फिर, हम ऐप के विज़िटर को निर्देश देंगे कि वे क्वेरी पैरामीटर को सीधे URL में कैसे पास कर सकते हैं:
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

इसके बाद, हम `st.experimental_get_query_params` कमांड की सामग्री प्रदर्शित करेंगे.
```python
# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

अंत में, हम URL के क्वेरी पैरामीटर से चयनात्मक जानकारी का चयन करेंगे और प्रदर्शित करेंगे:
```python
# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)
