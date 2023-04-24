# st.form

`st.form`は、「送信」ボタンとともに要素をバッチ処理するフォームを作成します。

通常、ユーザーがウィジェットを操作するたびに、Streamlitアプリが再実行されます。

フォームとは、他の要素とウィジェットを視覚的にグループ化し、送信ボタンを含むコンテナーです。ここでは、ユーザーは、1つ以上のウィジェットを何度でも再実行せずに操作できます。最後に、フォームの送信ボタンが押されると、フォーム内のすべてのウィジェット値が1つのバッチでStreamlitに送信されます。

フォームオブジェクトに要素を追加するには、`with`表記を使用するか（推奨）、フォーム上で直接メソッドを呼び出すだけで（最初に変数に割り当て、その後Streamlitメソッドを適用することで）オブジェクト表記として使用できます。サンプルアプリを参照してください。

フォームにはいくつかの制約があります。

- すべてのフォームには`st.form_submit_button`が必要です。
- `st.button`と`st.download_button`はフォームに追加できません。
- フォームはアプリ内の任意の場所（サイドバー、列など）に表示できますが、他のフォーム内に埋め込むことはできません。

フォームの詳細については、[ブログ記事](https://blog.streamlit.io/introducing-submit-button-and-forms/)を参照してください。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.form/ "Streamlitアプリ")

## コード

`st.form`の使い方は次のとおりです。

```python
import streamlit as st

st.title('st.form')

# with表記の使用例
# ※「完全な」は「Full」の訳だと思いますが訳さなくても伝わると思います。
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    
    #入力ウィジェット
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    #すべてのフォームには送信ボタンが必要です
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ? You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('?? Place your order!')


#オブジェクト表記を使用した短い例
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのタイトルテキストを作成します。

```python
st.title('st.form')
```

### 最初の例

最初の例から始めましょう。ここでは`st.form`コマンドを`with`表記で適用します。まず、フォーム内でサブヘッダー`Order your coffee`を記述し、次に、コーヒーの注文に関する情報を収集する複数の入力ウィジェット（`st.selectbox`、`st.select_slider`、`st.checkbox`）を作成します。最後に、`st.form_submit_button`コマンドで送信ボタンを作成します。これをクリックすると、すべてのユーザー入力が1つのバッチ情報としてアプリに送信され、処理されます。

```python
# with表記の完全な使用例
st.header('1.Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    #入力ウィジェット
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    
    #すべてのフォームには送信ボタンが必要です。
    submitted = st.form_submit_button('Submit')
```

次に、送信ボタンがクリックされた後に実行されるロジックを追加します。デフォルトでは、Streamlitアプリが読み込まれるたびに`else`ステートメントが実行され、`☝️ Place your order!`というメッセージが表示されます。送信ボタンをクリックすると、さまざまなウィジェットを介してユーザーが行ったすべての入力がいくつかの変数（例: `coffee_bean_val`、`coffee_roast_val`など）に保存され、f-stringを使用して`st.markdown`コマンドによって出力されます。

```python
if submitted:
    st.markdown(f'''
        ? You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('?? Place your order!')
```

### 2番目の例

次に、`st.form`をオブジェクト表記として使用する2番目の例を見てみましょう。ここでは、`st.form`コマンドが`form`変数に割り当てられています。続いて、`slider`や`form_submit_button`などのさまざまなStreamlitコマンドが`form`変数に適用されます。

```python
#オブジェクト表記を使用した短い例
st.header('2.Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

## 参考文献

- [`st.form`](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
- [送信ボタンとフォームの紹介](https://blog.streamlit.io/introducing-submit-button-and-forms/)