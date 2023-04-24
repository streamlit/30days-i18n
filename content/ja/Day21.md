# st.progress

`st.progress`は、反復処理の進行状況に応じてグラフィカルに更新される進行状況バーを表示します。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.progress/ "Streamlitアプリ")

## コード

`st.progress`の使い方は次のとおりです。

```python
import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、`time`ライブラリもインポートします。

```python
import streamlit as st
import time
```

次に、アプリのタイトルテキストを作成します。

```python
st.title('st.progress')
```

`st.expander`を使用して**バージョン情報ボックス**を作成し、`st.write`で説明を表示します。

```python
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
```

最後に、進行状況バーを定義し、開始値を`0`としてインスタンス化します。次に、`for`ループで`0`から`100`に達するまで反復します。各反復で`time.sleep(0.05)`を使用して、アプリが`my_bar`進行状況バーに値`1`を追加する前に`0.05`待機するようにして、バーのグラフィック表示が反復ごとに増加するようにします。

```python
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
```

## 参考文献

- [`st.progress`](https://docs.streamlit.io/library/api-reference/status/st.progress)