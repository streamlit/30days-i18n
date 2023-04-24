# st.latex

`st.latex`は、LaTeX形式の数式を表示します。

## 構築内容

`st.latex`コマンドでLaTeX構文を使って数式を表示するシンプルなアプリです。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.latex/ "Streamlitアプリ")

## コード

`st.latex`の使い方は次のとおりです。

```python
import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.latex')
```

次に、`st.latex`を使って数式を表示します。

```python
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

## リファレンス

- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)の詳細については、Streamlit APIのドキュメントを参照してください。