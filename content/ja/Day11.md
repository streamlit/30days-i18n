# st.multiselect

`st.multiselect`は、複数選択ウィジェットを表示します。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.multiselect/ "Streamlitアプリ")

## コード

`st.multiselect`の使い方は次のとおりです。

```python
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.multiselect')
```

次に、`st.multiselect`ウィジェットを使って、ユーザーが1つ以上の色を選択して入力できるようにします。

```python
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
```

最後に、選択された色を書き出します。

```python
st.write('You selected:', options)
```

## 参考文献

- [`st.multiselect`](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)