# st.button

`st.button`を使用すると、ボタンウィジェットを表示できます。

## 構築内容

ボタンが押されたかどうかによってメッセージを切り替えるシンプルなアプリ

アプリの流れ：

1. デフォルトでは、アプリは「`Goodbye`」を出力します
2. ボタンをクリックすると、アプリは「`Why hello there`」という代替メッセージを表示します

## デモアプリ

デプロイされたStreamlitアプリは、次のリンクに示すようになります。

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/ "Streamlitアプリ")

## コード

上記のアプリを実装するコードは次のとおりです。

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのヘッダーテキストを作成します。

```python
st.header('st.button')
```

次に、条件ステートメントの`if`と`else`を使って、代替メッセージを出力します。

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

上記のコードボックスからわかるように、`st.button()`コマンドは、`label`という引数に`Say hello`を与えることで、ボタンに表示されるテキストを指定できます。
※「`label`入力引数を受け入れ」という表現がわかりにくいと感じました。

`st.write`コマンドは、ボタンがクリックされたかどうかに応じて、`Why hello there`または`Goodbye`のいずれかのテキストメッセージを出力するために使用されます。これは、次のように実装されています。

```python
st.write('Why hello there')
```

および

```python
st.write('Goodbye')
```

ここで重要なのは、上記の`st.write`ステートメントは、上で説明した代替メッセージの表示プロセスを実行するために、`if`と`else`の条件下に置かれていることです。

## 次のステップ

ローカルでStreamlitアプリを作成したら https://streamlit.io/cloud. Streamlit Cloudについては今後の課題で説明します。

今回は最初の週なので、このウェブページ内にコード（上記のコードボックスに表示）とソリューション（デモアプリ）をすべて用意しました。

次の課題に進むために、まずは自分でStreamlitアプリを実装してみることをお勧めします。

行き詰まっても心配する必要はありません。いつでもソリューションを確認できます。

## リファレンス

[`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button)については、Streamlit APIのドキュメントを参照してください。