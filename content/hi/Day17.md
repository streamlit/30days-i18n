# st.secrets

`st.secrets` आपको API की, डेटाबेस पासवर्ड या अन्य यूज़रनेम और पासवर्ड जैसी गोपनीय जानकारी संग्रहीत करने की अनुमति देता है|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## कोड
यहां बताया गया है कि <3/> का उपयोग कैसे करें:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
```

इसके बाद ऐप के लिए एक टाइटल टेक्स्ट बनाया जाता है:
```python
st.title('st.secrets')
```

अंत में, हम स्टोर किए गए सीक्रेट प्रदर्शित करेंगे:
```python
st.write(st.secrets['message'])
```

यह ध्यान दिया जाना चाहिए कि, जैसे कि नीचे दिखाए गए स्क्रीनशॉट में दिखाया गया है, सीक्रेट को Streamlit Cloud में स्टोर किया जा सकता है|

यदि स्थानीय रूप से काम कर रहे हैं, तो उन्हें `.streamlit/secrets.toml` में स्टोर किया जा सकता है, लेकिन ऐप को डिप्लॉय करते समय इस फाइल को  GitHub रेपो में अपलोड न करना ध्यान में रखें|

## Further reading
- [अपने Streamlit ऐप्स में सीक्रेट जोड़ें](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [सीक्रेट्स मैनेजमेंट](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
