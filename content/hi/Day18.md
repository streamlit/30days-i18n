# st.file_uploader

`st.file_uploader` फ़ाइल अपलोडर विजेट [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)] प्रदर्शित करता है|

डिफ़ॉल्ट रूप से, अपलोड की गई फ़ाइलें 200MB तक सीमित हैं|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

## कोड
यहां बताया गया है कि `st.file_uploader` का उपयोग कैसे करें:
```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि <6/> लाइब्रेरी और अन्य आवश्यक लाइब्रेरी के रूप में इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
import pandas as pd
```

इसके बाद ऐप के लिए एक टाइटल टेक्स्ट बनाया जाता है:
```python
st.title('st.file_uploader')
```

Next, we'll use `st.file_uploader` to display a file uploader widget for accepting user input file:
अगला, हम यूज़र इनपुट फ़ाइल को स्वीकार करने के लिए फ़ाइल अपलोडर विजेट प्रदर्शित करने के लिए `st.file_uploader` का उपयोग करेंगे:
```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

अंत में, हम यूज़र को अपनी फ़ाइल अपलोड करने के लिए आमंत्रित करते हुए एक स्वागत संदेश प्रदर्शित करने के लिए कंडिशनल स्टेटमेंट को परिभाषित करते हैं (जैसा कि `else` कंडीशन में लागू किया गया है)| फ़ाइल अपलोड होने पर, `if` स्टेटमेंट्स सक्रिय हो जाते हैं और CSV फ़ाइल को `pandas` लाइब्रेरी द्वारा पढ़ा जाता है और `st.write` कमांड के माध्यम से प्रदर्शित किया जाता है|

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## इसी विषय से जुड़े कुछ और लिंक/लेख

1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [कॉन्फ़िगरेशन विकल्प सेट करें](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
