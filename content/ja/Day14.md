# Streamlitコンポーネント

コンポーネントは、Streamlitの可能性を拡張するサードパーティのPythonモジュールです\[[1](https://docs.streamlit.io/library/components)]。

## 利用可能なStreamlitコンポーネント

Streamlitのウェブサイトには、数十種類のStreamlitコンポーネントが掲載されています\[[2](https://streamlit.io/components)]。

Fanilo（Streamlit作成者）は、Wiki投稿にStreamlitコンポーネントの素晴らしいリストを公開しました\[[3](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)]。2022年4月現在、約85のStreamlitコンポーネントが掲載されています。

## 使い方

Streamlitコンポーネントのインストールは、pip-installを実行するだけです。

このチュートリアルでは、`streamlit_pandas_profiling`コンポーネントを使ってみましょう\[[4](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)]。

#### コンポーネントのインストール

```bash
pip install streamlit_pandas_profiling
```

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-components/ "Streamlitアプリ")

## コード

コンポーネントを使ってStreamlitアプリを構築する方法は次のとおりです。

```python
import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、アプリで使用する他のライブラリもインポートします。

```python
import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('`streamlit_pandas_profiling`')
```

次に、`pandas`の`read_csv`コマンドを使用してPenguinsデータセットを読み込みます。

```python
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
```

最後に、pandasプロファイリングレポートが`profile_report()`コマンドによって生成され、`st_profile_report`を使用して表示されます。

```python
pr = df.profile_report()
st_profile_report(pr)
```

## 独自コンポーネントの作成

独自のコンポーネントの作成に興味がある場合は、次のリソースを参照してください。

- [コンポーネントの作成](https://docs.streamlit.io/library/components/create)
- [コンポーネントの公開](https://docs.streamlit.io/library/components/publish)
- [コンポーネントAPI](https://docs.streamlit.io/library/components/components-api)
- [コンポーネントに関するブログ記事](https://blog.streamlit.io/introducing-streamlit-components/)

また、ビデオを使用して学習したい場合は、当社エンジニアのTim Conklingがわかりやすくまとめたチュートリアルがあります。

- [Streamlitコンポーネントの構築方法 \| パート1:](https://youtu.be/BuD3gILJW-Q)[ ](https://youtu.be/BuD3gILJW-Q)[セットアップとアーキテクチャ](https://youtu.be/BuD3gILJW-Q)
- [Streamlitコンポーネントの構築方法 \| パート2:](https://youtu.be/QjccJl_7Jco)[ ](https://youtu.be/QjccJl_7Jco)[パート2:](https://youtu.be/QjccJl_7Jco)[ ](https://youtu.be/QjccJl_7Jco)[スライダーウィジェットの作成](https://youtu.be/QjccJl_7Jco)

## コンポーネントに関する参考文献

1. [Streamlitコンポーネント - APIドキュメント](https://docs.streamlit.io/library/components)
2. [注目のStreamlitコンポーネント](https://streamlit.io/components)
3. [Streamlitコンポーネント - Community Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634)
4. [`streamlit_pandas_profiling`](https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling)