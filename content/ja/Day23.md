# st.experimental\_get\_query\_params

`st.experimental_get_query_params`を使用すると、ユーザーのブラウザーのURLから直接クエリパラメーターを取得できます。

## デモアプリ

1. 次のリンクは、クエリパラメーターなしでデモアプリを読み込みます（エラーメッセージが表示されます）。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.experimental_get_query_params/ "Streamlitアプリ")

2. 次のリンクは、クエリパラメーター付きでデモアプリを読み込みます（ここではエラーメッセージは表示されません）。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk "Streamlitアプリ")

## コード

`st.experimental_get_query_params`の使い方は次のとおりです。

```python
import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. 手順
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2.st.experimental_get_query_paramsのコンテンツ
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3.URLからの情報の取得と表示
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

次に、アプリにタイトルを付けます。

```python
st.title('st.experimental_get_query_params')
```

バージョン情報のドロップダウンボックスも追加しましょう。

```python
with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
```

次に、アプリの訪問者に、クエリパラメーターを直接URLに渡す手順を説明します。

```python
# 1.手順
st.header('1.Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')
```

続いて、`st.experimental_get_query_params`コマンドのコンテンツを表示します。

```python
# 2.st.experimental_get_query_paramsのコンテンツ
st.header('2.Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())
```

最後に、URLのクエリパラメーターから選択的情報を選択して表示します。

```python
# 3.URLからの情報の取得と表示
st.header('3.Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')
```

## 参考文献

- [`st.experimental_get_query_params`](https://docs.streamlit.io/library/api-reference/utilities/st.experimental_get_query_params)