# st.slider

`st.slider`を使用すると、スライダー入力ウィジェットを表示できます。

サポートされているデータ型は、int、float、date、time、datetimeです。

## 構築内容

スライダーウィジェットの調整によるユーザー入力を受け入れるためのさまざまな方法を示す、シンプルなアプリです。

アプリの流れ：

1. ユーザーがスライダーウィジェットを調整して値を選択します
2. アプリが選択された値を出力します

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.slider/ "Streamlitアプリ")

## コード

st.sliderの使い方は次のとおりです。

```python
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

#例1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#例2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#例3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

#例4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
from datetime import time, datetime
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.slider')
```

**例1**

スライダー:

```python
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
```

このように、`st.slider()`コマンドは、ユーザーの年齢に関するユーザー入力を収集するために使用されます。

最初の入力引数は、**スライダー**ウィジェットのすぐ上に`'How old are you?'`というテキストを表示します。

次の3つの整数`0, 130, 25`は、それぞれ最小値、最大値、デフォルト値を表します。

**例2**

範囲スライダー:

```python
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
```

範囲スライダーを使用すると、下限値と上限値のペアを選択できます。

最初の入力引数は、**範囲スライダー**ウィジェットのすぐ上に`'Select a range of values'`というテキストを表示します。

次の3つの引数`0.0, 100.0, (25.0, 75.0)`は、それぞれ最小値、最大値、最後のタプルは、デフォルト値として下限値に25.0、上限値に75.0を使用することを表します。

**例3**

時間範囲スライダー:

```python
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
```

時間範囲スライダーを使用すると、日時の下限値と上限値のペアを選択できます。

最初の入力引数は、**時間範囲スライダー**ウィジェットのすぐ上に`'Schedule your appointment:`というテキストを表示します。

日時の下限値と上限値のペアのデフォルト値は、それぞれ11:30と12:45に設定されています。

**例4**

日時スライダー:

```python
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
```

日時スライダーを使用すると、日時を選択できます。

最初の入力引数は、**日時**スライダーウィジェットのすぐ上に`'When do you start?'`というテキストを表示します。

日時のデフォルト値は、`value`オプションを使って2020年1月1日9:30に設定されました。

## 参考文献

次の関連ウィジェットも参照してください。

- [`st.select_slider`](https://docs.streamlit.io/library/api-reference/widgets/st.select_slider)