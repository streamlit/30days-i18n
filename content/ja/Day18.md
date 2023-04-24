# st.file\_uploader

`st.file_uploader`は、ファイルアップローダーウィジェットを表示します\[[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)]。

デフォルトでは、アップロードされるファイルは200MBに制限されています。これは、server.maxUploadSizeオプションを使用して設定できます。構成オプションの設定方法については、\[[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)]を参照してください。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/ "Streamlitアプリ")

## コード

`st.file_uploader`の使い方は次のとおりです。

```python
import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('?? Upload a CSV file')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートし、他の必須ライブラリもインポートします。

```python
import streamlit as st
import pandas as pd
```

続いて、アプリのタイトルテキストを作成します。

```python
st.title('st.file_uploader')
```

次に、`st.file_uploader`を使って、ユーザー入力ファイルを受け入れるファイルアップローダーウィジェットを表示します。

```python
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
```

最後に、（`else`条件で実装されているように）ユーザーにファイルのアップロードを促すウェルカムメッセージを最初に表示するための条件ステートメントを定義します。ファイルがアップロードされると、`if`ステートメントがアクティブになり、`pandas`ライブラリによってCSVファイルが読み込まれ、`st.write`コマンドによって表示されます。

```python
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('?? Upload a CSV file')
```

## 参考文献

1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [構成オプションの設定](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)