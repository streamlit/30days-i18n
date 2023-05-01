# Streamlit कंपोनेंट्स

कंपोनेंट्स थर्ड-पार्टी Python मॉड्यूल हैं, जो Streamlit [[1](https://docs.streamlit.io/library/components)] के साथ संभव है.

## कौन से Streamlit कंपोनेंट्स उपलब्ध हैं?

Streamlit की वेबसाइट पर कई दर्जनों Streamlit कंपोनेंट्स प्रदर्शित किए गए हैं [[2](https://streamlit.io/components)].

Fanilo (एक Streamlit क्रिएटर) ने wiki पोस्ट पर Streamlit कंपोनेंट्स की एक अद्भुत सूची को क्यूरेट किया है [[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)] जो अप्रैल 2022 तक लगभग 85 Streamlit कंपोनेंट्स को सूचीबद्ध करता है.


## कैसे इस्तेमाल करे?

Streamlit कंपोनेंट्स केवल एक पीआईपी-इंस्टाल दूर हैं.

इस ट्यूटोरियल में, चलिए आपको`streamlit_pandas_profiling` कंपोनेंट का उपयोग करना सिखाना शुरू करते हैं [[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)].

#### कंपोनेंट इंस्टाल करना

```bash
pip install streamlit_pandas_profiling
```

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/)

## कोड

यहां एक कंपोनेंट का उपयोग करके Streamlit ऐप बनाने का तरीका बताया गया है:

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी के जैसे ही `st` ऐप में इसी तरह इस्तेमाल की गई लाइब्रेरी के साथ-साथ अन्य लाइब्रेरी को इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
```

इसके बाद ऐप के लिए हेडर टेक्स्ट बनाया जाता है:

```python
st.header('`streamlit_pandas_profiling`')
```

इसके बाद, हम Penguins डेटासेट में `pandas` कमांड का `read_csv` उपयोग करके लोड करते हैं.

```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

अंत में, पांडाज़ प्रोफाइलिंग रिपोर्ट `profile_report()` कमांड के माध्यम से जेनरेट होती है और `st_profile_report` का उपयोग करके प्रदर्शित की जाती है:

```python
pr = ProfileReport(df, title="Profiling Report")
st_profile_report(pr)
```

## अपने खुद के कंपोनेंट्स बनाना

यदि आप अपना खुद का कंपोनेंट बनाने में रुचि रखते हैं, तो कृपया निम्नलिखित संसाधनों की जाँच करें:

- [कंपोनेंट बनाएँ](https://docs.streamlit.io/library/components/create)
- [कंपोनेंट प्रकाशित करें](https://docs.streamlit.io/library/components/publish)
- [कंपोनेंट्स API](https://docs.streamlit.io/library/components/components-api)
- [कंपोनेंट्स पर ब्लॉग पोस्ट](https://blog.streamlit.io/introducing-streamlit-components/)

वैकल्पिक रूप से, यदि आप वीडियो का उपयोग करना सीखना पसंद करते हैं, तो हमारे इंजीनियर टिम कॉंकलिंग ने कुछ अद्भुत ट्यूटोरियल तैयार किए हैं:

- [Streamlit कंपोनेंट कैसे बनाएं | भाग 1: सेटअप और आर्किटेक्च](https://youtu.be/BuD3gILJW-Q)
- [Streamlit कंपोनेंट कैसे बनाएं | भाग 2: भाग 2: एक स्लाइडर विजेट बनाएं](https://youtu.be/QjccJl_7Jco)

## कंपोनेंट्स से संबंधित कुछ और लिंक/लेख

1. [Streamlit कंपोनेंट्स - API दस्तावेज़ीकरण](https://docs.streamlit.io/library/components)
2. [फीचर्ड Streamlit कंपोनेंट्स](https://streamlit.io/components)
3. [Streamlit कंपोनेंट्स - कम्युनिटी ट्रैकर](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)
