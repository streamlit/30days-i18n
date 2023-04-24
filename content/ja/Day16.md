# Streamlitアプリのテーマのカスタマイズ

アプリと同じフォルダの`.streamlit`フォルダに保存されている設定ファイル`config.toml`のパラメーターを調整することで、テーマをカスタマイズできます。

## 構築内容

テーマをカスタマイズした結果を表示するシンプルなアプリです。これは、[`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml)ファイル内のHTML HEXコードをカスタマイズすることで可能になります。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-custom-theme/ "Streamlitアプリ")

## コード

[`streamlit_app.py`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/streamlit_app.py)ファイルのコードは次のとおりです。

```python
import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

[`.streamlit/config.toml`](https://github.com/dataprofessor/streamlit-custom-theme/blob/master/.streamlit/config.toml)ファイルのコードは次のとおりです。

```python
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのタイトルテキストを作成します。

```python
st.title('Theming with config.toml')
```

次に、`.streamlit/config.toml`ファイルの内容を表示します。まず、`st.write`でメモを表示し、`st.code`で実際のコードを表示します。

```python
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
```

最後に、サイドバーにスライダーウィジェットを作成し、選択された数字を表示します。

```python
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

このアプリで使用しているカスタムカラーについて、`.streamlit/config.toml`ファイルで指定されている設定を見てみましょう。

- `primaryColor="#F39C12"` - 第1カラーをオレンジに設定します。スライダーウィジェットのオレンジ色になります。
- `backgroundColor="#2E86C1"` - 背景色を青に設定します。メインパネルの背景色が青色になります。
- `secondaryBackgroundColor="#AED6F1"` - 第2の背景色を濃い灰色に設定します。サイドバーの背景色とメインパネルのコードボックスの背景色が濃い灰色になります。
- `textColor="#FFFFFF"` - テキストの色を白に設定します。
- `font="monospace"` - フォントを等幅に設定します。

## 参考文献

- [テーマ](https://docs.streamlit.io/library/advanced-features/theming)
- [HTMLカラーコード](https://htmlcolorcodes.com/)は好みの色を選択するための優れたツールです。