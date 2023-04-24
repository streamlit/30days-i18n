# Bored APIアプリを構築してAPIを使用する方法

Bored APIアプリは、退屈なときに楽しいことを提案してくれるアプリです。

技術的には、Streamlitアプリ内からAPIを使用する方法についても説明します。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/bored-api-app/ "Streamlitアプリ")

## コード

Bored-APIアプリの実装方法は次のとおりです。

```python
import streamlit as st
import requests

st.title('?? Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
    
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、`requests`ライブラリもインポートします。

```python
import streamlit as st
import requests
```

アプリのタイトルは`st.title`で表示されます。

```python
st.title('?? Bored API app')
```

次に、`st.selectbox`コマンドによって、**アクティビティタイプ**に関するユーザー入力を受け入れます。

```python
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
```

上記で選択されたアクティビティは、f-stringによってURLに追加され、結果のJSONデータを取得するために使用されます。

```python
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
```

ここでは、`st.expander`コマンドを使用して、アプリとJSONデータの情報を表示します。

```python
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)
```

次に、提案するアクティビティを次のように表示します。

```python
st.header('Suggested activity')
st.info(suggested_activity['activity'])
```

最後に、`Number of Participants`、`Type of Activity`、`Price`など、提案するアクティビティの付随情報も表示します。

```python
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
```

## 参考文献

- [Bored API](http://www.boredapi.com/)