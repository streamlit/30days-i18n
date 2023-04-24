# ローカル開発環境のセットアップ

実際にStreamlitの構築を開始する前に、まず開発環境をセットアップする必要があります。

まずはconda環境のインストールとセットアップから始めましょう。

## **condaのインストール**

- https://docs.conda.io/en/latest/miniconda.html にアクセスして、オペレーティングシステム（Windows、Mac、Linux）を選択し、`conda`をインストールします。
- インストーラーをダウンロードして実行し、`conda`をインストールします。

## **新しいconda環境の作成**

condaがインストールされたら、すべてのPythonライブラリの依存関係を管理するためのconda環境を作成しましょう。

Python 3.9で新しい環境を作成するには、次のように入力します。

```bash
conda create -n stenv python=3.9
```

`create -n stenv`は`stenv`という名前のconda環境を作成し、`python=3.9`でPythonバージョン3.9のconda環境をセットアップします。

## **conda環境のアクティブ化**

作成したばかりの`stenv`という名前のconda環境を使用するには、コマンドラインに次のように入力します。

```bash
conda activate stenv
```

## **Streamlitライブラリのインストール**

続いて、`streamlit`ライブラリをインストールします。

```bash
pip install streamlit
```

## **Streamlitデモアプリの起動**

Streamlitデモアプリ（図1）を起動するには、次のように入力します。

```bash
streamlit hello
```