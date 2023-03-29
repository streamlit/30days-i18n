# st.line_chart

`st.line_chart` एक लाइन चार्ट प्रदर्शित करता है.

यह सिंटैक्स-सूगर के आसपास है `st.altair_chart`. मुख्य अंतर यह है कि यह कमांड चार्ट की विशिष्टता का पता लगाने के लिए डेटा के अपने कॉलम और इंडेक्स का उपयोग करता है. नतीजतन, कम अनुकूलन योग्य होने के बावजूद, "बस इसे प्लॉट करें" परिदृश्यों के लिए इसका उपयोग करना आसान है.

यदि `st.line_chart` डेटा विशिष्टता का सही अनुमान नहीं लगाता है, तो st.altair_chart का उपयोग करके अपने इच्छित चार्ट को निर्दिष्ट करने का प्रयास करें.

## हम क्या बना रहे हैं?

लाइन चार्ट प्रदर्शित करने के लिए एक सरल ऐप.

ऐप का फ़्लो:
1. `NumPy` के माध्यम से रैंडम रूप से जेनरेट की गई संख्याओं से एक `Pandas` DataFrame बनाएं.
2. `st.line_chart()` कमांड के जरिए लाइन चार्ट बनाएं और प्रदर्शित करें.

## डेमो ऐप

[![Streamlit ऐप](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## कोड
यहां बताया गया है कि [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) का उपयोग कैसे करें:

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

## लाइन-बाय-लाइन स्पष्टीकरण

Streamlit ऐप बनाते समय सबसे पहली बात यह है कि `streamlit` लाइब्रेरी के जैसे ही `st` साथ-साथ अन्य लाइब्रेरी को इम्पोर्ट करके शुरू करना है:

```python
import streamlit as st
import pandas as pd
import numpy as np
```

इसके बाद, हम ऐप के लिए एक हेडर टेक्स्ट बनाते हैं:

```python
st.header('Line chart')
```

फिर, हम रैंडम रूप से जेनरेट की गई संख्याओं का DataFrame बनाते हैं, जिसमें 3 कॉलम होते हैं.

```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

अंत में, इनपुट डेटा के रूप में `chart_data` वेरिएबल में संग्रहीत DataFrame के साथ `st.line_chart()` का उपयोग करके एक लाइन चार्ट बनाया जाता है:

```python
st.line_chart(chart_data)
```

## इसी विषय से जुड़े कुछ और लिंक/लेख

निम्नलिखित संबंधित Streamlit कमांड के बारे में और पढ़ें, जिस पर [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) आधारित है:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
