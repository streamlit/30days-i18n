# Erstellung eines verschieb- und größenveränderbaren Dashboards mit Streamlit Elements

Streamlit Elements ist eine Komponente eines Drittanbieters, die von [okld] (https://github.com/okld) entwickelt wurde und dir die Möglichkeit bietet, schöne Apps und Dashboards mit Material UI-Widgets, Monaco-Editor (Visual Studio Code), Nivo-Diagrammen und vielem mehr zu erstellen.

## Wie wird es verwendet?

### Installation

Der erste Schritt besteht darin, Streamlit Elements in Ihrer Umgebung zu installieren:

```bash
pip install streamlit-elements==0.1.*
```

Es wird empfohlen, die Version auf `0.1.*` festzulegen, da zukünftige Versionen möglicherweise brechende API-Änderungen einführen.

### Verwendung

Eine ausführliche Anleitung zur Verwendung findet man in [Streamlit Elements README](https://github.com/okld/streamlit-elements#getting-started).

## Was bauen wir?

Das Ziel der heutigen Herausforderung ist es, ein Dashboard zu erstellen, das aus drei Material UI-Karten besteht:

- Eine erste Karte mit einem Monaco-Code-Editor zur Dateneingabe;
- Eine zweite Karte, die diese Daten in einem Nivo Bump-Diagramm anzeigt;
- Eine dritte Karte, um eine YouTube-Video-URL anzuzeigen, die mit `st.text_input` definiert wurde.

Man kann die von der Nivo Bump-Demo generierten Daten auf dem "Daten"-Tab verwenden: https://nivo.rocks/bump/.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-elements-demo/main)

## Code mit zeilenweiser Erklärung

```python
# Zuerst brauchen wir die folgenden Importe für unsere App.

import json
import streamlit as st
from pathlib import Path

# Was Streamlit Elements betrifft, brauchen wir alle diese Objekte.
# Alle verfügbaren Objekte und ihre Verwendung sind dort aufgeführt: https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# Seitenlayout ändern, damit das Dashboard die ganze Seite einnimmt.

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # URL für Medienplayer festlegen.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Standarddaten initialisieren für den Code-Editor und das Diagramm.
#
# Für dieses Tutorial brauchen wir Daten für ein Nivo Bump-Diagramm.
# Zufallsdaten erhälst du dort, im Tab 'Daten': https://nivo.rocks/bump/
#
# Wie man unten sieht wird dieser Session-State aktualisiert, wenn der
# Code-Editor geändert wird, und es wird von Nivo Bump Chart gelesen werden, um die Daten zu zeichnen.


if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# Ein Standardlayout für das Dashboard festlegen.
# Das Dashboard-Gitter hat standardmäßig 12 Spalten.
#
# Weitere Informationen zu den verfügbaren Parametern:
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # Das Editorelement wird an den Koordinaten x=0 und y=0 positioniert, nimmt 6/12 Spalten ein und hat eine Höhe von 3.
    dashboard.Item("editor", 0, 0, 6, 3),
    # Das Diagrammelement wird an den Koordinaten x=6 und y=0 positioniert, nimmt 6/12 Spalten ein und hat eine Höhe von 3.
    dashboard.Item("chart", 6, 0, 6, 3),
    # Das Medienelement wird an den Koordinaten x=0 und y=3 positioniert, nimmt 6/12 Spalten ein und hat eine Höhe von 4.
    dashboard.Item("media", 0, 2, 12, 4),
]

# Einen Rahmen erstellen, um Elemente anzuzeigen.

with elements("demo"):

    # Ein neues Dashboard mit dem oben angegebenen Layout erstellen.
    #
    # draggableHandle ist ein CSS-Query-Selektor, um den ziehbaren Teil jedes Dashboard-Elements zu definieren.
    # Hier werden Elemente mit einem 'draggable' Klassennamen ziehbar sein.
    #
    # Weitere Informationen zu den verfügbaren Parametern für das Dashboard-Gitter findet man hier:
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # Erste Karte, der Code-Editor.
        #
        # Wir benutzen den Parameter 'key', um das richtige Dashboard-Element zu identifizieren.
        #
        # Damit der Inhalt der Karte automatisch die verfügbare Höhe ausfüllt, verwenden wir CSS Flexbox.
        # sx ist ein Parameter, der bei jedem Material UI-Widget verfügbar ist, um CSS-Attribute zu definieren.
        #
        # Weitere Informationen zu Card, flexbox und sx:
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # Um diese Überschrift ziehbar zu machen, müssen wir nur ihren Klassennamen auf 'draggable' setzen,
            # wie oben in draggableHandle (Argument von dashboard.Grid) definiert.

            mui.CardHeader(title="Editor", className="draggable")

            # Wir möchten, dass der Inhalt der Karte die gesamte verfügbare Höhe einnimmt. Deswegen setzen wir den CSS-Wert flex auf 1.
            # Wir wollen auch, dass der Inhalt der Karte schrumpft, wenn die Karte verkleinert wird. Deswegen setzen wir minHeight auf 0.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Hier ist unser Monaco-Code-Editor.
                #
                # Zuerst setzen wir den Defaultwert auf st.session_state.data, den wir oben initialisiert haben.
                # Zweitens legen wir die zu verwendende Sprache fest, hier JSON.
                #
                # Dann wollen wir die Änderungen von dem Inhalt des Editors abrufen.
                # Die Monaco-Dokumentation zeigt, dass es eine onChange Eigenschaft gibt, die eine Funktion annimmt.
                # Diese Funktion wird jedes Mal aufgerufen, wenn eine Änderung vorgenommen wird, und der aktualisierte Inhaltswert wird in
                # den ersten Parameter übergeben (vgl. onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elemente bieten eine spezielle sync()-Funktion. Diese Funktion erstellt einen Callback, der
                # Parameter automatisch an die Session-State von Streamlit weiterleitet.
                #
                # Beispiele
                # --------
                # Erstelle einen Callback, der seinen ersten Parameter an ein Session-State-Element namens "data" weiterleitet:
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # Erstelle einen Callback, der seinen zweiten Parameter an ein Session-State-Element namens "ev" weiterleitet:
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # Erstelle einen Callback, der seine beiden Parameter an die Session-State weiterleitet:
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # Jetzt gibt es ein Problem: onChange wird jedes Mal aufgerufen, wenn eine Änderung vorgenommen wird. Das bedeutet, dass jedes Mal wenn
                # man ein einziges Zeichen eingibt, wird die gesamte Streamlit-App neu ausgeführt.
                #
                # Um dieses Problem zu vermeiden, kann man Streamlit Elements anweisen, auf ein anderes Ereignis zu warten
                # (z. B. ein Button-Klick), bevor die aktualisierten Daten gesendet werden. Dies wird durch Verwendung von lazy() als Wrapper für den Callback erreicht.
                #
                # Weitere Informationen zu den verfügbaren Parametern für Monaco:
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html


                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Der Monaco-Editor hat einen Lazy-Callback, der an onChange gebunden ist. Das bedeutet, dass selbst wenn man den
                # Inhalt von Monaco ändert, wird Streamlit nicht direkt benachrichtigt, also wird es nicht jedes Mal neu geladen.
                # Wir brauchen also ein anderes, nicht-lazy Ereignis, um ein Update auszulösen.
                #
                # Die Lösung ist, einen Button zu erstellen, der beim Klick einen Callback auslöst.
                # Unser Callback muss nichts Besonderes tun. Du kannst entweder eine leere
                # Python-Funktion erstellen, oder sync() ohne Argument verwenden.
                #
                # Jetzt jedes Mal, wenn du auf den Button klickst, wird der onClick-Callback ausgelöst. Aber jeder andere
                # Lazy-Callback, der sich in der Zwischenzeit geändert hat, wird ebenfalls aufgerufen.

                mui.Button("Apply changes", onClick=sync())

        # Zweite Karte, das Nivo Bump Chart.
        # Wir werden die gleiche Flexbox-Konfiguration wie bei der ersten Karte verwenden, um die Höhe des Inhalts automatisch anzupassen.

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # Um diese Überschrift ziehbar zu machen, müssen wir nur ihren Klassennamen auf 'draggable' setzen,
            # wie oben in draggableHandle (Argument von dashboard.Grid) definiert.

            mui.CardHeader(title="Chart", className="draggable")

            # Like above, we want to make our content grow and shrink as the user resizes the card,
            # by setting flex to 1 and minHeight to 0.

            # Wie oben wollen wir unseren Inhalt vergrößern und verkleinern lassen, wenn der Benutzer die Größe der Karte ändert.
            # Dies wird durch die Setzung von flex auf 1 und minHeight auf 0 erreicht.

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Hier werden wir unser Bump-Diagramm zeichnen.
                #
                # Für diese Übung können wir einfach das Beispiel von Nivo anpassen und es mit Streamlit Elements verwenden.
                # Das Beispiel von Nivo ist auf dem Tab 'code' verfügbar: https://nivo.rocks/bump/
                #
                # Data nimmt ein Dictionary als Parameter, also müssen wir unsere JSON-Daten von einem String in
                # ein Python-dictionary umwandeln, mit `json.loads()`.
                #
                # Für weitere Informationen über andere verfügbare Nivo-Diagramme:
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

        # Drittes Element des Dashboards: der Media-Player.

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # Dieses Element wird von ReactPlayer angetrieben, es unterstützt viele weitere Player
                # als YouTube. Sie können es dort ausprobieren: https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)

```

## Weitere Fragen?

Man kann alle Fragen zu Streamlit Elements oder zu dieser Herausforderung dort stellen: [Streamlit Elements Thema](https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616)