# st.latex

`st.latex` LaTeX के रूप में फ़ॉर्मेटेड मैथमेटिकल एक्स्प्रेशंस प्रदर्शित करें.

## हम क्या बना रहे हैं?

एक आसान ऐप जो `st.latex` कमांड के माध्यम से LaTeX सिंटैक्स का उपयोग करके एक मैथमेटिकल इक्वेश़न प्रदर्शित करता है.

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/)

## कोड

यहां बताया गया है कि `st.latex` का उपयोग कैसे करें:

```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इस तरह `st` से इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('st.latex')
```

आगे, हम मैथमेटिकल इक्वेश़न को `st.latex` के द्वारा प्रदर्शित कर रहे हैं:

```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## संदर्भ

- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex) के बारे में Streamlit API दस्तावेज़ीकरण में और पढ़ें.
