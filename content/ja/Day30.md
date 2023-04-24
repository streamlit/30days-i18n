# Streamlitアプリを作成する技術

今日は*#30DaysOfStreamlit*課題の30日目です。ここまでよく課題をやり遂げられました。

このチュートリアルでは、この学習課題で得た新しい知識を活かして、現実世界の問題を解決するStreamlitアプリを作成します。

## 現実世界の問題

コンテンツ作成者として、YouTubeビデオのサムネイル画像にアクセスできれば、ソーシャルプロモーションやコンテンツ作成に役立つリソースとなります。

この問題にどのように取り組み、Streamlitアプリを構築するかを考えてみましょう。

## 解決策

今日は、YouTubeビデオからサムネイル画像を抽出できるStreamlitアプリ`yt-img-app`を構築します。

簡単に言うと、Streamlitアプリで実行するのは、次の3つのステップだけです。

1. ユーザーからの入力としてYouTubeのURLを受け取ります
2. そのURLのテキスト処理を行い、一意のYouTubeビデオIDを抽出します
3. そのYouTubeビデオIDをカスタム関数への入力として使用し、YouTubeビデオからサムネイル画像を取得して表示します

## 手順

Streamlitアプリの使用を開始するには、YouTubeのURLをコピーして入力テキストボックスに貼り付けます。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/yt-img-app/ "Streamlitアプリ")

## コード

Streamlitアプリ`yt-img-app`を構築する方法は次のとおりです。

```python
import streamlit as st

st.title('??? yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
  
#画像設定
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
    
# YouTubeのサムネイル画像を表示します
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('?? Enter URL to continue ...')
```

## 行ごとの説明

Streamlitアプリを作成するときは、まず次のように`streamlit`ライブラリを`st`としてインポートします。

```python
import streamlit as st
```

次に、アプリのタイトルと付随するヘッダーを表示します。

```python
st.title('??? yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')
```

ついでに、「バージョン情報」の展開可能ボックスを追加することもできます。

```python
with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')
 
ここでは、使用する画質についてユーザー入力を受け入れるための選択ボックスを作成します。
```python
#画像設定
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
```

画像の抽出に使用するYouTubeビデオのURLでユーザー入力を受け入れる入力テキストボックスが表示されます。

```python
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')
```

入力URLのテキスト処理を行うためのカスタム関数です。

```python
def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid
```

最後に、フロー制御を使用して、URLを入力するリマインダーを表示するか（`else`ステートメント）、YouTubeのサムネイル画像を表示するか（`if`ステートメント）を決定します。

```python
# YouTubeのサムネイル画像を表示します
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('?? Enter URL to continue ...')
```

## まとめ

まとめると、Streamlitアプリの作成では、まず問題を特定して定義することから始めます。次に、その問題に取り組むための解決策を細かいステップに分解して考え、それをStreamlitアプリに実装します。

ここでは、ユーザーからの入力として必要なデータや情報、最終的に必要な出力を生成するためにユーザー入力を処理する際に使用するアプローチや方法も決定する必要があります。

このチュートリアルをお楽しみいただき、ありがとうございました。