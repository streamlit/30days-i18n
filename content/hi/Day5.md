# st.write

`st.write` Streamlit ऐप में टेक्स्ट और तर्क लिखने देता है.

टेक्स्ट प्रदर्शित करने में सक्षम होने के अलावा, निम्नलिखित को `st.write()` कमांड के माध्यम से भी प्रदर्शित किया जा सकता है:


- स्ट्रिंग्स प्रिंट करता है; `st.markdown()` की तरह काम करता है
- एक Python `dict` प्रदर्शित करता है
- `pandas` प्रदर्शित करता है, DataFrame को टेबल के रूप में प्रदर्शित किया जा सकता है
- `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh` के प्लॉट/ग्राफ़/चित्र
- और बहुत कुछ ([API दस्तावेज़ पर `st.write` देखें](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## हम क्या बना रहे हैं?

टेक्स्ट, संख्या, DataFrames और प्लॉट प्रदर्शित करने के लिए `st.write()` कमांड का उपयोग करने के विभिन्न तरीकों को दिखाने वाला एक आसान ऐप.

## डेमो ऐप

डिप्लॉय किए गए Streamlit ऐप को नीचे दिए गए लिंक में दिखाए गए जैसा दिखना चाहिए:

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## कोड

`st.write` का उपयोग करने का तरीका यहां दिया गया है:

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

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को `st` के रूप में इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.write')
```

**उदाहरण 1**
इसकी मूल उपयोग स्थिति टेक्स्ट और मार्कडाउन-फ़ॉर्मेटेड टेक्स्ट प्रदर्शित करना है:


```python
st.write('Hello, *World!* :sunglasses:')
```

**उदाहरण 2**
जैसा कि ऊपर उल्लेख किया गया है, इसका उपयोग अन्य डेटा फ़ॉर्मेट जैसे संख्याओं को प्रदर्शित करने के लिए भी किया जा सकता है:

```python
st.write(1234)
```

**दाहरण 3**
DataFrames को निम्नानुसार भी प्रदर्शित किया जा सकता है:

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**उदाहरण 4**
आप कई तर्कों में पास कर सकते हैं:

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**उदाहरण 5**
अंत में, आप निम्न प्रकार से एक वेरिएबल में पास करके प्लॉट भी प्रदर्शित कर सकते हैं:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## डेमो ऐप

डिप्लॉय किए गए Streamlit ऐप को नीचे दिए गए लिंक में दिखाए गए जैसा दिखना चाहिए:

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## आगे के स्टेप्स

अब जब आपने Streamlit ऐप को स्थानीय रूप से बना लिया है, तो इसे [Streamlit Community Cloud](https://streamlit.io/cloud) पर डिप्लॉय करने का समय आ गया है, जैसा कि आगामी चैलेंज में जल्द ही समझाया जाएगा.

क्योंकि यह आपकी चैलेंज का पहला हफ़्ता है, हम इस वेबपेज के ठीक अंदर पूरा कोड (जैसा कि ऊपर कोड बॉक्स में दिखाया गया है) और समाधान (डेमो ऐप) प्रदान करते हैं.

अगले चैलेंज में आगे बढ़ते हुए, यह अनुशंसा की जाती है कि आप पहले खुद Streamlit ऐप को लागू करने का प्रयास करें.

अगर आप अटक जाते हैं तो चिंता न करें, आप कभी भी समाधान देख सकते हैं.

## Further reading

[`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write) के अलावा, आप टेक्स्ट प्रदर्शित करने के अन्य तरीकों का पता लगा सकते हैं:

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
