# Streamlit ऐप्स की थीम को कस्टमाइज़ करना

हम `config.toml` में मापदंडों को समायोजित करके विषय को अनुकूलित कर सकते हैं, जो एक कॉन्फ़िगरेशन फ़ाइल है जो `.streamlit` फ़ोल्डर में ऐप के समान फ़ोल्डर में संग्रहीत है|

## हम क्या बना रहे हैं?

एक आसान ऐप जो हमारे थीम कस्टमाइज़ेशन का परिणाम दिखाता है|  यह [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) फ़ाइल के अंदर HTML HEX कोड को अनुकूलित करके संभव बनाया गया है|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/)

## कोड
यहाँ [`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py) फ़ाइल के लिए कोड है:
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

यहाँ [`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml) फ़ाइल के लिए कोड है:
```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
```

इसके बाद ऐप के लिए एक टाइटल टेक्स्ट बनाया जाता है:
```python
st.title('Theming with config.toml')
```
इसके बाद, हम `.streamlit/config.toml` फ़ाइल की सामग्री दिखाने जा रहे हैं, जिसे हम पहले `st.write` के माध्यम से एक नोट प्रदर्शित करेंगे, और उसके बाद, `st.code ` के माध्यम से वास्तविक कोड प्रदर्शित करेंगे| 

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

अंत में, हम साइडबार में एक स्लाइडर विजेट बना रहे हैं जिसके बाद चयनित संख्या प्रदर्शित होगी:
```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

आइए अब उन कस्टम रंगों पर एक नज़र डालते हैं जिनका हमने इस ऐप में उपयोग किया है, जो <15/> फ़ाइल में निर्दिष्ट है:
- `primaryColor="#F39C12"` - यह प्राथमिक रंग को नारंगी रंग में सेट करता है| स्लाइडर विजेट में नारंगी रंग पर ध्यान दें|
- `backgroundColor="#2E86C1"` - यह बैकग्राउंड का रंग नीला रंग में सेट करता है| ध्यान दें कि मुख्य पैनल का बैकग्राउंड रंग नीला है|
- `secondaryBackgroundColor="#AED6F1"` - यह सेकेंडरी बैकग्राउंड को डार्क ग्रे रंग में सेट करता है| मुख्य पैनल में साइडबार के ग्रे बैकग्राउंड रंग और कोड बॉक्स के बैकग्राउंड रंग पर ध्यान दें|
- `textColor="#FFFFFF"` - टेक्स्ट का रंग सफ़ेद पर सेट है|
- `font="monospace"` - यह फ़ॉन्ट को मोनोस्पेस पर सेट करता है|


## इस विषय से संबंधित कुछ और लिंक/लेख
- [थीमिंग](https://docs.streamlit.io/library/advanced-features/theming)
- [HTML रंग कोड](https://htmlcolorcodes.com/) आपकी पसंद के रंगों का चयन करने के लिए एक बेहतरीन टूल है|
