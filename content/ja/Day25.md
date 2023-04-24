# st.session\_state

ブラウザータブでのStreamlitアプリへのアクセスをセッションとして定義します。Streamlitサーバーに接続するブラウザータブごとに、新しいセッションが作成されます。Streamlitは、ユーザーがアプリを操作するたびに、スクリプトを上から下へ再実行します。各再実行は空白の状態で行われ、実行間で変数は共有されません。

セッション状態は、各ユーザーセッションの再実行間で変数を共有する方法です。Streamlitは、状態を保存して保持する機能に加えて、コールバックを使って状態を操作する機能も公開しています。

このチュートリアルでは、重量の変換アプリを構築する際のセッション状態とコールバックの使用法について説明します。

`st.session_state`を使用すると、Streamlitアプリでセッション状態を実装できます。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.session_state/ "Streamlitアプリ")

## コード

`st.session_state`の使い方は次のとおりです。

```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

まず、アプリのタイトルを作成します。

```python
st.title('st.session_state')
```

次に、重量をlbsからkgに、およびその逆に変換するためのカスタム関数を定義します。

```python
def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046
```

ここでは、`st.number_input`を使用して重量値の数値入力を受け入れます。

```python
st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)
```

上記2つのカスタム関数は、`st.number_input`コマンドで作成した数値ボックスに数値が入力されるとすぐに呼び出されます。`on_change`オプションで2つのカスタム関数`lbs_to_kg`と`kg_to_lbs`を指定していることに注目してください。

簡単に言うと、`st.number_input`ボックスに数値を入力すると、これらのカスタム関数によって数値が変換されます。

最後に、`st.session_state.kg`と`st.session_state.lbs`としてセッション状態に保存されている`kg`と`lbs`単位の重量値が、`st.write`で出力されます。

```python
st.header('Output')
st.write("st.session_state object:", st.session_state)
```

## 参考文献

- [セッション状態](https://docs.streamlit.io/library/api-reference/session-state)
- [アプリへのステートフル性の追加](https://docs.streamlit.io/library/advanced-features/session-state)