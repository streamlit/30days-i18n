# st.secrets

`st.secrets`は、APIキー、データベースパスワード、その他の認証情報などの機密情報を保存できます。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/ "Streamlitアプリ")

## コード

`st.secrets`の使い方は次のとおりです。

```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

続いて、アプリのタイトルテキストを作成します。

```python
st.title('st.secrets')
```

最後に、保存されているシークレットを表示します。

```python
st.write(st.secrets['message'])
```

以下のスクリーンショットに示すように、シークレットはStreamlit Cloudに保存できます。

ローカルで作業する場合は、`.streamlit/secrets.toml`に保存できますが、アプリのデプロイ時にGitHubリポジトリにアップロードしないようにしてください。

## 参考文献

- [Streamlitアプリへのシークレットの追加](https://blog.streamlit.io/secrets-in-sharing-apps/)
- [シークレットの管理](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)