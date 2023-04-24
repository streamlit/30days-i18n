# st.cache

`st.cache`を使うと、Streamlitアプリのパフォーマンスを最適化できます。

Streamlitは、ウェブからデータを読み込んだり、大規模なデータセットを操作したりでき、高コストの計算を行う場合でも、アプリのパフォーマンスを維持できるキャッシュメカニズムを提供します。これは`@st.cache`デコレーターで行います。

関数を@st.cacheデコレーターでマークすると、デコレーターは関数が呼び出されるたびに、いくつかの点を確認するようにStreamlitに指示します。

1. 関数を呼び出した入力パラメーター
2. 関数で使用される外部変数の値
3. 関数の本文
4. キャッシュされた関数内で使用される関数の本文

Streamlitがこの4つのコンポーネントの正確な値を、正確な組み合わせと順序で初めて確認した場合に、関数を実行し、その結果をローカルキャッシュに保存します。その後、次にキャッシュされた関数が呼び出されたときに、これらのコンポーネントが変更されていなければ、Streamlitは関数の実行を完全にスキップし、代わりに以前にキャッシュに保存された出力を返します。

Streamlitがこれらのコンポーネントの変更を追跡する方法は、ハッシュ化です。キャッシュはメモリ内のキーと値のストアと考えられます。キーは上記のすべてのハッシュであり、値は参照によって渡される実際の出力オブジェクトです。

最後に、`@st.cache`はキャッシュの動作を構成するための引数をサポートしています。詳細については、APIリファレンスを参照してください。

## 使い方

Streamlitアプリで定義するカスタム関数の前の行に、`st.cache`デコレーターを追加するだけです。以下の例を参照してください。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.cache/ "Streamlitアプリ")

## コード

`st.cache`の使い方は次のとおりです。

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

#キャッシュを使用する
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


#キャッシュを使用しない
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、アプリで仕様する他のライブラリもインポートします。

```python
import streamlit as st
import numpy as np
import pandas as pd
from time import time
```

続いて、アプリのタイトルテキストを作成します。

```python
st.title('Streamlit Cache')
```

次に、大規模なDataFrameを生成するための2つのカスタム関数を定義します。1つ目は`st.cache`デコレーターを使用し、2つ目は使用しません。

```python
@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(1000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df
```

最後に、`time()`コマンドを使用して実行時間を計りながら、カスタム関数を実行します。

```python
#キャッシュを使用する
a0 = time()
st.subheader('Using st.cache')

#ここにload_data_a関数を挿入する

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

#キャッシュを使用しない
b0 = time()
st.subheader('Not using st.cache')

#ここにload_data_b関数を挿入する

st.write(load_data_b())
b1 = time()
st.info(b1-b0)
```

最初の実行では、ほぼ同様の実行時間が得られます。アプリを再読み込みし、`st.cache`デコレーターを使用したときの実行時間の変化を確認してください。速度の向上は確認できましたか？

## 参考文献

- [`st.cache` APIドキュメント](https://docs.streamlit.io/library/api-reference/performance/st.cache)
- `st.cache`[でパフォーマンスを最適化](https://docs.streamlit.io/library/advanced-features/caching)
- [実験的なキャッシュプリミティブ](https://docs.streamlit.io/library/advanced-features/experimental-cache-primitives)
- [`st.experimental_memo`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_memo)
- [`st.experimental_singleton`](https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton)