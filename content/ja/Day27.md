# Streamlit Elementsを使ったドラッグおよびサイズ変更可能なダッシュボードの構築

Streamlit Elementsは、[okld](https://github.com/okld)製のサードパーティコンポーネントで、Material UIウィジェット、Monacoエディター（Visual Studio Code）、Nivoチャートなどを使って美しいアプリケーションやダッシュボードを作成するツールを提供します。

## 使い方

### インストール

まずは、お使いの環境にStreamlit Elementsをインストールします。

```bash
pip install streamlit-elements==0.1.*
```

将来のバージョンではAPIが変更される可能性があるため、バージョンは`0.1.*`に固定することをお勧めします。

### 使用法

詳細な使用ガイドについては、[Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started)を参照してください。

## 構築内容

今日の課題は、3つのMaterial UIカードで構成されるダッシュボードを作成することです。

- 最初のカードは、データを入力するためのMonacoコードエディターです。
- 2枚目のカードは、データをNivoバンプチャートで表示します。
- 3枚目のカードは、`st.text_input`で定義されたYouTubeビデオのURLを表示します。

Nivoバンプのデモから生成されたデータは、「データ」タブで使用できます（https://nivo.rocks/bump/）。

## デモアプリ

[![](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main "Streamlitアプリ")

## 行ごとの説明付きのコード

```python
#まず、アプリケーションに以下をインポートする必要があります。

import json
import streamlit as st
from pathlib import Path

#Streamlit Elementsでは、これらすべてのオブジェクトが必要になります。
#利用可能なすべてのオブジェクトと使用法については、こちらを参照してください。https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

#ダッシュボードがページ全体を占めるように、ページレイアウトを変更します。

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("??? #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    #メディアプレーヤーのURLを定義します。
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

#コードエディターとチャートのデフォルトデータを初期化します。
#
#このチュートリアルでは、Nivoバンプチャートのデータが必要です。
#「データ」タブでランダムなデータを取得できます（https://nivo.rocks/bump/）。
#
#以下に示すように、このセッション状態の項目はコードエディターが変更されると更新され、
# Nivoバンプチャートがそれを読み取ってデータを描画します。

if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

#デフォルトのダッシュボードレイアウトを定義します。
#ダッシュボードグリッドはデフォルトで12列あります。
#
#利用可能なパラメーターの詳細については、こちらを参照してください。
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    #エディター項目は座標x=0、y=0に配置され、6/12列を取り、高さは3です。
    dashboard.Item("editor", 0, 0, 6, 3),
    #グラフ項目は座標x=6、y=0に配置され、6/12の列を取り、高さは3です。
    dashboard.Item("chart", 6, 0, 6, 3),
    #メディア項目は座標x=0、y=3に配置され、6/12列を取り、高さは4です。
    dashboard.Item("media", 0, 2, 12, 4),
]

#要素を表示するフレームを作成します。

with elements("demo"):

    #上記で指定したレイアウトで新しいダッシュボードを作成します。
    #
    # draggableHandleは、各ダッシュボード項目のドラッグ可能な部分を定義するCSSクエリセレクターです。
    #ここでは、クラス名に「draggable」を含む要素がドラッグ可能になります。
    #
    #ダッシュボードグリッドで利用可能なパラメーターの詳細については、こちらを参照してください。
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        #最初のカードはコードエディターです。
        #
        #「key」パラメーターを使って、正しいダッシュボード項目を特定します。
        #
        #カードのコンテンツが自動的に利用可能な高さになるようにするには、CSS Flexboxを使用します。
        # sxは、CSS属性を定義するために、すべてのMaterial UIウィジェットで利用可能なパラメーターです。
        #
        #カード、Flexbox、sxの詳細については、こちらを参照してください。
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            #このヘッダーをドラッグ可能にするには、上記のdashboard.GridのdraggableHandleで定義したように、
            #クラス名を「draggable」に設定する必要があります。

            mui.CardHeader(title="Editor", className="draggable")

            # flex CSS値を1に設定することで、カードのコンテンツをすべて利用可能な高さにします。
            #また、minHeightを0に設定することで、カードを縮小するとカードのコンテンツも縮小されるようにします。

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                #これはMonacoコードエディターです。
                #
                #まず、上記で初期化したst.session_state.dataにデフォルト値を設定します。
                #次に、使用する言語（ここではJSON）を定義します。
                #
                #次に、エディターのコンテンツに加えられた変更を取得します。
                # Monacoのドキュメントを確認すると、関数を受け取るonChangeプロパティがあります。
                #この関数は、変更が行われるたびに呼び出され、更新されたコンテンツ値が
                #最初のパラメーターに渡されます（onChange: https://github.com/suren-atoyan/monaco-react#propsを参照）。
                #
                # Streamlit Elementsは、特別なsync()関数を提供します。この関数はコールバックを作成し、そのパラメーターを
                #Streamlitのセッション状態項目に自動的に転送します。
                #
                #例
                # --------
                #最初のパラメーターを「data」というセッション状態項目に転送するコールバックを作成します。
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # 2番目のパラメーターを「ev」というセッション状態項目に転送するコールバックを作成します。
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                #両方のパラメーターをセッション状態に転送するコールバックを作成します。
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                #ここで問題があります。onChangeは、変更が行われるたびに呼び出されます。
                #つまり、1文字を入力するたびに、Streamlitアプリ全体が再実行されます。
                #
                #この問題を回避するために、Streamlit Elementsに別のイベントが発生するまで待機するように指示できます。
                #（ボタンクリックのように）コールバックをlazy()で囲んで、更新されたデータを送信します。
                #
                # Monacoで利用可能なパラメーターの詳細については、こちらを参照してください。
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monacoエディターでは、onChangeに遅延コールバックをバインドしているため、
                # Monacoのコンテンツを変更しても、Streamlitには直接通知されず、毎回再読み込みされることはありません。
                #そのため、更新をトリガーするための遅延しない別のイベントが必要です。
                #
                #解決策は、クリック時にコールバックを起動するボタンを作成することです。
                #コールバックは特に何も実行する必要はありません。空の
                # Pythonの関数、または引数なしでsync()を使用します。
                #
                #これで、そのボタンをクリックするたびに、onClickコールバックが起動しますが、
                #その間に変更された他のすべての遅延コールバックも呼び出されます。

                mui.Button("Apply changes", onClick=sync())

        # 2枚目のカードのNivoバンプチャートです。
        # 1枚目のカードと同じFlexbox構成を使って、コンテンツの高さを自動調整します。

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            #このヘッダーをドラッグ可能にするには、上記のdashboard.GridのdraggableHandleで定義したように、
            #クラス名を「draggable」に設定する必要があります。

            mui.CardHeader(title="Chart", className="draggable")

            # 上記のように、ユーザーがカードのサイズを変更すると、コンテンツが拡大および縮小するようにします。
            # flexを1、minHeightを0に設定します。

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # ここにバンプチャートを表示します。
                #
                #この演習では、Nivoの例をアレンジしてStreamlit Elementsで動作するようにします。
                # Nivoの例は、こちらの「コード」タブから入手できます。https://nivo.rocks/bump/
                #
                # Dataは辞書をパラメーターとして受け取るため、まずjson.loads()を使用して
                # JSONデータを文字列からPython辞書に変換する必要があります。
                #
                # その他の利用可能なNivoチャートに関する詳細については、こちらを参照してください。
                # https://nivo.rocks/

                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        #ダッシュボードの3番目の要素はメディアプレーヤーです。

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                #この要素はReactPlayerを利用しており、
                # YouTube以外の多くのプレーヤーをサポートしています。こちらから確認できます。https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## お問い合わせ

Streamlit Elementsやこの課題に関するご質問は、こちらまでお気軽にお問い合わせください。[Streamlit Elementsのトピック](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)