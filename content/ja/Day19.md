# Streamlitアプリをレイアウトする方法

このチュートリアルでは、次のコマンドを使用してStreamlitアプリをレイアウトします。

- `st.set_page_config(layout="wide")` - アプリのコンテンツをワイドモードで表示します（それ以外の場合は、デフォルトでコンテンツは固定幅のボックスにカプセル化されます。
- `st.sidebar` - ウィジェットまたはテキスト/画像表示をサイドバーに配置します。
- `st.expander` - テキスト/画像表示を折りたたみ可能なコンテナーボックス内に配置します。
- `st.columns` - 表形式のスペース（または列）を作成し、その中にコンテンツを配置します。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-layout/ "Streamlitアプリ")

## コード

Streamlitアプリのレイアウトをカスタマイズする方法は次のとおりです。

```python
import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '??', '??', '??', '??', '??', '??', '??'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'?? Hello {user_name}!')
  else:
    st.write('??  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('?? Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'?? **{user_food}** is your favorite **food**!')
  else:
    st.write('?? Please choose your favorite **food**!')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

まず、`wide`モードで表示されるページレイアウトの定義から始めます。これにより、ページコンテンツをブラウザーの幅まで広げることができます。

```python
st.set_page_config(layout="wide")
```

次に、Streamlitアプリにタイトルを付けます。

```python
st.title('How to layout your Streamlit app')
```

アプリのタイトルの下に、`About this app`というタイトルの展開可能なボックスが配置されます。展開すると、内部に詳細が表示されます。

```python
with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
```

ユーザー入力を受け入れる入力ウィジェットは、Streamlitコマンド`text_input`と`selectbox`の前に`st.sidebar`コマンドを使用して指定したサイドバーに配置されます。ユーザーが入力または選択した入力値が変数`user_name`、`user_emoji`、`user_food`に割り当てられ、保存されます。

```python
st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '??', '??', '??', '??', '??', '??', '??'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
```

最後に、`st.columns`コマンドを使用して、`col1`、`col2`、`col3`に対応する3つの列を作成します。次に、`with`ステートメントで始まる個々のコードブロックを作成し、各列にコンテンツを割り当てます。コードブロックの中に、ユーザーが入力データ（サイドバーで指定）を指定したかどうかに応じて、2つの代替テキストのうち1つを表示する条件ステートメントを作成します。デフォルトでは、ページの`else`ステートメントの下のテキストが表示されます。ユーザーが入力データを指定すると、入力したデータに対応する情報が、`Output`ヘッダーテキストの下に表示されます。

```python
st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'?? Hello {user_name}!')
  else:
    st.write('??  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('?? Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'?? **{user_food}** is your favorite **food**!')
  else:
    st.write('?? Please choose your favorite **food**!')
```

`f`文字列を使用して、定型テキストとユーザーが指定した値を組み合わせている点にも注目してください。

## 参考文献

- [レイアウトとコンテナー](https://docs.streamlit.io/library/api-reference/layout)