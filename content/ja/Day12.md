# st.checkbox

`st.checkbox`は、チェックボックスウィジェットを表示します。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.checkbox/ "Streamlitアプリ")

## コード

`st.checkbox`の使い方は次のとおりです。

```python
import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more ??")
    
if coffee: 
     st.write("Okay, here's some coffee ?")

if cola:
     st.write("Here you go ??")
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.checkbox')
```

次に、\`st.write'を使って質問します。

```python
st.write ('What would you like to order?')
```

次に、チェックするメニュー項目をいくつか用意します。

```python
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
```

最後に、どのチェックボックスをチェックしたかによって、カスタムテキストを出力します。

```python
if icecream:
     st.write("Great! Here's some more ??")
    
if coffee: 
     st.write("Okay, here's some coffee ?")

if cola:
     st.write("Here you go ??")
```

## 参考文献

- [`st.checkbox`](https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)