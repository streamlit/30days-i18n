# अपने Streamlit ऐप को कैसे लेआउट करें

इस ट्यूटोरियल में, हम अपने Streamlit ऐप को लेआउट करने के लिए निम्न कमांड का उपयोग करने जा रहे हैं:
- `st.set_page_config(layout="wide")` - ऐप की सामग्री को वाइड मोड में प्रदर्शित करता है (अन्यथा डिफ़ॉल्ट रूप से, सामग्री एक निश्चित चौड़ाई वाले बॉक्स में एनकैप्सुलेटेड होती है|
- `st.sidebar` - साइडबार में प्रदर्शित विजेट्स या टेक्स्ट/इमेज को रखता है|
- `st.expander` - एक कोलैप्सिबल कंटेनर बॉक्स के अंदर प्रदर्शित टेक्स्ट/इमेज को रखता है|
- `st.columns` - एक सारणीबद्ध स्थान (या कॉलम) बनाएँ जिसके अंदर सामग्री को रखा जा सके|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/)

## कोड
यहां अपने Streamlit ऐप के लेआउट को कस्टमाइज़ करने का तरीका बताया गया है:
```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
```

हम पहले `widw` मोड में प्रदर्शित होने वाले पेज लेआउट को परिभाषित करके शुरू करेंगे, जो पेज की सामग्री को ब्राउज़र की चौड़ाई तक विस्तारित करने की अनुमति देता है.
```python
st.set_page_config(layout="wide")
```

आगे, हम Streamlit ऐप को एक टाइटल देंगे.
```python
st.title('How to layout your Streamlit app')
```

`About this app` टाइटल वाला एक विस्तार योग्य बॉक्स ऐप टाइटल के नीचे रखा गया है| विस्तार करने पर, हम अंदर अतिरिक्त विवरण देखेंगे|
```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

यूज़र इनपुट को स्वीकार करने के लिए इनपुट विजेट्स को साइडबार में रखा गया है जैसा कि Streamlit कमांड्स `st.sidebar` और `text_input` से पहले `selectbox` कमांड का उपयोग करके निर्दिष्ट किया गया है| यूज़र द्वारा दर्ज किए गए या चुने गए इनपुट मान `user_name`, `user_emoji` और `user_food` वेरिएबल्स में असाइन किए जाते हैं और संग्रहीत किए जाते हैं|
```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

Finally, we'll create 3 columns using the `st.columns` command which corresponds to `col1`, `col2` and `col3`. Then, we assign contents to each of the column by creating individual code blocks starting with the `with` statement. Underneath this, we create conditional statements that display 1 of 2 alternative text depending on whether the user had provided their input data (specified in the sidebar) or not. By default, the page displays text under the `else` statement. Upon providing user input, the corresponding information that the user gives to the app is displayed under the `Output` header text.
अंत में, हम `st.columns` कमांड का उपयोग करके 3 कॉलम बनाएंगे जो `col1`, `col2` और `col3` से संबंधित है| फिर, हम `with` स्टेटमेंट के साथ शुरू होने वाले अलग-अलग कोड ब्लॉक बनाकर प्रत्येक कॉलम में सामग्री असाइन करते हैं| इसके नीचे, हम कंडिशनल स्टेटमेंट बनाते हैं जो इस आधार पर 2 में से 1 वैकल्पिक टेक्स्ट प्रदर्शित करते हैं कि यूज़र ने अपना इनपुट डेटा (साइडबार में निर्दिष्ट) प्रदान किया था या नहीं| डिफ़ॉल्ट रूप से, पेज <21/> स्टेटमेंट के तहत टेक्स्ट प्रदर्शित करता है| यूज़र इनपुट प्रदान करने पर, यूज़र द्वारा ऐप को दी जाने वाली संबंधित जानकारी <22/> हेडर टेक्स्ट के तहत प्रदर्शित होती है|

```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```
यह भी ध्यान देने योग्य है कि यूज़र द्वारा प्रदान किए गए मानों के साथ प्री-केन्नड टेक्स्ट को संयोजित करने के लिए <23/> स्ट्रिंग्स का उपयोग किया गया था|

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [लेआउट और कंटेनर](https://docs.streamlit.io/library/api-reference/layout)
