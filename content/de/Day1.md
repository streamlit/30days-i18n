# Aufsetzen einer lokalen Entwicklungsumgebung

Bevor wir damit beginnen können, Streamlit Apps zu bauen, müssen wir zuerst eine Entwicklungsumgebung aufsetzen.

Lass uns damit starten, eine Condaumgebung zu installieren und zu erstellen.

## **Installiere Conda**
- Installiere `conda` indem du auf https://docs.conda.io/en/latest/miniconda.html gehst und dein Betriebssystem auswählst (Windows, Mac oder Linux).
- Lade und führe die Installationsroutine aus, um `conda` zu installieren.

## **Erstelle eine neue Condaumgebung**
Nun da du Conda installiert hast, lass uns eine Condaumgebung erstellen, um alle Python
Bibliotheksabhängigkeiten zu installieren.

Um eine neue Python 3.9 Umgebzung zu erstellen, führe folgenden Befehl aus:
```bash
conda create -n stenv python=3.9
```

wobei die Condaumgebung durch `create -n stenv` den Namen `stenv` bekommt und durch `python=3.9` Python 3.9 verwendet.

## **Aktiviere die neue Condaumgebung**

Um eine Condaumgebung zu verwenden, die wir mit dem Namen `stenv` gerade erst erstellt haben, führe den folgenden Befehl in der Kommandozeile aus:

```bash
conda activate stenv
```

## **Installiere die Streamlit Bibliothek**
Jetzt ist es an der Zeit, die `streamlit` Bibliothek zu installieren:
```bash
pip install streamlit
```

## **Starte die Streamlit Demoapplikation**
Um die Streamlit Demoapp zu starten (Grafik 1), tippe:
```bash
streamlit hello
```
