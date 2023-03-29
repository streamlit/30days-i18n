# st.form

`st.form` एक फ़ॉर्म बनाता है जो "सबमिट" बटन के साथ एलिमेंट को एक साथ बैच करता है|

आमतौर पर, जब भी कोई यूज़र किसी विजेट के साथ इंटरैक्ट करता है, तो Streamlit ऐप फिर से चालू हो जाता है|

फ़ॉर्म एक कंटेनर है जो विज़ुअल रूप से अन्य एलिमेंट्स और विजेट्स को एक साथ समूहित करता है और इसमें एक सबमिट बटन होता है|
इसमें, एक यूज़र एक या एक से अधिक विजेट्स के साथ जितनी बार चाहें उतनी बार इंटरैक्ट कर सकता है बिना दोबारा चलाए|
अंत में, जब फ़ॉर्म का सबमिट बटन दबाया जाता है, तो फ़ॉर्म के अंदर सभी विजेट मान एक ही बैच में Streamlit को भेजे जाएंगे.

फ़ॉर्म ऑब्जेक्ट में एलिमेंट्स जोड़ने के लिए, आप  `with` नोटेशन (पसंदीदा) का उपयोग कर सकते हैं या आप इसे ऑब्जेक्ट नोटेशन के रूप में सीधे फ़ॉर्म पर सीधे कॉल करके उपयोग कर सकते हैं (पहले इसे एक वेरिएबल पर असाइन करके और बाद में उस पर Streamlit तरीके लागू करके)|
उदाहरण ऐप में देखें|

फ़ॉर्म में कुछ प्रतिबंध हैं:
- हर फ़ॉर्म में एक `st.form_submit_button` होना चाहिए|
- `st.button` और  `st.download_button` को फ़ॉर्म में नहीं जोड़ा जा सकता है|
- फ़ॉर्म आपके ऐप (साइडबार, कॉलम आदि) में कहीं भी दिखाई दे सकते हैं, लेकिन उन्हें अन्य फ़ॉर्म के अंदर एम्बेड नहीं किया जा सकता है|

फ़ॉर्म के बारे में अधिक जानकारी के लिए, हमारे [ब्लॉग पोस्ट](https://blog.streamlit.io/introducing-submit-button-and-forms/) को देखें|

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/)

## कोड
यहां बताया गया है कि `st.form` का उपयोग कैसे करें:
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

## लाइन-बाय-लाइन स्पष्टीकरण
Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी को इम्पोर्ट करके शुरू करना है:
```python
import streamlit as st
```

इसके बाद ऐप के लिए एक टाइटल टेक्स्ट बनाया जाता है:
```python
st.title('st.form')
```

### पहला उदाहरण
आइए पहले उदाहरण से शुरू करते हैं, यहां हम `st.form` कमांड को `with` नोटेशन के माध्यम से लागू करेंगे|
फ़ॉर्म के अंदर, हम एक सबहेडर `Order your coffee` लिखने के साथ शुरू करेंगे, फिर कॉफ़ी ऑर्डर के बारे में जानकारी एकत्र करने के लिए कई इनपुट विजेट (`st.selectbox`, `st.select_slider` aऔरnd `st.checkbox`) बनाएंगे|
अंत में, `st.form_submit_button` कमांड के माध्यम से एक सबमिट बटन बनाया जाता है, जिस पर क्लिक करने पर सभी यूज़र इनपुट प्रोसेसिंग के लिए ऐप को जानकारी के एक बैच के रूप में भेज देंगे|

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

इसके बाद, हम तर्क जोड़ेंगे कि सबमिट बटन पर क्लिक करने के बाद क्या होता है| डिफ़ॉल्ट रूप से, जब भी Streamlit ऐप लोड होता है तो `else` स्टेटमेंट चलाया जाएगा और हमें एक संदेश `☝️ Place your order!` दिखाई देगा| जबकि सबमिट बटन पर क्लिक करने पर, विभिन्न विजेट्स के माध्यम से प्रदान किए गए सभी यूज़र इनपुट कई वेरिएबल्स (जैसे, `coffee_bean_val, `coffee_roast_val`, आदि) में संग्रहीत होते हैं और f-string की मदद से `st.markdown` कमांड के माध्यम से प्रिंट किए जाते हैं|
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


### दूसरा उदाहरण
चलिए अब दूसरे उदाहरण की ओर बढ़ते हैं जिसमें `st.form` को ऑब्जेक्ट नोटेशन के रूप में प्रयोग किया जाता है|
यहां, `st.form` कमांड को `form` वेरिएबल को असाइन किया गया है|
इसके बाद, विभिन्न Streamlit कमांड जैसे `slider` या `form_submit_button` को `form` वेरिएबल पर लागू किया जाता है.

```python
# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## इसी विषय से जुड़े कुछ और लिंक/लेख
- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [>पेश है सबमिट करें बटन और फ़ॉर्म](https://blog.streamlit.io/introducing-submit-button-and-forms/)
