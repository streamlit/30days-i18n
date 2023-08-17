# st.write

`st.write`を使用すると、Streamlitアプリにテキストや引数を書き込むことができます。

テキストを表示できるほか、`st.write()`コマンドを使って次の様な表示も可能です。

- `st.markdown()`のようにマークダウン形式の文字列を出力する
- Python `dict`の表示
- `pandas`の表示（DataFrameをテーブルとして表示できます）
- `matplotlib`、`plotly`、`altair`、`graphviz`、`bokeh`からのプロット/グラフ/図
- その他（[APIドキュメントのst.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write)を参照してください）

## 構築内容

テキスト、数値、DataFrame、プロットを表示するための`st.write()`コマンドのさまざまな使い方を示すシンプルなアプリです。

## デモアプリ

デプロイされたStreamlitアプリは、次のリンクに示すようになります。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/ "Streamlitアプリ")

## コード

st.writeの使い方は次のとおりです。

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

#例1

st.write('Hello, *World!* :sunglasses:')

#例2

st.write(1234)

#例3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

#例4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

#例5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.write')
```

**例1** 基本的なユースケースは、テキストやMarkdown形式のテキストの表示です。

```python
st.write('Hello, *World!* emoji')
```

**例2** 上記のように、数値など他のデータ形式の表示にも使用できます。

```python
st.write(1234)
```

**例3** DataFrameも次のように表示できます。

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**例4** 複数の引数を渡すことができます。

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**例5** 最後に、次のように変数に渡すことで、プロットも表示できます。

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## デモアプリ

デプロイされたStreamlitアプリは、次のリンクに示すようになります。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/ "Streamlitアプリ")

## 次のステップ

ローカルでStreamlitアプリを作成したら[Streamlit Cloud](https://streamlit.io/cloud).Streamlit Cloudについては今後の課題で説明します。

今回は最初の週なので、このウェブページ内にコード（上記のコードボックスに表示）とソリューション（デモアプリ）をすべて用意しました。

次の課題に進むために、まずは自分でStreamlitアプリを実装してみることをお勧めします。

行き詰まっても心配する必要はありません。いつでもソリューションを確認できます。

## 参考文献

[`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write)の他にも、テキストを表示する方法を参照してください。

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
