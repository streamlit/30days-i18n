# st.selectbox

`st.selectbox`を使用すると、選択ウィジェットを表示できます。

## 構築内容

ユーザーに好きな色を尋ねるシンプルなアプリです。

アプリの流れ：

1. ユーザーが色を選択します
2. アプリから選択された色が出力されます

## デモアプリ

デプロイされたStreamlitアプリは、次のリンクに示すようになります。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.selectbox/ "Streamlitアプリ")

## コード

上記のアプリを実装するコードは次のとおりです。

```python
import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.selectbox')
```

次に、`option`という変数を作成して、`st.selectbox()`コマンドを使って**選択**入力ウィジェットの形式でユーザー入力を受け入れるようにします。

```python
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
```

上記のコードボックスからわかるように、`st.selectbox()`コマンドは2つの入力引数を受け入れます。

1. 選択ウィジェットの上に表示されるテキスト（`'What is your favorite color?'`）
2. 選択可能な値`('Blue', 'Red', 'Green')`

最後に、次のように選択された色を出力します。

```python
st.write('Your favorite color is ', option)
```

## 次のステップ

ローカルでStreamlitアプリを作成したら、今度はこれを[Streamlit Cloud](https://streamlit.io/cloud)にデプロイしてみましょう。

## リファレンス

[`st.selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)の詳細