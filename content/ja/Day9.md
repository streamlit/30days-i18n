# st.line\_chart

`st.line_chart`は折れ線グラフを表示します。

これは`st.altair_chart`のシンタックスシュガー(より分かりやすい構文で書けるもの)です。主な違いは、このコマンドはデータの独自の列とインデックスを使用してグラフの仕様を決定することです。その結果、「これをプロットするだけ」という多くのシナリオで使いやすくなりますが、カスタマイズ性は低くなります。

`st.line_chart`がデータ仕様を正しく推測できない場合は、st.altair\_chartを使って目的のグラフを指定してみてください。

## 構築内容

折れ線グラフを表示するシンプルなアプリです。

アプリの流れ：

1. `NumPy`でランダムに生成された数値から`Pandas` DataFrameを作成します
2. `st.line_chart()`コマンドで折れ線グラフを作成して表示します

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/ "Streamlitアプリ")

## コード

[`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)の使い方は次のとおりです。

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

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、他のライブラリもインポートします。

```python
import streamlit as st
import pandas as pd
import numpy as np
```

次に、アプリのヘッダーテキストを作成します。

```python
st.header('Line chart')
```

次に、3つの列を含むランダムに生成された数値のDataFrameを作成します。

```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

最後に、`chart_data`変数に格納されたDataFrameを入力データとして、`st.line_chart()`を使って折れ線グラフを作成します。

```python
st.line_chart(chart_data)
```

## 参考文献

[`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart)の基になっている次の関連するStreamlitコマンドの詳細をご覧ください。

- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)